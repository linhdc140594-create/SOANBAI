# -*- coding: utf-8 -*-
"""
Module dùng chung cho việc render LaTeX và Markdown đáp án cho Phiếu Bài Tập Tuần Toán Lớp 5 (Thầy Lĩnh).
Đảm bảo chuẩn bố cục:
- Trang 1: Bảng thông tin + Điểm + Bảng 12 đáp án TN + 12 câu Trắc nghiệm + Bài 1 Tự luận (Đặt tính 4 ý).
- Trang 2: Bài 2 (Tìm x 4 ý) + Bài 3 (Đổi đơn vị 4 ý) + Bài 4 (Toán giải - 11 dòng kẻ) + Bài 5 (Toán nâng cao - 8 dòng kẻ).
- Mỗi mã đề đúng 2 trang A4 in 2 mặt (7 mã đề = 14 trang).
"""

import os
import re
import subprocess
import pypdf

ANSWER_TABLE = r"""\begin{tabularx}{\linewidth}{|c|*{12}{>{\centering\arraybackslash}X|}}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Đáp án} & & & & & & & & & & & & \\
\hline
\end{tabularx}"""

def fix_latex_math(text: str) -> str:
    """Sửa lỗi dấu phẩy thập phân, dấu phần trăm và format đơn vị trong LaTeX."""
    if not text:
        return ""
    # Sửa lỗi \\% thành \%
    text = text.replace(r"\\%", r"\%")
    # Chuyển đổi dấu phẩy trong số thập phân thành {,}
    text = re.sub(r'(\d+),(\d+)', r'\1{,}\2', text)
    # Thoát dấu % nếu chưa thoát (tránh biến thành comment trong LaTeX)
    text = re.sub(r'(?<!\\)%', r'\%', text)
    # Đơn vị diện tích và thể tích chuẩn math mode (thay thế đơn vị dài trước)
    for u in ['km', 'dm', 'cm', 'mm', 'm']:
        text = text.replace(f"{u}²", f"$\\text{{{u}}}^2$")
        text = text.replace(f"{u}³", f"$\\text{{{u}}}^3$")
    # Nếu còn ký tự ² hoặc ³ riêng lẻ
    text = text.replace("²", "$^2$").replace("³", "$^3$")
    # Sửa chỉ số dưới có chữ tiếng Việt trong math mode: S_{vuông} -> S_{\text{vuông}}
    text = re.sub(r'_\{([a-zA-Z\u00C0-\u1EF9]+)\}', lambda m: f"_{{\\text{{{m.group(1)}}}}}" if not m.group(1).startswith(r'\text') else m.group(0), text)
    return text

def render_tex(week_num: int, week_title: str, ma_de_list: list, grade: int = 5) -> str:
    week_str = f"TUẦN {week_num:02d}"
    grade_str = f"LỚP {grade}"

    header = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{enumerate}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.45cm, bottom=0.45cm, left=0.8cm, right=0.8cm]{geometry}
\DeclareUnicodeCharacter{00B2}{\ensuremath{^2}}
\DeclareUnicodeCharacter{00B3}{\ensuremath{^3}}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\fboxsep}{3.5pt}
\setlength{\fboxrule}{0.5pt}

% Dòng kẻ chấm mờ cự ly chuẩn viết tay tiểu học (18pt)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18pt%
  \vspace{0.4mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!55}\dotfill}\par%
  }%
  \vspace{0.2mm}%
  \endgroup%
}

% Khung bao quanh bài tập tự luận
\newcommand{\khungBaiTap}[1]{%
  \vspace{0.8mm}%
  \noindent\fbox{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \vspace{0.3mm}%
      #1%
      \vspace{0.3mm}%
    }%
  }%
  \vspace{0.5mm}%
}

% Ô bài tập đặt tính
\newcommand{\oDatTinh}[3][4]{%
  \vspace{0.3mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

% Câu trắc nghiệm dàn 4 đáp án trên 1 hàng ngang
\newcommand{\cauTN}[6]{%
  \noindent\textbf{Câu #1.} #2\par\vspace{0.1mm}%
  \noindent%
  \makebox[0.25\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.25\linewidth][l]{\textbf{B.} #4}%
  \makebox[0.25\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.25\linewidth][l]{\textbf{D.} #6}\par\vspace{0.6mm}%
}

% Câu trắc nghiệm dàn 2 đáp án / hàng
\newcommand{\cauTNhaiDong}[6]{%
  \noindent\textbf{Câu #1.} #2\par\vspace{0.1mm}%
  \noindent%
  \makebox[0.5\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.5\linewidth][l]{\textbf{B.} #4}\par\vspace{0.1mm}%
  \noindent%
  \makebox[0.5\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.5\linewidth][l]{\textbf{D.} #6}\par\vspace{0.6mm}%
}

\begin{document}
\pagestyle{empty}
\fontsize{10.2pt}{13.2pt}\selectfont
"""

    pages = []
    for item in ma_de_list:
        md = item["ma_de"]
        tn = item["tn"]
        b1 = item["bai1"]
        b2 = item["bai2"]
        b3 = item["bai3"]
        b4 = item["bai4"]
        b5 = item["bai5"]

        # Chuẩn hóa đề bài 4 và bài 5
        b4_de = fix_latex_math(b4.get("de", ""))
        b5_raw = b5.get("bieuthuc", "").strip()

        # Format bài 5
        geom_kw = ["tam giác", "hình thang", "hình tròn", "vành khuyên", "Một hình", "Cho hình", "Hình vuông"]
        is_word_prob = any(kw.lower() in b5_raw.lower() for kw in geom_kw)

        if is_word_prob:
            b5_render = fix_latex_math(b5_raw)
        else:
            prefix = "Tính nhanh:" if "Tính nhanh" in b5_raw else "Tính bằng cách thuận tiện nhất:"
            clean_expr = b5_raw
            for p in ["Tính bằng cách thuận tiện nhất:", "Tính thuận tiện:", "Tính nhanh:"]:
                clean_expr = clean_expr.replace(p, "")
            clean_expr = clean_expr.replace("$", "").strip()
            clean_expr = fix_latex_math(clean_expr)
            b5_render = f"{prefix}\\par\\vspace{{0.6mm}}\\centerline{{${clean_expr}$}}"

        # Trang 1: Mặt trước
        p1 = f"""% =============================================================================
% ========================= MÃ ĐỀ: {md} ========================================
% =============================================================================

% -------------------- TRANG 1: MẶT TRƯỚC --------------------
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU BÀI TẬP CUỐI TUẦN -- TOÁN {grade_str} ({week_str})}} & \\textbf{{MÃ ĐỀ: {md}}} \\\\
\\textit{{Trung tâm Toán Thầy Lĩnh -- Năm học: 2026 - 2027}} & \\textit{{Thời gian: 45 phút}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|p{{3.5cm}}|}}
\\hline
\\rule[-2mm]{{0pt}}{{7.5mm}}\\textbf{{Họ và tên:}} \\dotfill & \\textbf{{Lớp:}} \\makebox[2cm]{{\\dotfill}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.1cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent\\textbf{{BẢNG ĐIỀN ĐÁP ÁN TRẮC NGHIỆM (Mỗi câu đúng 0,25 điểm):}}
\\vspace{{0.6mm}}

{ANSWER_TABLE}

\\vspace{{1.2mm}}

\\noindent\\textbf{{\\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (3,0 điểm)}}
"""
        # 12 câu trắc nghiệm
        for i, (q, a, b, c, d, ans) in enumerate(tn, 1):
            q_fix = fix_latex_math(q)
            a_fix = fix_latex_math(a)
            b_fix = fix_latex_math(b)
            c_fix = fix_latex_math(c)
            d_fix = fix_latex_math(d)
            if i in [11, 12]:
                p1 += f"\n\\cauTNhaiDong{{{i}}}{{{q_fix}}}{{{a_fix}}}{{{b_fix}}}{{{c_fix}}}{{{d_fix}}}"
            else:
                p1 += f"\n\\cauTN{{{i}}}{{{q_fix}}}{{{a_fix}}}{{{b_fix}}}{{{c_fix}}}{{{d_fix}}}"

        # BÀI 1: ĐẶT TÍNH RỒI TÍNH (4 Ý) - TRANG 1
        def fmt_b1(val):
            val = val.strip()
            return val if val.startswith("$") else f"${val}$"

        p1 += f"""

\\vspace{{0.4mm}}
\\noindent\\textbf{{\\large PHẦN II. TỰ LUẬN (7,0 điểm)}}

\\noindent\\textbf{{Bài 1 (2,0 điểm). Đặt tính rồi tính:}}
\\vspace{{0.4mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|X|X|}}
\\hline
\\oDatTinh[4]{{a)}}{{{fmt_b1(b1[0])}}} & 
\\oDatTinh[4]{{b)}}{{{fmt_b1(b1[1])}}} & 
\\oDatTinh[4]{{c)}}{{{fmt_b1(b1[2])}}} & 
\\oDatTinh[4]{{d)}}{{{fmt_b1(b1[3])}}} \\tabularnewline
\\hline
\\end{{tabularx}}

\\newpage
"""

        # Trang 2: Tự luận (tiếp theo)
        p2 = f"""% -------------------- TRANG 2: MẶT SAU --------------------
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHẦN TỰ LUẬN (TIẾP THEO) -- PHIẾU BÀI TẬP {week_str}}} & \\textbf{{MÃ ĐỀ: {md}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{0.8mm}}

% BÀI 2: TÌM X (4 Ý)
\\khungBaiTap{{%
  \\textbf{{Bài 2 (1,5 điểm). Tìm $x$:}}\\par\\vspace{{0.6mm}}
  \\noindent
  \\begin{{minipage}}[t]{{0.485\\linewidth}}
    \\textbf{{a)}} ${b2[0][0]}$\\par
    \\dongke{{3}}
    \\vspace{{0.4mm}}
    \\textbf{{c)}} ${b2[2][0]}$\\par
    \\dongke{{3}}
  \\end{{minipage}}\\hfill
  \\begin{{minipage}}[t]{{0.485\\linewidth}}
    \\textbf{{b)}} ${b2[1][0]}$\\par
    \\dongke{{3}}
    \\vspace{{0.4mm}}
    \\textbf{{d)}} ${b2[3][0]}$\\par
    \\dongke{{3}}
  \\end{{minipage}}
}}

\\vspace{{0.8mm}}

% BÀI 3: ĐỔI ĐƠN VỊ (4 Ý - 1 CỘT TỪ TRÊN XUỐNG)
\\khungBaiTap{{%
  \\textbf{{Bài 3 (1,0 điểm). Viết số thích hợp vào chỗ chấm:}}\\par\\vspace{{0.8mm}}
  \\noindent
  a) ${b3[0][0]} = \\dotfill\\,{b3[0][1]}$\\par\\vspace{{1.4mm}}
  \\noindent
  b) ${b3[1][0]} = \\dotfill\\,{b3[1][1]}$\\par\\vspace{{1.4mm}}
  \\noindent
  c) ${b3[2][0]} = \\dotfill\\,{b3[2][1]}$\\par\\vspace{{1.4mm}}
  \\noindent
  d) ${b3[3][0]} = \\dotfill\\,{b3[3][1]}$\\par
}}

\\vspace{{0.8mm}}

% BÀI 4: BÀI TOÁN GIẢI (11 DÒNG KẺ)
\\khungBaiTap{{%
  \\textbf{{Bài 4 (1,5 điểm).}} {b4_de}
  \\par\\vspace{{0.3mm}}%
  \\noindent\\textit{{Bài giải:}}
  \\dongke{{11}}
}}

\\vspace{{0.8mm}}

% BÀI 5: TOÁN NÂNG CAO (8 DÒNG KẺ)
\\khungBaiTap{{%
  \\textbf{{Bài 5 (1,0 điểm).}} {b5_render}
  \\par\\vspace{{0.3mm}}%
  \\noindent\\textit{{Bài làm:}}
  \\dongke{{8}}
}}

\\newpage
"""
        pages.append(p1 + p2)

    footer = "\\end{document}\n"
    full_tex = header + "\n".join(pages) + footer
    return full_tex

def render_markdown_answers(week_num: int, week_title: str, topics: list, ma_de_list: list, grade: int = 5) -> str:
    week_str = f"TUẦN {week_num:02d}"
    grade_str = f"TOÁN LỚP {grade}"

    md = "# BẢNG ĐÁP ÁN & BAREM THANG ĐIỂM CHI TIẾT\n"
    md += f"## PHIẾU BÀI TẬP CUỐI TUẦN -- {grade_str} ({week_str})\n"
    md += f"### Chủ đề: {week_title}\n"
    md += "### Bộ 7 Mã Đề: 501 -- 502 -- 503 -- 504 -- 505 -- 506 -- 507 (Lớp Toán Thầy Lĩnh)\n\n"
    md += "---\n\n"
    md += "## I. BẢNG ĐÁP ÁN TRẮC NGHIỆM (3,0 ĐIỂM -- 0,25 ĐIỂM/CÂU)\n\n"

    # Header table
    md += "| Câu | " + " | ".join([f"Mã {item['ma_de']}" for item in ma_de_list]) + " | Nội dung kiến thức |\n"
    md += "| :-: | " + " | ".join([":-:" for _ in ma_de_list]) + " | :--- |\n"

    for c in range(12):
        row = f"| **{c+1}** | "
        ans_cols = []
        for item in ma_de_list:
            ans_cols.append(f"**{item['tn'][c][5]}**")
        topic_name = topics[c] if c < len(topics) else "Kiến thức trọng tâm"
        row += " | ".join(ans_cols) + f" | {topic_name} |\n"
        md += row

    md += "\n---\n\n"
    md += "## II. BAREM ĐIỂM TỰ LUẬN (7,0 ĐIỂM)\n\n"

    for item in ma_de_list:
        code = item["ma_de"]
        md += f"### 📌 MÃ ĐỀ: {code}\n\n"

        # Bài 1
        md += "**Bài 1 (2,0 điểm - 0,5 điểm/ý): Đặt tính rồi tính**\n"
        b1 = item["bai1"]
        ans1 = item["bai1_ans"]
        for idx_l, letter in enumerate(['a', 'b', 'c', 'd']):
            clean_b1 = b1[idx_l].replace("$", "").strip()
            clean_ans = ans1[idx_l].replace("$", "").strip()
            pts = "0,5đ"
            md += f"- {letter}) ${clean_b1} = \\mathbf{{{clean_ans}}}$ *({pts})*\n"
        md += "\n"

        # Bài 2
        md += "**Bài 2 (1,5 điểm): Tìm $x$**\n"
        b2 = item["bai2"]
        md += f"- a) ${b2[0][0]} \\implies {b2[0][1]} \\implies \\mathbf{{{b2[0][2]}}}$ *(0,4đ)*\n"
        md += f"- b) ${b2[1][0]} \\implies {b2[1][1]} \\implies \\mathbf{{{b2[1][2]}}}$ *(0,4đ)*\n"
        md += f"- c) ${b2[2][0]} \\implies {b2[2][1]} \\implies \\mathbf{{{b2[2][2]}}}$ *(0,35đ)*\n"
        md += f"- d) ${b2[3][0]} \\implies {b2[3][1]} \\implies \\mathbf{{{b2[3][2]}}}$ *(0,35đ)*\n\n"

        # Bài 3
        md += "**Bài 3 (1,0 điểm - 0,25 điểm/ý): Điền số thích hợp vào chỗ chấm**\n"
        b3 = item["bai3"]
        md += f"- a) ${b3[0][0]} = \\mathbf{{{b3[0][2]}}}\\,{b3[0][1]}$ *(0,25đ)*\n"
        md += f"- b) ${b3[1][0]} = \\mathbf{{{b3[1][2]}}}\\,{b3[1][1]}$ *(0,25đ)*\n"
        md += f"- c) ${b3[2][0]} = \\mathbf{{{b3[2][2]}}}\\,{b3[2][1]}$ *(0,25đ)*\n"
        md += f"- d) ${b3[3][0]} = \\mathbf{{{b3[3][2]}}}\\,{b3[3][1]}$ *(0,25đ)*\n\n"

        # Bài 4
        md += "**Bài 4 (1,5 điểm): Bài toán giải có lời văn (Chương trình Lớp 5)**\n"
        b4 = item["bai4"]
        md += f"- *Đề bài:* {b4['de']}\n"
        md += f"- *Lời giải chi tiết:*\n"
        for k in sorted(b4.keys()):
            if k != "de":
                md += f"  - {b4[k]}\n"
        md += "\n"

        # Bài 5
        md += "**Bài 5 (1,0 điểm): Bài toán nâng cao (Chương trình Lớp 5)**\n"
        b5 = item["bai5"]
        md += f"- *Đề bài:* {b5.get('bieuthuc', '')}\n"
        if "buoc1" in b5:
            md += f"  - Bước 1: {b5['buoc1']}\n"
        if "buoc2" in b5:
            md += f"  - Bước 2: {b5['buoc2']}\n"
        if "ans" in b5:
            md += f"  - Đáp số / Kết luận: {b5['ans']}\n"
        md += "\n---\n\n"

    return md

def compile_and_verify(week_num: int, base_dir: str):
    week_str = f"TUAN_{week_num:02d}"
    out_dir = os.path.join(base_dir, week_str)
    tex_filename = f"Phieu_Bai_Tap_Tuan_{week_num:02d}_Toan5.tex"
    pdf_filename = f"Phieu_Bai_Tap_Tuan_{week_num:02d}_Toan5.pdf"
    
    tex_path = os.path.join(out_dir, tex_filename)
    pdf_path = os.path.join(out_dir, pdf_filename)
    
    cmd = ["pdflatex", "-interaction=nonstopmode", tex_filename]
    res = subprocess.run(cmd, cwd=out_dir, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR compiling {week_str}: returncode {res.returncode}")
        log_lines = res.stdout.splitlines()[-35:]
        print("\n".join(log_lines))
        return False
        
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"SUCCESS: {week_str} compiled -> {pdf_filename} with {total_pages} pages.")
    assert total_pages == 14, f"Page count mismatch in {week_str}: expected 14, got {total_pages}"
    return True
