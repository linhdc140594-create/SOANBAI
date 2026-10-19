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

% Định nghĩa khu vực bài làm chia 2 cột có vách ngăn mờ ở giữa
\newcommand{\dongkeHaiCot}[1]{%
  \par\vspace{0.5mm}%
  \noindent%
  \begin{minipage}[t]{0.485\linewidth}%
    \dongke{#1}%
  \end{minipage}%
  \hfill%
  {\color{gray!60}\vrule}%
  \hfill%
  \begin{minipage}[t]{0.485\linewidth}%
    \dongke{#1}%
  \end{minipage}%
}

\begin{document}
\pagestyle{empty}
"""

FOOTER_TEMPLATE = r"""\end{document}
"""

DATA = {
    "101": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 6, BC = 10$. Khi đó $\sin C =$", r"\dfrac{3}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AC = 8, BC = 10$. Khi đó $\cos C =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 3, AC = 4$. Khi đó $\tan B =$", r"\dfrac{4}{3}"),
            (r"Cho góc nhọn $\alpha$ có $\sin \alpha = 0{,}75$. Khi đó $\cos(90^\circ - \alpha) =$", r"0{,}75"),
            (r"Giá trị của biểu thức $\sin^2 25^\circ + \sin^2 65^\circ$ bằng:", r"1"),
            (r"Giá trị của biểu thức $\tan 45^\circ - 2\sin 30^\circ$ bằng:", r"0"),
            (r"Cột cờ cao $7\text{ m}$ có bóng trên mặt đất dài $7\text{ m}$. Góc của tia nắng là:", r"45^\circ"),
            (r"Cặp $(1; y)$ là nghiệm của phương trình $3x + y = 7$. Khi đó $y =$", r"4"),
            (r"Tìm $m$ để cặp $(2; 1)$ là nghiệm của phương trình $mx + 3y = 7$:", r"2"),
            (r"Nghiệm dương của phương trình $(x - 4)(x + 1) = 0$ là:", r"4"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 8 \\ 3x - y = 7 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}-2} - \dfrac{4}{x-2\sqrt{x}}\right) : \dfrac{\sqrt{x}+2}{\sqrt{x}}$"),
        ],
        "c12": r"Hai tổ sản xuất cùng làm chung một công việc thì sau $12$ giờ sẽ hoàn thành. Nếu tổ I làm trong $4$ giờ rồi tổ II làm tiếp trong $7$ giờ thì cả hai tổ hoàn thành được $\dfrac{1}{2}$ công việc. Hỏi nếu làm riêng thì mỗi tổ mất bao lâu để hoàn thành xong công việc?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 6\text{ cm}, BC = 10\text{ cm}$.",
            "a": r"\textbf{a) (1,5 điểm)} Tính độ dài cạnh $AC$, số đo góc $B$ (làm tròn đến độ) và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HE \perp AB$ tại $E$ và $HF \perp AC$ tại $F$. Chứng minh rằng: $AE \cdot AB = AF \cdot AC$."
        }
    },
    "102": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 8, BC = 10$. Khi đó $\sin C =$", r"\dfrac{4}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AC = 6, BC = 10$. Khi đó $\cos C =$", r"\dfrac{3}{5}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 4, AC = 3$. Khi đó $\tan B =$", r"\dfrac{3}{4}"),
            (r"Cho góc nhọn $\alpha$ có $\cos \alpha = 0{,}65$. Khi đó $\sin(90^\circ - \alpha) =$", r"0{,}65"),
            (r"Giá trị của biểu thức $\cos^2 35^\circ + \cos^2 55^\circ$ bằng:", r"1"),
            (r"Giá trị của biểu thức $2\cos 60^\circ - \cot 45^\circ$ bằng:", r"0"),
            (r"Bóng cây dài $12\text{ m}$, tia nắng tạo góc $45^\circ$ với đất. Chiều cao cây là:", r"12\text{ m}"),
            (r"Cặp $(2; y)$ là nghiệm của phương trình $2x + y = 9$. Khi đó $y =$", r"5"),
            (r"Tìm $m$ để cặp $(1; 3)$ là nghiệm của phương trình $mx + 2y = 8$:", r"2"),
            (r"Nghiệm dương của phương trình $(x - 5)(x + 3) = 0$ là:", r"5"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x - y = 5 \\ x + y = 7 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}-3} - \dfrac{9}{x-3\sqrt{x}}\right) : \dfrac{\sqrt{x}+3}{\sqrt{x}}$"),
        ],
        "c12": r"Hai đội công nhân cùng sửa một đoạn đường thì sau $12$ ngày sẽ hoàn thành. Nếu đội thứ nhất làm trong $3$ ngày rồi đội thứ hai làm tiếp trong $8$ ngày thì cả hai đội hoàn thành được $\dfrac{1}{2}$ đoạn đường. Hỏi nếu làm một mình thì mỗi đội mất bao lâu để hoàn thành đoạn đường đó?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AC = 8\text{ cm}, BC = 10\text{ cm}$.",
            "a": r"\textbf{a) (1,5 điểm)} Tính độ dài cạnh $AB$, số đo góc $C$ (làm tròn đến độ) và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HE \perp AB$ tại $E$ và $HF \perp AC$ tại $F$. Chứng minh tứ giác $AEHF$ là hình chữ nhật và suy ra $EF = AH$."
        }
    },
    "103": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 5, BC = 13$. Khi đó $\sin C =$", r"\dfrac{5}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AC = 12, BC = 13$. Khi đó $\cos C =$", r"\dfrac{12}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 5, AC = 12$. Khi đó $\tan B =$", r"\dfrac{12}{5}"),
            (r"Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{5}{13}$. Khi đó $\cos(90^\circ - \alpha) =$", r"\dfrac{5}{13}"),
            (r"Giá trị của biểu thức $\sin^2 40^\circ + \sin^2 50^\circ$ bằng:", r"1"),
            (r"Giá trị của biểu thức $\sqrt{3}\tan 30^\circ - 1$ bằng:", r"0"),
            (r"Cách chân hải đăng $25\text{ m}$, góc nhìn lên đỉnh là $45^\circ$. Hải đăng cao:", r"25\text{ m}"),
            (r"Cặp $(3; y)$ là nghiệm của phương trình $x + 2y = 7$. Khi đó $y =$", r"2"),
            (r"Tìm $m$ để cặp $(3; 1)$ là nghiệm của phương trình $mx + 4y = 10$:", r"2"),
            (r"Nghiệm dương của phương trình $(x - 7)(x + 2) = 0$ là:", r"7"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 9 \\ x - y = 3 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 1$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}-1} - \dfrac{1}{x-\sqrt{x}}\right) : \dfrac{\sqrt{x}+1}{\sqrt{x}}$"),
        ],
        "c12": r"Hai người thợ cùng làm chung một công việc thì sau $16$ giờ sẽ hoàn thành. Nếu người thứ nhất làm trong $3$ giờ rồi người thứ hai làm tiếp trong $6$ giờ thì cả hai người làm được $\dfrac{1}{4}$ công việc. Hỏi nếu làm riêng thì mỗi người mất bao lâu để hoàn thành xong công việc?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 5\text{ cm}, BC = 13\text{ cm}$.",
            "a": r"\textbf{a) (1,5 điểm)} Tính độ dài cạnh $AC$, số đo góc $B$ (làm tròn đến độ) và độ dài đường cao $AH$ (làm tròn đến chữ số thập phân thứ nhất).",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HE \perp AB$ tại $E$ và $HF \perp AC$ tại $F$. Chứng minh rằng: $AE \cdot AB = AF \cdot AC$."
        }
    },
    "104": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 12, BC = 13$. Khi đó $\sin C =$", r"\dfrac{12}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AC = 5, BC = 13$. Khi đó $\cos C =$", r"\dfrac{5}{13}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 12, AC = 5$. Khi đó $\tan B =$", r"\dfrac{5}{12}"),
            (r"Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{7}{25}$. Khi đó $\sin(90^\circ - \alpha) =$", r"\dfrac{7}{25}"),
            (r"Giá trị của biểu thức $\cos^2 20^\circ + \cos^2 70^\circ$ bằng:", r"1"),
            (r"Giá trị của biểu thức $\tan 45^\circ - \sqrt{3}\cot 60^\circ$ bằng:", r"0"),
            (r"Thang dài $6\text{ m}$ dựa tường tạo góc $60^\circ$. Chân thang cách tường:", r"3\text{ m}"),
            (r"Cặp $(1; y)$ là nghiệm của phương trình $4x + y = 10$. Khi đó $y =$", r"6"),
            (r"Tìm $m$ để cặp $(2; 2)$ là nghiệm của phương trình $mx + y = 8$:", r"3"),
            (r"Nghiệm dương của phương trình $(x - 6)(x + 4) = 0$ là:", r"6"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x + y = 11 \\ 2x - y = 4 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}-4} - \dfrac{16}{x-4\sqrt{x}}\right) : \dfrac{\sqrt{x}+4}{\sqrt{x}}$"),
        ],
        "c12": r"Hai tổ công nhân cùng làm chung một công việc thì sau $15$ ngày sẽ hoàn thành. Nếu tổ I làm trong $3$ ngày rồi tổ II làm tiếp trong $5$ ngày thì cả hai tổ hoàn thành được $\dfrac{1}{4}$ công việc. Hỏi nếu làm một mình thì mỗi tổ mất bao lâu để hoàn thành xong công việc?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AC = 12\text{ cm}, BC = 13\text{ cm}$.",
            "a": r"\textbf{a) (1,5 điểm)} Tính độ dài cạnh $AB$, số đo góc $C$ (làm tròn đến độ) và độ dài đường cao $AH$ (làm tròn đến chữ số thập phân thứ nhất).",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HE \perp AB$ tại $E$ và $HF \perp AC$ tại $F$. Chứng minh tứ giác $AEHF$ là hình chữ nhật và suy ra $EF = AH$."
        }
    }
}

def render_code(code_str, d, ob11=22, vsa="0.8mm", dk12=16, dk13=16, vspace_mid="2.2mm"):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 07 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 07 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
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
    c12_text = d['c12']
    c13 = d['c13']
    p2 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 07 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 9 - TUẦN 07 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 12 (2,5 điểm).}} {c12_text}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk12}}}
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
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

"""
    return p1 + p2

def generate_tex(ob11=22, vsa="0.8mm", dk12=16, dk13=16, vspace_mid="2.2mm"):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

if __name__ == "__main__":
    tex_code = generate_tex(ob11=22, vsa="0.8mm", dk12=16, dk13=16, vspace_mid="2.2mm")
    out_path = "Phieu_Kiem_Tra_Tuan_07_Buoi_01.tex"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"Xuat file {out_path} thanh cong!")
