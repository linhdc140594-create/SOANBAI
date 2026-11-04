import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/') + '/chat/completions'
key = os.getenv('APIVN_API_KEY')
model = os.getenv('APIVN_MODEL', 'claude-sonnet-5-5')

headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}

de_bai = """
Cho tam giác ABC có ba góc nhọn nội tiếp đường tròn (O; R). Các đường cao AD, BF, CE của tam giác ABC cắt nhau tại H.
a) Chứng minh tứ giác BEHD nội tiếp một đường tròn.
b) Kéo dài AD cắt đường tròn (O) tại điểm thứ hai K. Kéo dài KE cắt đường tròn (O) tại điểm thứ hai I. Kẻ OM vuông góc với BC tại M. Gọi P là tâm đường tròn ngoại tiếp tam giác AEF. Gọi N là giao điểm của CI và EF.
   1) Chứng minh CE^2 = CN . CI.
   2) Chứng minh ba điểm M, N, P thẳng hàng.
"""

prompt = f"""Bạn là một chuyên gia bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào 10 chuyên Toán.
Dưới đây là một bài toán hình học 9+ xuất sắc trích từ Đề 12 - Tuyển tập 55 Đề Thi Vào Lớp 10:
{de_bai}

Hãy phân tích và giải mã bài toán này theo phương pháp SƠ ĐỒ TƯ DUY NGƯỢC (Reverse Thinking) để dạy học sinh tư duy bẻ khóa ý phân hóa khó nhất: "Chứng minh ba điểm M, N, P thẳng hàng".

Hãy trả về DUY NHẤT một chuỗi JSON hợp lệ (không có bất kỳ văn bản nào khác ngoài JSON, không markdown râu ria) theo cấu trúc sau:
{{
  "bai_toan": {{
    "ten_bai": "Hình học 9+ Đề 12 - Tuyển tập 55 Đề Tuyển Sinh Vào 10",
    "mo_hinh": "Trực tâm tam giác nhọn, đường trung trực của đoạn thẳng Euler và hệ thức lượng phương tích",
    "gia_thiet": "Tam giác ABC nhọn nội tiếp (O; R), đường cao AD, BF, CE cắt nhau tại H. AD cắt (O) tại K, KE cắt (O) tại I. OM vuông góc BC tại M. P là tâm ngoại tiếp tam giác AEF. N là giao của CI và EF.",
    "ket_luan_chinh": "1) CE^2 = CN . CI; 2) Ba điểm M, N, P thẳng hàng."
  }},
  "so_do_tu_duy_nguoc": [
    {{
      "tang": 1,
      "dich_den": "M, N, P thẳng hàng",
      "nhan_xet_cot_loi": "M và P đều thuộc đường trung trực của EF (do ME = MF = BC/2 và PE = PF). Do đó đường thẳng PM chính là đường trung trực của EF.",
      "cau_hoi_truy_nguoc": "Muốn M, N, P thẳng hàng thì điểm N phải nằm ở đâu đối với đường thẳng PM?",
      "muc_tieu_con": "Chứng minh N thuộc đường trung trực của EF (tức NE = NF, hay N là trung điểm của EF)."
    }},
    {{
      "tang": 2,
      "dich_den": "N là trung điểm của EF (NE = NF)",
      "cau_hoi_truy_nguoc": "EF là đoạn thẳng lơ lửng, làm thế nào để chứng minh N là trung điểm của nó?",
      "vu_khi_duong_phu": "Kẻ EG vuông góc với AC tại G. Khi đó tam giác EGF vuông tại G có cạnh huyền là EF. Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền. Do đó N là trung điểm EF khi và chỉ khi NG = NE = NF, tương đương tam giác NGF cân tại N (góc NGF = góc NFG).",
      "muc_tieu_con": "Chứng minh góc NGF = góc NFG"
    }},
    {{
      "tang": 3,
      "dich_den": "góc NGF = góc NFG",
      "cau_hoi_truy_nguoc": "Góc NFG liên hệ gì với các góc của tam giác ABC và đường tròn (O)?",
      "suy_luan": "Tứ giác BEFC nội tiếp nên góc NFG = góc AFE = góc ABC. Trong đường tròn (O), góc ABC = góc AIC (hai góc nội tiếp cùng chắn cung AC). Do đó, cần chứng minh góc NGF = góc AIC.",
      "muc_tieu_con": "Chứng minh góc NGF = góc AIC"
    }},
    {{
      "tang": 4,
      "dich_den": "góc NGF = góc AIC",
      "cau_hoi_truy_nguoc": "Làm thế nào để chuyển mối quan hệ hai góc này về tam giác đồng dạng?",
      "suy_luan": "Xét tam giác CNG và tam giác CAI có góc C chung. Hai tam giác này đồng dạng theo trường hợp c-g-c khi và chỉ khi CG/CN = CI/CA, tương đương tích CG . CA = CN . CI.",
      "muc_tieu_con": "Chứng minh tích CG . CA = CN . CI"
    }},
    {{
      "tang": 5,
      "dich_den": "CG . CA = CN . CI (ĐIỂM KHỞI PHÁT HOÀN HẢO)",
      "cau_hoi_truy_nguoc": "Tại sao CG . CA lại bằng CN . CI?",
      "suy_luan": "Thứ nhất: Hệ thức lượng trong tam giác AEC vuông tại E, đường cao EG cho ta CG . CA = CE^2. Thứ hai: Câu b1 đã chứng minh CE^2 = CN . CI. Do đó CG . CA = CN . CI = CE^2! Đây chính là mắt xích liên kết giữa câu b1 và câu b2, là điểm khởi đầu để trình bày lời giải xuôi."
    }}
  ],
  "nghe_thuat_su_pham": {{
    "tai_sao_nghi_ra_duong_phu": "Tại sao lại kẻ EG vuông góc AC mà không phải đường khác? Vì điểm E đã có sẵn góc AEC = 90 độ, hạ vuông góc xuống AC vừa tạo ra tam giác vuông EGF nhận EF làm cạnh huyền, vừa kích hoạt ngay hệ thức lượng CE^2 = CG . CA để ghép nối với giả thiết CE^2 = CN . CI của câu trước.",
    "chuoi_cau_hoi_dan_dat": [
      "Câu hỏi 1: Điểm M và điểm P có vai trò đối xứng gì đối với đoạn thẳng EF?",
      "Câu hỏi 2: Vậy muốn M, N, P thẳng hàng, điểm N bắt buộc phải có tính chất gì trên đoạn thẳng EF?",
      "Câu hỏi 3: Đoạn thẳng EF đang lơ lửng, muốn chứng minh trung điểm ta nên gắn nó vào loại hình học nào?",
      "Câu hỏi 4: Ta đã chứng minh CE^2 = CN . CI ở câu trước, làm sao tạo ra một tích đoạn thẳng mới bằng CE^2?"
    ]
  }},
  "barem_diem": [
    {{"muc": "Câu a", "diem": 0.75, "noi_dung": "Chứng minh tứ giác BEHD nội tiếp đường tròn đường kính BH"}},
    {{"muc": "Câu b1", "diem": 0.75, "noi_dung": "Chứng minh CE^2 = CN . CI qua hai tam giác đồng dạng CEN và CIE"}},
    {{"muc": "Câu b2 - Ý 1", "diem": 0.25, "noi_dung": "Chứng minh PM là đường trung trực của đoạn thẳng EF"}},
    {{"muc": "Câu b2 - Ý 2", "diem": 0.25, "noi_dung": "Kẻ đường phụ EG vuông góc AC, chứng minh tam giác CNG đồng dạng tam giác CAI"}},
    {{"muc": "Câu b2 - Ý 3", "diem": 0.25, "noi_dung": "Chứng minh tam giác NGF cân tại N, suy ra N là trung điểm của EF"}},
    {{"muc": "Câu b2 - Ý 4", "diem": 0.25, "noi_dung": "Từ PM là trung trực EF và N là trung điểm EF suy ra M, N, P thẳng hàng"}}
  ]
}}
"""

data = {
    'model': model,
    'messages': [
        {'role': 'system', 'content': 'Bạn là một chuyên gia giải toán THCS và lập trình viên xuất sắc, luôn trả về JSON hợp lệ chính xác 100%.'},
        {'role': 'user', 'content': prompt}
    ],
    'max_tokens': 3500,
    'temperature': 0.1
}

print(f"Calling API with model {model}...")
response = requests.post(url, headers=headers, json=data, timeout=60)
print(f"Status code: {response.status_code}")
content = response.json()['choices'][0]['message']['content'].strip()

if content.startswith('```json'):
    content = content[7:]
if content.startswith('```'):
    content = content[3:]
if content.endswith('```'):
    content = content[:-3]
content = content.strip()

out_json = 'LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_01/so_do_tu_duy_nguoc.json'
with open(out_json, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Saved JSON to: {out_json}")

# Parse test
try:
    d = json.loads(content)
    print("SUCCESS: JSON is 100% valid!")
    print("Keys:", list(d.keys()))
    print("Number of reverse mindmap levels:", len(d.get('so_do_tu_duy_nguoc', [])))
except Exception as e:
    print("Error parsing JSON:", e)

