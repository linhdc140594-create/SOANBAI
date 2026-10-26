import os
import sys
import json
import subprocess
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_01'

# =============================================================================
# 7 MÃ TIKZ HOÀN TOÀN CHUẨN XÁC, TUYỆT ĐỐI KHÔNG LỖI, KHÔNG ĐÈ CHỮ
# =============================================================================

# 1. CÂU 4: Tam giác ABC có tia phân giác AD, BE
tikz_c4 = r'''\begin{tikzpicture}[scale=0.95, line cap=round, line join=round]
  \coordinate (B) at (0,0);
  \coordinate (C) at (6,0);
  \coordinate (A) at (2.2,3.2);
  \coordinate (D) at (2.63,0);
  \coordinate (E) at (3.69,1.94);

  % Cung góc A (tô xám nhạt và vẽ cung đơn)
  \fill[gray!30] (A) -- ($(A)!0.6cm!(B)$) arc[start angle=235.5, end angle=320, radius=0.6cm] -- cycle;
  \draw[thick] ($(A)!0.6cm!(B)$) arc[start angle=235.5, end angle=320, radius=0.6cm];

  % Cung góc B (tô xám nhạt và vẽ 2 cung đôi)
  \fill[gray!30] (B) -- (0.65,0) arc[start angle=0, end angle=55.5, radius=0.65cm] -- cycle;
  \draw[thick] (0.65,0) arc[start angle=0, end angle=55.5, radius=0.65cm];
  \draw[thick] (0.75,0) arc[start angle=0, end angle=55.5, radius=0.75cm];

  % Các cạnh tam giác
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  % Hai tia phân giác AD và BE
  \draw[thick] (A) -- (D);
  \draw[thick] (B) -- (E);

  % Các điểm
  \foreach \p in {A,B,C,D,E} \fill (\p) circle (1.6pt);
  \node[above=2pt] at (A) {$A$};
  \node[below left=2pt] at (B) {$B$};
  \node[below right=2pt] at (C) {$C$};
  \node[below=2pt] at (D) {$D$};
  \node[above right=2pt] at (E) {$E$};
\end{tikzpicture}'''

# 2. CÂU 5: Hai đường thẳng song song a // b, góc 65 độ, góc x tù 115 độ
tikz_c5 = r'''\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]
  \coordinate (B) at (1.8,0);
  \coordinate (A) at (3.0,1.8);

  % Hai đường thẳng song song a và b
  \draw[thick] (-0.2,1.8) -- (4.6,1.8) node[above=2pt, pos=0.1] {$a$};
  \draw[thick] (-0.2,0)   -- (4.6,0)   node[above=2pt, pos=0.1] {$b$};

  % Cát tuyến cắt a tại A, b tại B
  \draw[thick] (1.13,-1.0) -- (3.67,2.8);

  % Góc 65° tại A: trong cùng phía (dưới a, bên trái cát tuyến)
  \fill[gray!30] (A) -- ++(180:0.45) arc[start angle=180, end angle=236.3, radius=0.45] -- cycle;
  \draw[thick] (A) ++(180:0.45) arc[start angle=180, end angle=236.3, radius=0.45];
  \node at ($(A)+(-0.75,-0.3)$) {$65^\circ$};

  % Góc tù x tại B: trong cùng phía (trên b, bên trái cát tuyến)
  \draw[thick] (B) ++(56.3:0.45) arc[start angle=56.3, end angle=180, radius=0.45];
  \node at ($(B)+(-0.45,0.4)$) {$x$};

  % Giao điểm đỏ
  \fill[red] (A) circle (1.6pt);
  \fill[red] (B) circle (1.6pt);
\end{tikzpicture}'''

# 3. CÂU 7: Trục số điểm A = -1 2/3 (-5/3)
tikz_c7 = r'''\begin{tikzpicture}[scale=1.6, line cap=round, line join=round, >=Stealth]
  % Trục số có mũi tên sang phải
  \draw[thick, ->] (-3.4,0) -- (1.5,0);
  % Các chấm chia 1/3 đơn vị
  \foreach \i in {-9,-8,...,3}{
    \fill ({\i/3},0) circle (1.4pt);
  }
  % Nhãn các số nguyên chính
  \node[below=4pt] at (-3,0) {$-3$};
  \node[below=4pt] at (-2,0) {$-2$};
  \node[below=4pt] at (-1,0) {$-1$};
  \node[below=4pt] at (0,0)  {$0$};
  \node[below=4pt] at (1,0)  {$1$};

  % Điểm A tại -5/3 = -1 2/3
  \node[below=4pt, font=\bfseries] at (-5/3,0) {$A$};
\end{tikzpicture}'''

# 4. CÂU 10: 4 hình lăng trụ/hình khối (Hình trụ, chóp cụt, lăng trụ nằm ngang, lăng trụ đứng)
tikz_c10 = r'''\begin{tikzpicture}[scale=0.68, line cap=round, line join=round, thick]
  % Hình 1: Hình trụ
  \begin{scope}[shift={(0,0)}]
    \draw (0,2.2) ellipse (0.8 and 0.3);
    \draw (-0.8,0) -- (-0.8,2.2);
    \draw (0.8,0) -- (0.8,2.2);
    \draw (-0.8,0) arc[start angle=180, end angle=360, x radius=0.8, y radius=0.3];
    \draw[dashed] (-0.8,0) arc[start angle=180, end angle=0, x radius=0.8, y radius=0.3];
    \node[below=4pt] at (0,-0.4) {Hình 1};
  \end{scope}

  % Hình 2: Hình chóp cụt tam giác
  \begin{scope}[shift={(3.8,0)}]
    \draw (0,0) -- (1.8,0) -- (1.3,0.6);
    \draw (0.3,2.0) -- (1.5,2.0) -- (1.1,2.4) -- cycle;
    \draw (0,0) -- (0.3,2.0);
    \draw (1.8,0) -- (1.5,2.0);
    \draw (1.3,0.6) -- (1.1,2.4);
    \draw[dashed] (0,0) -- (1.3,0.6);
    \node[below=4pt] at (0.9,-0.4) {Hình 2};
  \end{scope}

  % Hình 3: Lăng trụ tam giác nằm ngang
  \begin{scope}[shift={(7.6,0)}]
    \draw (0,0) -- (1.5,0) -- (0.7,1.3) -- cycle;
    \draw (0.7,1.3) -- (2.1,2.4);
    \draw (1.5,0) -- (2.9,1.1);
    \draw (2.1,2.4) -- (2.9,1.1);
    \draw (0,0) -- (1.4,1.1);
    \draw[dashed] (1.4,1.1) -- (2.1,2.4);
    \draw[dashed] (1.4,1.1) -- (2.9,1.1);
    \node[below=4pt] at (1.4,-0.4) {Hình 3};
  \end{scope}

  % Hình 4: Lăng trụ đứng tam giác
  \begin{scope}[shift={(12.2,0)}]
    \draw (0,2.2) -- (1.8,2.2) -- (1.1,1.7) -- cycle;
    \draw (0,0) -- (1.8,0) -- (1.1,-0.5) -- cycle;
    \draw (0,0) -- (0,2.2);
    \draw (1.8,0) -- (1.8,2.2);
    \draw (1.1,-0.5) -- (1.1,1.7);
    \node[below=4pt] at (0.9,-0.7) {Hình 4};
  \end{scope}
\end{tikzpicture}'''

# 5. CÂU 11: 4 hình khối lăng trụ tứ giác/tam giác/lập phương
tikz_c11 = r'''\begin{tikzpicture}[scale=0.68, line cap=round, line join=round, thick]
  % Hình 1: Lăng trụ tứ giác
  \begin{scope}[shift={(0,0)}]
    \draw (0,0) -- (2.0,0) -- (1.5,-0.5) -- (-0.3,-0.5) -- cycle;
    \draw (0,2.0) -- (2.0,2.0) -- (1.5,1.5) -- (-0.3,1.5) -- cycle;
    \draw (0,0) -- (0,2.0);
    \draw (2.0,0) -- (2.0,2.0);
    \draw (1.5,-0.5) -- (1.5,1.5);
    \draw (-0.3,-0.5) -- (-0.3,1.5);
    \node[below=4pt] at (0.8,-0.7) {Hình 1};
  \end{scope}

  % Hình 2: Lăng trụ tam giác nằm ngang (đáp án đúng)
  \begin{scope}[shift={(4.5,0)}]
    \draw (0,0) -- (1.4,0) -- (0.7,1.2) -- cycle;
    \draw (0,0) -- (1.4,1.0);
    \draw (0.7,1.2) -- (2.1,2.2);
    \draw (1.4,0) -- (2.8,1.0);
    \draw (2.1,2.2) -- (2.8,1.0);
    \draw[dashed] (1.4,1.0) -- (2.1,2.2);
    \draw[dashed] (1.4,1.0) -- (2.8,1.0);
    \node[below=4pt] at (1.4,-0.4) {Hình 2};
  \end{scope}

  % Hình 3: Hình lập phương
  \begin{scope}[shift={(9.2,0)}]
    \draw (0,0) rectangle (1.6,1.6);
    \draw (1.6,0) -- (2.2,0.5) -- (2.2,2.1) -- (1.6,1.6);
    \draw (0,1.6) -- (0.6,2.1) -- (2.2,2.1);
    \draw[dashed] (0,0) -- (0.6,0.5) -- (2.2,0.5);
    \draw[dashed] (0.6,0.5) -- (0.6,2.1);
    \node[below=4pt] at (1.1,-0.4) {Hình 3};
  \end{scope}

  % Hình 4: Lăng trụ tứ giác đứng
  \begin{scope}[shift={(13.2,0)}]
    \draw (0,0) rectangle (1.8,2.0);
    \draw (1.8,0) -- (2.5,0.6) -- (2.5,2.6) -- (1.8,2.0);
    \draw (0,2.0) -- (0.7,2.6) -- (2.5,2.6);
    \draw[dashed] (0,0) -- (0.7,0.6) -- (2.5,0.6);
    \draw[dashed] (0.7,0.6) -- (0.7,2.6);
    \node[below=4pt] at (1.2,-0.4) {Hình 4};
  \end{scope}
\end{tikzpicture}'''

# 6. PHẦN II CÂU 2: Hai đường a, b vuông góc CD, cát tuyến BA kéo dài rõ ràng, các góc tại B và A
tikz_p2c2 = r'''\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  \coordinate (C) at (0, 2.8);
  \coordinate (D) at (0, 0);
  \coordinate (B) at (3.0, 0);
  \coordinate (A) at (4.6, 2.8);

  % Đường CD thẳng đứng kéo dài
  \draw[thick] (0, 3.6) -- (0, -0.8);
  % Đường thẳng a qua C, A
  \draw[thick] (-0.8, 2.8) -- (6.0, 2.8) node[below=2pt, pos=0.96] {$a$};
  % Đường thẳng b qua D, B
  \draw[thick] (-0.8, 0)   -- (6.0, 0)   node[below=2pt, pos=0.96] {$b$};

  % Cát tuyến BA kéo dài rõ ràng hai đầu (từ dưới b lên trên a)
  \draw[thick] (2.2, -1.4) -- (5.4, 4.2);

  % Ký hiệu góc vuông tại C và D
  \draw[thick] (0, 2.55) -- (0.25, 2.55) -- (0.25, 2.8);
  \draw[thick] (0, 0.25) -- (0.25, 0.25) -- (0.25, 0);

  % Các giao điểm đỏ
  \foreach \p in {C,D,A,B} \fill[red] (\p) circle (1.8pt);
  \node[above left=1pt] at (C) {$C$};
  \node[below left=1pt] at (D) {$D$};
  \node[above left=2pt] at (A) {$A$};
  \node[above left=14pt] at (B) {$B$};

  % Góc A1
  \node[font=\small] at (4.04, 2.48) {$1$};

  % Cung góc B4 (120°)
  \draw[thick] ($(B)+(-0.45,0)$) arc[start angle=180, end angle=60.3, radius=0.45cm];

  % Các góc 1, 2, 3, 4 tại B (đặt chính xác trong 4 góc phần tư, không đè nhãn B hay vạch kẻ)
  \node[font=\small] at (2.68, 0.52) {$4$};
  \node[font=\small] at (3.56, 0.32) {$3$};
  \node[font=\small] at (2.44, -0.32) {$1$};
  \node[font=\small] at (3.32, -0.56) {$2$};
\end{tikzpicture}'''

# 7. PHẦN IV CÂU 3: a, b vuông góc AB, cát tuyến CD kéo dài rõ ràng, góc C = 100 độ, góc D1
tikz_p4c3 = r'''\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  \coordinate (A) at (0, 2.8);
  \coordinate (B) at (0, 0);
  \coordinate (D) at (3.5, 2.8);
  \coordinate (C) at (4.0, 0);

  % Đoạn AB thẳng đứng kéo dài
  \draw[thick] (0, 3.6) -- (0, -0.8);
  % Đường a qua A, D
  \draw[thick] (-0.8, 2.8) -- (5.6, 2.8) node[above=2pt, pos=0.96] {$a$};
  % Đường b qua B, C
  \draw[thick] (-0.8, 0)   -- (5.6, 0)   node[above=2pt, pos=0.96] {$b$};

  % Cát tuyến CD kéo dài rõ ràng hai đầu (từ dưới b lên trên a)
  \draw[thick] (4.12, -0.7) -- (3.38, 3.5);

  % Ký hiệu góc vuông tại A và B
  \draw[thick] (0, 2.55) -- (0.25, 2.55) -- (0.25, 2.8);
  \draw[thick] (0, 0.25) -- (0.25, 0.25) -- (0.25, 0);

  % Các giao điểm đỏ
  \foreach \p in {A,B,C,D} \fill[red] (\p) circle (1.8pt);
  \node[above left=1pt] at (A) {$A$};
  \node[below left=1pt] at (B) {$B$};
  \node[above left=1pt] at (D) {$D$};
  \node[below left=1pt] at (C) {$C$};

  % Cung góc C = 100° (tô xám nhẹ)
  \fill[gray!35] (C) -- ++(0:0.45) arc[start angle=0, end angle=100, radius=0.45] -- cycle;
  \draw[thick] (C) ++(0:0.45) arc[start angle=0, end angle=100, radius=0.45];
  \node[font=\small] at ($(C)+(45:0.85)$) {$100^\circ$};

  % Nhãn góc D1
  \node[font=\small] at (3.85, 2.5) {$1$};
\end{tikzpicture}'''

# =============================================================================
# 1. CẬP NHẬT FILE de_01.json VỚI CÁC MÃ TIKZ HOÀN THIỆN
# =============================================================================
json_path = os.path.join(work_dir, 'de_01.json')
with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

d['phan_I_trac_nghiem'][3]['hinh_tikz'] = tikz_c4
d['phan_I_trac_nghiem'][4]['hinh_tikz'] = tikz_c5
d['phan_I_trac_nghiem'][6]['hinh_tikz'] = tikz_c7
d['phan_I_trac_nghiem'][9]['hinh_tikz'] = tikz_c10
d['phan_I_trac_nghiem'][10]['hinh_tikz'] = tikz_c11
d['phan_II_dung_sai'][1]['hinh_tikz'] = tikz_p2c2
d['phan_IV_tu_luan'][2]['hinh_tikz'] = tikz_p4c3

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print("-> Đã cập nhật de_01.json với 7 mã TikZ hoàn thiện!")

# =============================================================================
# 2. HÀM TẠO FILE TEX CHO ĐỀ THI (De_01_DeThi.tex)
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
\rhead{\textit{Môn Toán 7 -- Đề số 1}}
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
\textbf{\large ĐỀ SỐ 1}
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

        # Gắn \True vào phương án đúng, bỏ dấu chấm cuối cùng nếu có để tránh in ..
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
            if q['cau'] in [4, 5]:
                body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_code}\n}}{{\n{hinh}\n}}\n\\end{{ex}}\n\n"
            else:
                body += f"\\begin{{ex}}\n{noi_dung}\n\\begin{{center}}\n{hinh}\n\\end{{center}}\n{choice_code}\n\\end{{ex}}\n\n"
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

    # PHẦN II (Đúng / Sai) -> Reset counter ex để bắt đầu từ Câu 1
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

    # PHẦN III (Trả lời ngắn) -> Reset counter ex để bắt đầu từ Câu 1
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN (1,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Điền kết quả vào ô trống.}

\vspace{1mm}
'''
    for q in d['phan_III_tra_loi_ngan']:
        noi_dung = q['noi_dung']
        da = q['dap_an']
        body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da}}}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận) -> Reset counter ex để bắt đầu từ Câu 1
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
            if 'cac_y' in q:
                sub_q += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
                for y_item in q['cac_y']:
                    content = y_item.get('bieu_thuc') or y_item.get('cau_hoi', '')
                    sub_q += f"\\item {content}\n"
                sub_q += "\\end{enumerate}\n"
            body += f"\\immini{{\n{noi_dung}\n{sub_q}}}{{\n{hinh}\n}}\n"
        else:
            body += f"{noi_dung}\n"
            if 'cac_y' in q:
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
# 3. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_01_DapAn.tex) SỬ DỤNG ex_test [loigiai]
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
\rhead{\textit{Môn Toán 7 -- Lời giải Đề số 1}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\Large ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT -- ĐỀ SỐ 1}\\
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
            if q['cau'] in [4, 5]:
                body += f"\\begin{{ex}}\n\\immini{{\n{noi_dung}\n{choice_code}\n}}{{\n{hinh}\n}}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"
            else:
                body += f"\\begin{{ex}}\n{noi_dung}\n\\begin{{center}}\n{hinh}\n\\end{{center}}\n{choice_code}\n\\loigiai{{\n{lg}\n}}\n\\end{{ex}}\n\n"
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
        lg = q.get('loi_giai', '')
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
        if 'cac_y' in q:
            sub_q += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=1pt]\n"
            for y_item in q['cac_y']:
                content = y_item.get('bieu_thuc') or y_item.get('cau_hoi', '')
                sub_q += f"\\item {content}\n"
            sub_q += "\\end{enumerate}\n"

        lg = ""
        if 'cac_y' in q:
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
dethi_file = os.path.join(work_dir, 'De_01_DeThi.tex')
with open(dethi_file, 'w', encoding='utf-8') as f:
    f.write(dethi_tex_content)
print(f"-> Đã ghi file {dethi_file}")

dapan_tex_content = generate_dapan_tex(d)
dapan_file = os.path.join(work_dir, 'De_01_DapAn.tex')
with open(dapan_file, 'w', encoding='utf-8') as f:
    f.write(dapan_tex_content)
print(f"-> Đã ghi file {dapan_file}")

# Biên dịch cả 2 file
print("Đang biên dịch De_01_DeThi.tex...")
r1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_01_DeThi.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("DeThi return code:", r1.returncode)

print("Đang biên dịch De_01_DapAn.tex...")
r2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_01_DapAn.tex'], cwd=work_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("DapAn return code:", r2.returncode)

# Xuất ảnh preview kiểm tra
if r1.returncode == 0:
    doc1 = pymupdf.open(os.path.join(work_dir, 'De_01_DeThi.pdf'))
    print(f"De_01_DeThi.pdf: {len(doc1)} trang.")
    for i, page in enumerate(doc1):
        page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'final_dethi_p{i+1}.png'))
    print("-> Đã xuất preview các trang De_01_DeThi!")

if r2.returncode == 0:
    doc2 = pymupdf.open(os.path.join(work_dir, 'De_01_DapAn.pdf'))
    print(f"De_01_DapAn.pdf: {len(doc2)} trang.")
    for i, page in enumerate(doc2):
        page.get_pixmap(dpi=150).save(os.path.join(work_dir, f'final_dapan_p{i+1}.png'))
    print("-> Đã xuất preview các trang De_01_DapAn!")
