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
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 3, BC = 5$). Khi đó $\sin C =$", r"\dfrac{3}{5}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AC = 4, BC = 5$). Khi đó $\cos C =$", r"\dfrac{4}{5}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 3, AC = 4$). Khi đó $\tan B =$", r"\dfrac{4}{3}"),
            (r"Góc nhọn $\alpha$ có $\sin \alpha = 0{,}6$. Khi đó $\cos(90^\circ - \alpha) =$", r"0{,}6"),
            (r"Cột cờ cao $5\text{ m}$, bóng dài $5\text{ m}$. Góc của tia nắng và đất là:", r"45^\circ"),
            (r"Bóng cây dài $8\text{ m}$, tia nắng tạo góc $45^\circ$ với đất. Chiều cao cây:", r"8\text{ m}"),
            (r"Cách chân tháp $30\text{ m}$, góc nâng lên đỉnh tháp là $45^\circ$. Tháp cao:", r"30\text{ m}"),
            (r"Thang dài $4\text{ m}$ dựa tường tạo góc $60^\circ$. Chân thang cách tường:", r"2\text{ m}"),
            (r"Máy bay bay $4000\text{ m}$ theo góc $30^\circ$. Độ cao đạt được là:", r"2000\text{ m}"),
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B} = 30^\circ, BC = 10\text{ cm}$). Cạnh $AC =$", r"5\text{ cm}"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x - y = 5 \\ 2x + y = 5 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 3(x - 1) - 2y = 2 \\ 2(x + y) + y = 12 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x \ge 0, x \ne 1$:\par $A = \dfrac{x + 2}{x - 1} - \dfrac{\sqrt{x}}{\sqrt{x} + 1}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 2} - \dfrac{4}{x - 2\sqrt{x}}\right) : \dfrac{x - 4}{x}$"),
        ],
        "c13": r"Một mảnh đất hình chữ nhật có diện tích nhất định. Nếu tăng chiều dài thêm $3\text{ m}$ và giảm chiều rộng đi $2\text{ m}$ thì diện tích mảnh đất giảm $6\text{ m}^2$. Nếu giảm chiều dài đi $5\text{ m}$ và tăng chiều rộng thêm $5\text{ m}$ thì diện tích mảnh đất tăng thêm $25\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu của mảnh đất."
    },
    "102": {
        "sa": [
            (r"$\Delta ABC$ vuông tại $A$ ($AC = 4, BC = 5$). Khi đó $\sin B =$", r"\dfrac{4}{5}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 6, BC = 10$). Khi đó $\cos B =$", r"\dfrac{3}{5}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 4, AC = 3$). Khi đó $\tan B =$", r"\dfrac{3}{4}"),
            (r"Góc nhọn $\alpha$ có $\cos \alpha = 0{,}8$. Khi đó $\sin(90^\circ - \alpha) =$", r"0{,}8"),
            (r"Cột cờ cao $3\sqrt{3}\text{ m}$, bóng dài $3\text{ m}$. Góc của tia nắng và đất:", r"60^\circ"),
            (r"Bóng cây dài $6\sqrt{3}\text{ m}$, tia nắng tạo góc $30^\circ$ với đất. Cây cao:", r"6\text{ m}"),
            (r"Cách tòa nhà $40\text{ m}$, góc nâng lên đỉnh tòa nhà là $45^\circ$. Nhà cao:", r"40\text{ m}"),
            (r"Thang dài $6\text{ m}$ dựa tường tạo góc $60^\circ$. Chân thang cách tường:", r"3\text{ m}"),
            (r"Máy bay bay $6000\text{ m}$ theo góc $30^\circ$. Độ cao đạt được là:", r"3000\text{ m}"),
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B} = 30^\circ, BC = 12\text{ cm}$). Cạnh $AC =$", r"6\text{ cm}"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 7 \\ 3x - y = 8 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 2(x + 1) + 3y = 15 \\ 3(x - y) + y = 0 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x \ge 0, x \ne 1$:\par $A = \dfrac{x + 3}{x - 1} - \dfrac{\sqrt{x}}{\sqrt{x} + 1}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 3} - \dfrac{9}{x - 3\sqrt{x}}\right) : \dfrac{x - 9}{x}$"),
        ],
        "c13": r"Một khu vườn hình chữ nhật có diện tích nhất định. Nếu tăng chiều rộng thêm $5\text{ m}$ và giảm chiều dài đi $5\text{ m}$ thì diện tích khu vườn tăng thêm $50\text{ m}^2$. Nếu giảm chiều rộng đi $5\text{ m}$ và tăng chiều dài thêm $10\text{ m}$ thì diện tích khu vườn không thay đổi. Tính chiều dài và chiều rộng ban đầu của khu vườn."
    },
    "103": {
        "sa": [
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 5, BC = 13$). Khi đó $\sin C =$", r"\dfrac{5}{13}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AC = 12, BC = 13$). Khi đó $\cos C =$", r"\dfrac{12}{13}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 5, AC = 12$). Khi đó $\tan B =$", r"\dfrac{12}{5}"),
            (r"Góc nhọn $\alpha$ có $\sin \alpha = \dfrac{5}{13}$. Khi đó $\cos(90^\circ - \alpha) =$", r"\dfrac{5}{13}"),
            (r"Cột đèn cao $4\text{ m}$, bóng dài $4\sqrt{3}\text{ m}$. Góc của tia nắng và đất:", r"30^\circ"),
            (r"Bóng cây dài $4\sqrt{3}\text{ m}$, tia nắng tạo góc $30^\circ$ với đất. Cây cao:", r"4\text{ m}"),
            (r"Cách chân tháp $20\sqrt{3}\text{ m}$, góc nâng lên đỉnh tháp là $30^\circ$. Tháp cao:", r"20\text{ m}"),
            (r"Thang dài $5\text{ m}$ dựa tường tạo góc $60^\circ$. Chân thang cách tường:", r"2{,}5\text{ m}"),
            (r"Máy bay bay $5000\text{ m}$ theo góc $30^\circ$. Độ cao đạt được là:", r"2500\text{ m}"),
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B} = 60^\circ, AB = 4\text{ cm}$). Cạnh $BC =$", r"8\text{ cm}"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 4x - y = 7 \\ x + y = 3 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 3(x + y) + y = 18 \\ 2x - 3(y - 1) = -2 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x \ge 0, x \ne 4$:\par $A = \dfrac{x + 2}{x - 4} - \dfrac{\sqrt{x}}{\sqrt{x} + 2}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 1$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 1} - \dfrac{1}{x - \sqrt{x}}\right) : \dfrac{x - 1}{x}$"),
        ],
        "c13": r"Một thửa ruộng hình chữ nhật có diện tích nhất định. Nếu tăng chiều dài thêm $5\text{ m}$ và giảm chiều rộng đi $3\text{ m}$ thì diện tích thửa ruộng giảm $15\text{ m}^2$. Nếu giảm chiều dài đi $5\text{ m}$ và tăng chiều rộng thêm $5\text{ m}$ thì diện tích thửa ruộng tăng thêm $25\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu của thửa ruộng."
    },
    "104": {
        "sa": [
            (r"$\Delta ABC$ vuông tại $A$ ($AC = 12, BC = 13$). Khi đó $\sin B =$", r"\dfrac{12}{13}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 5, BC = 13$). Khi đó $\cos B =$", r"\dfrac{5}{13}"),
            (r"$\Delta ABC$ vuông tại $A$ ($AB = 12, AC = 5$). Khi đó $\tan B =$", r"\dfrac{5}{12}"),
            (r"Góc nhọn $\alpha$ có $\cos \alpha = \dfrac{12}{13}$. Khi đó $\sin(90^\circ - \alpha) =$", r"\dfrac{12}{13}"),
            (r"Cây cau cao $2\sqrt{3}\text{ m}$, bóng dài $2\text{ m}$. Góc của tia nắng và đất:", r"60^\circ"),
            (r"Bóng cây dài $10\text{ m}$, tia nắng tạo góc $45^\circ$ với đất. Chiều cao cây:", r"10\text{ m}"),
            (r"Cách chân tháp $10\sqrt{3}\text{ m}$, góc nâng lên đỉnh tháp là $60^\circ$. Tháp cao:", r"30\text{ m}"),
            (r"Thang dài $8\text{ m}$ dựa tường tạo góc $60^\circ$. Chân thang cách tường:", r"4\text{ m}"),
            (r"Máy bay bay $8000\text{ m}$ theo góc $30^\circ$. Độ cao đạt được là:", r"4000\text{ m}"),
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B} = 60^\circ, AB = 6\text{ cm}$). Cạnh $BC =$", r"12\text{ cm}"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x + y = 11 \\ 2x - y = 4 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 3(x + 1) + 2y = 13 \\ 2(x - y) - y = -2 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x \ge 0, x \ne 4$:\par $A = \dfrac{x + 4}{x - 4} - \dfrac{\sqrt{x}}{\sqrt{x} + 2}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 4} - \dfrac{16}{x - 4\sqrt{x}}\right) : \dfrac{x - 16}{x}$"),
        ],
        "c13": r"Một sân trường hình chữ nhật có diện tích nhất định. Nếu tăng chiều dài thêm $5\text{ m}$ và giảm chiều rộng đi $2\text{ m}$ thì diện tích sân trường tăng thêm $20\text{ m}^2$. Nếu giảm chiều dài đi $5\text{ m}$ và tăng chiều rộng thêm $4\text{ m}$ thì diện tích sân trường cũng tăng thêm $20\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu của sân trường."
    }
}

def render_code(code_str, d, ob11=20, vsa="0.7mm", ob12=13, dk13=20, vspace_mid="2.0mm"):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 06 - BUỔI 02: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 06 - BUỔI 02}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
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

\\vspace{{1.0mm}}
"""
    # 10 câu trả lời ngắn
    for idx, (quest, ans) in enumerate(d["sa"], 1):
        p1 += f"""\\noindent\\textbf{{Câu {idx} (0,25 điểm).}} {quest} \\shortans{{{ans}}}\\par\\vspace{{{vsa}}}
"""

    # Câu 11: 2 ý giải hệ phương trình
    p1 += f"""\\vspace{{0.5mm}}
\\noindent\\textbf{{Câu 11 (2,5 điểm). Giải các hệ phương trình sau:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{{d['c11'][0][0]}}}{{{d['c11'][0][1]}}} & 
\\oBaiTap[{ob11}]{{{d['c11'][1][0]}}}{{{d['c11'][1][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
"""

    # Trang 2
    c13_text = d['c13']
    p2 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 06 - BUỔI 02: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 9 - TUẦN 06 - BUỔI 02}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}

\\noindent\\textbf{{Câu 12 (2,5 điểm). Biến đổi và rút gọn biểu thức:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{{d['c12'][0][0]}}}{{{d['c12'][0][1]}}} & 
\\oBaiTap[{ob12}]{{{d['c12'][1][0]}}}{{{d['c12'][1][1]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_mid}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 13 (2,5 điểm).}} {c13_text}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

"""
    return p1 + p2

def generate_tex(ob11=20, vsa="0.7mm", ob12=13, dk13=20, vspace_mid="2.0mm"):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, ob12=ob12, dk13=dk13, vspace_mid=vspace_mid)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

if __name__ == "__main__":
    tex_code = generate_tex(ob11=20, vsa="0.7mm", ob12=13, dk13=20, vspace_mid="2.0mm")
    out_path = "Phieu_Kiem_Tra_Tuan_06_Buoi_02.tex"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"Xuat file {out_path} thanh cong!")
