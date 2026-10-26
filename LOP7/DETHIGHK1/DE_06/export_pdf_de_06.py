import os
import sys
import json
import subprocess
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_06'
json_path = os.path.join(work_dir, 'de_06.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# 1. HÀM TẠO FILE TEX CHO ĐỀ THI (De_06_DeThi.tex)
# =============================================================================
def generate_dethi_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage[top=1.2cm, bottom=1.2cm, left=1.5cm, right=1.5cm]{geometry}
\usepackage[dethi]{ex_test}
\SAOPTN{widthSA=2.6,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ chuẩn viết tay
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

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Môn Toán 7 -- Đề số 6}}
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

\vspace{1.5mm}
\noindent
\begin{tabularx}{\linewidth}{|p{3.5cm}|X|}
\hline
\centering\textbf{Điểm số} & \centering\textbf{Lời nhận xét của thầy cô giáo} \tabularnewline
\rule{0pt}{1.6cm} & \\
\hline
\end{tabularx}

\vspace{2.5mm}
\begin{center}
\textbf{\large ĐỀ SỐ 6}
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

    # Bảng đáp án trắc nghiệm Phần I
    body += r'''
\vspace{1mm}
\noindent\textbf{BẢNG TRẢ LỜI TRẮC NGHIỆM PHẦN I:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Chọn} & \rule{0pt}{0.65cm} & & & & & & & & & & & \\
\hline
\end{tabular}
\end{center}
\vspace{2mm}
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
\textbf{Đ/S} & \rule{0pt}{0.6cm} & & & & \textbf{Đ/S} & & & & \\
\hline
\end{tabular}
\end{center}
\vspace{2mm}
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
            body += f"\\begin{{ex}}\n{noi_dung}\n\\begin{{center}}\n{hinh}\n\\end{{center}}\n\\hfill\\shortans{{{da_box}}}\n\\end{{ex}}\n\n"
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
                body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('cau_hoi', '')
                    body += f"\\item {content}\n"
                body += "\\end{enumerate}\n"
        body += "\\end{ex}\n\\vspace{1.5mm}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# =============================================================================
# 2. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_06_DapAn.tex)
# =============================================================================
def generate_dapan_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage[top=1.2cm, bottom=1.2cm, left=1.5cm, right=1.5cm]{geometry}
\usepackage[loigiai]{ex_test}
\SAOPTN{widthSA=2.6,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Lời giải chi tiết -- Đề số 6}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I -- Toán 7}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\Large HƯỚNG DẪN CHẤM VÀ LỜI GIẢI CHI TIẾT}\\
\vspace{1.5mm}
\textbf{\large MÔN: TOÁN 7 -- ĐỀ SỐ 6}
\end{center}
\vspace{2mm}
'''

    # PHẦN I ĐÁP ÁN
    body = r'''
\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN}

\vspace{1mm}
'''
    for q in d['phan_I_trac_nghiem']:
        noi_dung = q['noi_dung']
        opts = q['lua_chon']
        da = q.get('dap_an', '').strip().upper()
        hinh = q.get('hinh_tikz')
        lg = q.get('loi_giai', '')

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

    # PHẦN II ĐÁP ÁN
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
        for md in mds:
            is_true = "đúng" in md.get('dap_an', '').lower()
            prefix = "\\True " if is_true else ""
            txt = md['noi_dung'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
        
        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)

        lg_full = "\\begin{itemize}[leftmargin=0.5cm, itemsep=1pt]\n"
        for md in mds:
            y_name = md['y']
            is_t = "đúng" in md.get('dap_an', '').lower()
            status_str = "\\textbf{Đúng}" if is_t else "\\textbf{Sai}"
            lg_full += f"\\item \\textbf{{{y_name})}} {status_str}. {md.get('loi_giai', '')}\n"
        lg_full += "\\end{itemize}"

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_tf_code}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{lg_full}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\loigiai{{\n{lg_full}\n}}\n\\end{{ex}}\n\n"

    # PHẦN III ĐÁP ÁN
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
        lg = q.get('loi_giai', '')
        if hinh:
            body += f"\\begin{{ex}}\n{noi_dung}\n\\begin{{center}}\n{hinh}\n\\end{{center}}\n\\hfill\\shortans{{{da_box}}}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da_box}}}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"

    # PHẦN IV ĐÁP ÁN
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN}

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
                body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('cau_hoi', '')
                    body += f"\\item {content}\n"
                body += "\\end{enumerate}\n"

        # Lời giải
        body += "\\loigiai{\n"
        if q.get('cac_y'):
            for y_item in q['cac_y']:
                y_label = y_item.get('y', '')
                lg_y = y_item.get('loi_giai', '')
                body += f"\\textbf{{{y_label})}} {lg_y}\n\n"
        else:
            body += f"{q.get('loi_giai', '')}\n"
        body += "}\n\\end{ex}\n\\vspace{1.5mm}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# =============================================================================
# THỰC THI BIÊN DỊCH VÀ XUẤT FILE
# =============================================================================
tex_dethi = os.path.join(work_dir, 'De_06_DeThi.tex')
tex_dapan = os.path.join(work_dir, 'De_06_DapAn.tex')

print("Writing De_06_DeThi.tex...")
with open(tex_dethi, 'w', encoding='utf-8') as f:
    f.write(generate_dethi_tex(d))

print("Writing De_06_DapAn.tex...")
with open(tex_dapan, 'w', encoding='utf-8') as f:
    f.write(generate_dapan_tex(d))

print("Compiling De_06_DeThi.pdf with pdflatex...")
res1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_06_DeThi.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print(f"DeThi compile returncode: {res1.returncode}")
if res1.returncode != 0:
    for line in res1.stdout.split('\n')[-30:]:
        print(line)

print("Compiling De_06_DapAn.pdf with pdflatex...")
res2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_06_DapAn.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print(f"DapAn compile returncode: {res2.returncode}")
if res2.returncode != 0:
    for line in res2.stdout.split('\n')[-30:]:
        print(line)

# RENDER TRANG PREVIEW
if res1.returncode == 0:
    doc = pymupdf.open(os.path.join(work_dir, 'De_06_DeThi.pdf'))
    print(f"De_06_DeThi.pdf has {len(doc)} pages.")
    for i, p in enumerate(doc):
        p.get_pixmap(dpi=150).save(os.path.join(work_dir, f'De_06_DeThi_p{i+1}.png'))

if res2.returncode == 0:
    doc = pymupdf.open(os.path.join(work_dir, 'De_06_DapAn.pdf'))
    print(f"De_06_DapAn.pdf has {len(doc)} pages.")
    for i, p in enumerate(doc):
        p.get_pixmap(dpi=150).save(os.path.join(work_dir, f'De_06_DapAn_p{i+1}.png'))

print("Completed export for ĐỀ SỐ 6!")
