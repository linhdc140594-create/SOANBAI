import json
import os
import subprocess
import pypdf
import numpy as np

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def make_tikz(code):
    if code == "101":
        return r'''\begin{tikzpicture}[scale=0.72, >=stealth, line join=round, line cap=round]
  \coordinate (B) at (0, 0);
  \coordinate (C) at (4.0, 0);
  \coordinate (A) at (1.2, 2.7);
  \coordinate (D) at (0.6, 1.35);
  \coordinate (E) at (2.6, 1.35);
  \coordinate (F) at (4.6, 1.35);

  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[thick] (D) -- (F);
  \draw[thick] (A) -- (F) -- (C);
  \draw[dashed] (D) -- (C);

  % Vach danh dau trung diem AD = DB
  \draw (0.22, 0.73) -- (0.38, 0.67);
  \draw (0.82, 2.08) -- (0.98, 2.02);

  % Vach danh dau ED = EF
  \draw (1.55, 1.25) -- (1.55, 1.45);
  \draw (1.65, 1.25) -- (1.65, 1.45);
  \draw (3.55, 1.25) -- (3.55, 1.45);
  \draw (3.65, 1.25) -- (3.65, 1.45);

  \fill (A) circle (1.3pt) node[above] {$A$};
  \fill (B) circle (1.3pt) node[below left=-1pt] {$B$};
  \fill (C) circle (1.3pt) node[below right=-1pt] {$C$};
  \fill (D) circle (1.3pt) node[left] {$D$};
  \fill (E) circle (1.3pt) node[above left=-1pt] {$E$};
  \fill (F) circle (1.3pt) node[right] {$F$};
\end{tikzpicture}'''
    elif code == "102":
        return r'''\begin{tikzpicture}[scale=0.72, >=stealth, line join=round, line cap=round]
  \coordinate (N) at (0, 0);
  \coordinate (P) at (4.0, 0);
  \coordinate (M) at (1.2, 2.7);
  \coordinate (D) at (0.6, 1.35);
  \coordinate (E) at (2.6, 1.35);
  \coordinate (F) at (4.6, 1.35);

  \draw[thick] (M) -- (N) -- (P) -- cycle;
  \draw[thick] (D) -- (F);
  \draw[thick] (M) -- (F) -- (P);
  \draw[dashed] (D) -- (P);

  % Vach danh dau trung diem MD = DN
  \draw (0.22, 0.73) -- (0.38, 0.67);
  \draw (0.82, 2.08) -- (0.98, 2.02);

  % Vach danh dau ED = EF
  \draw (1.55, 1.25) -- (1.55, 1.45);
  \draw (1.65, 1.25) -- (1.65, 1.45);
  \draw (3.55, 1.25) -- (3.55, 1.45);
  \draw (3.65, 1.25) -- (3.65, 1.45);

  \fill (M) circle (1.3pt) node[above] {$M$};
  \fill (N) circle (1.3pt) node[below left=-1pt] {$N$};
  \fill (P) circle (1.3pt) node[below right=-1pt] {$P$};
  \fill (D) circle (1.3pt) node[left] {$D$};
  \fill (E) circle (1.3pt) node[above left=-1pt] {$E$};
  \fill (F) circle (1.3pt) node[right] {$F$};
\end{tikzpicture}'''
    elif code == "103":
        return r'''\begin{tikzpicture}[scale=0.72, >=stealth, line join=round, line cap=round]
  \coordinate (B) at (0, 0);
  \coordinate (C) at (4.0, 0);
  \coordinate (A) at (1.2, 2.7);
  \coordinate (M) at (0.6, 1.35);
  \coordinate (N) at (2.6, 1.35);
  \coordinate (P) at (4.6, 1.35);

  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[thick] (M) -- (P);
  \draw[thick] (A) -- (P) -- (C);
  \draw[dashed] (M) -- (C);

  % Vach danh dau trung diem AM = MB
  \draw (0.22, 0.73) -- (0.38, 0.67);
  \draw (0.82, 2.08) -- (0.98, 2.02);

  % Vach danh dau NM = NP
  \draw (1.55, 1.25) -- (1.55, 1.45);
  \draw (1.65, 1.25) -- (1.65, 1.45);
  \draw (3.55, 1.25) -- (3.55, 1.45);
  \draw (3.65, 1.25) -- (3.65, 1.45);

  \fill (A) circle (1.3pt) node[above] {$A$};
  \fill (B) circle (1.3pt) node[below left=-1pt] {$B$};
  \fill (C) circle (1.3pt) node[below right=-1pt] {$C$};
  \fill (M) circle (1.3pt) node[left] {$M$};
  \fill (N) circle (1.3pt) node[above left=-1pt] {$N$};
  \fill (P) circle (1.3pt) node[right] {$P$};
\end{tikzpicture}'''
    else:  # 104
        return r'''\begin{tikzpicture}[scale=0.72, >=stealth, line join=round, line cap=round]
  \coordinate (E) at (0, 0);
  \coordinate (F) at (4.0, 0);
  \coordinate (D) at (1.2, 2.7);
  \coordinate (M) at (0.6, 1.35);
  \coordinate (N) at (2.6, 1.35);
  \coordinate (P) at (4.6, 1.35);

  \draw[thick] (D) -- (E) -- (F) -- cycle;
  \draw[thick] (M) -- (P);
  \draw[thick] (D) -- (P) -- (F);
  \draw[dashed] (M) -- (F);

  % Vach danh dau trung diem DM = ME
  \draw (0.22, 0.73) -- (0.38, 0.67);
  \draw (0.82, 2.08) -- (0.98, 2.02);

  % Vach danh dau NM = NP
  \draw (1.55, 1.25) -- (1.55, 1.45);
  \draw (1.65, 1.25) -- (1.65, 1.45);
  \draw (3.55, 1.25) -- (3.55, 1.45);
  \draw (3.65, 1.25) -- (3.65, 1.45);

  \fill (D) circle (1.3pt) node[above] {$D$};
  \fill (E) circle (1.3pt) node[below left=-1pt] {$E$};
  \fill (F) circle (1.3pt) node[below right=-1pt] {$F$};
  \fill (M) circle (1.3pt) node[left] {$M$};
  \fill (N) circle (1.3pt) node[above left=-1pt] {$N$};
  \fill (P) circle (1.3pt) node[right] {$P$};
\end{tikzpicture}'''

def build_tex(data, vspace_short="1.8mm", ob11=6, ob12=5, dk13=11, dk14=7):
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

\SAOPTN{widthSA=2.8,heightSA=0.62}
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
% ========================= TOAN 8 TUAN 11 BUOI 01 - MA DE {c} =================
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
            p1 += f"\\noindent\\textbf{{Câu {i+1} (0,25 điểm).}} {q} \\shortans{{{ans}}}\\par\\vspace{{{vspace_short}}}\n"
        
        # Cau 11
        q11 = cd["q11"]
        p1 += f'''\\vspace{{0.2mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Phân tích các đa thức sau thành nhân tử:}}
\\vspace{{0.6mm}}

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
        tikz_code = make_tikz(c)
        
        p2 = f'''% =============================================================================
% ========================= TOAN 8 TUAN 11 BUOI 01 - MA DE {c} =================
% ========================= TRANG 2/2 ==========================================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p2}}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm $x$, biết:}}
\\vspace{{0.6mm}}

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

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.68\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,0 điểm).}} {q13["de"]}\\par\\vspace{{0.4mm}}
\\textbf{{a)}} {q13["a"]}\\par\\vspace{{0.4mm}}
\\textbf{{b)}} {q13["b"]}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.30\\linewidth}}
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
    import pymupdf
    import numpy as np
    from PIL import Image

    doc = pymupdf.open(pdf_path)
    print(f"Total pages: {len(doc)}")
    
    # Render preview images for page 1 and page 2
    pix1 = doc[0].get_pixmap(dpi=150)
    pix1.save(os.path.join(CUR_DIR, "page_1.png"))
    pix2 = doc[1].get_pixmap(dpi=150)
    pix2.save(os.path.join(CUR_DIR, "page_2.png"))
    print("Exported page_1.png and page_2.png successfully.")
    
    # Measure bottom margins of page 1 and page 2
    margins = []
    for page_idx in range(min(2, len(doc))):
        pix = doc[page_idx].get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples).convert("L")
        arr = np.array(img)
        h, w = arr.shape
        non_white = np.where(arr < 250)[0]
        if len(non_white) > 0:
            last_row = non_white[-1]
            margin_bottom_px = h - last_row
            margin_bottom_mm = (margin_bottom_px / 150) * 25.4
            print(f"Page {page_idx+1} bottom margin: {margin_bottom_mm:.2f} mm")
            margins.append(margin_bottom_mm)
    return margins

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    candidates = [
        ("1.8mm", 6, 5, 11, 7),
        ("1.7mm", 6, 5, 11, 7),
        ("1.6mm", 6, 5, 11, 7),
        ("1.5mm", 6, 5, 11, 7),
    ]
    
    for vspace_short, ob11, ob12, dk13, dk14 in candidates:
        print(f"\n--- Testing config: vspace_short={vspace_short}, ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14} ---")
        tex_content = build_tex(data, vspace_short=vspace_short, ob11=ob11, ob12=ob12, dk13=dk13, dk14=dk14)
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(tex_content)
            
        cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
        subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(pdf_path):
            reader = pypdf.PdfReader(pdf_path)
            num_pages = len(reader.pages)
            print(f"-> Result: {num_pages} pages")
            if num_pages == 8:
                print(">>> SUCCESS! Exactly 8 pages! Checking margins...")
                margins = check_margins(pdf_path)
                if all(10.0 <= m <= 15.0 for m in margins):
                    print(">>> PERFECT! Margins are within the ideal gold standard (10-15 mm)!")
                    return
                else:
                    print("Page margins tested:", margins)
            
    print("Optimization completed.")

if __name__ == "__main__":
    main()
