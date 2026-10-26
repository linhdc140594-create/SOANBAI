import json
import os
import sys
import subprocess
import pypdf
import fitz

sys.stdout.reconfigure(encoding='utf-8')

work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01'
json_path = os.path.join(work_dir, 'de_01.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Mã TikZ Câu 4 chuẩn SGK
tikz_cau4 = r'''\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]
  \coordinate (B) at (0,0);
  \coordinate (C) at (5,0);
  \coordinate (A) at (1.8,2.7);

  % Chân đường phân giác AD và BE
  \path let \p1 = ($(A)-(B)$), \p2 = ($(A)-(C)$),
            \n1 = {veclen(\x1,\y1)}, \n2 = {veclen(\x2,\y2)} in
        coordinate (D) at ($(B)!{\n1/(\n1+\n2)}!(C)$);

  \path let \p1 = ($(B)-(A)$), \p2 = ($(B)-(C)$),
            \n1 = {veclen(\x1,\y1)}, \n2 = {veclen(\x2,\y2)} in
        coordinate (E) at ($(A)!{\n1/(\n1+\n2)}!(C)$);

  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[thick] (A) -- (D);
  \draw[thick] (B) -- (E);

  % Hai góc bằng nhau tại A: 2 cung cùng bán kính có 1 gạch tick ở giữa
  \draw[thick] ($(A)!0.5cm!(B)$) arc[start angle=236.3, end angle=285.5, radius=0.5cm];
  \draw[thick] ($(A)!0.5cm!(D)$) arc[start angle=285.5, end angle=329.8, radius=0.5cm];
  \draw[thick] ($(A)+(260.9:0.42cm)$) -- ($(A)+(260.9:0.58cm)$);
  \draw[thick] ($(A)+(307.6:0.42cm)$) -- ($(A)+(307.6:0.58cm)$);

  % Hai góc bằng nhau tại B: 2 cung cùng bán kính có 2 gạch tick ở giữa
  \draw[thick] ($(B)!0.75cm!(C)$) arc[start angle=0, end angle=28.15, radius=0.75cm];
  \draw[thick] ($(B)!0.75cm!(E)$) arc[start angle=28.15, end angle=56.3, radius=0.75cm];
  \draw[thick] ($(B)+(12.5:0.67cm)$) -- ($(B)+(12.5:0.83cm)$);
  \draw[thick] ($(B)+(15.5:0.67cm)$) -- ($(B)+(15.5:0.83cm)$);
  \draw[thick] ($(B)+(40.5:0.67cm)$) -- ($(B)+(40.5:0.83cm)$);
  \draw[thick] ($(B)+(43.5:0.67cm)$) -- ($(B)+(43.5:0.83cm)$);

  \node[above=2pt] at (A) {$A$};
  \node[below left=2pt] at (B) {$B$};
  \node[below right=2pt] at (C) {$C$};
  \node[below=2pt] at (D) {$D$};
  \node[right=2pt] at (E) {$E$};

  \fill (A) circle (1.5pt) (B) circle (1.5pt) (C) circle (1.5pt) (D) circle (1.5pt) (E) circle (1.5pt);
\end{tikzpicture}'''

# 2. Mã TikZ Câu 5 chuẩn góc trong cùng phía
tikz_cau5 = r'''\begin{tikzpicture}[scale=1.05, line cap=round, line join=round]
  \draw[thick] (-1.5, 2) -- (3.8, 2) node[above, pos=0.15] {$a$};
  \draw[thick] (-1.5, 0) -- (3.8, 0) node[above, pos=0.15] {$b$};

  \coordinate (P) at (2.4, 2);
  \coordinate (Q) at (1.47, 0);

  \draw[thick] ($(Q)!-0.35!(P)$) -- ($(P)!1.3!(Q)$);

  \fill[red] (P) circle (1.5pt);
  \fill[red] (Q) circle (1.5pt);

  % Góc 65°: góc nhọn trong cùng phía tại P
  \draw[thick, fill=gray!25] (P) -- ++(180:0.55cm) arc[start angle=180, end angle=245.0, radius=0.55cm] -- cycle;
  \node at ($(P)+(-0.95, -0.45)$) {$65^\circ$};

  % Góc x: góc tù trong cùng phía tại Q
  \draw[thick] ($(Q)+(65.0:0.55cm)$) arc[start angle=65.0, end angle=180, radius=0.55cm];
  \node at ($(Q)+(-0.55, 0.45)$) {$x$};
\end{tikzpicture}'''

# 3. Mã TikZ Phần II Câu 2
tikz_p2c2 = r'''\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  \coordinate (C) at (0, 3.2);
  \coordinate (D) at (0, 0);
  \coordinate (A) at (4.8, 3.2);
  \coordinate (B) at (3.0, 0);

  \draw[thick] (0, 4.0) -- (0, -0.8);
  \draw[thick] (-1.2, 3.2) -- (6.8, 3.2) node[above, pos=0.95] {$a$};
  \draw[thick] (-1.2, 0) -- (6.8, 0) node[above, pos=0.95] {$b$};
  \draw[thick] ($(B)!-0.25!(A)$) -- ($(A)!1.25!(B)$);

  % Ký hiệu góc vuông tại C và D
  \draw[thick] (0, 2.9) -- (0.3, 2.9) -- (0.3, 3.2);
  \draw[thick] (0, 0.3) -- (0.3, 0.3) -- (0.3, 0);

  \foreach \p in {C,D,A,B} \fill[red] (\p) circle (1.8pt);
  \node[above left=1pt] at (C) {$C$};
  \node[below left=1pt] at (D) {$D$};
  \node[above left=1pt] at (A) {$A$};
  \node[above left=3pt] at (B) {$B$};

  \node at ($(A)+(-0.55,-0.3)$) {$1$};

  \node at ($(B)+(-0.6, 0.45)$) {$4$};
  \node at ($(B)+(0.55, 0.4)$) {$3$};
  \node at ($(B)+(-0.55, -0.4)$) {$1$};
  \node at ($(B)+(0.6, -0.45)$) {$2$};

  \draw[thick] ($(B)+(-0.55,0)$) arc[start angle=180, end angle=60.6, radius=0.55cm];
\end{tikzpicture}'''

# 4. Mã TikZ Phần IV Câu 3
tikz_p4c3 = r'''\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  \coordinate (A) at (0, 3.2);
  \coordinate (B) at (0, 0);
  \coordinate (D) at (3.6, 3.2);
  \coordinate (C) at (4.4, 0);

  \draw[thick] (0, 4.0) -- (0, -0.8);
  \draw[thick] (-1.0, 3.2) -- (6.2, 3.2) node[above, pos=0.95] {$a$};
  \draw[thick] (-1.0, 0) -- (6.2, 0) node[above, pos=0.95] {$b$};
  \draw[thick] ($(C)!-0.25!(D)$) -- ($(D)!1.25!(C)$);

  % Ký hiệu góc vuông tại A và B
  \draw[thick] (0, 2.9) -- (0.3, 2.9) -- (0.3, 3.2);
  \draw[thick] (0, 0.3) -- (0.3, 0.3) -- (0.3, 0);

  \foreach \p in {A,B,C,D} \fill[red] (\p) circle (1.8pt);
  \node[above left=1pt] at (A) {$A$};
  \node[below left=1pt] at (B) {$B$};
  \node[above left=1pt] at (D) {$D$};
  \node[below right=1pt] at (C) {$C$};

  % Góc C = 100°
  \draw[thick] ($(C)+(-0.55,0)$) arc[start angle=180, end angle=104, radius=0.55cm];
  \node at ($(C)+(-0.95, 0.5)$) {$100^\circ$};

  % Góc D1
  \draw[thick] ($(D)+(0.5,0)$) arc[start angle=0, end angle=-76, radius=0.5cm];
  \node at ($(D)+(0.45,-0.4)$) {$1$};
\end{tikzpicture}'''

# Cập nhật vào de_01.json
for q in d['phan_I_trac_nghiem']:
    if q['cau'] == 4:
        q['hinh_tikz'] = tikz_cau4
    elif q['cau'] == 5:
        q['hinh_tikz'] = tikz_cau5

for q in d['phan_II_dung_sai']:
    if q['cau'] == 2:
        q['hinh_tikz'] = tikz_p2c2

for q in d['phan_IV_tu_luan']:
    if q['cau'] == 3:
        q['hinh_tikz'] = tikz_p4c3

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Đã cập nhật de_01.json thành công!")

# Chạy lại export_pdf_de_01.py
res = subprocess.run(['python', 'export_pdf_de_01.py'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print('Stderr:', res.stderr)

# Render lại preview ảnh trang 1 và 2 của Đề thi
doc_de = fitz.open(os.path.join(work_dir, 'De_01_DeThi.pdf'))
doc_de[0].get_pixmap(dpi=150).save(os.path.join(work_dir, 'preview_dethi_p1.png'))
doc_de[1].get_pixmap(dpi=150).save(os.path.join(work_dir, 'preview_dethi_p2.png'))
print("Đã cập nhật preview ảnh thành công!")
