import os
import sys
import json
import subprocess
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_14'
json_path = os.path.join(work_dir, 'de_14.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# 1. HÀM TẠO FILE TEX CHO ĐỀ THI (De_14_DeThi.tex)
# =============================================================================
def generate_dethi_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage[top=0.8cm, bottom=0.8cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage[dethi]{ex_test}
\SAOPTN{widthSA=2.6,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Môn Toán 7 -- Đề số 14}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

% --- KHUNG TIÊU ĐỀ ĐỀ THI ---
\noindent
\begin{tabularx}{\linewidth}{X r}
\textbf{TRƯỜNG THCS: \dotfill} & \textbf{ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I} \\
\textbf{Họ và tên: \dotfill} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{Lớp: \dotfill \quad SBD: \dotfill} & \textbf{Môn: TOÁN 7} \\
& \textit{Thời gian làm bài: 90 phút (không kể thời gian phát đề)}
\end{tabularx}

\vspace{1mm}
\noindent
\begin{tabularx}{\linewidth}{|p{3.5cm}|X|}
\hline
\centering\textbf{Điểm số} & \centering\textbf{Lời nhận xét của thầy cô giáo} \tabularnewline
\rule{0pt}{0.8cm} & \\
\hline
\end{tabularx}

\vspace{1.5mm}
\begin{center}
\textbf{\large ĐỀ SỐ 14}
\end{center}
'''

    # PHẦN I
    body = r'''
\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)}

\textit{Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi chỉ chọn một phương án đúng nhất và ghi vào bảng đáp án.}

\vspace{1mm}
'''
    for q in d['phan_I_trac_nghiem']:
        noi_dung = q['noi_dung']
        opts = q['lua_chon']
        da = q.get('dap_an', '').strip().upper()
        hinh = q.get('hinh_tikz')

        def clean_opt(val):
            val = val.strip()
            if not val.endswith('$') and val.endswith('.'):
                val = val[:-1].strip()
            return val

        a_txt = ("\\True " if da == 'A' else "") + clean_opt(opts.get('A', ''))
        b_txt = ("\\True " if da == 'B' else "") + clean_opt(opts.get('B', ''))
        c_txt = ("\\True " if da == 'C' else "") + clean_opt(opts.get('C', ''))
        d_txt = ("\\True " if da == 'D' else "") + clean_opt(opts.get('D', ''))

        choice_code = f"\\choice\n{{{a_txt}}}\n{{{b_txt}}}\n{{{c_txt}}}\n{{{d_txt}}}"

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_code}\n}}{{\n{hinh}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n\\end{{ex}}\n\n"

        if q['cau'] == 8:
            body += "\\newpage\n"

    # Bảng đáp án trắc nghiệm Phần I
    body += r'''
\vspace{1mm}
\noindent\textbf{BẢNG TRẢ LỜI TRẮC NGHIỆM PHẦN I:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Chọn} & \rule{0pt}{0.48cm} & & & & & & & & & & & \\
\hline
\end{tabular}
\end{center}
\vspace{1mm}
'''

    # PHẦN II (Đúng / Sai) -> Reset counter ex
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI (2,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}

\vspace{1mm}
'''
    for q in d['phan_II_dung_sai']:
        noi_dung = q['noi_dung']
        hinh = q.get('hinh_tikz')
        mds = q['menh_de']

        tf_items = []
        for md in mds:
            is_true = "đúng" in md.get('dap_an', '').lower()
            prefix = "\\True " if is_true else ""
            txt = md['noi_dung'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
        
        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_tf_code}\n}}{{\n{hinh}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\end{{ex}}\n\n"

    # Bảng điền đáp án Đúng/Sai
    body += r'''
\noindent\textbf{BẢNG TRẢ LỜI PHẦN II:}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu 1} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} & \textbf{Câu 2} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\
\hline
\textbf{Đ/S} & \rule{0pt}{0.45cm} & & & & \textbf{Đ/S} & & & & \\
\hline
\end{tabular}
\end{center}
\vspace{1mm}
'''

    # PHẦN III (Trả lời ngắn) -> Reset counter ex
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN (1,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Điền kết quả vào ô trống.}

\vspace{1mm}
'''
    for q in d['phan_III_tra_loi_ngan']:
        noi_dung = q['noi_dung']
        da = q['dap_an'].strip()
        da_box = da if (da.startswith('$') or not any(c in da for c in ['^', '\\', '_'])) else f"${da}$"
        hinh = q.get('hinh_tikz')
        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n\\vspace{{1mm}}\n\\hfill\\shortans{{{da_box}}}\n}}{{\n{hinh}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da_box}}}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận) -> Reset counter ex
    body += r'''
\newpage
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (4,0 điểm)}

\textit{Thí sinh trình bày chi tiết lời giải vào giấy làm bài.}

\vspace{1mm}
'''
    for q in d['phan_IV_tu_luan']:
        noi_dung = q['noi_dung']
        hinh = q.get('hinh_tikz')

        body += f"\\begin{{ex}}\n"
        if hinh:
            sub_q = ""
            if q.get('cac_y'):
                sub_q += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('cau_hoi', '')
                    sub_q += f"\\item {content}\n"
                sub_q += "\\end{enumerate}\n"
            body += f"\\immini{{\n{noi_dung}\n{sub_q}}}{{\n{hinh}\n}}\n"
        else:
            body += f"{noi_dung}\n"
            if q.get('cac_y'):
                sub_q = "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('cau_hoi', '')
                    sub_q += f"\\item {content}\n"
                sub_q += "\\end{enumerate}\n"
                body += sub_q
        body += "\\end{ex}\n\\vspace{2mm}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# =============================================================================
# 2. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_14_DapAn.tex)
# =============================================================================
def generate_dapan_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage[top=1.0cm, bottom=1.0cm, left=1.3cm, right=1.3cm]{geometry}
\usepackage[loigiai]{ex_test}
\SAOPTN{widthSA=2.6,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{1pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Lời giải chi tiết -- Đề số 14}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I -- Toán 7}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\Large HƯỚNG DẪN CHẤM VÀ LỜI GIẢI CHI TIẾT}\\
\vspace{1mm}
\textbf{\large MÔN: TOÁN 7 -- ĐỀ SỐ 14}
\end{center}
\vspace{2mm}
'''

    # PHẦN I
    body = r'''
\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN}

\vspace{1mm}
'''
    for q in d['phan_I_trac_nghiem']:
        noi_dung = q['noi_dung']
        opts = q['lua_chon']
        da = q.get('dap_an', '').strip().upper()
        hinh = q.get('hinh_tikz')
        lg = q.get('loi_giai', '').strip()

        def clean_opt(val):
            val = val.strip()
            if not val.endswith('$') and val.endswith('.'):
                val = val[:-1].strip()
            return val

        a_txt = ("\\True " if da == 'A' else "") + clean_opt(opts.get('A', ''))
        b_txt = ("\\True " if da == 'B' else "") + clean_opt(opts.get('B', ''))
        c_txt = ("\\True " if da == 'C' else "") + clean_opt(opts.get('C', ''))
        d_txt = ("\\True " if da == 'D' else "") + clean_opt(opts.get('D', ''))

        choice_code = f"\\choice\n{{{a_txt}}}\n{{{b_txt}}}\n{{{c_txt}}}\n{{{d_txt}}}"

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_code}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"

    # PHẦN II
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI}

\vspace{1mm}
'''
    for q in d['phan_II_dung_sai']:
        noi_dung = q['noi_dung']
        hinh = q.get('hinh_tikz')
        mds = q['menh_de']

        tf_items = []
        lg_items = []
        for md in mds:
            is_true = "đúng" in md.get('dap_an', '').lower()
            prefix = "\\True " if is_true else ""
            txt = md['noi_dung'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
            y_label = md['y'] + ")"
            lg_items.append(f"\\item \\textbf{{{y_label}}} \\textbf{{{md['dap_an']}}}. {md['loi_giai']}")

        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)
        lg_full = "\\begin{itemize}[leftmargin=0.6cm, itemsep=1pt]\n" + "\n".join(lg_items) + "\n\\end{itemize}"

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_tf_code}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{lg_full}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\loigiai{{\n{lg_full}\n}}\n\\end{{ex}}\n\n"

    # PHẦN III
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN}

\vspace{1mm}
'''
    for q in d['phan_III_tra_loi_ngan']:
        noi_dung = q['noi_dung']
        da = q['dap_an'].strip()
        da_box = da if (da.startswith('$') or not any(c in da for c in ['^', '\\', '_'])) else f"${da}$"
        hinh = q.get('hinh_tikz')
        lg = q.get('loi_giai', '').strip()
        lg_content = f"{lg}\n\n\\textbf{{Đáp số:}} {da_box}"

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n\\vspace{{1mm}}\n\\hfill\\shortans{{{da_box}}}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{lg_content}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da_box}}}\n\\loigiai{{\n{lg_content}\n}}\n\\end{{ex}}\n\n"

    # PHẦN IV
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN}

\vspace{1mm}
'''
    for q in d['phan_IV_tu_luan']:
        noi_dung = q['noi_dung']
        hinh = q.get('hinh_tikz')

        lg_parts = []
        if q.get('cac_y'):
            for y_item in q['cac_y']:
                y_label = y_item.get('y', '')
                y_lg = y_item.get('loi_giai', '')
                lg_parts.append(f"\\textbf{{{y_label})}} {y_lg}")
            full_lg = "\n\n".join(lg_parts)
        else:
            full_lg = q.get('loi_giai', '')

        body += f"\\begin{{ex}}\n"
        if hinh:
            sub_q = ""
            if q.get('cac_y'):
                sub_q += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('cau_hoi', '')
                    sub_q += f"\\item {content}\n"
                sub_q += "\\end{enumerate}\n"
            body += f"\\immini{{\n{noi_dung}\n{sub_q}}}{{\n{hinh}\n}}\n\\loigiai{{\n{full_lg}\n}}\n"
        else:
            body += f"{noi_dung}\n"
            if q.get('cac_y'):
                sub_q = "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('cau_hoi', '')
                    sub_q += f"\\item {content}\n"
                sub_q += "\\end{enumerate}\n"
                body += sub_q
            body += f"\\loigiai{{\n{full_lg}\n}}\n"
        body += "\\end{ex}\n\\vspace{2mm}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# =============================================================================
# THỰC THI XUẤT VÀ BIÊN DỊCH
# =============================================================================
dethi_tex = generate_dethi_tex(d)
dethi_tex_path = os.path.join(work_dir, 'De_14_DeThi.tex')
with open(dethi_tex_path, 'w', encoding='utf-8') as f:
    f.write(dethi_tex)
print("Writing De_14_DeThi.tex...")

dapan_tex = generate_dapan_tex(d)
dapan_tex_path = os.path.join(work_dir, 'De_14_DapAn.tex')
with open(dapan_tex_path, 'w', encoding='utf-8') as f:
    f.write(dapan_tex)
print("Writing De_14_DapAn.tex...")

print("Compiling De_14_DeThi.pdf with pdflatex...")
res1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_14_DeThi.tex'], cwd=work_dir, capture_output=True)
print(f"DeThi compile returncode: {res1.returncode}")

print("Compiling De_14_DapAn.pdf with pdflatex...")
res2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_14_DapAn.tex'], cwd=work_dir, capture_output=True)
print(f"DapAn compile returncode: {res2.returncode}")

if res1.returncode == 0:
    doc1 = pymupdf.open(os.path.join(work_dir, 'De_14_DeThi.pdf'))
    print(f"De_14_DeThi.pdf has {len(doc1)} pages.")
    for i, page in enumerate(doc1):
        pix = page.get_pixmap(dpi=150)
        pix.save(os.path.join(work_dir, f'De_14_DeThi_p{i+1}.png'))

if res2.returncode == 0:
    doc2 = pymupdf.open(os.path.join(work_dir, 'De_14_DapAn.pdf'))
    print(f"De_14_DapAn.pdf has {len(doc2)} pages.")
    for i, page in enumerate(doc2):
        pix = page.get_pixmap(dpi=150)
        pix.save(os.path.join(work_dir, f'De_14_DapAn_p{i+1}.png'))

print("Completed export for ĐỀ SỐ 14!")
