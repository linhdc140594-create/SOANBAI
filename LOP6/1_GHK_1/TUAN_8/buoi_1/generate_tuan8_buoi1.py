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

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=5, ob12=5, dk13=10, dk14=7):
    res = f'''% =============================================================================
% ========================= TOÁN 6 - TUẦN 08 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 08 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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

\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
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
\\oBaiTap[{ob11}]{{e)}}{{{q11['e']}}} & 
\\oBaiTap[{ob11}]{{f)}}{{{q11['f']}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
% =============================================================================
% ========================= TOÁN 6 - TUẦN 08 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 6 - TUẦN 08 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
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
\\textbf{{Câu 13 (1,5 điểm).}} {q13['de']}\\par
\\textbf{{a) (0,75 điểm)}} {q13['a']}\\par
\\textbf{{b) (0,75 điểm)}} {q13['b']}\\par
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
            (r'Tập hợp $A = \{x \in \mathbb{N} \mid 10 \le x \le 45\}$ có bao nhiêu phần tử?', '36'),
            (r'Số La Mã $\text{XXVIII}$ có giá trị trong hệ thập phân là bao nhiêu?', '28'),
            (r'Viết gọn tích $3^4 \cdot 3^3$ dưới dạng một lũy thừa.', '3^7'),
            (r'Giá trị của biểu thức $50 - 3 \cdot 2^3$ bằng bao nhiêu?', '26'),
            (r'Số dư của phép chia tổng $(35 + 120 + 43)$ cho $5$ là bao nhiêu?', '3'),
            (r'Tìm chữ số $x$ để số $\overline{45x}$ chia hết cho $9$ ($x > 0$).', '9'),
            (r'Trong các số $13; 21; 27; 35$, số nguyên tố là số nào?', '13'),
            (r'Một hình lục giác đều có bao nhiêu đường chéo chính?', '3'),
            (r'Một mảnh đất hình thoi có độ dài cạnh là $12\text{ m}$. Chu vi là:', r'48\text{ m}'),
            (r'Mảnh bìa hình thoi có hai đường chéo là $10\text{ cm}$ và $14\text{ cm}$. Diện tích là:', r'70\text{ cm}^2'),
        ],
        'q11': {
            'a': r'145 - 2^3 \cdot 5 + 3^2 \cdot 4',
            'b': r'38 + 147 + 62 + 53',
            'c': r'48 \cdot 67 + 48 \cdot 33 - 800',
            'd': r'180 : (25 - 7) + 3^2 \cdot 5',
            'e': r'180 : [45 - (18 - 15)^2]',
            'f': r'250 : \{ 90 - [32 + (14 - 12)^3] \}',
        },
        'q12': {
            'a': r'4 \cdot x + 15 = 47',
            'b': r'85 - 3 \cdot (x + 4) = 40',
            'c': r'3 \cdot 2^{x+1} - 12 = 36',
            'd': r'\text{Tìm } x \text{ lớn nhất biết } 24 \ \vdots \ x \text{ và } 36 \ \vdots \ x',
        },
        'q13': {
            'de': r'Bác Ba có một mảnh vườn trồng rau hình chữ nhật có chiều dài $15\text{ m}$ và chiều rộng $8\text{ m}$. Bác Ba dự định làm hàng rào lưới thép bao quanh khu vườn (chừa lại cổng ra vào rộng $2\text{ m}$).',
            'a': r'Tính chu vi và diện tích của mảnh vườn.',
            'b': r'Biết chi phí làm mỗi mét hàng rào là $120.000$ đồng. Hỏi bác Ba phải trả bao nhiêu tiền làm hàng rào?',
        },
        'q14': {
            'de': r'Cho tổng $A = 1 + 3 + 3^2 + 3^3 + \dots + 3^{21}$. Chứng minh rằng $A$ chia hết cho $4$.',
        }
    },
    '102': {
        'short': [
            (r'Tập hợp $A = \{x \in \mathbb{N} \mid 12 \le x \le 55\}$ có bao nhiêu phần tử?', '44'),
            (r'Số La Mã $\text{XXIV}$ có giá trị trong hệ thập phân là bao nhiêu?', '24'),
            (r'Viết gọn tích $2^5 \cdot 2^4$ dưới dạng một lũy thừa.', '2^9'),
            (r'Giá trị của biểu thức $60 - 4 \cdot 3^2$ bằng bao nhiêu?', '24'),
            (r'Số dư của phép chia tổng $(45 + 130 + 54)$ cho $5$ là bao nhiêu?', '4'),
            (r'Tìm chữ số $x$ lớn nhất để số $\overline{32x}$ chia hết cho $3$.', '7'),
            (r'Trong các số $17; 25; 33; 49$, số nguyên tố là số nào?', '17'),
            (r'Một hình lục giác đều có bao nhiêu cạnh bằng nhau?', '6'),
            (r'Một mảnh đất hình thoi có độ dài cạnh là $15\text{ m}$. Chu vi là:', r'60\text{ m}'),
            (r'Mảnh bìa hình thoi có hai đường chéo là $12\text{ cm}$ và $15\text{ cm}$. Diện tích là:', r'90\text{ cm}^2'),
        ],
        'q11': {
            'a': r'155 - 2^4 \cdot 3 + 4^2 \cdot 2',
            'b': r'46 + 138 + 54 + 62',
            'c': r'56 \cdot 72 + 56 \cdot 28 - 600',
            'd': r'160 : (24 - 8) + 4^2 \cdot 3',
            'e': r'210 : [58 - (19 - 15)^2]',
            'f': r'300 : \{ 100 - [32 + (15 - 13)^3] \}',
        },
        'q12': {
            'a': r'5 \cdot x + 18 = 53',
            'b': r'95 - 4 \cdot (x + 3) = 47',
            'c': r'2 \cdot 3^{x+1} - 15 = 39',
            'd': r'\text{Tìm } x \text{ lớn nhất biết } 30 \ \vdots \ x \text{ và } 45 \ \vdots \ x',
        },
        'q13': {
            'de': r'Bác Ba có một mảnh vườn trồng rau hình chữ nhật có chiều dài $16\text{ m}$ và chiều rộng $9\text{ m}$. Bác Ba dự định làm hàng rào lưới thép bao quanh khu vườn (chừa lại cổng ra vào rộng $2\text{ m}$).',
            'a': r'Tính chu vi và diện tích của mảnh vườn.',
            'b': r'Biết chi phí làm mỗi mét hàng rào là $150.000$ đồng. Hỏi bác Ba phải trả bao nhiêu tiền làm hàng rào?',
        },
        'q14': {
            'de': r'Cho tổng $B = 1 + 4 + 4^2 + 4^3 + \dots + 4^{21}$. Chứng minh rằng $B$ chia hết cho $5$.',
        }
    },
    '103': {
        'short': [
            (r'Tập hợp $A = \{x \in \mathbb{N} \mid 15 \le x \le 63\}$ có bao nhiêu phần tử?', '49'),
            (r'Số La Mã $\text{XXIX}$ có giá trị trong hệ thập phân là bao nhiêu?', '29'),
            (r'Viết gọn tích $5^3 \cdot 5^4$ dưới dạng một lũy thừa.', '5^7'),
            (r'Giá trị của biểu thức $70 - 2 \cdot 4^2$ bằng bao nhiêu?', '38'),
            (r'Số dư của phép chia tổng $(55 + 140 + 62)$ cho $5$ là bao nhiêu?', '2'),
            (r'Tìm chữ số $x$ lớn nhất để số $\overline{51x}$ chia hết cho $3$.', '9'),
            (r'Trong các số $19; 39; 51; 57$, số nguyên tố là số nào?', '19'),
            (r'Một hình lục giác đều có bao nhiêu góc ở các đỉnh bằng nhau?', '6'),
            (r'Một mảnh đất hình thoi có độ dài cạnh là $14\text{ m}$. Chu vi là:', r'56\text{ m}'),
            (r'Mảnh bìa hình thoi có hai đường chéo là $8\text{ cm}$ và $16\text{ cm}$. Diện tích là:', r'64\text{ cm}^2'),
        ],
        'q11': {
            'a': r'165 - 3^3 \cdot 2 + 5^2 \cdot 3',
            'b': r'29 + 154 + 71 + 46',
            'c': r'64 \cdot 75 + 64 \cdot 25 - 400',
            'd': r'210 : (27 - 6) + 5^2 \cdot 2',
            'e': r'220 : [69 - (21 - 16)^2]',
            'f': r'350 : \{ 110 - [32 + (16 - 14)^3] \}',
        },
        'q12': {
            'a': r'6 \cdot x + 14 = 56',
            'b': r'90 - 5 \cdot (x + 2) = 45',
            'c': r'4 \cdot 2^{x+2} - 18 = 46',
            'd': r'\text{Tìm } x \text{ lớn nhất biết } 28 \ \vdots \ x \text{ và } 42 \ \vdots \ x',
        },
        'q13': {
            'de': r'Bác Ba có một mảnh vườn trồng rau hình chữ nhật có chiều dài $18\text{ m}$ và chiều rộng $10\text{ m}$. Bác Ba dự định làm hàng rào lưới thép bao quanh khu vườn (chừa lại cổng ra vào rộng $2\text{ m}$).',
            'a': r'Tính chu vi và diện tích của mảnh vườn.',
            'b': r'Biết chi phí làm mỗi mét hàng rào là $140.000$ đồng. Hỏi bác Ba phải trả bao nhiêu tiền làm hàng rào?',
        },
        'q14': {
            'de': r'Cho tổng $C = 1 + 5 + 5^2 + 5^3 + \dots + 5^{21}$. Chứng minh rằng $C$ chia hết cho $6$.',
        }
    },
    '104': {
        'short': [
            (r'Tập hợp $A = \{x \in \mathbb{N} \mid 18 \le x \le 72\}$ có bao nhiêu phần tử?', '55'),
            (r'Số La Mã $\text{XXVII}$ có giá trị trong hệ thập phân là bao nhiêu?', '27'),
            (r'Viết gọn tích $7^2 \cdot 7^5$ dưới dạng một lũy thừa.', '7^7'),
            (r'Giá trị của biểu thức $80 - 5 \cdot 2^3$ bằng bao nhiêu?', '40'),
            (r'Số dư của phép chia tổng $(65 + 150 + 71)$ cho $5$ là bao nhiêu?', '1'),
            (r'Tìm chữ số $x$ để số $\overline{63x}$ chia hết cho $9$ ($x > 0$).', '9'),
            (r'Trong các số $23; 35; 45; 63$, số nguyên tố là số nào?', '23'),
            (r'Một hình vuông có bao nhiêu trục đối xứng?', '4'),
            (r'Một mảnh đất hình thoi có độ dài cạnh là $16\text{ m}$. Chu vi là:', r'64\text{ m}'),
            (r'Mảnh bìa hình thoi có hai đường chéo là $14\text{ cm}$ và $18\text{ cm}$. Diện tích là:', r'126\text{ cm}^2'),
        ],
        'q11': {
            'a': r'175 - 2^5 \cdot 2 + 3^3 \cdot 3',
            'b': r'37 + 165 + 63 + 35',
            'c': r'72 \cdot 81 + 72 \cdot 19 - 200',
            'd': r'240 : (29 - 5) + 6^2 \cdot 2',
            'e': r'240 : [84 - (23 - 17)^2]',
            'f': r'400 : \{ 120 - [32 + (17 - 15)^3] \}',
        },
        'q12': {
            'a': r'7 \cdot x + 16 = 65',
            'b': r'100 - 6 \cdot (x + 1) = 52',
            'c': r'5 \cdot 3^{x-1} + 15 = 60',
            'd': r'\text{Tìm } x \text{ lớn nhất biết } 32 \ \vdots \ x \text{ và } 48 \ \vdots \ x',
        },
        'q13': {
            'de': r'Bác Ba có một mảnh vườn trồng rau hình chữ nhật có chiều dài $20\text{ m}$ và chiều rộng $11\text{ m}$. Bác Ba dự định làm hàng rào lưới thép bao quanh khu vườn (chừa lại cổng ra vào rộng $2\text{ m}$).',
            'a': r'Tính chu vi và diện tích của mảnh vườn.',
            'b': r'Biết chi phí làm mỗi mét hàng rào là $130.000$ đồng. Hỏi bác Ba phải trả bao nhiêu tiền làm hàng rào?',
        },
        'q14': {
            'de': r'Cho tổng $D = 1 + 2 + 2^2 + 2^3 + \dots + 2^{23}$. Chứng minh rằng $D$ chia hết cho $3$.',
        }
    }
}

def generate_pdf(ob11=5, ob12=5, dk13=10, dk14=7):
    content = tex_template
    for ma_de in ['101', '102', '103', '104']:
        d = de_data[ma_de]
        content += render_de(ma_de, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11, ob12, dk13, dk14)
    content += r'\end{document}'

    tex_path = 'Phieu_Kiem_Tra_Tuan_08_Buoi_01.tex'
    pdf_path = 'Phieu_Kiem_Tra_Tuan_08_Buoi_01.pdf'

    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Compiling {tex_path} with ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}...")
    cmd = ['pdflatex', '-interaction=nonstopmode', tex_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        print(f"Generated PDF with {num_pages} pages.")
        return num_pages
    else:
        print("PDF compilation failed!")
        return -1

if __name__ == '__main__':
    # Initial run
    pages = generate_pdf(ob11=5, ob12=5, dk13=10, dk14=7)
    print(f"Final Page Count: {pages}")
