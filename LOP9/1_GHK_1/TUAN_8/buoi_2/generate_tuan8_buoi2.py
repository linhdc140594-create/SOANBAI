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
            (r"Giá trị của biểu thức $\sqrt{49} - \sqrt{16}$ bằng:", r"3"),
            (r"Biểu thức $\sqrt{2x - 6}$ xác định khi:", r"x \ge 3"),
            (r"Nghiệm của bất phương trình $3x - 9 \ge 0$ là:", r"x \ge 3"),
            (r"Nghiệm của hệ $\begin{cases} 2x - y = 3 \\ x + y = 3 \end{cases}$ là $(x; y) =$", r"(2; 1)"),
            (r"Cho $\Delta ABC$ vuông tại $A$ ($AB=3, AC=4$). Khi đó $\sin C =$", r"\dfrac{3}{5}"),
            (r"$\Delta ABC$ vuông tại $A$ ($BC = 10, \widehat{B}=60^\circ$). Cạnh $AC =$", r"5\sqrt{3}\text{ cm}"),
            (r"Rút gọn biểu thức $\sqrt{(3 - \sqrt{11})^2}$ được:", r"\sqrt{11} - 3"),
            (r"Giá trị của biểu thức $\sin^2 35^\circ + \sin^2 55^\circ$ bằng:", r"1"),
            (r"Cây cao $8\text{ m}$ đổ bóng dài $8\text{ m}$. Góc của tia nắng là:", r"45^\circ"),
            (r"Nghiệm của phương trình $\sqrt{3x + 1} = 4$ là $x =$", r"5"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"Giải hệ phương trình:\par $\begin{cases} 2x - y = 6 \\ 3x + y = 14 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 1$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x}-1} - \dfrac{1}{x-\sqrt{x}}\right) : \dfrac{\sqrt{x}+1}{x-1}$"),
        ],
        "c12": r"Một đội xe dự định chở $75$ tấn hàng để ủng hộ đồng bào miền Trung bị lũ lụt. Lúc sắp khởi hành, đội nhận được ủng hộ thêm $5$ tấn hàng nữa và đồng thời được bổ sung thêm $5$ xe cùng loại, do đó mỗi xe chở ít hơn dự định $1$ tấn hàng. Hỏi ban đầu đội xe dự định sử dụng bao nhiêu chiếc xe? (Biết mỗi xe chở khối lượng hàng như nhau).",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Cho $AB = 9\text{ cm}$ và $AC = 12\text{ cm}$. Tính độ dài cạnh huyền $BC$, đường cao $AH$ và số đo góc $B$ (làm tròn đến độ).",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh $\Delta ADE \backsim \Delta ACB$."
        }
    },
    "102": {
        "sa": [
            (r"Giá trị của biểu thức $\sqrt{64} - \sqrt{25}$ bằng:", r"3"),
            (r"Biểu thức $\sqrt{3x - 12}$ xác định khi:", r"x \ge 4"),
            (r"Nghiệm của bất phương trình $2x - 8 \ge 0$ là:", r"x \ge 4"),
            (r"Nghiệm của hệ $\begin{cases} 2x - y = 4 \\ x + y = 5 \end{cases}$ là $(x; y) =$", r"(3; 2)"),
            (r"Cho $\Delta ABC$ vuông tại $A$ ($AB=3, AC=4$). Khi đó $\cos C =$", r"\dfrac{4}{5}"),
            (r"$\Delta ABC$ vuông tại $A$ ($BC = 8, \widehat{B}=60^\circ$). Cạnh $AC =$", r"4\sqrt{3}\text{ cm}"),
            (r"Rút gọn biểu thức $\sqrt{(2 - \sqrt{5})^2}$ được:", r"\sqrt{5} - 2"),
            (r"Giá trị của biểu thức $\cos^2 25^\circ + \cos^2 65^\circ$ bằng:", r"1"),
            (r"Cột đèn cao $6\text{ m}$ đổ bóng dài $6\text{ m}$. Góc của tia nắng là:", r"45^\circ"),
            (r"Nghiệm của phương trình $\sqrt{2x + 5} = 5$ là $x =$", r"10"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"Giải hệ phương trình:\par $\begin{cases} 3x - y = 7 \\ 2x + y = 8 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 4$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x}-2} - \dfrac{4}{x-2\sqrt{x}}\right) : \dfrac{\sqrt{x}+2}{x-4}$"),
        ],
        "c12": r"Một đội xe theo kế hoạch phải chở $60$ tấn hàng để phục vụ xây dựng trường học. Khi thực hiện, có $2$ xe được điều đi làm nhiệm vụ khác nên mỗi xe còn lại phải chở thêm $1$ tấn hàng nữa mới hết số hàng. Hỏi ban đầu đội xe có bao nhiêu chiếc xe? (Biết mỗi xe chở khối lượng hàng như nhau).",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Cho $AB = 12\text{ cm}$ và $AC = 16\text{ cm}$. Tính độ dài cạnh huyền $BC$, đường cao $AH$ và số đo góc $B$ (làm tròn đến độ).",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh $\Delta ADE \backsim \Delta ACB$."
        }
    },
    "103": {
        "sa": [
            (r"Giá trị của biểu thức $\sqrt{81} - \sqrt{36}$ bằng:", r"3"),
            (r"Biểu thức $\sqrt{4x - 8}$ xác định khi:", r"x \ge 2"),
            (r"Nghiệm của bất phương trình $4x - 12 \ge 0$ là:", r"x \ge 3"),
            (r"Nghiệm của hệ $\begin{cases} 3x - y = 5 \\ x + y = 3 \end{cases}$ là $(x; y) =$", r"(2; 1)"),
            (r"Cho $\Delta ABC$ vuông tại $A$ ($AB=5, AC=12$). Khi đó $\sin C =$", r"\dfrac{5}{13}"),
            (r"$\Delta ABC$ vuông tại $A$ ($BC = 6, \widehat{B}=60^\circ$). Cạnh $AC =$", r"3\sqrt{3}\text{ cm}"),
            (r"Rút gọn biểu thức $\sqrt{(1 - \sqrt{2})^2}$ được:", r"\sqrt{2} - 1"),
            (r"Giá trị của biểu thức $\sin^2 18^\circ + \sin^2 72^\circ$ bằng:", r"1"),
            (r"Tháp cao $50\text{ m}$ đổ bóng dài $50\text{ m}$. Góc của tia nắng là:", r"45^\circ"),
            (r"Nghiệm của phương trình $\sqrt{4x + 9} = 5$ là $x =$", r"4"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"Giải hệ phương trình:\par $\begin{cases} 2x + y = 11 \\ 3x - y = 4 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 9$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x}-3} - \dfrac{9}{x-3\sqrt{x}}\right) : \dfrac{\sqrt{x}+3}{x-9}$"),
        ],
        "c12": r"Một đội xe dự định chở $80$ tấn hàng cứu trợ đồng bào bị ảnh hưởng do bão. Lúc sắp khởi hành, có $4$ xe được điều đi làm việc khác nên mỗi xe còn lại phải chở nhiều hơn dự định $1$ tấn hàng mới hết số hàng. Hỏi ban đầu đội xe có bao nhiêu chiếc xe? (Biết mỗi xe chở khối lượng hàng như nhau).",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Cho $AB = 6\text{ cm}$ và $AC = 8\text{ cm}$. Tính độ dài cạnh huyền $BC$, đường cao $AH$ và số đo góc $B$ (làm tròn đến độ).",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh $\Delta ADE \backsim \Delta ACB$."
        }
    },
    "104": {
        "sa": [
            (r"Giá trị của biểu thức $\sqrt{100} - \sqrt{49}$ bằng:", r"3"),
            (r"Biểu thức $\sqrt{5x - 25}$ xác định khi:", r"x \ge 5"),
            (r"Nghiệm của bất phương trình $5x - 15 \ge 0$ là:", r"x \ge 3"),
            (r"Nghiệm của hệ $\begin{cases} 2x - y = 5 \\ x + y = 4 \end{cases}$ là $(x; y) =$", r"(3; 1)"),
            (r"Cho $\Delta ABC$ vuông tại $A$ ($AB=5, AC=12$). Khi đó $\cos C =$", r"\dfrac{12}{13}"),
            (r"$\Delta ABC$ vuông tại $A$ ($BC = 12, \widehat{B}=60^\circ$). Cạnh $AC =$", r"6\sqrt{3}\text{ cm}"),
            (r"Rút gọn biểu thức $\sqrt{(3 - \sqrt{10})^2}$ được:", r"\sqrt{10} - 3"),
            (r"Giá trị của biểu thức $\cos^2 40^\circ + \cos^2 50^\circ$ bằng:", r"1"),
            (r"Ống khói cao $25\text{ m}$ đổ bóng dài $25\text{ m}$. Góc của tia nắng là:", r"45^\circ"),
            (r"Nghiệm của phương trình $\sqrt{5x + 4} = 7$ là $x =$", r"9"),
        ],
        "c11": [
            ("a) (1,25 điểm)", r"Giải hệ phương trình:\par $\begin{cases} 4x - y = 9 \\ 2x + y = 9 \end{cases}$"),
            ("b) (1,25 điểm)", r"Rút gọn với $x > 0, x \ne 16$:\par $B = \left(\dfrac{\sqrt{x}}{\sqrt{x}-4} - \dfrac{16}{x-4\sqrt{x}}\right) : \dfrac{\sqrt{x}+4}{x-16}$"),
        ],
        "c12": r"Một đội xe theo kế hoạch phải chở $90$ tấn nông sản đi tiêu thụ tại các siêu thị. Khi thực hiện, do có $3$ xe được điều chuyển đi nơi khác nên mỗi xe còn lại phải chở thêm $1$ tấn hàng mới hết số hàng. Hỏi ban đầu đội xe có bao nhiêu chiếc xe? (Biết mỗi xe chở khối lượng hàng như nhau).",
        "c13": {
            "gt": r"Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ ($H \in BC$).",
            "a": r"\textbf{a) (1,5 điểm)} Cho $AB = 15\text{ cm}$ và $AC = 20\text{ cm}$. Tính độ dài cạnh huyền $BC$, đường cao $AH$ và số đo góc $B$ (làm tròn đến độ).",
            "b": r"\textbf{b) (1,0 điểm)} Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh $\Delta ADE \backsim \Delta ACB$."
        }
    }
}

def render_code(code_str, d, ob11=22, vsa="0.6mm", dk12=16, dk13=16, vspace_mid="2.0mm"):
    # Trang 1
    p1 = f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 08 - BUỔI 02: MÃ ĐỀ {code_str} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 08 - BUỔI 02}} & \\textbf{{Mã đề: {code_str} - Trang 1/2}} \\\\
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
% ========================= TOÁN 9 - TUẦN 08 - BUỔI 02: MÃ ĐỀ {code_str} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 9 - TUẦN 08 - BUỔI 02}} & \\textbf{{Mã đề: {code_str} - Trang 2/2}} \\\\
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

def generate_tex(ob11=22, vsa="0.5mm", dk12=16, dk13=18, vspace_mid="2.0mm"):
    content = HEADER_TEMPLATE
    for idx, code in enumerate(["101", "102", "103", "104"]):
        content += render_code(code, DATA[code], ob11=ob11, vsa=vsa, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid)
        if idx < 3:
            content += "\\newpage\n"
    content += FOOTER_TEMPLATE
    return content

def compile_pdf(tex_file="Phieu_Kiem_Tra_Tuan_08_Buoi_02.tex"):
    cmd = ["pdflatex", "-interaction=nonstopmode", tex_file]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode

def get_page_count(pdf_file="Phieu_Kiem_Tra_Tuan_08_Buoi_02.pdf"):
    from pypdf import PdfReader
    reader = PdfReader(pdf_file)
    return len(reader.pages)

if __name__ == "__main__":
    out_tex = "Phieu_Kiem_Tra_Tuan_08_Buoi_02.tex"
    out_pdf = "Phieu_Kiem_Tra_Tuan_08_Buoi_02.pdf"

    ob11 = 22
    vsa = "0.5mm"
    dk12 = 16
    dk13 = 18
    vspace_mid = "2.0mm"

    tex_code = generate_tex(ob11=ob11, vsa=vsa, dk12=dk12, dk13=dk13, vspace_mid=vspace_mid)
    with open(out_tex, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"-> Da tao file {out_tex}")

    ret = compile_pdf(out_tex)
    if ret != 0:
        print("Loi bien dich pdflatex!")
        sys.exit(1)

    pages = get_page_count(out_pdf)
    print(f"=== KET QUA HOAN TAT: File PDF dat CHINH XAC {pages} TRANG! ===")

