import json
import os
import subprocess
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_tikz_buoi2(c):
    if c == "101":
        return r'''\begin{tikzpicture}[scale=0.70, >=stealth, line join=round, line cap=round]
  \coordinate (B) at (-1.6, 0);
  \coordinate (C) at (1.6, 0);
  \coordinate (M) at (0, 0);
  \coordinate (A) at (0, 2.4);
  \coordinate (I) at (0.8, 1.2);
  \coordinate (K) at (1.6, 2.4);
  \draw[thick] (B) -- (A) -- (K) -- (C) -- cycle;
  \draw[thick] (A) -- (M);
  \draw[thick] (A) -- (C);
  \draw[thick, dashed] (M) -- (K);
  \draw (0, 0.2) -- (0.2, 0.2) -- (0.2, 0);
  \fill (A) circle (1.2pt) node[above left=-1pt] {$A$};
  \fill (B) circle (1.2pt) node[below left=-1pt] {$B$};
  \fill (C) circle (1.2pt) node[below right=-1pt] {$C$};
  \fill (M) circle (1.2pt) node[below=-1pt] {$M$};
  \fill (I) circle (1.2pt) node[above left=-1pt] {$I$};
  \fill (K) circle (1.2pt) node[above right=-1pt] {$K$};
\end{tikzpicture}'''
    elif c == "102":
        return r'''\begin{tikzpicture}[scale=0.70, >=stealth, line join=round, line cap=round]
  \coordinate (B) at (-1.6, 0);
  \coordinate (C) at (1.6, 0);
  \coordinate (M) at (0, 0);
  \coordinate (A) at (0, 2.4);
  \coordinate (H) at (-0.8, 1.2);
  \coordinate (E) at (-1.6, 2.4);
  \draw[thick] (C) -- (A) -- (E) -- (B) -- cycle;
  \draw[thick] (A) -- (M);
  \draw[thick] (A) -- (B);
  \draw[thick, dashed] (M) -- (E);
  \draw (0, 0.2) -- (-0.2, 0.2) -- (-0.2, 0);
  \fill (A) circle (1.2pt) node[above right=-1pt] {$A$};
  \fill (B) circle (1.2pt) node[below left=-1pt] {$B$};
  \fill (C) circle (1.2pt) node[below right=-1pt] {$C$};
  \fill (M) circle (1.2pt) node[below=-1pt] {$M$};
  \fill (H) circle (1.2pt) node[above right=-1pt] {$H$};
  \fill (E) circle (1.2pt) node[above left=-1pt] {$E$};
\end{tikzpicture}'''
    elif c == "103":
        return r'''\begin{tikzpicture}[scale=0.70, >=stealth, line join=round, line cap=round]
  \coordinate (N) at (-1.6, 0);
  \coordinate (P) at (1.6, 0);
  \coordinate (I) at (0, 0);
  \coordinate (M) at (0, 2.4);
  \coordinate (K) at (0.8, 1.2);
  \coordinate (E) at (1.6, 2.4);
  \draw[thick] (N) -- (M) -- (E) -- (P) -- cycle;
  \draw[thick] (M) -- (I);
  \draw[thick] (M) -- (P);
  \draw[thick, dashed] (I) -- (E);
  \draw (0, 0.2) -- (0.2, 0.2) -- (0.2, 0);
  \fill (M) circle (1.2pt) node[above left=-1pt] {$M$};
  \fill (N) circle (1.2pt) node[below left=-1pt] {$N$};
  \fill (P) circle (1.2pt) node[below right=-1pt] {$P$};
  \fill (I) circle (1.2pt) node[below=-1pt] {$I$};
  \fill (K) circle (1.2pt) node[above left=-1pt] {$K$};
  \fill (E) circle (1.2pt) node[above right=-1pt] {$E$};
\end{tikzpicture}'''
    else:
        return r'''\begin{tikzpicture}[scale=0.70, >=stealth, line join=round, line cap=round]
  \coordinate (E) at (-1.6, 0);
  \coordinate (F) at (1.6, 0);
  \coordinate (I) at (0, 0);
  \coordinate (D) at (0, 2.4);
  \coordinate (H) at (-0.8, 1.2);
  \coordinate (G) at (-1.6, 2.4);
  \draw[thick] (F) -- (D) -- (G) -- (E) -- cycle;
  \draw[thick] (D) -- (I);
  \draw[thick] (D) -- (E);
  \draw[thick, dashed] (I) -- (G);
  \draw (0, 0.2) -- (-0.2, 0.2) -- (-0.2, 0);
  \fill (D) circle (1.2pt) node[above right=-1pt] {$D$};
  \fill (E) circle (1.2pt) node[below left=-1pt] {$E$};
  \fill (F) circle (1.2pt) node[below right=-1pt] {$F$};
  \fill (I) circle (1.2pt) node[below=-1pt] {$I$};
  \fill (H) circle (1.2pt) node[above right=-1pt] {$H$};
  \fill (G) circle (1.2pt) node[above left=-1pt] {$G$};
\end{tikzpicture}'''

def build_tex(data, vspace_short="2.3mm", ob11=5, ob12=5, dk13=11, dk14=7):
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

% Dong ke cham mo chuan viet tay
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

% Khu vuc bai lam chia 2 cot co vach ngan mo o giua
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

% Dinh nghia o bai tap tu luan trong bang
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
% ========================= TOAN 8 TUAN 09 BUOI 02 - MA DE {c} =================
% ========================= TRANG 1/2 ==========================================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p1}}} & \\textbf{{Mã đề: {c} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.4mm}}
'''
        # 10 cau ngan
        for i, (q, ans) in enumerate(cd["short"]):
            p1 += f"\\noindent\\textbf{{Câu {i+1} (0,25 điểm).}} {q} \\shortans{{{ans}}}\\par\\vspace{{{vspace_short}}}\n"
        
        # Cau 11
        q11 = cd["q11"]
        p1 += f'''\\vspace{{0.2mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính và phân tích đa thức thành nhân tử:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a) (0,5 điểm)}}{{{q11["a"]}}} & 
\\oBaiTap[{ob11}]{{b) (0,5 điểm)}}{{{q11["b"]}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c) (0,5 điểm)}}{{{q11["c"]}}} & 
\\oBaiTap[{ob11}]{{d) (0,5 điểm)}}{{{q11["d"]}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{e) (0,5 điểm)}}{{{q11["e"]}}} & 
\\oBaiTap[{ob11}]{{f) (0,5 điểm)}}{{{q11["f"]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
'''
        # --- TRANG 2 ---
        q12 = cd["q12"]
        q13 = cd["q13"]
        q14 = cd["q14"]
        tikz_code = get_tikz_buoi2(c)
        
        p2 = f'''% =============================================================================
% ========================= TOAN 8 TUAN 09 BUOI 02 - MA DE {c} =================
% ========================= TRANG 2/2 ==========================================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p2}}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.4mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số thực $x$, biết:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{a) (0,5 điểm)}}{{{q12["a"]}}} & 
\\oBaiTap[{ob12}]{{b) (0,5 điểm)}}{{{q12["b"]}}} \\\\
\\hline
\\oBaiTap[{ob12}]{{c) (0,5 điểm)}}{{{q12["c"]}}} & 
\\oBaiTap[{ob12}]{{d) (0,5 điểm)}}{{{q12["d"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.4mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.64\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,0 điểm).}} {q13["de"]}\\par\\vspace{{0.4mm}}
\\textbf{{a)}} {q13["a"]}\\par\\vspace{{0.4mm}}
\\textbf{{b)}} {q13["b"]}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.34\\linewidth}}
\\vspace{{0pt}}\\centering
{tikz_code}
\\end{{minipage}}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.4mm}}

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

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    vspace_short = "2.3mm"
    ob11 = 6
    ob12 = 5
    dk13 = 11
    dk14 = 7
    
    print(f"Generating TeX with vspace_short={vspace_short}, ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}...")
    tex_content = build_tex(data, vspace_short=vspace_short, ob11=ob11, ob12=ob12, dk13=dk13, dk14=dk14)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    print("Compiling pdflatex...")
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
    res = subprocess.run(cmd, cwd=CUR_DIR, capture_output=True, text=True)
    
    if not os.path.exists(pdf_path):
        print("Compilation failed! Log:")
        print(res.stdout[-2000:])
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    print(f"Resulting PDF page count: {num_pages}")
    
    if num_pages == 8:
        print("SUCCESS! Exactly 8 pages.")
    else:
        print(f"WARNING: Page count is {num_pages}, expected 8!")

if __name__ == "__main__":
    main()

