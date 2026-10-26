import json
import os
import subprocess
import pypdf
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01'
json_path = os.path.join(work_dir, 'de_01.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# CÁC MÃ TIKZ ĐƯỢC CHUẨN HÓA ĐỈNH CAO THEO ĐÚNG SÁCH & BAREM
# =============================================================================

# 1. CÂU 4: Hai góc xám bằng nhau tại A, hai vòng cung góc bằng nhau tại B
tikz_c4 = r'''\begin{tikzpicture}[scale=1.15, line cap=round, line join=round]
  \coordinate (B) at (0,0);
  \coordinate (C) at (5.2,0);
  \coordinate (A) at (1.9,2.8);

  % Toạ độ chính xác của chân phân giác D trên BC và E trên AC
  \path let \p1 = ($(A)-(B)$), \p2 = ($(A)-(C)$),
            \n1 = {veclen(\x1,\y1)}, \n2 = {veclen(\x2,\y2)} in
        coordinate (D) at ($(B)!{\n1/(\n1+\n2)}!(C)$);

  \path let \p1 = ($(B)-(A)$), \p2 = ($(B)-(C)$),
            \n1 = {veclen(\x1,\y1)}, \n2 = {veclen(\x2,\y2)} in
        coordinate (E) at ($(A)!{\n1/(\n1+\n2)}!(C)$);

  % Tại đỉnh A: Hai góc xám bằng nhau (BAD và DAC)
  \fill[gray!40] (A) -- ($(A)!0.55cm!(B)$) arc[start angle=235.8, end angle=283.4, radius=0.55cm] -- cycle;
  \fill[gray!40] (A) -- ($(A)!0.55cm!(D)$) arc[start angle=283.4, end angle=330.3, radius=0.55cm] -- cycle;
  \draw[thick] ($(A)!0.55cm!(B)$) arc[start angle=235.8, end angle=283.4, radius=0.55cm];
  \draw[thick] ($(A)!0.55cm!(D)$) arc[start angle=283.4, end angle=330.3, radius=0.55cm];

  % Tại đỉnh B: Hai vòng cung góc bằng nhau (ABE và EBC)
  \draw[thick] ($(B)!0.65cm!(C)$) arc[start angle=0, end angle=27.9, radius=0.65cm];
  \draw[thick] ($(B)!0.65cm!(E)$) arc[start angle=27.9, end angle=55.8, radius=0.65cm];

  % Các cạnh tam giác và phân giác
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[thick] (A) -- (D);
  \draw[thick] (B) -- (E);

  % Điểm và nhãn
  \foreach \p in {A,B,C,D,E} \fill (\p) circle (1.5pt);
  \node[above=2pt] at (A) {$A$};
  \node[below left=2pt] at (B) {$B$};
  \node[below right=2pt] at (C) {$C$};
  \node[below=2pt] at (D) {$D$};
  \node[above right=1pt] at (E) {$E$};
\end{tikzpicture}'''

# 2. CÂU 5: Hai góc trong cùng phía (65 độ nhọn và x tù, tổng 180 độ)
tikz_c5 = r'''\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]
  \coordinate (B) at (0,0);
  \coordinate (A) at (1.1,1.9);

  % Hai đường thẳng song song a và b
  \draw[thick] (-2.2,1.9) -- (3.2,1.9) node[above, pos=0.15] {$a$};
  \draw[thick] (-2.2,0)   -- (3.2,0)   node[above, pos=0.15] {$b$};

  % Cát tuyến đi qua B và A
  \draw[thick] (-0.6,-1.04) -- (1.8,3.12);

  % Góc nhọn 65° tại A: trong cùng phía (dưới a, bên trái cát tuyến)
  \fill[gray!35] (A) -- ++(180:0.5cm) arc[start angle=180, end angle=240, radius=0.5cm] -- cycle;
  \draw[thick] (A) ++(180:0.5cm) arc[start angle=180, end angle=240, radius=0.5cm];
  \node at ($(A)+(-0.95,-0.4)$) {$65^\circ$};

  % Góc tù x tại B: trong cùng phía (trên b, bên trái cát tuyến, 115°)
  \draw[thick] (B) ++(60:0.55cm) arc[start angle=60, end angle=180, radius=0.55cm];
  \node at ($(B)+(-0.55,0.45)$) {$x$};

  % Hai giao điểm đỏ
  \fill[red] (A) circle (1.6pt);
  \fill[red] (B) circle (1.6pt);
\end{tikzpicture}'''

# 3. CÂU 7: Trục số điểm A = -1 2/3 (-5/3)
tikz_c7 = r'''\begin{tikzpicture}[scale=1.5, line cap=round, line join=round]
  \draw[thick, ->] (-3.6,0) -- (1.6,0);
  % Vạch số nguyên chính
  \foreach \x in {-3,-2,-1,0,1}{
    \draw[thick] (\x,0.12) -- (\x,-0.12) node[below=2pt] {$\x$};
  }
  % Vạch chia phần ba (mỗi đơn vị chia 3)
  \foreach \x in {-3.333,-2.667,-2.333,-1.667,-1.333,-0.667,-0.333,0.333,0.667,1.333}{
    \draw (\x,0.06) -- (\x,-0.06);
  }
  % Điểm A tại -5/3 = -1.667
  \fill[red] (-1.667,0) circle (2pt);
  \node[above=3pt, font=\bfseries] at (-1.667,0) {$A$};
\end{tikzpicture}'''

# 4. CÂU 10: 4 hình 3D (Hình trụ, chóp cụt, lăng trụ nằm ngang, lăng trụ đứng)
tikz_c10 = r'''\begin{tikzpicture}[scale=0.6, line cap=round, line join=round]
  % Hình 1: Hình trụ
  \begin{scope}[shift={(0,0)}]
    \draw[thick] (0,0) ellipse (0.9 and 0.35);
    \draw[thick] (-0.9,0) -- (-0.9,2.5);
    \draw[thick] (0.9,0) -- (0.9,2.5);
    \draw[thick] (0,2.5) ellipse (0.9 and 0.35);
    \node[below=3pt] at (0,-0.4) {Hình 1};
  \end{scope}

  % Hình 2: Hình chóp cụt tam giác
  \begin{scope}[shift={(4.5,0)}]
    \draw[thick] (0,0) -- (2,0) -- (1.5,0.7) -- cycle;
    \draw[thick] (0.3,2.2) -- (1.7,2.2) -- (1.3,2.7) -- cycle;
    \draw[thick] (0,0) -- (0.3,2.2);
    \draw[thick] (2,0) -- (1.7,2.2);
    \draw[dashed] (1.5,0.7) -- (1.3,2.7);
    \node[below=3pt] at (1,-0.4) {Hình 2};
  \end{scope}

  % Hình 3: Lăng trụ tam giác nằm ngang
  \begin{scope}[shift={(9,0)}]
    \draw[thick] (0,0) -- (1.6,0) -- (0.8,1.5) -- cycle;
    \draw[thick] (0,0) -- (1.5,1.2);
    \draw[thick] (0.8,1.5) -- (2.3,2.7);
    \draw[thick] (1.6,0) -- (3.1,1.2);
    \draw[thick] (2.3,2.7) -- (3.1,1.2);
    \draw[dashed] (1.5,1.2) -- (2.3,2.7);
    \draw[dashed] (1.5,1.2) -- (3.1,1.2);
    \node[below=3pt] at (1.5,-0.4) {Hình 3};
  \end{scope}

  % Hình 4: Lăng trụ đứng tam giác (đúng)
  \begin{scope}[shift={(14,0)}]
    \draw[thick] (0,0) -- (2,0) -- (1.2,-0.6) -- cycle;
    \draw[thick] (0,2.5) -- (2,2.5) -- (1.2,1.9) -- cycle;
    \draw[thick] (0,0) -- (0,2.5);
    \draw[thick] (2,0) -- (2,2.5);
    \draw[thick] (1.2,-0.6) -- (1.2,1.9);
    \node[below=3pt] at (1,-0.8) {Hình 4};
  \end{scope}
\end{tikzpicture}'''

# 5. CÂU 11: 4 hình khối
tikz_c11 = r'''\begin{tikzpicture}[scale=0.6, line cap=round, line join=round]
  % Hình 1: Hình hộp chữ nhật
  \begin{scope}[shift={(0,0)}]
    \draw[thick] (0,0) rectangle (2,2.2);
    \draw[thick] (2,0) -- (2.8,0.7) -- (2.8,2.9) -- (2,2.2);
    \draw[thick] (0,2.2) -- (0.8,2.9) -- (2.8,2.9);
    \draw[dashed] (0,0) -- (0.8,0.7) -- (2.8,0.7);
    \draw[dashed] (0.8,0.7) -- (0.8,2.9);
    \node[below=3pt] at (1.4,-0.4) {Hình 1};
  \end{scope}

  % Hình 2: Lăng trụ đứng tam giác (không phải tứ giác)
  \begin{scope}[shift={(5,0)}]
    \draw[thick] (0,0) -- (2,0) -- (1.2,-0.5) -- cycle;
    \draw[thick] (0,2.2) -- (2,2.2) -- (1.2,1.7) -- cycle;
    \draw[thick] (0,0) -- (0,2.2);
    \draw[thick] (2,0) -- (2,2.2);
    \draw[thick] (1.2,-0.5) -- (1.2,1.7);
    \node[below=3pt] at (1,-0.8) {Hình 2};
  \end{scope}

  % Hình 3: Hình lập phương
  \begin{scope}[shift={(9.5,0)}]
    \draw[thick] (0,0) rectangle (1.8,1.8);
    \draw[thick] (1.8,0) -- (2.5,0.6) -- (2.5,2.4) -- (1.8,1.8);
    \draw[thick] (0,1.8) -- (0.7,2.4) -- (2.5,2.4);
    \draw[dashed] (0,0) -- (0.7,0.6) -- (2.5,0.6);
    \draw[dashed] (0.7,0.6) -- (0.7,2.4);
    \node[below=3pt] at (1.2,-0.4) {Hình 3};
  \end{scope}

  % Hình 4: Hình lăng trụ đứng tứ giác có đáy hình thang
  \begin{scope}[shift={(14,0)}]
    \draw[thick] (0,0) -- (2.2,0) -- (1.6,-0.6) -- (-0.4,-0.6) -- cycle;
    \draw[thick] (0,2.2) -- (2.2,2.2) -- (1.6,1.6) -- (-0.4,1.6) -- cycle;
    \draw[thick] (0,0) -- (0,2.2);
    \draw[thick] (2.2,0) -- (2.2,2.2);
    \draw[thick] (1.6,-0.6) -- (1.6,1.6);
    \draw[thick] (-0.4,-0.6) -- (-0.4,1.6);
    \node[below=3pt] at (0.9,-0.8) {Hình 4};
  \end{scope}
\end{tikzpicture}'''

# 6. PHẦN II CÂU 2: Hai đường a, b vuông góc CD, góc B4 = 120 độ
tikz_p2c2 = r'''\begin{tikzpicture}[scale=0.95, line cap=round, line join=round]
  \coordinate (C) at (0, 3.2);
  \coordinate (D) at (0, 0);
  \coordinate (A) at (4.8, 3.2);
  \coordinate (B) at (3.0, 0);

  % Đường CD thẳng đứng kéo dài
  \draw[thick] (0, 4.0) -- (0, -0.8);
  % Đường a qua C, A
  \draw[thick] (-1.2, 3.2) -- (6.8, 3.2) node[above, pos=0.96] {$a$};
  % Đường b qua D, B
  \draw[thick] (-1.2, 0) -- (6.8, 0) node[above, pos=0.96] {$b$};
  % Cát tuyến qua B, A kéo dài
  \draw[thick] ($(B)!-0.25!(A)$) -- ($(A)!1.25!(B)$);

  % Ký hiệu góc vuông tại C và D chuẩn ô vuông
  \draw[thick] (0, 2.9) -- (0.3, 2.9) -- (0.3, 3.2);
  \draw[thick] (0, 0.3) -- (0.3, 0.3) -- (0.3, 0);

  % Các giao điểm
  \foreach \p in {C,D,A,B} \fill[red] (\p) circle (1.8pt);
  \node[above left=1pt] at (C) {$C$};
  \node[below left=1pt] at (D) {$D$};
  \node[above left=1pt] at (A) {$A$};
  \node[above left=3pt] at (B) {$B$};

  % Tại A: góc A1 (so le trong với B3)
  \node[font=\small] at ($(A)+(-0.55,-0.3)$) {$1$};

  % Tại B: 4 góc được đánh số 1, 2, 3, 4 rõ ràng
  \node[font=\small] at ($(B)+(-0.6, 0.45)$) {$4$};
  \node[font=\small] at ($(B)+(0.55, 0.4)$) {$3$};
  \node[font=\small] at ($(B)+(-0.55, -0.4)$) {$1$};
  \node[font=\small] at ($(B)+(0.6, -0.45)$) {$2$};

  % Cung góc B4 (120°)
  \draw[thick] ($(B)+(-0.55,0)$) arc[start angle=180, end angle=60.6, radius=0.55cm];
\end{tikzpicture}'''

# 7. PHẦN IV CÂU 3: a, b vuông góc AB, góc C = 100 độ, góc D1
tikz_p4c3 = r'''\begin{tikzpicture}[scale=0.95, line cap=round, line join=round]
  \coordinate (A) at (0, 3.2);
  \coordinate (B) at (0, 0);
  \coordinate (D) at (3.6, 3.2);
  \coordinate (C) at (4.4, 0);

  % Đoạn AB vuông góc kéo dài
  \draw[thick] (0, 4.0) -- (0, -0.8);
  % Đường a qua A, D
  \draw[thick] (-1.0, 3.2) -- (6.2, 3.2) node[above, pos=0.96] {$a$};
  % Đường b qua B, C
  \draw[thick] (-1.0, 0) -- (6.2, 0) node[above, pos=0.96] {$b$};
  % Cát tuyến CD kéo dài
  \draw[thick] ($(C)!-0.25!(D)$) -- ($(D)!1.25!(C)$);

  % Ký hiệu góc vuông tại A và B
  \draw[thick] (0, 2.9) -- (0.3, 2.9) -- (0.3, 3.2);
  \draw[thick] (0, 0.3) -- (0.3, 0.3) -- (0.3, 0);

  % Các giao điểm
  \foreach \p in {A,B,C,D} \fill[red] (\p) circle (1.8pt);
  \node[above left=1pt] at (A) {$A$};
  \node[below left=1pt] at (B) {$B$};
  \node[above left=1pt] at (D) {$D$};
  \node[below right=1pt] at (C) {$C$};

  % Góc C = 100° (góc trong cùng phía tại C)
  \draw[thick] ($(C)+(-0.55,0)$) arc[start angle=180, end angle=104, radius=0.55cm];
  \node at ($(C)+(-0.95, 0.5)$) {$100^\circ$};

  % Góc D1
  \draw[thick] ($(D)+(0.5,0)$) arc[start angle=0, end angle=-76, radius=0.5cm];
  \node at ($(D)+(0.45,-0.4)$) {$1$};
\end{tikzpicture}'''

# Cập nhật vào de_01.json
for q in d['phan_I_trac_nghiem']:
    if q['cau'] == 4: q['hinh_tikz'] = tikz_c4
    elif q['cau'] == 5: q['hinh_tikz'] = tikz_c5
    elif q['cau'] == 7: q['hinh_tikz'] = tikz_c7
    elif q['cau'] == 10: q['hinh_tikz'] = tikz_c10
    elif q['cau'] == 11: q['hinh_tikz'] = tikz_c11

for q in d['phan_II_dung_sai']:
    if q['cau'] == 2: q['hinh_tikz'] = tikz_p2c2

for q in d['phan_IV_tu_luan']:
    if q['cau'] == 3: q['hinh_tikz'] = tikz_p4c3

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Đã cập nhật de_01.json với toàn bộ 7 hình TikZ chuẩn tuyệt đối!")

# Biên dịch lại cả 2 file PDF
res = subprocess.run(['python', 'export_pdf_de_01.py'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print('Stderr:', res.stderr)

# Xuất ảnh preview mới
doc_de = fitz.open(os.path.join(work_dir, 'De_01_DeThi.pdf'))
print(f"De_01_DeThi.pdf: {len(doc_de)} trang")
for idx, page in enumerate(doc_de):
    page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'preview_dethi_p{idx+1}.png'))

doc_da = fitz.open(os.path.join(work_dir, 'De_01_DapAn.pdf'))
print(f"De_01_DapAn.pdf: {len(doc_da)} trang")
for idx, page in enumerate(doc_da):
    page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'preview_dapan_p{idx+1}.png'))

print("ĐÃ HOÀN TẤT VÀ XUẤT ẢNH PREVIEW CỦA TẤT CẢ CÁC TRANG!")
