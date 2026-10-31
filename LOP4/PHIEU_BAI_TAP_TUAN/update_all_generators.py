# -*- coding: utf-8 -*-
"""
Script cập nhật vĩnh viễn dữ liệu Lớp 5 (Bài 4 và Bài 5) vào từng file generator:
generate_tuan_09.py -> generate_tuan_16.py.
Đồng thời render và biên dịch toàn bộ 8 tuần, kiểm tra đúng 14 trang/file.
"""

import os
import sys
import json
import pprint
import importlib.util

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\GitHub\quanlytrungtamthaylinh-main\1.SACH\LOP4\PHIEU_BAI_TAP_TUAN"
DATA_FILE = os.path.join(BASE_DIR, "grade5_bai4_bai5_data.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    g5_data = json.load(f)

WEEK_TITLES = {
    9: "Yến, tạ, tấn -- Đề-xi-mét vuông, mét vuông, mi-li-mét vuông",
    10: "Giây, thế kỉ -- Thực hành trải nghiệm đơn vị đo đại lượng",
    11: "Luyện tập chung đại lượng -- Phép cộng các số có nhiều chữ số",
    12: "Phép trừ các số có nhiều chữ số -- Tính chất giao hoán, kết hợp của phép cộng",
    13: "Tìm hai số khi biết tổng và hiệu của hai số đó -- Luyện tập chung",
    14: "Hai đường thẳng vuông góc -- Góc nhọn, góc tù, góc bẹt",
    15: "Hai đường thẳng song song -- Thực hành vẽ hai đường thẳng song song",
    16: "Hình bình hành, hình thoi -- Ôn tập tổng hợp cuối học kì 1",
}

DEFAULT_TOPICS = [
    "Cấu tạo số, đọc viết số đến lớp triệu",
    "Xác định giá trị và hàng của chữ số",
    "So sánh các số có nhiều chữ số",
    "Làm tròn số đến hàng trăm nghìn",
    "Đổi đơn vị đo khối lượng (yến, tạ, tấn)",
    "Đổi đơn vị đo diện tích (dm2, m2, mm2)",
    "Thời gian: Thế kỉ, năm, phút, giây",
    "Đặt tính và tính cộng, trừ số lớn",
    "Tìm thành phần chưa biết (Tìm x)",
    "Tính chất phép cộng và phép trừ",
    "Bài toán rút về đơn vị / tỉ lệ",
    "Bài toán thực tế diện tích và khối lượng",
]

for w in range(9, 17):
    week_str = f"TUAN_{w:02d}"
    gen_file = os.path.join(BASE_DIR, f"generate_tuan_{w:02d}.py")
    
    spec = importlib.util.spec_from_file_location(f"gen_{w}", gen_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    
    w_updates = g5_data.get(str(w), [])
    ma_de_list = mod.MA_DE_LIST
    for idx, item in enumerate(ma_de_list):
        if idx < len(w_updates):
            item["bai4"] = w_updates[idx]["bai4"]
            item["bai5"] = w_updates[idx]["bai5"]
            
    title = getattr(mod, "WEEK_TITLE", WEEK_TITLES[w])
    topics = getattr(mod, "TOPICS", DEFAULT_TOPICS)
    
    # Format ma_de_list as clean python code
    formatted_ma_de = pprint.pformat(ma_de_list, width=120, sort_dicts=False, compact=False)
    formatted_topics = pprint.pformat(topics, width=100, sort_dicts=False)
    
    new_script_content = f"""# -*- coding: utf-8 -*-
\"\"\"
Script sinh Phiếu bài tập cuối tuần Toán 4 - {week_str} với 7 Mã đề (401 -> 407).
Chủ đề: {title}
Bài 4 và Bài 5: Nâng cao & chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
\"\"\"

import os
import sys
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = {w}
WEEK_TITLE = {repr(title)}

TOPICS = {formatted_topics}

MA_DE_LIST = {formatted_ma_de}

def main():
    base_dir = r"{BASE_DIR}"
    out_dir = os.path.join(base_dir, f"TUAN_{{WEEK_NUM:02d}}")
    os.makedirs(out_dir, exist_ok=True)

    tex_content = render_tex(WEEK_NUM, WEEK_TITLE, MA_DE_LIST)
    tex_path = os.path.join(out_dir, f"Phieu_Bai_Tap_Tuan_{{WEEK_NUM:02d}}_Toan4.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
    print("Wrote:", tex_path)

    md_content = render_markdown_answers(WEEK_NUM, WEEK_TITLE, TOPICS, MA_DE_LIST)
    md_path = os.path.join(out_dir, "DAP_AN_VA_THANG_DIEM.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print("Wrote:", md_path)

    compile_and_verify(WEEK_NUM, base_dir)

if __name__ == "__main__":
    main()
"""
    with open(gen_file, "w", encoding="utf-8") as f:
        f.write(new_script_content)
    print(f"Updated source file: {gen_file}")

print("\nRunning apply_grade5_updates to compile all 8 weeks...")
os.system(f"python {os.path.join(BASE_DIR, 'apply_grade5_updates.py')}")

