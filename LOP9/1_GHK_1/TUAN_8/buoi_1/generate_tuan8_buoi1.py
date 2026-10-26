import os
import subprocess
import sys

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
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 10\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"5\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 8\text{ cm}, \widehat{B} = 60^\circ$. Cạnh $AB =$", r"4\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 6\text{ cm}, \widehat{B} = 45^\circ$. Cạnh $AC =$", r"6\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 3\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"3\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\cos \alpha = 0{,}8$. Khi đó $\sin(90^\circ - \alpha) =$", r"0{,}8"),
            (r"Giá trị của biểu thức $P = 2\sin 30^\circ + \sqrt{3}\tan 60^\circ$ bằng:", r"4"),
            (r"Tòa nhà cao $20\text{ m}$ đổ bóng dài $20\text{ m}$. Góc nâng Mặt Trời là:", r"45^\circ"),
            (r"Thang dài $4\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"2\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 7 \\ x - y = 3 \end{cases}$ là $(x; y) =$", r"(5; 2)"),
            (r"Nghiệm dương của phương trình $(x - 6)(x + 2) = 0$ là:", r"6"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x + y = 7 \\ 3x - y = 8 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+2} + \dfrac{4\sqrt{x}}{x-4}\right) : \dfrac{\sqrt{x}+2}{x-4}$"),
        ],
        "c12": r"Theo kế hoạch, hai tổ sản xuất phải làm được tổng cộng $700$ sản phẩm. Nhờ cải tiến kỹ thuật, tổ I đã làm vượt mức kế hoạch $15\%$, tổ II đã làm vượt mức kế hoạch $20\%$, do đó cả hai tổ đã làm được $820$ sản phẩm. Hỏi theo kế hoạch, mỗi tổ phải sản xuất bao nhiêu sản phẩm?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 8\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$."
        }
    },
    "102": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 12\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"6\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 10\text{ cm}, \widehat{B} = 60^\circ$. Cạnh $AB =$", r"5\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 8\text{ cm}, \widehat{B} = 45^\circ$. Cạnh $AC =$", r"8\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 4\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"4\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\sin \alpha = 0{,}6$. Khi đó $\cos(90^\circ - \alpha) =$", r"0{,}6"),
            (r"Giá trị của biểu thức $P = 2\cos 60^\circ + \sqrt{3}\cot 30^\circ$ bằng:", r"4"),
            (r"Cột cờ cao $15\text{ m}$ đổ bóng dài $15\text{ m}$. Góc nâng Mặt Trời là:", r"45^\circ"),
            (r"Thang dài $6\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"3\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 8 \\ x - y = 2 \end{cases}$ là $(x; y) =$", r"(5; 3)"),
            (r"Nghiệm dương của phương trình $(x - 7)(x + 3) = 0$ là:", r"7"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 3x + y = 10 \\ 2x - y = 5 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+3} + \dfrac{6\sqrt{x}}{x-9}\right) : \dfrac{\sqrt{x}+3}{x-9}$"),
        ],
        "c12": r"Theo kế hoạch, hai tổ công nhân dự định dệt tổng cộng $800$ chiếc áo len. Do thi đua, tổ I dệt vượt mức $20\%$, tổ II dệt vượt mức $15\%$, nên cả hai tổ đã dệt được $945$ chiếc áo len. Hỏi theo kế hoạch, mỗi tổ dự định dệt bao nhiêu chiếc áo len?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 10\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AC, AB$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh rằng: $AD \cdot AB = AE \cdot AC$."
        }
    },
    "103": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 16\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"8\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 6\text{ cm}, \widehat{B} = 60^\circ$. Cạnh $AB =$", r"3\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 5\text{ cm}, \widehat{B} = 45^\circ$. Cạnh $AC =$", r"5\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 5\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"5\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{5}{13}$. Khi đó $\sin(90^\circ - \alpha) =$", r"\dfrac{5}{13}"),
            (r"Giá trị của biểu thức $P = 4\sin 30^\circ - \tan 45^\circ$ bằng:", r"1"),
            (r"Hải đăng cao $30\text{ m}$ đổ bóng dài $30\text{ m}$. Góc nâng Mặt Trời là:", r"45^\circ"),
            (r"Thang dài $5\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"2{,}5\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 9 \\ x - y = 1 \end{cases}$ là $(x; y) =$", r"(5; 4)"),
            (r"Nghiệm dương của phương trình $(x - 8)(x + 1) = 0$ là:", r"8"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} 2x - y = 5 \\ x + y = 4 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 1$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+1} + \dfrac{2\sqrt{x}}{x-1}\right) : \dfrac{\sqrt{x}+1}{x-1}$"),
        ],
        "c12": r"Theo kế hoạch, hai xưởng cơ khí phải đúc tổng cộng $600$ chi tiết máy. Khi thực hiện, xưởng I vượt mức $10\%$, xưởng II vượt mức $15\%$, vì thế cả hai xưởng đúc được $675$ chi tiết máy. Hỏi theo kế hoạch, mỗi xưởng phải đúc bao nhiêu chi tiết máy?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 12\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$."
        }
    },
    "104": {
        "sa": [
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 14\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"7\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $BC = 14\text{ cm}, \widehat{B} = 60^\circ$. Cạnh $AB =$", r"7\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 9\text{ cm}, \widehat{B} = 45^\circ$. Cạnh $AC =$", r"9\text{ cm}"),
            (r"Cho $\Delta ABC$ vuông tại $A$ có $AB = 2\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$. Cạnh $AC =$", r"2\text{ cm}"),
            (r"Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{12}{13}$. Khi đó $\cos(90^\circ - \alpha) =$", r"\dfrac{12}{13}"),
            (r"Giá trị của biểu thức $P = 2\cos 60^\circ + \tan 45^\circ$ bằng:", r"2"),
            (r"Cây cau cao $12\text{ m}$ đổ bóng dài $12\text{ m}$. Góc của tia nắng là:", r"45^\circ"),
            (r"Thang dài $8\text{ m}$ nghiêng $60^\circ$ với đất. Chân thang cách tường:", r"4\text{ m}"),
            (r"Nghiệm của hệ $\begin{cases} x + y = 6 \\ x - y = 4 \end{cases}$ là $(x; y) =$", r"(5; 1)"),
            (r"Nghiệm dương của phương trình $(x - 9)(x + 4) = 0$ là:", r"9"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"$\begin{cases} x + 2y = 8 \\ 3x - 2y = 4 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+4} + \dfrac{8\sqrt{x}}{x-16}\right) : \dfrac{\sqrt{x}+4}{x-16}$"),
        ],
        "c12": r"Theo kế hoạch, hai lớp $9A$ và $9B$ dự định thu gom tổng cộng $500\text{ kg}$ giấy vụn. Thực tế, lớp $9A$ vượt mức $15\%$, lớp $9B$ vượt mức $10\%$, nên cả hai lớp thu gom được $560\text{ kg}$ giấy vụn. Hỏi theo kế hoạch, mỗi lớp dự định thu gom bao nhiêu ki-lô-gam giấy vụn?",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 14\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Tính số đo góc $C$, độ dài các cạnh $AC, AB$ và độ dài đường cao $AH$.",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh rằng: $AD \cdot AB = AE \cdot AC$."
        }
    }
}

def render_code(code_str, d, ob11=21, vsa="0.6mm", dk12=16, dk13=17, vspace_mid="2.0mm"):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 08 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 08 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
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
% ========================= TOÁN 9 - TUẦN 08 - BUỔI 01: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 9 - TUẦN 08 - BUỔI 01}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 12 (2,5 điểm).}} {c12_text}\\par
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

def generate_tex(ob11=21, vsa="0.6mm", dk12=16, dk13=17, vspace_mid="2.0mm"):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

def compile_pdf(tex_file="Phieu_Kiem_Tra_Tuan_08_Buoi_01.tex"):
    cmd = ["pdflatex", "-interaction=nonstopmode", tex_file]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode

def get_page_count(pdf_file="Phieu_Kiem_Tra_Tuan_08_Buoi_01.pdf"):
    from pypdf import PdfReader
    reader = PdfReader(pdf_file)
    return len(reader.pages)

if __name__ == "__main__":
    out_tex = "Phieu_Kiem_Tra_Tuan_08_Buoi_01.tex"
    out_pdf = "Phieu_Kiem_Tra_Tuan_08_Buoi_01.pdf"

    # Thử cấu hình tối ưu để đạt 8 trang và sát mép đáy nhất
    best_config = None
    for ob11 in [22, 21, 20]:
        for vsa in ["0.7mm", "0.6mm"]:
            for dk13 in [17, 16]:
                for dk12 in [16, 15]:
                    tex_code = generate_tex(ob11=ob11, vsa=vsa, dk12=dk12, dk13=dk13, vspace_mid="2.0mm")
                    with open(out_tex, "w", encoding="utf-8") as f:
                        f.write(tex_code)
                    ret = compile_pdf(out_tex)
                    if ret == 0:
                        pages = get_page_count(out_pdf)
                        if pages == 8:
                            best_config = (ob11, vsa, dk12, dk13)
                            print(f"-> Dat chuan 8 trang voi: ob11={ob11}, vsa={vsa}, dk12={dk12}, dk13={dk13}")
                            break
                    if best_config:
                        break
            if best_config:
                break
        if best_config:
            break

    if best_config:
        print(f"=== KET QUA HOAN TAT: File PDF dat CHINH XAC 8 TRANG! ===")
    else:
        print("Khong tim thay cau hinh phu hop!")
