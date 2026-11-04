import os
import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'd:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1'
pdf_path = os.path.join(base_dir, 'bo-de-on-tap-giua-hoc-ki-1-mon-toan-6-nam-2026-2027-theo-cau-truc-moi.pdf')

doc = pymupdf.open(pdf_path)

# Ma trận trang cho 15 đề (trang 1-based, inclusive)
de_map = [
    (1, (2, 5), (62, 69)),
    (2, (6, 9), (70, 77)),
    (3, (10, 13), (78, 85)),
    (4, (14, 17), (86, 92)),
    (5, (18, 20), (93, 99)),
    (6, (21, 24), (100, 107)),
    (7, (25, 28), (108, 116)),
    (8, (29, 32), (117, 123)),
    (9, (33, 36), (124, 129)),
    (10, (37, 40), (130, 136)),
    (11, (41, 44), (137, 143)),
    (12, (45, 48), (144, 151)),
    (13, (49, 52), (152, 162)),
    (14, (53, 56), (163, 170)),
    (15, (57, 61), (171, 180))
]

print("=== BẮT ĐẦU TRÍCH XUẤT RAW TEXT & CROPS CHO 15 ĐỀ TOÁN 6 ===")

for num, (t_start, t_end), (s_start, s_end) in de_map:
    de_dir = os.path.join(base_dir, f'DE_{num:02d}')
    crops_dir = os.path.join(de_dir, 'crops')
    os.makedirs(crops_dir, exist_ok=True)
    
    # 1. Trích xuất text Đề thi
    test_text = []
    for p in range(t_start - 1, t_end):
        test_text.append(f"--- TRANG {p+1} ---\n" + doc[p].get_text())
        # Cắt ảnh nhúng nếu có
        for img_idx, img in enumerate(doc[p].get_images()):
            xref = img[0]
            base_img = doc.extract_image(xref)
            img_bytes = base_img["image"]
            img_ext = base_img["ext"]
            img_name = f"test_p{p+1}_xref{xref}.{img_ext}"
            with open(os.path.join(crops_dir, img_name), "wb") as f_img:
                f_img.write(img_bytes)
                
    raw_test_file = os.path.join(de_dir, f'raw_test_de_{num:02d}.txt')
    with open(raw_test_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(test_text))
        
    # 2. Trích xuất text Lời giải
    sol_text = []
    for p in range(s_start - 1, s_end):
        sol_text.append(f"--- TRANG {p+1} ---\n" + doc[p].get_text())
        for img_idx, img in enumerate(doc[p].get_images()):
            xref = img[0]
            base_img = doc.extract_image(xref)
            img_bytes = base_img["image"]
            img_ext = base_img["ext"]
            img_name = f"sol_p{p+1}_xref{xref}.{img_ext}"
            with open(os.path.join(crops_dir, img_name), "wb") as f_img:
                f_img.write(img_bytes)
                
    raw_sol_file = os.path.join(de_dir, f'raw_sol_de_{num:02d}.txt')
    with open(raw_sol_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(sol_text))
        
    print(f"Đề {num:02d}: Đề (trang {t_start}-{t_end}) | Giải (trang {s_start}-{s_end}) -> Trích xuất thành công!")

print("=== HOÀN TẤT TRÍCH XUẤT TOÀN BỘ 15 ĐỀ! ===")

