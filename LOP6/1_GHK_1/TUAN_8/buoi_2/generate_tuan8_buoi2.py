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

\SAOPTN{widthSA=2.7,heightSA=0.62}

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
% ========================= TOÁN 6 - TUẦN 08 - BUỔI 02: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 08 - BUỔI 02}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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
% ========================= TOÁN 6 - TUẦN 08 - BUỔI 02: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 6 - TUẦN 08 - BUỔI 02}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
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
            (r'Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 48\}$ có bao nhiêu phần tử?', '48'),
            (r'Số La Mã $\text{XXVI}$ có giá trị trong hệ thập phân là bao nhiêu?', '26'),
            (r'Viết gọn kết quả của phép chia $5^8 : 5^3$ dưới dạng một lũy thừa.', '5^5'),
            (r'Giá trị của biểu thức $40 + 20 : 2^2$ bằng bao nhiêu?', '45'),
            (r'Chữ số tận cùng của số tự nhiên chia hết cho cả $2$ và $5$ là:', '0'),
            (r'Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{5x2}$ chia hết cho $3$.', '2'),
            (r'Phân tích số $24$ ra thừa số nguyên tố có kết quả là gì?', r'2^3 \cdot 3'),
            (r'Hai đường chéo của hình bình hành cắt nhau tại:', r'\text{Trung điểm}'),
            (r'Một hình chữ nhật có chiều dài $14\text{ m}$, chiều rộng $6\text{ m}$. Chu vi là:', r'40\text{ m}'),
            (r'Hình bình hành có độ dài đáy $15\text{ cm}$, chiều cao $8\text{ cm}$. Diện tích là:', r'120\text{ cm}^2'),
        ],
        'q11': {
            'a': r'185 - 3^2 \cdot 6 + 2^4 \cdot 3',
            'b': r'125 + 74 + 175 + 26',
            'c': r'37 \cdot 64 + 37 \cdot 36 + 300',
            'd': r'240 : (35 - 11) + 2^3 \cdot 5',
            'e': r'160 : [52 - (15 - 9)^2]',
            'f': r'500 : \{ 130 - [53 + (17 - 14)^3] \}',
        },
        'q12': {
            'a': r'(x - 12) : 4 = 15',
            'b': r'120 - [45 - (x - 3)] = 85',
            'c': r'(x - 2)^3 = 27',
            'd': r'$x \ \vdots \ 12$, $x \ \vdots \ 18$ và $50 < x < 100$.',
        },
        'q13': {
            'de': r'Chi đội $6\text{A}$ có $24$ bạn nam và $36$ bạn nữ. Cô giáo chủ nhiệm muốn chia đều số nam và số nữ vào các tổ học tập sao cho số nam và số nữ ở mỗi tổ là như nhau.',
            'a': r'Cô giáo có thể chia được nhiều nhất thành bao nhiêu tổ?',
            'b': r'Khi đó, ở mỗi tổ có bao nhiêu bạn nam và bao nhiêu bạn nữ?',
        },
        'q14': {
            'de': r'Cho biểu thức $A = 2 + 2^2 + 2^3 + \dots + 2^{60}$. Chứng minh rằng $A$ chia hết cho $7$.',
        }
    },
    '102': {
        'short': [
            (r'Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 56\}$ có bao nhiêu phần tử?', '56'),
            (r'Số La Mã $\text{XXIII}$ có giá trị trong hệ thập phân là bao nhiêu?', '23'),
            (r'Viết gọn kết quả của phép chia $6^9 : 6^4$ dưới dạng một lũy thừa.', '6^5'),
            (r'Giá trị của biểu thức $50 + 36 : 3^2$ bằng bao nhiêu?', '54'),
            (r'Số dư khi chia một số có chữ số tận cùng là $3$ cho $5$ là:', '3'),
            (r'Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{4x5}$ chia hết cho $3$.', '3'),
            (r'Phân tích số $36$ ra thừa số nguyên tố có kết quả là gì?', r'2^2 \cdot 3^2'),
            (r'Hai cạnh đối diện của hình bình hành có tính chất:', r'\text{Song song, bằng nhau}'),
            (r'Một hình chữ nhật có chiều dài $15\text{ m}$, chiều rộng $7\text{ m}$. Chu vi là:', r'44\text{ m}'),
            (r'Hình bình hành có độ dài đáy $16\text{ cm}$, chiều cao $7\text{ cm}$. Diện tích là:', r'112\text{ cm}^2'),
        ],
        'q11': {
            'a': r'195 - 4^2 \cdot 4 + 3^3 \cdot 2',
            'b': r'135 + 68 + 165 + 32',
            'c': r'43 \cdot 78 + 43 \cdot 22 + 700',
            'd': r'260 : (38 - 12) + 3^2 \cdot 6',
            'e': r'180 : [67 - (17 - 10)^2]',
            'f': r'600 : \{ 140 - [53 + (18 - 15)^3] \}',
        },
        'q12': {
            'a': r'(x - 15) : 5 = 14',
            'b': r'130 - [55 - (x - 4)] = 90',
            'c': r'(x - 3)^3 = 64',
            'd': r'$x \ \vdots \ 15$, $x \ \vdots \ 20$ và $80 < x < 150$.',
        },
        'q13': {
            'de': r'Chi đội $6\text{B}$ có $28$ bạn nam và $42$ bạn nữ. Cô giáo chủ nhiệm muốn chia đều số nam và số nữ vào các tổ học tập sao cho số tổ là nhiều nhất.',
            'a': r'Cô giáo có thể chia được nhiều nhất thành bao nhiêu tổ?',
            'b': r'Khi đó, ở mỗi tổ có bao nhiêu bạn nam và bao nhiêu bạn nữ?',
        },
        'q14': {
            'de': r'Cho biểu thức $B = 3 + 3^2 + 3^3 + \dots + 3^{60}$. Chứng minh rằng $B$ chia hết cho $13$.',
        }
    },
    '103': {
        'short': [
            (r'Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 64\}$ có bao nhiêu phần tử?', '64'),
            (r'Số La Mã $\text{XXV}$ có giá trị trong hệ thập phân là bao nhiêu?', '25'),
            (r'Viết gọn kết quả của phép chia $7^7 : 7^2$ dưới dạng một lũy thừa.', '7^5'),
            (r'Giá trị của biểu thức $60 + 48 : 2^4$ bằng bao nhiêu?', '63'),
            (r'Số dư khi chia một số có chữ số tận cùng là $7$ cho $5$ là:', '2'),
            (r'Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{6x1}$ chia hết cho $3$.', '2'),
            (r'Phân tích số $40$ ra thừa số nguyên tố có kết quả là gì?', r'2^3 \cdot 5'),
            (r'Hai góc đối diện của một hình bình hành có số đo:', r'\text{Bằng nhau}'),
            (r'Một hình chữ nhật có chiều dài $16\text{ m}$, chiều rộng $8\text{ m}$. Chu vi là:', r'48\text{ m}'),
            (r'Hình bình hành có độ dài đáy $18\text{ cm}$, chiều cao $6\text{ cm}$. Diện tích là:', r'108\text{ cm}^2'),
        ],
        'q11': {
            'a': r'175 - 2^5 \cdot 3 + 5^2 \cdot 3',
            'b': r'145 + 57 + 155 + 43',
            'c': r'52 \cdot 83 + 52 \cdot 17 + 800',
            'd': r'280 : (42 - 14) + 4^2 \cdot 3',
            'e': r'200 : [84 - (19 - 11)^2]',
            'f': r'700 : \{ 150 - [53 + (19 - 16)^3] \}',
        },
        'q12': {
            'a': r'(x - 14) : 6 = 12',
            'b': r'140 - [65 - (x - 5)] = 95',
            'c': r'(x - 1)^3 = 125',
            'd': r'$x \ \vdots \ 14$, $x \ \vdots \ 21$ và $60 < x < 100$.',
        },
        'q13': {
            'de': r'Chi đội $6\text{C}$ có $32$ bạn nam và $48$ bạn nữ. Cô giáo chủ nhiệm muốn chia đều số nam và số nữ vào các nhóm sao cho số nhóm là nhiều nhất.',
            'a': r'Cô giáo có thể chia được nhiều nhất thành bao nhiêu nhóm?',
            'b': r'Khi đó, ở mỗi nhóm có bao nhiêu bạn nam và bao nhiêu bạn nữ?',
        },
        'q14': {
            'de': r'Cho biểu thức $C = 4 + 4^2 + 4^3 + \dots + 4^{60}$. Chứng minh rằng $C$ chia hết cho $21$.',
        }
    },
    '104': {
        'short': [
            (r'Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 75\}$ có bao nhiêu phần tử?', '75'),
            (r'Số La Mã $\text{XXII}$ có giá trị trong hệ thập phân là bao nhiêu?', '22'),
            (r'Viết gọn kết quả của phép chia $8^8 : 8^3$ dưới dạng một lũy thừa.', '8^5'),
            (r'Giá trị của biểu thức $70 + 75 : 5^2$ bằng bao nhiêu?', '73'),
            (r'Số dư khi chia một số có chữ số tận cùng là $8$ cho $5$ là:', '3'),
            (r'Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{7x3}$ chia hết cho $3$.', '2'),
            (r'Phân tích số $48$ ra thừa số nguyên tố có kết quả là gì?', r'2^4 \cdot 3'),
            (r'Hai đường chéo của một hình thoi có tính chất:', r'\text{Vuông góc}'),
            (r'Một hình chữ nhật có chiều dài $18\text{ m}$, chiều rộng $9\text{ m}$. Chu vi là:', r'54\text{ m}'),
            (r'Hình bình hành có độ dài đáy $20\text{ cm}$, chiều cao $8\text{ cm}$. Diện tích là:', r'160\text{ cm}^2'),
        ],
        'q11': {
            'a': r'165 - 3^3 \cdot 3 + 4^3 \cdot 1',
            'b': r'115 + 86 + 185 + 14',
            'c': r'61 \cdot 74 + 61 \cdot 26 + 900',
            'd': r'300 : (45 - 15) + 5^2 \cdot 2',
            'e': r'220 : [103 - (21 - 12)^2]',
            'f': r'800 : \{ 160 - [53 + (20 - 17)^3] \}',
        },
        'q12': {
            'a': r'(x - 16) : 7 = 11',
            'b': r'150 - [75 - (x - 6)] = 100',
            'c': r'(x - 4)^3 = 8',
            'd': r'$x \ \vdots \ 16$, $x \ \vdots \ 24$ và $70 < x < 120$.',
        },
        'q13': {
            'de': r'Chi đội $6\text{D}$ có $30$ bạn nam và $45$ bạn nữ. Cô giáo chủ nhiệm muốn chia đều số nam và số nữ vào các tổ học tập sao cho số tổ là nhiều nhất.',
            'a': r'Cô giáo có thể chia được nhiều nhất thành bao nhiêu tổ?',
            'b': r'Khi đó, ở mỗi tổ có bao nhiêu bạn nam và bao nhiêu bạn nữ?',
        },
        'q14': {
            'de': r'Cho biểu thức $D = 5 + 5^2 + 5^3 + \dots + 5^{60}$. Chứng minh rằng $D$ chia hết cho $31$.',
        }
    }
}

def generate_pdf(ob11=6, ob12=5, dk13=12, dk14=9):
    content = tex_template
    for ma_de in ['101', '102', '103', '104']:
        d = de_data[ma_de]
        content += render_de(ma_de, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11, ob12, dk13, dk14)
    content += r'\end{document}'

    tex_path = 'Phieu_Kiem_Tra_Tuan_08_Buoi_02.tex'
    pdf_path = 'Phieu_Kiem_Tra_Tuan_08_Buoi_02.pdf'

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
    pages = generate_pdf(ob11=6, ob12=5, dk13=12, dk14=9)
    print(f"Final Page Count: {pages}")

