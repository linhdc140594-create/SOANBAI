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

\SAOPTN{widthSA=3.2,heightSA=0.62}

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

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=8, ob12=5, dk13=11, dk14=7):
    res = f'''% =============================================================================
% ========================= TOÁN 6 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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
% ========================= TOÁN 6 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 6 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
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
            ("Một hình vuông có độ dài cạnh bằng $9\\text{ cm}$. Chu vi của hình vuông đó bằng bao nhiêu?", "36\\text{ cm}"),
            ("Một mảnh đất hình chữ nhật có chiều dài $12\\text{ m}$ và chiều rộng $5\\text{ m}$. Diện tích của mảnh đất đó bằng bao nhiêu?", "60\\text{ m}^2"),
            ("Một hình thoi có độ dài hai đường chéo lần lượt là $8\\text{ cm}$ và $10\\text{ cm}$. Diện tích của hình thoi đó bằng bao nhiêu?", "40\\text{ cm}^2"),
            ("Một hình bình hành có độ dài cạnh đáy là $12\\text{ cm}$ và chiều cao tương ứng là $6\\text{ cm}$. Diện tích của hình bình hành đó bằng bao nhiêu?", "72\\text{ cm}^2"),
            ("Giá trị của biểu thức $2^4 \\cdot 5 - 3^2 \\cdot 4$ bằng bao nhiêu?", "44"),
            ("Một hình vuông có diện tích bằng $64\\text{ cm}^2$. Độ dài cạnh của hình vuông đó bằng bao nhiêu?", "8\\text{ cm}"),
            ("Một hình chữ nhật có chiều dài $15\\text{ cm}$ và chiều rộng $8\\text{ cm}$. Chu vi của hình chữ nhật đó bằng bao nhiêu?", "46\\text{ cm}"),
            ("Một hình thoi có chu vi bằng $36\\text{ cm}$. Độ dài cạnh của hình thoi đó bằng bao nhiêu?", "9\\text{ cm}"),
            ("Một hình bình hành có diện tích bằng $48\\text{ cm}^2$ và độ dài đáy bằng $8\\text{ cm}$. Chiều cao tương ứng bằng bao nhiêu?", "6\\text{ cm}"),
            ("Giá trị của biểu thức $5 \\cdot 2^3 - 3^3$ bằng bao nhiêu?", "13")
        ],
        'q11': {
            'a': '$135 - 3^2 \\cdot 10 + 2^3 \\cdot 5$',
            'b': '$47 \\cdot 68 + 47 \\cdot 32 - 700$',
            'c': '$160 : [65 - (18 - 11)^2]$',
            'd': '$200 : \\{ 80 - [22 + (9 - 7)^3] \\}$'
        },
        'q12': {
            'a': '$45 + 5 \\cdot (x - 3) = 75$',
            'b': '$95 - (3x + 14) = 45$',
            'c': '$2 \\cdot 3^{x+1} - 15 = 39$',
            'd': 'Một hình chữ nhật có chu vi bằng $40\\text{ cm}$, chiều rộng $x\\text{ cm}$, dài $12\\text{ cm}$. Tìm $x$.'
        },
        'q13': {
            'de': 'Bác An có một mảnh vườn hình chữ nhật có chiều dài $20\\text{ m}$ và chiều rộng $12\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh vườn đó.',
            'b': 'Bác An dự định làm hàng rào lưới thép bao quanh khu vườn, chừa lại một cổng ra vào rộng $2\\text{ m}$. Tính chiều dài hàng rào lưới thép và số tiền bác An phải trả để mua lưới thép, biết giá mỗi mét lưới thép là $60\\ 000$ đồng.'
        },
        'q14': {
            'de': 'Cho tổng $A = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{99} + 3^{100}$. Chứng minh rằng $2A + 1$ là một lũy thừa của $3$.'
        }
    },
    '102': {
        'short': [
            ("Một hình vuông có độ dài cạnh bằng $8\\text{ cm}$. Chu vi của hình vuông đó bằng bao nhiêu?", "32\\text{ cm}"),
            ("Một mảnh đất hình chữ nhật có chiều dài $15\\text{ m}$ và chiều rộng $4\\text{ m}$. Diện tích của mảnh đất đó bằng bao nhiêu?", "60\\text{ m}^2"),
            ("Một hình thoi có độ dài hai đường chéo lần lượt là $6\\text{ cm}$ và $12\\text{ cm}$. Diện tích của hình thoi đó bằng bao nhiêu?", "36\\text{ cm}^2"),
            ("Một hình bình hành có độ dài cạnh đáy là $15\\text{ cm}$ và chiều cao tương ứng là $4\\text{ cm}$. Diện tích của hình bình hành đó bằng bao nhiêu?", "60\\text{ cm}^2"),
            ("Giá trị của biểu thức $3^3 \\cdot 2 - 2^4 \\cdot 3$ bằng bao nhiêu?", "6"),
            ("Một hình vuông có diện tích bằng $81\\text{ cm}^2$. Độ dài cạnh của hình vuông đó bằng bao nhiêu?", "9\\text{ cm}"),
            ("Một hình chữ nhật có chiều dài $16\\text{ cm}$ và chiều rộng $7\\text{ cm}$. Chu vi của hình chữ nhật đó bằng bao nhiêu?", "46\\text{ cm}"),
            ("Một hình thoi có chu vi bằng $48\\text{ cm}$. Độ dài cạnh của hình thoi đó bằng bao nhiêu?", "12\\text{ cm}"),
            ("Một hình bình hành có diện tích bằng $54\\text{ cm}^2$ và độ dài đáy bằng $9\\text{ cm}$. Chiều cao tương ứng bằng bao nhiêu?", "6\\text{ cm}"),
            ("Giá trị của biểu thức $4 \\cdot 3^2 - 2^4$ bằng bao nhiêu?", "20")
        ],
        'q11': {
            'a': '$145 - 2^3 \\cdot 10 + 3^2 \\cdot 5$',
            'b': '$53 \\cdot 74 + 53 \\cdot 26 - 800$',
            'c': '$180 : [54 - (16 - 10)^2]$',
            'd': '$300 : \\{ 90 - [22 + (8 - 6)^3] \\}$'
        },
        'q12': {
            'a': '$38 + 4 \\cdot (x - 2) = 62$',
            'b': '$86 - (4x + 10) = 44$',
            'c': '$3 \\cdot 2^{x+1} - 12 = 36$',
            'd': 'Một hình thoi có chu vi bằng $52\\text{ cm}$ và độ dài cạnh bằng $x\\text{ cm}$. Tìm $x$.'
        },
        'q13': {
            'de': 'Bác Bình có một mảnh vườn hình chữ nhật có chiều dài $25\\text{ m}$ và chiều rộng $10\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh vườn đó.',
            'b': 'Bác Bình dự định làm hàng rào lưới thép bao quanh khu vườn, chừa lại một cổng ra vào rộng $3\\text{ m}$. Tính chiều dài hàng rào lưới thép và số tiền bác Bình phải trả để mua lưới thép, biết giá mỗi mét lưới thép là $55\\ 000$ đồng.'
        },
        'q14': {
            'de': 'Cho tổng $B = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{99} + 2^{100}$. Chứng minh rằng $B + 1$ là một lũy thừa của $2$.'
        }
    },
    '103': {
        'short': [
            ("Một hình vuông có độ dài cạnh bằng $7\\text{ cm}$. Chu vi của hình vuông đó bằng bao nhiêu?", "28\\text{ cm}"),
            ("Một mảnh đất hình chữ nhật có chiều dài $14\\text{ m}$ và chiều rộng $5\\text{ m}$. Diện tích của mảnh đất đó bằng bao nhiêu?", "70\\text{ m}^2"),
            ("Một hình thoi có độ dài hai đường chéo lần lượt là $8\\text{ cm}$ và $14\\text{ cm}$. Diện tích của hình thoi đó bằng bao nhiêu?", "56\\text{ cm}^2"),
            ("Một hình bình hành có độ dài cạnh đáy là $14\\text{ cm}$ và chiều cao tương ứng là $5\\text{ cm}$. Diện tích của hình bình hành đó bằng bao nhiêu?", "70\\text{ cm}^2"),
            ("Giá trị của biểu thức $2^5 \\cdot 3 - 5^2 \\cdot 2$ bằng bao nhiêu?", "46"),
            ("Một hình vuông có diện tích bằng $49\\text{ cm}^2$. Độ dài cạnh của hình vuông đó bằng bao nhiêu?", "7\\text{ cm}"),
            ("Một hình chữ nhật có chiều dài $18\\text{ cm}$ và chiều rộng $6\\text{ cm}$. Chu vi của hình chữ nhật đó bằng bao nhiêu?", "48\\text{ cm}"),
            ("Một hình thoi có chu vi bằng $44\\text{ cm}$. Độ dài cạnh của hình thoi đó bằng bao nhiêu?", "11\\text{ cm}"),
            ("Một hình bình hành có diện tích bằng $63\\text{ cm}^2$ và độ dài đáy bằng $7\\text{ cm}$. Chiều cao tương ứng bằng bao nhiêu?", "9\\text{ cm}"),
            ("Giá trị của biểu thức $6 \\cdot 2^3 - 4^2$ bằng bao nhiêu?", "32")
        ],
        'q11': {
            'a': '$150 - 4^2 \\cdot 5 + 2^4 \\cdot 3$',
            'b': '$36 \\cdot 83 + 36 \\cdot 17 - 600$',
            'c': '$210 : [51 - (15 - 9)^2]$',
            'd': '$240 : \\{ 85 - [37 + (7 - 5)^3] \\}$'
        },
        'q12': {
            'a': '$52 + 6 \\cdot (x - 4) = 88$',
            'b': '$98 - (5x + 13) = 45$',
            'c': '$4 \\cdot 3^{x-1} - 10 = 26$',
            'd': 'Một hình bình hành có diện tích bằng $84\\text{ cm}^2$, chiều cao $7\\text{ cm}$, cạnh đáy tương ứng là $x\\text{ cm}$. Tìm $x$.'
        },
        'q13': {
            'de': 'Bác Cường có một mảnh vườn hình chữ nhật có chiều dài $18\\text{ m}$ và chiều rộng $12\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh vườn đó.',
            'b': 'Bác Cường dự định làm hàng rào lưới thép bao quanh khu vườn, chừa lại một cổng ra vào rộng $2\\text{ m}$. Tính chiều dài hàng rào lưới thép và số tiền bác Cường phải trả để mua lưới thép, biết giá mỗi mét lưới thép là $65\\ 000$ đồng.'
        },
        'q14': {
            'de': 'Cho tổng $C = 1 + 4 + 4^2 + 4^3 + \\dots + 4^{49} + 4^{50}$. Chứng minh rằng $3C + 1$ là một lũy thừa của $4$.'
        }
    },
    '104': {
        'short': [
            ("Một hình vuông có độ dài cạnh bằng $11\\text{ cm}$. Chu vi của hình vuông đó bằng bao nhiêu?", "44\\text{ cm}"),
            ("Một mảnh đất hình chữ nhật có chiều dài $16\\text{ m}$ và chiều rộng $5\\text{ m}$. Diện tích của mảnh đất đó bằng bao nhiêu?", "80\\text{ m}^2"),
            ("Một hình thoi có độ dài hai đường chéo lần lượt là $10\\text{ cm}$ và $12\\text{ cm}$. Diện tích của hình thoi đó bằng bao nhiêu?", "60\\text{ cm}^2"),
            ("Một hình bình hành có độ dài cạnh đáy là $18\\text{ cm}$ và chiều cao tương ứng là $5\\text{ cm}$. Diện tích của hình bình hành đó bằng bao nhiêu?", "90\\text{ cm}^2"),
            ("Giá trị của biểu thức $3^2 \\cdot 10 - 2^3 \\cdot 5$ bằng bao nhiêu?", "50"),
            ("Một hình vuông có diện tích bằng $100\\text{ cm}^2$. Độ dài cạnh của hình vuông đó bằng bao nhiêu?", "10\\text{ cm}"),
            ("Một hình chữ nhật có chiều dài $20\\text{ cm}$ và chiều rộng $6\\text{ cm}$. Chu vi của hình chữ nhật đó bằng bao nhiêu?", "52\\text{ cm}"),
            ("Một hình thoi có chu vi bằng $56\\text{ cm}$. Độ dài cạnh của hình thoi đó bằng bao nhiêu?", "14\\text{ cm}"),
            ("Một hình bình hành có diện tích bằng $72\\text{ cm}^2$ và độ dài đáy bằng $8\\text{ cm}$. Chiều cao tương ứng bằng bao nhiêu?", "9\\text{ cm}"),
            ("Giá trị của biểu thức $7 \\cdot 2^3 - 5^2$ bằng bao nhiêu?", "31")
        ],
        'q11': {
            'a': '$160 - 5^2 \\cdot 4 + 3^3 \\cdot 2$',
            'b': '$64 \\cdot 69 + 64 \\cdot 31 - 900$',
            'c': '$240 : [52 - (18 - 12)^2]$',
            'd': '$280 : \\{ 95 - [47 + (6 - 4)^3] \\}$'
        },
        'q12': {
            'a': '$41 + 7 \\cdot (x - 3) = 76$',
            'b': '$105 - (6x + 15) = 42$',
            'c': '$5 \\cdot 2^{x-1} - 14 = 26$',
            'd': 'Một hình chữ nhật có diện tích bằng $96\\text{ cm}^2$, chiều rộng bằng $8\\text{ cm}$, chiều dài bằng $x\\text{ cm}$. Tìm $x$.'
        },
        'q13': {
            'de': 'Bác Dũng có một mảnh vườn hình chữ nhật có chiều dài $22\\text{ m}$ và chiều rộng $10\\text{ m}$.',
            'a': 'Tính chu vi và diện tích của mảnh vườn đó.',
            'b': 'Bác Dũng dự định làm hàng rào lưới thép bao quanh khu vườn, chừa lại một cổng ra vào rộng $2\\text{ m}$. Tính chiều dài hàng rào lưới thép và số tiền bác Dũng phải trả để mua lưới thép, biết giá mỗi mét lưới thép là $50\\ 000$ đồng.'
        },
        'q14': {
            'de': 'Cho tổng $D = 1 + 5 + 5^2 + 5^3 + \\dots + 5^{49} + 5^{50}$. Chứng minh rằng $4D + 1$ là một lũy thừa của $5$.'
        }
    }
}

full_tex = tex_template
for ma in ['101', '102', '103', '104']:
    d = de_data[ma]
    full_tex += render_de(ma, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11=8, ob12=5, dk13=11, dk14=7)

full_tex += r'\end{document}' + '\n'

out_path = r'd:\4. GitHub\SACH\LOP6\PHIEU_KIEM_TRA\1_GHK_1\TUAN_6\buoi_1\Phieu_Kiem_Tra_Tuan_06_Buoi_01.tex'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print('Wrote final Phieu_Kiem_Tra_Tuan_06_Buoi_01.tex with ob11=8.')
