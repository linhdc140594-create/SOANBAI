import os
import sys
import json
import urllib.request
import re

# Đảm bảo in tiếng Việt không bị lỗi font trên Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from exam_engine import build_exam_pdf

def load_env(env_path=None):
    if not env_path:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        env_path = os.path.join(root_dir, '.env')
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env_vars[k.strip()] = v.strip()
    return env_vars

def call_ai_api(prompt, system_prompt="You are an expert Math teacher and LaTeX exam generator.", model=None, env=None):
    if env is None:
        env = load_env()
    api_key = env.get('APIVN_API_KEY')
    base_url = env.get('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/')
    if not model:
        model = env.get('APIVN_MODEL', 'claude-sonnet-5-5')

    url = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    data_bytes = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data_bytes, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    })
    
    with urllib.request.urlopen(req, timeout=60) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        return res['choices'][0]['message']['content']

def extract_json_from_text(text):
    text = text.strip()
    if '```json' in text:
        match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
    if '```' in text:
        match = re.search(r'```\s*(\{.*?\})\s*```', text, re.DOTALL)
        if match:
            return json.loads(match.group(1))
    # Tim cap ngoac {} ngoai cung
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1:
        return json.loads(text[start:end+1])
    return json.loads(text)

def generate_exam_from_plan(plan_file_path):
    plan_file_path = os.path.abspath(plan_file_path)
    if not os.path.exists(plan_file_path):
        print(f"Lỗi: Không tìm thấy file kế hoạch: {plan_file_path}")
        return False

    work_dir = os.path.dirname(plan_file_path)
    print(f"==================================================")
    print(f"BẮT ĐẦU TẠO ĐỀ TỰ ĐỘNG CHO: {plan_file_path}")
    print(f"Thư mục làm việc: {work_dir}")
    print(f"==================================================")

    with open(plan_file_path, 'r', encoding='utf-8') as f:
        plan_content = f.read()

    env = load_env()
    model = env.get('APIVN_MODEL', 'claude-sonnet-5-5')
    print(f"-> Đang kết nối API ({model}) để trích xuất cấu trúc 4 mã đề sang JSON...")

    prompt_extract = f"""Dưới đây là kế hoạch nội dung và ma trận đề kiểm tra:
---
{plan_content}
---

Hãy trích xuất và chuẩn hóa nội dung của CẢ 4 MÃ ĐỀ (101, 102, 103, 104) thành DUY NHẤT một đối tượng JSON chuẩn theo đúng định dạng sau. 
CHÚ Ý:
- LaTeX phải dùng dấu gạch chéo kép nếu cần (ví dụ \\frac{{...}}{{...}}).
- Trả về JSON thuần túy, không thêm lời chào hay giải thích ngoài khối JSON.

{{
  "title_p1": "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN ... - TUẦN ... - BUỔI ...",
  "title_p2": "TOÁN ... - TUẦN ... - BUỔI ...",
  "base_filename": "Phieu_Kiem_Tra_Tuan_..._Buoi_...",
  "codes": {{
    "101": {{
      "short": [
        ["Đề câu 1...", "Đáp án 1"],
        ["Đề câu 2...", "Đáp án 2"],
        ... (đủ 10 câu trả lời ngắn)
      ],
      "q11": {{
        "a": "Biểu thức phép tính ý a",
        "b": "Biểu thức phép tính ý b",
        "c": "Biểu thức phép tính ý c",
        "d": "Biểu thức phép tính ý d"
      }},
      "q12": {{
        "a": "Phương trình ý a",
        "b": "Phương trình ý b",
        "c": "Phương trình ý c",
        "d": "Phương trình ý d"
      }},
      "q13": {{
        "de": "Nội dung bài toán hình học / thực tế...",
        "a": "Nội dung câu hỏi a...",
        "b": "Nội dung câu hỏi b..."
      }},
      "q14": {{
        "de": "Nội dung câu 14 nâng cao..."
      }}
    }},
    "102": {{ ... tương tự cho mã đề 102 ... }},
    "103": {{ ... tương tự cho mã đề 103 ... }},
    "104": {{ ... tương tự cho mã đề 104 ... }}
  }}
}}
"""

    response_text = call_ai_api(prompt_extract, model=model, env=env)
    
    try:
        data = extract_json_from_text(response_text)
    except Exception as e:
        print(f"Lỗi phân tích JSON từ AI: {e}")
        debug_path = os.path.join(work_dir, "ai_response_debug.txt")
        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(response_text)
        print(f"Đã lưu phản hồi AI vào: {debug_path}")
        return False

    json_path = os.path.join(work_dir, "data_de.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"-> Đã trích xuất xong dữ liệu JSON: {json_path}")

    # Tiến hành biên dịch LaTeX bằng exam_engine
    title_p1 = data.get("title_p1", "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN")
    title_p2 = data.get("title_p2", "PHIẾU KIỂM TRA")
    base_filename = data.get("base_filename", "Phieu_Kiem_Tra")
    codes_data = data.get("codes", {})

    print(f"-> Đang dựng mã nguồn LaTeX & biên dịch PDF 8 trang chuẩn...")
    success, msg = build_exam_pdf(codes_data, title_p1, title_p2, work_dir, base_filename=base_filename)
    print(f"-> Kết quả biên dịch: {msg}")

    # Sinh đáp án chi tiết nếu cần
    ans_file = os.path.join(work_dir, "DAP_AN_VA_THANG_DIEM.md")
    if not os.path.exists(ans_file) or os.path.getsize(ans_file) < 100:
        print(f"-> Đang tự động sinh file Đáp án & Barem điểm ({ans_file})...")
        prompt_ans = f"""Dưới đây là kế hoạch và dữ liệu đề kiểm tra của 4 mã đề:
---
{plan_content}
---

Hãy viết file DAP_AN_VA_THANG_DIEM.md hoàn chỉnh theo chuẩn AGENTS.md:
1. Bảng đáp án ngắn gọn 10 câu trả lời ngắn cho CẢ 4 MÃ ĐỀ (101, 102, 103, 104).
2. Lời giải chi tiết từng bước cho Câu 11, Câu 12, Câu 13, Câu 14 của cả 4 mã đề kèm thang điểm chi tiết đến 0,25 điểm.
"""
        ans_content = call_ai_api(prompt_ans, model=model, env=env)
        with open(ans_file, 'w', encoding='utf-8') as f:
            f.write(ans_content)
        print(f"-> Đã tạo xong file Đáp án: {ans_file}")

    print("==================================================")
    print("HOÀN TẤT THÀNH CÔNG QUY TRÌNH!")
    print("==================================================")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        plan_path = sys.argv[1]
    else:
        # Mac dinh thu nghiem voi file LOP7 Tuan 7 Buoi 1
        plan_path = os.path.join(os.path.dirname(__file__), "LOP7", "1_GHK_1", "TUAN_7", "buoi_1", "KE_HOACH_TUAN_07_BUOI_01.md")
    
    generate_exam_from_plan(plan_path)
