import os
import sys
import shutil
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\bo-de-on-tap-giua-hoc-ki-1-mon-toan-7-nam-2026-2027-theo-cau-truc-moi.pdf'
out_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_11'
crops_dir = os.path.join(out_dir, 'crops')

os.makedirs(crops_dir, exist_ok=True)

# Copy ex_test.sty
src_sty = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_10\ex_test.sty'
dst_sty = os.path.join(out_dir, 'ex_test.sty')
if not os.path.exists(dst_sty):
    shutil.copy(src_sty, dst_sty)
    print("Copied ex_test.sty to DE_11")

doc = pymupdf.open(pdf_path)

# Test pages: 50 to 53 (0-indexed)
raw_test = []
for p in range(50, 54):
    page = doc[p]
    raw_test.append(f"\n=== PAGE {p+1} ===\n")
    raw_test.append(page.get_text())
    
    # Save whole page image
    pix = page.get_pixmap(dpi=150)
    pix.save(os.path.join(out_dir, f'orig_p{p+1}.png'))
    
    # Extract images on page
    for img_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_name = f"test_p{p+1}_xref{xref}.{image_ext}"
        with open(os.path.join(crops_dir, img_name), "wb") as f_img:
            f_img.write(image_bytes)

with open(os.path.join(out_dir, 'raw_test_de_11.txt'), 'w', encoding='utf-8') as f:
    f.write("\n".join(raw_test))
print("Saved raw_test_de_11.txt and page images")

# Sol pages: 186 to 196 (0-indexed)
raw_sol = []
for p in range(186, 197):
    page = doc[p]
    raw_sol.append(f"\n=== PAGE {p+1} ===\n")
    raw_sol.append(page.get_text())
    
    # Extract images on page
    for img_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_name = f"sol_p{p+1}_xref{xref}.{image_ext}"
        with open(os.path.join(crops_dir, img_name), "wb") as f_img:
            f_img.write(image_bytes)

with open(os.path.join(out_dir, 'raw_sol_de_11.txt'), 'w', encoding='utf-8') as f:
    f.write("\n".join(raw_sol))
print("Saved raw_sol_de_11.txt and crop images")
