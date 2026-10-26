import os
import sys
import json
import base64
import urllib.request
import fitz
import pypdf

sys.path.append(r'd:\GitHub\SOANBAI-main')
from auto_create_exam import load_env

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

env = load_env()
pdf_path = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\bo-de-on-tap-giua-hoc-ki-1-mon-toan-7-nam-2026-2027-theo-cau-truc-moi.pdf'
out_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)

def get_page_b64(page_idx):
    pix = doc[page_idx].get_pixmap(dpi=150)
    return base64.b64encode(pix.tobytes('png')).decode('utf-8')

def call_ai(messages, max_tokens=4000):
    url = f"{env.get('APIVN_BASE_URL').rstrip('/')}/chat/completions"
    payload = {
        'model': env.get('APIVN_MODEL', 'claude-sonnet-5-5'),
        'messages': messages,
        'temperature': 0.1,
        'max_tokens': max_tokens
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
        'Authorization': f"Bearer {env.get('APIVN_API_KEY')}",
        'Content-Type': 'application/json'
    })
    with urllib.request.urlopen(req, timeout=180) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        return res['choices'][0]['message']['content']

def extract_json(text):
    text = text.strip()
    if '```json' in text:
        text = text.split('```json')[1].split('```')[0].strip()
    elif '```' in text:
        text = text.split('```')[1].split('```')[0].strip()
    start = text.find('{')
    end = text.rfind('}')
    if start != -1 and end != -1:
        return json.loads(text[start:end+1])
    return json.loads(text)

# Đọc text lời giải Đề 1 (trang 75 đến 86)
reader = pypdf.PdfReader(pdf_path)
solution_text = ""
for p in range(74, 86):
    solution_text += f"\n--- Trang Lời Giải {p+1} ---\n" + reader.pages[p].extract_text()

print("Đang xử lý Phần I (Trắc nghiệm 12 câu) với ảnh trang 2, 3, 4...")
b64_p2 = get_page_b64(1) # Trang 2
b64_p3 = get_page_b64(2) # Trang 3
b64_p4 = get_page_b64(3) # Trang 4

prompt_p1 = f"""Dưới đây là 3 ảnh trang của Phần I (Câu 1 đến Câu 12) của Đề số 1 Toán 7.
Dưới đây là văn bản phần Lời giải chi tiết tương ứng:
===
{solution_text[:6000]}
===

YÊU CẦU:
Trích xuất toàn bộ 12 câu của Phần I thành một mảng JSON các object theo định dạng:
{{
  "phan_I_trac_nghiem": [
    {{
      "cau": 1,
      "noi_dung": "...",
      "hinh_tikz": null, // hoặc chuỗi mã TikZ nếu câu có hình vẽ
      "lua_chon": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
      "dap_an": "B",
      "loi_giai": "..."
    }},
    ...
  ]
}}

LƯU Ý QUAN TRỌNG VỀ HÌNH VẼ TIKZ:
- Các câu có hình vẽ (như Câu 4: tam giác có tia phân giác, Câu 5: hai đường thẳng song song a//b và góc, Câu 7: trục số biểu diễn điểm A, Câu 10, Câu 11: các hình lăng trụ/hình học không gian): BẮT BUỘC viết mã TikZ hoàn chỉnh, đẹp, gọn gàng, tự bao hàm trong \\begin{{tikzpicture}} ... \\end{{tikzpicture}}. Không dùng gói lạ, dùng tikz thuần (các thư viện calc, angles, quotes, arrows.meta).
- Với Câu 10 và Câu 11: nếu vẽ 4 hình A, B, C, D thì có thể vẽ 4 sub-pictures hoặc 1 cụm tikzplayer có 4 hình với nhãn Hình 1, Hình 2, Hình 3, Hình 4 rõ ràng.
- Giữ nguyên công thức toán bằng cú pháp LaTeX chuẩn (chú ý escape dấu gạch chéo \\\\ trong JSON).
- Chỉ trả về duy nhất khối JSON chuẩn.
"""

msg_p1 = [
    {
        'role': 'user',
        'content': [
            {'type': 'text', 'text': prompt_p1},
            {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{b64_p2}'}},
            {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{b64_p3}'}},
            {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{b64_p4}'}}
        ]
    }
]

res_p1_text = call_ai(msg_p1, max_tokens=4000)
data_p1 = extract_json(res_p1_text)
print("-> Đã trích xuất xong Phần I!")

print("Đang xử lý Phần II, III, IV với ảnh trang 5, 6...")
b64_p5 = get_page_b64(4) # Trang 5
b64_p6 = get_page_b64(5) # Trang 6

prompt_p2 = f"""Dưới đây là 2 ảnh trang của Phần II (Đúng sai), Phần III (Trả lời ngắn), Phần IV (Tự luận) của Đề số 1 Toán 7.
Dưới đây là văn bản phần Lời giải chi tiết tương ứng:
===
{solution_text[5000:]}
===

YÊU CẦU:
Trích xuất toàn bộ Phần II, Phần III, Phần IV thành JSON theo định dạng sau:
{{
  "phan_II_dung_sai": [
    {{
      "cau": 1,
      "noi_dung": "Cho các số: ... Xét tính đúng sai của các mệnh đề sau:",
      "hinh_tikz": null,
      "menh_de": [
        {{"y": "a", "noi_dung": "...", "dap_an": "Đúng", "loi_giai": "..."}},
        {{"y": "b", "noi_dung": "...", "dap_an": "Sai", "loi_giai": "..."}},
        {{"y": "c", "noi_dung": "...", "dap_an": "Sai", "loi_giai": "..."}},
        {{"y": "d", "noi_dung": "...", "dap_an": "Đúng", "loi_giai": "..."}}
      ]
    }},
    {{
      "cau": 2,
      "noi_dung": "Cho hình vẽ, biết đường thẳng a vuông góc với CD...",
      "hinh_tikz": "\\\\begin{{tikzpicture}} ... \\\\end{{tikzpicture}}", // BẮT BUỘC VẼ TIKZ CHO HÌNH CÂU 2
      "menh_de": [
        {{"y": "a", "noi_dung": "...", "dap_an": "Đúng", "loi_giai": "..."}},
        {{"y": "b", "noi_dung": "...", "dap_an": "Đúng", "loi_giai": "..."}},
        {{"y": "c", "noi_dung": "...", "dap_an": "Đúng", "loi_giai": "..."}},
        {{"y": "d", "noi_dung": "...", "dap_an": "Sai", "loi_giai": "..."}}
      ]
    }}
  ],
  "phan_III_tra_loi_ngan": [
    {{
      "cau": 1,
      "noi_dung": "...",
      "hinh_tikz": null,
      "dap_an": "35^\\circ",
      "loi_giai": "..."
    }},
    {{
      "cau": 2,
      "noi_dung": "...",
      "hinh_tikz": null,
      "dap_an": "-0.5",
      "loi_giai": "..."
    }}
  ],
  "phan_IV_tu_luan": [
    {{
      "cau": 1,
      "noi_dung": "Tính hợp lí",
      "hinh_tikz": null,
      "cac_y": [
        {{"y": "a", "bieu_thuc": "...", "loi_giai": "..."}},
        {{"y": "b", "bieu_thuc": "...", "loi_giai": "..."}}
      ]
    }},
    {{
      "cau": 2,
      "noi_dung": "Tìm x, biết:",
      "hinh_tikz": null,
      "cac_y": [
        {{"y": "a", "bieu_thuc": "...", "loi_giai": "..."}},
        {{"y": "b", "bieu_thuc": "...", "loi_giai": "..."}},
        {{"y": "c", "bieu_thuc": "...", "loi_giai": "..."}}
      ]
    }},
    {{
      "cau": 3,
      "noi_dung": "Cho hình vẽ, biết a vuông góc AB, b vuông góc AB, góc C = 100°...",
      "hinh_tikz": "\\\\begin{{tikzpicture}} ... \\\\end{{tikzpicture}}", // BẮT BUỘC VẼ TIKZ CHO HÌNH CÂU 3
      "cac_y": [
        {{"y": "a", "cau_hoi": "Chứng tỏ a // b", "loi_giai": "..."}},
        {{"y": "b", "cau_hoi": "Tính góc D1?", "loi_giai": "..."}}
      ]
    }},
    {{
      "cau": 4,
      "noi_dung": "Tính các góc của tam giác ABC biết: góc A/3 = góc B/4 = góc C/2",
      "hinh_tikz": null,
      "loi_giai": "..."
    }}
  ]
}}

LƯU Ý VỀ TIKZ:
- Câu 2 Phần II và Câu 3 Phần IV có hình vẽ hình học phẳng rất rõ ràng trong ảnh. Hãy vẽ TikZ chi tiết, chính xác góc, ký hiệu vuông góc, tên các điểm A, B, C, D, đường thẳng a, b.
- Thoát dấu gạch chéo \\\\ hợp lệ trong JSON.
- Chỉ trả về duy nhất chuỗi JSON chuẩn.
"""

msg_p2 = [
    {
        'role': 'user',
        'content': [
            {'type': 'text', 'text': prompt_p2},
            {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{b64_p5}'}},
            {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{b64_p6}'}}
        ]
    }
]

res_p2_text = call_ai(msg_p2, max_tokens=4000)
data_p2 = extract_json(res_p2_text)
print("-> Đã trích xuất xong Phần II, III, IV!")

# Gộp thành de_01.json hoàn chỉnh
full_data = {
    "de_so": 1,
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I 2026 – 2027",
    "mon": "Toán 7",
    "thoi_gian": "90 phút",
    "phan_I_trac_nghiem": data_p1.get("phan_I_trac_nghiem", []),
    "phan_II_dung_sai": data_p2.get("phan_II_dung_sai", []),
    "phan_III_tra_loi_ngan": data_p2.get("phan_III_tra_loi_ngan", []),
    "phan_IV_tu_luan": data_p2.get("phan_IV_tu_luan", [])
}

json_file = os.path.join(out_dir, "de_01.json")
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(full_data, f, ensure_ascii=False, indent=2)

print(f"==================================================")
print(f"XUẤT SẮC! ĐÃ LƯU FILE JSON HOÀN CHỈNH: {json_file}")
print(f"==================================================")
