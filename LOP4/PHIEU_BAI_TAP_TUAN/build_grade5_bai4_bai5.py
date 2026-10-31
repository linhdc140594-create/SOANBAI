# -*- coding: utf-8 -*-
"""
Script gọi API apivn.vn (deepseek-v4.1-flash) để sáng tạo Bài 4 & Bài 5
cho 8 tuần (Tuần 09 -> Tuần 16) phù hợp chương trình Học kì 1 Lớp 5.
"""

import sys
import os
import json
import time
import requests

sys.stdout.reconfigure(encoding='utf-8')

API_KEY = "sk-NPHkwWDNZwJ32kLzOyCRgW7S3pl72cNST6SfZcuxYf5kthMu"
URL = "https://apivn.vn/v1/chat/completions"
MODEL = "deepseek-v4.1-flash"

WEEK_CONFIGS = {
    9: {
        "title": "Đơn vị đo diện tích (héc-ta ha, m2), số thập phân, bài toán diện tích và sản lượng nông sản",
        "bai4_desc": "Bài toán thực tế diện tích mảnh đất (chữ nhật/hình bình hành), đổi ra mét vuông và héc-ta (ha), tính sản lượng thu hoạch nông sản hoặc năng suất",
        "bai5_desc": "Tính thuận tiện với phân số hoặc số thập phân, nhóm số hạng tạo thành số tự nhiên tròn"
    },
    10: {
        "title": "Phép cộng và phép trừ số thập phân",
        "bai4_desc": "Bài toán thực tế 3 bước tính về phép cộng và phép trừ số thập phân (khối lượng hàng hóa tấn/tạ, cự ly km/m, xuất nhập kho)",
        "bai5_desc": "Tính bằng cách thuận tiện nhất: tính chất giao hoán và kết hợp của phép cộng/trừ số thập phân (nhóm tạo thành số tự nhiên tròn chục, tròn trăm)"
    },
    11: {
        "title": "Phép nhân và phép chia số thập phân",
        "bai4_desc": "Bài toán thực tế về nhân, chia số thập phân (tính tiền mua hàng, lượng xăng dầu tiêu thụ theo km, bài toán rút về đơn vị với số thập phân)",
        "bai5_desc": "Tính thuận tiện phép nhân số thập phân: áp dụng tính chất phân phối a x b + a x c = a x (b + c) với số thập phân"
    },
    12: {
        "title": "Nhân, chia số thập phân với 10, 100, 1000... và 0.1, 0.01... Phối hợp 4 phép tính",
        "bai4_desc": "Bài toán kinh tế/đo lường thực tế kết hợp chuyển đổi đơn vị và 4 phép tính số thập phân, tính chi phí, giá thành",
        "bai5_desc": "Tính nhanh biểu thức số thập phân: dạng a x 101 - a hoặc a x 9.9 + a x 0.1 hoặc 0.25 x 4 x a"
    },
    13: {
        "title": "Hình tam giác - Diện tích hình tam giác. Hình thang - Diện tích hình thang",
        "bai4_desc": "Bài toán thực tế về diện tích thửa ruộng hình tam giác hoặc hình thang (đáy lớn, đáy bé, chiều cao), tính sản lượng lúa/ngô thu hoạch được theo tạ hoặc tấn",
        "bai5_desc": "Bài toán nâng cao về tỉ số diện tích hình tam giác, hoặc diện tích hình thang khi tăng giảm đáy"
    },
    14: {
        "title": "Đường tròn - Chu vi và diện tích hình tròn",
        "bai4_desc": "Bài toán thực tế về chu vi và diện tích hình tròn (bánh xe lăn được quãng đường, bồn hoa hình tròn, đường bao quanh giếng nước)",
        "bai5_desc": "Tính diện tích phần tô đậm giữa hình vuông và hình tròn nội tiếp (hoặc hình vành khuyên)"
    },
    15: {
        "title": "Luyện tập chung hình phẳng (tam giác, thang, tròn) & số thập phân",
        "bai4_desc": "Bài toán thực tế hình phẳng kết hợp (mảnh đất hình thang hoặc hình chữ nhật ghép tam giác), tính chi phí làm sân, lát gạch, trồng cỏ",
        "bai5_desc": "Tính bằng cách thuận tiện nhất: tổng một dãy số thập phân cách đều hoặc biểu thức phân phối số thập phân"
    },
    16: {
        "title": "Ôn tập tổng hợp cuối học kì 1 Lớp 5 (Số thập phân, hình học, tỉ số phần trăm)",
        "bai4_desc": "Bài toán tổng hợp ôn thi học kì 1 Lớp 5: mảnh đất hình thang có đáy lớn, đáy bé, chiều cao; tính diện tích và tỉ số phần trăm diện tích làm nhà/trồng cây",
        "bai5_desc": "Bài toán nâng cao ôn thi học kì 1: tính nhanh biểu thức số thập phân dạng phân thức hoặc dãy số đặc biệt"
    }
}

def generate_week_bai4_bai5(week_num: int):
    cfg = WEEK_CONFIGS[week_num]
    prompt = f"""Bạn là chuyên gia biên soạn đề thi Toán Lớp 5 theo chương trình GDPT 2018 cho Trung tâm Toán Thầy Lĩnh.
Hãy tạo BÀI 4 và BÀI 5 phần tự luận cho 7 MÃ ĐỀ (401, 402, 403, 404, 405, 406, 407) của TUẦN {week_num}.
Chủ đề tuần {week_num}: {cfg['title']}.

Yêu cầu cụ thể:
1. Bài 4 (1,5 điểm): {cfg['bai4_desc']}.
   - Số liệu thực tế, phong phú, khác nhau giữa 7 mã đề.
   - Các phép tính phải ra số tự nhiên hoặc số thập phân đẹp (tối đa 2 chữ số thập phân, không tuần hoàn).
   - Lời giải chia làm 3-4 bước rõ ràng, viết bằng LaTeX chuẩn ($...$), độ dài vừa vặn 11 dòng kẻ chấm.
2. Bài 5 (1,0 điểm): {cfg['bai5_desc']}.
   - Phù hợp trình độ học sinh khá giỏi lớp 5.
   - Lời giải 2-3 bước ngắn gọn, viết bằng LaTeX chuẩn, vừa vặn 6-8 dòng kẻ chấm.

Trả về DUY NHẤT một mảng JSON (không có markdown ```json, không văn bản phụ):
[
  {{
    "ma_de": "401",
    "bai4": {{
      "de": "Một thửa ruộng hình...",
      "b1": "Lời giải bước 1...",
      "b2": "Lời giải bước 2...",
      "b3": "Lời giải bước 3...",
      "b4": "Lời giải bước 4..."
    }},
    "bai5": {{
      "bieuthuc": "K = ...",
      "buoc1": "= ...",
      "buoc2": "= ...",
      "ans": "= ..."
    }}
  }},
  ... (cho đủ 7 mã đề 401 đến 407)
]
"""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': MODEL,
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }

    for attempt in range(3):
        try:
            print(f"Calling API for Week {week_num} (attempt {attempt+1})...")
            resp = requests.post(URL, headers=headers, json=data, timeout=60)
            if resp.status_code == 200:
                raw = resp.json()['choices'][0]['message']['content'].strip()
                # Remove any markdown code blocks
                if raw.startswith("```"):
                    lines = raw.split("\n")
                    if lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines and lines[-1].startswith("```"):
                        lines = lines[:-1]
                    raw = "\n".join(lines).strip()
                parsed = json.loads(raw)
                if len(parsed) >= 7:
                    print(f"Week {week_num} generated successfully ({len(parsed)} codes).")
                    return parsed
            else:
                print(f"API Error {resp.status_code}: {resp.text}")
        except Exception as e:
            print(f"Error on week {week_num}: {e}")
        time.sleep(2)
    return None

if __name__ == "__main__":
    results = {}
    for w in range(9, 17):
        data = generate_week_bai4_bai5(w)
        if data:
            results[str(w)] = data
        time.sleep(1)

    out_file = r"d:\GitHub\quanlytrungtamthaylinh-main\1.SACH\LOP4\PHIEU_BAI_TAP_TUAN\grade5_bai4_bai5_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Finished! Saved all data to {out_file}")

