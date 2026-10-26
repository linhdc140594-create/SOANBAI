import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\bo-de-on-tap-giua-hoc-ki-1-mon-toan-7-nam-2026-2027-theo-cau-truc-moi.pdf'
out_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01\crops'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# --- 1. Câu 4 (Trang 2, index 1) ---
p2 = doc[1]
r4 = p2.search_for("Câu 4")
r_next = p2.search_for("A. ")
# Hình nằm giữa câu 4 và các phương án A, B, C, D
# Cắt từ dưới dòng đề Câu 4 đến trên dòng A.
crop_c4 = fitz.Rect(70, r4[0].y1, p2.rect.width - 70, r_next[-1].y0)
p2.get_pixmap(clip=crop_c4, dpi=300).save(os.path.join(out_dir, 'c4_tamgiac_phangiac.png'))

# --- 2. Câu 5 (Trang 3, index 2) ---
p3 = doc[2]
r5 = p3.search_for("Câu 5")
r5_ans = p3.search_for("A. ")
crop_c5 = fitz.Rect(70, r5[0].y1, p3.rect.width - 70, r5_ans[0].y0)
p3.get_pixmap(clip=crop_c5, dpi=300).save(os.path.join(out_dir, 'c5_songsong_cat.png'))

# --- 3. Câu 7 (Trang 3, index 2) ---
r7 = p3.search_for("Câu 7")
r7_ans = p3.search_for("A. ")
# r7_ans[1] is for Cau 7
crop_c7 = fitz.Rect(70, r7[0].y1, p3.rect.width - 70, r7_ans[1].y0)
p3.get_pixmap(clip=crop_c7, dpi=300).save(os.path.join(out_dir, 'c7_truc_so.png'))

# --- 4. Câu 10 (Trang 4, index 3) ---
p4 = doc[3]
r10 = p4.search_for("Câu 10")
r10_ans = p4.search_for("A. ")
crop_c10 = fitz.Rect(70, r10[0].y1, p4.rect.width - 70, r10_ans[0].y0)
p4.get_pixmap(clip=crop_c10, dpi=300).save(os.path.join(out_dir, 'c10_khoi_langtru.png'))

# --- 5. Câu 11 (Trang 4, index 3) ---
r11 = p4.search_for("Câu 11")
r11_ans = p4.search_for("A. ")
crop_c11 = fitz.Rect(70, r11[0].y1, p4.rect.width - 70, r11_ans[1].y0)
p4.get_pixmap(clip=crop_c11, dpi=300).save(os.path.join(out_dir, 'c11_khoi_hop.png'))

# --- 6. Phần II Câu 2 (Trang 5, index 4) ---
p5 = doc[4]
r_p2c2 = p5.search_for("Câu 2")
r_p2c2_y = p5.search_for("a)")
crop_p2c2 = fitz.Rect(70, r_p2c2[0].y1, p5.rect.width - 70, r_p2c2_y[1].y0)
p5.get_pixmap(clip=crop_p2c2, dpi=300).save(os.path.join(out_dir, 'p2c2_vuonggoc_cd.png'))

# --- 7. Phần IV Câu 3 (Trang 6, index 5) ---
p6 = doc[5]
r_p4c3 = p6.search_for("Câu 3")
# Hình nằm bên cạnh hoặc phía dưới
crop_p4c3 = fitz.Rect(p6.rect.width * 0.45, r_p4c3[0].y0 - 10, p6.rect.width - 40, p6.rect.height - 100)
p6.get_pixmap(clip=crop_p4c3, dpi=300).save(os.path.join(out_dir, 'p4c3_vuonggoc_ab.png'))

print("Đã crop xong toàn bộ 7 hình vẽ ở độ phân giải siêu nét 300 DPI!")
