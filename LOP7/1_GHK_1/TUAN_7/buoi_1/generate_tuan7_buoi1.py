import os
import subprocess
import pypdf
import fitz # PyMuPDF

tex_template = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=2.6,heightSA=0.62}

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

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=10, ob12=5, dk13=11, dk14=8):
    res = f'''% =============================================================================
% ========================= TOÁN 7 - TUẦN 07 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 07 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

'''
    # 10 câu trả lời ngắn
    for idx, (text, ans) in enumerate(q_short, 1):
        res += f'\\noindent\\textbf{{Câu {idx} (0,25 điểm).}} {text} \\shortans{{{ans}}}\\par\\vspace{{0.5mm}}\n'

    res += f'''\\vspace{{0.6mm}}

\\noindent\\textbf{{Câu 11 (2,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.8mm}}

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
% ========================= TOÁN 7 - TUẦN 07 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 7 - TUẦN 07 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số hữu tỉ $x$, biết:}}
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
\\begin{{minipage}}[t]{{0.65\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,5 điểm).}} {q13['de']}\\par\\vspace{{0.4mm}}
\\textbf{{a) (1,25 điểm)}} {q13['a']}\\par\\vspace{{0.4mm}}
\\textbf{{b) (1,25 điểm)}} {q13['b']}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.33\\linewidth}}
\\vspace{{0pt}}\\centering
\\begin{{tikzpicture}}[scale=0.85, >=stealth, line join=round, line cap=round]
  % Hai duong thang a va b
  \\draw[thick] (0.2, 2.5) -- (4.2, 2.5) node[right=1pt] {{$a$}};
  \\draw[thick] (0.2, 0.7) -- (4.2, 0.7) node[right=1pt] {{$b$}};
  % Cat tuyen c
  \\draw[thick] (0.8, -0.2) -- (2.9, 3.4) node[above=1pt] {{$c$}};
  % Giao diem A(2.37, 2.5) va B(1.31, 0.7)
  \\fill (2.37, 2.5) circle (1.5pt);
  \\node[font=\\footnotesize, fill=white, inner sep=1pt] at (2.05, 3.1) {{$A$}};
  
  \\fill (1.31, 0.7) circle (1.5pt);
  \\node[font=\\footnotesize, fill=white, inner sep=1pt] at (1.0, 1.3) {{$B$}};
  
  % Cung goc A1 va B1
  \\draw[red!80!black, thick] (2.37, 2.5) ++(0:0.45) arc (0:59.7:0.45);
  \\draw[red!80!black, thick] (1.31, 0.7) ++(0:0.45) arc (0:59.7:0.45);
  
  % So goc tai A
  \\node[red!80!black, font=\\scriptsize] at (2.95, 2.85) {{$1$}};
  \\node[font=\\scriptsize] at (1.75, 2.75) {{$2$}};
  \\node[font=\\scriptsize] at (1.75, 2.25) {{$3$}};
  \\node[font=\\scriptsize] at (2.85, 2.2) {{$4$}};
  
  % So goc tai B
  \\node[red!80!black, font=\\scriptsize] at (1.9, 1.05) {{$1$}};
  \\node[font=\\scriptsize] at (0.7, 0.95) {{$2$}};
  \\node[font=\\scriptsize] at (0.7, 0.45) {{$3$}};
  \\node[font=\\scriptsize] at (1.8, 0.4) {{$4$}};
\\end{{tikzpicture}}
\\end{{minipage}}\\par
\\vspace{{0.5mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (1,0 điểm).}} {q14['de']}\\par
\\vspace{{0.5mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}

\\newpage

'''
    return res

de_data = {
    '101': {
        'short': [
            (r"Giá trị của $\sqrt{144}$ bằng bao nhiêu?", "12"),
            (r"Giá trị của biểu thức $\vert -5{,}2\vert - \vert 3{,}2\vert$ bằng bao nhiêu?", "2"),
            (r"Làm tròn số $28{,}647$ đến hàng phần mười được kết quả là:", "28{,}6"),
            (r"Cho hai góc $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, biết $\widehat{xOy}=75^\circ$. Số đo góc $\widehat{yOz}$ là:", "105^\\circ"),
            (r"Hai đường thẳng cắt nhau tạo góc $48^\circ$. Số đo góc đối đỉnh với nó là:", "48^\\circ"),
            (r"Cho tia $Ot$ là phân giác của góc $\widehat{mOn} = 110^\circ$. Số đo góc $\widehat{mOt}$ là:", "55^\\circ"),
            (r"Giá trị của biểu thức $\left(-\frac{1}{3}\right)^2 + \frac{8}{9}$ bằng bao nhiêu?", "1"),
            (r"Qua điểm $M \notin a$, có bao nhiêu đường thẳng song song với $a$?", "1"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 9$.", "81"),
            (r"Cuốn sách giá $80\,000$ đ được giảm giá $15\%$. Số tiền được giảm là:", "12\,000\\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{5}{14} + \left(-\frac{7}{3}\right) + \frac{9}{14}$",
            'b': r"$\frac{7}{11} \cdot \left(-\frac{8}{15}\right) + \frac{7}{11} \cdot \left(-\frac{7}{15}\right)$",
            'c': r"$\left(-\frac{1}{2}\right)^2 \cdot 12 - 2{,}5 \cdot 4$",
            'd': r"$\sqrt{\frac{36}{25}} - \vert -0{,}2\vert + \sqrt{49}$"
        },
        'q12': {
            'a': r"$x - \frac{1}{4} = \frac{5}{12}$",
            'b': r"$\frac{3}{5}x + \frac{1}{2} = \frac{11}{10}$",
            'c': r"$\left(x + \frac{1}{3}\right)^2 = \frac{16}{25}$",
            'd': r"$\vert 3x - 1\vert = 5$"
        },
        'q13': {
            'de': r"Cho hình vẽ bên, biết đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ lần lượt tại hai điểm $A$ và $B$, trong đó $\widehat{A}_1 = \widehat{B}_1 = 60^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo các góc còn lại tại đỉnh $A$ và đỉnh $B$ (tức tính các góc $\widehat{A}_2, \widehat{A}_3, \widehat{A}_4$ và $\widehat{B}_2, \widehat{B}_3, \widehat{B}_4$)."
        },
        'q14': {
            'de': r"Cho biểu thức $A = \frac{1}{2} + \frac{1}{2^2} + \frac{1}{2^3} + \dots + \frac{1}{2^{2026}}$. Hãy so sánh $A$ với $1$."
        }
    },
    '102': {
        'short': [
            (r"Giá trị của $\sqrt{169}$ bằng bao nhiêu?", "13"),
            (r"Giá trị của biểu thức $\vert -6{,}4\vert - \vert 3{,}4\vert$ bằng bao nhiêu?", "3"),
            (r"Làm tròn số $37{,}482$ đến hàng phần mười được kết quả là:", "37{,}5"),
            (r"Cho hai góc $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, biết $\widehat{xOy}=55^\circ$. Số đo góc $\widehat{yOz}$ là:", "125^\\circ"),
            (r"Hai đường thẳng cắt nhau tạo góc $62^\circ$. Số đo góc đối đỉnh với nó là:", "62^\\circ"),
            (r"Cho tia $Ot$ là phân giác của góc $\widehat{mOn} = 120^\circ$. Số đo góc $\widehat{mOt}$ là:", "60^\\circ"),
            (r"Giá trị của biểu thức $\left(-\frac{2}{5}\right)^2 + \frac{21}{25}$ bằng bao nhiêu?", "1"),
            (r"Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì chúng:", "\\text{song song}"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 10$.", "100"),
            (r"Chiếc ba lô giá $240\,000$ đ được giảm giá $15\%$. Số tiền được giảm là:", "36\,000\\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{4}{15} + \left(-\frac{5}{2}\right) + \frac{11}{15}$",
            'b': r"$\frac{9}{13} \cdot \left(-\frac{5}{17}\right) + \frac{9}{13} \cdot \left(-\frac{12}{17}\right)$",
            'c': r"$\left(-\frac{1}{3}\right)^2 \cdot 18 - 3{,}5 \cdot 2$",
            'd': r"$\sqrt{\frac{64}{25}} - \vert -0{,}6\vert + \sqrt{64}$"
        },
        'q12': {
            'a': r"$x - \frac{1}{6} = \frac{7}{18}$",
            'b': r"$\frac{4}{7}x + \frac{1}{3} = \frac{19}{21}$",
            'c': r"$\left(x - \frac{1}{4}\right)^2 = \frac{25}{16}$",
            'd': r"$\vert 3x + 2\vert = 8$"
        },
        'q13': {
            'de': r"Cho hình vẽ bên, biết đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ lần lượt tại hai điểm $A$ và $B$, trong đó $\widehat{A}_1 = \widehat{B}_1 = 70^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo các góc còn lại tại đỉnh $A$ và đỉnh $B$ (tức tính các góc $\widehat{A}_2, \widehat{A}_3, \widehat{A}_4$ và $\widehat{B}_2, \widehat{B}_3, \widehat{B}_4$)."
        },
        'q14': {
            'de': r"Cho biểu thức $B = \frac{1}{3} + \frac{1}{3^2} + \frac{1}{3^3} + \dots + \frac{1}{3^{2026}}$. Hãy so sánh $B$ với $\frac{1}{2}$."
        }
    },
    '103': {
        'short': [
            (r"Giá trị của $\sqrt{196}$ bằng bao nhiêu?", "14"),
            (r"Giá trị của biểu thức $\vert -7{,}6\vert - \vert 3{,}6\vert$ bằng bao nhiêu?", "4"),
            (r"Làm tròn số $46{,}359$ đến hàng phần mười được kết quả là:", "46{,}4"),
            (r"Cho hai góc $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, biết $\widehat{xOy}=65^\circ$. Số đo góc $\widehat{yOz}$ là:", "115^\\circ"),
            (r"Hai đường thẳng cắt nhau tạo góc $54^\circ$. Số đo góc đối đỉnh với nó là:", "54^\\circ"),
            (r"Cho tia $Ot$ là phân giác của góc $\widehat{mOn} = 130^\circ$. Số đo góc $\widehat{mOt}$ là:", "65^\\circ"),
            (r"Giá trị của biểu thức $\left(-\frac{3}{5}\right)^2 + \frac{16}{25}$ bằng bao nhiêu?", "1"),
            (r"Hai đường thẳng phân biệt cùng vuông góc với đường thẳng thứ ba thì chúng:", "\\text{song song}"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 11$.", "121"),
            (r"Đôi dép giá $160\,000$ đ được giảm giá $15\%$. Số tiền được giảm là:", "24\,000\\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{7}{18} + \left(-\frac{8}{3}\right) + \frac{11}{18}$",
            'b': r"$\frac{5}{12} \cdot \left(-\frac{11}{19}\right) + \frac{5}{12} \cdot \left(-\frac{8}{19}\right)$",
            'c': r"$\left(-\frac{1}{2}\right)^3 \cdot 16 + 1{,}5 \cdot (-4)$",
            'd': r"$\sqrt{\frac{49}{16}} - \vert -0{,}75\vert + \sqrt{81}$"
        },
        'q12': {
            'a': r"$x - \frac{1}{5} = \frac{7}{20}$",
            'b': r"$\frac{5}{8}x - \frac{1}{4} = \frac{3}{8}$",
            'c': r"$\left(x + \frac{1}{2}\right)^2 = \frac{9}{4}$",
            'd': r"$\vert 2x - 3\vert = 7$"
        },
        'q13': {
            'de': r"Cho hình vẽ bên, biết đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ lần lượt tại hai điểm $A$ và $B$, trong đó $\widehat{A}_1 = \widehat{B}_1 = 50^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo các góc còn lại tại đỉnh $A$ và đỉnh $B$ (tức tính các góc $\widehat{A}_2, \widehat{A}_3, \widehat{A}_4$ và $\widehat{B}_2, \widehat{B}_3, \widehat{B}_4$)."
        },
        'q14': {
            'de': r"Cho biểu thức $C = \frac{1}{4} + \frac{1}{4^2} + \frac{1}{4^3} + \dots + \frac{1}{4^{2026}}$. Hãy so sánh $C$ với $\frac{1}{3}$."
        }
    },
    '104': {
        'short': [
            (r"Giá trị của $\sqrt{225}$ bằng bao nhiêu?", "15"),
            (r"Giá trị của biểu thức $\vert -8{,}8\vert - \vert 3{,}8\vert$ bằng bao nhiêu?", "5"),
            (r"Làm tròn số $54{,}728$ đến hàng phần mười được kết quả là:", "54{,}7"),
            (r"Cho hai góc $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, biết $\widehat{xOy}=85^\circ$. Số đo góc $\widehat{yOz}$ là:", "95^\\circ"),
            (r"Hai đường thẳng cắt nhau tạo góc $76^\circ$. Số đo góc đối đỉnh với nó là:", "76^\\circ"),
            (r"Cho tia $Ot$ là phân giác của góc $\widehat{mOn} = 140^\circ$. Số đo góc $\widehat{mOt}$ là:", "70^\\circ"),
            (r"Giá trị của biểu thức $\left(-\frac{1}{4}\right)^2 + \frac{15}{16}$ bằng bao nhiêu?", "1"),
            (r"Cho $a \parallel b$, nếu $c \perp a$ thì đường thẳng $c$ có quan hệ gì với đường thẳng $b$?", "\\text{vuông góc}"),
            (r"Tìm số thực $x \ge 0$, biết $\sqrt{x} = 12$.", "144"),
            (r"Chiếc áo giá $120\,000$ đ được giảm giá $15\%$. Số tiền được giảm là:", "18\,000\\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{5}{16} + \left(-\frac{7}{2}\right) + \frac{11}{16}$",
            'b': r"$\frac{6}{17} \cdot \left(-\frac{13}{21}\right) + \frac{6}{17} \cdot \left(-\frac{8}{21}\right)$",
            'c': r"$\left(-\frac{2}{3}\right)^2 \cdot 9 - 4{,}5 \cdot 2$",
            'd': r"$\sqrt{\frac{81}{16}} - \vert -1{,}25\vert + \sqrt{100}$"
        },
        'q12': {
            'a': r"$x - \frac{1}{3} = \frac{5}{12}$",
            'b': r"$\frac{2}{5}x - \frac{1}{10} = \frac{3}{10}$",
            'c': r"$\left(x - \frac{1}{5}\right)^2 = \frac{16}{25}$",
            'd': r"$\vert 2x + 5\vert = 9$"
        },
        'q13': {
            'de': r"Cho hình vẽ bên, biết đường thẳng $c$ cắt hai đường thẳng $a$ và $b$ lần lượt tại hai điểm $A$ và $B$, trong đó $\widehat{A}_1 = \widehat{B}_1 = 65^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo các góc còn lại tại đỉnh $A$ và đỉnh $B$ (tức tính các góc $\widehat{A}_2, \widehat{A}_3, \widehat{A}_4$ và $\widehat{B}_2, \widehat{B}_3, \widehat{B}_4$)."
        },
        'q14': {
            'de': r"Cho biểu thức $D = \frac{1}{5} + \frac{1}{5^2} + \frac{1}{5^3} + \dots + \frac{1}{5^{2026}}$. Hãy so sánh $D$ với $\frac{1}{4}$."
        }
    }
}

full_tex = tex_template
for ma in ['101', '102', '103', '104']:
    d = de_data[ma]
    full_tex += render_de(ma, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11=10, ob12=5, dk13=11, dk14=8)

full_tex += r'\end{document}' + '\n'

script_dir = os.path.dirname(os.path.abspath(__file__))
tex_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_01.tex')
with open(tex_file, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print(f"Generated {tex_file}")

# Biên dịch LaTeX
print("Compiling LaTeX...")
cmd = ["pdflatex", "-interaction=nonstopmode", "Phieu_Kiem_Tra_Tuan_07_Buoi_01.tex"]
proc = subprocess.run(cmd, cwd=script_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

pdf_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_01.pdf')
if os.path.exists(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    num_pages = len(reader.pages)
    print(f"PDF generated successfully: {pdf_file}")
    print(f"Total pages: {num_pages} (Target: 8 pages)")
    if num_pages == 8:
        print("PERFECT: Exactly 8 pages!")
        # Xuất ảnh trang 1 và 2 để kiểm tra giao diện
        doc = fitz.open(pdf_file)
        doc[0].get_pixmap(dpi=150).save(os.path.join(script_dir, 'page_1.png'))
        doc[1].get_pixmap(dpi=150).save(os.path.join(script_dir, 'page_2.png'))
        print("Updated page_1.png and page_2.png")
    else:
        print(f"WARNING: Page count is {num_pages}, expected 8 pages. Adjust spacing!")
else:
    print("Compilation failed, PDF not found.")
