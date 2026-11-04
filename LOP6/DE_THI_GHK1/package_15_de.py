# -*- coding: utf-8 -*-
import os
import sys
import shutil
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
root_dir = r"d:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1"

dir_dethi = os.path.join(root_dir, "PHAN_DE_THI")
dir_loigiai = os.path.join(root_dir, "PHAN_LOI_GIAI")
os.makedirs(dir_dethi, exist_ok=True)
os.makedirs(dir_loigiai, exist_ok=True)

print("=" * 70)
print("KIỂM TRA VÀ ĐÓNG GÓI TRỌN BỘ 15 ĐỀ THI VÀ LỜI GIẢI TOÁN 6 - GHK1")
print("=" * 70)

dethi_list = []
dapan_list = []

for i in range(1, 16):
    de_folder_name = f"DE_{i:02d}"
    folder_path = os.path.join(root_dir, de_folder_name)
    dethi_file = os.path.join(folder_path, f"De_{i:02d}_DeThi.pdf")
    dapan_file = os.path.join(folder_path, f"De_{i:02d}_DapAn.pdf")
    
    if not os.path.exists(dethi_file):
        print(f"[THIẾU] Đề {i:02d}: Không tìm thấy file {dethi_file}")
    else:
        p_count = len(pymupdf.open(dethi_file))
        dest_dethi = os.path.join(dir_dethi, f"De_{i:02d}_DeThi.pdf")
        shutil.copy2(dethi_file, dest_dethi)
        dethi_list.append(dest_dethi)
        dethi_str = f"{p_count} trang"

    if not os.path.exists(dapan_file):
        print(f"[THIẾU] Lời giải {i:02d}: Không tìm thấy file {dapan_file}")
    else:
        p_count = len(pymupdf.open(dapan_file))
        dest_dapan = os.path.join(dir_loigiai, f"De_{i:02d}_DapAn.pdf")
        shutil.copy2(dapan_file, dest_dapan)
        dapan_list.append(dest_dapan)
        dapan_str = f"{p_count} trang"

    print(f"Đề {i:02d}: Đề thi ({dethi_str}) | Hướng dẫn giải ({dapan_str}) -> Đã copy vào thư mục tập trung")

print("\n" + "=" * 70)
print("GỘP TẬP TRUNG FILE TỔNG HỢP PDF")
print("=" * 70)

# 1. Gộp 15 Đề thi
merged_dethi_doc = pymupdf.open()
for f in dethi_list:
    doc = pymupdf.open(f)
    merged_dethi_doc.insert_pdf(doc)

out_dethi_pdf = os.path.join(root_dir, "TONG_HOP_15_DE_THI.pdf")
merged_dethi_doc.save(out_dethi_pdf)
print(f"-> Gộp THÀNH CÔNG Đề thi: {out_dethi_pdf}")
print(f"   Tổng số trang Đề thi: {len(merged_dethi_doc)} trang")

# 2. Gộp 15 Lời giải
merged_dapan_doc = pymupdf.open()
for f in dapan_list:
    doc = pymupdf.open(f)
    merged_dapan_doc.insert_pdf(doc)

out_dapan_pdf = os.path.join(root_dir, "TONG_HOP_15_DE_LOI_GIAI.pdf")
merged_dapan_doc.save(out_dapan_pdf)
print(f"-> Gộp THÀNH CÔNG Lời giải: {out_dapan_pdf}")
print(f"   Tổng số trang Lời giải: {len(merged_dapan_doc)} trang")

print("=" * 70)
print("HOÀN THÀNH 100% QUY TRÌNH!")

