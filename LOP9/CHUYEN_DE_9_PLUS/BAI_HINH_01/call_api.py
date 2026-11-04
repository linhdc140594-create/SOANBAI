import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/') + '/chat/completions'
key = os.getenv('APIVN_API_KEY')
model = os.getenv('APIVN_MODEL', 'claude-sonnet-5-5')

headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

prompt = """Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.
Hãy phân tích sâu và giải mã bài toán hình học 9+ sau (Trích Đề 12 - Tuyển tập 55 Đề Thi Vào Lớp 10):

ĐỀ BÀI:
Cho tam giác ABC có ba góc nhọn nội tiếp đường tròn (O; R). Các đường cao AD, BF, CE của tam giác ABC cắt nhau tại H.
a) Chứng minh tứ giác BEHD nội tiếp một đường tròn.
b) Kéo dài AD cắt đường tròn (O) tại điểm thứ hai K. Kéo dài KE cắt đường tròn (O) tại điểm thứ hai I. Kẻ OM vuông góc với BC tại M. Gọi P là tâm đường tròn ngoại tiếp tam giác AEF. Gọi N là giao điểm của CI và EF.
   1) Chứng minh CE^2 = CN . CI.
   2) Chứng minh ba điểm M, N, P thẳng hàng.

YÊU CẦU:
Hãy trả về DUY NHẤT một chuỗi JSON hợp lệ (bọc trong khối ```json ... ``` hoặc thuần JSON) có cấu trúc như sau:
{
  "bai_toan": {
    "nguon": "Đề 12 - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh_cot_loi": "Mô hình Trực tâm tam giác nhọn nội tiếp đường tròn kết hợp đường trung trực và phương tích",
    "gia_thiet": "...",
    "ket_luan": "..."
  },
  "so_do_tu_duy_nguoc": {
    "muc_tieu_1": {
      "dich_den": "CE^2 = CN . CI",
      "cac_buoc_truy_nguoc": [
        "Cần: Tam giác CEN đồng dạng tam giác CIE (c-g-c hoặc g-g)",
        "Góc C chung, cần góc CEN = góc CIE",
        "Có góc CEN = góc FEH = góc FAH = góc KAC (cùng chắn cung FH của đường tròn ngoại tiếp tứ giác AEHF)",
        "Có góc CIE = góc CIK = góc CAK = góc KAC (hai góc nội tiếp cùng chắn cung CK của (O))",
        "Suy ra góc CEN = góc CIE -> Hai tam giác đồng dạng -> CE^2 = CN . CI"
      ]
    },
    "muc_tieu_2": {
      "dich_den": "Ba điểm M, N, P thẳng hàng",
      "nhan_xet_cot_loi": "M và P cùng thuộc đường trung trực của đoạn thẳng EF",
      "chien_luoc": "Chứng minh N cũng thuộc đường trung trực của EF (tức NE = NF, hay N là trung điểm của EF)",
      "cac_tang_truy_nguoc": [
        {
          "tang": 1,
          "muc_tieu": "N thuộc đường trung trực của EF",
          "cau_hoi": "Làm sao để chứng minh N là trung điểm của EF khi N chỉ là giao điểm của CI và EF?",
          "loi_giai_truy_nguoc": "Chứng minh NE = NF"
        },
        {
          "tang": 2,
          "muc_tieu": "Chứng minh NE = NF",
          "cau_hoi": "Tạo ra một tam giác vuông chứa cạnh huyền EF để dùng tính chất đường trung tuyến ứng với cạnh huyền?",
          "loi_giai_truy_nguoc": "Kẻ đường phụ EG vuông góc với AC tại G. Khi đó tam giác EGF vuông tại G có cạnh huyền là EF. Nếu N là trung điểm EF thì NG = NE = NF, nghĩa là tam giác NGF cân tại N và tam giác NGE cân tại N."
        },
        {
          "tang": 3,
          "muc_tieu": "Chứng minh tam giác NGF cân tại N (góc NGF = góc NFG)",
          "cau_hoi": "Góc NFG và góc NGF liên hệ như thế nào với các góc của tam giác ABC và đường tròn (O)?",
          "loi_giai_truy_nguoc": "Góc NFG = góc AFE = góc ABC (do tứ giác BEFC nội tiếp). Do đó cần góc NGF = góc ABC = góc AIC (cùng chắn cung AC của (O))."
        },
        {
          "tang": 4,
          "muc_tieu": "Chứng minh góc NGF = góc CIA",
          "cau_hoi": "Làm sao đưa góc NGF và góc CIA về hai tam giác đồng dạng?",
          "loi_giai_truy_nguoc": "Xét tam giác CNG và tam giác CAI có góc C chung. Cần CG/CN = CI/CA <=> CG . CA = CN . CI."
        },
        {
          "tang": 5,
          "muc_tieu": "Chứng minh CG . CA = CN . CI",
          "cau_hoi": "CG . CA và CN . CI cùng bằng đại lượng nào?",
          "loi_giai_truy_nguoc": "CG . CA = CE^2 (hệ thức lượng trong tam giác AEC vuông tại E, đường cao EG). Mặt khác CN . CI = CE^2 (đã chứng minh ở câu 1). Suy ra CG . CA = CN . CI = CE^2. ĐÂY LÀ ĐIỂM XUẤT PHÁT!"
        }
      ]
    }
  },
  "phan_tich_su_pham_ke_duong_phu": {
    "ten_duong_phu": "Kẻ EG vuông góc với AC tại G (G thuộc AC)",
    "tai_sao_nghi_ra": "Giáo viên hướng dẫn: Học sinh nhìn thấy EF nằm lơ lửng, muốn chứng minh N là trung điểm EF thì cách kinh điển là gắn EF vào một tam giác vuông nhận EF làm cạnh huyền. Vì E đã có sẵn góc vuông AEC = 90 độ, nên từ E kẻ vuông góc với AC ta vừa tạo được góc vuông EGF = 90 độ, vừa kích hoạt được hệ thức lượng CE^2 = CG . CA để kết nối với giả thiết CE^2 = CN . CI!",
    "chuoi_cau_hoi_goi_mo": [
      "Bước 1: Đường thẳng PM có tính chất đặc biệt gì đối với đoạn thẳng EF?",
      "Bước 2: Vậy muốn M, N, P thẳng hàng, điểm N phải có vị trí gì trên EF?",
      "Bước 3: Muốn chứng minh N là trung điểm EF của một đoạn thẳng lơ lửng, ta nên gắn EF vào hình nào?",
      "Bước 4: Ta đã có hệ thức CE^2 = CN . CI ở câu trước, làm sao để tạo ra tích CG . CA = CE^2?"
    ]
  },
  "loi_giai_trinh_bay_chuan_muc": {
    "cau_a": "...",
    "cau_b1": "...",
    "cau_b2": "..."
  },
  "barem_diem_chi_tiet": [
    {"phan": "Câu a", "noi_dung": "Chứng minh tứ giác BEHD nội tiếp", "diem": "0.75đ"},
    {"phan": "Câu b1", "noi_dung": "Chứng minh CE^2 = CN . CI", "diem": "0.75đ"},
    {"phan": "Câu b2 - Ý 1", "noi_dung": "Chứng minh PM là đường trung trực của EF", "diem": "0.50đ"},
    {"phan": "Câu b2 - Ý 2", "noi_dung": "Kẻ đường phụ EG vuông góc AC, chứng minh tam giác CNG đồng dạng tam giác CAI", "diem": "0.50đ"},
    {"phan": "Câu b2 - Ý 3", "noi_dung": "Chứng minh N là trung điểm EF và kết luận thẳng hàng", "diem": "0.50đ"}
  ]
}
"""

data = {
    'model': model,
    'messages': [
        {'role': 'system', 'content': 'Bạn là một chuyên gia toán học THCS cao cấp, luôn trả về JSON hợp lệ chính xác.'},
        {'role': 'user', 'content': prompt}
    ],
    'max_tokens': 4000,
    'temperature': 0.2
}

print(f"Calling API model {model}...")
resp = requests.post(url, headers=headers, json=data, timeout=90)
print(f"Status code: {resp.status_code}")
content = resp.json()['choices'][0]['message']['content']

# Clean json markdown if present
clean_json = content.strip()
if clean_json.startswith('```json'):
    clean_json = clean_json[7:]
if clean_json.startswith('```'):
    clean_json = clean_json[3:]
if clean_json.endswith('```'):
    clean_json = clean_json[:-3]
clean_json = clean_json.strip()

output_path = 'LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_01/so_do_tu_duy_nguoc.json'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(clean_json)

print(f"Saved to {output_path}")

# Verify parsing
try:
    parsed = json.loads(clean_json)
    print("Successfully parsed JSON! Root keys:", list(parsed.keys()))
except Exception as e:
    print("Warning: JSON parse error:", e)

