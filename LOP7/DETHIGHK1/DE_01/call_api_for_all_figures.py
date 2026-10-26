import os
import sys
import json
import base64
import urllib.request
import re

sys.path.append(r'd:\GitHub\SOANBAI-main')
from auto_create_exam import load_env

sys.stdout.reconfigure(encoding='utf-8')
env = load_env()
crops_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01\crops'

figures = [
    {
        'key': 'c4',
        'file': 'fig_c4.png',
        'desc': 'Tam giác ABC có tia phân giác AD (của góc A) và BE (của góc B). Đỉnh A có 2 góc nhỏ bằng nhau (kí hiệu 2 cung kèm tick/chấm), đỉnh B có 2 góc nhỏ bằng nhau (kí hiệu 2 cung kèm tick đôi). Tên các điểm A, B, C, D, E.'
    },
    {
        'key': 'c5',
        'file': 'fig_c5.png',
        'desc': 'Hai đường thẳng song song a và b bị cắt bởi cát tuyến. Góc nhọn 65 độ ở miền trong cùng phía (dưới đường a, bên trái cát tuyến). Góc x ở miền trong cùng phía (trên đường b, bên trái cát tuyến). Chữ số 65 độ và chữ x phải nằm thoáng trong miền góc, tuyệt đối không đè lên đường cát tuyến.'
    },
    {
        'key': 'c7',
        'file': 'fig_c7.png',
        'desc': 'Trục số ngang có mũi tên sang phải. Các vạch nguyên từ -3 đến 1. Giữa mỗi 2 số nguyên chia làm 3 đoạn bằng nhau (bằng các vạch chia nhỏ). Điểm A nằm tại vị trí -1 và 2/3 (tức -5/3). Có chấm tròn đen tại A và nhãn A ở trên.'
    },
    {
        'key': 'c10',
        'file': 'fig_c10.png',
        'desc': 'Cụm 4 hình vẽ 3D: Hình 1 là hình trụ tròn; Hình 2 là hình chóp cụt tam giác; Hình 3 là hình lăng trụ đứng tam giác đặt nằm ngang; Hình 4 là hình lăng trụ đứng tam giác đặt thẳng đứng (có 2 đáy là tam giác song song, các mặt bên là hình chữ nhật). Dưới mỗi hình có nhãn "Hình 1", "Hình 2", "Hình 3", "Hình 4".'
    },
    {
        'key': 'c11',
        'file': 'fig_c11.png',
        'desc': 'Cụm 4 hình vẽ 3D: Hình 1 là hình hộp chữ nhật/lăng trụ đứng tứ giác; Hình 2 là hình lăng trụ đứng tam giác; Hình 3 là hình lập phương; Hình 4 là hình lăng trụ xiên hoặc tứ diện/chóp cụt. Dưới mỗi hình có nhãn "Hình 1", "Hình 2", "Hình 3", "Hình 4".'
    },
    {
        'key': 'p2c2',
        'file': 'fig_p2c2.png',
        'desc': 'Hai đường thẳng ngang a (trên) và b (dưới) cùng vuông góc với đường thẳng đứng CD tại C và D (có ký hiệu ô vuông góc vuông chuẩn tại C và D). Cát tuyến đi qua B (trên đường b) và A (trên đường a). Tại đỉnh B có 4 góc được đánh số 1, 2, 3, 4 ở 4 góc phần tư. Tại đỉnh A có góc A1 (so le trong với B3). Góc B4 = 120 độ.'
    },
    {
        'key': 'p4c3',
        'file': 'fig_p4c3.png',
        'desc': 'Hai đường thẳng ngang a và b cùng vuông góc với đường thẳng đứng AB tại A và B (có ký hiệu góc vuông chuẩn tại A và B). Cát tuyến CD cắt a tại D và b tại C. Tại C có góc C = 100 độ (có cung tròn và số 100 độ rõ ràng). Tại D có góc D1 (có số 1).'
    }
]

def call_vision_tikz(fig_info):
    img_path = os.path.join(crops_dir, fig_info['file'])
    with open(img_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')

    prompt = f"""Bạn là một chuyên gia toán học và chuyên gia lập trình TikZ cao cấp.
Dưới đây là ảnh chụp cận cảnh độ phân giải cao 300 DPI của hình vẽ trong đề thi Toán THCS ({fig_info['file']}).
Mô tả sơ bộ bài toán: {fig_info['desc']}

HÃY DÙNG MẮT THẦN THỊ GIÁC SOI THẬT KỸ VÀ TÁI TẠO MÃ TIKZ HOÀN HẢO 100%:
1. ĐO ĐẠC HÌNH HỌC & TỌA ĐỘ:
   - Xác định tọa độ các điểm chuẩn xác, các tỉ lệ cạnh và phương hướng.
2. KÝ HIỆU GÓC (Angle markings - CỰC KỲ QUAN TRỌNG):
   - Ký hiệu góc vuông: Vẽ ô vuông chuẩn xác tại đỉnh (dùng các đoạn thẳng vuông góc nhỏ 0.2cm - 0.25cm).
   - Ký hiệu góc bằng nhau (như góc phân giác): Vẽ các cung góc riêng biệt có cùng bán kính và CÓ CÙNG VẠCH TICK đánh dấu (hoặc tick đôi) để người xem nhận biết ngay hai góc bằng nhau.
   - Vòng cung góc số đo: Bán kính vừa phải (0.4cm - 0.6cm), nhãn số đo (ví dụ: $65^\\circ$, $100^\\circ$, $x$, số $1, 2, 3, 4$) phải đặt thoáng ở vị trí phân giác góc, TUYỆT ĐỐI KHÔNG ĐÈ LÊN NÉT VẼ ĐƯỜNG THẲNG HOẶC ĐIỂM.
3. ĐƯỜNG NÉT & NHÃN ĐỈNH:
   - Nét vẽ rõ ràng, nét đứt (dashed) cho nét khuất trong hình 3D, nét liền (thick/thin) cho nét thấy.
   - Nhãn điểm ($A, B, C, D, E$, tên đường $a, b$) đặt lệch ngoài (above, below, left, right) với khoảng cách offset an toàn.
4. ĐỊNH DẠNG:
   - Trả về mã TikZ gói gọn trong duy nhất một môi trường:
     \\begin{{tikzpicture}}[scale=..., line cap=round, line join=round]
     ...
     \\end{{tikzpicture}}
   - Không dùng package lạ ngoài tikz (các thư viện chuẩn: calc, angles, quotes, arrows.meta).
   - Chỉ trả về khối code LaTeX trong ```latex ... ```.
"""

    payload = {
        'model': env.get('APIVN_MODEL', 'claude-sonnet-5-5'),
        'messages': [
            {'role': 'user', 'content': [
                {'type': 'text', 'text': prompt},
                {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{b64}'}}
            ]}
        ],
        'temperature': 0.1,
        'max_tokens': 1800
    }

    url = f"{env.get('APIVN_BASE_URL').rstrip('/')}/chat/completions"
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
        'Authorization': f"Bearer {env.get('APIVN_API_KEY')}",
        'Content-Type': 'application/json'
    })
    with urllib.request.urlopen(req, timeout=120) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        content = res['choices'][0]['message']['content']
        match = re.search(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', content, re.DOTALL)
        if match:
            return match.group(0)
        return content

results = {}
for fig in figures:
    print(f"-> Đang gửi API soi kỹ hình {fig['key']} ({fig['file']})...")
    tikz_code = call_vision_tikz(fig)
    results[fig['key']] = tikz_code
    print(f"   Đã nhận mã TikZ cho {fig['key']} ({len(tikz_code)} ký tự)!")

out_json = os.path.join(r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01', 'perfect_tikz.json')
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"==================================================")
print(f"ĐÃ LƯU TOÀN BỘ 7 HÌNH VẼ TIKZ SIÊU CHUẨN VÀO: {out_json}")
print(f"==================================================")
