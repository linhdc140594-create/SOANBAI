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
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=12\text{ cm}$). Cạnh $AC =$", r"6\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{3}{5}$. Khi đó $\cos \alpha =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=4, CH=9$. Khi đó $AH =$", r"6"),
            (r"Rút gọn biểu thức $\sqrt{(2 - \sqrt{5})^2}$ được kết quả:", r"\sqrt{5} - 2"),
            (r"Biểu thức $\sqrt{3x - 6}$ xác định khi:", r"x \ge 2"),
            (r"Giá trị của biểu thức $\sqrt{18} : \sqrt{2} + \sqrt{16}$ là:", r"7"),
            (r"Nghiệm của phương trình $\sqrt{2x - 1} = 3$ là $x =$", r"5"),
            (r"Thang dài $5\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"2{,}5\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$ là $(x; y) =$", r"(3; 2)"),
            (r"Giá trị $\sin^2 10^\circ + \dots + \sin^2 80^\circ$ (8 số hạng) là:", r"4"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + 3y = 12 \\ 3x - y = 7 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $P = \left(\dfrac{1}{\sqrt{x}-2} + \dfrac{1}{\sqrt{x}+2}\right) \cdot \dfrac{x-4}{\sqrt{x}}$"),
        ],
        "c12": {
            "text": r"Hai xe máy cùng khởi hành một lúc từ hai địa điểm $A$ và $B$ cách nhau $90\text{ km}$, đi ngược chiều nhau và gặp nhau sau $1{,}5$ giờ. Biết rằng vận tốc của xe đi từ $A$ lớn hơn vận tốc của xe đi từ $B$ là $10\text{ km/h}$. Tính vận tốc của mỗi xe máy."
        },
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 12\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AC, AB$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh rằng: $AD \cdot AB = AE \cdot AC$."
        }
    },
    "102": {
        "sa": [
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=16\text{ cm}$). Cạnh $AC =$", r"8\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{3}{5}$. Khi đó $\sin \alpha =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=2, CH=8$. Khi đó $AH =$", r"4"),
            (r"Rút gọn biểu thức $\sqrt{(3 - \sqrt{10})^2}$ được kết quả:", r"\sqrt{10} - 3"),
            (r"Biểu thức $\sqrt{2x - 8}$ xác định khi:", r"x \ge 4"),
            (r"Giá trị của biểu thức $\sqrt{50} : \sqrt{2} - \sqrt{9}$ là:", r"2"),
            (r"Nghiệm của phương trình $\sqrt{3x + 1} = 4$ là $x =$", r"5"),
            (r"Thang dài $6\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"3\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 6 \\ x - y = 2 \end{cases}$ là $(x; y) =$", r"(4; 2)"),
            (r"Giá trị $\cos^2 10^\circ + \dots + \cos^2 80^\circ$ (8 số hạng) là:", r"4"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x + 2y = 13 \\ 2x - y = 4 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $P = \left(\dfrac{1}{\sqrt{x}-3} + \dfrac{1}{\sqrt{x}+3}\right) \cdot \dfrac{x-9}{\sqrt{x}}$"),
        ],
        "c12": {
            "text": r"Hai ô tô khởi hành cùng một lúc từ hai địa điểm $A$ và $B$ cách nhau $120\text{ km}$, đi ngược chiều nhau và gặp nhau sau $1{,}5$ giờ. Biết vận tốc ô tô đi từ $A$ lớn hơn vận tốc ô tô đi từ $B$ là $20\text{ km/h}$. Tính vận tốc của mỗi ô tô."
        },
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 10\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$."
        }
    },
    "103": {
        "sa": [
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=14\text{ cm}$). Cạnh $AC =$", r"7\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{5}{13}$. Khi đó $\cos \alpha =$", r"\dfrac{12}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=1, CH=9$. Khi đó $AH =$", r"3"),
            (r"Rút gọn biểu thức $\sqrt{(1 - \sqrt{3})^2}$ được kết quả:", r"\sqrt{3} - 1"),
            (r"Biểu thức $\sqrt{4x - 12}$ xác định khi:", r"x \ge 3"),
            (r"Giá trị của biểu thức $\sqrt{75} : \sqrt{3} + \sqrt{25}$ là:", r"10"),
            (r"Nghiệm của phương trình $\sqrt{4x + 1} = 5$ là $x =$", r"6"),
            (r"Thang dài $4\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"2\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 7 \\ x - y = 1 \end{cases}$ là $(x; y) =$", r"(4; 3)"),
            (r"Giá trị $\sin^2 15^\circ + \sin^2 35^\circ + \sin^2 55^\circ + \sin^2 75^\circ$ là:", r"2"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 7 \\ 3x + 2y = 12 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 1$:\par $P = \left(\dfrac{1}{\sqrt{x}-1} + \dfrac{1}{\sqrt{x}+1}\right) \cdot \dfrac{x-1}{\sqrt{x}}$"),
        ],
        "c12": {
            "text": r"Hai người đi xe đạp cùng khởi hành một lúc từ hai địa điểm $A$ và $B$ cách nhau $48\text{ km}$, đi ngược chiều nhau và gặp nhau sau $2$ giờ. Biết vận tốc người đi từ $A$ lớn hơn vận tốc người đi từ $B$ là $4\text{ km/h}$. Tính vận tốc của mỗi người."
        },
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 8\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AC, AB$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh rằng: $AD \cdot AB = AE \cdot AC$."
        }
    },
    "104": {
        "sa": [
            (r"$\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=18\text{ cm}$). Cạnh $AC =$", r"9\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{5}{13}$. Khi đó $\sin \alpha =$", r"\dfrac{12}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$, đường cao $AH$. Biết $BH=3, CH=12$. Khi đó $AH =$", r"6"),
            (r"Rút gọn biểu thức $\sqrt{(2 - \sqrt{7})^2}$ được kết quả:", r"\sqrt{7} - 2"),
            (r"Biểu thức $\sqrt{5x - 15}$ xác định khi:", r"x \ge 3"),
            (r"Giá trị của biểu thức $\sqrt{48} : \sqrt{3} - \sqrt{4}$ là:", r"2"),
            (r"Nghiệm của phương trình $\sqrt{2x + 5} = 5$ là $x =$", r"10"),
            (r"Thang dài $8\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"4\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 8 \\ x - y = 2 \end{cases}$ là $(x; y) =$", r"(5; 3)"),
            (r"Giá trị $\cos^2 15^\circ + \cos^2 35^\circ + \cos^2 55^\circ + \cos^2 75^\circ$ là:", r"2"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x - 2y = 5 \\ x + 2y = 7 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $P = \left(\dfrac{1}{\sqrt{x}-4} + \dfrac{1}{\sqrt{x}+4}\right) \cdot \dfrac{x-16}{\sqrt{x}}$"),
        ],
        "c12": {
            "text": r"Hai xe máy khởi hành cùng một lúc từ hai địa điểm $A$ và $B$ cách nhau $100\text{ km}$, đi ngược chiều nhau và gặp nhau sau $1{,}25$ giờ (tức $1$ giờ $15$ phút). Biết vận tốc xe đi từ $A$ lớn hơn vận tốc xe đi từ $B$ là $16\text{ km/h}$. Tính vận tốc của mỗi xe."
        },
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 12\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$."
        }
    }
}

def render_code(code_str, d, ob11=20, vsa="0.6mm", dk12=16, dk13=17, vspace_mid="2.0mm"):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 07 - BUỔI 02: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 07 - BUỔI 02}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
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

    # Câu 11: 2 ý
    p1 += f"""\\vspace{{0.8mm}}
\\noindent\\textbf{{Câu 11 (2,5 điểm). Đại số tổng hợp:}}
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
    c12 = d['c12']
    c13 = d['c13']
    p2 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 07 - BUỔI 02: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 9 - TUẦN 07 - BUỔI 02}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 12 (2,5 điểm).}} {c12['text']}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk12}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{{vspace_mid}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 13 (2,5 điểm).}} {c13['gt']}\\par
{c13['a']}\\par
{c13['b']}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

"""
    return p1 + p2

def generate_tex(ob11=20, vsa="0.6mm", dk12=16, dk13=17, vspace_mid="2.0mm"):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

if __name__ == "__main__":
    tex_code = generate_tex(ob11=20, vsa="0.6mm", dk12=16, dk13=17, vspace_mid="2.0mm")
    out_path = "Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"Xuat file {out_path} thanh cong!")
