import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\bo-de-on-tap-giua-hoc-ki-1-mon-toan-7-nam-2026-2027-theo-cau-truc-moi.pdf'
out_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01\crops'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# 1. Câu 4 (Page 2: y = 462 to 720)
p2 = doc[1]
fitz.Rect(50, 475, p2.rect.width - 50, 710)
p2.get_pixmap(clip=fitz.Rect(50, 475, p2.rect.width - 50, 700), dpi=300).save(os.path.join(out_dir, 'fig_c4.png'))

# 2. Câu 5 (Page 3: y = 72 to 240)
p3 = doc[2]
p3.get_pixmap(clip=fitz.Rect(50, 75, p3.rect.width - 50, 240), dpi=300).save(os.path.join(out_dir, 'fig_c5.png'))

# 3. Câu 7 (Page 3: y = 370 to 510)
p3.get_pixmap(clip=fitz.Rect(50, 375, p3.rect.width - 50, 505), dpi=300).save(os.path.join(out_dir, 'fig_c7.png'))

# 4. Câu 10 (Page 4: y = 72 to 245)
p4 = doc[3]
p4.get_pixmap(clip=fitz.Rect(50, 75, p4.rect.width - 50, 245), dpi=300).save(os.path.join(out_dir, 'fig_c10.png'))

# 5. Câu 11 (Page 4: y = 251 to 425)
p4.get_pixmap(clip=fitz.Rect(50, 255, p4.rect.width - 50, 425), dpi=300).save(os.path.join(out_dir, 'fig_c11.png'))

# 6. Phần II Câu 2 (Page 5: y = 161 to 460)
p5 = doc[4]
p5.get_pixmap(clip=fitz.Rect(50, 165, p5.rect.width - 50, 460), dpi=300).save(os.path.join(out_dir, 'fig_p2c2.png'))

# 7. Phần IV Câu 3 (Page 6: y = 280 to 550)
p6 = doc[5]
p6.get_pixmap(clip=fitz.Rect(50, 280, p6.rect.width - 50, 560), dpi=300).save(os.path.join(out_dir, 'fig_p4c3.png'))

print("Crop toàn bộ 7 hình vẽ ở độ phân giải siêu nét 300 DPI thành công!")
for f in sorted(os.listdir(out_dir)):
    if f.startswith('fig_'):
        size = os.path.getsize(os.path.join(out_dir, f))
        print(f"  - {f}: {size} bytes")
