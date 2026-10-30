import json
import os
import subprocess
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_tikz_buoi2():
    return r'''\begin{tikzpicture}[scale=0.68, >=stealth, line join=round, line cap=round]
  \coordinate (A) at (-2, 0);
  \coordinate (B) at (2, 0);
  \coordinate (O) at (0, 0);
  \coordinate (C) at (1, 1.732);
  \coordinate (H) at (1, 0);
  \coordinate (M) at (-0.5, 0.866);
  \draw[thick] (-2, 0) -- (2, 0);
  \draw[thick] (2, 0) arc (0:180:2);
  \draw[thick] (-2, 0) -- (1, 1.732) -- (2, 0);
  \draw[thick] (1, 1.732) -- (1, 0);
  \draw[thick, dashed] (0, 0) -- (-0.5, 0.866);
  \draw[thick, dashed] (1, 1.732) -- (0, 0);
  \draw (1, 0.2) -- (1.2, 0.2) -- (1.2, 0);
  \fill (A) circle (1.2pt) node[below left=-1pt] {$A$};
  \fill (B) circle (1.2pt) node[below right=-1pt] {$B$};
  \fill (O) circle (1.2pt) node[below=-1pt] {$O$};
  \fill (C) circle (1.2pt) node[above right=-1pt] {$C$};
  \fill (H) circle (1.2pt) node[below=-1pt] {$H$};
  \fill (M) circle (1.2pt) node[above left=-1pt] {$M$};
\end{tikzpicture}'''

def build_tex(data, vsa="0.6mm", ob11=20, dk12=16, dk13=16, vspace_mid="1.2mm"):
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

\SAOPTN{widthSA=3.2,heightSA=0.62}
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

% Dinh nghia o bai tap tu luan trong bang
\newcommand{\oBaiTap}[3][6]{%
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
% ========================= TOAN 9 TUAN 09 BUOI 02 - MA DE {c} =================
% ========================= TRANG 1/2 ==========================================
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
        # 10 cau ngan
        for i, (q, ans) in enumerate(cd["short"]):
            p1 += f"\\noindent\\textbf{{Câu {i+1} (0,25 điểm).}} {q} \\shortans{{{ans}}}\\par\\vspace{{{vsa}}}\n"
        
        # Cau 11
        c11 = cd["c11"]
        p1 += f'''\\vspace{{0.8mm}}
\\noindent\\textbf{{Câu 11 (2,5 điểm). Đại số tổng hợp:}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{{c11[0][0]}}}{{{c11[0][1]}}} & 
\\oBaiTap[{ob11}]{{{c11[1][0]}}}{{{c11[1][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
'''
        # --- TRANG 2 ---
        c12 = cd["c12"]
        c13 = cd["c13"]
        tikz_code = get_tikz_buoi2()
        
        p2 = f'''% =============================================================================
% ========================= TOAN 9 TUAN 09 BUOI 02 - MA DE {c} =================
% ========================= TRANG 2/2 ==========================================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p2}}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 12 (2,5 điểm).}} {c12}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk12}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{{vspace_mid}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.64\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,5 điểm).}} {c13["gt"]}\\par\\vspace{{0.4mm}}
{c13["a"]}\\par\\vspace{{0.4mm}}
{c13["b"]}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.34\\linewidth}}
\\vspace{{0pt}}\\centering
{tikz_code}
\\end{{minipage}}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
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
    
    vsa = "0.6mm"
    ob11 = 20
    dk12 = 16
    dk13 = 16
    vspace_mid = "1.2mm"
    
    print(f"Generating TeX with vsa={vsa}, ob11={ob11}, dk12={dk12}, dk13={dk13}...")
    tex_content = build_tex(data, vsa=vsa, ob11=ob11, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid)
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
