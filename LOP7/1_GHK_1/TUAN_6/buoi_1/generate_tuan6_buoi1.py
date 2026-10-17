import os
import subprocess

HEADER_TEMPLATE = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=3.2,heightSA=0.62}

\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ đều đặn chuẩn viết tay
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
"""

FOOTER_TEMPLATE = r"""\end{document}
"""

DATA = {
    "101": {
        "sa": [
            (r"Tìm căn bậc hai số học của $49$.", r"7"),
            (r"Tính giá trị của biểu thức: $|-4{,}5| + |2{,}5|$.", r"7"),
            (r"Làm tròn số $15{,}738$ đến chữ số thập phân thứ hai.", r"15{,}74"),
            (r"Cho góc $\widehat{AOB} = 65^\circ$. Số đo của góc kề bù với góc $\widehat{AOB}$ là:", r"115^\circ"),
            (r"Hai đường thẳng cắt nhau tạo thành một góc bằng $55^\circ$. Số đo góc đối đỉnh với nó là:", r"55^\circ"),
            (r"Cho tia $Oz$ là tia phân giác của góc $\widehat{xOy} = 70^\circ$. Số đo góc $\widehat{xOz}$ là:", r"35^\circ"),
            (r"Tính giá trị của biểu thức: $\left(-\dfrac{2}{3}\right)^2 + \dfrac{5}{9}$.", r"1"),
            (r"Cho $a // b$, một đường thẳng cắt $a$ và $b$. Biết một góc so le trong bằng $60^\circ$, số đo góc so le trong còn lại là:", r"60^\circ"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 5$.", r"25"),
            (r"Một chiếc cặp giá $200\,000$ đồng được giảm giá $10\%$. Số tiền được giảm là (đồng):", r"20\,000"),
        ],
        "c11": [
            ("a)", r"$\dfrac{3}{7} + \left(-\dfrac{5}{2}\right) + \dfrac{4}{7}$"),
            ("b)", r"$\dfrac{4}{9} \cdot \left(-\dfrac{5}{13}\right) + \dfrac{4}{9} \cdot \left(-\dfrac{8}{13}\right)$"),
            ("c)", r"$\left(-\dfrac{1}{2}\right)^3 : \dfrac{1}{4} + 2{,}5 \cdot (-2)$"),
            ("d)", r"$\sqrt{\dfrac{25}{4}} - |-1{,}5| + \sqrt{16}$"),
        ],
        "c12": [
            ("a)", r"$x + \dfrac{2}{3} = \dfrac{5}{6}$"),
            ("b)", r"$\dfrac{3}{4}x - \dfrac{1}{2} = \dfrac{1}{4}$"),
            ("c)", r"$\left(x - \dfrac{1}{2}\right)^2 = \dfrac{9}{16}$"),
            ("d)", r"$|2x - 1| = 3$"),
        ],
        "c13": {
            "alpha": "60^\\circ",
        },
        "c14": {
            "expr": r"A = |x - 3| + 2026",
        }
    },
    "102": {
        "sa": [
            (r"Tìm căn bậc hai số học của $81$.", r"9"),
            (r"Tính giá trị của biểu thức: $|-3{,}8| + |2{,}2|$.", r"6"),
            (r"Làm tròn số $24{,}816$ đến chữ số thập phân thứ hai.", r"24{,}82"),
            (r"Cho góc $\widehat{AOB} = 75^\circ$. Số đo của góc kề bù với góc $\widehat{AOB}$ là:", r"105^\circ"),
            (r"Hai đường thẳng cắt nhau tạo thành một góc bằng $68^\circ$. Số đo góc đối đỉnh với nó là:", r"68^\circ"),
            (r"Cho tia $Oz$ là tia phân giác của góc $\widehat{xOy} = 84^\circ$. Số đo góc $\widehat{xOz}$ là:", r"42^\circ"),
            (r"Tính giá trị của biểu thức: $\left(-\dfrac{3}{4}\right)^2 + \dfrac{7}{16}$.", r"1"),
            (r"Cho $a // b$, biết một góc đồng vị có số đo bằng $70^\circ$, số đo góc đồng vị tương ứng là:", r"70^\circ"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 7$.", r"49"),
            (r"Một chiếc áo giá $300\,000$ đồng được giảm giá $10\%$. Số tiền được giảm là (đồng):", r"30\,000"),
        ],
        "c11": [
            ("a)", r"$\dfrac{2}{9} + \left(-\dfrac{7}{3}\right) + \dfrac{7}{9}$"),
            ("b)", r"$\dfrac{5}{8} \cdot \left(-\dfrac{7}{15}\right) + \dfrac{5}{8} \cdot \left(-\dfrac{8}{15}\right)$"),
            ("c)", r"$\left(-\dfrac{1}{3}\right)^2 : \dfrac{1}{9} - 1{,}5 \cdot 4$"),
            ("d)", r"$\sqrt{\dfrac{49}{4}} - |-2{,}5| + \sqrt{25}$"),
        ],
        "c12": [
            ("a)", r"$x + \dfrac{3}{4} = \dfrac{7}{8}$"),
            ("b)", r"$\dfrac{2}{3}x - \dfrac{1}{6} = \dfrac{1}{2}$"),
            ("c)", r"$\left(x - \dfrac{1}{3}\right)^2 = \dfrac{4}{9}$"),
            ("d)", r"$|2x - 3| = 5$"),
        ],
        "c13": {
            "alpha": "70^\\circ",
        },
        "c14": {
            "expr": r"A = |x - 5| + 2025",
        }
    },
    "103": {
        "sa": [
            (r"Tìm căn bậc hai số học của $64$.", r"8"),
            (r"Tính giá trị của biểu thức: $|-5{,}4| + |2{,}6|$.", r"8"),
            (r"Làm tròn số $18{,}364$ đến chữ số thập phân thứ hai.", r"18{,}36"),
            (r"Cho góc $\widehat{AOB} = 50^\circ$. Số đo của góc kề bù với góc $\widehat{AOB}$ là:", r"130^\circ"),
            (r"Hai đường thẳng cắt nhau tạo thành một góc bằng $42^\circ$. Số đo góc đối đỉnh với nó là:", r"42^\circ"),
            (r"Cho tia $Oz$ là tia phân giác của góc $\widehat{xOy} = 96^\circ$. Số đo góc $\widehat{xOz}$ là:", r"48^\circ"),
            (r"Tính giá trị của biểu thức: $\left(-\dfrac{1}{2}\right)^3 + \dfrac{9}{8}$.", r"1"),
            (r"Cho $a // b$, biết một góc so le trong bằng $55^\circ$, số đo góc so le trong còn lại là:", r"55^\circ"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 8$.", r"64"),
            (r"Một đôi giày giá $400\,000$ đồng được giảm giá $10\%$. Số tiền được giảm là (đồng):", r"40\,000"),
        ],
        "c11": [
            ("a)", r"$\dfrac{4}{11} + \left(-\dfrac{5}{2}\right) + \dfrac{7}{11}$"),
            ("b)", r"$\dfrac{3}{7} \cdot \left(-\dfrac{9}{17}\right) + \dfrac{3}{7} \cdot \left(-\dfrac{8}{17}\right)$"),
            ("c)", r"$\left(-\dfrac{1}{2}\right)^2 \cdot 8 - 3{,}5 \cdot 2$"),
            ("d)", r"$\sqrt{\dfrac{81}{4}} - |-3{,}5| + \sqrt{36}$"),
        ],
        "c12": [
            ("a)", r"$x - \dfrac{1}{3} = \dfrac{1}{6}$"),
            ("b)", r"$\dfrac{4}{5}x + \dfrac{1}{5} = 1$"),
            ("c)", r"$\left(x + \dfrac{1}{2}\right)^2 = \dfrac{25}{16}$"),
            ("d)", r"$|2x + 1| = 5$"),
        ],
        "c13": {
            "alpha": "50^\\circ",
        },
        "c14": {
            "expr": r"A = |x + 4| + 2026",
        }
    },
    "104": {
        "sa": [
            (r"Tìm căn bậc hai số học của $100$.", r"10"),
            (r"Tính giá trị của biểu thức: $|-6{,}3| + |2{,}7|$.", r"9"),
            (r"Làm tròn số $32{,}645$ đến chữ số thập phân thứ hai.", r"32{,}65"),
            (r"Cho góc $\widehat{AOB} = 80^\circ$. Số đo của góc kề bù với góc $\widehat{AOB}$ là:", r"100^\circ"),
            (r"Hai đường thẳng cắt nhau tạo thành một góc bằng $72^\circ$. Số đo góc đối đỉnh với nó là:", r"72^\circ"),
            (r"Cho tia $Oz$ là tia phân giác của góc $\widehat{xOy} = 64^\circ$. Số đo góc $\widehat{xOz}$ là:", r"32^\circ"),
            (r"Tính giá trị của biểu thức: $\left(-\dfrac{2}{5}\right)^2 + \dfrac{21}{25}$.", r"1"),
            (r"Cho $a // b$, biết một góc đồng vị có số đo bằng $80^\circ$, số đo góc đồng vị tương ứng là:", r"80^\circ"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 6$.", r"36"),
            (r"Một quyển sách giá $150\,000$ đồng được giảm giá $10\%$. Số tiền được giảm là (đồng):", r"15\,000"),
        ],
        "c11": [
            ("a)", r"$\dfrac{5}{13} + \left(-\dfrac{8}{3}\right) + \dfrac{8}{13}$"),
            ("b)", r"$\dfrac{7}{12} \cdot \left(-\dfrac{11}{19}\right) + \dfrac{7}{12} \cdot \left(-\dfrac{8}{19}\right)$"),
            ("c)", r"$\left(-\dfrac{2}{3}\right)^2 : \dfrac{4}{9} + 4{,}5 \cdot (-2)$"),
            ("d)", r"$\sqrt{\dfrac{121}{4}} - |-4{,}5| + \sqrt{9}$"),
        ],
        "c12": [
            ("a)", r"$x - \dfrac{2}{5} = \dfrac{3}{10}$"),
            ("b)", r"$\dfrac{5}{6}x - \dfrac{1}{3} = \dfrac{1}{2}$"),
            ("c)", r"$\left(x - \dfrac{1}{4}\right)^2 = \dfrac{9}{16}$"),
            ("d)", r"$|2x - 5| = 3$"),
        ],
        "c13": {
            "alpha": "80^\\circ",
        },
        "c14": {
            "expr": r"A = |x - 7| + 2024",
        }
    }
}

def render_code(code_str, d, ob11=9, vsa="0.8mm", ob12=5, dk13=13, dk14=8):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 7 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}
"""
    # 10 câu trả lời ngắn
    for idx, (quest, ans) in enumerate(d["sa"], 1):
        p1 += f"""\\noindent\\textbf{{Câu {idx} (0,25 điểm).}} {quest} \\shortans{{{ans}}}\\par\\vspace{{{vsa}}}
"""

    # Câu 11
    p1 += f"""\\vspace{{0.8mm}}
\\noindent\\textbf{{Câu 11 (2,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{{d['c11'][0][0]}}}{{{d['c11'][0][1]}}} & 
\\oBaiTap[{ob11}]{{{d['c11'][1][0]}}}{{{d['c11'][1][1]}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{{d['c11'][2][0]}}}{{{d['c11'][2][1]}}} & 
\\oBaiTap[{ob11}]{{{d['c11'][3][0]}}}{{{d['c11'][3][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
"""

    # Trang 2
    p2 = f"""% =============================================================================
% ========================= TOÁN 7 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 7 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số hữu tỉ $x$, biết:}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{{d['c12'][0][0]}}}{{{d['c12'][0][1]}}} & 
\\oBaiTap[{ob12}]{{{d['c12'][1][0]}}}{{{d['c12'][1][1]}}} \\\\
\\hline
\\oBaiTap[{ob12}]{{{d['c12'][2][0]}}}{{{d['c12'][2][1]}}} & 
\\oBaiTap[{ob12}]{{{d['c12'][3][0]}}}{{{d['c12'][3][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 13 (2,5 điểm).}} Cho hai góc kề bù $\\widehat{{xOy}}$ và $\\widehat{{yOz}}$. Biết $\\widehat{{xOy}} = {d['c13']['alpha']}$.\\par
\\textbf{{a) (1,25 điểm)}} Tính số đo góc $\\widehat{{yOz}}$.\\par
\\textbf{{b) (1,25 điểm)}} Vẽ tia $Om$ là tia phân giác của góc $\\widehat{{yOz}}$. Tính số đo góc $\\widehat{{xOm}}$.\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (1,0 điểm).}} Tìm giá trị nhỏ nhất của biểu thức ${d['c14']['expr']}$. Chỉ ra giá trị của $x$ để biểu thức đạt giá trị nhỏ nhất đó.\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}

"""
    return p1 + p2

def generate_tex(ob11=9, vsa="0.8mm", ob12=5, dk13=13, dk14=8):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, ob12=ob12, dk13=dk13, dk14=dk14)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

if __name__ == "__main__":
    tex_code = generate_tex(ob11=9, vsa="0.8mm", ob12=5, dk13=13, dk14=8)
    out_path = "Phieu_Kiem_Tra_Tuan_06_Buoi_01.tex"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"Đã xuất file {out_path} thành công!")
