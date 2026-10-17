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
            # (type, q, A, B, C, D)
            ('cauTNB', "Trong tam giác đều $ABC$, khẳng định nào sau đây là \\textbf{sai}?", "$AB = BC = CA$", "Ba góc ở đỉnh bằng nhau", "Mỗi góc bằng $60^\\circ$", "Mỗi góc bằng $90^\\circ$"),
            ('cauTNB', "Trong các khẳng định sau về hình vuông $ABCD$, khẳng định nào \\textbf{đúng}?", "Bốn góc bằng nhau và bằng $90^\\circ$", "Hai đường chéo không bằng nhau", "Hai đường chéo song song", "Bốn cạnh có độ dài khác nhau"),
            ('cauTN', "Lục giác đều $ABCDEF$ có bao nhiêu đường chéo chính?", "$3$", "$6$", "$4$", "$9$"),
            ('cauTN', "Một biển báo giao thông hình tam giác đều có cạnh $70\\text{ cm}$. Chu vi của biển báo đó là:", "$140\\text{ cm}$", "$210\\text{ cm}$", "$280\\text{ cm}$", "$70\\text{ cm}$"),
            ('cauTNB', "Cho lục giác đều $ABCDEF$ có tâm $O$. Các đoạn thẳng $OA, OB, OC, OD, OE, OF$ có độ dài:", "Đôi một vuông góc", "Bằng nhau", "Khác nhau hoàn toàn", "Song song với nhau")
        ],
        'c1': [
            ("a)", "$35 + 25 \\cdot 2 - 3^3$"),
            ("b)", "$28 \\cdot 64 + 28 \\cdot 36 - 800$"),
            ("c)", "$140 : [50 - (42 - 2^2 \\cdot 3)]$"),
            ("d)", "$300 : \\{ 160 - [44 + (7 - 3)^2] \\}$")
        ],
        'c2': [
            ("a)", "$35 + 4(x - 3) = 63$"),
            ("b)", "$130 - [50 - (x - 4)] = 95$"),
            ("c)", "$3 \\cdot 2^x - 7 = 41$"),
            ("d)", "Chu vi hình vuông cạnh $x\\text{ (cm)}$ bằng $48\\text{ cm}$")
        ],
        'c3': {
            'context': "Bác An có một mảnh vườn trồng hoa hình vuông có độ dài cạnh là $12\\text{ m}$. Bác An dự định làm hàng rào lưới thép xung quanh mảnh vườn, chỉ để lại một lối đi rộng $2\\text{ m}$.",
            'a': "Tính chu vi của mảnh vườn hình vuông đó.",
            'b': "Tính chiều dài lưới thép cần mua để rào và số tiền bác An phải trả, biết giá mỗi mét lưới thép là $65\\,000\\text{ đồng}$."
        }
    },
    102: {
        'tn': [
            ('cauTN', "Tam giác đều có độ dài cạnh bằng $a$ thì chu vi của nó bằng:", "$3a$", "$4a$", "$a^2$", "$6a$"),
            ('cauTN', "Một hình vuông có độ dài cạnh là $6\\text{ cm}$. Chu vi của hình vuông đó là:", "$12\\text{ cm}$", "$36\\text{ cm}$", "$24\\text{ cm}$", "$18\\text{ cm}$"),
            ('cauTN', "Trong một hình lục giác đều, số đo của mỗi góc bằng:", "$60^\\circ$", "$90^\\circ$", "$120^\\circ$", "$108^\\circ$"),
            ('cauTNB', "Trong thực tế, hình ảnh nào sau đây thường có dạng hình lục giác đều?", "Viên gạch lát nền", "Lỗ tổ ong", "Biển báo đường cấm", "Mặt bàn cờ vua"),
            ('cauTN', "Cho một tam giác đều có chu vi bằng $36\\text{ cm}$. Độ dài mỗi cạnh của tam giác đó là:", "$12\\text{ cm}$", "$9\\text{ cm}$", "$18\\text{ cm}$", "$6\\text{ cm}$")
        ],
        'c1': [
            ("a)", "$45 + 30 \\cdot 2 - 2^4$"),
            ("b)", "$36 \\cdot 58 + 36 \\cdot 42 - 600$"),
            ("c)", "$160 : [50 - (46 - 2^4)]$"),
            ("d)", "$400 : \\{ 180 - [55 + (8 - 3)^2] \\}$")
        ],
        'c2': [
            ("a)", "$42 + 5(x - 2) = 77$"),
            ("b)", "$140 - [60 - (x - 5)] = 105$"),
            ("c)", "$2 \\cdot 3^x - 8 = 46$"),
            ("d)", "Chu vi tam giác đều cạnh $x\\text{ (cm)}$ bằng $45\\text{ cm}$")
        ],
        'c3': {
            'context': "Bác Bình có một mảnh vườn trồng rau hình vuông có độ dài cạnh là $15\\text{ m}$. Bác Bình làm hàng rào dây thép gai xung quanh mảnh vườn và để lại một cổng vào rộng $3\\text{ m}$.",
            'a': "Tính chu vi của mảnh vườn hình vuông đó.",
            'b': "Tính chiều dài hàng rào dây thép gai cần làm và tổng chi phí, biết giá mỗi mét dây thép gai là $50\\,000\\text{ đồng}$."
        }
    },
    103: {
        'tn': [
            ('cauTN', "Mỗi góc của một tam giác đều có số đo bằng:", "$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$180^\\circ$"),
            ('cauTNB', "Khẳng định nào sau đây là \\textbf{sai} khi nói về hình vuông?", "Bốn cạnh bằng nhau", "Hai đường chéo vuông góc", "Hai đường chéo bằng nhau", "Bốn góc có số đo $60^\\circ$"),
            ('cauTNB', "Khẳng định nào sau đây là \\textbf{đúng} khi nói về lục giác đều?", "Có 6 cạnh bằng nhau, 6 góc bằng nhau", "Có 6 đường chéo chính", "Mỗi góc có số đo $60^\\circ$", "Không có tâm đối xứng"),
            ('cauTN', "Một khung tranh hình vuông có độ dài cạnh là $45\\text{ cm}$. Chu vi khung tranh đó là:", "$90\\text{ cm}$", "$180\\text{ cm}$", "$135\\text{ cm}$", "$200\\text{ cm}$"),
            ('cauTNB', "Hai đường chéo của một hình vuông có tính chất nào sau đây?", "Bằng nhau và vuông góc với nhau", "Bằng nhau nhưng không vuông góc", "Vuông góc nhưng không bằng nhau", "Song song với nhau")
        ],
        'c1': [
            ("a)", "$55 + 15 \\cdot 3 - 3^3$"),
            ("b)", "$47 \\cdot 73 + 47 \\cdot 27 - 700$"),
            ("c)", "$150 : [70 - (58 - 3^2 \\cdot 2)]$"),
            ("d)", "$500 : \\{ 200 - [75 + (9 - 4)^2] \\}$")
        ],
        'c2': [
            ("a)", "$28 + 3(x - 5) = 55$"),
            ("b)", "$150 - [70 - (x - 6)] = 115$"),
            ("c)", "$5 \\cdot 2^x - 15 = 65$"),
            ("d)", "Chu vi hình lục giác đều cạnh $x\\text{ (cm)}$ bằng $54\\text{ cm}$")
        ],
        'c3': {
            'context': "Nhà trường xây dựng một bồn hoa hình lục giác đều được ghép từ $6$ tam giác đều có cạnh bằng nhau, mỗi cạnh dài $3\\text{ m}$. Nhà trường muốn làm viền gạch bao quanh mép ngoài bồn hoa.",
            'a': "Tính chu vi của bồn hoa hình lục giác đều đó.",
            'b': "Tính tổng chi phí làm viền gạch trang trí, biết chi phí làm mỗi mét viền gạch là $120\\,000\\text{ đồng}$."
        }
    },
    104: {
        'tn': [
            ('cauTN', "Cho tam giác đều $MNP$ có cạnh $MN = 5\\text{ cm}$. Độ dài cạnh $NP$ là:", "$10\\text{ cm}$", "$15\\text{ cm}$", "$5\\text{ cm}$", "$25\\text{ cm}$"),
            ('cauTN', "Một hình vuông có chu vi là $28\\text{ cm}$. Độ dài cạnh hình vuông đó là:", "$14\\text{ cm}$", "$7\\text{ cm}$", "$8\\text{ cm}$", "$6\\text{ cm}$"),
            ('cauTNB', "Hình lục giác đều có cấu tạo gồm:", "$4$ tam giác đều ghép lại", "$5$ tam giác đều ghép lại", "$6$ tam giác đều ghép lại", "$8$ tam giác đều ghép lại"),
            ('cauTN', "Một mảnh bìa hình lục giác đều có độ dài mỗi cạnh là $8\\text{ cm}$. Chu vi mảnh bìa đó là:", "$24\\text{ cm}$", "$32\\text{ cm}$", "$48\\text{ cm}$", "$64\\text{ cm}$"),
            ('cauTNB', "Đặc điểm cơ bản của hình lục giác đều là:", "$6$ đỉnh, $6$ cạnh, $3$ đường chéo chính", "$6$ đỉnh, $5$ cạnh, $4$ đường chéo chính", "$8$ đỉnh, $6$ cạnh, $3$ đường chéo chính", "$6$ đỉnh, $6$ cạnh, $6$ đường chéo chính")
        ],
        'c1': [
            ("a)", "$65 + 20 \\cdot 3 - 2^5$"),
            ("b)", "$54 \\cdot 81 + 54 \\cdot 19 - 400$"),
            ("c)", "$210 : [60 - (48 - 3^2 \\cdot 2)]$"),
            ("d)", "$600 : \\{ 220 - [95 + (8 - 3)^2] \\}$")
        ],
        'c2': [
            ("a)", "$36 + 4(x - 6) = 68$"),
            ("b)", "$160 - [80 - (x - 8)] = 125$"),
            ("c)", "$4 \\cdot 3^x - 11 = 97$"),
            ("d)", "Chu vi hình vuông cạnh $x\\text{ (cm)}$ bằng $60\\text{ cm}$")
        ],
        'c3': {
            'context': "Một khu vui chơi có một bãi cát hình lục giác đều có độ dài mỗi cạnh là $4\\text{ m}$. Ban quản lý cần lắp đặt thanh xốp bảo vệ xung quanh mép ngoài bãi cát, chừa một lối ra vào rộng $2\\text{ m}$.",
            'a': "Tính chu vi của bãi cát hình lục giác đều đó.",
            'b': "Tính chiều dài thanh xốp bảo vệ cần lắp đặt và tổng chi phí, biết mỗi mét thanh xốp có giá $85\\,000\\text{ đồng}$."
        }
    }
}

tex_content = tex_header
for de in [101, 102, 103, 104]:
    data = de_data[de]
    tex_content += f"""
% =============================================================================
% ========================= TOÁN 6 - TUẦN 05 - BUỔI 01: MÃ ĐỀ {de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 05 - BUỔI 01}} & \\textbf{{Mã đề: {de} - Trang 1/2}} \\\\
\\textit{{Chủ đề: Bài 18: Tam giác đều, hình vuông}} & \\textit{{Thời gian: 45 phút}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\rule[-2.5mm]{{0pt}}{{8.5mm}}\\textbf{{Họ và tên học sinh:}} \\hfill \\textbf{{SĐT:}} \\makebox[4.5cm]{{\\dotfill}} \\\\
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

\\vspace{{1.5mm}}

\\noindent\\textbf{{\\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,5 điểm)}} \\hfill \\textit{{(Khoanh tròn đáp án đúng)}}
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
\\oBaiTap[8]{{{data['c1'][0][0]}}}{{{data['c1'][0][1]}}} & 
\\oBaiTap[8]{{{data['c1'][1][0]}}}{{{data['c1'][1][1]}}} \\\\
\\hline
\\oBaiTap[8]{{{data['c1'][2][0]}}}{{{data['c1'][2][1]}}} & 
\\oBaiTap[8]{{{data['c1'][3][0]}}}{{{data['c1'][3][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
% =============================================================================
% ========================= TOÁN 6 - TUẦN 05 - BUỔI 01: MÃ ĐỀ {de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHẦN II. TỰ LUẬN (Tiếp theo) - TOÁN 6 TUẦN 05 BUỔI 01}} & \\textbf{{Mã đề: {de} - Trang 2/2}} \\\\
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

target_file = os.path.join(os.path.dirname(__file__), 'Phieu_Kiem_Tra_Tuan_05_Buoi_01.tex')
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(tex_content)

print(f'{target_file} updated successfully')
