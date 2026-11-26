import json
import os
import subprocess
import pypdf
import numpy as np
from PIL import Image

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def make_drawing_area():
    return r'''\begin{tikzpicture}
  \draw[gray!60, dashed, rounded corners=3pt] (0, 0) rectangle (8.0, 3.3);
  \node[gray!60, below=1pt] at (4.0, 0) {\footnotesize\textit{(Khu vực vẽ hình)}};
\end{tikzpicture}'''

def build_tex(data, vsa="0.8mm", ob11=19, dk12=15, dk13=14, vspace_mid="2.5mm", vspace_top2="1.5mm"):
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
% ========================= TOAN 9 TUAN 12 BUOI 02 - MA DE {c} =================
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
        drawing_area_code = make_drawing_area()

        p2 = f'''% =============================================================================
% ========================= TOAN 9 TUAN 12 BUOI 02 - MA DE {c} =================
% ========================= TRANG 2/2 ==========================================
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
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk12}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{{vspace_mid}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.54\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,5 điểm).}} {c13["gt"]}\\par\\vspace{{0.4mm}}
{c13["a"]}\\par\\vspace{{0.4mm}}
{c13["b"]}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.44\\linewidth}}
\\vspace{{0pt}}\\centering
{drawing_area_code}
\\end{{minipage}}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk13}}}
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
        # (vsa, ob11, dk12, dk13, vspace_mid, vspace_top2)
        ("0.8mm", 19, 15, 14, "2.5mm", "1.2mm"),
        ("0.8mm", 19, 15, 14, "2.0mm", "1.2mm"),
        ("0.9mm", 19, 15, 14, "2.5mm", "1.2mm"),
        ("0.7mm", 19, 15, 14, "2.5mm", "1.2mm"),
        ("0.8mm", 19, 15, 14, "3.0mm", "1.2mm"),
        ("0.8mm", 19, 14, 14, "4.5mm", "1.5mm"),
        ("0.8mm", 19, 15, 13, "4.5mm", "1.5mm"),
    ]

    best_match = None
    for vsa, ob11, dk12, dk13, vspace_mid, vspace_top2 in candidates:
        print(f"\n--- Testing config: vsa={vsa}, ob11={ob11}, dk12={dk12}, dk13={dk13}, vspace_mid={vspace_mid}, vspace_top2={vspace_top2} ---")
        tex_content = build_tex(data, vsa=vsa, ob11=ob11, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid, vspace_top2=vspace_top2)
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
                if all(10.0 <= m <= 14.5 for m in margins):
                    print(">>> PERFECT! Margins are within the ideal gold standard (10-14.5 mm)!")
                    best_match = (vsa, ob11, dk12, dk13, vspace_mid, vspace_top2)
                    break
                else:
                    print("Page margins tested:", margins)

    if best_match:
        print(f"\nOptimal configuration found: {best_match}")
    else:
        print("\nFinished search.")

if __name__ == "__main__":
    main()
