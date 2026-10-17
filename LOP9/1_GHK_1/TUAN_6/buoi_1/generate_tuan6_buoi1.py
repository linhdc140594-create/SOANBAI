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
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 3, BC = 5$. Khi đó $\sin B =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 3, BC = 5$. Khi đó $\cos B =$", r"\dfrac{3}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 4, AC = 3$. Khi đó $\tan B =$", r"\dfrac{3}{4}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=4, CH=9$. Độ dài $AH$ là:", r"6"),
            (r"Một cột cờ cao $6\text{ m}$ có bóng trên mặt đất dài $6\text{ m}$. Góc tạo bởi tia nắng và mặt đất là:", r"45^\circ"),
            (r"Cặp $(1; y)$ là nghiệm của phương trình $2x + y = 5$. Khi đó $y =$", r"3"),
            (r"Tìm $m$ để cặp $(1; 2)$ là nghiệm phương trình $mx + y = 5$:", r"3"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 5$:", r"25"),
            (r"Nghiệm nguyên dương của phương trình $(x - 3)(x + 2) = 0$ là:", r"3"),
            (r"Nghiệm của phương trình $\sqrt{2x + 1} = 3$ là $x =$", r"4"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 2(x - 1) + y = 4 \\ 3x - 2y = 2 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $A = \dfrac{\sqrt{x}}{\sqrt{x} - 3} - \dfrac{9}{x - 3\sqrt{x}}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $B = \left(\dfrac{1}{\sqrt{x} - 2} + \dfrac{1}{\sqrt{x} + 2}\right) \cdot \dfrac{x - 4}{2\sqrt{x}}$"),
        ],
        "c13": {
            "p1": "3", "p2": "2", "s1": "34\\,000",
            "q1": "2", "q2": "4", "s2": "36\\,000",
        }
    },
    "102": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 6, BC = 10$. Khi đó $\sin B =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 6, BC = 10$. Khi đó $\cos B =$", r"\dfrac{3}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 8, AC = 6$. Khi đó $\tan B =$", r"\dfrac{3}{4}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=1, CH=4$. Độ dài $AH$ là:", r"2"),
            (r"Một cột đèn cao $5\text{ m}$ có bóng trên mặt đất dài $5\text{ m}$. Góc tạo bởi tia nắng và mặt đất là:", r"45^\circ"),
            (r"Cặp $(2; y)$ là nghiệm của phương trình $3x + y = 8$. Khi đó $y =$", r"2"),
            (r"Tìm $m$ để cặp $(2; 1)$ là nghiệm phương trình $mx + 2y = 8$:", r"3"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 6$:", r"36"),
            (r"Nghiệm nguyên dương của phương trình $(x - 5)(x + 1) = 0$ là:", r"5"),
            (r"Nghiệm của phương trình $\sqrt{3x + 1} = 4$ là $x =$", r"5"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x + y = 8 \\ x - y = 0 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 3(x + y) - 2x = 7 \\ 2x - y = 0 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $A = \dfrac{\sqrt{x}}{\sqrt{x} - 2} - \dfrac{4}{x - 2\sqrt{x}}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $B = \left(\dfrac{1}{\sqrt{x} - 3} + \dfrac{1}{\sqrt{x} + 3}\right) \cdot \dfrac{x - 9}{2\sqrt{x}}$"),
        ],
        "c13": {
            "p1": "4", "p2": "2", "s1": "42\\,000",
            "q1": "3", "q2": "5", "s2": "49\\,000",
        }
    },
    "103": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 5, BC = 13$. Khi đó $\sin B =$", r"\dfrac{12}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 5, BC = 13$. Khi đó $\cos B =$", r"\dfrac{5}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 12, AC = 5$. Khi đó $\tan B =$", r"\dfrac{5}{12}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=2, CH=8$. Độ dài $AH$ là:", r"4"),
            (r"Một cây cau cao $8\text{ m}$ có bóng trên mặt đất dài $8\text{ m}$. Góc tạo bởi tia nắng và mặt đất là:", r"45^\circ"),
            (r"Cặp $(1; y)$ là nghiệm của phương trình $4x + y = 7$. Khi đó $y =$", r"3"),
            (r"Tìm $m$ để cặp $(1; 3)$ là nghiệm phương trình $mx + y = 7$:", r"4"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 7$:", r"49"),
            (r"Nghiệm nguyên dương của phương trình $(x - 4)(x + 3) = 0$ là:", r"4"),
            (r"Nghiệm của phương trình $\sqrt{2x + 5} = 5$ là $x =$", r"10"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 8 \\ x - y = 1 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 2(x - y) + 3y = 7 \\ 3x + 2y = 11 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $A = \dfrac{\sqrt{x}}{\sqrt{x} - 4} - \dfrac{16}{x - 4\sqrt{x}}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 1$:\par $B = \left(\dfrac{1}{\sqrt{x} - 1} + \dfrac{1}{\sqrt{x} + 1}\right) \cdot \dfrac{x - 1}{2\sqrt{x}}$"),
        ],
        "c13": {
            "p1": "2", "p2": "3", "s1": "31\\,000",
            "q1": "5", "q2": "2", "s2": "50\\,000",
        }
    },
    "104": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 8, BC = 10$. Khi đó $\sin B =$", r"\dfrac{3}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 8, BC = 10$. Khi đó $\cos B =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 3, AC = 4$. Khi đó $\tan B =$", r"\dfrac{4}{3}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=3, CH=12$. Độ dài $AH$ là:", r"6"),
            (r"Một ngọn tháp cao $10\text{ m}$ có bóng trên mặt đất dài $10\text{ m}$. Góc tạo bởi tia nắng và mặt đất là:", r"45^\circ"),
            (r"Cặp $(2; y)$ là nghiệm của phương trình $2x + y = 6$. Khi đó $y =$", r"2"),
            (r"Tìm $m$ để cặp $(2; 2)$ là nghiệm phương trình $mx + y = 6$:", r"2"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 4$:", r"16"),
            (r"Nghiệm nguyên dương của phương trình $(x - 6)(x + 2) = 0$ là:", r"6"),
            (r"Nghiệm của phương trình $\sqrt{4x + 9} = 5$ là $x =$", r"4"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x + y = 10 \\ x - y = 2 \end{cases}$"),
            ("b) (1,25 điểm)", r"$\begin{cases} 3(x - 1) + 2y = 7 \\ 2x + y = 6 \end{cases}$"),
        ],
        "c12": [
            ("a) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 25$:\par $A = \dfrac{\sqrt{x}}{\sqrt{x} - 5} - \dfrac{25}{x - 5\sqrt{x}}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $B = \left(\dfrac{1}{\sqrt{x} - 4} + \dfrac{1}{\sqrt{x} + 4}\right) \cdot \dfrac{x - 16}{2\sqrt{x}}$"),
        ],
        "c13": {
            "p1": "3", "p2": "4", "s1": "44\\,000",
            "q1": "4", "q2": "2", "s2": "42\\,000",
        }
    }
}

def render_code(code_str, d, ob11=21, vsa="0.8mm", ob12=13, dk13=22, vspace_mid="2.5mm"):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
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

    # Câu 11: 2 ý giải hệ phương trình
    p1 += f"""\\vspace{{0.8mm}}
\\noindent\\textbf{{Câu 11 (2,5 điểm). Giải các hệ phương trình sau:}}
\\vspace{{0.6mm}}

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
    c13 = d['c13']
    p2 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 06 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 9 - TUẦN 06 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,5 điểm). Biến đổi và rút gọn biểu thức:}}
\\vspace{{0.6mm}}

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
\\textbf{{Câu 13 (2,5 điểm).}} Hai bạn An và Bình đến một nhà sách mua đồ dùng học tập. Bạn An mua ${c13['p1']}$ quyển vở và ${c13['p2']}$ chiếc bút bi cùng loại hết tổng cộng ${c13['s1']}$ đồng. Bạn Bình mua ${c13['q1']}$ quyển vở và ${c13['q2']}$ chiếc bút bi cùng loại hết tổng cộng ${c13['s2']}$ đồng. Tính giá tiền của mỗi quyển vở và mỗi chiếc bút bi.\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

"""
    return p1 + p2

def generate_tex(ob11=21, vsa="0.8mm", ob12=13, dk13=22, vspace_mid="2.5mm"):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, ob12=ob12, dk13=dk13, vspace_mid=vspace_mid)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

if __name__ == "__main__":
    tex_code = generate_tex(ob11=21, vsa="0.8mm", ob12=13, dk13=22, vspace_mid="2.5mm")
    out_path = "Phieu_Kiem_Tra_Tuan_06_Buoi_01.tex"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"Xuat file {out_path} thanh cong!")
