# -*- coding: utf-8 -*-
import os
import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

root_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1'
phan_de_thi_dir = os.path.join(root_dir, 'PHAN_DE_THI')
phan_loi_giai_dir = os.path.join(root_dir, 'PHAN_LOI_GIAI')

print("="*60)
print("BẮT ĐẦU ĐÓNG GÓI VÀ TỔNG HỢP 10 BỘ ĐỀ TOÁN 9 GIỮA KÌ I")
print("="*60)

# 1. Gộp toàn bộ 10 Đề Thi
doc_all_dethi = pymupdf.open()
for i in range(1, 11):
    pdf_name = f"De_{i:02d}_DeThi.pdf"
    pdf_path = os.path.join(phan_de_thi_dir, pdf_name)
    if os.path.exists(pdf_path):
        sub_doc = pymupdf.open(pdf_path)
        print(f"Đã nạp {pdf_name}: {len(sub_doc)} trang")
        doc_all_dethi.insert_pdf(sub_doc)
    else:
        print(f"CẢNH BÁO: Chưa có {pdf_path}")

if len(doc_all_dethi) > 0:
    tong_hop_dethi_path = os.path.join(phan_de_thi_dir, 'TONG_HOP_10_DE_THI.pdf')
    root_dethi_path = os.path.join(root_dir, 'TONG_HOP_10_DE_THI.pdf')
    doc_all_dethi.save(tong_hop_dethi_path)
    doc_all_dethi.save(root_dethi_path)
    print(f"\n=> ĐÃ XUẤT: TONG_HOP_10_DE_THI.pdf ({len(doc_all_dethi)} trang)")
else:
    print("\n=> Chưa có đề thi nào được biên dịch.")

# 2. Gộp toàn bộ 10 Hướng Dẫn Giải
doc_all_loigiai = pymupdf.open()
for i in range(1, 11):
    pdf_name = f"De_{i:02d}_DapAn.pdf"
    pdf_path = os.path.join(phan_loi_giai_dir, pdf_name)
    if os.path.exists(pdf_path):
        sub_doc = pymupdf.open(pdf_path)
        print(f"Đã nạp {pdf_name}: {len(sub_doc)} trang")
        doc_all_loigiai.insert_pdf(sub_doc)
    else:
        print(f"CẢNH BÁO: Chưa có {pdf_path}")

if len(doc_all_loigiai) > 0:
    tong_hop_loigiai_path = os.path.join(phan_loi_giai_dir, 'TONG_HOP_10_DE_LOI_GIAI.pdf')
    root_loigiai_path = os.path.join(root_dir, 'TONG_HOP_10_DE_LOI_GIAI.pdf')
    doc_all_loigiai.save(tong_hop_loigiai_path)
    doc_all_loigiai.save(root_loigiai_path)
    print(f"\n=> ĐÃ XUẤT: TONG_HOP_10_DE_LOI_GIAI.pdf ({len(doc_all_loigiai)} trang)")
else:
    print("\n=> Chưa có lời giải nào được biên dịch.")

print("="*60)

