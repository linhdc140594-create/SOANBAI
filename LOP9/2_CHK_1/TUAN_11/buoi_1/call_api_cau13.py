import os
import json
import requests
from dotenv import load_dotenv

load_dotenv('d:/4. GitHub/PHIEU_KIEM_TRA_THCS/.env')

url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/') + '/chat/completions'
key = os.getenv('APIVN_API_KEY')
model = os.getenv('APIVN_MODEL', 'claude-sonnet-5-5')

headers = {
    'Authorization': f'Bearer {key}',
    'Content-Type': 'application/json'
}

prompt = """Bạn là chuyên gia tổ chức thi và biên soạn đáp án môn Toán 9 THCS chuẩn chương trình mới.
Hãy thẩm định và viết lời giải chi tiết kèm thang điểm (barem) chuẩn mực, chia nhỏ tới 0,25 điểm cho bài toán hình học sau:

ĐỀ BÀI:
Cho đường tròn (O; R) và điểm A nằm bên ngoài đường tròn. Từ A kẻ hai tiếp tuyến AB, AC với (O) (B, C là các tiếp điểm). Gọi H là giao điểm của OA và BC.
a) (1,25 điểm) Chứng minh OA vuông góc với BC tại H. Cho R = 6 cm và góc BOC = 120 độ, hãy tính độ dài cung nhỏ BC của đường tròn (O).
b) (1,25 điểm) Kẻ đường kính BD của đường tròn (O). Chứng minh CD song song với OA.

YÊU CẦU:
1. Lời giải chặt chẽ từng bước theo sách giáo khoa Toán 9 hiện hành (Kết nối tri thức / Cánh diều).
2. Barem điểm chi tiết đến 0,25đ cho cả câu a và câu b.
3. Nhận xét tính tương đương với các mã đề 102 (R=9cm, goc BOC=80 độ), 103 (R=8cm, goc BOC=90 độ), 104 (R=12cm, goc BOC=60 độ).
"""

payload = {
    "model": model,
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
}

try:
    res = requests.post(url, headers=headers, json=payload, timeout=60)
    res.raise_for_status()
    ans = res.json()['choices'][0]['message']['content']
    with open('d:/4. GitHub/PHIEU_KIEM_TRA_THCS/LOP9/2_CHK_1/TUAN_11/buoi_1/api_cau13_output.txt', 'w', encoding='utf-8') as f:
        f.write(ans)
    print("API consulted successfully!")
except Exception as e:
    print("API Error:", e)
