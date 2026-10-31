# -*- coding: utf-8 -*-
"""
Script cập nhật Bài 4 và Bài 5 chuẩn Lớp 5 vào tất cả các tuần (Tuần 9 đến 16).
Biên dịch lại toàn bộ PDF và kiểm tra 14 trang/file.
"""

import os
import sys
import json
import subprocess
import pypdf
import importlib.util

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\GitHub\quanlytrungtamthaylinh-main\1.SACH\LOP4\PHIEU_BAI_TAP_TUAN"
DATA_FILE = os.path.join(BASE_DIR, "grade5_bai4_bai5_data.json")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    g5_data = json.load(f)

from shared_template import render_tex, render_markdown_answers, compile_and_verify

all_success = True

for w in range(9, 17):
    week_str = f"TUAN_{w:02d}"
    gen_file = os.path.join(BASE_DIR, f"generate_tuan_{w:02d}.py")
    
    # Load existing module
    spec = importlib.util.spec_from_file_location(f"gen_{w}", gen_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    
    # Update bai4 and bai5 for each ma_de
    w_updates = g5_data.get(str(w), [])
    for idx, item in enumerate(mod.MA_DE_LIST):
        if idx < len(w_updates):
            item["bai4"] = w_updates[idx]["bai4"]
            item["bai5"] = w_updates[idx]["bai5"]
            
    # Write updated generator file back
    # Also write tex and md
    out_dir = os.path.join(BASE_DIR, week_str)
    os.makedirs(out_dir, exist_ok=True)
    
    week_title = getattr(mod, "WEEK_TITLE", "Yến, tạ, tấn -- Đề-xi-mét vuông, mét vuông, mi-li-mét vuông")
    topics = getattr(mod, "TOPICS", [
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
    ])
    ma_de_list = mod.MA_DE_LIST
    
    tex_content = render_tex(w, week_title, ma_de_list)
    tex_path = os.path.join(out_dir, f"Phieu_Bai_Tap_Tuan_{w:02d}_Toan4.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
        
    md_content = render_markdown_answers(w, week_title, topics, ma_de_list)
    md_path = os.path.join(out_dir, "DAP_AN_VA_THANG_DIEM.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    # Compile
    ok = compile_and_verify(w, BASE_DIR)
    if not ok:
        all_success = False

print("\n" + "="*50)
if all_success:
    print("ALL 8 WEEKS SUCCESSFULLY UPDATED & COMPILED WITH GRADE 5 BAI 4 & 5!")
else:
    print("SOME WEEKS FAILED COMPILATION.")
