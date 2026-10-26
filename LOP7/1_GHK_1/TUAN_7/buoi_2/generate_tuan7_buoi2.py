import os
import subprocess
import pypdf
import fitz  # PyMuPDF

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
'''

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=10, ob12=5, dk13=11, dk14=5):
    alpha_val = q13['alpha']
    beta_val = q14['beta']
    res = f'''% =============================================================================
% ========================= TOÁN 7 - TUẦN 07 - BUỔI 02: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 07 - BUỔI 02}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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
% ========================= TOÁN 7 - TUẦN 07 - BUỔI 02: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 7 - TUẦN 07 - BUỔI 02}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số hữu tỉ $x$, biết:}}
\\vspace{{0.6mm}}

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

\\vspace{{1.2mm}}

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
  % Duong thang vuong goc AB
  \\draw[thick] (0.8, 0.3) -- (0.8, 2.9);
  % Duong thang a di qua A
  \\draw[thick] (0.3, 2.5) -- (4.2, 2.5) node[right=1pt] {{$a$}};
  % Duong thang b di qua B
  \\draw[thick] (0.3, 0.7) -- (4.2, 0.7) node[right=1pt] {{$b$}};
  % Cat tuyen c di qua C va D (C(3.0, 2.5) va D(2.1, 0.7))
  \\draw[thick] (3.35, 3.2) node[above=1pt] {{$c$}} -- (1.75, -0.0);
  
  % Giao diem A va B
  \\fill (0.8, 2.5) circle (1.5pt) node[above left=1pt] {{$A$}};
  \\fill (0.8, 0.7) circle (1.5pt) node[below left=1pt] {{$B$}};
  % Ky hieu vuong goc tai A va B
  \\draw (0.8, 2.25) -- (1.05, 2.25) -- (1.05, 2.5);
  \\draw (0.8, 0.95) -- (1.05, 0.95) -- (1.05, 0.7);
  
  % Giao diem C va D
  \\fill (3.0, 2.5) circle (1.5pt) node[above=2pt] {{$C$}};
  \\fill (2.1, 0.7) circle (1.5pt) node[below=2pt] {{$D$}};
  
  % Cung goc nhon ACD (huong tu 180 do ve 243.4 do)
  \\draw[red!80!black, thick] (3.0, 2.5) ++(180:0.45) arc (180:243.4:0.45);
  \\node[red!80!black, font=\\scriptsize] at (2.42, 2.12) {{{alpha_val}}};
  
  % Cung goc D1 (so le trong voi ACD)
  \\draw[blue!80!black, thick] (2.1, 0.7) ++(0:0.45) arc (0:63.4:0.45);
  \\node[blue!80!black, font=\\scriptsize] at (2.68, 0.95) {{$1$}};
\\end{{tikzpicture}}
\\end{{minipage}}\\par
\\vspace{{0.5mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.65\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 14 (1,0 điểm).}} {q14['de']}\\par\\vspace{{0.4mm}}
\\textbf{{a) (0,5 điểm)}} {q14['a']}\\par\\vspace{{0.4mm}}
\\textbf{{b) (0,5 điểm)}} {q14['b']}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.33\\linewidth}}
\\vspace{{0pt}}\\centering
\\begin{{tikzpicture}}[scale=0.75, >=stealth, line join=round, line cap=round]
  % Duong thang vuong goc MN
  \\draw[thick] (0.8, 0.2) -- (0.8, 2.6);
  % Duong thang x di qua M
  \\draw[thick] (0.3, 2.2) -- (4.0, 2.2) node[right=1pt] {{$x$}};
  % Duong thang y di qua N
  \\draw[thick] (0.3, 0.6) -- (4.0, 0.6) node[right=1pt] {{$y$}};
  % Cat tuyen d di qua P va Q
  \\draw[thick] (3.25, 2.8) node[above=1pt] {{$d$}} -- (1.65, -0.0);
  
  % Giao diem M va N
  \\fill (0.8, 2.2) circle (1.5pt) node[above left=1pt] {{$M$}};
  \\fill (0.8, 0.6) circle (1.5pt) node[below left=1pt] {{$N$}};
  % Ky hieu vuong goc tai M va N
  \\draw (0.8, 1.95) -- (1.05, 1.95) -- (1.05, 2.2);
  \\draw (0.8, 0.85) -- (1.05, 0.85) -- (1.05, 0.6);
  
  % Giao diem P va Q
  \\fill (2.9, 2.2) circle (1.5pt) node[above=2pt] {{$P$}};
  \\fill (2.0, 0.6) circle (1.5pt) node[below=2pt] {{$Q$}};
  
  % Cung goc nhon MPQ
  \\draw[red!80!black, thick] (2.9, 2.2) ++(180:0.45) arc (180:240.6:0.45);
  \\node[red!80!black, font=\\scriptsize] at (2.32, 1.82) {{{beta_val}}};
  
  % Cung goc Q1 (so le trong voi MPQ)
  \\draw[blue!80!black, thick] (2.0, 0.6) ++(0:0.45) arc (0:60.6:0.45);
  \\node[blue!80!black, font=\\scriptsize] at (2.58, 0.85) {{$1$}};
\\end{{tikzpicture}}
\\end{{minipage}}\\par
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
            (r"Số đối của số hữu tỉ $-\frac{7}{12}$ bằng bao nhiêu?", r"\frac{7}{12}"),
            (r"Giá trị của biểu thức $\left(-\frac{2}{3}\right)^3$ bằng bao nhiêu?", r"-\frac{8}{27}"),
            (r"Giá trị của căn bậc hai số học $\sqrt{\frac{49}{81}}$ bằng bao nhiêu?", r"\frac{7}{9}"),
            (r"Tính giá trị của biểu thức $\lvert -7{,}5\rvert + \lvert -2{,}5\rvert$.", "10"),
            (r"Làm tròn số $15{,}374$ đến hàng phần trăm được kết quả là:", "15{,}37"),
            (r"Cho hai góc $\widehat{aOb}$ và $\widehat{bOc}$ kề bù, biết $\widehat{aOb}=65^\circ$. Số đo góc $\widehat{bOc}$ là:", "115^\\circ"),
            (r"Tia $Oz$ là phân giác của góc $\widehat{xOy}$. Biết $\widehat{xOz}=40^\circ$, số đo $\widehat{xOy}$ là:", "80^\\circ"),
            (r"Một định lí gồm hai phần là Kết luận và phần nào?", r"\text{Giả thiết}"),
            (r"Cho $a \perp c$ và $b \perp c$ ($a \ne b$). Quan hệ giữa hai đường thẳng $a$ và $b$ là:", r"\text{song song}"),
            (r"Hộp bút giá $50\,000$ đ, giảm giá $20\%$. Số tiền người mua phải trả là:", r"40\,000\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{7}{12} + \left(-\frac{5}{6}\right) + \frac{5}{12}$",
            'b': r"$\frac{13}{17} \cdot \left(-\frac{5}{9}\right) + \frac{13}{17} \cdot \left(-\frac{4}{9}\right)$",
            'c': r"$\left(-\frac{1}{2}\right)^3 \cdot 8 - 1{,}25 \cdot 4$",
            'd': r"$\sqrt{\frac{49}{16}} - \lvert -0{,}75\rvert + \sqrt{64}$"
        },
        'q12': {
            'a': r"$x + \frac{1}{3} = \frac{5}{6}$",
            'b': r"$\frac{2}{3}x - \frac{1}{2} = \frac{5}{6}$",
            'c': r"$\left(x - \frac{1}{2}\right)^2 = \frac{9}{16}$",
            'd': r"$\lvert 2x - 1\rvert = 5$"
        },
        'q13': {
            'alpha': r"$70^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $AB$ lần lượt tại $A$ và $B$. Đường thẳng $c$ cắt $a$ tại $C$ và cắt $b$ tại $D$ sao cho $\widehat{ACD} = 70^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo góc $\widehat{BDC}$ và góc $\widehat{D}_1$."
        },
        'q14': {
            'beta': r"$60^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $x$ và $y$ cùng vuông góc với đường thẳng $MN$ lần lượt tại $M$ và $N$. Đường thẳng $d$ cắt $x$ tại $P$ và cắt $y$ tại $Q$ sao cho $\widehat{MPQ} = 60^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $x$ song song với đường thẳng $y$ ($x \parallel y$).",
            'b': r"Tính số đo góc $\widehat{NQP}$ và góc $\widehat{Q}_1$."
        }
    },
    '102': {
        'short': [
            (r"Số đối của số hữu tỉ $-\frac{9}{14}$ bằng bao nhiêu?", r"\frac{9}{14}"),
            (r"Giá trị của biểu thức $\left(-\frac{3}{2}\right)^3$ bằng bao nhiêu?", r"-\frac{27}{8}"),
            (r"Giá trị của căn bậc hai số học $\sqrt{\frac{64}{121}}$ bằng bao nhiêu?", r"\frac{8}{11}"),
            (r"Tính giá trị của biểu thức $\lvert -8{,}4\rvert + \lvert -1{,}6\rvert$.", "10"),
            (r"Làm tròn số $24{,}682$ đến hàng phần trăm được kết quả là:", "24{,}68"),
            (r"Cho hai góc $\widehat{aOb}$ và $\widehat{bOc}$ kề bù, biết $\widehat{aOb}=45^\circ$. Số đo góc $\widehat{bOc}$ là:", "135^\\circ"),
            (r"Tia $Oz$ là phân giác của góc $\widehat{xOy}$. Biết $\widehat{xOz}=35^\circ$, số đo $\widehat{xOy}$ là:", "70^\\circ"),
            (r"Trong định lí dạng ''Nếu $P$ thì $Q$'', phần $P$ được gọi là gì?", r"\text{Giả thiết}"),
            (r"Cho $a \parallel b$. Nếu đường thẳng $c \perp a$ thì đường thẳng $c$ có quan hệ gì với $b$?", r"\text{vuông góc}"),
            (r"Chiếc compa giá $40\,000$ đ, giảm giá $20\%$. Số tiền người mua phải trả là:", r"32\,000\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{8}{15} + \left(-\frac{3}{4}\right) + \frac{7}{15}$",
            'b': r"$\frac{15}{19} \cdot \left(-\frac{7}{11}\right) + \frac{15}{19} \cdot \left(-\frac{4}{11}\right)$",
            'c': r"$\left(-\frac{1}{3}\right)^2 \cdot 27 - 2{,}5 \cdot 2$",
            'd': r"$\sqrt{\frac{81}{25}} - \lvert -0{,}8\rvert + \sqrt{49}$"
        },
        'q12': {
            'a': r"$x + \frac{1}{4} = \frac{7}{8}$",
            'b': r"$\frac{3}{4}x - \frac{1}{3} = \frac{5}{12}$",
            'c': r"$\left(x + \frac{1}{3}\right)^2 = \frac{25}{9}$",
            'd': r"$\lvert 2x + 1\rvert = 7$"
        },
        'q13': {
            'alpha': r"$65^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $AB$ lần lượt tại $A$ và $B$. Đường thẳng $c$ cắt $a$ tại $C$ và cắt $b$ tại $D$ sao cho $\widehat{ACD} = 65^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo góc $\widehat{BDC}$ và góc $\widehat{D}_1$."
        },
        'q14': {
            'beta': r"$55^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $x$ và $y$ cùng vuông góc với đường thẳng $MN$ lần lượt tại $M$ và $N$. Đường thẳng $d$ cắt $x$ tại $P$ và cắt $y$ tại $Q$ sao cho $\widehat{MPQ} = 55^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $x$ song song với đường thẳng $y$ ($x \parallel y$).",
            'b': r"Tính số đo góc $\widehat{NQP}$ và góc $\widehat{Q}_1$."
        }
    },
    '103': {
        'short': [
            (r"Số đối của số hữu tỉ $-\frac{8}{15}$ bằng bao nhiêu?", r"\frac{8}{15}"),
            (r"Giá trị của biểu thức $\left(-\frac{3}{4}\right)^3$ bằng bao nhiêu?", r"-\frac{27}{64}"),
            (r"Giá trị của căn bậc hai số học $\sqrt{\frac{36}{169}}$ bằng bao nhiêu?", r"\frac{6}{13}"),
            (r"Tính giá trị của biểu thức $\lvert -6{,}8\rvert + \lvert -3{,}2\rvert$.", "10"),
            (r"Làm tròn số $32{,}519$ đến hàng phần trăm được kết quả là:", "32{,}52"),
            (r"Cho hai góc $\widehat{aOb}$ và $\widehat{bOc}$ kề bù, biết $\widehat{aOb}=50^\circ$. Số đo góc $\widehat{bOc}$ là:", "130^\\circ"),
            (r"Tia $Oz$ là phân giác của góc $\widehat{xOy}$. Biết $\widehat{xOz}=45^\circ$, số đo $\widehat{xOy}$ là:", "90^\\circ"),
            (r"Trong định lí dạng ''Nếu $P$ thì $Q$'', phần $Q$ được gọi là gì?", r"\text{Kết luận}"),
            (r"Cho $a \parallel b$ và $b \parallel c$ ($a \ne c$). Quan hệ giữa hai đường thẳng $a$ và $c$ là:", r"\text{song song}"),
            (r"Bộ thước kẻ giá $30\,000$ đ, giảm giá $20\%$. Số tiền người mua phải trả là:", r"24\,000\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{9}{14} + \left(-\frac{2}{3}\right) + \frac{5}{14}$",
            'b': r"$\frac{11}{23} \cdot \left(-\frac{9}{14}\right) + \frac{11}{23} \cdot \left(-\frac{5}{14}\right)$",
            'c': r"$\left(-\frac{1}{2}\right)^2 \cdot 16 - 3{,}5 \cdot 2$",
            'd': r"$\sqrt{\frac{25}{16}} - \lvert -0{,}25\rvert + \sqrt{100}$"
        },
        'q12': {
            'a': r"$x + \frac{1}{5} = \frac{7}{10}$",
            'b': r"$\frac{4}{5}x - \frac{1}{2} = \frac{3}{10}$",
            'c': r"$\left(x - \frac{1}{4}\right)^2 = \frac{9}{16}$",
            'd': r"$\lvert 3x - 2\rvert = 7$"
        },
        'q13': {
            'alpha': r"$75^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $AB$ lần lượt tại $A$ và $B$. Đường thẳng $c$ cắt $a$ tại $C$ và cắt $b$ tại $D$ sao cho $\widehat{ACD} = 75^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo góc $\widehat{BDC}$ và góc $\widehat{D}_1$."
        },
        'q14': {
            'beta': r"$50^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $x$ và $y$ cùng vuông góc với đường thẳng $MN$ lần lượt tại $M$ và $N$. Đường thẳng $d$ cắt $x$ tại $P$ và cắt $y$ tại $Q$ sao cho $\widehat{MPQ} = 50^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $x$ song song với đường thẳng $y$ ($x \parallel y$).",
            'b': r"Tính số đo góc $\widehat{NQP}$ và góc $\widehat{Q}_1$."
        }
    },
    '104': {
        'short': [
            (r"Số đối của số hữu tỉ $-\frac{11}{16}$ bằng bao nhiêu?", r"\frac{11}{16}"),
            (r"Giá trị của biểu thức $\left(-\frac{2}{5}\right)^3$ bằng bao nhiêu?", r"-\frac{8}{125}"),
            (r"Giá trị của căn bậc hai số học $\sqrt{\frac{25}{144}}$ bằng bao nhiêu?", r"\frac{5}{12}"),
            (r"Tính giá trị của biểu thức $\lvert -9{,}3\rvert + \lvert -0{,}7\rvert$.", "10"),
            (r"Làm tròn số $41{,}736$ đến hàng phần trăm được kết quả là:", "41{,}74"),
            (r"Cho hai góc $\widehat{aOb}$ và $\widehat{bOc}$ kề bù, biết $\widehat{aOb}=70^\circ$. Số đo góc $\widehat{bOc}$ là:", "110^\\circ"),
            (r"Tia $Oz$ là phân giác của góc $\widehat{xOy}$. Biết $\widehat{xOz}=55^\circ$, số đo $\widehat{xOy}$ là:", "110^\\circ"),
            (r"Lập luận từ giả thiết để suy ra kết luận của một định lí gọi là gì?", r"\text{Chứng minh định lí}"),
            (r"Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng:", r"\text{song song}"),
            (r"Quyển vở có giá $20\,000$ đ, được giảm giá $20\%$. Số tiền người mua phải trả là:", r"16\,000\text{ đ}"),
        ],
        'q11': {
            'a': r"$\frac{11}{18} + \left(-\frac{4}{5}\right) + \frac{7}{18}$",
            'b': r"$\frac{14}{25} \cdot \left(-\frac{8}{13}\right) + \frac{14}{25} \cdot \left(-\frac{5}{13}\right)$",
            'c': r"$\left(-\frac{2}{3}\right)^2 \cdot 18 - 1{,}5 \cdot 4$",
            'd': r"$\sqrt{\frac{36}{25}} - \lvert -0{,}2\rvert + \sqrt{81}$"
        },
        'q12': {
            'a': r"$x + \frac{1}{6} = \frac{5}{12}$",
            'b': r"$\frac{5}{6}x - \frac{1}{4} = \frac{7}{12}$",
            'c': r"$\left(x + \frac{1}{2}\right)^2 = \frac{25}{4}$",
            'd': r"$\lvert 3x + 1\rvert = 8$"
        },
        'q13': {
            'alpha': r"$80^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $AB$ lần lượt tại $A$ và $B$. Đường thẳng $c$ cắt $a$ tại $C$ và cắt $b$ tại $D$ sao cho $\widehat{ACD} = 80^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $a$ song song với đường thẳng $b$ ($a \parallel b$).",
            'b': r"Tính số đo góc $\widehat{BDC}$ và góc $\widehat{D}_1$."
        },
        'q14': {
            'beta': r"$65^\circ$",
            'de': r"Cho hình vẽ bên, biết hai đường thẳng $x$ và $y$ cùng vuông góc với đường thẳng $MN$ lần lượt tại $M$ và $N$. Đường thẳng $d$ cắt $x$ tại $P$ và cắt $y$ tại $Q$ sao cho $\widehat{MPQ} = 65^\circ$.",
            'a': r"Chứng minh rằng đường thẳng $x$ song song với đường thẳng $y$ ($x \parallel y$).",
            'b': r"Tính số đo góc $\widehat{NQP}$ và góc $\widehat{Q}_1$."
        }
    }
}

full_tex = tex_template
for ma in ['101', '102', '103', '104']:
    d = de_data[ma]
    full_tex += render_de(ma, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11=10, ob12=5, dk13=9, dk14=6)

full_tex += r'\end{document}' + '\n'

script_dir = os.path.dirname(os.path.abspath(__file__))
tex_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex')
with open(tex_file, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print(f"Generated {tex_file}")

# Biên dịch LaTeX
print("Compiling LaTeX...")
cmd = ["pdflatex", "-interaction=nonstopmode", "Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex"]
proc = subprocess.run(cmd, cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

pdf_file = os.path.join(script_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_02.pdf')
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
        # Đồng bộ sang thư mục cha TUAN_7
        import shutil
        parent_dir = os.path.dirname(script_dir)
        shutil.copy(tex_file, os.path.join(parent_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex'))
        shutil.copy(pdf_file, os.path.join(parent_dir, 'Phieu_Kiem_Tra_Tuan_07_Buoi_02.pdf'))
        print("Synchronized tex and pdf to parent folder TUAN_7")
    else:
        print(f"WARNING: Page count is {num_pages}, expected 8 pages. Adjust spacing!")
else:
    print("Compilation failed, PDF not found.")
    print("Error output:")
    print(proc.stdout[-1500:])
