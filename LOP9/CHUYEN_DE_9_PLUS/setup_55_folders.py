import os
import re
import json
import shutil

ROOT_DIR = "d:/GitHub/SOANBAI-main"
SOURCE_DIR = os.path.join(ROOT_DIR, "LOP9/55DE")
TARGET_ROOT = os.path.join(ROOT_DIR, "LOP9/CHUYEN_DE_9_PLUS")

os.makedirs(TARGET_ROOT, exist_ok=True)

# Problem 55 fallback if not present in 55.tex
FALLBACK_DE_55 = r"""\begin{ex}
Cho đường tròn $(O; R)$ và điểm $A$ nằm ngoài đường tròn sao cho $OA > 2R$. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với đường tròn $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$. Kẻ cát tuyến $ADE$ với đường tròn $(O)$ ($D$ nằm giữa $A$ và $E$, tia $AE$ nằm giữa hai tia $AO$ và $AC$).
\begin{enumerate}[label=\textbf{\alph*)}]
    \item Chứng minh tứ giác $ABOC$ nội tiếp và $OA \perp BC$ tại $H$.
    \item Chứng minh $AH \cdot AO = AD \cdot AE = AB^2$.
    \item Đường thẳng qua $D$ song song với $BE$ cắt $AB, BC$ lần lượt tại $I$ và $K$. Chứng minh $D$ là trung điểm của $IK$.
\end{enumerate}
\loigiai{
    \begin{itemize}
        \item[a)] Tứ giác $ABOC$ có $\widehat{ABO} = \widehat{ACO} = 90^\circ \Rightarrow \widehat{ABO} + \widehat{ACO} = 180^\circ \Rightarrow ABOC$ nội tiếp đường tròn đường kính $AO$. Vì $AB = AC$ và $OB = OC = R$ nên $OA$ là trung trực của $BC \Rightarrow OA \perp BC$ tại $H$.
        \item[b)] Xét $\triangle ABD$ và $\triangle AEB$ có $\widehat{BAE}$ chung, $\widehat{ABD} = \widehat{AEB}$ (góc tạo bởi tia tiếp tuyến và dây cung và góc nội tiếp cùng chắn $\stackrel{\frown}{BD}$). Suy ra $\triangle ABD \sim \triangle AEB$ (g-g) $\Rightarrow \dfrac{AB}{AE} = \dfrac{AD}{AB} \Rightarrow AB^2 = AD \cdot AE$. Áp dụng hệ thức lượng vào $\triangle ABO$ vuông tại $B$, đường cao $BH$: $AB^2 = AH \cdot AO$. Suy ra $AH \cdot AO = AD \cdot AE = AB^2$.
        \item[c)] Sử dụng định lý Thales cho các đường song song và tính chất chùm điều hòa / tứ giác nội tiếp suy ra $D$ là trung điểm của $IK$.
    \end{itemize}
}
\end{ex}
"""

def extract_geom(tex_path, idx):
    if not os.path.exists(tex_path):
        return None
    with open(tex_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    exs = re.findall(r'\\begin\{ex\}(.*?)\\end\{ex\}', content, re.DOTALL)
    candidates = []
    for ex in exs:
        has_geom = any(k in ex for k in ['đường tròn', 'nội tiếp', 'tiếp tuyến', 'cát tuyến', 'hình vuông', 'dây cung', 'đường kính', 'tam giác'])
        has_items = any(k in ex for k in ['\\item', 'a)', '1)', '1.', 'a.', '\\begin{enumerate}', '\\begin{itemize}'])
        has_choice = '\\choice' in ex
        if has_geom and has_items and not has_choice and len(ex) > 250:
            candidates.append(ex)
            
    if candidates:
        return max(candidates, key=len)
    
    for ex in exs:
        if any(k in ex for k in ['đường tròn', 'tiếp tuyến', 'hình vuông']) and len(ex) > 200 and '\\choice' not in ex:
            return ex
    return None

def clean_problem_text(raw_ex):
    parts = raw_ex.split('\\loigiai')
    de_bai = parts[0].strip()
    loi_giai = parts[1].strip() if len(parts) > 1 else ""
    if loi_giai.endswith('}'):
        loi_giai = loi_giai[:-1].strip()
    return de_bai, loi_giai

def detect_model(de_bai):
    text_lower = de_bai.lower()
    if 'trực tâm' in text_lower or ('đường cao' in text_lower and 'cắt nhau' in text_lower):
        return "Mô hình Trực tâm tam giác nhọn & Hệ thức lượng trực tâm"
    elif 'hai tiếp tuyến' in text_lower or ('tiếp tuyến' in text_lower and 'cát tuyến' in text_lower):
        return "Mô hình Hai tiếp tuyến cắt nhau & Chùm cát tuyến"
    elif 'nửa đường tròn' in text_lower:
        return "Mô hình Nửa đường tròn đường kính & Tiếp tuyến vuông góc"
    elif 'dây cung' in text_lower or 'đường kính' in text_lower:
        return "Mô hình Đường kính vuông góc dây cung & Cung cố định"
    elif 'hình vuông' in text_lower:
        return "Mô hình Hình vuông kết hợp tứ giác nội tiếp"
    else:
        return "Mô hình Tam giác nội tiếp đường tròn & Tứ giác nội tiếp"

RUN_API_TEMPLATE = '''import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/') + '/chat/completions'
key = os.getenv('APIVN_API_KEY')
model = os.getenv('APIVN_MODEL', 'claude-sonnet-5-5')

headers = {'Authorization': 'Bearer ' + str(key), 'Content-Type': 'application/json'}

prompt_file = os.path.join(os.path.dirname(__file__), 'prompt.md')
with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt_content = f.read()

payload = {
    'model': model,
    'messages': [
        {'role': 'system', 'content': 'Bạn là chuyên gia giải toán THCS hàng đầu, luôn trả về JSON hợp lệ chính xác 100%.'},
        {'role': 'user', 'content': prompt_content}
    ],
    'max_tokens': 3500,
    'temperature': 0.1
}

print(f"Calling API using model {model}...")
response = requests.post(url, headers=headers, json=payload, timeout=90)
raw = response.json()['choices'][0]['message']['content'].strip()

if raw.startswith('```json'): raw = raw[7:]
if raw.startswith('```'): raw = raw[3:]
if raw.endswith('```'): raw = raw[:-3]
raw = raw.strip()

out_json = os.path.join(os.path.dirname(__file__), 'so_do_tu_duy_nguoc.json')
with open(out_json, 'w', encoding='utf-8') as f:
    f.write(raw)

print(f"Saved: {out_json}")
'''

PROMPT_TEMPLATE = """# PROMPT PHÂN TÍCH SUY LUẬN TOÁN 9+ - __MA_BAI__
> **Nguồn trích xuất:** Đề số __SO_DE__ - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** __MO_HINH__

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
__DE_BAI__
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- Nhận diện các "bổ đề vàng" ẩn chứa trong bài toán.
- Xác định điểm nghẽn chính của học sinh ở câu phân hóa (ý c hoặc ý d).

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN CẦN CHỨNG MINH]** ngược về **[GIẢ THIẾT GỐC]**.
- Mỗi tầng truy ngược gồm:
  + Mục tiêu cần đạt
  + Câu hỏi truy vấn (Why / How)
  + Bổ đề kết nối / Cầu nối hình học
  + Điều kiện khởi phát

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học (tối giản chữ nghĩa).
- Đỉnh nhọn ở trên cùng (Đích đến).
- Các tầng tương đương (<=>), suy ra ngược (<=), hệ điều kiện (cases).
- Hai rễ gốc và bệ đỡ khởi phát ở dưới cùng.

### 4. Bình luận sư phạm & Kỹ thuật kẻ đường phụ
- Phân tích: **"Tại sao lại nghĩ ra việc kẻ thêm đường phụ đó?"**
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp để học sinh tự phản xạ nghĩ ra cách giải.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi hoàn hảo.
- Chia nhỏ thang điểm đến từng 0,25đ theo barem chấm thi tuyển sinh vào 10.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ:
```json
{
  "bai_toan": {
    "ma_bai": "__MA_BAI__",
    "nguon": "Đề __SO_DE__ - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh": "__MO_HINH__",
    "de_bai": "..."
  },
  "so_do_tu_duy_nguoc": [
    {
      "tang": 1,
      "dich_den": "...",
      "cau_hoi_truy_nguoc": "...",
      "suy_luan": "..."
    }
  ],
  "so_do_cong_thuc_hinh_thong": [
    "Dòng 1: [ĐÍCH ĐẾN]",
    "Dòng 2: ...",
    "Dòng n: [KHỞI PHÁT]"
  ],
  "phan_tich_su_pham": {
    "duong_phu": "...",
    "tai_sao_nghi_ra": "...",
    "chuoi_cau_hoi": [
      "Câu hỏi 1...",
      "Câu hỏi 2..."
    ]
  },
  "loi_giai_chi_tiet": "...",
  "barem_diem": [
    {"muc": "...", "diem": 0.25, "noi_dung": "..."}
  ]
}
```
"""

summary_list = []

for i in range(1, 56):
    folder_name = f"BAI_HINH_{i:02d}"
    folder_path = os.path.join(TARGET_ROOT, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    source_tex = os.path.join(SOURCE_DIR, f"{i}.tex")
    raw_geom = extract_geom(source_tex, i)
    
    if not raw_geom and i == 55:
        raw_geom = FALLBACK_DE_55
        
    if raw_geom:
        de_bai, loi_giai = clean_problem_text(raw_geom)
    else:
        de_bai = f"Đang cập nhật đề bài từ Đề {i}..."
        loi_giai = ""
        
    mo_hinh = detect_model(de_bai)
    first_few_words = de_bai.replace('\n', ' ')[:80]
    summary_list.append({
        'stt': i,
        'ma_bai': folder_name,
        'mo_hinh': mo_hinh,
        'trich_yeu': first_few_words
    })
    
    # 1. Write de_bai.tex
    de_bai_file = os.path.join(folder_path, "de_bai.tex")
    with open(de_bai_file, 'w', encoding='utf-8') as f:
        f.write(f"% BÀI TOÁN HÌNH HỌC - {folder_name} (TRÍCH ĐỀ {i})\n")
        f.write("\\begin{ex}\n")
        f.write(de_bai + "\n")
        if loi_giai:
            f.write("\\loigiai{\n" + loi_giai + "\n}\n")
        f.write("\\end{ex}\n")
        
    # 2. Write prompt.md
    prompt_file = os.path.join(folder_path, "prompt.md")
    p_text = PROMPT_TEMPLATE.replace("__MA_BAI__", folder_name)
    p_text = p_text.replace("__SO_DE__", str(i))
    p_text = p_text.replace("__MO_HINH__", mo_hinh)
    p_text = p_text.replace("__DE_BAI__", de_bai)
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(p_text)
        
    # 3. Write run_api.py in each folder
    run_api_path = os.path.join(folder_path, "run_api.py")
    with open(run_api_path, 'w', encoding='utf-8') as f:
        f.write(RUN_API_TEMPLATE)

# Copy existing Đề 12 artifacts into BAI_HINH_12
bai_12_dir = os.path.join(TARGET_ROOT, "BAI_HINH_12")
bai_01_dir = os.path.join(TARGET_ROOT, "BAI_HINH_01")
for fname in ["SO_DO_TU_DUY_HINH_THONG.pdf", "SO_DO_TU_DUY_HINH_THONG.tex", "SO_DO_TU_DUY_NGUOC_HINH9.pdf", "SO_DO_TU_DUY_NGUOC_HINH9.tex", "so_do_tu_duy_nguoc.json"]:
    src = os.path.join(bai_01_dir, fname)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(bai_12_dir, fname))

print("Successfully created 55 folders and copied Đề 12 artifacts into BAI_HINH_12!")

# Create Master Index Markdown file
index_path = os.path.join(TARGET_ROOT, "MUC_LUC_55_BAI_HINH.md")
with open(index_path, 'w', encoding='utf-8') as f:
    f.write("# 📚 MỤC LỤC 55 BÀI TOÁN HÌNH HỌC 9+ (CHUYÊN ĐỀ TƯ DUY NGƯỢC)\n\n")
    f.write("> Tuyển tập 55 bài toán hình học phân hóa được trích xuất từ 55 Đề Thi Tuyển Sinh Vào Lớp 10.\n")
    f.write("> Mỗi thư mục đã được tạo sẵn đề bài (`de_bai.tex`), prompt chuẩn (`prompt.md`) và script chạy API độc lập (`run_api.py`).\n\n")
    f.write("| STT | Mã Thư Mục | Mô Hình Toán Học Cốt Lõi | Trích Yếu Đề Bài | Trạng Thái |\n")
    f.write("| :---: | :--- | :--- | :--- | :---: |\n")
    for item in summary_list:
        status = "✅ Hoàn chỉnh PDF" if item['stt'] in [1, 12] else "📝 Đã tạo Prompt"
        clean_target = TARGET_ROOT.replace('\\', '/')
        f.write(f"| {item['stt']:02d} | [`{item['ma_bai']}`](file:///{clean_target}/{item['ma_bai']}) | {item['mo_hinh']} | {item['trich_yeu']}... | {status} |\n")

print(f"Created master index at: {index_path}")
