import json
import os
import subprocess
import pypdf
import pymupdf
import numpy as np

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

data_05 = {
    "base_filename": "Phieu_Kiem_Tra_Tuan_12_Buoi_01_Ma05",
    "title_p1": "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 8 - TUẦN 12 - BUỔI 01",
    "title_p2": "TOÁN 8 - TUẦN 12 - BUỔI 01",
    "code": "05",
    "short": [
        [
            "Cho $\\Delta ABC$ vuông tại $A$ có $AB = 8\\text{ cm}, AC = 15\\text{ cm}$. Tính $BC =$",
            "17\\text{ cm}"
        ],
        [
            "Cho $\\Delta ABC, MN \\parallel BC$. Biết $AM = 3, AB = 9, BC = 12$. $MN =$",
            "4"
        ],
        [
            "Cho $\\Delta ABC, DE \\parallel BC$. Biết $AD = 3, DB = 9, AE = 4$. Tính $EC =$",
            "12"
        ],
        [
            "Điều kiện xác định của phân thức $\\dfrac{3x + 5}{x - 7}$ là:",
            "x \\ne 7"
        ],
        [
            "Giá trị của phân thức $P = \\dfrac{x + 5}{x - 2}$ tại $x = 3$ là:",
            "8"
        ],
        [
            "Rút gọn phân thức $\\dfrac{15x^3y^2}{25x^2y^3} =$ (với $xy \\ne 0$):",
            "\\dfrac{3x}{5y}"
        ],
        [
            "Với giá trị nào của $x$ thì phân thức $\\dfrac{6x - 18}{x + 5} = 0$?",
            "x = 3"
        ],
        [
            "Điền vào chỗ trống: $\\dfrac{x + 3}{x - 5} = \\dfrac{\\dots}{x^2 - 25}$.",
            "(x + 3)(x + 5)"
        ],
        [
            "Cọc $1\\text{ m}$ bóng $1{,}5\\text{ m}$; cột cờ bóng $15\\text{ m}$. Chiều cao cột cờ là:",
            "10\\text{ m}"
        ],
        [
            "Rút gọn phân thức $\\dfrac{x^2 - 81}{x - 9} =$ (với $x \\ne 9$):",
            "x + 9"
        ]
    ],
    "q11": {
        "a": "\\dfrac{6x + 18}{x^2 - 9}",
        "b": "\\dfrac{x^2 - 64}{(x + 8)^2}",
        "c": "\\dfrac{x^2 - 12x + 36}{3x - 18}",
        "d": "\\dfrac{xy - 6y + 2x - 12}{x^2 - 36}",
        "e": "\\dfrac{x^2 - 9x + 20}{x^2 - 16}",
        "f": "\\dfrac{x^3 - 64}{x^2 + 4x + 16}"
    },
    "q12": {
        "a": "\\dfrac{3x - 2}{4} = \\dfrac{x + 2}{2}",
        "b": "(2x - 10)(x + 6) = 0",
        "c": "\\dfrac{x^2 - 49}{x - 7} = 0",
        "d": "x^2 - 8x + 7 = 0"
    },
    "q13": {
        "de": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 15\\text{ cm}, AC = 20\\text{ cm}$.",
        "a": "Tính độ dài cạnh huyền $BC$.",
        "b": "Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 6\\text{ cm}$. Kẻ đường thẳng qua $D$ song song với $BC$ cắt cạnh $AC$ tại $E$. Tính độ dài các đoạn thẳng $AE$ và $DE$."
    },
    "q14": {
        "de": "Tìm giá trị lớn nhất của biểu thức: $E = \\dfrac{24}{x^2 - 6x + 15}$ với $x \\in \\mathbb{R}$."
    }
}

def make_tikz():
    return r'''\begin{tikzpicture}[scale=0.85, >=stealth, line join=round, line cap=round, font=\footnotesize]
  \coordinate (A) at (0, 0);
  \coordinate (B) at (0, 2.7);
  \coordinate (C) at (3.6, 0);

  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Vuông góc tại A
  \draw (0, 0.22) -- (0.22, 0.22) -- (0.22, 0);

  \fill (A) circle (1.2pt) node[below left=-1pt] {$A$};
  \fill (B) circle (1.2pt) node[left] {$B$};
  \fill (C) circle (1.2pt) node[below] {$C$};
\end{tikzpicture}'''

def format_math(expr):
    expr = expr.strip()
    if expr.startswith('$') and expr.endswith('$'):
        return expr
    return f"${expr}$"

def build_tex(data, vspace_short="1.5mm", ob11=5, ob12=5, dk13=10, dk14=6, vspace_top2="2.2mm", vspace_mid="2.2mm"):
    t_p1 = data["title_p1"]
    t_p2 = data["title_p2"]
    c = data["code"]
    
    preamble = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=2.8,heightSA=0.62}
\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ chuẩn viết tay
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{1.0mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!60}\dotfill}\par%
  }%
  \vspace{0.6mm}%
  \endgroup%
}

% Khu vực bài làm chia 2 cột có vách ngăn mờ ở giữa
\newcommand{\dongkeHaiCot}[1]{%
  \par\vspace{0.5mm}%
  \noindent%
  \begin{minipage}[t]{0.485\linewidth}%
    \dongke{#1}%
  \end{minipage}%
  \hfill%
  {\color{gray!60}\vrule}%
  \hfill%
  \begin{minipage}[t]{0.485\linewidth}%
    \dongke{#1}%
  \end{minipage}%
}

% Định nghĩa ô bài tập tự luận trong bảng
\newcommand{\oBaiTap}[3][5]{%
  \vspace{1.0mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

\begin{document}
\pagestyle{empty}
'''
    content = [preamble]
    
    # --- TRANG 1 ---
    p1 = f'''% =============================================================================
% ========================= MA DE {c} - MAT TRUOC (TRANG 1/2) =============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p1}}} & \\textbf{{Mã đề: {c} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}
'''
    # 10 câu trả lời ngắn
    for i, q in enumerate(data["short"], 1):
        p1 += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q[0]} \\shortans{{{q[1]}}}\\par\\vspace{{{vspace_short}}}\n"
        
    # Câu 11
    q11 = data["q11"]
    p1 += f'''\\vspace{{0.2mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Rút gọn các phân thức đại số sau:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a) (0,5 điểm)}}{{{format_math(q11["a"])}}} & 
\\oBaiTap[{ob11}]{{b) (0,5 điểm)}}{{{format_math(q11["b"])}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c) (0,5 điểm)}}{{{format_math(q11["c"])}}} & 
\\oBaiTap[{ob11}]{{d) (0,5 điểm)}}{{{format_math(q11["d"])}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{e) (0,5 điểm)}}{{{format_math(q11["e"])}}} & 
\\oBaiTap[{ob11}]{{f) (0,5 điểm)}}{{{format_math(q11["f"])}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
'''
    # --- TRANG 2 ---
    q12 = data["q12"]
    q13 = data["q13"]
    q14 = data["q14"]
    tikz_code = make_tikz()
    
    p2 = f'''% =============================================================================
% ========================= MA DE {c} - MAT SAU (TRANG 2/2) ==============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\centering\\textbf{{{t_p2} | Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_top2}}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm $x$, biết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{a) (0,5 điểm)}}{{{format_math(q12["a"])}}} & 
\\oBaiTap[{ob12}]{{b) (0,5 điểm)}}{{{format_math(q12["b"])}}} \\\\
\\hline
\\oBaiTap[{ob12}]{{c) (0,5 điểm)}}{{{format_math(q12["c"])}}} & 
\\oBaiTap[{ob12}]{{d) (0,5 điểm)}}{{{format_math(q12["d"])}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_mid}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.62\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,0 điểm).}} {q13["de"]}\\par\\vspace{{0.3mm}}
\\textbf{{a) (1,0 điểm)}} {q13["a"]}\\par\\vspace{{0.3mm}}
\\textbf{{b) (1,0 điểm)}} {q13["b"]}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.36\\linewidth}}
\\vspace{{0pt}}\\centering
{tikz_code}
\\end{{minipage}}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{{vspace_mid}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (0,5 điểm).}} {q14["de"]}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}
'''
    content.append(p1)
    content.append(p2)
    content.append("\\end{document}\n")
    return "".join(content)

def check_margins(pdf_path):
    doc = pymupdf.open(pdf_path)
    margins = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
        gray = np.mean(img, axis=2) if pix.n >= 3 else img[:,:,0]
        non_white = np.where(gray < 250)
        if len(non_white[0]) > 0:
            last_y = np.max(non_white[0])
            m = ((pix.h - last_y) / 150.0) * 25.4
            margins.append(m)
        else:
            margins.append(0.0)
    doc.close()
    return margins

def render_preview(pdf_path):
    doc = pymupdf.open(pdf_path)
    if len(doc) >= 1:
        pix1 = doc[0].get_pixmap(dpi=150)
        p1 = os.path.join(CUR_DIR, "page_1_ma05.png")
        pix1.save(p1)
        print(f"Rendered {p1}")
    if len(doc) >= 2:
        pix2 = doc[1].get_pixmap(dpi=150)
        p2 = os.path.join(CUR_DIR, "page_2_ma05.png")
        pix2.save(p2)
        print(f"Rendered {p2}")
    doc.close()

def main():
    base_name = data_05["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    # Cấu hình chuẩn Gold Standard
    cfg = ("1.5mm", 5, 5, 10, 6, "2.2mm", "2.2mm")
    vspace_short, ob11, ob12, dk13, dk14, vspace_top2, vspace_mid = cfg
    
    print(f"Generating LaTeX for Mã 05: vspace_short={vspace_short}, ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}")
    tex_content = build_tex(data_05, vspace_short=vspace_short, ob11=ob11, ob12=ob12, dk13=dk13, dk14=dk14, vspace_top2=vspace_top2, vspace_mid=vspace_mid)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    print("Compiling pdflatex (run 1)...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"], cwd=CUR_DIR, capture_output=True)
    print("Compiling pdflatex (run 2)...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"], cwd=CUR_DIR, capture_output=True)
    
    if not os.path.exists(pdf_path):
        print("Compilation failed! PDF not generated.")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    margins = check_margins(pdf_path)
    print(f"Total pages: {num_pages}")
    for idx, m in enumerate(margins):
        p_no = idx + 1
        print(f"Page {idx+1:02d} (Mã 05 - Trang {p_no}/2): bottom margin = {m:.2f} mm")
        
    render_preview(pdf_path)
    
    if num_pages == 2 and all(10.0 <= m <= 15.5 for m in margins):
        print(">>> SUCCESS: Exactly 2 pages and all margins strictly within 10-15 mm! <<<")
    else:
        print("Review margin details above.")

if __name__ == "__main__":
    main()
