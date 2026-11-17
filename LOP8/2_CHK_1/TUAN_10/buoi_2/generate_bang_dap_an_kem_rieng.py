import os
import subprocess
import pymupdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_pdf():
    tex_path = os.path.join(CUR_DIR, "Bang_Dap_An_Ren_Luyen_Dai_So_Tuan_10_Buoi_02.tex")
    pdf_path = os.path.join(CUR_DIR, "Bang_Dap_An_Ren_Luyen_Dai_So_Tuan_10_Buoi_02.pdf")
    
    tex_content = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{array}
\usepackage[table]{xcolor}
\usepackage[top=0.7cm, bottom=0.7cm, left=0.7cm, right=0.7cm]{geometry}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\renewcommand{\arraystretch}{1.22}

\begin{document}
\pagestyle{empty}

% Header
\begin{center}
  {\fontsize{14}{17}\selectfont\bfseries BẢNG ĐÁP ÁN PHIẾU RÈN LUYỆN ĐẠI SỐ -- TOÁN 8}\\[2.5pt]
  {\fontsize{11.5}{14}\selectfont\bfseries\color{blue!80!black} TUẦN 10 -- BUỔI 02: THỰC HIỆN PHÉP TÍNH \& TÌM $X$ (BẬC NHẤT)}\\[2pt]
  {\small\itshape (Tài liệu dành cho Thầy Cô và Phụ huynh đối chiếu, kiểm tra kết quả bài làm \quad|\quad Lớp Toán Thầy Lĩnh)}
\end{center}

\vspace{1.5mm}

% PHẦN I
\noindent
{\bfseries\large I. CÂU 1: THỰC HIỆN PHÉP TÍNH \& RÚT GỌN (5,0 ĐIỂM -- 0,4 ĐIỂM/Ý)}
\vspace{1.0mm}

\noindent
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash\bfseries}p{1.0cm}|*{4}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{blue!15}
Ý & Mã đề 101 & Mã đề 102 & Mã đề 103 & Mã đề 104 \tabularnewline
\hline
a) & $2x^2 + 10x$ & $3x^2 + 12x$ & $4x^2 + 12x$ & $5x^2 + 10x$ \tabularnewline
\hline
\rowcolor{gray!7}
b) & $6x^3 - 12x^2 + 3x$ & $6x^3 - 10x^2 + 4x$ & $6x^3 - 9x^2 + 12x$ & $8x^3 - 12x^2 + 4x$ \tabularnewline
\hline
c) & $-8x^3 + 12x^2 y$ & $-9x^3 + 6x^2 y$ & $-5x^3 + 10x^2 y$ & $-6x^3 + 8x^2 y$ \tabularnewline
\hline
\rowcolor{gray!7}
d) & $x^2 + 7x + 12$ & $x^2 + 7x + 10$ & $x^2 + 7x + 6$ & $x^2 + 8x + 15$ \tabularnewline
\hline
e) & $x^2 + 4x - 12$ & $x^2 + 4x - 21$ & $x^2 + 6x - 7$ & $x^2 + 2x - 24$ \tabularnewline
\hline
\rowcolor{gray!7}
f) & $7x - 4$ & $8x - 3$ & $7x - 2$ & $10x - 8$ \tabularnewline
\hline
g) & $x^2 + 10x + 25$ & $x^2 + 8x + 16$ & $x^2 + 12x + 36$ & $x^2 + 14x + 49$ \tabularnewline
\hline
\rowcolor{gray!7}
h) & $4x^2 - 12x + 9$ & $9x^2 - 12x + 4$ & $4x^2 - 20x + 25$ & $9x^2 - 24x + 16$ \tabularnewline
\hline
i) & $9x^2 - 4$ & $4x^2 - 25$ & $16x^2 - 9$ & $25x^2 - 4$ \tabularnewline
\hline
\rowcolor{gray!7}
j) & $4x^2 - 3x + 2$ & $3x^2 - 2x + 1$ & $4x^2 - 3x + 2$ & $4x^2 - 3x + 2$ \tabularnewline
\hline
k) & $3xy - 2y^2 + y$ & $3xy - 2y^2 + y$ & $4xy - 3y^2 + 2y$ & $4xy - 3y^2 + 2y$ \tabularnewline
\hline
\rowcolor{gray!7}
l) & $12x$ & $16x$ & $20x$ & $8x$ \tabularnewline
\hline
\end{tabularx}

\vspace{3.0mm}

% PHẦN II
\noindent
{\bfseries\large II. CÂU 2: TÌM SỐ THỰC $X$, BIẾT: (5,0 ĐIỂM -- 0,4 ĐIỂM/Ý)}
\vspace{1.0mm}

\noindent
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash\bfseries}p{1.0cm}|*{4}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{blue!15}
Ý & Mã đề 101 & Mã đề 102 & Mã đề 103 & Mã đề 104 \tabularnewline
\hline
a) & $x = 9$ & $x = 8$ & $x = 7$ & $x = 7$ \tabularnewline
\hline
\rowcolor{gray!7}
b) & $x = 3$ & $x = 3$ & $x = 3$ & $x = 3$ \tabularnewline
\hline
c) & $x = 3$ & $x = 3$ & $x = 3$ & $x = 3$ \tabularnewline
\hline
\rowcolor{gray!7}
d) & $x = 3$ & $x = 5$ & $x = 14$ & $x = 3$ \tabularnewline
\hline
e) & $x = 8$ & $x = 3$ & $x = 5$ & $x = 8$ \tabularnewline
\hline
\rowcolor{gray!7}
f) & $x = 3$ & $x = 4$ & $x = 3$ & $x = 2$ \tabularnewline
\hline
g) & $x = 3$ & $x = 3$ & $x = 3$ & $x = 3$ \tabularnewline
\hline
\rowcolor{gray!7}
h) & $x = 3$ & $x = 4$ & $x = 4$ & $x = 4$ \tabularnewline
\hline
i) & $x = 7$ & $x = 4$ & $x = 7$ & $x = 3$ \tabularnewline
\hline
\rowcolor{gray!7}
j) & $x = 2$ & $x = 2$ & $x = 2$ & $x = 3$ \tabularnewline
\hline
k) & $x = 2$ & $x = 2$ & $x = 2$ & $x = 2$ \tabularnewline
\hline
\rowcolor{gray!7}
l) & $x = 1$ & $x = 2$ & $x = 1$ & $x = 1$ \tabularnewline
\hline
\end{tabularx}

\end{document}
'''
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
    print(f"Generated {tex_path}")
    
    cmd = ["pdflatex", "-interaction=nonstopmode", "Bang_Dap_An_Ren_Luyen_Dai_So_Tuan_10_Buoi_02.tex"]
    subprocess.run(cmd, cwd=CUR_DIR, capture_output=True)
    
    if os.path.exists(pdf_path):
        doc = pymupdf.open(pdf_path)
        print(f"Generated PDF successfully. Total pages: {len(doc)}")
        for i, page in enumerate(doc):
            text_rects = page.get_text('blocks')
            max_y = max(b[3] for b in text_rects) if text_rects else 0
            margin = page.rect.height - max_y
            print(f"Page {i+1}: max_y = {max_y:.1f}, bottom margin = {margin:.1f} pt ({margin*25.4/72:.1f} mm)")
    else:
        print("Error: PDF generation failed.")

if __name__ == "__main__":
    generate_pdf()
