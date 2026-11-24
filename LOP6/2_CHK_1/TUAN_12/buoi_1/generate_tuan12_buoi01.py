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

def format_math(expr):
    expr = expr.strip()
    if expr.startswith('$') and expr.endswith('$'):
        return expr
    return f"${expr}$"

def build_tex(data, ob11=7, vsa="0.25mm", ob12_ab=5, ob12_cd=6, dk13=10, dk14=7):
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

% Định nghĩa ô bài tập tự luận trong bảng
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
\\centering\\textbf{{Điểm số}} & \\centering\\textbf{{Lời nhận xét của thầy cô}} \\tabularnewline
\\rule{{0pt}}{{1.8cm}} & \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}
'''
        for i, q in enumerate(cd["short"], 1):
            p1 += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q[0]} \\shortans{{{q[1]}}}\\par\\vspace{{{vsa}}}\n"
        
        p1 += f'''
\\vspace{{0.3mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.4mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a)}}{{{format_math(cd["q11"]["a"])}}} & \\oBaiTap[{ob11}]{{b)}}{{{format_math(cd["q11"]["b"])}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c)}}{{{format_math(cd["q11"]["c"])}}} & \\oBaiTap[{ob11}]{{d)}}{{{format_math(cd["q11"]["d"])}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{e)}}{{{format_math(cd["q11"]["e"])}}} & \\oBaiTap[{ob11}]{{f)}}{{{format_math(cd["q11"]["f"])}}} \\\\
\\hline
\\end{{tabularx}}
\\newpage
'''
        # --- TRANG 2 ---
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

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số nguyên $x$, biết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12_ab}]{{a)}}{{{format_math(cd["q12"]["a"])}}} & \\oBaiTap[{ob12_ab}]{{b)}}{{{format_math(cd["q12"]["b"])}}} \\\\
\\hline
\\oBaiTap[{ob12_cd}]{{c)}}{{{format_math(cd["q12"]["c"])}}} & \\oBaiTap[{ob12_cd}]{{d)}}{{{cd["q12"]["d"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.4mm}}
\\textbf{{Câu 13 (2,0 điểm).}} {cd["q13"]["de"]}\\par\\vspace{{0.3mm}}
\\textbf{{a) (1,0 điểm)}} {cd["q13"]["a"]}\\par\\vspace{{0.3mm}}
\\textbf{{b) (1,0 điểm)}} {cd["q13"]["b"]}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.4mm}}
\\textbf{{Câu 14 (0,5 điểm).}} {cd["q14"]["de"]}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}
'''
        if idx < len(code_list) - 1:
            p2 += "\n\\newpage\n"
        
        content.append(p1)
        content.append(p2)
        
    content.append("\\end{document}\n")
    return "".join(content)

def check_pdf_margins(pdf_path):
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

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    # Cấu hình tối ưu chuẩn vàng
    cfg = {"ob11": 7, "vsa": "0.25mm", "ob12_ab": 5, "ob12_cd": 6, "dk13": 9, "dk14": 8}
    
    print(f"Generating TeX with config: {cfg}...")
    tex_content = build_tex(data, **cfg)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
    print("Compiling pdflatex (run 1)...")
    subprocess.run(cmd, cwd=CUR_DIR, capture_output=True)
    print("Compiling pdflatex (run 2 for references)...")
    subprocess.run(cmd, cwd=CUR_DIR, capture_output=True)
    
    if not os.path.exists(pdf_path):
        print("Compilation error! Check log.")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    margins = check_pdf_margins(pdf_path)
    print(f"Total pages: {num_pages}")
    for idx, m in enumerate(margins):
        code = 101 + (idx // 2)
        p_no = (idx % 2) + 1
        print(f"Page {idx+1:02d} (Mã {code} - Trang {p_no}/2): bottom margin = {m:.2f} mm")
    
    # Render preview pngs for Mã 101 (Trang 1 và Trang 2)
    doc = pymupdf.open(pdf_path)
    for p_no in range(min(2, num_pages)):
        pix = doc[p_no].get_pixmap(dpi=150)
        out_img = os.path.join(CUR_DIR, f"page_{p_no+1}.png")
        pix.save(out_img)
        print(f"Rendered {out_img}")
    doc.close()
    
    if num_pages == 8 and all(10.0 <= m <= 15.5 for m in margins):
        print(">>> SUCCESS: Exactly 8 pages and all margins within 10-15 mm! <<<")
    else:
        print("Review margin details above.")

if __name__ == "__main__":
    main()
