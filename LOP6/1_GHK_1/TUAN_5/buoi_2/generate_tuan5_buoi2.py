import os
import subprocess

tex_header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ đều đặn chuẩn viết tay (khoảng cách 7.2mm rộng rãi)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=20.5pt%
  \vspace{1.5mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!60}\dotfill}\par%
  }%
  \vspace{1mm}%
  \endgroup%
}

% Định nghĩa ô bài tập tự luận trong bảng
\newcommand{\oBaiTap}[3][6]{%
  \vspace{1.5mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

% Câu trắc nghiệm 1 dòng (4 đáp án, mỗi đáp án 0.25\linewidth)
\newcommand{\cauTN}[6]{% \cauTN{số câu}{đề}{A}{B}{C}{D}
  \noindent\textbf{Câu #1.} #2\par\vspace{0.4mm}%
  \noindent%
  \makebox[0.25\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.25\linewidth][l]{\textbf{B.} #4}%
  \makebox[0.25\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.25\linewidth][l]{\textbf{D.} #6}\par\vspace{0.8mm}%
}

% Câu trắc nghiệm 2 dòng (mỗi dòng 2 đáp án, mỗi đáp án 0.5\linewidth) cho đáp án dài
\newcommand{\cauTNB}[6]{% \cauTNB{số câu}{đề}{A}{B}{C}{D}
  \noindent\textbf{Câu #1.} #2\par\vspace{0.4mm}%
  \noindent%
  \makebox[0.5\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.5\linewidth][l]{\textbf{B.} #4}\par\vspace{0.4mm}%
  \noindent%
  \makebox[0.5\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.5\linewidth][l]{\textbf{D.} #6}\par\vspace{0.8mm}%
}

\begin{document}
\pagestyle{empty}
'''

de_data = {
    101: {
        'tn': [
            ('cauTN', "Trong các số sau: $125, 230, 342, 515$, số chia hết cho cả $2$ và $5$ là:", "$125$", "$230$", "$342$", "$515$"),
            ('cauTN', "Số nào sau đây chia hết cho $3$?", "$145$", "$253$", "$357$", "$418$"),
            ('cauTN', "Cho số $A = \\overline{35*}$. Để $A$ chia hết cho $9$ thì chữ số $*$ thích hợp là:", "$1$", "$4$", "$7$", "$9$"),
            ('cauTNB', "Khẳng định nào sau đây là \\textbf{sai}?", "Nếu $a \\ \\vdots \\ 4$ và $b \\ \\vdots \\ 4$ thì $(a+b) \\ \\vdots \\ 4$", "Nếu $a \\ \\vdots \\ 5$ và $b \\ \\not\\vdots \\ 5$ thì $(a+b) \\ \\not\\vdots \\ 5$", "Nếu $(a+b) \\ \\vdots \\ 6$ thì mỗi số $a, b$ đều chia hết cho 6", "Nếu $a, b \\ \\vdots \\ 3$ thì $(a-b) \\ \\vdots \\ 3$ (với $a \\ge b$)"),
            ('cauTN', "Trong các số: $120, 235, 348, 540$, số chia hết cho cả $2, 3, 5$ và $9$ là:", "$120$", "$235$", "$348$", "$540$")
        ],
        'c1': [
            ("a)", "$38 + 24 \\cdot 2 - 2^4$"),
            ("b)", "$43 \\cdot 78 + 43 \\cdot 22 - 800$"),
            ("c)", "$120 : [54 - (50 - 2^3 \\cdot 2)]$"),
            ("d)", "$240 : \\{ 180 - [75 + (8 - 3)^2] \\}$")
        ],
        'c2': [
            ("a)", "$24 + 3(x - 2) = 45$"),
            ("b)", "$2 \\cdot 3^x - 14 = 40$"),
            ("c)", "Tìm số tự nhiên $x$ lớn nhất, biết rằng $48 \\ \\vdots \\ x$ và $72 \\ \\vdots \\ x$."),
            ("d)", "Tìm số tự nhiên $x$, biết rằng $60 \\ \\vdots \\ x$, $84 \\ \\vdots \\ x$ và $x > 6$.")
        ],
        'c3': {
            'context': "Bác Hùng có một khu đất hình chữ nhật có chiều dài là $18\\text{ m}$ và chiều rộng là $12\\text{ m}$. Bác dự định làm hàng rào lưới thép B40 xung quanh khu đất và để lại một cổng ra vào rộng $2\\text{ m}$.",
            'a': "Tính chu vi của khu đất hình chữ nhật đó.",
            'b': "Tính chiều dài hàng rào lưới thép B40 cần làm và số tiền bác Hùng phải trả để mua lưới thép, biết giá mỗi mét lưới thép là $80\\,000\\text{ đồng}$."
        }
    },
    102: {
        'tn': [
            ('cauTN', "Số nào sau đây chia hết cho $2$ nhưng \\textbf{không chia hết} cho $5$?", "$150$", "$274$", "$385$", "$411$"),
            ('cauTN', "Số nào sau đây chia hết cho cả $3$ và $9$?", "$123$", "$234$", "$345$", "$456$"),
            ('cauTN', "Cho số $\\overline{4*7}$. Chữ số $*$ thích hợp để số đó chia hết cho $3$ có thể là:", "$1$", "$2$", "$3$", "$5$"),
            ('cauTN', "Tổng nào sau đây chia hết cho $7$?", "$14 + 21 + 35$", "$14 + 21 + 36$", "$7 + 15 + 28$", "$21 + 30 + 49$"),
            ('cauTNB', "Một số tự nhiên có chữ số tận cùng bằng $0$ và tổng các chữ số chia hết cho $3$ thì số đó:", "Chỉ chia hết cho 2 và 5", "Chỉ chia hết cho 3", "Chia hết cho cả 2, 3 và 5", "Chia hết cho cả 2, 3, 5 và 9")
        ],
        'c1': [
            ("a)", "$42 + 25 \\cdot 2 - 3^3$"),
            ("b)", "$37 \\cdot 64 + 37 \\cdot 36 - 700$"),
            ("c)", "$140 : [54 - (50 - 2^4)]$"),
            ("d)", "$320 : \\{ 180 - [75 + (11 - 6)^2] \\}$")
        ],
        'c2': [
            ("a)", "$35 + 4(x - 3) = 67$"),
            ("b)", "$3 \\cdot 2^x - 7 = 41$"),
            ("c)", "Tìm số tự nhiên $x$ lớn nhất, biết rằng $56 \\ \\vdots \\ x$ và $84 \\ \\vdots \\ x$."),
            ("d)", "Tìm số tự nhiên $x$, biết rằng $70 \\ \\vdots \\ x$, $105 \\ \\vdots \\ x$ và $x > 10$.")
        ],
        'c3': {
            'context': "Bác Minh có một mảnh vườn trồng hoa hình chữ nhật có chiều dài là $20\\text{ m}$ và chiều rộng là $15\\text{ m}$. Bác dự định làm hàng rào dây thép gai xung quanh vườn và chừa lại một lối đi rộng $3\\text{ m}$.",
            'a': "Tính chu vi của mảnh vườn hình chữ nhật đó.",
            'b': "Tính chiều dài dây thép gai cần làm và số tiền bác Minh phải trả, biết giá mỗi mét dây thép gai là $60\\,000\\text{ đồng}$."
        }
    },
    103: {
        'tn': [
            ('cauTN', "Số nào sau đây chia hết cho $5$ nhưng \\textbf{không chia hết} cho $2$?", "$240$", "$375$", "$468$", "$512$"),
            ('cauTN', "Số nào sau đây \\textbf{không chia hết} cho $3$?", "$132$", "$246$", "$357$", "$418$"),
            ('cauTNB', "Chữ số thích hợp điền vào dấu $*$ để số $\\overline{58*}$ chia hết cho cả $2$ và $5$ là:", "$0$", "$2$", "$5$", "Không có chữ số nào"),
            ('cauTNB', "Cho tổng $S = 24 + 36 + x$ (với $x \\in \\mathbb{N}$). Để $S$ chia hết cho $6$ thì:", "$x$ là số tự nhiên bất kỳ", "$x$ phải chia hết cho 6", "$x$ không chia hết cho 6", "$x$ chia cho 6 dư 1"),
            ('cauTN', "Trong các số sau: $342, 516, 725, 814$, số chia hết cho $9$ là:", "$342$", "$516$", "$725$", "$814$")
        ],
        'c1': [
            ("a)", "$45 + 18 \\cdot 3 - 2^5$"),
            ("b)", "$52 \\cdot 73 + 52 \\cdot 27 - 1200$"),
            ("c)", "$180 : [60 - (46 - 2^4)]$"),
            ("d)", "$400 : \\{ 210 - [85 + (9 - 4)^2] \\}$")
        ],
        'c2': [
            ("a)", "$28 + 5(x - 4) = 73$"),
            ("b)", "$5 \\cdot 2^x - 12 = 68$"),
            ("c)", "Tìm số tự nhiên $x$ lớn nhất, biết rằng $54 \\ \\vdots \\ x$ và $90 \\ \\vdots \\ x$."),
            ("d)", "Tìm số tự nhiên $x$, biết rằng $45 \\ \\vdots \\ x$, $75 \\ \\vdots \\ x$ và $x > 5$.")
        ],
        'c3': {
            'context': "Một khung cửa sổ bằng nhôm kính hình chữ nhật có chiều dài là $160\\text{ cm}$ và chiều rộng là $120\\text{ cm}$. Người thợ cần lắp đặt dải gioăng cao su bảo vệ bao quanh toàn bộ viền ngoài của khung cửa sổ.",
            'a': "Tính chu vi của khung cửa sổ đó (theo đơn vị mét).",
            'b': "Tính tổng chi phí mua dải gioăng cao su, biết đơn giá mỗi mét gioăng là $45\\,000\\text{ đồng}$."
        }
    },
    104: {
        'tn': [
            ('cauTN', "Các số có chữ số tận cùng là $0, 2, 4, 6, 8$ thì chắc chắn:", "Chia hết cho 5", "Chia hết cho 3", "Chia hết cho 2", "Chia hết cho cả 2 và 5"),
            ('cauTNB', "Khẳng định nào sau đây là \\textbf{đúng}?", "Mọi số chia hết cho 3 đều chia hết cho 9", "Mọi số chia hết cho 9 đều chia hết cho 3", "Số có chữ số tận cùng là 9 thì chia hết cho 9", "Số có tổng các chữ số bằng 6 thì chia hết cho 9"),
            ('cauTN', "Chữ số $*$ thích hợp để số $\\overline{7*5}$ chia hết cho $9$ là:", "$3$", "$5$", "$6$", "$9$"),
            ('cauTN', "Hiệu nào sau đây chia hết cho $8$?", "$64 - 24$", "$56 - 25$", "$48 - 18$", "$72 - 30$"),
            ('cauTN', "Số tự nhiên nhỏ nhất có ba chữ số khác nhau chia hết cho cả $2$ và $5$ là:", "$100$", "$120$", "$102$", "$105$")
        ],
        'c1': [
            ("a)", "$56 + 15 \\cdot 3 - 3^3$"),
            ("b)", "$64 \\cdot 82 + 64 \\cdot 18 - 1400$"),
            ("c)", "$200 : [55 - (46 - 2^4)]$"),
            ("d)", "$500 : \\{ 220 - [95 + (8 - 3)^2] \\}$")
        ],
        'c2': [
            ("a)", "$36 + 6(x - 5) = 84$"),
            ("b)", "$4 \\cdot 3^x - 22 = 86$"),
            ("c)", "Tìm số tự nhiên $x$ lớn nhất, biết rằng $64 \\ \\vdots \\ x$ và $96 \\ \\vdots \\ x$."),
            ("d)", "Tìm số tự nhiên $x$, biết rằng $40 \\ \\vdots \\ x$, $60 \\ \\vdots \\ x$ và $x > 10$.")
        ],
        'c3': {
            'context': "Một biển hiệu quảng cáo có dạng hình thoi với độ dài mỗi cạnh là $2{,}5\\text{ m}$. Ban quản lý cửa hàng cần lắp dải đèn LED trang trí chạy dọc theo toàn bộ viền ngoài của biển quảng cáo đó.",
            'a': "Tính chu vi của biển hiệu quảng cáo hình thoi đó.",
            'b': "Tính tổng số tiền cần thanh toán để mua dải đèn LED, biết giá tiền mỗi mét đèn LED là $115\\,000\\text{ đồng}$."
        }
    }
}

tex_content = tex_header
for de in [101, 102, 103, 104]:
    data = de_data[de]
    tex_content += f"""
% =============================================================================
% ========================= TOÁN 6 - TUẦN 05 - BUỔI 02: MÃ ĐỀ {de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 05 - BUỔI 02}} & \\textbf{{Mã đề: {de} - Trang 1/2}} \\\\
\\textit{{Chủ đề: Dấu hiệu chia hết (2, 3, 5, 9) --- Tìm ƯCLN --- Tứ giác thực tế}} & \\textit{{Thời gian: 45 phút}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\rule[-3.5mm]{{0pt}}{{10mm}}\\textbf{{Họ và tên học sinh:}} \\hfill \\textbf{{Mã HS:}} \\makebox[3.5cm]{{}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.3cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{BẢNG ĐIỀN ĐÁP ÁN TRẮC NGHIỆM (Mỗi câu đúng 0,5 điểm):}}
\\vspace{{0.8mm}}

\\noindent
\\begingroup
\\setlength{{\\tabcolsep}}{{3pt}}
\\renewcommand{{\\arraystretch}}{{1.35}}
\\begin{{tabularx}}{{\\linewidth}}{{|c|*{{5}}{{>{{\\centering\\arraybackslash}}X|}}}}
\\hline
\\textbf{{Câu}} & \\textbf{{1}} & \\textbf{{2}} & \\textbf{{3}} & \\textbf{{4}} & \\textbf{{5}} \\\\
\\hline
\\textbf{{Đáp án}} & & & & & \\\\
\\hline
\\end{{tabularx}}
\endgroup

\\vspace{{1.5mm}}

\\noindent\\textbf{{\\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,5 điểm)}}
\\vspace{{1mm}}
"""
    for idx, tn in enumerate(data['tn'], 1):
        macro = tn[0]
        tex_content += f"\n\\{macro}{{{idx}}}{{{tn[1]}}}{{{tn[2]}}}{{{tn[3]}}}{{{tn[4]}}}{{{tn[5]}}}\n"

    tex_content += f"""
\\vspace{{1.2mm}}

\\noindent\\textbf{{\\large PHẦN II. TỰ LUẬN (7,5 điểm)}}

\\noindent\\textbf{{Câu 1 (2,5 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[6]{{{data['c1'][0][0]}}}{{{data['c1'][0][1]}}} & 
\\oBaiTap[6]{{{data['c1'][1][0]}}}{{{data['c1'][1][1]}}} \\\\
\\hline
\\oBaiTap[6]{{{data['c1'][2][0]}}}{{{data['c1'][2][1]}}} & 
\\oBaiTap[6]{{{data['c1'][3][0]}}}{{{data['c1'][3][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
% =============================================================================
% ========================= TOÁN 6 - TUẦN 05 - BUỔI 02: MÃ ĐỀ {de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHẦN II. TỰ LUẬN (Tiếp theo) - TOÁN 6 TUẦN 05 BUỔI 02}} & \\textbf{{Mã đề: {de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{2.5mm}}

\\noindent\\textbf{{\\large Câu 2 (2,5 điểm). Tìm số tự nhiên $x$, biết:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[6]{{{data['c2'][0][0]}}}{{{data['c2'][0][1]}}} & 
\\oBaiTap[6]{{{data['c2'][1][0]}}}{{{data['c2'][1][1]}}} \\\\
\\hline
\\oBaiTap[6]{{{data['c2'][2][0]}}}{{{data['c2'][2][1]}}} & 
\\oBaiTap[6]{{{data['c2'][3][0]}}}{{{data['c2'][3][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{2.5mm}}

\\noindent\\textbf{{\\large Câu 3 (2,5 điểm). Bài toán thực tế:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
{data['c3']['context']}\\par
\\textbf{{a) (1,25 điểm)}} {data['c3']['a']}\\par
\\textbf{{b) (1,25 điểm)}} {data['c3']['b']}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{14}}
\\\\ \\hline
\\end{{tabularx}}
"""
    if de < 104:
        tex_content += "\n\\newpage\n"

tex_content += "\n\\end{document}\n"

target_file = os.path.join(os.path.dirname(__file__), 'Phieu_Kiem_Tra_Tuan_05_Buoi_02.tex')
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(tex_content)

print(f'{target_file} updated successfully')
