import json
import os
import subprocess
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_tex(data, n_b1=6, n_b2=5, n_b3=5, n_b4=6, n_b5a=3, n_b5b=4, n_b5c=5):
    codes = ["101", "102", "103", "104"]
    
    preamble = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

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
    
    for idx, c in enumerate(codes):
        cd = data[c]
        # Page 1
        p1 = f'''% =============================================================================
% ========================= MA DE {c} - MAT TRUOC (TRANG 1/2) =============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU RÈN LUYỆN CHUYÊN ĐỀ TOÁN 6 - CÂU 11 \\& CÂU 12}} & \\textbf{{Mã đề: {c} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.0cm}}|p{{3.0cm}}|X|}}
\\hline
\\centering\\textbf{{Điểm Câu 11}} & \\centering\\textbf{{Điểm Câu 12}} & \\centering\\textbf{{Lời nhận xét của thầy cô}} \\tabularnewline
\\rule{{0pt}}{{1.8cm}} & & \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Bài 1 (2,0 điểm). Tính một cách hợp lý (nếu có thể):}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{n_b1}]{{a)}}{{{cd["bai1"]["a"]}}} & \\oBaiTap[{n_b1}]{{b)}}{{{cd["bai1"]["b"]}}} \\\\
\\hline
\\oBaiTap[{n_b1}]{{c)}}{{{cd["bai1"]["c"]}}} & \\oBaiTap[{n_b1}]{{d)}}{{{cd["bai1"]["d"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Bài 2 (3,0 điểm). Thực hiện phép tính:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{n_b2}]{{a)}}{{{cd["bai2"]["a"]}}} & \\oBaiTap[{n_b2}]{{b)}}{{{cd["bai2"]["b"]}}} \\\\
\\hline
\\oBaiTap[{n_b2}]{{c)}}{{{cd["bai2"]["c"]}}} & \\oBaiTap[{n_b2}]{{d)}}{{{cd["bai2"]["d"]}}} \\\\
\\hline
\\oBaiTap[{n_b2}]{{e)}}{{{cd["bai2"]["e"]}}} & \\oBaiTap[{n_b2}]{{f)}}{{{cd["bai2"]["f"]}}} \\\\
\\hline
\\end{{tabularx}}
\\newpage
'''
        # Page 2
        p2 = f'''% =============================================================================
% ========================= MA DE {c} - MAT SAU (TRANG 2/2) ==============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|r|}}
\\hline
\\textbf{{TOÁN 6 - CHUYÊN ĐỀ CÂU 11 \\& CÂU 12}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Bài 3 (2,0 điểm). Tìm số tự nhiên $x$, biết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{n_b3}]{{a)}}{{{cd["bai3"]["a"]}}} & \\oBaiTap[{n_b3}]{{b)}}{{{cd["bai3"]["b"]}}} \\\\
\\hline
\\oBaiTap[{n_b3}]{{c)}}{{{cd["bai3"]["c"]}}} & \\oBaiTap[{n_b3}]{{d)}}{{{cd["bai3"]["d"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Bài 4 (1,5 điểm). Tìm số tự nhiên $x$ chứa lũy thừa:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|X|}}
\\hline
\\oBaiTap[{n_b4}]{{a)}}{{{cd["bai4"]["a"]}}} & \\oBaiTap[{n_b4}]{{b)}}{{{cd["bai4"]["b"]}}} & \\oBaiTap[{n_b4}]{{c)}}{{{cd["bai4"]["c"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Bài 5 (1,5 điểm). Tìm số nguyên $x$ \\& Bài toán chia hết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\oBaiTap[{n_b5a}]{{a)}}{{{cd["bai5"]["a"]}}} \\\\
\\hline
\\oBaiTap[{n_b5b}]{{b)}}{{{cd["bai5"]["b"]}}} \\\\
\\hline
\\oBaiTap[{n_b5c}]{{c)}}{{{cd["bai5"]["c"]}}} \\\\
\\hline
\\end{{tabularx}}
'''
        if idx < len(codes) - 1:
            p2 += "\\newpage\n\n"
        else:
            p2 += "\n\\end{document}\n"
            
        content.append(p1)
        content.append(p2)
        
    return "".join(content)

def compile_pdf(tex_path):
    print("Compiling LaTeX to PDF...")
    cmd = ["pdflatex", "-interaction=nonstopmode", os.path.basename(tex_path)]
    work_dir = os.path.dirname(tex_path)
    res = subprocess.run(cmd, cwd=work_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf_path = tex_path.replace(".tex", ".pdf")
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        print(f"Generated PDF successfully: {len(reader.pages)} pages.")
        return len(reader.pages)
    else:
        print("Compilation failed!")
        return -1

def main():
    data = load_data()
    tex_file = os.path.join(CUR_DIR, "Phieu_Chuyen_De_Cau_11_12.tex")
    
    # Optimal parameters for exactly 8 pages and 12-14mm margins
    tex_str = build_tex(data, n_b1=6, n_b2=5, n_b3=5, n_b4=6, n_b5a=3, n_b5b=4, n_b5c=5)
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(tex_str)
        
    pages = compile_pdf(tex_file)
    print(f"Initial pages: {pages}")

if __name__ == "__main__":
    main()
