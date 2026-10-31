# -*- coding: utf-8 -*-
"""
Runner script tự động chạy tất cả 8 tuần (Tuần 09 -> Tuần 16) môn Toán Lớp 5.
Biên dịch LaTeX và kiểm tra độ dài chính xác 14 trang/file PDF.
"""

import os
import sys
import subprocess
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("="*60)
print("BẮT ĐẦU BIÊN DỊCH VÀ KIỂM TRA PHIẾU BÀI TẬP TUẦN TOÁN LỚP 5")
print("="*60)

all_passed = True
results = []

for w in range(9, 17):
    gen_script = os.path.join(BASE_DIR, f"generate_tuan_{w:02d}.py")
    week_str = f"TUAN_{w:02d}"
    pdf_path = os.path.join(BASE_DIR, week_str, f"Phieu_Bai_Tap_Tuan_{w:02d}_Toan5.pdf")
    
    print(f"\n[+] Đang xử lý {week_str}...")
    res = subprocess.run([sys.executable, gen_script], cwd=BASE_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[-] LỖI chạy {gen_script}:")
        print(res.stderr)
        all_passed = False
        results.append((w, "LỖI BIÊN DỊCH", 0))
        continue
        
    if not os.path.exists(pdf_path):
        print(f"[-] Không tìm thấy file PDF: {pdf_path}")
        all_passed = False
        results.append((w, "THIẾU PDF", 0))
        continue
        
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    if total_pages == 14:
        print(f"[OK] {week_str}: 14 trang chuẩn.")
        results.append((w, "THÀNH CÔNG", 14))
    else:
        print(f"[-] {week_str}: Sai số trang ({total_pages} trang thay vì 14)!")
        all_passed = False
        results.append((w, "SAI SỐ TRANG", total_pages))

print("\n" + "="*60)
print("KẾT QUẢ TỔNG HỢP CÁC TUẦN TOÁN LỚP 5:")
print("="*60)
for w, status, pages in results:
    print(f"Tuần {w:02d}: {status} - {pages} trang")

if all_passed:
    print("\n🎉 TẤT CẢ 8 TUẦN (TUẦN 09 -> 16) HOÀN HẢO VỚI ĐÚNG 14 TRANG/FILE PDF!")
else:
    print("\n❌ CÓ LỖI XẢY RA TRONG QUÁ TRÌNH BIÊN DỊCH!")

