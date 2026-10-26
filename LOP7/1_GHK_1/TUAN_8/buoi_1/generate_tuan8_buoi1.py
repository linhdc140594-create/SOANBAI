import os
import subprocess
import pypdf

TEX_TEMPLATE = r'''\documentclass[12pt,a4paper]{article}
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

% Khu vực bài làm chia 2 cột có vách ngăn mờ ở giữa
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

% Định nghĩa ô bài tập tự luận trong bảng
\newcommand{\oBaiTap}[3][5]{%
  \vspace{1.0mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

\begin{document}
\pagestyle{empty}
'''

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=5, ob12=5, dk13=10, dk14=6, vsa1=0.5, vsa2=0.5):
    res = f'''% =============================================================================
% ========================= TOÁN 7 - TUẦN 08 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 08 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
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
        res += f'\\noindent\\textbf{{Câu {idx} (0,25 điểm).}} {text} \\shortans{{{ans}}}\\par\\vspace{{{vsa1}mm}}\n'

    res += f'''\\vspace{{0.4mm}}

\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a) (0,5 điểm)}}{{{q11['a']}}} & 
\\oBaiTap[{ob11}]{{b) (0,5 điểm)}}{{{q11['b']}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c) (0,5 điểm)}}{{{q11['c']}}} & 
\\oBaiTap[{ob11}]{{d) (0,5 điểm)}}{{{q11['d']}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{e) (0,5 điểm)}}{{{q11['e']}}} & 
\\oBaiTap[{ob11}]{{f) (0,5 điểm)}}{{{q11['f']}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
% =============================================================================
% ========================= TOÁN 7 - TUẦN 08 - BUỔI 01: MÃ ĐỀ {ma_de} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{TOÁN 7 - TUẦN 08 - BUỔI 01}} & \\textbf{{Mã đề: {ma_de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số hữu tỉ $x$, biết:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{a) (0,5 điểm)}}{{{q12['a']}}} & 
\\oBaiTap[{ob12}]{{b) (0,5 điểm)}}{{{q12['b']}}} \\\\
\\hline
\\oBaiTap[{ob12}]{{c) (0,5 điểm)}}{{{q12['c']}}} & 
\\oBaiTap[{ob12}]{{d) (0,5 điểm)}}{{{q12['d']}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.68\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,0 điểm).}} {q13['de']}\\par\\vspace{{0.4mm}}
\\textbf{{a) (1,0 điểm)}} {q13['a']}\\par\\vspace{{0.4mm}}
\\textbf{{b) (1,0 điểm)}} {q13['b']}
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.30\\linewidth}}
\\vspace{{0pt}}\\centering
\\begin{{tikzpicture}}[scale=0.85, >=stealth, line join=round, line cap=round]
  % Hai tia Ax va By
  \\draw[thick, ->] (0.5, 2.3) -- (3.6, 2.3) node[above right=-2pt] {{$x$}};
  \\draw[thick, ->] (0.5, 0.5) -- (3.6, 0.5) node[above right=-2pt] {{$y$}};
  
  % Doan AO va BO
  \\draw[thick] (0.8, 2.3) -- (2.3, 1.4) -- (0.8, 0.5);
  
  % Diem A, B, O
  \\fill (0.8, 2.3) circle (1.5pt) node[above left=1pt] {{$A$}};
  \\fill (0.8, 0.5) circle (1.5pt) node[below left=1pt] {{$B$}};
  \\fill (2.3, 1.4) circle (1.5pt) node[right=2pt] {{$O$}};
  
  % Goc xAO va yBO
  \\draw[red!80!black, thick] (0.8, 2.3) ++(0:0.45) arc (0:-31:0.45);
  \\node[red!80!black, font=\\scriptsize] at (1.5, 2.0) {{${q13['alpha']}^\\circ$}};
  
  \\draw[blue!80!black, thick] (0.8, 0.5) ++(0:0.45) arc (0:31:0.45);
  \\node[blue!80!black, font=\\scriptsize] at (1.5, 0.8) {{${q13['beta']}^\\circ$}};
\\end{{tikzpicture}}
\\end{{minipage}}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (0,5 điểm).}} {q14['de']}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongkeHaiCot{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}

\\newpage
'''
    return res

DATA = {
    '101': {
        'short': [
            (r'Số đối của số hữu tỉ $-\frac{5}{14}$ là:', r'\frac{5}{14}'),
            (r'Giá trị của biểu thức $\sqrt{\frac{49}{100}}$ bằng:', r'\frac{7}{10}'),
            (r'Giá trị của biểu thức $|-4{,}7| + |3{,}3|$ bằng:', r'8'),
            (r'Làm tròn số thập phân $19{,}462$ đến hàng phần mười:', r'19{,}5'),
            (r'Hai đường thẳng cắt nhau tạo góc $55^\circ$. Góc đối đỉnh với nó có số đo là:', r'55^\circ'),
            (r'Cho hai góc kề bù $\widehat{xOy}$ và $\widehat{yOz}$, biết $\widehat{xOy} = 60^\circ$. Số đo $\widehat{yOz}$ là:', r'120^\circ'),
            (r'Tia $Ot$ là tia phân giác của góc $\widehat{xOy} = 130^\circ$. Số đo của $\widehat{xOt}$ là:', r'65^\circ'),
            (r'Cho $a \parallel b$. Một góc so le trong với góc $45^\circ$ có số đo là:', r'45^\circ'),
            (r'Cho $a \parallel b$ và $c \perp a$. Quan hệ giữa hai đường thẳng $c$ và $b$ là:', r'\text{vuông góc}'),
            (r'Một cặp sách giá $250\,000$ đ, giảm $20\%$. Số tiền được giảm là:', r'50\,000\text{ đ}')
        ],
        'q11': {
            'a': r'$\dfrac{7}{15} - \dfrac{5}{8} + \dfrac{8}{15} - \dfrac{3}{8}$',
            'b': r'$\dfrac{12}{19} \cdot \dfrac{5}{7} + \dfrac{12}{19} \cdot \dfrac{2}{7} - \dfrac{12}{19}$',
            'c': r'$\left(-\dfrac{1}{2}\right)^3 \cdot 16 + \left(\dfrac{2}{3}\right)^2 \cdot 9$',
            'd': r'$\sqrt{\dfrac{49}{16}} - \left|-\dfrac{3}{4}\right| + \sqrt{64}$',
            'e': r'$\left(\dfrac{3}{4} - 0{,}2\right) : \dfrac{11}{20} + \dfrac{5}{11} \cdot 1{,}1$',
            'f': r'$\dfrac{4^2 \cdot 9^3}{6^4}$'
        },
        'q12': {
            'a': r'$x + \dfrac{2}{5} = \dfrac{9}{10}$',
            'b': r'$\dfrac{2}{3}x - \dfrac{1}{2} = \dfrac{5}{6}$',
            'c': r'$\left(x - \dfrac{1}{2}\right)^2 = \dfrac{9}{16}$',
            'd': r'$\left|2x - \dfrac{1}{3}\right| = \dfrac{5}{3}$'
        },
        'q13': {
            'de': r'Cho hai tia $Ax$ và $By$ song song với nhau ($Ax \parallel By$). Điểm $O$ nằm giữa hai đường thẳng chứa tia $Ax$ và $By$ sao cho tia $Ax$ và tia $By$ cùng nằm về một phía đối với đường thẳng $AB$. Biết $\widehat{xAO} = 40^\circ$ và $\widehat{yBO} = 50^\circ$.',
            'a': r'Kẻ tia $Oz \parallel Ax$ (tia $Oz$ nằm trong góc $\widehat{AOB}$). Giải thích vì sao $Oz \parallel By$.',
            'b': r'Tính số đo góc $\widehat{AOB}$.',
            'alpha': 40,
            'beta': 50
        },
        'q14': {
            'de': r'Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 2026| + |x - 2|$.'
        }
    },
    '102': {
        'short': [
            (r'Số đối của số hữu tỉ $-\frac{7}{18}$ là:', r'\frac{7}{18}'),
            (r'Giá trị của biểu thức $\sqrt{\frac{64}{81}}$ bằng:', r'\frac{8}{9}'),
            (r'Giá trị của biểu thức $|-5{,}6| + |3{,}4|$ bằng:', r'9'),
            (r'Làm tròn số thập phân $28{,}371$ đến hàng phần mười:', r'28{,}4'),
            (r'Hai đường thẳng cắt nhau tạo góc $65^\circ$. Góc đối đỉnh với nó có số đo là:', r'65^\circ'),
            (r'Cho hai góc kề bù $\widehat{xOy}$ và $\widehat{yOz}$, biết $\widehat{xOy} = 70^\circ$. Số đo $\widehat{yOz}$ là:', r'110^\circ'),
            (r'Tia $Ot$ là tia phân giác của góc $\widehat{xOy} = 150^\circ$. Số đo của $\widehat{xOt}$ là:', r'75^\circ'),
            (r'Cho $a \parallel b$. Một góc đồng vị với góc $60^\circ$ có số đo là:', r'60^\circ'),
            (r'Qua điểm $M$ ở ngoài đường thẳng $d$, có bao nhiêu đường thẳng song song với $d$?', r'1'),
            (r'Một hộp bút giá $80\,000$ đồng, đang giảm giá $25\%$. Số tiền được giảm là:', r'20\,000\text{ đ}')
        ],
        'q11': {
            'a': r'$\dfrac{5}{13} - \dfrac{7}{10} + \dfrac{8}{13} - \dfrac{3}{10}$',
            'b': r'$\dfrac{15}{23} \cdot \dfrac{4}{9} + \dfrac{15}{23} \cdot \dfrac{5}{9} - \dfrac{15}{23}$',
            'c': r'$\left(-\dfrac{1}{3}\right)^2 \cdot 18 + \left(-\dfrac{1}{2}\right)^3 \cdot 24$',
            'd': r'$\sqrt{\dfrac{81}{25}} - \left|-\dfrac{4}{5}\right| + \sqrt{49}$',
            'e': r'$\left(\dfrac{4}{5} - 0{,}25\right) : \dfrac{11}{20} + \dfrac{3}{11} \cdot 2{,}2$',
            'f': r'$\dfrac{8^2 \cdot 27^2}{6^5}$'
        },
        'q12': {
            'a': r'$x + \dfrac{1}{3} = \dfrac{5}{6}$',
            'b': r'$\dfrac{3}{4}x - \dfrac{1}{3} = \dfrac{7}{6}$',
            'c': r'$\left(x - \dfrac{1}{3}\right)^2 = \dfrac{16}{25}$',
            'd': r'$\left|2x - \dfrac{1}{2}\right| = \dfrac{7}{2}$'
        },
        'q13': {
            'de': r'Cho hai tia $Ax$ và $By$ song song với nhau ($Ax \parallel By$). Điểm $O$ nằm giữa hai đường thẳng chứa tia $Ax$ và $By$ sao cho tia $Ax$ và tia $By$ cùng nằm về một phía đối với đường thẳng $AB$. Biết $\widehat{xAO} = 35^\circ$ và $\widehat{yBO} = 55^\circ$.',
            'a': r'Kẻ tia $Oz \parallel Ax$ (tia $Oz$ nằm trong góc $\widehat{AOB}$). Giải thích vì sao $Oz \parallel By$.',
            'b': r'Tính số đo góc $\widehat{AOB}$.',
            'alpha': 35,
            'beta': 55
        },
        'q14': {
            'de': r'Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 2025| + |x - 1|$.'
        }
    },
    '103': {
        'short': [
            (r'Số đối của số hữu tỉ $-\frac{9}{16}$ là:', r'\frac{9}{16}'),
            (r'Giá trị của biểu thức $\sqrt{\frac{81}{121}}$ bằng:', r'\frac{9}{11}'),
            (r'Giá trị của biểu thức $|-6{,}8| + |3{,}2|$ bằng:', r'10'),
            (r'Làm tròn số thập phân $37{,}584$ đến hàng phần mười:', r'37{,}6'),
            (r'Hai đường thẳng cắt nhau tạo góc $75^\circ$. Góc đối đỉnh với nó có số đo là:', r'75^\circ'),
            (r'Cho hai góc kề bù $\widehat{xOy}$ và $\widehat{yOz}$, biết $\widehat{xOy} = 50^\circ$. Số đo $\widehat{yOz}$ là:', r'130^\circ'),
            (r'Tia $Ot$ là tia phân giác của góc $\widehat{xOy} = 140^\circ$. Số đo của $\widehat{xOt}$ là:', r'70^\circ'),
            (r'Cho $a \parallel b$. Một góc trong cùng phía với góc $70^\circ$ có số đo là:', r'110^\circ'),
            (r'Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì hai đường thẳng đó:', r'\text{song song}'),
            (r'Một đôi giày giá $300\,000$ đồng, đang giảm giá $15\%$. Số tiền được giảm là:', r'45\,000\text{ đ}')
        ],
        'q11': {
            'a': r'$\dfrac{9}{17} - \dfrac{4}{9} + \dfrac{8}{17} - \dfrac{5}{9}$',
            'b': r'$\dfrac{17}{21} \cdot \dfrac{3}{8} + \dfrac{17}{21} \cdot \dfrac{5}{8} - \dfrac{17}{21}$',
            'c': r'$\left(-\dfrac{1}{2}\right)^4 \cdot 32 + \left(-\dfrac{2}{3}\right)^2 \cdot 18$',
            'd': r'$\sqrt{\dfrac{64}{9}} - \left|-\dfrac{5}{3}\right| + \sqrt{100}$',
            'e': r'$\left(\dfrac{2}{3} - 0{,}25\right) : \dfrac{5}{12} + \dfrac{4}{7} \cdot 1{,}4$',
            'f': r'$\dfrac{4^3 \cdot 9^2}{6^4}$'
        },
        'q12': {
            'a': r'$x + \dfrac{3}{4} = \dfrac{11}{12}$',
            'b': r'$\dfrac{4}{5}x - \dfrac{1}{2} = \dfrac{11}{10}$',
            'c': r'$\left(x - \dfrac{1}{4}\right)^2 = \dfrac{25}{36}$',
            'd': r'$\left|3x - \dfrac{1}{4}\right| = \dfrac{11}{4}$'
        },
        'q13': {
            'de': r'Cho hai tia $Ax$ và $By$ song song với nhau ($Ax \parallel By$). Điểm $O$ nằm giữa hai đường thẳng chứa tia $Ax$ và $By$ sao cho tia $Ax$ và tia $By$ cùng nằm về một phía đối với đường thẳng $AB$. Biết $\widehat{xAO} = 45^\circ$ và $\widehat{yBO} = 65^\circ$.',
            'a': r'Kẻ tia $Oz \parallel Ax$ (tia $Oz$ nằm trong góc $\widehat{AOB}$). Giải thích vì sao $Oz \parallel By$.',
            'b': r'Tính số đo góc $\widehat{AOB}$.',
            'alpha': 45,
            'beta': 65
        },
        'q14': {
            'de': r'Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 2026| + |x - 6|$.'
        }
    },
    '104': {
        'short': [
            (r'Số đối của số hữu tỉ $-\frac{11}{20}$ là:', r'\frac{11}{20}'),
            (r'Giá trị của biểu thức $\sqrt{\frac{121}{144}}$ bằng:', r'\frac{11}{12}'),
            (r'Giá trị của biểu thức $|-7{,}5| + |3{,}5|$ bằng:', r'11'),
            (r'Làm tròn số thập phân $46{,}293$ đến hàng phần mười:', r'46{,}3'),
            (r'Hai đường thẳng cắt nhau tạo góc $85^\circ$. Góc đối đỉnh với nó có số đo là:', r'85^\circ'),
            (r'Cho hai góc kề bù $\widehat{xOy}$ và $\widehat{yOz}$, biết $\widehat{xOy} = 80^\circ$. Số đo $\widehat{yOz}$ là:', r'100^\circ'),
            (r'Tia $Ot$ là tia phân giác của góc $\widehat{xOy} = 160^\circ$. Số đo của $\widehat{xOt}$ là:', r'80^\circ'),
            (r'Cho $a \parallel b$. Một góc trong cùng phía với góc $80^\circ$ có số đo là:', r'100^\circ'),
            (r'Hai đường thẳng phân biệt cùng vuông góc với đường thẳng thứ ba thì hai đường thẳng đó:', r'\text{song song}'),
            (r'Một chiếc áo khoác giá $400\,000$ đồng, đang giảm giá $10\%$. Số tiền được giảm là:', r'40\,000\text{ đ}')
        ],
        'q11': {
            'a': r'$\dfrac{6}{19} - \dfrac{5}{11} + \dfrac{13}{19} - \dfrac{6}{11}$',
            'b': r'$\dfrac{14}{25} \cdot \dfrac{7}{10} + \dfrac{14}{25} \cdot \dfrac{3}{10} - \dfrac{14}{25}$',
            'c': r'$\left(-\dfrac{3}{2}\right)^2 \cdot 8 - \left(-\dfrac{1}{3}\right)^3 \cdot 54$',
            'd': r'$\sqrt{\dfrac{121}{36}} - \left|-\dfrac{5}{6}\right| + \sqrt{121}$',
            'e': r'$\left(\dfrac{3}{5} - 0{,}25\right) : \dfrac{7}{20} + \dfrac{5}{9} \cdot 1{,}8$',
            'f': r'$\dfrac{25^2 \cdot 4^3}{10^4}$'
        },
        'q12': {
            'a': r'$x + \dfrac{2}{7} = \dfrac{11}{14}$',
            'b': r'$\dfrac{5}{6}x - \dfrac{1}{4} = \dfrac{17}{12}$',
            'c': r'$\left(x - \dfrac{1}{5}\right)^2 = \dfrac{9}{25}$',
            'd': r'$\left|2x - \dfrac{1}{5}\right| = \dfrac{9}{5}$'
        },
        'q13': {
            'de': r'Cho hai tia $Ax$ và $By$ song song với nhau ($Ax \parallel By$). Điểm $O$ nằm giữa hai đường thẳng chứa tia $Ax$ và $By$ sao cho tia $Ax$ và tia $By$ cùng nằm về một phía đối với đường thẳng $AB$. Biết $\widehat{xAO} = 50^\circ$ và $\widehat{yBO} = 60^\circ$.',
            'a': r'Kẻ tia $Oz \parallel Ax$ (tia $Oz$ nằm trong góc $\widehat{AOB}$). Giải thích vì sao $Oz \parallel By$.',
            'b': r'Tính số đo góc $\widehat{AOB}$.',
            'alpha': 50,
            'beta': 60
        },
        'q14': {
            'de': r'Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 2024| + |x - 4|$.'
        }
    }
}

def generate_pdf(ob11=5, ob12=5, dk13=10, dk14=6, vsa1=0.5):
    tex_content = TEX_TEMPLATE
    for ma_de in ['101', '102', '103', '104']:
        d = DATA[ma_de]
        tex_content += render_de(ma_de, d['short'], d['q11'], d['q12'], d['q13'], d['q14'],
                                 ob11=ob11, ob12=ob12, dk13=dk13, dk14=dk14, vsa1=vsa1)
    tex_content += r'\end{document}'

    tex_path = 'Phieu_Kiem_Tra_Tuan_08_Buoi_01.tex'
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)

    print(f"Compiling {tex_path} with ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}, vsa1={vsa1}...")
    cmd = ['pdflatex', '-interaction=nonstopmode', tex_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    pdf_path = 'Phieu_Kiem_Tra_Tuan_08_Buoi_01.pdf'
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        return num_pages
    else:
        print("PDF compilation failed!")
        return -1

if __name__ == '__main__':
    # Initial run
    num_pages = generate_pdf(ob11=5, ob12=5, dk13=10, dk14=6, vsa1=0.4)
    print(f"Resulting pages: {num_pages}")
