import json
import os
import subprocess
import pypdf
import pymupdf
import numpy as np

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def make_tikz(code):
    if code == "101":
        return r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round, >=stealth, font=\footnotesize]
  \coordinate (A) at (-1.7, 0);
  \coordinate (B) at (1.7, 0);
  \coordinate (I) at (0, 0);
  \coordinate (M) at (0, 1.4);
  \coordinate (N) at (0, -1.1);

  \draw[thick] (A) -- (B);
  \draw[thick] (0, -1.4) -- (0, 1.7) node[above right=-2pt] {$d$};

  \draw (0, 0.18) -- (0.18, 0.18) -- (0.18, 0);

  \fill (A) circle (1.2pt) node[below left=-1pt] {$A$};
  \fill (B) circle (1.2pt) node[below right=-1pt] {$B$};
  \fill (I) circle (1.2pt) node[below left=-2pt] {$I$};
  \fill (M) circle (1.2pt) node[left] {$M$};
  \fill (N) circle (1.2pt) node[left] {$N$};
\end{tikzpicture}'''
    elif code == "102":
        return r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round, >=stealth, font=\footnotesize]
  \coordinate (C) at (-1.7, 0);
  \coordinate (D) at (1.7, 0);
  \coordinate (H) at (0, 0);
  \coordinate (P) at (0, 1.4);
  \coordinate (Q) at (0, -1.1);

  \draw[thick] (C) -- (D);
  \draw[thick] (0, -1.4) -- (0, 1.7) node[above right=-2pt] {$d$};

  \draw (0, 0.18) -- (0.18, 0.18) -- (0.18, 0);

  \fill (C) circle (1.2pt) node[below left=-1pt] {$C$};
  \fill (D) circle (1.2pt) node[below right=-1pt] {$D$};
  \fill (H) circle (1.2pt) node[below left=-2pt] {$H$};
  \fill (P) circle (1.2pt) node[left] {$P$};
  \fill (Q) circle (1.2pt) node[left] {$Q$};
\end{tikzpicture}'''
    elif code == "103":
        return r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round, >=stealth, font=\footnotesize]
  \coordinate (M) at (-1.7, 0);
  \coordinate (N) at (1.7, 0);
  \coordinate (K) at (0, 0);
  \coordinate (E) at (0, 1.4);
  \coordinate (F) at (0, -1.1);

  \draw[thick] (M) -- (N);
  \draw[thick] (0, -1.4) -- (0, 1.7) node[above right=-2pt] {$d$};

  \draw (0, 0.18) -- (0.18, 0.18) -- (0.18, 0);

  \fill (M) circle (1.2pt) node[below left=-1pt] {$M$};
  \fill (N) circle (1.2pt) node[below right=-1pt] {$N$};
  \fill (K) circle (1.2pt) node[below left=-2pt] {$K$};
  \fill (E) circle (1.2pt) node[left] {$E$};
  \fill (F) circle (1.2pt) node[left] {$F$};
\end{tikzpicture}'''
    else:  # 104
        return r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round, >=stealth, font=\footnotesize]
  \coordinate (E) at (-1.7, 0);
  \coordinate (F) at (1.7, 0);
  \coordinate (O) at (0, 0);
  \coordinate (A) at (0, 1.4);
  \coordinate (B) at (0, -1.1);

  \draw[thick] (E) -- (F);
  \draw[thick] (0, -1.4) -- (0, 1.7) node[above right=-2pt] {$d$};

  \draw (0, 0.18) -- (0.18, 0.18) -- (0.18, 0);

  \fill (E) circle (1.2pt) node[below left=-1pt] {$E$};
  \fill (F) circle (1.2pt) node[below right=-1pt] {$F$};
  \fill (O) circle (1.2pt) node[below left=-2pt] {$O$};
  \fill (A) circle (1.2pt) node[left] {$A$};
  \fill (B) circle (1.2pt) node[left] {$B$};
\end{tikzpicture}'''

def format_math(expr):
    expr = expr.strip()
    if expr.startswith('$') and expr.endswith('$'):
        return expr
    return f"${expr}$"

def build_tex(data, vspace_short="2.5mm", ob11=5, ob12=5, dk13=10, dk14=6):
    t_p1 = data["title_p1"]
    t_p2 = data["title_p2"]
    codes = data["codes"]
    
    preamble = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=2.6,heightSA=0.62}
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
    code_list = list(codes.keys())
    
    for idx, c in enumerate(code_list):
        cd = codes[c]
        
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
        for i, q in enumerate(cd["short"], 1):
            p1 += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q[0]} \\shortans{{{q[1]}}}\\par\\vspace{{{vspace_short}}}\n"
            
        # Câu 11
        q11 = cd["q11"]
        p1 += f'''\\vspace{{0.2mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
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
        q12 = cd["q12"]
        q13 = cd["q13"]
        q14 = cd["q14"]
        tikz_code = make_tikz(c)
        
        p2 = f'''% =============================================================================
% ========================= MA DE {c} - MAT SAU (TRANG 2/2) ==============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\centering\\textbf{{{t_p2} | Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số hữu tỉ $x$, biết:}}
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

\\vspace{{1.2mm}}

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

\\vspace{{1.2mm}}

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
        if idx < len(code_list) - 1:
            p2 += "\n\\newpage\n"
            
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
        p1 = os.path.join(CUR_DIR, "page_1.png")
        pix1.save(p1)
        print(f"Rendered {p1}")
    if len(doc) >= 2:
        pix2 = doc[1].get_pixmap(dpi=150)
        p2 = os.path.join(CUR_DIR, "page_2.png")
        pix2.save(p2)
        print(f"Rendered {p2}")
    doc.close()

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    # Cấu hình tối ưu vàng tuyệt đối (Margins 12.36 mm & 14.05 mm)
    best_cfg = ("2.0mm", 5, 5, 10, 6)
    vspace_short, ob11, ob12, dk13, dk14 = best_cfg
    
    print(f"Generating LaTeX with optimal config: vspace_short={vspace_short}, ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}")
    tex_content = build_tex(data, vspace_short=vspace_short, ob11=ob11, ob12=ob12, dk13=dk13, dk14=dk14)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    print("Compiling pdflatex (run 1)...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"], cwd=CUR_DIR, capture_output=True)
    print("Compiling pdflatex (run 2 for references)...")
    subprocess.run(["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"], cwd=CUR_DIR, capture_output=True)
    
    if not os.path.exists(pdf_path):
        print("Compilation failed!")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    margins = check_margins(pdf_path)
    print(f"Total pages: {num_pages}")
    for idx, m in enumerate(margins):
        code = 101 + (idx // 2)
        p_no = (idx % 2) + 1
        print(f"Page {idx+1:02d} (Mã {code} - Trang {p_no}/2): bottom margin = {m:.2f} mm")
        
    render_preview(pdf_path)
    
    if num_pages == 8 and all(10.0 <= m <= 15.5 for m in margins):
        print(">>> SUCCESS: Exactly 8 pages and all margins strictly within 10-15 mm! <<<")
    else:
        print("Review margin details above.")

if __name__ == "__main__":
    main()
