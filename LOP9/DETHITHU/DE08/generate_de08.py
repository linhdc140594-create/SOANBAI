# -*- coding: utf-8 -*-
"""
Script sinh Phiếu Kiểm Tra Đề Thi Thử Vào Lớp 10 THPT (ĐỀ 08).
Gồm 4 mã đề: 101, 102, 103, 104.
Mỗi mã đề đúng 4 mặt A4 (2 tờ in 2 mặt).
Tổng cộng đúng 16 trang PDF.
"""

import os
import json
import subprocess
import pypdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'data_de08.json'), 'r', encoding='utf-8') as f:
    DATA = json.load(f)

TIKZ_FIGURE = r"""\begin{tikzpicture}[line join = round, line cap=round,>=stealth,font=\scriptsize,scale=0.72]
  \def\r{2.2}
  \coordinate (O) at (0,0);
  \coordinate (B) at (-\r,0);
  \coordinate (C) at (\r,0);
  \coordinate (A) at (-0.6,3.6);
  
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \fill (A) circle (1.2pt);
  \fill (B) circle (1.2pt);
  \fill (C) circle (1.2pt);
  
  \node[above] at (A) {$A$};
  \node[below left] at (B) {$B$};
  \node[below right] at (C) {$C$};
  
  % Chừa khoảng không gian bên dưới BC và xung quanh để học sinh tự vẽ hình
  \path (-\r-0.4, -\r-0.2) rectangle (\r+0.4, 3.8);
\end{tikzpicture}"""

def render_latex(config):
    # Dynamic spacing parameters
    vspace_dk1 = config.get('vspace_dk1', '0.8mm')
    ob12_lines = config.get('ob12_lines', 14)
    ob3_lines = config.get('ob3_lines', 12)
    ob4_lines = config.get('ob4_lines', 8)
    ob5_lines = config.get('ob5_lines', 11)
    ob6_lines = config.get('ob6_lines', 32)
    ob7a_lines = config.get('ob7a_lines', 16)
    ob7b_lines = config.get('ob7b_lines', 16)

    preamble = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{tikz}
\usetikzlibrary{angles, quotes, intersections, calc}
\usepackage{xcolor}
\usepackage[top=0.8cm, bottom=0.8cm, left=1.1cm, right=1.1cm]{geometry}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\fboxsep}{3.5pt}
\setlength{\fboxrule}{0.5pt}

% Dòng kẻ chấm mờ cự ly chuẩn viết tay (18.5pt)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{0.6mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!55}\dotfill}\par%
  }%
  \vspace{0.3mm}%
  \endgroup%
}

% Dòng kẻ chia 2 cột có vách ngăn mờ ở giữa
\newcommand{\dongkeHaiCot}[1]{%
  \par\vspace{0.3mm}%
  \arrayrulecolor{gray!40}%
  \begin{tabularx}{\linewidth}{@{}X|X@{}}
    \dongke{#1} & \dongke{#1}
  \end{tabularx}%
  \arrayrulecolor{black}%
}

% Khung bao quanh bài tập tự luận
\newcommand{\khungBaiTap}[1]{%
  \vspace{0.6mm}%
  \noindent\fbox{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \vspace{0.3mm}%
      #1%
      \vspace{0.3mm}%
    }%
  }%
  \vspace{0.5mm}%
}

% Câu trắc nghiệm 4 phương án trên 1 hàng
\newcommand{\cauTN}[6]{%
  \noindent\textbf{Câu #1.} #2\par\vspace{0.1mm}%
  \noindent%
  \makebox[0.25\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.25\linewidth][l]{\textbf{B.} #4}%
  \makebox[0.25\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.25\linewidth][l]{\textbf{D.} #6}\par\vspace{0.6mm}%
}

\begin{document}
\pagestyle{empty}
\fontsize{10.2pt}{13.2pt}\selectfont
"""

    codes_tex = []
    codes = ["101", "102", "103", "104"]

    for code in codes:
        c_data = DATA["codes"][code]
        b6_shared = DATA["b6_shared"]
        b7b_shared = DATA["b7b_shared"]

        # TRANG 1/4: Header + Họ tên/Lớp + Điểm/Nhận xét + 8 câu TN (1 hàng) + Bảng 2 cột (Bài 1 | Bài 2)
        p1 = f"""% =============================================================================
% ========================= MÃ ĐỀ: {code} - TRANG 1/4 =========================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{ĐỀ THI THỬ VÀO LỚP 10 THPT (ĐỀ 08) -- TOÁN 9}} & \\textbf{{Mã đề: {code} -- Trang 1/4}} \\\\
\\textit{{Lớp Toán Thầy Lĩnh -- Thời gian làm bài: 120 phút}} & \\textit{{(Đề gồm 04 trang)}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|p{{3.5cm}}|}}
\\hline
\\rule[-1.5mm]{{0pt}}{{6.8mm}}\\textbf{{Họ và tên học sinh:}} \\dotfill & \\textbf{{Lớp:}} \\makebox[2cm]{{\\dotfill}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.4cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}
\\noindent\\textbf{{\\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,0 điểm)}}
"""
        for i, q in enumerate(c_data["tn"], 1):
            p1 += f"\n\\cauTN{{{i}}}{{{q['cau']}}}{{{q['a']}}}{{{q['b']}}}{{{q['c']}}}{{{q['d']}}}"

        p1 += f"""
\\vspace{{0.4mm}}
\\noindent\\textbf{{\\large PHẦN II. TỰ LUẬN (8,0 điểm)}}
\\vspace{{0.6mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\vspace{{0.3mm}}
\\textbf{{Bài 1 (1,0 điểm).}} Giải hệ phương trình:
\\vspace{{-1.0mm}}
\\[ {c_data['b1']} \\]
\\vspace{{-2.0mm}}
\\noindent\\textit{{Bài giải:}}\\par
\\dongke{{{ob12_lines}}}
&
\\vspace{{0.3mm}}
\\textbf{{Bài 2 (1,0 điểm).}} Rút gọn biểu thức sau:
\\vspace{{-1.0mm}}
\\[ {c_data['b2']} \\]
\\vspace{{-2.0mm}}
\\noindent\\textit{{Bài giải:}}\\par
\\dongke{{{ob12_lines}}}
\\\\ \\hline
\\end{{tabularx}}

\\newpage
"""

        # TRANG 2/4: Bài 3 + Bài 4 + Bài 5 (đều chia 2 cột, tăng số dòng cho Bài 3)
        p2 = f"""% =============================================================================
% ========================= MÃ ĐỀ: {code} - TRANG 2/4 =========================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{ĐỀ THI THỬ VÀO LỚP 10 THPT (ĐỀ 08) -- TOÁN 9}} & \\textbf{{Mã đề: {code} -- Trang 2/4}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{0.6mm}}

\\khungBaiTap{{%
  \\textbf{{Bài 3 (1,0 điểm).}} Cho phương trình ${c_data['b3']}$, không giải phương trình, hãy tính giá trị của biểu thức: ${c_data['b3_expr']}$%
  \\par\\vspace{{0.3mm}}%
  \\noindent\\textit{{Bài giải:}}\\par%
  \\dongkeHaiCot{{{ob3_lines}}}%
}}

\\vspace{{0.6mm}}

\\khungBaiTap{{%
  \\textbf{{Bài 4 (1,0 điểm).}} Bạn {c_data['b4_name']} chơi trò chơi gieo đồng thời hai con xúc xắc cân đối đồng chất I và II. Tính xác suất của biến cố: \\textit{{“{c_data['b4_event']}”}}.%
  \\par\\vspace{{0.3mm}}%
  \\noindent\\textit{{Bài giải:}}\\par%
  \\dongkeHaiCot{{{ob4_lines}}}%
}}

\\vspace{{0.6mm}}

\\khungBaiTap{{%
  \\textbf{{Bài 5 (1,0 điểm).}} {c_data['b5_text']}%
  \\par\\vspace{{0.3mm}}%
  \\noindent\\textit{{Bài giải:}}\\par%
  \\dongkeHaiCot{{{ob5_lines}}}%
}}

\\newpage
"""

        # TRANG 3/4: Bài 6 Hình học (Minipage trái đề, Minipage phải TikZ tam giác ABC + dòng kẻ chia 2 cột)
        p3 = f"""% =============================================================================
% ========================= MÃ ĐỀ: {code} - TRANG 3/4 =========================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{ĐỀ THI THỬ VÀO LỚP 10 THPT (ĐỀ 08) -- TOÁN 9}} & \\textbf{{Mã đề: {code} -- Trang 3/4}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{0.6mm}}

\\khungBaiTap{{%
  \\noindent
  \\begin{{minipage}}[t]{{0.58\\linewidth}}
    \\vspace{{0pt}}%
    \\textbf{{Bài 6 (2,0 điểm).}} {b6_shared['de']}\\par\\vspace{{0.8mm}}
    \\textbf{{a) (1,0 điểm)}} {b6_shared['cau_a']}\\par\\vspace{{0.6mm}}
    \\textbf{{b) (1,0 điểm)}} {b6_shared['cau_b']}
  \\end{{minipage}}\\hfill
  \\begin{{minipage}}[t]{{0.40\\linewidth}}
    \\vspace{{0pt}}%
    \\centering
    {TIKZ_FIGURE}
  \\end{{minipage}}
  \\par\\vspace{{0.6mm}}%
  \\noindent\\textit{{Bài giải:}}\\par\\vspace{{0.3mm}}%
  \\arrayrulecolor{{gray!40}}%
  \\begin{{tabularx}}{{\\linewidth}}{{@{{}}X|X@{{}}}}
    \\dongke{{{ob6_lines}}} & \\dongke{{{ob6_lines}}}
  \\end{{tabularx}}%
  \\arrayrulecolor{{black}}%
}}

\\newpage
"""

        # TRANG 4/4: Bài 7a + Bài 7b (chia 2 cột)
        p4 = f"""% =============================================================================
% ========================= MÃ ĐỀ: {code} - TRANG 4/4 =========================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{ĐỀ THI THỬ VÀO LỚP 10 THPT (ĐỀ 08) -- TOÁN 9}} & \\textbf{{Mã đề: {code} -- Trang 4/4}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.5mm}}

\\khungBaiTap{{%
  \\textbf{{Bài 7a (0,5 điểm).}} Một xí nghiệp sản xuất {c_data['b7a_sp1']} sản phẩm loại I và {c_data['b7a_sp2']} sản phẩm loại II trong thời gian {c_data['b7a_time']} giờ. Mỗi giờ sản xuất được số sản phẩm loại I nhiều hơn số sản phẩm loại II là {c_data['b7a_diff']} sản phẩm. Hỏi mỗi giờ xí nghiệp sản xuất được bao nhiêu sản phẩm mỗi loại?%
  \\par\\vspace{{0.4mm}}%
  \\noindent\\textit{{Bài giải:}}\\par%
  \\dongkeHaiCot{{{ob7a_lines}}}%
}}

\\vspace{{1.5mm}}

\\khungBaiTap{{%
  \\textbf{{Bài 7b (0,5 điểm).}} {b7b_shared['de']}%
  \\par\\vspace{{0.4mm}}%
  \\noindent\\textit{{Bài giải:}}\\par%
  \\dongkeHaiCot{{{ob7b_lines}}}%
}}

\\vspace{{1.5mm}}
\\noindent\\textit{{(Ghi chú: Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.)}}

\\newpage
"""
        codes_tex.append(p1 + p2 + p3 + p4)

    footer = "\\end{document}\n"
    return preamble + "\n".join(codes_tex) + footer

def compile_tex(tex_path):
    cmd = ["pdflatex", "-interaction=nonstopmode", os.path.basename(tex_path)]
    work_dir = os.path.dirname(tex_path)
    res = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
    return res.returncode == 0

def check_pages_and_margins(pdf_path):
    import fitz
    import numpy as np
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    margins = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
        gray = np.mean(img, axis=2) if pix.n >= 3 else img[:,:,0]
        non_white = np.where(gray < 250)
        if len(non_white[0]) > 0:
            last_y = np.max(non_white[0])
            margin_mm = ((pix.h - last_y) / 150.0) * 25.4
            margins.append(margin_mm)
        else:
            margins.append(0.0)
    doc.close()
    return total_pages, margins

def main():
    tex_filename = "Phieu_Kiem_Tra_De_08.tex"
    pdf_filename = "Phieu_Kiem_Tra_De_08.pdf"
    tex_path = os.path.join(BASE_DIR, tex_filename)
    pdf_path = os.path.join(BASE_DIR, pdf_filename)

    # Analytically tuned configuration
    config = {
        'ob12_lines': 14,
        'ob3_lines': 12,
        'ob4_lines': 8,
        'ob5_lines': 11,
        'ob6_lines': 32,
        'ob7a_lines': 17,
        'ob7b_lines': 16
    }

    tex_content = render_latex(config)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print("Wrote tuned TeX to:", tex_path)

    success = compile_tex(tex_path)
    if not success:
        print("Compilation failed! Check log.")
        return

    pages, margins = check_pages_and_margins(pdf_path)
    print(f"Total Pages: {pages}")
    for idx, m in enumerate(margins):
        code = 101 + (idx // 4)
        p_in_code = (idx % 4) + 1
        print(f"Page {idx+1:02d} (Mã {code} - P{p_in_code}/4): bottom margin = {m:.2f} mm")

    # Render preview pngs for Mã 101 (Pages 1 to 4)
    import fitz
    doc = fitz.open(pdf_path)
    for p_no in range(4):
        pix = doc[p_no].get_pixmap(dpi=150)
        out_img = os.path.join(BASE_DIR, f"page_{p_no+1}.png")
        pix.save(out_img)
        print(f"Rendered {out_img}")

if __name__ == '__main__':
    main()
