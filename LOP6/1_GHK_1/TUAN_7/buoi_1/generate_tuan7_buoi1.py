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
% ========================= TOÁN 6 - TUẦN 07 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 07 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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
% ========================= TOÁN 6 - TUẦN 07 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 6 - TUẦN 07 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
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
            ("Tập hợp $A = \\{x \\in \\mathbb{N} \\mid 12 \\le x \\le 45\\}$ có bao nhiêu phần tử?", "34"),
            ("Số La Mã $\\text{XXIV}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "24"),
            ("Viết gọn tích $2^3 \\cdot 2^5$ dưới dạng một lũy thừa.", "2^8"),
            ("Giá trị của biểu thức $30 - 2 \\cdot 3^2$ bằng bao nhiêu?", "12"),
            ("Số dư của phép chia tổng $(45 + 120 + 23)$ cho $5$ bằng bao nhiêu?", "3"),
            ("Tìm chữ số $x$ lớn nhất để số $\\overline{23x}$ chia hết cho $3$.", "7"),
            ("Trong các số $11; 15; 21; 27$, số nguyên tố là số nào?", "11"),
            ("Một hình lục giác đều có bao nhiêu đường chéo chính?", "3"),
            ("Tính chu vi hình chữ nhật có kích thước $15\\text{ m} \\times 8\\text{ m}$.", "46\\text{ m}"),
            ("Tính diện tích hình thoi có hai đường chéo $8\\text{ cm}$ và $10\\text{ cm}$.", "40\\text{ cm}^2")
        ],
        'q11': {
            'a': '$145 - 2^3 \\cdot 5 + 3^2 \\cdot 4$',
            'b': '$48 \\cdot 67 + 48 \\cdot 33 - 800$',
            'c': '$180 : [45 - (18 - 15)^2]$',
            'd': '$250 : \\{ 90 - [32 + (14 - 12)^3] \\}$'
        },
        'q12': {
            'a': '$4 \\cdot x + 15 = 47$',
            'b': '$85 - 3 \\cdot (x + 4) = 40$',
            'c': '$3 \\cdot 2^{x+1} - 12 = 36$',
            'd': 'Tìm số tự nhiên $x$ lớn nhất, biết $24 \\ \\vdots \\ x$ và $36 \\ \\vdots \\ x$.'
        },
        'q13': {
            'de': 'Bác An có một mảnh sân hình chữ nhật có chiều dài $16\\text{ m}$ và chiều rộng $10\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh sân hình chữ nhật đó.',
            'b': 'Bác An dùng những viên gạch hình vuông có cạnh $40\\text{ cm}$ để lát kín mảnh sân đó. Hỏi bác An cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $25\\ 000$ đồng, tính tổng số tiền bác An phải trả để mua gạch.'
        },
        'q14': {
            'de': 'Cho tổng $A = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{21}$. Chứng minh rằng $A$ chia hết cho $4$.'
        }
    },
    '102': {
        'short': [
            ("Tập hợp $A = \\{x \\in \\mathbb{N} \\mid 15 \\le x \\le 58\\}$ có bao nhiêu phần tử?", "44"),
            ("Số La Mã $\\text{XXVII}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "27"),
            ("Viết gọn tích $3^2 \\cdot 3^4$ dưới dạng một lũy thừa.", "3^6"),
            ("Giá trị của biểu thức $40 - 3 \\cdot 2^3$ bằng bao nhiêu?", "16"),
            ("Số dư của phép chia tổng $(35 + 150 + 24)$ cho $5$ bằng bao nhiêu?", "4"),
            ("Tìm chữ số $x$ lớn nhất để số $\\overline{34x}$ chia hết cho $3$.", "8"),
            ("Trong các số $13; 25; 33; 35$, số nguyên tố là số nào?", "13"),
            ("Một hình lục giác đều có bao nhiêu cạnh bằng nhau?", "6"),
            ("Tính chu vi hình chữ nhật có kích thước $16\\text{ m} \\times 7\\text{ m}$.", "46\\text{ m}"),
            ("Tính diện tích hình thoi có hai đường chéo $6\\text{ cm}$ và $12\\text{ cm}$.", "36\\text{ cm}^2")
        ],
        'q11': {
            'a': '$155 - 2^4 \\cdot 3 + 4^2 \\cdot 2$',
            'b': '$56 \\cdot 72 + 56 \\cdot 28 - 600$',
            'c': '$210 : [58 - (19 - 15)^2]$',
            'd': '$300 : \\{ 100 - [32 + (15 - 13)^3] \\}$'
        },
        'q12': {
            'a': '$5 \\cdot x + 18 = 53$',
            'b': '$95 - 4 \\cdot (x + 3) = 47$',
            'c': '$2 \\cdot 3^{x+1} - 15 = 39$',
            'd': 'Tìm số tự nhiên $x$ lớn nhất, biết $30 \\ \\vdots \\ x$ và $45 \\ \\vdots \\ x$.'
        },
        'q13': {
            'de': 'Bác Bình có một mảnh sân hình chữ nhật có chiều dài $18\\text{ m}$ và chiều rộng $10\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh sân hình chữ nhật đó.',
            'b': 'Bác Bình dùng những viên gạch hình vuông có cạnh $50\\text{ cm}$ để lát kín mảnh sân đó. Hỏi bác Bình cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $35\\ 000$ đồng, tính tổng số tiền bác Bình phải trả để mua gạch.'
        },
        'q14': {
            'de': 'Cho tổng $B = 1 + 4 + 4^2 + 4^3 + \\dots + 4^{21}$. Chứng minh rằng $B$ chia hết cho $5$.'
        }
    },
    '103': {
        'short': [
            ("Tập hợp $A = \\{x \\in \\mathbb{N} \\mid 18 \\le x \\le 62\\}$ có bao nhiêu phần tử?", "45"),
            ("Số La Mã $\\text{XXIX}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "29"),
            ("Viết gọn tích $5^2 \\cdot 5^3$ dưới dạng một lũy thừa.", "5^5"),
            ("Giá trị của biểu thức $50 - 4 \\cdot 2^3$ bằng bao nhiêu?", "18"),
            ("Số dư của phép chia tổng $(65 + 140 + 32)$ cho $5$ bằng bao nhiêu?", "2"),
            ("Tìm chữ số $x$ lớn nhất để số $\\overline{45x}$ chia hết cho $3$.", "9"),
            ("Trong các số $17; 27; 39; 49$, số nguyên tố là số nào?", "17"),
            ("Một hình lục giác đều có bao nhiêu góc ở các đỉnh bằng nhau?", "6"),
            ("Tính chu vi hình chữ nhật có kích thước $18\\text{ m} \\times 6\\text{ m}$.", "48\\text{ m}"),
            ("Tính diện tích hình thoi có hai đường chéo $8\\text{ cm}$ và $14\\text{ cm}$.", "56\\text{ cm}^2")
        ],
        'q11': {
            'a': '$165 - 3^3 \\cdot 2 + 5^2 \\cdot 3$',
            'b': '$64 \\cdot 75 + 64 \\cdot 25 - 400$',
            'c': '$220 : [69 - (21 - 16)^2]$',
            'd': '$350 : \\{ 110 - [32 + (16 - 14)^3] \\}$'
        },
        'q12': {
            'a': '$6 \\cdot x + 14 = 56$',
            'b': '$90 - 5 \\cdot (x + 2) = 45$',
            'c': '$4 \\cdot 2^{x+2} - 18 = 46$',
            'd': 'Tìm số tự nhiên $x$ lớn nhất, biết $28 \\ \\vdots \\ x$ và $42 \\ \\vdots \\ x$.'
        },
        'q13': {
            'de': 'Bác Cường có một mảnh sân hình chữ nhật có chiều dài $20\\text{ m}$ và chiều rộng $12\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh sân hình chữ nhật đó.',
            'b': 'Bác Cường dùng những viên gạch hình vuông có cạnh $40\\text{ cm}$ để lát kín mảnh sân đó. Hỏi bác Cường cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $20\\ 000$ đồng, tính tổng số tiền bác Cường phải trả để mua gạch.'
        },
        'q14': {
            'de': 'Cho tổng $C = 1 + 5 + 5^2 + 5^3 + \\dots + 5^{21}$. Chứng minh rằng $C$ chia hết cho $6$.'
        }
    },
    '104': {
        'short': [
            ("Tập hợp $A = \\{x \\in \\mathbb{N} \\mid 14 \\le x \\le 69\\}$ có bao nhiêu phần tử?", "56"),
            ("Số La Mã $\\text{XXVI}$ có giá trị trong hệ thập phân bằng bao nhiêu?", "26"),
            ("Viết gọn tích $2^4 \\cdot 2^3$ dưới dạng một lũy thừa.", "2^7"),
            ("Giá trị của biểu thức $60 - 5 \\cdot 2^3$ bằng bao nhiêu?", "20"),
            ("Số dư của phép chia tổng $(75 + 160 + 41)$ cho $5$ bằng bao nhiêu?", "1"),
            ("Tìm chữ số $x$ lớn nhất để số $\\overline{16x}$ chia hết cho $3$.", "8"),
            ("Trong các số $19; 35; 45; 51$, số nguyên tố là số nào?", "19"),
            ("Một hình thoi có bao nhiêu cặp cạnh đối diện song song với nhau?", "2"),
            ("Tính chu vi hình chữ nhật có kích thước $20\\text{ m} \\times 7\\text{ m}$.", "54\\text{ m}"),
            ("Tính diện tích hình thoi có hai đường chéo $10\\text{ cm}$ và $12\\text{ cm}$.", "60\\text{ cm}^2")
        ],
        'q11': {
            'a': '$175 - 2^5 \\cdot 2 + 3^3 \\cdot 3$',
            'b': '$72 \\cdot 81 + 72 \\cdot 19 - 200$',
            'c': '$240 : [84 - (23 - 17)^2]$',
            'd': '$400 : \\{ 120 - [32 + (17 - 15)^3] \\}$'
        },
        'q12': {
            'a': '$7 \\cdot x + 16 = 65$',
            'b': '$100 - 6 \\cdot (x + 1) = 52$',
            'c': '$5 \\cdot 3^{x-1} + 15 = 60$',
            'd': 'Tìm số tự nhiên $x$ lớn nhất, biết $32 \\ \\vdots \\ x$ và $48 \\ \\vdots \\ x$.'
        },
        'q13': {
            'de': 'Bác Dũng có một mảnh sân hình chữ nhật có chiều dài $25\\text{ m}$ và chiều rộng $10\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh sân hình chữ nhật đó.',
            'b': 'Bác Dũng dùng những viên gạch hình vuông có cạnh $50\\text{ cm}$ để lát kín mảnh sân đó. Hỏi bác Dũng cần bao nhiêu viên gạch (bỏ qua mép vữa)? Biết mỗi viên gạch có giá $30\\ 000$ đồng, tính tổng số tiền bác Dũng phải trả để mua gạch.'
        },
        'q14': {
            'de': 'Cho tổng $D = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{21}$. Chứng minh rằng $D$ chia hết cho $3$.'
        }
    }
}

full_tex = tex_template
for ma in ['101', '102', '103', '104']:
    d = de_data[ma]
    full_tex += render_de(ma, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11=10, ob12=5, dk13=11, dk14=8)

full_tex += r'\end{document}' + '\n'

script_dir = os.path.dirname(os.path.abspath(__file__))
tex_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_01.tex')

with open(tex_file, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print(f"Generated {tex_file}")

# Biên dịch LaTeX
print("Compiling LaTeX...")
cmd = ["pdflatex", "-interaction=nonstopmode", "Phieu_Kiem_Tra_Tuan_07_Buoi_01.tex"]
proc = subprocess.run(cmd, cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

pdf_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_01.pdf')
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
