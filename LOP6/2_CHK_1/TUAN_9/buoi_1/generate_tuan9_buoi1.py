import json
import os
import subprocess
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_tex(data, ob11=7, ob12_ab=5, ob12_cd=7, dk13=11, dk14=7):
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
        # Page 1
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
            p1 += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q[0]} \\shortans{{{q[1]}}}\\par\\vspace{{0.25mm}}\n"
        
        p1 += f'''
\\vspace{{0.3mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.4mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a)}}{{{cd["q11"]["a"]}}} & \\oBaiTap[{ob11}]{{b)}}{{{cd["q11"]["b"]}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c)}}{{{cd["q11"]["c"]}}} & \\oBaiTap[{ob11}]{{d)}}{{{cd["q11"]["d"]}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{e)}}{{{cd["q11"]["e"]}}} & \\oBaiTap[{ob11}]{{f)}}{{{cd["q11"]["f"]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
'''
        # Page 2
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

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số tự nhiên $x$, biết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12_ab}]{{a)}}{{{cd["q12"]["a"]}}} & \\oBaiTap[{ob12_ab}]{{b)}}{{{cd["q12"]["b"]}}} \\\\
\\hline
\\oBaiTap[{ob12_cd}]{{c)}}{{{cd["q12"]["c"]}}} & \\oBaiTap[{ob12_cd}]{{d)}}{{{cd["q12"]["d"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 13 (2,0 điểm).}} {cd["q13"]["de"]}\\par
\\textbf{{a) (1,0 điểm)}} {cd["q13"]["a"]}\\par
\\textbf{{b) (1,0 điểm)}} {cd["q13"]["b"]}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
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

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    ob11 = 7
    ob12_ab = 5
    ob12_cd = 7
    dk13 = 11
    dk14 = 7
    
    print(f"Generating TeX with ob11={ob11}, ob12_ab={ob12_ab}, ob12_cd={ob12_cd}, dk13={dk13}, dk14={dk14}...")
    tex_content = build_tex(data, ob11=ob11, ob12_ab=ob12_ab, ob12_cd=ob12_cd, dk13=dk13, dk14=dk14)
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
