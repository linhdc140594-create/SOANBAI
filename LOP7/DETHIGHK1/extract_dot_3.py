import os
import sys
import shutil
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\bo-de-on-tap-giua-hoc-ki-1-mon-toan-7-nam-2026-2027-theo-cau-truc-moi.pdf'
base_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1'
src_sty = os.path.join(base_dir, 'DE_11', 'ex_test.sty')
doc = pymupdf.open(pdf_path)

de_configs = [
    (12, (54, 58), (197, 207)),
    (13, (59, 63), (208, 219)),
    (14, (64, 69), (220, 230))
]

for de_num, (t_start, t_end), (s_start, s_end) in de_configs:
    out_dir = os.path.join(base_dir, f'DE_{de_num:02d}')
    crops_dir = os.path.join(out_dir, 'crops')
    os.makedirs(crops_dir, exist_ok=True)
    
    # copy ex_test.sty
    dst_sty = os.path.join(out_dir, 'ex_test.sty')
    if not os.path.exists(dst_sty):
        shutil.copy(src_sty, dst_sty)
        
    # extract test
    raw_test = []
    for p in range(t_start, t_end + 1):
        page = doc[p]
        raw_test.append(f"\n=== PAGE {p+1} ===\n")
        raw_test.append(page.get_text())
        pix = page.get_pixmap(dpi=150)
        pix.save(os.path.join(out_dir, f"orig_p{p+1}.png"))
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            try:
                base_image = doc.extract_image(xref)
                ext = base_image["ext"]
                with open(os.path.join(crops_dir, f"test_p{p+1}_xref{xref}.{ext}"), 'wb') as f_img:
                    f_img.write(base_image['image'])
            except Exception as e:
                pass
    with open(os.path.join(out_dir, f'raw_test_de_{de_num:02d}.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(raw_test))
        
    # extract sol
    raw_sol = []
    for p in range(s_start, s_end + 1):
        page = doc[p]
        raw_sol.append(f"\n=== PAGE {p+1} ===\n")
        raw_sol.append(page.get_text())
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            try:
                base_image = doc.extract_image(xref)
                ext = base_image["ext"]
                with open(os.path.join(crops_dir, f"sol_p{p+1}_xref{xref}.{ext}"), 'wb') as f_img:
                    f_img.write(base_image['image'])
            except Exception as e:
                pass
    with open(os.path.join(out_dir, f'raw_sol_de_{de_num:02d}.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(raw_sol))
        
    print(f"Extracted DE_{de_num:02d}: test p{t_start+1}-p{t_end+1}, sol p{s_start+1}-p{s_end+1}")
