import json
import os
import subprocess
import pypdf
import numpy as np

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de_co_ban.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_tex(data, ob1=5, ob2=5, vspace_p2="1.5mm"):
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

% Dinh nghia o bai tap tu luan trong bang cho Trang 1 va Trang 2
\newcommand{\oBaiTapMot}[3][4]{%
  \vspace{2.8mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}
\newcommand{\oBaiTapHai}[3][5]{%
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
        q1 = cd["q1"]
        q2 = cd["q2"]
        
        # --- TRANG 1 ---
        p1 = f'''% =============================================================================
% ========================= MA DE {c} - TRANG 1/2 =============================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p1}}} & \\textbf{{Mã đề: {c} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{2.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{2.2mm}}
\\noindent\\textbf{{Câu 1 (5,0 điểm). Thực hiện các phép tính sau:}}
\\vspace{{1.0mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTapMot[{ob1}]{{a) (0,4 điểm)}}{{{q1["a"]}}} & 
\\oBaiTapMot[{ob1}]{{b) (0,4 điểm)}}{{{q1["b"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{c) (0,4 điểm)}}{{{q1["c"]}}} & 
\\oBaiTapMot[{ob1}]{{d) (0,4 điểm)}}{{{q1["d"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{e) (0,4 điểm)}}{{{q1["e"]}}} & 
\\oBaiTapMot[{ob1}]{{f) (0,4 điểm)}}{{{q1["f"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{g) (0,4 điểm)}}{{{q1["g"]}}} & 
\\oBaiTapMot[{ob1}]{{h) (0,4 điểm)}}{{{q1["h"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{i) (0,4 điểm)}}{{{q1["i"]}}} & 
\\oBaiTapMot[{ob1}]{{j) (0,4 điểm)}}{{{q1["j"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{k) (0,5 điểm)}}{{{q1["k"]}}} & 
\\oBaiTapMot[{ob1}]{{l) (0,5 điểm)}}{{{q1["l"]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
'''
        # --- TRANG 2 ---
        p2 = f'''% =============================================================================
% ========================= MA DE {c} - TRANG 2/2 =============================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p2}}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_p2}}}
\\noindent\\textbf{{Câu 2 (5,0 điểm). Phân tích các đa thức sau thành nhân tử:}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTapHai[{ob2}]{{a) (0,4 điểm)}}{{{q2["a"]}}} & 
\\oBaiTapHai[{ob2}]{{b) (0,4 điểm)}}{{{q2["b"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{c) (0,4 điểm)}}{{{q2["c"]}}} & 
\\oBaiTapHai[{ob2}]{{d) (0,4 điểm)}}{{{q2["d"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{e) (0,4 điểm)}}{{{q2["e"]}}} & 
\\oBaiTapHai[{ob2}]{{f) (0,4 điểm)}}{{{q2["f"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{g) (0,4 điểm)}}{{{q2["g"]}}} & 
\\oBaiTapHai[{ob2}]{{h) (0,4 điểm)}}{{{q2["h"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{i) (0,4 điểm)}}{{{q2["i"]}}} & 
\\oBaiTapHai[{ob2}]{{j) (0,4 điểm)}}{{{q2["j"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{k) (0,5 điểm)}}{{{q2["k"]}}} & 
\\oBaiTapHai[{ob2}]{{l) (0,5 điểm)}}{{{q2["l"]}}} \\\\
\\hline
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
    pix1.save(os.path.join(CUR_DIR, "page_co_ban_1.png"))
    pix2 = doc[1].get_pixmap(dpi=150)
    pix2.save(os.path.join(CUR_DIR, "page_co_ban_2.png"))
    print("Exported page_co_ban_1.png and page_co_ban_2.png successfully.")
    
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
        (4, 5, "2.0mm"),
        (4, 5, "2.5mm"),
        (4, 5, "3.0mm"),
        (4, 5, "3.5mm"),
        (4, 5, "4.0mm"),
    ]
    
    best_config = None
    best_margins = None
    best_score = float('inf')
    
    for ob1, ob2, vspace_p2 in candidates:
        print(f"\n--- Testing config: ob1={ob1}, ob2={ob2}, vspace_p2={vspace_p2} ---")
        tex_content = build_tex(data, ob1=ob1, ob2=ob2, vspace_p2=vspace_p2)
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
                score = sum(abs(m - 12.5) for m in margins)
                if all(10.0 <= m <= 15.0 for m in margins):
                    print(">>> PERFECT! Margins are within the ideal gold standard (10-15 mm)!")
                    return
                if score < best_score:
                    best_score = score
                    best_config = (ob1, ob2, vspace_p2)
                    best_margins = margins
            
    if best_config:
        print(f"\n>>> Applying best found 8-page config: {best_config} with margins {best_margins}")
        ob1, ob2, vspace_p2 = best_config
        tex_content = build_tex(data, ob1=ob1, ob2=ob2, vspace_p2=vspace_p2)
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(tex_content)
        cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
        subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        check_margins(pdf_path)
    else:
        print("Optimization completed.")

if __name__ == "__main__":
    main()
