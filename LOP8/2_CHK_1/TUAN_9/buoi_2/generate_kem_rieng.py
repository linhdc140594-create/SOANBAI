import json
import os
import subprocess
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de_kem_rieng.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_tex(data, ob1=4, ob2=5):
    t_p1 = data["title_p1"]
    t_p2 = data["title_p2"]
    codes = data["codes"]
    labels = ["a)", "b)", "c)", "d)", "e)", "f)", "g)", "h)", "i)", "j)", "k)", "l)"]
    
    preamble = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.5cm, bottom=0.5cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\setlength{\parskip}{0pt}

% Dong ke cham mo chuan viet tay
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{0.8mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!60}\dotfill}\par%
  }%
  \vspace{0.4mm}%
  \endgroup%
}

% Dinh nghia o bai tap tu luan trong bang
\newcommand{\oBaiTap}[3][4]{%
  \vspace{0.6mm}%
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
        q1_list = cd["q1"]
        q2_list = cd["q2"]
        
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

\\vspace{{1.0mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.25cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}
\\noindent\\textbf{{Câu 1 (5,0 điểm). Thực hiện phép tính (rút gọn nếu có thể):}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
'''
        for row in range(6):
            i1 = row * 2
            i2 = row * 2 + 1
            item1 = f"\\oBaiTap[{ob1}]{{{labels[i1]}}}{{{q1_list[i1]}}}"
            item2 = f"\\oBaiTap[{ob1}]{{{labels[i2]}}}{{{q1_list[i2]}}}"
            p1 += f"{item1} & {item2} \\\\\n\\hline\n"
        p1 += "\\end{tabularx}\n\n\\newpage\n"
        
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

\\vspace{{1.2mm}}
\\noindent\\textbf{{Câu 2 (5,0 điểm). Tìm số thực $x$, biết:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
'''
        for row in range(6):
            i1 = row * 2
            i2 = row * 2 + 1
            item1 = f"\\oBaiTap[{ob2}]{{{labels[i1]}}}{{{q2_list[i1]}}}"
            item2 = f"\\oBaiTap[{ob2}]{{{labels[i2]}}}{{{q2_list[i2]}}}"
            p2 += f"{item1} & {item2} \\\\\n\\hline\n"
        p2 += "\\end{tabularx}\n\n"
        
        if idx < len(code_list) - 1:
            p2 += "\\newpage\n"
            
        content.append(p1)
        content.append(p2)
        
    content.append("\\end{document}\n")
    return "".join(content)

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    # Try combinations of ob1, ob2
    for ob1 in [5, 4]:
        for ob2 in [6, 5]:
            print(f"Testing ob1={ob1}, ob2={ob2}...")
            tex_content = build_tex(data, ob1=ob1, ob2=ob2)
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(tex_content)
                
            cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
            subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            if os.path.exists(pdf_path):
                reader = pypdf.PdfReader(pdf_path)
                num_pages = len(reader.pages)
                print(f"Resulting PDF page count: {num_pages}")
                if num_pages == 8:
                    print(f"SUCCESS with ob1={ob1}, ob2={ob2}! Exactly 8 pages.")
                    return
                else:
                    print(f"Failed: Page count is {num_pages}, expected 8.")

if __name__ == "__main__":
    main()

