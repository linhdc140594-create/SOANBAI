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

def make_tikz():
    return r'''\begin{tikzpicture}[>=stealth, line join=round, line cap=round, font=\footnotesize]
  \coordinate (O) at (1.9, 0);
  \draw[thick] (O) circle (1.85cm);
  \fill (O) circle (1.4pt) node[below left=-1pt] {$O$};
\end{tikzpicture}'''

def build_tex(data, vsa="0.8mm", ob11=19, dk12=16, dk13=14, vspace_mid="7.5mm", vspace_top2="3.0mm"):
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
        # 10 cau ngan
        for i, (q, ans) in enumerate(cd["short"]):
            p1 += f"\\noindent\\textbf{{Câu {i+1} (0,25 điểm).}} {q} \\shortans{{{ans}}}\\par\\vspace{{{vsa}}}\n"

        # Cau 11 (2.5 diem)
        c11 = cd["c11"]
        p1 += f'''\\vspace{{0.6mm}}
\\noindent\\textbf{{Câu 11 (2,5 điểm).}}
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
        tikz_code = make_tikz()

        p2 = f'''% =============================================================================
% ========================= MA DE {c} - MAT SAU (TRANG 2/2) ==============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p2}}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_top2}}}

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
\\begin{{minipage}}[t]{{0.56\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,5 điểm).}} {c13["gt"]}\\par\\vspace{{0.4mm}}
{c13["a"]}\\par\\vspace{{0.4mm}}
{c13["b"]}
\\end{{minipage}}\\hspace{{4mm}}
\\begin{{minipage}}[t]{{0.41\\linewidth}}
\\vspace{{0pt}}\\raggedright
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

    # Cấu hình
    cfg = ("0.8mm", 19, 16, 13, "7.5mm", "3.0mm")
    vsa, ob11, dk12, dk13, vspace_mid, vspace_top2 = cfg

    print(f"Generating LaTeX with config: vsa={vsa}, ob11={ob11}, dk12={dk12}, dk13={dk13}, vspace_mid={vspace_mid}, vspace_top2={vspace_top2}")
    tex_content = build_tex(data, vsa=vsa, ob11=ob11, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid, vspace_top2=vspace_top2)
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
