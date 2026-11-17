import json
import os
import subprocess
import pypdf
import pymupdf

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

def build_tex(data, ob11=7, vsa="0.25mm", ob12_ab=5, ob12_cd=6, dk13=11, dk14=7):
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
\\oBaiTap[{ob12_cd}]{{c)}}{{{format_math(cd["q12"]["c"])}}} & \\oBaiTap[{ob12_cd}]{{d)}}{{{format_math(cd["q12"]["d"])}}} \\\\
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
        rects = page.get_drawings()
        max_y = max([r['rect'].y1 for r in rects]) if rects else 0
        margin_bottom_mm = (841.89 - max_y) * 25.4 / 72
        margins.append(margin_bottom_mm)
    return margins

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    # Cấu hình tối ưu chuẩn vàng: lề dưới 10.2mm - 10.7mm khít mép giấy cả 2 mặt
    cfg = {"ob11": 7, "vsa": "0.25mm", "ob12_ab": 5, "ob12_cd": 6, "dk13": 12, "dk14": 8}
    
    print(f"Generating TeX with optimal config: {cfg}...")
    tex_content = build_tex(data, **cfg)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
    print("Compiling pdflatex (run 1)...")
    subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Compiling pdflatex (run 2 for stable references)...")
    subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if not os.path.exists(pdf_path):
        print("Compilation error!")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    margins = check_pdf_margins(pdf_path)
    print(f"Total pages: {num_pages}")
    print(f"Bottom margins (mm): {[round(m, 1) for m in margins]}")
    
    if num_pages == 8:
        print(">>> SUCCESS: Exactly 8 pages and perfect margins! <<<")
    else:
        print(f"WARNING: Page count is {num_pages}, expected 8!")

if __name__ == "__main__":
    main()
