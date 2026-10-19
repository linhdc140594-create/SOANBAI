import os
import subprocess
import pypdf
try:
    import fitz # PyMuPDF
except ImportError:
    fitz = None

TEX_HEADER_TEMPLATE = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=2.6,heightSA=0.62}
\setlength{\parskip}{0pt}

% Dong ke cham mo chuan viet tay
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

% Dinh nghia o bai tap tu luan trong bang
\newcommand{\oBaiTap}[3][6]{%
  \vspace{1.0mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

\begin{document}
\pagestyle{empty}
'''

def render_code_page(title_p1, title_p2, ma_de, q_short, q11, q12, q13, q14, ob11=10, ob12=5, dk13=11, dk14=8):
    """
    Render 2 trang (Trang 1/2 va Trang 2/2) cho mot ma de.
    """
    short_items_tex = ""
    for i, item in enumerate(q_short, 1):
        if isinstance(item, (list, tuple)):
            q_text, ans = item[0], item[1]
            short_items_tex += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q_text} \\shortans{{{ans}}}\\par\\vspace{{0.3mm}}\n"
        elif isinstance(item, dict):
            q_text, ans = item['de'], item['dap_an']
            short_items_tex += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q_text} \\shortans{{{ans}}}\\par\\vspace{{0.3mm}}\n"
        else:
            short_items_tex += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {item}\\par\\vspace{{0.3mm}}\n"

    q13_de = q13.get('de', '')
    q13_a = q13.get('a', '')
    q13_b = q13.get('b', '')
    q14_de = q14.get('de', '')

    res = f'''% =============================================================================
% ========================= MA DE {ma_de} - MAT TRUOC (TRANG 1/2) =============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{title_p1}}} & \\textbf{{Mã đề: {ma_de} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{Điểm số}} & \\centering\\textbf{{Lời nhận xét của thầy cô}} \\tabularnewline
\\rule{{0pt}}{{1.8cm}} & \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

{short_items_tex}
\\vspace{{0.5mm}}
\\noindent\\textbf{{Câu 11 (2,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a)}}{{{q11.get('a', '')}}} & \\oBaiTap[{ob11}]{{b)}}{{{q11.get('b', '')}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c)}}{{{q11.get('c', '')}}} & \\oBaiTap[{ob11}]{{d)}}{{{q11.get('d', '')}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
% =============================================================================
% ========================= MA DE {ma_de} - MAT SAU (TRANG 2/2) ==============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\centering\\textbf{{{title_p2} | Mã đề: {ma_de} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm $x$, biết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12}]{{a)}}{{{q12.get('a', '')}}} & \\oBaiTap[{ob12}]{{b)}}{{{q12.get('b', '')}}} \\\\
\\hline
\\oBaiTap[{ob12}]{{c)}}{{{q12.get('c', '')}}} & \\oBaiTap[{ob12}]{{d)}}{{{q12.get('d', '')}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 13 (2,5 điểm).}} {q13_de}\\par
\\textbf{{a) (1,25 điểm)}} {q13_a}\\par
\\textbf{{b) (1,25 điểm)}} {q13_b}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
\\textbf{{Câu 14 (1,0 điểm).}} {q14_de}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}

\\newpage
'''
    return res

def build_exam_pdf(data_4_codes, title_p1, title_p2, work_dir, base_filename="Phieu_Kiem_Tra", ob11=10, ob12=5, dk13=11, dk14=8):
    """
    Sinh file .tex va bien dich PDF, tu dong kiem tra 8 trang.
    """
    tex_file = os.path.join(work_dir, f"{base_filename}.tex")
    pdf_file = os.path.join(work_dir, f"{base_filename}.pdf")

    # Thu tu ma de mac dinh
    codes = ['101', '102', '103', '104']

    # Vong lap tinh chinh tu dong neu trang bi lech (Auto-tuning)
    for attempt in range(4):
        full_tex = TEX_HEADER_TEMPLATE
        for ma in codes:
            d = data_4_codes[ma]
            full_tex += render_code_page(
                title_p1=title_p1,
                title_p2=title_p2,
                ma_de=ma,
                q_short=d['short'],
                q11=d['q11'],
                q12=d['q12'],
                q13=d['q13'],
                q14=d['q14'],
                ob11=ob11,
                ob12=ob12,
                dk13=dk13,
                dk14=dk14
            )
        full_tex += r'\end{document}' + '\n'

        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(full_tex)

        # Bien dich pdflatex
        cmd = ["pdflatex", "-interaction=nonstopmode", os.path.basename(tex_file)]
        subprocess.run(cmd, cwd=work_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if not os.path.exists(pdf_file):
            return False, "Biên dịch LaTeX thất bại, không tìm thấy file PDF."

        reader = pypdf.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        print(f"[Engine] Lan thu {attempt+1}: {num_pages} trang (Muc tieu: 8 trang) [ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}]")

        if num_pages == 8:
            # Xuat anh xem truoc trang 1 va trang 2
            if fitz:
                doc = fitz.open(pdf_file)
                doc[0].get_pixmap(dpi=150).save(os.path.join(work_dir, 'page_1.png'))
                doc[1].get_pixmap(dpi=150).save(os.path.join(work_dir, 'page_2.png'))
            return True, f"HOAN HAO: PDF dat dung 8 trang chuan [ob11={ob11}, ob12={ob12}, dk13={dk13}, dk14={dk14}]"

        elif num_pages > 8:
            # Tran trang -> giam dong ke
            if ob11 > 8:
                ob11 -= 1
            elif dk13 > 10:
                dk13 -= 1
            elif dk14 > 6:
                dk14 -= 1
            else:
                ob12 -= 1
        else:
            # Hut trang (<8) -> tang dong ke
            if ob11 < 11:
                ob11 += 1
            elif dk13 < 12:
                dk13 += 1
            else:
                dk14 += 1

    return False, f"Chua dat dung 8 trang sau 4 lan vi chinh (hien tai {num_pages} trang)."
