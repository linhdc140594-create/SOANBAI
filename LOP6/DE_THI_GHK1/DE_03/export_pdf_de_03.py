import os
import sys
import json
import subprocess
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1\DE_03'
json_path = os.path.join(work_dir, 'de_03.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# 1. HÀM TẠO FILE TEX CHO ĐỀ THI (De_03_DeThi.tex)
# =============================================================================
def generate_dethi_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta,patterns}
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
\rhead{\textit{Môn Toán 6 -- Đề số 3}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

% --- KHUNG TIÊU ĐỀ ĐỀ THI ---
\noindent
\begin{tabularx}{\linewidth}{X r}
\textbf{TRƯỜNG THCS: \dotfill} & \textbf{ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I} \\
\textbf{Họ và tên: \dotfill} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{Lớp: \dotfill \quad SBD: \dotfill} & \textbf{Môn: TOÁN 6} \\
\hline
\end{tabularx}
\vspace{2mm}

\begin{center}
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 3}\\
  \textit{Thời gian làm bài: 90 phút (Không kể thời gian phát đề)}
\end{center}
\vspace{1mm}

% --- PHẦN I ---
\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)}

\textit{Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án duy nhất.}

\vspace{1mm}
'''
    body = ""
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

    # PHẦN II (Đúng / Sai)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI (2,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}

\vspace{1mm}
'''
    for q in d['phan_II_dung_sai']:
        noi_dung = q['noi_dung']
        cac_y = q['cac_y']

        tf_items = []
        for y_item in cac_y:
            is_true = y_item.get('dung_sai', False)
            prefix = "\\True " if is_true else ""
            txt = y_item['khang_dinh'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
        
        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)
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

    # PHẦN III (Trả lời ngắn)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN (2,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Điền kết quả số vào ô trống tương ứng.}

\vspace{1mm}
'''
    for q in d['phan_III_tra_loi_ngan']:
        noi_dung = q['noi_dung']
        da = q['dap_an'].strip()
        body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da}}}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (3,0 điểm)}

\textit{Thí sinh trình bày chi tiết lời giải vào giấy làm bài.}

\vspace{1mm}
'''
    for q in d['phan_IV_tu_luan']:
        cau_num = q['cau']
        diem = q.get('diem_tong', '')
        diem_str = f" ({diem} điểm)" if diem else ""
        noi_dung = q.get('noi_dung', '')

        body += f"\\begin{{ex}}{diem_str}\n"
        if noi_dung:
            body += f"{noi_dung}\n"

        if q.get('cac_y'):
            body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=2pt]\n"
            for y_item in q['cac_y']:
                y_label = y_item.get('y', '')
                de_item = y_item.get('de', '')
                body += f"\\item {de_item}\n"
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
# 2. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_03_DapAn.tex)
# =============================================================================
def generate_dapan_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta,patterns}
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
\rhead{\textit{Môn Toán 6 -- Hướng dẫn giải Đề số 3}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
  \textbf{\Large HƯỚNG DẪN GIẢI CHI TIẾT VÀ BẢNG ĐÁP ÁN}\\
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 3}\\
  \textit{Môn: Toán 6 -- Năm học 2026 -- 2027}
\end{center}
\vspace{2mm}

% --- BẢNG ĐÁP ÁN TRẮC NGHIỆM TỔNG HỢP ---
\noindent\textbf{\large A. BẢNG ĐÁP ÁN TRẮC NGHIỆM TỔNG HỢP}
\vspace{1.5mm}

\noindent\textbf{1. Phần I (Mỗi câu trả lời đúng được 0,25 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Đ/A} & \textbf{D} & \textbf{C} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{B} & \textbf{A} & \textbf{C} & \textbf{C} & \textbf{A} & \textbf{D} & \textbf{A} \\
\hline
\end{tabular}
\end{center}
\vspace{1mm}

\noindent\textbf{2. Phần II (Đúng/Sai):}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu 1} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} & \textbf{Câu 2} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\
\hline
\textbf{Đ/S} & \textbf{Đ} & \textbf{S} & \textbf{S} & \textbf{Đ} & \textbf{Đ/S} & \textbf{Đ} & \textbf{S} & \textbf{S} & \textbf{Đ} \\
\hline
\end{tabular}
\end{center}
\vspace{1mm}

\noindent\textbf{3. Phần III (Mỗi câu trả lời đúng được 1,0 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
\textbf{Câu} & \textbf{Câu 1} & \textbf{Câu 2} \\
\hline
\textbf{Đáp án} & \textbf{4} & \textbf{8} \\
\hline
\end{tabular}
\end{center}
\vspace{3mm}

% --- LỜI GIẢI CHI TIẾT ---
\noindent\textbf{\large B. HƯỚNG DẪN GIẢI CHI TIẾT TỪNG CÂU}
\vspace{2mm}

\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN}
\vspace{1mm}
'''
    body = ""
    for q in d['phan_I_trac_nghiem']:
        noi_dung = q['noi_dung']
        opts = q['lua_chon']
        da = q.get('dap_an', '').strip().upper()
        hinh = q.get('hinh_tikz')
        loi_giai = q.get('loi_giai', '')

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
            body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_code}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"

    # PHẦN II (Đúng / Sai)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI}
\vspace{1mm}
'''
    for q in d['phan_II_dung_sai']:
        noi_dung = q['noi_dung']
        cac_y = q['cac_y']

        tf_items = []
        giai_thich_items = []
        for y_item in cac_y:
            is_true = y_item.get('dung_sai', False)
            prefix = "\\True " if is_true else ""
            txt = y_item['khang_dinh'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
            gt = y_item.get('giai_thich', '')
            status_str = "\\textbf{Đúng}" if is_true else "\\textbf{Sai}"
            y_lbl = y_item['y']
            giai_thich_items.append(f"\\item \\textbf{{{y_lbl})}} {status_str}. {gt}")
        
        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)
        loigiai_tf = "\\begin{itemize}[leftmargin=0.6cm, itemsep=1pt]\n" + "\n".join(giai_thich_items) + "\n\\end{itemize}"

        body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\loigiai{{\n{loigiai_tf}\n}}\n\\end{{ex}}\n\n"

    # PHẦN III (Trả lời ngắn)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN}
\vspace{1mm}
'''
    for q in d['phan_III_tra_loi_ngan']:
        noi_dung = q['noi_dung']
        da = q['dap_an'].strip()
        loi_giai = q.get('loi_giai', '')
        body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da}}}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (3,0 ĐIỂM - CÓ BAREM ĐIỂM CHI TIẾT)}
\vspace{1mm}
'''
    for q in d['phan_IV_tu_luan']:
        cau_num = q['cau']
        diem = q.get('diem_tong', '')
        diem_str = f" ({diem} điểm)" if diem else ""
        noi_dung = q.get('noi_dung', '')

        body += f"\\begin{{ex}}{diem_str}\n"
        if noi_dung:
            body += f"{noi_dung}\n"

        if q.get('cac_y'):
            body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=2pt]\n"
            for y_item in q['cac_y']:
                y_label = y_item.get('y', '')
                de_item = y_item.get('de', '')
                body += f"\\item {de_item}\n"
            body += "\\end{enumerate}\n"

        # Lời giải tự luận
        loigiai_tl = "\\begin{itemize}[leftmargin=0.5cm, itemsep=3pt]\n"
        for y_item in q.get('cac_y', []):
            y_label = y_item.get('y', '')
            diem_y = y_item.get('diem', '')
            diem_tag = f" \\hfill \\textbf{{[{diem_y}đ]}}" if diem_y else ""
            loigiai_content = y_item.get('loi_giai', '')
            loigiai_tl += f"\\item \\textbf{{{y_label})}} {loigiai_content}{diem_tag}\n"
        loigiai_tl += "\\end{itemize}"

        body += f"\\loigiai{{\n{loigiai_tl}\n}}\n\\end{{ex}}\n\\vspace{{1.5mm}}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer

# =============================================================================
# 3. BIÊN SOẠN FILE VÀ BIÊN DỊCH PDF
# =============================================================================
print("=== BẮT ĐẦU TẠO FILE TEX & BIÊN DỊCH PDF CHO ĐỀ 03 LỚP 6 ===")

dethi_tex_content = generate_dethi_tex(d)
dethi_tex_path = os.path.join(work_dir, 'De_03_DeThi.tex')
with open(dethi_tex_path, 'w', encoding='utf-8') as f:
    f.write(dethi_tex_content)
print("Đã tạo:", dethi_tex_path)

dapan_tex_content = generate_dapan_tex(d)
dapan_tex_path = os.path.join(work_dir, 'De_03_DapAn.tex')
with open(dapan_tex_path, 'w', encoding='utf-8') as f:
    f.write(dapan_tex_content)
print("Đã tạo:", dapan_tex_path)

# Biên dịch pdflatex
for target in ['De_03_DeThi', 'De_03_DapAn']:
    print(f"\n-> Đang biên dịch {target}.tex...")
    cmd = ['pdflatex', '-interaction=nonstopmode', f'{target}.tex']
    res = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
    pdf_out = os.path.join(work_dir, f'{target}.pdf')
    if os.path.exists(pdf_out):
        reader = pymupdf.open(pdf_out)
        print(f"✅ Biên dịch thành công: {target}.pdf ({len(reader)} trang)")
    else:
        print(f"❌ Lỗi biên dịch {target}.tex:")
        print(res.stdout[-1500:])

print("\n=== HOÀN TẤT ĐỀ 03! ===")

