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
% ========================= TOÁN 8 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 8 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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

\\noindent\\textbf{{Câu 11 (2,0 điểm). Thực hiện phép tính và rút gọn biểu thức:}}
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
% ========================= TOÁN 8 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 8 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số thực $x$, biết:}}
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
            ("Bậc của đơn thức $5x^3 y^2 z$ là:", "6"),
            ("Bậc của đa thức $P = 2x^4 y - 3x^2 y^3 + x - 5$ là:", "5"),
            ("Giá trị của biểu thức $x^2 - 2xy + y^2$ tại $x = 12, y = 2$ bằng:", "100"),
            ("Điền số thích hợp vào chỗ trống: $(x + 4)^2 = x^2 + 8x + \\boxed{\\dots}$", "16"),
            ("Tính nhanh giá trị của biểu thức $52^2 - 48^2 = $", "400"),
            ("Rút gọn biểu thức $(x - 2)(x^2 + 2x + 4)$ rồi tính giá trị tại $x = 3$ được:", "19"),
            ("Kết quả của phép chia đơn thức $12x^5 y^3 : 4x^3 y$ là:", "3x^2 y^2"),
            ("Kết quả của phép chia đa thức $(6x^3 y^2 - 9x^2 y^2) : 3x^2 y^2$ là:", "2x - 3"),
            ("Tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 110^\\circ$. Số đo của góc $D$ bằng:", "100^\\circ"),
            ("Hình bình hành $ABCD$ có $\\widehat{A} = 70^\\circ$. Số đo của góc $B$ bằng:", "110^\\circ")
        ],
        'q11': {
            'a': '$2x(x - 3) - x(2x - 1)$',
            'b': '$(x - 2)(x + 3) - x(x + 1)$',
            'c': '$(x + 3)^2 - (x - 2)(x + 2) - 6x$',
            'd': '$(8x^4 y^3 - 12x^3 y^2 + 4x^2 y^2) : 4x^2 y^2$'
        },
        'q12': {
            'a': '$x(x - 2) - x^2 + 4x = 6$',
            'b': '$(x + 1)^2 - x(x - 2) = 9$',
            'c': '$(x + 3)^2 - (x - 2)(x + 2) = 25$',
            'd': '$(x - 1)(x^2 + x + 1) - x(x - 2)(x + 2) = 15$'
        },
        'q13': {
            'de': 'Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$). Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$, lấy điểm $D$ sao cho $MD = MA$.',
            'a': 'Chứng minh rằng tứ giác $ABDC$ là hình bình hành.',
            'b': 'Chứng minh tứ giác $ABDC$ là hình chữ nhật. Cho biết $AB = 6\\text{ cm}, AC = 8\\text{ cm}$, hãy tính độ dài đường chéo $AD$.'
        },
        'q14': {
            'de': 'Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 6x + 14$. Chỉ ra giá trị của $x$ để $A$ đạt giá trị nhỏ nhất đó.'
        }
    },
    '102': {
        'short': [
            ("Bậc của đơn thức $-4x^2 y^4 z$ là:", "7"),
            ("Bậc của đa thức $P = 3x^5 y - 4x^3 y^3 + 2y - 1$ là:", "6"),
            ("Giá trị của biểu thức $x^2 + 2xy + y^2$ tại $x = 17, y = 3$ bằng:", "400"),
            ("Điền số thích hợp vào chỗ trống: $(x + 5)^2 = x^2 + 10x + \\boxed{\\dots}$", "25"),
            ("Tính nhanh giá trị của biểu thức $63^2 - 37^2 = $", "2600"),
            ("Rút gọn biểu thức $(x - 3)(x^2 + 3x + 9)$ rồi tính giá trị tại $x = 4$ được:", "37"),
            ("Kết quả của phép chia đơn thức $15x^6 y^4 : 3x^4 y^2$ là:", "5x^2 y^2"),
            ("Kết quả của phép chia đa thức $(8x^3 y^2 - 10x^2 y^2) : 2x^2 y^2$ là:", "4x - 5"),
            ("Tứ giác $ABCD$ có $\\widehat{A} = 65^\\circ, \\widehat{B} = 85^\\circ, \\widehat{C} = 100^\\circ$. Số đo của góc $D$ bằng:", "110^\\circ"),
            ("Hình bình hành $ABCD$ có $\\widehat{A} = 65^\\circ$. Số đo của góc $B$ bằng:", "115^\\circ")
        ],
        'q11': {
            'a': '$3x(x - 2) - x(3x - 1)$',
            'b': '$(x - 3)(x + 4) - x(x + 1)$',
            'c': '$(x + 4)^2 - (x - 3)(x + 3) - 8x$',
            'd': '$(9x^4 y^3 - 15x^3 y^2 + 6x^2 y^2) : 3x^2 y^2$'
        },
        'q12': {
            'a': '$x(x - 3) - x^2 + 5x = 8$',
            'b': '$(x + 2)^2 - x(x - 2) = 16$',
            'c': '$(x + 2)^2 - (x - 3)(x + 3) = 21$',
            'd': '$(x + 1)(x^2 - x + 1) - x(x - 3)(x + 3) = 28$'
        },
        'q13': {
            'de': 'Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$). Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$, lấy điểm $D$ sao cho $MD = MA$.',
            'a': 'Chứng minh rằng tứ giác $ABDC$ là hình bình hành.',
            'b': 'Chứng minh tứ giác $ABDC$ là hình chữ nhật. Cho biết $AB = 5\\text{ cm}, AC = 12\\text{ cm}$, hãy tính độ dài đường chéo $AD$.'
        },
        'q14': {
            'de': 'Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 4x + 11$. Chỉ ra giá trị của $x$ để $A$ đạt giá trị nhỏ nhất đó.'
        }
    },
    '103': {
        'short': [
            ("Bậc của đơn thức $7x^3 y^3 z^2$ là:", "8"),
            ("Bậc của đa thức $P = 5x^3 y^2 - x^4 y^3 + 7x - 2$ là:", "7"),
            ("Giá trị của biểu thức $x^2 - 2xy + y^2$ tại $x = 23, y = 3$ bằng:", "400"),
            ("Điền số thích hợp vào chỗ trống: $(x - 6)^2 = x^2 - 12x + \\boxed{\\dots}$", "36"),
            ("Tính nhanh giá trị của biểu thức $74^2 - 26^2 = $", "4800"),
            ("Rút gọn biểu thức $(x + 2)(x^2 - 2x + 4)$ rồi tính giá trị tại $x = 3$ được:", "35"),
            ("Kết quả của phép chia đơn thức $18x^5 y^4 : 6x^3 y^3$ là:", "3x^2 y"),
            ("Kết quả của phép chia đa thức $(12x^3 y^2 - 8x^2 y^2) : 4x^2 y^2$ là:", "3x - 2"),
            ("Tứ giác $ABCD$ có $\\widehat{A} = 75^\\circ, \\widehat{B} = 95^\\circ, \\widehat{C} = 110^\\circ$. Số đo của góc $D$ bằng:", "80^\\circ"),
            ("Hình bình hành $ABCD$ có $\\widehat{A} = 80^\\circ$. Số đo của góc $B$ bằng:", "100^\\circ")
        ],
        'q11': {
            'a': '$4x(x - 2) - x(4x - 3)$',
            'b': '$(x - 1)(x + 2) - x(x + 1)$',
            'c': '$(x + 2)^2 - (x - 4)(x + 4) - 4x$',
            'd': '$(10x^4 y^3 - 14x^3 y^2 + 6x^2 y^2) : 2x^2 y^2$'
        },
        'q12': {
            'a': '$x(x - 4) - x^2 + 7x = 9$',
            'b': '$(x + 1)^2 - x(x - 3) = 11$',
            'c': '$(x + 3)^2 - (x - 1)(x + 1) = 22$',
            'd': '$(x - 2)(x^2 + 2x + 4) - x(x - 2)(x + 2) = 4$'
        },
        'q13': {
            'de': 'Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$). Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$, lấy điểm $D$ sao cho $MD = MA$.',
            'a': 'Chứng minh rằng tứ giác $ABDC$ là hình bình hành.',
            'b': 'Chứng minh tứ giác $ABDC$ là hình chữ nhật. Cho biết $AB = 8\\text{ cm}, AC = 15\\text{ cm}$, hãy tính độ dài đường chéo $AD$.'
        },
        'q14': {
            'de': 'Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 8x + 20$. Chỉ ra giá trị của $x$ để $A$ đạt giá trị nhỏ nhất đó.'
        }
    },
    '104': {
        'short': [
            ("Bậc của đơn thức $-2x^4 y^3 z$ là:", "8"),
            ("Bậc của đa thức $P = 4x^2 y^3 - 2x^5 y^2 + 3y^4 - 6$ là:", "7"),
            ("Giá trị của biểu thức $x^2 + 2xy + y^2$ tại $x = 28, y = 2$ bằng:", "900"),
            ("Điền số thích hợp vào chỗ trống: $(x - 7)^2 = x^2 - 14x + \\boxed{\\dots}$", "49"),
            ("Tính nhanh giá trị của biểu thức $85^2 - 15^2 = $", "7000"),
            ("Rút gọn biểu thức $(x + 1)(x^2 - x + 1)$ rồi tính giá trị tại $x = 4$ được:", "65"),
            ("Kết quả của phép chia đơn thức $20x^6 y^5 : 5x^4 y^3$ là:", "4x^2 y^2"),
            ("Kết quả của phép chia đa thức $(15x^3 y^2 - 10x^2 y^2) : 5x^2 y^2$ là:", "3x - 2"),
            ("Tứ giác $ABCD$ có $\\widehat{A} = 85^\\circ, \\widehat{B} = 75^\\circ, \\widehat{C} = 120^\\circ$. Số đo của góc $D$ bằng:", "80^\\circ"),
            ("Hình bình hành $ABCD$ có $\\widehat{A} = 75^\\circ$. Số đo của góc $B$ bằng:", "105^\\circ")
        ],
        'q11': {
            'a': '$2x(x - 4) - x(2x - 3)$',
            'b': '$(x - 4)(x + 5) - x(x + 1)$',
            'c': '$(x + 5)^2 - (x - 2)(x + 2) - 10x$',
            'd': '$(12x^4 y^3 - 16x^3 y^2 + 8x^2 y^2) : 4x^2 y^2$'
        },
        'q12': {
            'a': '$x(x - 5) - x^2 + 8x = 12$',
            'b': '$(x + 2)^2 - x(x - 1) = 19$',
            'c': '$(x + 2)^2 - (x - 4)(x + 4) = 32$',
            'd': '$(x + 2)(x^2 - 2x + 4) - x(x - 2)(x + 2) = 20$'
        },
        'q13': {
            'de': 'Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$). Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$, lấy điểm $D$ sao cho $MD = MA$.',
            'a': 'Chứng minh rằng tứ giác $ABDC$ là hình bình hành.',
            'b': 'Chứng minh tứ giác $ABDC$ là hình chữ nhật. Cho biết $AB = 9\\text{ cm}, AC = 12\\text{ cm}$, hãy tính độ dài đường chéo $AD$.'
        },
        'q14': {
            'de': 'Tìm giá trị nhỏ nhất của biểu thức $A = x^2 - 10x + 28$. Chỉ ra giá trị của $x$ để $A$ đạt giá trị nhỏ nhất đó.'
        }
    }
}

def generate_and_build(ob11=8, ob12=5, dk13=11, dk14=7):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    full_tex = tex_template
    for ma in ['101', '102', '103', '104']:
        d = de_data[ma]
        full_tex += render_de(ma, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11=ob11, ob12=ob12, dk13=dk13, dk14=dk14)
    full_tex += r'\end{document}' + '\n'

    tex_file = os.path.join(cur_dir, 'Phieu_Kiem_Tra_Tuan_06_Buoi_01.tex')
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(full_tex)
    print(f'Wrote LaTeX to {tex_file}')

    cmd = ['pdflatex', '-interaction=nonstopmode', 'Phieu_Kiem_Tra_Tuan_06_Buoi_01.tex']
    print("Compiling LaTeX...")
    res = subprocess.run(cmd, cwd=cur_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("LaTeX compilation had errors or warnings:")
        log_lines = res.stdout.splitlines()[-30:]
        print("\n".join(log_lines))
    else:
        print("Compilation successful!")

    pdf_file = os.path.join(cur_dir, 'Phieu_Kiem_Tra_Tuan_06_Buoi_01.pdf')
    if os.path.exists(pdf_file):
        reader = pypdf.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        print(f"Total pages in PDF: {num_pages}")
        return num_pages
    else:
        print("PDF file not found!")
        return -1

if __name__ == '__main__':
    generate_and_build()
