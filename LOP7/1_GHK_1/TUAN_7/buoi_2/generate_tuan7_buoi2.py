import os
import sys
import json
import math
import subprocess
import pypdf
import fitz  # PyMuPDF

# Đảm bảo in tiếng Việt không lỗi font
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

tex_template_header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=3.2,heightSA=0.62}

\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ đều đặn chuẩn viết tay (khoảng cách dòng 18.5pt)
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

% Định nghĩa ô bài tập tự luận trong bảng 2x2
\newcommand{\oBaiTap}[3][6]{%
  \vspace{1.0mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

\begin{document}
\pagestyle{empty}
'''

def generate_tikz(alpha_deg):
    alpha_rad = math.radians(alpha_deg)
    y_A = 2.3
    y_B = 0.5
    h = y_A - y_B  # 1.8
    x_AB = 0.8
    x_C = 2.5
    x_D = x_C - h / math.tan(alpha_rad)
    
    # Tính tọa độ kéo dài cát tuyến c
    dx = (x_D - x_C)
    c_top_y = 2.85
    c_top_x = x_C + (c_top_y - y_A) * (dx / -h)
    c_bot_y = 0.05
    c_bot_x = x_C + (c_bot_y - y_A) * (dx / -h)
    
    r_arc = 0.38
    
    tikz = f"""\\begin{{tikzpicture}}[scale=0.76, >=stealth, line join=round, line cap=round]
  % Duong thang a va b
  \\draw[thick] (0.2, {y_A:.2f}) -- (3.9, {y_A:.2f}) node[right=1pt] {{$a$}};
  \\draw[thick] (0.2, {y_B:.2f}) -- (3.9, {y_B:.2f}) node[right=1pt] {{$b$}};
  
  % Doan thang vuong goc AB
  \\draw[thick] ({x_AB:.2f}, 0.05) -- ({x_AB:.2f}, 2.85);
  \\fill ({x_AB:.2f}, {y_A:.2f}) circle (1.5pt) node[above left] {{$A$}};
  \\fill ({x_AB:.2f}, {y_B:.2f}) circle (1.5pt) node[below left] {{$B$}};
  
  % Ki hieu goc vuong tai A va B
  \\draw ({x_AB:.2f}, {y_A - 0.22:.2f}) -- ({x_AB + 0.22:.2f}, {y_A - 0.22:.2f}) -- ({x_AB + 0.22:.2f}, {y_A:.2f});
  \\draw ({x_AB:.2f}, {y_B + 0.22:.2f}) -- ({x_AB + 0.22:.2f}, {y_B + 0.22:.2f}) -- ({x_AB + 0.22:.2f}, {y_B:.2f});
  
  % Cat tuyen c (ve tu bot den top de node c o tren cung)
  \\draw[thick] ({c_bot_x:.2f}, {c_bot_y:.2f}) -- ({c_top_x:.2f}, {c_top_y:.2f}) node[above=1pt] {{$c$}};
  \\fill ({x_C:.2f}, {y_A:.2f}) circle (1.5pt) node[above right=1pt] {{$C$}};
  \\fill ({x_D:.2f}, {y_B:.2f}) circle (1.5pt) node[below right=1pt] {{$D$}};
  
  % Cung goc C1 (goc ACD = alpha)
  \\draw[red!80!black, thick] ({x_C:.2f}, {y_A:.2f}) ++(180:{r_arc:.2f}) arc (180:{180 + alpha_deg}:{r_arc:.2f});
  \\node[red!80!black, font=\\scriptsize] at ({x_C - 0.42:.2f}, {y_A - 0.26:.2f}) {{$1$}};
  
  % Cung goc D1 (so le trong voi C1: goc giua Db phai va DC)
  \\draw[red!80!black, thick] ({x_D:.2f}, {y_B:.2f}) ++(0:{r_arc:.2f}) arc (0:{alpha_deg}:{r_arc:.2f});
  \\node[red!80!black, font=\\scriptsize] at ({x_D + 0.42:.2f}, {y_B + 0.24:.2f}) {{$1$}};
  
  % Cung goc D2 (trong cung phia voi C1: goc BDC)
  \\draw[blue!80!black, thick] ({x_D:.2f}, {y_B:.2f}) ++({alpha_deg}:{r_arc + 0.08:.2f}) arc ({alpha_deg}:180:{r_arc + 0.08:.2f});
  \\node[blue!80!black, font=\\scriptsize] at ({x_D - 0.36:.2f}, {y_B + 0.28:.2f}) {{$2$}};
\\end{{tikzpicture}}"""
    return tikz

def render_de(ma_de, q_short, q11, q12, q13, q14, ob11=8, ob12=5, dk13=11, dk14=7):
    tikz_fig = generate_tikz(q13['angle'])
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

\\vspace{{1.2mm}}

'''
    # 10 câu trả lời ngắn
    for idx, (text, ans) in enumerate(q_short, 1):
        res += f'\\noindent\\textbf{{Câu {idx} (0,25 điểm).}} {text} \\shortans{{{ans}}}\\par\\vspace{{0.35mm}}\n'

    res += f'''\\vspace{{0.6mm}}

\\noindent\\textbf{{Câu 11 (2,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a)}}{{${q11['a']}$}} & 
\\oBaiTap[{ob11}]{{b)}}{{${q11['b']}$}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c)}}{{${q11['c']}$}} & 
\\oBaiTap[{ob11}]{{d)}}{{${q11['d']}$}} \\\\
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
\\oBaiTap[{ob12}]{{a)}}{{${q12['a']}$}} & 
\\oBaiTap[{ob12}]{{b)}}{{${q12['b']}$}} \\\\
\\hline
\\oBaiTap[{ob12}]{{c)}}{{${q12['c']}$}} & 
\\oBaiTap[{ob12}]{{d)}}{{${q12['d']}$}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\begin{{minipage}}[t]{{0.67\\linewidth}}
\\vspace{{0pt}}
\\textbf{{Câu 13 (2,5 điểm).}} Cho hình vẽ bên, biết đường thẳng $a \\perp AB$ tại $A$ và $b \\perp AB$ tại $B$. Đường thẳng $c$ cắt $a$ tại $C$ và cắt $b$ tại $D$ tạo thành góc $\\widehat{{C}}_1 = {q13['angle']}^\\circ$.\\par\\vspace{{0.4mm}}
\\textbf{{a) (1,25 điểm)}} Ghi Giả thiết (GT), Kết luận (KL) của bài toán. Chứng minh rằng $a \\parallel b$.\\par\\vspace{{0.4mm}}
\\textbf{{b) (1,25 điểm)}} Hãy tính số đo của góc so le trong $\\widehat{{D}}_1$ và góc trong cùng phía $\\widehat{{D}}_2$ với góc $\\widehat{{C}}_1$.
\\end{{minipage}}\\hfill
\\begin{{minipage}}[t]{{0.31\\linewidth}}
\\vspace{{0pt}}\\centering
{tikz_fig}
\\end{{minipage}}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (1,0 điểm).}} {q14['de']}\\par
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
            ("Trong định lí: \\textit{\"Nếu một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với đường thẳng kia\"}, phần kết luận là gì?", "nó cũng vuông góc với đường thẳng kia"),
            ("Giá trị của biểu thức $\\sqrt{121} - \\sqrt{25}$ bằng bao nhiêu?", "6"),
            ("Giá trị của biểu thức $\\vert -4{,}7\\vert + \\vert 3{,}3\\vert$ bằng bao nhiêu?", "8"),
            ("Làm tròn số $19{,}453$ đến hàng phần mười (chữ số thập phân thứ nhất).", "19{,}5"),
            ("Cho hai góc $\\widehat{xOy}$ và $\\widehat{yOz}$ kề bù, biết $\\widehat{xOy} = 65^\\circ$. Số đo góc $\\widehat{yOz}$ là:", "115^\\circ"),
            ("Cho $a \\perp c$ và $b \\perp c$. Quan hệ giữa hai đường thẳng phân biệt $a$ và $b$ là:", "song song"),
            ("Giá trị của biểu thức $\\left(-\\frac{2}{3}\\right)^2 + \\frac{5}{9}$ bằng bao nhiêu?", "1"),
            ("Cho tia $Oz$ là tia phân giác của $\\widehat{xOy} = 84^\\circ$. Số đo góc $\\widehat{xOz}$ là:", "42^\\circ"),
            ("Tìm số thực $x \\ge 0$, biết $\\sqrt{x} = 8$.", "64"),
            ("Hộp bút giá $50\\,000$ đ được giảm giá $20\\%$. Số tiền được giảm là:", "10\\,000\\text{ đ}")
        ],
        'q11': {
            'a': r"\frac{7}{15} + \left(-\frac{8}{5}\right) + \frac{8}{15}",
            'b': r"\frac{5}{9} \cdot \left(-\frac{7}{13}\right) + \frac{5}{9} \cdot \left(-\frac{6}{13}\right)",
            'c': r"\left(-\frac{1}{2}\right)^2 \cdot 24 - 1{,}5 \cdot 6",
            'd': r"\sqrt{\frac{49}{25}} - \vert -0{,}4\vert + \sqrt{81}"
        },
        'q12': {
            'a': r"x - \frac{1}{3} = \frac{5}{9}",
            'b': r"\frac{2}{3}x + \frac{1}{4} = \frac{11}{12}",
            'c': r"\left(x - \frac{1}{2}\right)^2 = \frac{9}{16}",
            'd': r"\vert 2x - 1\vert = 7"
        },
        'q13': {
            'angle': 70
        },
        'q14': {
            'de': r"Cho biểu thức $A = \frac{1}{2} + \frac{1}{2^2} + \frac{1}{2^3} + \dots + \frac{1}{2^{100}}$. Chứng minh rằng $A < 1$."
        }
    },
    '102': {
        'short': [
            ("Trong định lí: \\textit{\"Nếu hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì chúng song song với nhau\"}, phần kết luận là gì?", "chúng song song với nhau"),
            ("Giá trị của biểu thức $\\sqrt{144} - \\sqrt{49}$ bằng bao nhiêu?", "5"),
            ("Giá trị của biểu thức $\\vert -5{,}6\\vert + \\vert 3{,}4\\vert$ bằng bao nhiêu?", "9"),
            ("Làm tròn số $28{,}374$ đến hàng phần mười (chữ số thập phân thứ nhất).", "28{,}4"),
            ("Cho hai góc $\\widehat{xOy}$ và $\\widehat{yOz}$ kề bù, biết $\\widehat{xOy} = 70^\\circ$. Số đo góc $\\widehat{yOz}$ là:", "110^\\circ"),
            ("Cho $a \\parallel b$ và $c \\perp a$. Quan hệ giữa đường thẳng $c$ và đường thẳng $b$ là:", "vuông góc"),
            ("Giá trị của biểu thức $\\left(-\\frac{3}{4}\\right)^2 + \\frac{7}{16}$ bằng bao nhiêu?", "1"),
            ("Cho tia $Oz$ là tia phân giác của $\\widehat{xOy} = 76^\\circ$. Số đo góc $\\widehat{xOz}$ là:", "38^\\circ"),
            ("Tìm số thực $x \\ge 0$, biết $\\sqrt{x} = 7$.", "49"),
            ("Cuốn từ điển giá $150\\,000$ đ được giảm $20\\%$. Số tiền được giảm là:", "30\\,000\\text{ đ}")
        ],
        'q11': {
            'a': r"\frac{5}{18} + \left(-\frac{7}{4}\right) + \frac{13}{18}",
            'b': r"\frac{4}{11} \cdot \left(-\frac{9}{17}\right) + \frac{4}{11} \cdot \left(-\frac{8}{17}\right)",
            'c': r"\left(-\frac{1}{3}\right)^2 \cdot 27 - 2{,}5 \cdot 4",
            'd': r"\sqrt{\frac{64}{25}} - \vert -0{,}6\vert + \sqrt{100}"
        },
        'q12': {
            'a': r"x - \frac{1}{4} = \frac{7}{16}",
            'b': r"\frac{3}{4}x + \frac{1}{5} = \frac{19}{20}",
            'c': r"\left(x + \frac{1}{3}\right)^2 = \frac{25}{36}",
            'd': r"\vert 2x + 3\vert = 9"
        },
        'q13': {
            'angle': 65
        },
        'q14': {
            'de': r"Cho biểu thức $B = \frac{1}{3} + \frac{1}{3^2} + \frac{1}{3^3} + \dots + \frac{1}{3^{100}}$. Chứng minh rằng $B < \frac{1}{2}$."
        }
    },
    '103': {
        'short': [
            ("Trong định lí: \\textit{\"Nếu hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau\"}, phần kết luận là gì?", "chúng song song với nhau"),
            ("Giá trị của biểu thức $\\sqrt{169} - \\sqrt{64}$ bằng bao nhiêu?", "5"),
            ("Giá trị của biểu thức $\\vert -6{,}8\\vert + \\vert 3{,}2\\vert$ bằng bao nhiêu?", "10"),
            ("Làm tròn số $35{,}628$ đến hàng phần mười (chữ số thập phân thứ nhất).", "35{,}6"),
            ("Cho hai góc $\\widehat{xOy}$ và $\\widehat{yOz}$ kề bù, biết $\\widehat{xOy} = 80^\\circ$. Số đo góc $\\widehat{yOz}$ là:", "100^\\circ"),
            ("Cho $a \\parallel b$ và $b \\parallel c$. Quan hệ giữa hai đường thẳng phân biệt $a$ và $c$ là:", "song song"),
            ("Giá trị của biểu thức $\\left(-\\frac{4}{5}\\right)^2 + \\frac{9}{25}$ bằng bao nhiêu?", "1"),
            ("Cho tia $Oz$ là tia phân giác của $\\widehat{xOy} = 92^\\circ$. Số đo góc $\\widehat{xOz}$ là:", "46^\\circ"),
            ("Tìm số thực $x \\ge 0$, biết $\\sqrt{x} = 6$.", "36"),
            ("Bộ đồng phục giá $250\\,000$ đ được giảm $20\\%$. Số tiền được giảm là:", "50\\,000\\text{ đ}")
        ],
        'q11': {
            'a': r"\frac{8}{21} + \left(-\frac{5}{3}\right) + \frac{13}{21}",
            'b': r"\frac{6}{13} \cdot \left(-\frac{11}{19}\right) + \frac{6}{13} \cdot \left(-\frac{8}{19}\right)",
            'c': r"\left(-\frac{1}{2}\right)^3 \cdot 32 + 2{,}5 \cdot (-4)",
            'd': r"\sqrt{\frac{81}{16}} - \vert -1{,}25\vert + \sqrt{64}"
        },
        'q12': {
            'a': r"x - \frac{1}{5} = \frac{9}{25}",
            'b': r"\frac{4}{5}x - \frac{1}{2} = \frac{3}{10}",
            'c': r"\left(x - \frac{1}{4}\right)^2 = \frac{49}{64}",
            'd': r"\vert 3x - 2\vert = 7"
        },
        'q13': {
            'angle': 75
        },
        'q14': {
            'de': r"Cho biểu thức $C = \frac{1}{4} + \frac{1}{4^2} + \frac{1}{4^3} + \dots + \frac{1}{4^{100}}$. Chứng minh rằng $C < \frac{1}{3}$."
        }
    },
    '104': {
        'short': [
            ("Trong định lí: \\textit{\"Nếu hai góc đối đỉnh thì hai góc đó bằng nhau\"}, phần kết luận là gì?", "hai góc đó bằng nhau"),
            ("Giá trị của biểu thức $\\sqrt{196} - \\sqrt{81}$ bằng bao nhiêu?", "5"),
            ("Giá trị của biểu thức $\\vert -7{,}5\\vert + \\vert 4{,}5\\vert$ bằng bao nhiêu?", "12"),
            ("Làm tròn số $42{,}865$ đến hàng phần mười (chữ số thập phân thứ nhất).", "42{,}9"),
            ("Cho hai góc $\\widehat{xOy}$ và $\\widehat{yOz}$ kề bù, biết $\\widehat{xOy} = 50^\\circ$. Số đo góc $\\widehat{yOz}$ là:", "130^\\circ"),
            ("Hai đường thẳng $xx', yy'$ cắt nhau tại $O$. Nếu $\\widehat{xOy} = 90^\\circ$ thì góc đối đỉnh $\\widehat{x'Oy'}$ bằng:", "90^\\circ"),
            ("Giá trị của biểu thức $\\left(-\\frac{5}{6}\\right)^2 + \\frac{11}{36}$ bằng bao nhiêu?", "1"),
            ("Cho tia $Oz$ là tia phân giác của $\\widehat{xOy} = 104^\\circ$. Số đo góc $\\widehat{xOz}$ là:", "52^\\circ"),
            ("Tìm số thực $x \\ge 0$, biết $\\sqrt{x} = 5$.", "25"),
            ("Chiếc cặp sách giá $200\\,000$ đ giảm $20\\%$. Số tiền được giảm là:", "40\\,000\\text{ đ}")
        ],
        'q11': {
            'a': r"\frac{7}{20} + \left(-\frac{9}{5}\right) + \frac{13}{20}",
            'b': r"\frac{7}{15} \cdot \left(-\frac{14}{23}\right) + \frac{7}{15} \cdot \left(-\frac{9}{23}\right)",
            'c': r"\left(-\frac{2}{3}\right)^2 \cdot 18 - 3{,}5 \cdot 4",
            'd': r"\sqrt{\frac{121}{25}} - \vert -1{,}2\vert + \sqrt{49}"
        },
        'q12': {
            'a': r"x - \frac{1}{6} = \frac{11}{36}",
            'b': r"\frac{5}{6}x - \frac{1}{3} = \frac{1}{2}",
            'c': r"\left(x + \frac{1}{5}\right)^2 = \frac{36}{25}",
            'd': r"\vert 3x + 4\vert = 10"
        },
        'q13': {
            'angle': 55
        },
        'q14': {
            'de': r"Cho biểu thức $D = \frac{1}{5} + \frac{1}{5^2} + \frac{1}{5^3} + \dots + \frac{1}{5^{100}}$. Chứng minh rằng $D < \frac{1}{4}$."
        }
    }
}

def build_full_tex(ob11=8, ob12=5, dk13=11, dk14=8):
    content = tex_template_header
    for ma_de in ['101', '102', '103', '104']:
        d = de_data[ma_de]
        content += render_de(ma_de, d['short'], d['q11'], d['q12'], d['q13'], d['q14'], ob11, ob12, dk13, dk14)
    content += r'\end{document}'
    return content

def compile_pdf(tex_path, work_dir):
    cmd = ['pdflatex', '-interaction=nonstopmode', os.path.basename(tex_path)]
    p = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
    return p.returncode == 0

def get_page_count(pdf_path):
    if not os.path.exists(pdf_path):
        return -1
    reader = pypdf.PdfReader(pdf_path)
    return len(reader.pages)

def export_preview_images(pdf_path, work_dir):
    doc = fitz.open(pdf_path)
    if len(doc) >= 2:
        page1 = doc.load_page(0)
        pix1 = page1.get_pixmap(dpi=150)
        pix1.save(os.path.join(work_dir, "page_1.png"))
        
        page2 = doc.load_page(1)
        pix2 = page2.get_pixmap(dpi=150)
        pix2.save(os.path.join(work_dir, "page_2.png"))
        print("Đã xuất ảnh xem trước: page_1.png và page_2.png")
    doc.close()

def export_answers_md(work_dir):
    md_content = """# ĐÁP ÁN & THANG ĐIỂM CHI TIẾT
## TOÁN 7 - TUẦN 07 - BUỔI 02
### CHỦ ĐỀ: BÀI 11 - ĐỊNH LÍ VÀ CHỨNG MINH ĐỊNH LÍ (TỔNG ÔN THI GIỮA HỌC KỲ 1)
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 BẢNG ĐÁP ÁN 10 CÂU TRẢ LỜI NGẮN (2,5 ĐIỂM - MỖI CÂU 0,25 Đ)

| Câu | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 | Điểm |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Câu 1** | nó cũng vuông góc với đường thẳng kia | chúng song song với nhau | chúng song song với nhau | hai góc đó bằng nhau | 0,25 đ |
| **Câu 2** | $6$ | $5$ | $5$ | $5$ | 0,25 đ |
| **Câu 3** | $8$ | $9$ | $10$ | $12$ | 0,25 đ |
| **Câu 4** | $19{,}5$ | $28{,}4$ | $35{,}6$ | $42{,}9$ | 0,25 đ |
| **Câu 5** | $115^\\circ$ | $110^\\circ$ | $100^\\circ$ | $130^\\circ$ | 0,25 đ |
| **Câu 6** | song song | vuông góc | song song | $90^\\circ$ | 0,25 đ |
| **Câu 7** | $1$ | $1$ | $1$ | $1$ | 0,25 đ |
| **Câu 8** | $42^\\circ$ | $38^\\circ$ | $46^\\circ$ | $52^\\circ$ | 0,25 đ |
| **Câu 9** | $64$ | $49$ | $36$ | $25$ | 0,25 đ |
| **Câu 10** | $10\\,000\\text{ đ}$ | $30\\,000\\text{ đ}$ | $50\\,000\\text{ đ}$ | $40\\,000\\text{ đ}$ | 0,25 đ |

---

## 📝 BAREM CHẤM TỰ LUẬN CHI TIẾT (CÂU 11 - CÂU 14)

### CÂU 11 (2,0 ĐIỂM). THỰC HIỆN PHÉP TÍNH (MỖI Ý 0,5 ĐIỂM)

#### Mã đề 101:
* **a) (0,5 đ):** $\\frac{7}{15} + \\left(-\\frac{8}{5}\\right) + \\frac{8}{15} = \\left(\\frac{7}{15} + \\frac{8}{15}\\right) - \\frac{8}{5} = 1 - \\frac{8}{5} = -\\frac{3}{5}$.
* **b) (0,5 đ):** $\\frac{5}{9} \\cdot \\left(-\\frac{7}{13}\\right) + \\frac{5}{9} \\cdot \\left(-\\frac{6}{13}\\right) = \\frac{5}{9}\\left(-\\frac{7}{13} - \\frac{6}{13}\\right) = \\frac{5}{9} \\cdot (-1) = -\\frac{5}{9}$.
* **c) (0,5 đ):** $\\left(-\\frac{1}{2}\\right)^2 \\cdot 24 - 1{,}5 \\cdot 6 = \\frac{1}{4} \\cdot 24 - 9 = 6 - 9 = -3$.
* **d) (0,5 đ):** $\\sqrt{\\frac{49}{25}} - \\vert -0{,}4\\vert + \\sqrt{81} = \\frac{7}{5} - \\frac{2}{5} + 9 = 1 + 9 = 10$.

#### Mã đề 102:
* **a) (0,5 đ):** $\\frac{5}{18} + \\left(-\\frac{7}{4}\\right) + \\frac{13}{18} = \\left(\\frac{5}{18} + \\frac{13}{18}\\right) - \\frac{7}{4} = 1 - \\frac{7}{4} = -\\frac{3}{4}$.
* **b) (0,5 đ):** $\\frac{4}{11} \\cdot \\left(-\\frac{9}{17}\\right) + \\frac{4}{11} \\cdot \\left(-\\frac{8}{17}\\right) = \\frac{4}{11}\\left(-\\frac{17}{17}\\right) = -\\frac{4}{11}$.
* **c) (0,5 đ):** $\\left(-\\frac{1}{3}\\right)^2 \\cdot 27 - 2{,}5 \\cdot 4 = \\frac{1}{9} \\cdot 27 - 10 = 3 - 10 = -7$.
* **d) (0,5 đ):** $\\sqrt{\\frac{64}{25}} - \\vert -0{,}6\\vert + \\sqrt{100} = \\frac{8}{5} - \\frac{3}{5} + 10 = 1 + 10 = 11$.

#### Mã đề 103:
* **a) (0,5 đ):** $\\frac{8}{21} + \\left(-\\frac{5}{3}\\right) + \\frac{13}{21} = \\left(\\frac{8}{21} + \\frac{13}{21}\\right) - \\frac{5}{3} = 1 - \\frac{5}{3} = -\\frac{2}{3}$.
* **b) (0,5 đ):** $\\frac{6}{13} \\cdot \\left(-\\frac{11}{19}\\right) + \\frac{6}{13} \\cdot \\left(-\\frac{8}{19}\\right) = \\frac{6}{13}\\left(-\\frac{19}{19}\\right) = -\\frac{6}{13}$.
* **c) (0,5 đ):** $\\left(-\\frac{1}{2}\\right)^3 \\cdot 32 + 2{,}5 \\cdot (-4) = -\\frac{1}{8} \\cdot 32 - 10 = -4 - 10 = -14$.
* **d) (0,5 đ):** $\\sqrt{\\frac{81}{16}} - \\vert -1{,}25\\vert + \\sqrt{64} = \\frac{9}{4} - \\frac{5}{4} + 8 = 1 + 8 = 9$.

#### Mã đề 104:
* **a) (0,5 đ):** $\\frac{7}{20} + \\left(-\\frac{9}{5}\\right) + \\frac{13}{20} = \\left(\\frac{7}{20} + \\frac{13}{20}\\right) - \\frac{9}{5} = 1 - \\frac{9}{5} = -\\frac{4}{5}$.
* **b) (0,5 đ):** $\\frac{7}{15} \\cdot \\left(-\\frac{14}{23}\\right) + \\frac{7}{15} \\cdot \\left(-\\frac{9}{23}\\right) = \\frac{7}{15}\\left(-\\frac{23}{23}\\right) = -\\frac{7}{15}$.
* **c) (0,5 đ):** $\\left(-\\frac{2}{3}\\right)^2 \\cdot 18 - 3{,}5 \\cdot 4 = \\frac{4}{9} \\cdot 18 - 14 = 8 - 14 = -6$.
* **d) (0,5 đ):** $\\sqrt{\\frac{121}{25}} - \\vert -1{,}2\\vert + \\sqrt{49} = \\frac{11}{5} - \\frac{6}{5} + 7 = 1 + 7 = 8$.

---

### CÂU 12 (2,0 ĐIỂM). TÌM SỐ HỮU TỈ $x$, BIẾT (MỖI Ý 0,5 ĐIỂM)

#### Mã đề 101:
* **a) (0,5 đ):** $x - \\frac{1}{3} = \\frac{5}{9} \\implies x = \\frac{5}{9} + \\frac{3}{9} = \\frac{8}{9}$.
* **b) (0,5 đ):** $\\frac{2}{3}x + \\frac{1}{4} = \\frac{11}{12} \\implies \\frac{2}{3}x = \\frac{11}{12} - \\frac{3}{12} = \\frac{8}{12} = \\frac{2}{3} \\implies x = 1$.
* **c) (0,5 đ):** $\\left(x - \\frac{1}{2}\\right)^2 = \\frac{9}{16} \\implies x - \\frac{1}{2} = \\pm\\frac{3}{4} \\implies x = \\frac{5}{4}$ hoặc $x = -\\frac{1}{4}$.
* **d) (0,5 đ):** $\\vert 2x - 1\\vert = 7 \\implies 2x - 1 = 7$ hoặc $2x - 1 = -7 \\implies x = 4$ hoặc $x = -3$.

#### Mã đề 102:
* **a) (0,5 đ):** $x - \\frac{1}{4} = \\frac{7}{16} \\implies x = \\frac{7}{16} + \\frac{4}{16} = \\frac{11}{16}$.
* **b) (0,5 đ):** $\\frac{3}{4}x + \\frac{1}{5} = \\frac{19}{20} \\implies \\frac{3}{4}x = \\frac{19}{20} - \\frac{4}{20} = \\frac{15}{20} = \\frac{3}{4} \\implies x = 1$.
* **c) (0,5 đ):** $\\left(x + \\frac{1}{3}\\right)^2 = \\frac{25}{36} \\implies x + \\frac{1}{3} = \\pm\\frac{5}{6} \\implies x = \\frac{1}{2}$ hoặc $x = -\\frac{7}{6}$.
* **d) (0,5 đ):** $\\vert 2x + 3\\vert = 9 \\implies 2x + 3 = 9$ hoặc $2x + 3 = -9 \\implies x = 3$ hoặc $x = -6$.

#### Mã đề 103:
* **a) (0,5 đ):** $x - \\frac{1}{5} = \\frac{9}{25} \\implies x = \\frac{9}{25} + \\frac{5}{25} = \\frac{14}{25}$.
* **b) (0,5 đ):** $\\frac{4}{5}x - \\frac{1}{2} = \\frac{3}{10} \\implies \\frac{4}{5}x = \\frac{3}{10} + \\frac{5}{10} = \\frac{8}{10} = \\frac{4}{5} \\implies x = 1$.
* **c) (0,5 đ):** $\\left(x - \\frac{1}{4}\\right)^2 = \\frac{49}{64} \\implies x - \\frac{1}{4} = \\pm\\frac{7}{8} \\implies x = \\frac{9}{8}$ hoặc $x = -\\frac{5}{8}$.
* **d) (0,5 đ):** $\\vert 3x - 2\\vert = 7 \\implies 3x - 2 = 7$ hoặc $3x - 2 = -7 \\implies x = 3$ hoặc $x = -\\frac{5}{3}$.

#### Mã đề 104:
* **a) (0,5 đ):** $x - \\frac{1}{6} = \\frac{11}{36} \\implies x = \\frac{11}{36} + \\frac{6}{36} = \\frac{17}{36}$.
* **b) (0,5 đ):** $\\frac{5}{6}x - \\frac{1}{3} = \\frac{1}{2} \\implies \\frac{5}{6}x = \\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6} \\implies x = 1$.
* **c) (0,5 đ):** $\\left(x + \\frac{1}{5}\\right)^2 = \\frac{36}{25} \\implies x + \\frac{1}{5} = \\pm\\frac{6}{5} \\implies x = 1$ hoặc $x = -\\frac{7}{5}$.
* **d) (0,5 đ):** $\\vert 3x + 4\\vert = 10 \\implies 3x + 4 = 10$ hoặc $3x + 4 = -10 \\implies x = 2$ hoặc $x = -\\frac{14}{3}$.

---

### CÂU 13 (2,5 ĐIỂM). HÌNH HỌC - ĐỊNH LÍ VÀ CHỨNG MINH ĐỊNH LÍ

* **a) (1,25 điểm):**
  - **Ghi GT, KL (0,5 đ):**
    + **GT:** $a \\perp AB$ tại $A$; $b \\perp AB$ tại $B$; cát tuyến $c$ cắt $a, b$ tại $C, D$; $\\widehat{C}_1 = \\alpha$.
    + **KL:** $a \\parallel b$; tính số đo $\\widehat{D}_1, \\widehat{D}_2$.
  - **Chứng minh $a \\parallel b$ (0,75 đ):**
    Vì $a \\perp AB$ và $b \\perp AB$ nên theo định lí *\"Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau\"*, ta suy ra $a \\parallel b$.

* **b) (1,25 điểm): Tính số đo góc:**
  - **Mã đề 101 ($\\widehat{C}_1 = 70^\\circ$):**
    + Vì $a \\parallel b$ nên $\\widehat{D}_1 = \\widehat{C}_1 = 70^\\circ$ (hai góc so le trong). *(0,6đ)*
    + Vì $\\widehat{D}_2$ và $\\widehat{C}_1$ là hai góc trong cùng phía nên $\\widehat{D}_2 + \\widehat{C}_1 = 180^\\circ \\implies \\widehat{D}_2 = 180^\\circ - 70^\\circ = 110^\\circ$. *(0,65đ)*
  - **Mã đề 102 ($\\widehat{C}_1 = 65^\\circ$):**
    + $\\widehat{D}_1 = \\widehat{C}_1 = 65^\\circ$ (so le trong). *(0,6đ)*
    + $\\widehat{D}_2 = 180^\\circ - 65^\\circ = 115^\\circ$ (trong cùng phía bù nhau). *(0,65đ)*
  - **Mã đề 103 ($\\widehat{C}_1 = 75^\\circ$):**
    + $\\widehat{D}_1 = \\widehat{C}_1 = 75^\\circ$ (so le trong). *(0,6đ)*
    + $\\widehat{D}_2 = 180^\\circ - 75^\\circ = 105^\\circ$ (trong cùng phía bù nhau). *(0,65đ)*
  - **Mã đề 104 ($\\widehat{C}_1 = 55^\\circ$):**
    + $\\widehat{D}_1 = \\widehat{C}_1 = 55^\\circ$ (so le trong). *(0,6đ)*
    + $\\widehat{D}_2 = 180^\\circ - 55^\\circ = 125^\\circ$ (trong cùng phía bù nhau). *(0,65đ)*

---

### CÂU 14 (1,0 ĐIỂM). BÀI TOÁN NÂNG CAO

* **Mã đề 101 ($A < 1$):**
  - Ta có: $2A = 1 + \\frac{1}{2} + \\frac{1}{2^2} + \\dots + \\frac{1}{2^{99}}$. *(0,35đ)*
  - Lấy $2A - A = 1 - \\frac{1}{2^{100}} \\implies A = 1 - \\frac{1}{2^{100}}$. *(0,35đ)*
  - Vì $\\frac{1}{2^{100}} > 0$ nên $A < 1$ (đpcm). *(0,3đ)*

* **Mã đề 102 ($B < \\frac{1}{2}$):**
  - Ta có: $3B = 1 + \\frac{1}{3} + \\frac{1}{3^2} + \\dots + \\frac{1}{3^{99}}$. *(0,35đ)*
  - Lấy $3B - B = 2B = 1 - \\frac{1}{3^{100}} < 1$. *(0,35đ)*
  - Suy ra $B < \\frac{1}{2}$ (đpcm). *(0,3đ)*

* **Mã đề 103 ($C < \\frac{1}{3}$):**
  - Ta có: $4C = 1 + \\frac{1}{4} + \\frac{1}{4^2} + \\dots + \\frac{1}{4^{99}}$. *(0,35đ)*
  - Lấy $4C - C = 3C = 1 - \\frac{1}{4^{100}} < 1$. *(0,35đ)*
  - Suy ra $C < \\frac{1}{3}$ (đpcm). *(0,3đ)*

* **Mã đề 104 ($D < \\frac{1}{4}$):**
  - Ta có: $5D = 1 + \\frac{1}{5} + \\frac{1}{5^2} + \\dots + \\frac{1}{5^{99}}$. *(0,35đ)*
  - Lấy $5D - D = 4D = 1 - \\frac{1}{5^{100}} < 1$. *(0,35đ)*
  - Suy ra $D < \\frac{1}{4}$ (đpcm). *(0,3đ)*
"""
    with open(os.path.join(work_dir, "DAP_AN_VA_THANG_DIEM.md"), "w", encoding="utf-8") as f:
        f.write(md_content)
    print("Đã tạo file đáp án: DAP_AN_VA_THANG_DIEM.md")

def main():
    work_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(work_dir, "data_de.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(de_data, f, ensure_ascii=False, indent=2)
    print("Đã lưu dữ liệu đề: data_de.json")
    
    tex_path = os.path.join(work_dir, "Phieu_Kiem_Tra_Tuan_07_Buoi_02.tex")
    pdf_path = os.path.join(work_dir, "Phieu_Kiem_Tra_Tuan_07_Buoi_02.pdf")
    
    # Cấu hình dòng kẻ ban đầu
    ob11 = 8
    ob12 = 5
    dk13 = 11
    dk14 = 8
    
    tex_content = build_full_tex(ob11, ob12, dk13, dk14)
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
    print("Đã tạo file TeX ban đầu.")
    
    print("Đang biên dịch PDF lần 1...")
    success = compile_pdf(tex_path, work_dir)
    if not success:
        print("Lỗi biên dịch LaTeX! Đang hiển thị log...")
        log_path = os.path.join(work_dir, "Phieu_Kiem_Tra_Tuan_07_Buoi_02.log")
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8", errors="ignore") as lf:
                lines = lf.readlines()
                for line in lines[-40:]:
                    print(line, end="")
        return
    
    page_count = get_page_count(pdf_path)
    print(f"-> Số trang sau lần biên dịch đầu tiên: {page_count} trang.")
    
    # Tinh chỉnh tự động nếu chưa đạt đúng 8 trang
    # Thử điều chỉnh tham số nếu trang bị tràn hoặc thiếu
    tuning_attempts = [
        (8, 5, 11, 7),
        (8, 5, 10, 7),
        (7, 5, 10, 7),
        (8, 5, 11, 6),
        (9, 5, 11, 7)
    ]
    
    attempt = 0
    while page_count != 8 and attempt < len(tuning_attempts):
        ob11, ob12, dk13, dk14 = tuning_attempts[attempt]
        attempt += 1
        print(f"Thử cấu hình dãn dòng {attempt}: ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}...")
        tex_content = build_full_tex(ob11, ob12, dk13, dk14)
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_content)
        compile_pdf(tex_path, work_dir)
        page_count = get_page_count(pdf_path)
        print(f"-> Kết quả: {page_count} trang.")
    
    if page_count == 8:
        print("==================================================")
        print("CHÚC MỪNG! ĐÃ BIÊN DỊCH THÀNH CÔNG ĐÚNG CHÍNH XÁC 8 TRANG PDF!")
        print("==================================================")
        export_preview_images(pdf_path, work_dir)
        export_answers_md(work_dir)
    else:
        print(f"CẢNH BÁO: Số trang hiện tại là {page_count} (khác 8 trang). Cần kiểm tra lại dãn dòng!")

if __name__ == '__main__':
    main()
