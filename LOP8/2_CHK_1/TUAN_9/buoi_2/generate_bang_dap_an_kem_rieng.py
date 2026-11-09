import os
import subprocess
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_pdf():
    tex_path = os.path.join(CUR_DIR, "Bang_Dap_An_Ren_Luyen_Dai_So_Tuan_09_Buoi_02.tex")
    pdf_path = os.path.join(CUR_DIR, "Bang_Dap_An_Ren_Luyen_Dai_So_Tuan_09_Buoi_02.pdf")
    
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
  {\fontsize{11.5}{14}\selectfont\bfseries\color{blue!80!black} TUẦN 09 -- BUỔI 02: CỦNG CỐ KỸ NĂNG TÍNH TOÁN \& TÌM $X$}\\[2pt]
  {\small\itshape (Tài liệu dành cho Phụ huynh đối chiếu, kiểm tra kết quả bài làm của học sinh \quad|\quad Lớp Toán Thầy Lĩnh)}
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
a) & $2x^2 + 8x$ & $3x^2 + 9x$ & $4x^2 + 8x$ & $5x^2 + 10x$ \tabularnewline
\hline
\rowcolor{gray!7}
b) & $6x^3 - 9x^2 + 3x$ & $6x^3 - 8x^2 + 4x$ & $8x^3 - 12x^2 + 4x$ & $10x^3 - 10x^2 + 5x$ \tabularnewline
\hline
c) & $-4x^3 + 8x^2 y$ & $-3x^3 + 9x^2 y$ & $-5x^3 + 10x^2 y$ & $-4x^3 + 6x^2 y$ \tabularnewline
\hline
\rowcolor{gray!7}
d) & $x^2 + 5x + 6$ & $x^2 + 5x + 4$ & $x^2 + 7x + 10$ & $x^2 + 7x + 6$ \tabularnewline
\hline
e) & $x^2 + 4x - 5$ & $x^2 + 4x - 12$ & $x^2 + 4x - 21$ & $x^2 + 6x - 16$ \tabularnewline
\hline
\rowcolor{gray!7}
f) & $5x - 3$ & $5x - 2$ & $5x - 12$ & $7x - 6$ \tabularnewline
\hline
g) & $x^2 + 6x + 9$ & $x^2 + 8x + 16$ & $x^2 + 10x + 25$ & $x^2 + 12x + 36$ \tabularnewline
\hline
\rowcolor{gray!7}
h) & $4x^2 - 4x + 1$ & $9x^2 - 6x + 1$ & $4x^2 - 12x + 9$ & $9x^2 - 12x + 4$ \tabularnewline
\hline
i) & $x^2 - 16$ & $x^2 - 25$ & $x^2 - 36$ & $x^2 - 49$ \tabularnewline
\hline
\rowcolor{gray!7}
j) & $3x^2 - 2x + 1$ & $3x^2 - 2x + 1$ & $4x^2 - 3x + 1$ & $3x^2 - 2x + 1$ \tabularnewline
\hline
k) & $3xy - 2y^2 + y$ & $3xy - 2y^2 + y$ & $4xy - 3y^2 + 2y$ & $3xy - 2y^2 + y$ \tabularnewline
\hline
\rowcolor{gray!7}
l) & $8x$ & $12x$ & $16x$ & $20x$ \tabularnewline
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
a) & $x = 7$ & $x = 7$ & $x = 5$ & $x = 12$ \tabularnewline
\hline
\rowcolor{gray!7}
b) & $x = 3$ & $x = 3$ & $x = 3$ & $x = 4$ \tabularnewline
\hline
c) & $x = 2$ & $x = 2$ & $x = 2$ & $x = 2$ \tabularnewline
\hline
\rowcolor{gray!7}
d) & $x = 4$ & $x = 5$ & $x = 3$ & $x = 7$ \tabularnewline
\hline
e) & $x = 7$ & $x = 4$ & $x = 5$ & $x = 3$ \tabularnewline
\hline
\rowcolor{gray!7}
f) & $x = 3$ & $x = 11$ & $x = 2$ & $x = 5$ \tabularnewline
\hline
g) & $x = \pm 5$ & $x = \pm 6$ & $x = \pm 7$ & $x = \pm 8$ \tabularnewline
\hline
\rowcolor{gray!7}
h) & $x \in \{5; -1\}$ & $x \in \{7; -1\}$ & $x \in \{9; -1\}$ & $x \in \{9; 1\}$ \tabularnewline
\hline
i) & $x \in \{1; -7\}$ & $x \in \{3; -7\}$ & $x \in \{2; -10\}$ & $x \in \{2; -12\}$ \tabularnewline
\hline
\rowcolor{gray!7}
j) & $x \in \{7; -5\}$ & $x \in \{9; -5\}$ & $x \in \{11; -5\}$ & $x \in \{13; -5\}$ \tabularnewline
\hline
k) & $x \in \{3; -2\}$ & $x \in \{4; -1\}$ & $x \in \left\{3; -\dfrac{7}{3}\right\}$ & $x \in \left\{3; -\dfrac{5}{3}\right\}$ \tabularnewline
\hline
\rowcolor{gray!7}
l) & $x \in \{2; -5\}$ & $x \in \{3; -4\}$ & $x \in \left\{\dfrac{4}{3}; -2\right\}$ & $x \in \{7; -2\}$ \tabularnewline
\hline
\end{tabularx}

\vfill
\begin{center}
  \footnotesize\color{gray!80}
  \textit{* Ghi chú: Học sinh làm đúng mỗi ý được 0,4 điểm; làm đúng trọn vẹn cả 24 ý đạt 10,0 điểm.\\Hệ thống Phiếu Rèn Luyện Đại Số -- Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)}
\end{center}

\end{document}
'''
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    cmd = ["pdflatex", "-interaction=nonstopmode", "Bang_Dap_An_Ren_Luyen_Dai_So_Tuan_09_Buoi_02.tex"]
    subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        print("Page count:", len(reader.pages))
    else:
        print("Compilation failed!")

if __name__ == "__main__":
    generate_pdf()

