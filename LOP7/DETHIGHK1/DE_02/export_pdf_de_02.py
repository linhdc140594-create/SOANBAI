import os
import sys
import json
import subprocess
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_02'
json_path = os.path.join(work_dir, 'de_02.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# 1. HÀM TẠO FILE TEX CHO ĐỀ THI (De_02_DeThi.tex)
# =============================================================================
def generate_dethi_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta}
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
\rhead{\textit{Môn Toán 7 -- Đề số 2}}
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
\textbf{\large ĐỀ SỐ 2}
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
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (4,0 điểm)}

\textit{Thí sinh trình bày chi tiết lời giải vào giấy làm bài.}

\vspace{1mm}
'''
    for q in d['phan_IV_tu_luan']:
        cau_num = q['cau']
        noi_dung = q['noi_dung']
        hinh = q.get('hinh_tikz')

        body += f"\\begin{{ex}}\n"
        if hinh:
            sub_q = ""
            if q.get('cac_y'):
                sub_q += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('bieu_thuc') or y_item.get('cau_hoi', '')
                    sub_q += f"\\item {content}\n"
                sub_q += "\\end{enumerate}\n"
            body += f"\\immini{{\n{noi_dung}\n{sub_q}}}{{\n{hinh}\n}}\n"
        else:
            body += f"{noi_dung}\n"
            if q.get('cac_y'):
                body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('bieu_thuc') or y_item.get('cau_hoi', '')
                    body += f"\\item {content}\n"
                body += "\\end{enumerate}\n"

        body += f"\\end{{ex}}\n\\vspace{{1.5mm}}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# =============================================================================
# 2. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_02_DapAn.tex)
# =============================================================================
def generate_dapan_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage[top=1.2cm, bottom=1.2cm, left=1.5cm, right=1.5cm]{geometry}
\usepackage[loigiai]{ex_test}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Môn Toán 7 -- Lời giải Đề số 2}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\Large ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT -- ĐỀ SỐ 2}\\
\textit{Môn: TOÁN 7 -- Thời gian làm bài: 90 phút}
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
        lg = ""
        for md in mds:
            lg += f"\\textbf{{{md['y']})}} {md.get('loi_giai', '')}\\par\n"

        if hinh:
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_tf_code}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"

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

        sub_q = ""
        if q.get('cac_y'):
            sub_q += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
            for y_item in q['cac_y']:
                content = y_item.get('bieu_thuc') or y_item.get('cau_hoi', '')
                sub_q += f"\\item {content}\n"
            sub_q += "\\end{enumerate}\n"

        lg = ""
        if q.get('cac_y'):
            for y_item in q['cac_y']:
                y_label = y_item.get('y', '')
                y_lg = y_item.get('loi_giai', '')
                lg += f"\\textbf{{{y_label})}} {y_lg}\\par\n"
        else:
            lg = q.get('loi_giai', '')

        body += f"\\begin{{ex}}\n"
        if hinh:
            body += f"\\immini{{\n{noi_dung}\n{sub_q}}}{{\n{hinh}\n}}\n"
        else:
            body += f"{noi_dung}\n{sub_q}\n"
        body += f"\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\\vspace{{1.5mm}}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# Ghi ra các file .tex
dethi_tex_content = generate_dethi_tex(d)
dethi_file = os.path.join(work_dir, 'De_02_DeThi.tex')
with open(dethi_file, 'w', encoding='utf-8') as f:
    f.write(dethi_tex_content)
print(f"-> Đã ghi file {dethi_file}")

dapan_tex_content = generate_dapan_tex(d)
dapan_file = os.path.join(work_dir, 'De_02_DapAn.tex')
with open(dapan_file, 'w', encoding='utf-8') as f:
    f.write(dapan_tex_content)
print(f"-> Đã ghi file {dapan_file}")

# Biên dịch cả 2 file
print("Đang biên dịch De_02_DeThi.tex...")
r1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_02_DeThi.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("DeThi return code:", r1.returncode)

print("Đang biên dịch De_02_DapAn.tex...")
r2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_02_DapAn.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("DapAn return code:", r2.returncode)

# Xuất ảnh preview kiểm tra
if r1.returncode == 0:
    doc1 = pymupdf.open(os.path.join(work_dir, 'De_02_DeThi.pdf'))
    print(f"De_02_DeThi.pdf: {len(doc1)} trang.")
    for i, page in enumerate(doc1):
        page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'preview_dethi_p{i+1}.png'))
    print("-> Đã xuất preview các trang De_02_DeThi!")
else:
    for l in r1.stdout.split('\n')[-25:]:
        print(l)

if r2.returncode == 0:
    doc2 = pymupdf.open(os.path.join(work_dir, 'De_02_DapAn.pdf'))
    print(f"De_02_DapAn.pdf: {len(doc2)} trang.")
    for i, page in enumerate(doc2):
        page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'preview_dapan_p{i+1}.png'))
    print("-> Đã xuất preview các trang De_02_DapAn!")
else:
    for l in r2.stdout.split('\n')[-25:]:
        print(l)
