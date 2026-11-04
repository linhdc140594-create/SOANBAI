import os
import sys
import shutil
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\GitHub\SOANBAI-main\LOP8\DETHIGHK1'
pdf_path = os.path.join(base_dir, 'bo-de-on-tap-giua-hoc-ki-1-mon-toan-8-nam-2026-2027-theo-cau-truc-moi.pdf')
sty_source = os.path.join(base_dir, 'ex_test.sty')

doc = pymupdf.open(pdf_path)

# Ma trận trang cho 10 đề Lớp 8 (trang 1-based, inclusive)
de_map = [
    (1,  (2, 5),   (42, 51)),
    (2,  (6, 9),   (52, 61)),
    (3,  (10, 13), (62, 71)),
    (4,  (14, 17), (72, 80)),
    (5,  (18, 21), (81, 89)),
    (6,  (22, 25), (90, 98)),
    (7,  (26, 29), (99, 107)),
    (8,  (30, 33), (108, 115)),
    (9,  (34, 37), (116, 124)),
    (10, (38, 41), (125, 134))
]

print("=== BẮT ĐẦU TRÍCH XUẤT RAW TEXT, CROPS & CẤU TRÚC 10 ĐỀ TOÁN 8 ===")

for num, (t_start, t_end), (s_start, s_end) in de_map:
    de_dir = os.path.join(base_dir, f'DE_{num:02d}')
    crops_dir = os.path.join(de_dir, 'crops')
    os.makedirs(crops_dir, exist_ok=True)
    
    # 0. Copy ex_test.sty vào thư mục con
    if os.path.exists(sty_source):
        shutil.copy2(sty_source, os.path.join(de_dir, 'ex_test.sty'))
    
    # 1. Trích xuất text Đề thi
    test_text = []
    for p in range(t_start - 1, t_end):
        test_text.append(f"--- TRANG {p+1} ---\n" + doc[p].get_text())
        # Cắt ảnh nhúng nếu có
        for img_idx, img in enumerate(doc[p].get_images()):
            xref = img[0]
            try:
                base_img = doc.extract_image(xref)
                img_bytes = base_img["image"]
                img_ext = base_img["ext"]
                img_name = f"test_p{p+1}_xref{xref}.{img_ext}"
                with open(os.path.join(crops_dir, img_name), "wb") as f_img:
                    f_img.write(img_bytes)
            except Exception as e:
                pass
                
    raw_test_file = os.path.join(de_dir, f'raw_test_de_{num:02d}.txt')
    with open(raw_test_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(test_text))
        
    # 2. Trích xuất text Lời giải
    sol_text = []
    for p in range(s_start - 1, s_end):
        sol_text.append(f"--- TRANG {p+1} ---\n" + doc[p].get_text())
        for img_idx, img in enumerate(doc[p].get_images()):
            xref = img[0]
            try:
                base_img = doc.extract_image(xref)
                img_bytes = base_img["image"]
                img_ext = base_img["ext"]
                img_name = f"sol_p{p+1}_xref{xref}.{img_ext}"
                with open(os.path.join(crops_dir, img_name), "wb") as f_img:
                    f_img.write(img_bytes)
            except Exception as e:
                pass
                
    raw_sol_file = os.path.join(de_dir, f'raw_sol_de_{num:02d}.txt')
    with open(raw_sol_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(sol_text))
        
    print(f"Đề {num:02d}: Đề (trang {t_start:3d}-{t_end:3d}) | Giải (trang {s_start:3d}-{s_end:3d}) -> Khởi tạo & trích xuất thành công!")

# Tạo sẵn 2 thư mục tập trung
os.makedirs(os.path.join(base_dir, 'PHAN_DE_THI'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'PHAN_LOI_GIAI'), exist_ok=True)

print("=== HOÀN TẤT TRÍCH XUẤT TOÀN BỘ 10 ĐỀ VÀ THIẾT LẬP THƯ MỤC LỚP 8! ===")

