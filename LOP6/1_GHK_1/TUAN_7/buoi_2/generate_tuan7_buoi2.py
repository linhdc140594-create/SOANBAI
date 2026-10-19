import os
import subprocess
import pypdf

tex_template = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=2.8,heightSA=0.62}

\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ đều đặn chuẩn viết tay (khoảng cách 6.5mm rộng rãi vừa vặn)
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

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=10, ob12=5, dk13=11, dk14=8):
    res = f'''% =============================================================================
% ========================= TOÁN 6 - TUẦN 07 - BUỔI 02: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 07 - BUỔI 02}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

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
    # 10 câu trả lời ngắn
    for idx, (text, ans) in enumerate(q_short, 1):
        res += f'\\noindent\\textbf{{Câu {idx} (0,25 điểm).}} {text} \\shortans{{{ans}}}\\par\\vspace{{0.3mm}}\n'

    res += f'''\\vspace{{0.4mm}}

\\noindent\\textbf{{Câu 11 (2,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a)}}{{{q11['a']}}} & 
\\oBaiTap[{ob11}]{{b)}}{{{q11['b']}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c)}}{{{q11['c']}}} & 
\\oBaiTap[{ob11}]{{d)}}{{{q11['d']}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
% =============================================================================
% ========================= TOÁN 6 - TUẦN 07 - BUỔI 02: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 6 - TUẦN 07 - BUỔI 02}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số tự nhiên $x$, biết:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{a)}}{{{q12['a']}}} & 
\\oBaiTap[{ob12}]{{b)}}{{{q12['b']}}} \\\\
\\hline
\\oBaiTap[{ob12}]{{c)}}{{{q12['c']}}} & 
\\oBaiTap[{ob12}]{{d)}}{{{q12['d']}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 13 (2,5 điểm).}} {q13['de']}\\par
\\textbf{{a) (1,25 điểm)}} {q13['a']}\\par
\\textbf{{b) (1,25 điểm)}} {q13['b']}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (1,0 điểm).}} {q14['de']}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}

\\newpage

'''
    return res

de_data = {
    '101': {
        'short': [
            ("Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 16 \\le x \\le 55\\}$ có bao nhiêu phần tử?", "40"),
            ("Số La Mã $\\text{XIX}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "19"),
            ("Viết gọn thương $3^8 : 3^3$ dưới dạng một lũy thừa.", "3^5"),
            ("Giá trị của biểu thức $50 - 3 \\cdot 3^2$ bằng bao nhiêu?", "23"),
            ("Số dư của phép chia tổng $(36 + 180 + 22)$ cho $9$ bằng bao nhiêu?", "4"),
            ("Tìm chữ số $x$ để số $\\overline{3x5}$ chia hết cho $9$.", "1"),
            ("Trong các số $17; 21; 25; 27$, số nguyên tố là số nào?", "17"),
            ("Một hình tam giác đều có bao nhiêu trục đối xứng?", "3"),
            ("Tính chu vi mảnh đất hình vuông có cạnh $15\\text{ m}$.", "60\\text{ m}"),
            ("Tính diện tích hình bình hành có đáy $12\\text{ cm}$ và chiều cao $6\\text{ cm}$.", "72\\text{ cm}^2"),
        ],
        'q11': {
            'a': r"$135 - 3^2 \cdot 4 + 2^4 \cdot 5$",
            'b': r"$37 \cdot 64 + 37 \cdot 36 - 700$",
            'c': r"$200 : [66 - (19 - 15)^2]$",
            'd': r"$180 : \{ 75 - [22 + (16 - 14)^3] \}$"
        },
        'q12': {
            'a': r"$3 \cdot x - 14 = 34$",
            'b': r"$75 - 4 \cdot (x - 2) = 43$",
            'c': r"$4 \cdot 3^{x-1} + 14 = 50$",
            'd': r"Tìm số tự nhiên $x$ lớn nhất, biết $36 \ \vdots \ x$ và $54 \ \vdots \ x$."
        },
        'q13': {
            'de': r"Bác Hải có một căn phòng hình chữ nhật có chiều dài $12\text{ m}$ và chiều rộng $8\text{ m}$.",
            'a': r"Tính chu vi và diện tích của căn phòng hình chữ nhật đó.",
            'b': r"Bác Hải dùng những viên gạch men hình vuông có cạnh $40\text{ cm}$ để lát kín nền căn phòng đó. Hỏi bác Hải cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $22\ 000$ đồng, tính tổng số tiền bác Hải phải trả để mua gạch."
        },
        'q14': {
            'de': r"Cho tổng $A = 2 + 2^2 + 2^3 + 2^4 + \dots + 2^{20}$. Chứng minh rằng $A$ chia hết cho $3$."
        }
    },
    '102': {
        'short': [
            ("Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 18 \\le x \\le 67\\}$ có bao nhiêu phần tử?", "50"),
            ("Số La Mã $\\text{XXIII}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "23"),
            ("Viết gọn thương $5^7 : 5^4$ dưới dạng một lũy thừa.", "5^3"),
            ("Giá trị của biểu thức $70 - 4 \\cdot 3^2$ bằng bao nhiêu?", "34"),
            ("Số dư của phép chia tổng $(45 + 270 + 32)$ cho $9$ bằng bao nhiêu?", "5"),
            ("Tìm chữ số $x$ để số $\\overline{4x3}$ chia hết cho $9$.", "2"),
            ("Trong các số $23; 33; 35; 39$, số nguyên tố là số nào?", "23"),
            ("Một hình vuông có bao nhiêu trục đối xứng?", "4"),
            ("Tính chu vi mảnh đất hình vuông có cạnh $18\\text{ m}$.", "72\\text{ m}"),
            ("Tính diện tích hình bình hành có đáy $15\\text{ cm}$ và chiều cao $8\\text{ cm}$.", "120\\text{ cm}^2"),
        ],
        'q11': {
            'a': r"$145 - 2^4 \cdot 3 + 3^3 \cdot 2$",
            'b': r"$43 \cdot 78 + 43 \cdot 22 - 300$",
            'c': r"$240 : [76 - (18 - 14)^2]$",
            'd': r"$220 : \{ 85 - [22 + (17 - 15)^3] \}$"
        },
        'q12': {
            'a': r"$4 \cdot x - 17 = 39$",
            'b': r"$85 - 5 \cdot (x - 3) = 45$",
            'c': r"$3 \cdot 2^{x+2} + 16 = 64$",
            'd': r"Tìm số tự nhiên $x$ lớn nhất, biết $40 \ \vdots \ x$ và $60 \ \vdots \ x$."
        },
        'q13': {
            'de': r"Bác Hải có một căn phòng hình chữ nhật có chiều dài $15\text{ m}$ và chiều rộng $8\text{ m}$.",
            'a': r"Tính chu vi và diện tích của căn phòng hình chữ nhật đó.",
            'b': r"Bác Hải dùng những viên gạch men hình vuông có cạnh $50\text{ cm}$ để lát kín nền căn phòng đó. Hỏi bác Hải cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $32\ 000$ đồng, tính tổng số tiền bác Hải phải trả để mua gạch."
        },
        'q14': {
            'de': r"Cho tổng $B = 3 + 3^2 + 3^3 + 3^4 + \dots + 3^{20}$. Chứng minh rằng $B$ chia hết cho $4$."
        }
    },
    '103': {
        'short': [
            ("Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 12 \\le x \\le 71\\}$ có bao nhiêu phần tử?", "60"),
            ("Số La Mã $\\text{XXVIII}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "28"),
            ("Viết gọn thương $2^9 : 2^5$ dưới dạng một lũy thừa.", "2^4"),
            ("Giá trị của biểu thức $80 - 2 \\cdot 4^2$ bằng bao nhiêu?", "48"),
            ("Số dư của phép chia tổng $(54 + 360 + 25)$ cho $9$ bằng bao nhiêu?", "7"),
            ("Tìm chữ số $x$ để số $\\overline{5x1}$ chia hết cho $9$.", "3"),
            ("Trong các số $29; 39; 49; 51$, số nguyên tố là số nào?", "29"),
            ("Một hình lục giác đều có bao nhiêu đường chéo chính?", "3"),
            ("Tính chu vi mảnh đất hình vuông có cạnh $25\\text{ m}$.", "100\\text{ m}"),
            ("Tính diện tích hình bình hành có đáy $14\\text{ cm}$ và chiều cao $5\\text{ cm}$.", "70\\text{ cm}^2"),
        ],
        'q11': {
            'a': r"$165 - 4^2 \cdot 3 + 2^5 \cdot 2$",
            'b': r"$52 \cdot 83 + 52 \cdot 17 - 200$",
            'c': r"$280 : [86 - (17 - 13)^2]$",
            'd': r"$260 : \{ 95 - [22 + (18 - 16)^3] \}$"
        },
        'q12': {
            'a': r"$5 \cdot x - 16 = 49$",
            'b': r"$95 - 6 \cdot (x - 1) = 47$",
            'c': r"$5 \cdot 2^{x+1} - 18 = 62$",
            'd': r"Tìm số tự nhiên $x$ lớn nhất, biết $42 \ \vdots \ x$ và $70 \ \vdots \ x$."
        },
        'q13': {
            'de': r"Bác Hải có một căn phòng hình chữ nhật có chiều dài $16\text{ m}$ và chiều rộng $9\text{ m}$.",
            'a': r"Tính chu vi và diện tích của căn phòng hình chữ nhật đó.",
            'b': r"Bác Hải dùng những viên gạch men hình vuông có cạnh $40\text{ cm}$ để lát kín nền căn phòng đó. Hỏi bác Hải cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $24\ 000$ đồng, tính tổng số tiền bác Hải phải trả để mua gạch."
        },
        'q14': {
            'de': r"Cho tổng $C = 4 + 4^2 + 4^3 + 4^4 + \dots + 4^{20}$. Chứng minh rằng $C$ chia hết cho $5$."
        }
    },
    '104': {
        'short': [
            ("Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 15 \\le x \\le 84\\}$ có bao nhiêu phần tử?", "70"),
            ("Số La Mã $\\text{XVI}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "16"),
            ("Viết gọn thương $7^6 : 7^2$ dưới dạng một lũy thừa.", "7^4"),
            ("Giá trị của biểu thức $90 - 3 \\cdot 4^2$ bằng bao nhiêu?", "42"),
            ("Số dư của phép chia tổng $(63 + 180 + 42)$ cho $9$ bằng bao nhiêu?", "6"),
            ("Tìm chữ số $x$ để số $\\overline{2x3}$ chia hết cho $9$.", "4"),
            ("Trong các số $31; 45; 55; 57$, số nguyên tố là số nào?", "31"),
            ("Một hình thoi có bao nhiêu cạnh bằng nhau?", "4"),
            ("Tính chu vi mảnh đất hình vuông có cạnh $16\\text{ m}$.", "64\\text{ m}"),
            ("Tính diện tích hình bình hành có đáy $16\\text{ cm}$ và chiều cao $7\\text{ cm}$.", "112\\text{ cm}^2"),
        ],
        'q11': {
            'a': r"$185 - 5^2 \cdot 2 + 3^2 \cdot 6$",
            'b': r"$61 \cdot 74 + 61 \cdot 26 - 100$",
            'c': r"$320 : [96 - (16 - 12)^2]$",
            'd': r"$300 : \{ 105 - [22 + (19 - 17)^3] \}$"
        },
        'q12': {
            'a': r"$6 \cdot x - 19 = 53$",
            'b': r"$90 - 7 \cdot (x - 2) = 41$",
            'c': r"$2 \cdot 5^{x-1} + 10 = 60$",
            'd': r"Tìm số tự nhiên $x$ lớn nhất, biết $48 \ \vdots \ x$ và $72 \ \vdots \ x$."
        },
        'q13': {
            'de': r"Bác Hải có một căn phòng hình chữ nhật có chiều dài $20\text{ m}$ và chiều rộng $9\text{ m}$.",
            'a': r"Tính chu vi và diện tích của căn phòng hình chữ nhật đó.",
            'b': r"Bác Hải dùng những viên gạch men hình vuông có cạnh $50\text{ cm}$ để lát kín nền căn phòng đó. Hỏi bác Hải cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $35\ 000$ đồng, tính tổng số tiền bác Hải phải trả để mua gạch."
        },
        'q14': {
            'de': r"Cho tổng $D = 5 + 5^2 + 5^3 + 5^4 + \dots + 5^{20}$. Chứng minh rằng $D$ chia hết cho $6$."
        }
    }
}

full_tex = tex_template
for ma in ['101', '102', '103', '104']:
    d = de_data[ma]
    full_tex += render_de(ma, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11=10, ob12=5, dk13=11, dk14=8)

full_tex += r'\end{document}' + '\n'

script_dir = os.path.dirname(os.path.abspath(__file__))
tex_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex')
with open(tex_file, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print(f"Generated {tex_file}")

# Biên dịch LaTeX
print("Compiling LaTeX...")
cmd = ["pdflatex", "-interaction=nonstopmode", "Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex"]
proc = subprocess.run(cmd, cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

pdf_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_02.pdf')
if os.path.exists(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    num_pages = len(reader.pages)
    print(f"PDF generated successfully: {pdf_file}")
    print(f"Total pages: {num_pages} (Target: 8 pages)")
    if num_pages == 8:
        print("PERFECT: Exactly 8 pages!")
    else:
        print(f"WARNING: Page count is {num_pages}, expected 8 pages. Adjust spacing!")
else:
    print("Compilation failed, PDF not found.")
    print(proc.stdout[-500:])
