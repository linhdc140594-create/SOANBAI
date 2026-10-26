import json
import os
import sys
import subprocess
import fitz

sys.stdout.reconfigure(encoding='utf-8')

work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01'
json_path = os.path.join(work_dir, 'perfect_tikz.json')

with open(json_path, 'r', encoding='utf-8') as f:
    tikz_data = json.load(f)

tex_blocks = []
keys = ['c4', 'c5', 'c7', 'c10', 'c11', 'p2c2', 'p4c3']
titles = {
    'c4': 'Câu 4. Tam giác ABC có phân giác AD và BE',
    'c5': 'Câu 5. Hai đường thẳng song song a // b',
    'c7': 'Câu 7. Trục số điểm A',
    'c10': 'Câu 10. Bốn hình lăng trụ/hình khối',
    'c11': 'Câu 11. Bốn hình khối lăng trụ/hình hộp',
    'p2c2': 'Phần II Câu 2. Vuông góc CD và các góc tại B, A',
    'p4c3': 'Phần IV Câu 3. Vuông góc AB và góc C = 100 độ'
}

for k in keys:
    code = tikz_data[k]
    # Bỏ documentclass nếu có lọt vào
    if r'\documentclass' in code:
        import re
        m = re.search(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', code, re.DOTALL)
        if m:
            code = m.group(0)
    tex_blocks.append(f"\\section*{{{titles[k]}}}\n\\begin{{center}}\n{code}\n\\end{{center}}\n")

full_tex = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta,positioning}
\usepackage[top=1.5cm, bottom=1.5cm, left=1.8cm, right=1.8cm]{geometry}

\begin{document}
''' + '\n\\vspace{0.5cm}\n'.join(tex_blocks) + r'''
\end{document}
'''

tex_file = os.path.join(work_dir, 'verify_7_figures.tex')
with open(tex_file, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print("Đang biên dịch verify_7_figures.tex...")
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'verify_7_figures.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print('Return code:', res.returncode)

if res.returncode == 0:
    pdf_file = os.path.join(work_dir, 'verify_7_figures.pdf')
    doc = fitz.open(pdf_file)
    print(f"-> Biên dịch thành công ({len(doc)} trang)!")
    for idx, page in enumerate(doc):
        page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'preview_verify_p{idx+1}.png'))
    print("-> Đã xuất ảnh preview từng trang thành công!")
else:
    print("Lỗi biên dịch:")
    for l in res.stdout.split('\n')[-30:]:
        print(l)
