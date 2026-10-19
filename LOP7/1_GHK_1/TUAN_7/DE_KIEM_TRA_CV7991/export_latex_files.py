# -*- coding: utf-8 -*-
"""
export_latex_files.py
Xuất 5 file LaTeX độc lập từ dữ liệu chuẩn Công văn 7991:
1. ma_tran_va_dac_ta.tex
2. de_01.tex (Chuẩn 2 trang A4: Trang 1/2 và Trang 2/2)
3. dap_an_de_01.tex (Chuẩn 1 trang A4)
4. de_02.tex (Chuẩn 2 trang A4: Trang 1/2 và Trang 2/2)
5. dap_an_de_02.tex (Chuẩn 1 trang A4)
"""

import os
import sys
import subprocess
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# 1. FILE: ma_tran_va_dac_ta.tex
# ==============================================================================

MA_TRAN_TEX = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{array}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage[landscape, top=1.2cm, bottom=1.2cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\rfoot{\small\textit{Trang \thepage}}
\lfoot{\small\textit{Ma trận và Bản đặc tả Đề kiểm tra Giữa HK I -- Toán 7 -- Năm học 2026--2027}}
\renewcommand{\headrulewidth}{0pt}

\newcolumntype{Y}{>{\centering\arraybackslash}X}
\newcolumntype{M}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}

\begin{document}

\begin{center}
  \textbf{\large MA TRẬN, BẢN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA HỌC KÌ I}\\[2mm]
  \textbf{\large MÔN TOÁN -- LỚP 7 -- NĂM HỌC 2026 -- 2027}\\[1mm]
  \textit{(Căn cứ theo Công văn 7991/BGDĐT-GDTrH -- Áp dụng chung cho Đề 1 và Đề 2)}
\end{center}

\vspace{1.5mm}
\noindent\textbf{\large I. KHUNG MA TRẬN ĐỀ KIỂM TRA (Bước 1)}
\vspace{1mm}

\noindent
\small
\begin{tabularx}{\linewidth}{|M{7mm}|L{2.8cm}|X|*{12}{M{7mm}|}M{1.1cm}|M{1.3cm}|}
\hline
\multirow{3}{*}{\textbf{TT}} & \multirow{3}{*}{\textbf{Chủ đề / Chương}} & \multirow{3}{*}{\textbf{Nội dung / đơn vị kiến thức}} & \multicolumn{12}{c|}{\textbf{Mức độ đánh giá}} & \multicolumn{2}{c|}{\textbf{Tổng}} \\ \cline{4-17}
& & & \multicolumn{3}{c|}{\textbf{Nhiều lựa chọn}} & \multicolumn{3}{c|}{\textbf{Đúng -- Sai (ý)}} & \multicolumn{3}{c|}{\textbf{Trả lời ngắn}} & \multicolumn{3}{c|}{\textbf{Tự luận}} & \textbf{Số} & \textbf{Điểm} \\ \cline{4-15}
& & & \textbf{B} & \textbf{H} & \textbf{VD} & \textbf{B} & \textbf{H} & \textbf{VD} & \textbf{B} & \textbf{H} & \textbf{VD} & \textbf{B} & \textbf{H} & \textbf{VD} & \textbf{câu/ý} & \textbf{(\%)} \\ \hline

1 & \textbf{Chương I: Số hữu tỉ} & Tập hợp số hữu tỉ. Thứ tự trong $\mathbb{Q}$ (Bài 1) & 2 & & & & & & & & & & & & 2 & 0,5 (5\%) \\ \cline{3-17}
& & Các phép tính với số hữu tỉ (Bài 2, 3, 4) & 2 & & & & & & & 1 & & & 1 & 2 & 6 & 3,0 (30\%) \\ \hline

2 & \textbf{Chương II: Số thực} & Số thập phân vô hạn tuần hoàn. Làm tròn (Bài 5) & 1 & 1 & & & & & & & & & & & 2 & 0,5 (5\%) \\ \cline{3-17}
& & Số vô tỉ. Căn bậc hai số học. Số thực (Bài 6, 7) & 2 & & & 1 & 2 & 1 & 1 & & 1 & & & & 8 & 2,5 (25\%) \\ \hline

3 & \textbf{Chương III: Góc \& ĐT song song} & Góc ở vị trí đặc biệt. Tia phân giác (Bài 8, 9) & 1 & 1 & & & & & & & & & & & 2 & 0,5 (5\%) \\ \cline{3-17}
& & Hai đường thẳng song song (Bài 10) & 2 & & & 2 & 1 & 1 & & 1 & & & 1 & & 8 & 2,5 (25\%) \\ \cline{3-17}
& & Định lí và chứng minh định lí (Bài 11) & & & & & & & & & & & & 1 & 1 & 0,5 (5\%) \\ \hline

\multicolumn{3}{|c|}{\textbf{Tổng số câu / ý}} & \textbf{8} & \textbf{2} & \textbf{0} & \textbf{3} & \textbf{3} & \textbf{2} & \textbf{1} & \textbf{2} & \textbf{1} & \textbf{0} & \textbf{2} & \textbf{3} & \textbf{29} & \textbf{10,0} \\ \hline
\multicolumn{3}{|c|}{\textbf{Tổng số điểm}} & \multicolumn{3}{c|}{\textbf{3,0 điểm}} & \multicolumn{3}{c|}{\textbf{2,0 điểm}} & \multicolumn{3}{c|}{\textbf{2,0 điểm}} & \multicolumn{3}{c|}{\textbf{3,0 điểm}} & \multicolumn{2}{c|}{\textbf{10,0 đ}} \\ \hline
\multicolumn{3}{|c|}{\textbf{Tỉ lệ \%}} & \multicolumn{3}{c|}{\textbf{30\%}} & \multicolumn{3}{c|}{\textbf{20\%}} & \multicolumn{3}{c|}{\textbf{20\%}} & \multicolumn{3}{c|}{\textbf{30\%}} & \multicolumn{2}{c|}{\textbf{100\%}} \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textit{* Ghi chú tỉ lệ nhận thức:} Nhận biết: 4,0 điểm (40\%) -- Thông hiểu: 3,0 điểm (30\%) -- Vận dụng: 3,0 điểm (30\%).\\
\textit{* Phân môn:} Đại số 6,5 điểm (65\%) -- Hình học 3,5 điểm (35\%).

\newpage
\noindent\textbf{\large II. BẢN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA HỌC KÌ I (Bước 2)}
\vspace{2mm}

\noindent
\small
\begin{tabularx}{\linewidth}{|M{7mm}|L{2.8cm}|L{3.2cm}|M{1.4cm}|X|L{3.2cm}|M{1.1cm}|M{1.6cm}|}
\hline
\textbf{TT} & \textbf{Chương/Chủ đề} & \textbf{Nội dung} & \textbf{Mức độ} & \textbf{Yêu cầu cần đạt} & \textbf{Dạng câu / Câu số} & \textbf{Số câu} & \textbf{Năng lực} \\ \hline

1 & \textbf{Số hữu tỉ} (Chương I) & Tập hợp số hữu tỉ. Thứ tự trong $\mathbb{Q}$ & Biết & Nhận biết số hữu tỉ, kí hiệu $\mathbb{Q}$, số đối, thứ tự trong $\mathbb{Q}$. & NLC: C1, C2 & 2 & TD, GT \\ \cline{3-8}
& & Phép tính với số hữu tỉ & Biết & Luỹ thừa với số mũ tự nhiên; quy tắc chuyển vế, dấu ngoặc. & NLC: C3, C4 & 2 & TD \\ \cline{4-8}
& & & Hiểu & Tính toán thành thạo, tìm $x$, phối hợp các phép tính. & TLN: C16;\; TL: 19a & 2 & TD, CC \\ \cline{4-8}
& & & VD & Vận dụng giải bài toán tìm $x$ luỹ thừa, bài toán thực tế tỉ số/phần trăm. & TL: 19b, C20 & 2 & GQ, CC \\ \hline

2 & \textbf{Số thực} (Chương II) & Số thập phân VHTH. Làm tròn số & Biết & Nhận biết chu kì của số thập phân vô hạn tuần hoàn. & NLC: C5 & 1 & TD \\ \cline{4-8}
& & & Hiểu & Ước lượng và làm tròn số theo độ chính xác cho trước. & NLC: C8 & 1 & TD, CC \\ \cline{3-8}
& & Căn bậc hai số học. Số thực & Biết & Căn bậc hai số học, số vô tỉ, giá trị tuyệt đối. & NLC: C6, C7;\; ĐS: 13a;\; TLN: C15 & 4 & TD \\ \cline{4-8}
& & & Hiểu & So sánh các số thực, tính chất số thập phân vô hạn tuần hoàn. & ĐS: 13b, 13c & 2 & TD, CC \\ \cline{4-8}
& & & VD & Giải phương trình chứa dấu giá trị tuyệt đối; bài toán thực tế căn bậc hai. & ĐS: 13d;\; TLN: C18 & 2 & TD, GQ \\ \hline

3 & \textbf{Góc \& ĐT song song} (Chương III) & Góc đặc biệt. Tia phân giác & Biết & Tính chất hai góc đối đỉnh; khái niệm tia phân giác. & NLC: C9 & 1 & TD \\ \cline{4-8}
& & & Hiểu & Tính số đo góc kề bù, góc đối đỉnh, góc tạo bởi tia phân giác. & NLC: C11 & 1 & TD, GT \\ \cline{3-8}
& & Hai ĐT song song & Biết & Tiên đề Euclid; nhận biết góc so le trong, đồng vị; quan hệ từ vuông góc đến song song. & NLC: C10, C12;\; ĐS: 14a, 14b & 4 & TD, GT \\ \cline{4-8}
& & & Hiểu & Dấu hiệu nhận biết hai đường thẳng song song; tính số đo góc tạo bởi cát tuyến. & ĐS: 14c;\; TLN: C17;\; TL: 21a & 3 & TD, GT \\ \cline{4-8}
& & & VD & Vận dụng tia phân giác và song song tính góc phức hợp. & ĐS: 14d & 1 & TD, GQ \\ \cline{3-8}
& & Định lí \& Chứng minh định lí & VD & Chứng minh bài toán hình học có lập luận chặt chẽ (song song, vuông góc). & TL: 21b & 1 & TD, GQ \\ \hline
\end{tabularx}

\newpage
\noindent\textbf{\large III. BƯỚC 5: BẢNG KIỂM TRA LẠI ĐỀ (Áp dụng chung cho Đề 1 và Đề 2)}
\vspace{2mm}

\noindent
\normalsize
\begin{tabularx}{\linewidth}{|M{1.2cm}|L{4.2cm}|X|M{2.4cm}|}
\hline
\textbf{STT} & \textbf{Tiêu chí kiểm tra} & \textbf{Kết quả đối soát thực tế} & \textbf{Kết luận} \\ \hline
1 & \textbf{Độ cân đối giữa các mức độ nhận thức} & Biết 4,0 đ (40\%) -- Hiểu 3,0 đ (30\%) -- Vận dụng 3,0 đ (30\%). Đúng chuẩn quy định tại Công văn 7991. Dạng câu: Nhiều lựa chọn 3,0 đ; Đúng/Sai 2,0 đ; Trả lời ngắn 2,0 đ; Tự luận 3,0 đ. & \textbf{ĐẠT} \\ \hline
2 & \textbf{Tỉ lệ phân môn} & Đại số 6,5 đ (65\%) -- Hình học 3,5 đ (35\%). Phù hợp tiến độ dạy học đến tuần 10 (Đại số 24 tiết $\approx 69\%$, Hình học 11 tiết $\approx 31\%$). & \textbf{ĐẠT} \\ \hline
3 & \textbf{Sự phù hợp chuẩn đầu ra} & Mọi câu hỏi bám sát chuẩn kiến thức, kĩ năng môn Toán 7 (CT GDPT 2018). Không sử dụng các kiến thức chưa học (tam giác bằng nhau, định lí Pythagore). & \textbf{ĐẠT} \\ \hline
4 & \textbf{Tính chính xác của đáp án} & Đã giải độc lập cả hai mã đề. Các câu trắc nghiệm chỉ có 1 phương án đúng duy nhất; lời giải tự luận phân bậc $0{,}25$đ rõ ràng. & \textbf{ĐẠT} \\ \hline
\end{tabularx}

\end{document}
'''

# ==============================================================================
# 2. FILE: de_01.tex (Gọn gàng chính xác 2 trang A4, TikZ cực nét)
# ==============================================================================

DE_01_TEX = r'''\documentclass[10.5pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage[top=0.9cm, bottom=0.9cm, left=1.1cm, right=1.1cm]{geometry}
\usepackage{fancyhdr}
\usepackage{enumitem}

\pagestyle{fancy}
\fancyhf{}
\rfoot{\small\textit{Trang \thepage/2}}
\lfoot{\small\textit{Đề kiểm tra Giữa học kì I -- Môn Toán 7 -- Đề 1}}
\renewcommand{\headrulewidth}{0pt}

\setlength{\parskip}{0.5pt}

\begin{document}

\noindent
\begin{tabularx}{\linewidth}{X r}
\textbf{TRƯỜNG THCS \dots\dots\dots\dots\dots\dots} & \textbf{ĐỀ KIỂM TRA GIỮA HỌC KÌ I -- NĂM HỌC 2026 -- 2027} \\
\textbf{TỔ: \dots\dots\dots\dots\dots\dots} & \textbf{Môn: TOÁN -- Lớp 7} \\
\textit{(Đề 1 -- gồm 02 trang)} & \textit{Thời gian làm bài: 90 phút (không kể thời gian giao đề)} \\
\end{tabularx}

\vspace{1mm}
\noindent
\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{
\textbf{Họ và tên học sinh:} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots \textbf{Lớp:} \dots\dots\dots \textbf{Số báo danh:} \dots\dots\dots
}}

\vspace{1.5mm}
\noindent\textbf{\large PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (3,0 điểm).}
\vspace{0.5mm}

\noindent\textit{Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}

\vspace{1mm}
\noindent\textbf{Câu 1.} Khẳng định nào sau đây đúng?\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\dfrac{2}{3} \in \mathbb{Z}$ & B. $-\dfrac{3}{5} \in \mathbb{Q}$ & C. $-5 \notin \mathbb{Q}$ & D. $0,5 \notin \mathbb{Q}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 2.} Số đối của số hữu tỉ $-\dfrac{4}{7}$ là\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\dfrac{4}{7}$ & B. $-\dfrac{4}{7}$ & C. $\dfrac{7}{4}$ & D. $-\dfrac{7}{4}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 3.} Với $x$ là số hữu tỉ khác 0, tích $x^5 \cdot x^3$ bằng\\
\begin{tabularx}{\linewidth}{X X X X}
A. $x^{15}$ & B. $x^2$ & C. $2x^8$ & D. $x^8$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 4.} Áp dụng quy tắc chuyển vế, từ đẳng thức $x + \dfrac{1}{2} = \dfrac{3}{4}$ ta được\\
\begin{tabularx}{\linewidth}{X X X X}
A. $x = \dfrac{3}{4} + \dfrac{1}{2}$ & B. $x = \dfrac{1}{2} - \dfrac{3}{4}$ & C. $x = \dfrac{3}{4} - \dfrac{1}{2}$ & D. $x = \dfrac{3}{4} \cdot \dfrac{1}{2}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 5.} Phân số nào sau đây viết được dưới dạng số thập phân vô hạn tuần hoàn?\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\dfrac{3}{8}$ & B. $\dfrac{5}{12}$ & C. $\dfrac{7}{20}$ & D. $\dfrac{9}{25}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 6.} Căn bậc hai số học của 64 là\\
\begin{tabularx}{\linewidth}{X X X X}
A. $8$ & B. $-8$ & C. $32$ & D. $8$ và $-8$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 7.} Số nào sau đây là số vô tỉ?\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\sqrt{9}$ & B. $-0,(3)$ & C. $\dfrac{2}{7}$ & D. $\sqrt{5}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 8.} Làm tròn số $3,14159$ với độ chính xác $0,005$ ta được\\
\begin{tabularx}{\linewidth}{X X X X}
A. $3,141$ & B. $3,15$ & C. $3,14$ & D. $3,1$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 9.} Hai góc đối đỉnh thì\\
\begin{tabularx}{\linewidth}{X X X X}
A. bù nhau. & B. bằng nhau. & C. phụ nhau. & D. kề nhau.
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 10.} Qua một điểm $M$ nằm ngoài đường thẳng $a$, có bao nhiêu đường thẳng song song với $a$?\\
\begin{tabularx}{\linewidth}{X X X X}
A. Không có. & B. Có hai. & C. Có vô số. & D. Chỉ có một.
\end{tabularx}

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 11.} Cho hình bên, biết $\widehat{xOy} = 110^\circ$. Số đo góc $yOx'$ là\\
\begin{tabularx}{\linewidth}{X X}
A. $70^\circ$ & B. $110^\circ$ \\
C. $90^\circ$ & D. $20^\circ$
\end{tabularx}
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]
  \coordinate (O) at (0,0);
  \coordinate (X) at (1.9,0);
  \coordinate (Xp) at (-1.9,0);
  \coordinate (Y) at ({1.7*cos(110)}, {1.7*sin(110)});
  \draw[very thick] (Xp) node[left] {$x'$} -- (X) node[right] {$x$};
  \draw[very thick] (O) -- (Y) node[above] {$y$};
  \fill (O) circle (1.8pt) node[below=2pt] {$O$};
  \draw[thick] (0.38,0) arc (0:110:0.38);
  \node at (55:0.7) {\small $110^\circ$};
\end{tikzpicture}
\end{minipage}

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 12.} Cho hình bên, đường thẳng $c$ cắt hai đường thẳng $a, b$ lần lượt tại $A, B$. Cặp góc nào sau đây là cặp góc so le trong?\\
\begin{tabularx}{\linewidth}{X X}
A. $\widehat{A}_1$ và $\widehat{B}_1$ & B. $\widehat{A}_4$ và $\widehat{B}_1$ \\
C. $\widehat{A}_4$ và $\widehat{B}_2$ & D. $\widehat{A}_2$ và $\widehat{A}_4$
\end{tabularx}
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.75, line cap=round, line join=round]
  \draw[very thick] (-1.9, 0.9) -- (1.9, 0.9) node[right] {$a$};
  \draw[very thick] (-1.9, -0.7) -- (1.9, -0.7) node[right] {$b$};
  \coordinate (A) at (0.4, 0.9);
  \coordinate (B) at (-0.3, -0.7);
  \draw[very thick] ($ (B) - (0.35, 0.65) $) -- ($ (A) + (0.35, 0.65) $) node[above] {$c$};
  \fill (A) circle (1.8pt);
  \fill (B) circle (1.8pt);
  \node[above=6pt] at (A) {$A$};
  \node[below=6pt] at (B) {$B$};
  \node at ($ (A) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (A) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (A) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (A) + (0.42, -0.28) $) {\small $4$};
  \node at ($ (B) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (B) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (B) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (B) + (0.42, -0.28) $) {\small $4$};
\end{tikzpicture}
\end{minipage}

\newpage
\noindent\textbf{\large PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm).}
\vspace{0.5mm}

\noindent\textit{Thí sinh trả lời từ câu 13 đến câu 14. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}

\vspace{1mm}
\noindent\textbf{Câu 13.} Cho các số thực $a = \sqrt{2}$; $b = -\dfrac{5}{3}$; $c = 1,(3)$; $d = |-1,5|$.\\
\begin{tabularx}{\linewidth}{X X}
\textbf{a)} $a$ là số hữu tỉ. & \textbf{b)} $c$ là số thập phân VHTH có chu kì là 3. \\
\textbf{c)} $b < d < a$. & \textbf{d)} Giá trị của $x$ thỏa mãn $\left|x - \dfrac{1}{2}\right| = d$ là $x = 2$ và $x = -1$.
\end{tabularx}

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 14.} Cho hình bên, đường thẳng $a$ và $b$ cùng vuông góc với $c$; đường thẳng $d$ cắt $a, b$ tại $M, N$ và $\widehat{M}_1 = 50^\circ$.\\
\textbf{a)} $\widehat{M}_3 = 50^\circ$.\hfill\textbf{b)} $a \parallel b$.\\
\textbf{c)} $\widehat{N}_2 = 50^\circ$.\hfill\textbf{d)} Tia phân giác góc $M_3$ cắt $b$ tại $P$. Khi đó $\widehat{MPN} = 50^\circ$.
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.72, line cap=round, line join=round]
  \draw[very thick] (-1.7, -1.2) -- (-1.7, 1.4) node[left] {$c$};
  \draw[very thick] (-2.1, 0.9) -- (1.8, 0.9) node[right] {$a$};
  \draw[very thick] (-2.1, -0.7) -- (1.8, -0.7) node[right] {$b$};
  \draw[thick] (-1.7, 0.9) rectangle ++(0.18, -0.18);
  \draw[thick] (-1.7, -0.7) rectangle ++(0.18, 0.18);
  \coordinate (M) at (0.4, 0.9);
  \coordinate (N) at (-0.3, -0.7);
  \draw[very thick] ($ (N) - (0.35, 0.65) $) -- ($ (M) + (0.35, 0.65) $) node[above right] {$d$};
  \fill (M) circle (1.8pt);
  \fill (N) circle (1.8pt);
  \node[above=6pt] at (M) {$M$};
  \node[below=6pt] at (N) {$N$};
  \node at ($ (M) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (M) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (M) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (M) + (0.42, -0.28) $) {\small $4$};
  \node at ($ (N) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (N) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (N) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (N) + (0.42, -0.28) $) {\small $4$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\noindent\textbf{\large PHẦN III. Câu trắc nghiệm trả lời ngắn (2,0 điểm).}
\vspace{0.5mm}

\noindent\textit{Thí sinh trả lời từ câu 15 đến câu 18.}

\vspace{1mm}
\noindent\textbf{Câu 15.} Tính giá trị của biểu thức $\sqrt{49} - \sqrt{16}$.\hfill
\textbf{Câu 16.} Tìm $x$, biết $\dfrac{3}{5}x + \dfrac{1}{4} = -\dfrac{7}{20}$.

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 17.} Cho hình bên, biết $a \parallel b$, đường thẳng $c$ cắt $a, b$ lần lượt tại $E, F$ và $\widehat{E}_1 = 72^\circ$. Tính số đo góc $F_2$ (đơn vị: độ).\\
\textbf{Câu 18.} Một mảnh vườn hình vuông có diện tích $150\text{ m}^2$. Bác An làm hàng rào bao quanh mảnh vườn (không để lối đi). Tính độ dài hàng rào (đơn vị: mét, làm tròn đến hàng đơn vị).
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.72, line cap=round, line join=round]
  \draw[very thick] (-1.9, 0.9) -- (1.9, 0.9) node[right] {$a$};
  \draw[very thick] (-1.9, -0.7) -- (1.9, -0.7) node[right] {$b$};
  \coordinate (E) at (0.4, 0.9);
  \coordinate (F) at (-0.3, -0.7);
  \draw[very thick] ($ (F) - (0.35, 0.65) $) -- ($ (E) + (0.35, 0.65) $) node[above] {$c$};
  \fill (E) circle (1.8pt);
  \fill (F) circle (1.8pt);
  \node[above=6pt] at (E) {$E$};
  \node[below=6pt] at (F) {$F$};
  \node at ($ (E) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (E) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (E) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (E) + (0.42, -0.28) $) {\small $4$};
  \node at ($ (F) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (F) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (F) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (F) + (0.42, -0.28) $) {\small $4$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\noindent\textbf{\large PHẦN IV. Tự luận (3,0 điểm).}
\vspace{1mm}

\noindent\textbf{Câu 19 (1,0 điểm).} a) Tính hợp lí: $\dfrac{5}{7} \cdot \dfrac{3}{11} + \dfrac{5}{7} \cdot \dfrac{8}{11} - \dfrac{12}{7}$. \quad b) Tìm $x$, biết $\left(x - \dfrac{1}{2}\right)^2 = \dfrac{9}{16}$.

\vspace{1mm}
\noindent\textbf{Câu 20 (1,0 điểm).} Một cửa hàng nhập về $120\text{ kg}$ gạo. Ngày thứ nhất bán được $\dfrac{1}{4}$ số gạo, ngày thứ hai bán được $\dfrac{2}{3}$ số gạo còn lại.\\
\textbf{a)} Sau hai ngày, cửa hàng còn lại bao nhiêu ki-lô-gam gạo?\\
\textbf{b)} Ngày thứ ba, cửa hàng bán hết số gạo còn lại với giá giảm 10\% so với giá niêm yết là $18\,000$ đồng/kg. Tính số tiền cửa hàng thu được trong ngày thứ ba.

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.64\linewidth}
\textbf{Câu 21 (1,0 điểm).} Cho hình bên, đường thẳng $AB$ cắt hai đường thẳng $xx'$ và $yy'$ lần lượt tại $A$ và $B$; biết $\widehat{xAB} = 120^\circ, \widehat{ABy} = 60^\circ$.\\
\textbf{a)} Chứng minh $xx' \parallel yy'$.\\
\textbf{b)} Vẽ tia $At$ là tia phân giác của góc $\widehat{xAB}$, tia $Bz$ là tia phân giác của góc $\widehat{ABy'}$ (như hình bên). Chứng minh $At \parallel Bz$.
\end{minipage}
\hfill
\begin{minipage}[m]{0.34\linewidth}
\centering
\begin{tikzpicture}[scale=0.82, line cap=round, line join=round]
  \coordinate (X) at (-2.0, 0.9);
  \coordinate (Xp) at (2.0, 0.9);
  \coordinate (Y) at (-2.0, -0.8);
  \coordinate (Yp) at (2.0, -0.8);
  \draw[very thick] (X) node[left] {$x$} -- (Xp) node[right] {$x'$};
  \draw[very thick] (Y) node[left] {$y$} -- (Yp) node[right] {$y'$};
  \coordinate (A) at (-0.3, 0.9);
  \coordinate (B) at (0.5, -0.8);
  \draw[very thick] ($ (A)!-0.35!(B) $) -- ($ (B)!-0.35!(A) $);
  \fill (A) circle (1.8pt) node[above right=3pt] {$A$};
  \fill (B) circle (1.8pt) node[below left=3pt] {$B$};
  \draw[thick] ($ (A) + (-0.35, 0) $) arc (180:295:0.35);
  \node at ($ (A) + (-0.72, -0.28) $) {\small $120^\circ$};
  \draw[thick] ($ (B) + (-0.32, 0) $) arc (180:115:0.32);
  \node at ($ (B) + (-0.55, 0.3) $) {\small $60^\circ$};
  \coordinate (T) at (-1.3, -0.8);
  \coordinate (Z) at (1.5, 0.9);
  \draw[very thick, dashed] (A) -- (T);
  \node[above=2pt] at (T) {$t$};
  \draw[very thick, dashed] (B) -- (Z);
  \node[above=2pt] at (Z) {$z$};
\end{tikzpicture}
\end{minipage}

\vfill
\begin{center}
\textbf{--------- HẾT ---------}\\
\textit{(Giáo viên coi kiểm tra không giải thích gì thêm)}
\end{center}

\end{document}
'''

# ==============================================================================
# 3. FILE: dap_an_de_01.tex
# ==============================================================================

DAP_AN_01_TEX = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage[top=1.0cm, bottom=1.0cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\rfoot{\small\textit{Trang \thepage}}
\lfoot{\small\textit{Hướng dẫn chấm -- Đề 1 (Toán 7, Giữa HK I)}}
\renewcommand{\headrulewidth}{0pt}

\newcolumntype{Y}{>{\centering\arraybackslash}X}

\begin{document}

\begin{center}
  \textbf{\large ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM -- ĐỀ 1}\\[1mm]
  \textbf{\large KIỂM TRA GIỮA HỌC KÌ I -- MÔN TOÁN 7 -- NĂM HỌC 2026 -- 2027}
\end{center}

\vspace{1mm}
\noindent\textbf{\large PHẦN I. (3,0 điểm) Mỗi câu trả lời đúng được 0,25 điểm.}
\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|c|*{12}{Y|}}
\hline
\textbf{Câu} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\ \hline
\textbf{Đáp án} & \textbf{B} & \textbf{A} & \textbf{D} & \textbf{C} & \textbf{B} & \textbf{A} & \textbf{D} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textbf{\large PHẦN II. (2,0 điểm)}
\vspace{0.5mm}

\noindent\textit{Quy tắc chấm: Đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng 4 ý được 1,0đ.}

\vspace{1mm}
\noindent
\begin{tabularx}{\linewidth}{|c|c|c|X|}
\hline
\textbf{Câu} & \textbf{Ý} & \textbf{Đáp án} & \textbf{Giải thích tóm tắt} \\ \hline
\multirow{4}{*}{\textbf{13}} & a) & \textbf{Sai} & $\sqrt{2}$ là số vô tỉ, không phải số hữu tỉ. \\ \cline{2-4}
& b) & \textbf{Đúng} & $1,(3) = 1,333\dots$ có chu kì là 3. \\ \cline{2-4}
& c) & \textbf{Sai} & $b \approx -1,67; d = 1,5; a \approx 1,414 \Rightarrow b < a < d$. \\ \cline{2-4}
& d) & \textbf{Đúng} & $x - 1/2 = 1,5 \Rightarrow x = 2$ hoặc $x - 1/2 = -1,5 \Rightarrow x = -1$. \\ \hline
\multirow{4}{*}{\textbf{14}} & a) & \textbf{Đúng} & $\widehat{M}_3$ và $\widehat{M}_1$ là hai góc đối đỉnh. \\ \cline{2-4}
& b) & \textbf{Đúng} & Cùng vuông góc với đường thẳng thứ ba thì song song. \\ \cline{2-4}
& c) & \textbf{Sai} & $\widehat{M}_2 = 180^\circ - 50^\circ = 130^\circ \Rightarrow \widehat{N}_2 = 130^\circ$ (đồng vị). \\ \cline{2-4}
& d) & \textbf{Sai} & $\widehat{M}_3 = 50^\circ$; tia phân giác tạo góc $25^\circ \Rightarrow \widehat{MPN} = 25^\circ$ (so le trong). \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textbf{\large PHẦN III. (2,0 điểm) Mỗi câu đúng được 0,5 điểm.}
\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|c|c|X|}
\hline
\textbf{Câu} & \textbf{Đáp án} & \textbf{Hướng dẫn giải tóm tắt} \\ \hline
\textbf{15} & \textbf{3} & $\sqrt{49} - \sqrt{16} = 7 - 4 = 3$. \\ \hline
\textbf{16} & \textbf{-1} & $\dfrac{3}{5}x = -\dfrac{7}{20} - \dfrac{5}{20} = -\dfrac{3}{5} \Rightarrow x = -1$. \\ \hline
\textbf{17} & \textbf{108} & $a \parallel b \Rightarrow \widehat{F}_1 = \widehat{E}_1 = 72^\circ$ (đồng vị); $\widehat{F}_2 = 180^\circ - 72^\circ = 108^\circ$ (kề bù). \\ \hline
\textbf{18} & \textbf{49} & Cạnh mảnh vườn: $\sqrt{150} \approx 12,247\text{ m}$. Hàng rào: $4\sqrt{150} \approx 48,99 \approx 49\text{ m}$. \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textbf{\large PHẦN IV. Tự luận (3,0 điểm)}
\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|c|c|X|c|}
\hline
\textbf{Câu} & \textbf{Ý} & \textbf{Nội dung lời giải} & \textbf{Điểm} \\ \hline
\multirow{4}{*}{\textbf{19}} & \multirow{2}{*}{a)} & $\dfrac{5}{7} \cdot \dfrac{3}{11} + \dfrac{5}{7} \cdot \dfrac{8}{11} - \dfrac{12}{7} = \dfrac{5}{7} \cdot \left(\dfrac{3}{11} + \dfrac{8}{11}\right) - \dfrac{12}{7}$ & 0,25 đ \\ \cline{3-4}
& & $= \dfrac{5}{7} \cdot 1 - \dfrac{12}{7} = \dfrac{5 - 12}{7} = -1$. & 0,25 đ \\ \cline{2-4}
& \multirow{2}{*}{b)} & $\left(x - \dfrac{1}{2}\right)^2 = \dfrac{9}{16} \Rightarrow x - \dfrac{1}{2} = \dfrac{3}{4}$ hoặc $x - \dfrac{1}{2} = -\dfrac{3}{4}$. & 0,25 đ \\ \cline{3-4}
& & Với $x - \dfrac{1}{2} = \dfrac{3}{4} \Rightarrow x = \dfrac{5}{4}$; với $x - \dfrac{1}{2} = -\dfrac{3}{4} \Rightarrow x = -\dfrac{1}{4}$. Vậy $x \in \left\{\dfrac{5}{4}; -\dfrac{1}{4}\right\}$. & 0,25 đ \\ \hline

\multirow{4}{*}{\textbf{20}} & \multirow{2}{*}{a)} & Ngày 1 bán: $120 \cdot \dfrac{1}{4} = 30\text{ kg}$, còn lại $120 - 30 = 90\text{ kg}$.\newline Ngày 2 bán: $90 \cdot \dfrac{2}{3} = 60\text{ kg}$. & 0,25 đ \\ \cline{3-4}
& & Sau hai ngày, cửa hàng còn lại: $90 - 60 = 30\text{ (kg)}$. & 0,25 đ \\ \cline{2-4}
& \multirow{2}{*}{b)} & Giá bán mỗi kg ngày thứ ba: $18\,000 \cdot (100\% - 10\%) = 16\,200\text{ (đồng/kg)}$. & 0,25 đ \\ \cline{3-4}
& & Số tiền thu được trong ngày thứ ba: $30 \cdot 16\,200 = 486\,000\text{ (đồng)}$. & 0,25 đ \\ \hline

\multirow{4}{*}{\textbf{21}} & \multirow{2}{*}{a)} & Ta có $\widehat{x'AB} = 180^\circ - \widehat{xAB} = 180^\circ - 120^\circ = 60^\circ$ (hai góc kề bù). & 0,25 đ \\ \cline{3-4}
& & Mà $\widehat{x'AB} = \widehat{ABy} = 60^\circ$, hai góc này ở vị trí so le trong nên $xx' \parallel yy'$. & 0,25 đ \\ \cline{2-4}
& \multirow{2}{*}{b)} & Tia $At$ là phân giác của $\widehat{xAB} \Rightarrow \widehat{tAB} = \dfrac{1}{2}\widehat{xAB} = 60^\circ$.\newline Tia $Bz$ là phân giác của $\widehat{ABy'} \Rightarrow \widehat{ABz} = \dfrac{1}{2}\widehat{ABy'} = \dfrac{1}{2}(180^\circ - 60^\circ) = 60^\circ$. & 0,25 đ \\ \cline{3-4}
& & Do đó $\widehat{tAB} = \widehat{ABz} = 60^\circ$, mà hai góc này ở vị trí so le trong nên $At \parallel Bz$. & 0,25 đ \\ \hline
\end{tabularx}

\end{document}
'''

# ==============================================================================
# 4. FILE: de_02.tex (Gọn gàng chính xác 2 trang A4, TikZ cực nét)
# ==============================================================================

DE_02_TEX = r'''\documentclass[10.5pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage[top=0.9cm, bottom=0.9cm, left=1.1cm, right=1.1cm]{geometry}
\usepackage{fancyhdr}
\usepackage{enumitem}

\pagestyle{fancy}
\fancyhf{}
\rfoot{\small\textit{Trang \thepage/2}}
\lfoot{\small\textit{Đề kiểm tra Giữa học kì I -- Môn Toán 7 -- Đề 2}}
\renewcommand{\headrulewidth}{0pt}

\setlength{\parskip}{0.5pt}

\begin{document}

\noindent
\begin{tabularx}{\linewidth}{X r}
\textbf{TRƯỜNG THCS \dots\dots\dots\dots\dots\dots} & \textbf{ĐỀ KIỂM TRA GIỮA HỌC KÌ I -- NĂM HỌC 2026 -- 2027} \\
\textbf{TỔ: \dots\dots\dots\dots\dots\dots} & \textbf{Môn: TOÁN -- Lớp 7} \\
\textit{(Đề 2 -- gồm 02 trang)} & \textit{Thời gian làm bài: 90 phút (không kể thời gian giao đề)} \\
\end{tabularx}

\vspace{1mm}
\noindent
\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{
\textbf{Họ và tên học sinh:} \dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots\dots \textbf{Lớp:} \dots\dots\dots \textbf{Số báo danh:} \dots\dots\dots
}}

\vspace{1.5mm}
\noindent\textbf{\large PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (3,0 điểm).}
\vspace{0.5mm}

\noindent\textit{Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án.}

\vspace{1mm}
\noindent\textbf{Câu 1.} Tập hợp các số hữu tỉ được kí hiệu là\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\mathbb{N}$ & B. $\mathbb{Z}$ & C. $\mathbb{Q}$ & D. $\mathbb{R}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 2.} Trong các số hữu tỉ $-\dfrac{2}{3}; \dfrac{1}{2}; -\dfrac{3}{4}; 0$, số nhỏ nhất là\\
\begin{tabularx}{\linewidth}{X X X X}
A. $-\dfrac{2}{3}$ & B. $-\dfrac{3}{4}$ & C. $0$ & D. $\dfrac{1}{2}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 3.} Với $x$ là số hữu tỉ, $(x^3)^4$ bằng\\
\begin{tabularx}{\linewidth}{X X X X}
A. $x^{12}$ & B. $x^7$ & C. $x^{81}$ & D. $x^{64}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 4.} Bỏ dấu ngoặc trong biểu thức $\dfrac{1}{3} - \left(\dfrac{1}{2} - \dfrac{1}{4}\right)$ ta được\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\dfrac{1}{3} - \dfrac{1}{2} - \dfrac{1}{4}$ & B. $\dfrac{1}{3} + \dfrac{1}{2} - \dfrac{1}{4}$ & C. $\dfrac{1}{3} + \dfrac{1}{2} + \dfrac{1}{4}$ & D. $\dfrac{1}{3} - \dfrac{1}{2} + \dfrac{1}{4}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 5.} Số thập phân vô hạn tuần hoàn $2,1(6)$ có chu kì là\\
\begin{tabularx}{\linewidth}{X X X X}
A. $1$ & B. $16$ & C. $6$ & D. $21$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 6.} Khẳng định nào sau đây đúng?\\
\begin{tabularx}{\linewidth}{X X X X}
A. $\sqrt{81} = -9$ & B. $\sqrt{81} = 9$ & C. $\sqrt{81} = \pm 9$ & D. $\sqrt{81} = 40,5$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 7.} Giá trị tuyệt đối của số thực $-\sqrt{3}$ là\\
\begin{tabularx}{\linewidth}{X X X X}
A. $-\sqrt{3}$ & B. $3$ & C. $-3$ & D. $\sqrt{3}$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 8.} Làm tròn số $-12,4578$ với độ chính xác $0,05$ ta được\\
\begin{tabularx}{\linewidth}{X X X X}
A. $-12,5$ & B. $-12,4$ & C. $-12,46$ & D. $-12,45$
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 9.} Tia $Oz$ là tia phân giác của góc $xOy$ khi\\
\begin{tabularx}{\linewidth}{X X}
A. $Oz \perp Ox$. & B. $Oz$ nằm giữa $Ox$ và $Oy$. \\
C. $Oz$ nằm giữa $Ox, Oy$ và $\widehat{xOz} = \widehat{zOy}$. & D. $\widehat{xOz} + \widehat{zOy} = \widehat{xOy}$.
\end{tabularx}

\vspace{1mm}
\noindent\textbf{Câu 10.} Đường thẳng $c$ cắt hai đường thẳng song song $a$ và $b$. Khẳng định nào sau đây đúng?\\
\begin{tabularx}{\linewidth}{X X}
A. Hai góc so le trong bù nhau. & B. Hai góc đồng vị bằng nhau. \\
C. Hai góc trong cùng phía bằng nhau. & D. Hai góc đồng vị bù nhau.
\end{tabularx}

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 11.} Cho hình bên, tia $Ot$ là tia phân giác của góc $xOy$ và $\widehat{xOy} = 130^\circ$. Số đo góc $xOt$ là\\
\begin{tabularx}{\linewidth}{X X}
A. $130^\circ$ & B. $50^\circ$ \\
C. $115^\circ$ & D. $65^\circ$
\end{tabularx}
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]
  \coordinate (O) at (0,0);
  \coordinate (X) at (1.9,0);
  \coordinate (Y) at ({1.8*cos(130)}, {1.8*sin(130)});
  \coordinate (T) at ({1.8*cos(65)}, {1.8*sin(65)});
  \draw[very thick] (O) -- (X) node[right] {$x$};
  \draw[very thick] (O) -- (Y) node[above left] {$y$};
  \draw[very thick] (O) -- (T) node[above right] {$t$};
  \fill (O) circle (1.8pt) node[below=2pt] {$O$};
  \draw[thick] (0.55,0) arc (0:130:0.55);
  \draw[thick] (0.38,0) arc (0:65:0.38);
  \node at (100:0.9) {\small $130^\circ$};
\end{tikzpicture}
\end{minipage}

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 12.} Cho hình bên, đường thẳng $c$ cắt hai đường thẳng $a, b$ lần lượt tại $A, B$. Cặp góc nào sau đây là cặp góc đồng vị?\\
\begin{tabularx}{\linewidth}{X X}
A. $\widehat{A}_2$ và $\widehat{B}_2$ & B. $\widehat{A}_3$ và $\widehat{B}_1$ \\
C. $\widehat{A}_4$ và $\widehat{B}_1$ & D. $\widehat{A}_1$ và $\widehat{A}_3$
\end{tabularx}
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.75, line cap=round, line join=round]
  \draw[very thick] (-1.9, 0.9) -- (1.9, 0.9) node[right] {$a$};
  \draw[very thick] (-1.9, -0.7) -- (1.9, -0.7) node[right] {$b$};
  \coordinate (A) at (-0.3, 0.9);
  \coordinate (B) at (0.4, -0.7);
  \draw[very thick] ($ (A) + (-0.32, 0.72) $) node[above] {$c$} -- ($ (B) + (0.32, -0.72) $);
  \fill (A) circle (1.8pt);
  \fill (B) circle (1.8pt);
  \node at ($ (A) + (-0.62, 0.30) $) {$A$};
  \node at ($ (B) + (0.62, -0.30) $) {$B$};
  \node at ($ (A) + (0.35, 0.25) $) {\small $1$};
  \node at ($ (A) + (-0.32, 0.20) $) {\small $2$};
  \node at ($ (A) + (-0.35, -0.22) $) {\small $3$};
  \node at ($ (A) + (0.35, -0.22) $) {\small $4$};
  \node at ($ (B) + (0.35, 0.25) $) {\small $1$};
  \node at ($ (B) + (-0.35, 0.20) $) {\small $2$};
  \node at ($ (B) + (-0.35, -0.22) $) {\small $3$};
  \node at ($ (B) + (0.32, -0.20) $) {\small $4$};
\end{tikzpicture}
\end{minipage}

\newpage
\noindent\textbf{\large PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm).}
\vspace{0.5mm}

\noindent\textit{Thí sinh trả lời từ câu 13 đến câu 14. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}

\vspace{1mm}
\noindent\textbf{Câu 13.} Cho các số thực $x = -\sqrt{7}$; $y = \dfrac{7}{11}$; $z = -2,6$; $t = \left|-\dfrac{5}{2}\right|$.\\
\begin{tabularx}{\linewidth}{X X}
\textbf{a)} $x$ là số vô tỉ. & \textbf{b)} $y = 0,6(3)$. \\
\textbf{c)} $z < x < t$. & \textbf{d)} Tổng các giá trị của $m$ thỏa mãn $|m + 1| = t$ bằng $-2$.
\end{tabularx}

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 14.} Cho hình bên, đường thẳng $c$ cắt hai đường thẳng $a, b$ lần lượt tại $M, N$; biết $\widehat{M}_2 = 115^\circ$ và $\widehat{N}_1 = 65^\circ$.\\
\textbf{a)} $\widehat{M}_1$ và $\widehat{M}_2$ là hai góc kề bù.\\
\textbf{b)} $\widehat{M}_1$ và $\widehat{N}_1$ là hai góc so le trong.\\
\textbf{c)} $a \parallel b$.\\
\textbf{d)} Tia phân giác của góc $M_3$ cắt đường thẳng $b$ tại $P$. Khi đó $\widehat{MPN} = 32,5^\circ$.
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.72, line cap=round, line join=round]
  \draw[very thick] (-1.9, 0.9) -- (1.9, 0.9) node[right] {$a$};
  \draw[very thick] (-1.9, -0.7) -- (1.9, -0.7) node[right] {$b$};
  \coordinate (M) at (0.4, 0.9);
  \coordinate (N) at (-0.3, -0.7);
  \draw[very thick] ($ (N) - (0.35, 0.65) $) -- ($ (M) + (0.35, 0.65) $) node[above] {$c$};
  \fill (M) circle (1.8pt);
  \fill (N) circle (1.8pt);
  \node[above=6pt] at (M) {$M$};
  \node[below=6pt] at (N) {$N$};
  \node at ($ (M) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (M) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (M) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (M) + (0.42, -0.28) $) {\small $4$};
  \node at ($ (N) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (N) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (N) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (N) + (0.42, -0.28) $) {\small $4$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\noindent\textbf{\large PHẦN III. Câu trắc nghiệm trả lời ngắn (2,0 điểm).}
\vspace{0.5mm}

\noindent\textit{Thí sinh trả lời từ câu 15 đến câu 18.}

\vspace{1mm}
\noindent\textbf{Câu 15.} Tính giá trị của biểu thức $3\sqrt{16} - \sqrt{121}$.\hfill
\textbf{Câu 16.} Tìm $x$, biết $\dfrac{1}{2} - \dfrac{2}{3}x = -\dfrac{5}{6}$.

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.65\linewidth}
\textbf{Câu 17.} Cho hình bên, biết $a \parallel b$, đường thẳng $c$ cắt $a, b$ lần lượt tại $H, K$ và $\widehat{H}_2 = 125^\circ$. Tính số đo góc $K_1$ (đơn vị: độ).\\
\textbf{Câu 18.} Một tấm bìa hình vuông có diện tích $75\text{ cm}^2$. Bạn Lan dán một sợi ruy băng sát theo bốn cạnh của tấm bìa. Tính độ dài sợi ruy băng (đơn vị: xăng-ti-mét, làm tròn đến hàng đơn vị).
\end{minipage}
\hfill
\begin{minipage}[m]{0.33\linewidth}
\centering
\begin{tikzpicture}[scale=0.72, line cap=round, line join=round]
  \draw[very thick] (-1.9, 0.9) -- (1.9, 0.9) node[right] {$a$};
  \draw[very thick] (-1.9, -0.7) -- (1.9, -0.7) node[right] {$b$};
  \coordinate (H) at (0.4, 0.9);
  \coordinate (K) at (-0.3, -0.7);
  \draw[very thick] ($ (K) - (0.35, 0.65) $) -- ($ (H) + (0.35, 0.65) $) node[above] {$c$};
  \fill (H) circle (1.8pt);
  \fill (K) circle (1.8pt);
  \node[above=6pt] at (H) {$H$};
  \node[below=6pt] at (K) {$K$};
  \node at ($ (H) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (H) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (H) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (H) + (0.42, -0.28) $) {\small $4$};
  \node at ($ (K) + (0.42, 0.28) $) {\small $1$};
  \node at ($ (K) + (-0.42, 0.28) $) {\small $2$};
  \node at ($ (K) + (-0.42, -0.28) $) {\small $3$};
  \node at ($ (K) + (0.42, -0.28) $) {\small $4$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\noindent\textbf{\large PHẦN IV. Tự luận (3,0 điểm).}
\vspace{1mm}

\noindent\textbf{Câu 19 (1,0 điểm).} a) Tính hợp lí: $\dfrac{4}{9} \cdot \dfrac{13}{5} - \dfrac{4}{9} \cdot \dfrac{8}{5} + \dfrac{5}{9}$. \quad b) Tìm $x$, biết $\left(2x + \dfrac{1}{3}\right)^2 = \dfrac{25}{9}$.

\vspace{1mm}
\noindent\textbf{Câu 20 (1,0 điểm).} Thư viện trường có 240 quyển truyện. Lớp 7A mượn $\dfrac{1}{3}$ số truyện, lớp 7B mượn $\dfrac{3}{8}$ số truyện còn lại.\\
\textbf{a)} Sau khi hai lớp mượn, thư viện còn lại bao nhiêu quyển truyện?\\
\textbf{b)} Nhà trường mua thêm một số quyển truyện bằng $\dfrac{2}{5}$ số truyện còn lại ở câu a). Giá bìa mỗi quyển là $50\,000$ đồng và được giảm 12\% giá bìa. Tính số tiền nhà trường phải trả.

\vspace{1mm}
\noindent
\begin{minipage}[m]{0.64\linewidth}
\textbf{Câu 21 (1,0 điểm).} Cho hình bên, đường thẳng $AB$ cắt hai đường thẳng $mm'$ và $nn'$ lần lượt tại $A$ và $B$; biết $\widehat{mAB} = 110^\circ, \widehat{ABn} = 70^\circ$.\\
\textbf{a)} Chứng minh $mm' \parallel nn'$. \\
\textbf{b)} Đường thẳng $d$ đi qua $A$ và vuông góc với $mm'$, cắt $nn'$ tại $C$ (như hình bên). Chứng minh $d \perp nn'$ và tính số đo góc $BAC$.
\end{minipage}
\hfill
\begin{minipage}[m]{0.34\linewidth}
\centering
\begin{tikzpicture}[scale=0.82, line cap=round, line join=round]
  \coordinate (M) at (-2.0, 0.9);
  \coordinate (Mp) at (2.0, 0.9);
  \coordinate (N) at (-2.0, -0.8);
  \coordinate (Np) at (2.0, -0.8);
  \draw[very thick] (M) node[left] {$m$} -- (Mp) node[right] {$m'$};
  \draw[very thick] (N) node[left] {$n$} -- (Np) node[right] {$n'$};
  \coordinate (A) at (-0.4, 0.9);
  \coordinate (B) at (0.6, -0.8);
  \coordinate (C) at (-0.4, -0.8);
  \draw[very thick] ($ (A)!-0.35!(B) $) -- ($ (B)!-0.35!(A) $);
  \draw[very thick, dashed] (A) -- (C);
  \draw[very thick] ($ (A) + (0, 0.45) $) node[above] {$d$} -- (A);
  \draw[very thick] (C) -- ($ (C) + (0, -0.28) $);
  \draw[thick] (A) rectangle ++(-0.18, -0.18);
  \fill (A) circle (1.8pt) node[above right=3pt] {$A$};
  \fill (B) circle (1.8pt) node[below right=3pt] {$B$};
  \fill (C) circle (1.8pt) node[below left=3pt] {$C$};
  \draw[thick] ($ (A) + (-0.35, 0) $) arc (180:300:0.35);
  \node at ($ (A) + (-0.72, -0.32) $) {\small $110^\circ$};
  \draw[thick] ($ (B) + (-0.35, 0) $) arc (180:120:0.35);
  \node at (0.1, -0.45) {\small $70^\circ$};
\end{tikzpicture}
\end{minipage}

\vfill
\begin{center}
\textbf{--------- HẾT ---------}\\
\textit{(Giáo viên coi kiểm tra không giải thích gì thêm)}
\end{center}

\end{document}
'''

# ==============================================================================
# 5. FILE: dap_an_de_02.tex
# ==============================================================================

DAP_AN_02_TEX = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage[top=1.0cm, bottom=1.0cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\rfoot{\small\textit{Trang \thepage}}
\lfoot{\small\textit{Hướng dẫn chấm -- Đề 2 (Toán 7, Giữa HK I)}}
\renewcommand{\headrulewidth}{0pt}

\newcolumntype{Y}{>{\centering\arraybackslash}X}

\begin{document}

\begin{center}
  \textbf{\large ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM -- ĐỀ 2}\\[1mm]
  \textbf{\large KIỂM TRA GIỮA HỌC KÌ I -- MÔN TOÁN 7 -- NĂM HỌC 2026 -- 2027}
\end{center}

\vspace{1mm}
\noindent\textbf{\large PHẦN I. (3,0 điểm) Mỗi câu trả lời đúng được 0,25 điểm.}
\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|c|*{12}{Y|}}
\hline
\textbf{Câu} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\ \hline
\textbf{Đáp án} & \textbf{C} & \textbf{B} & \textbf{A} & \textbf{D} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} & \textbf{C} & \textbf{B} & \textbf{D} & \textbf{A} \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textbf{\large PHẦN II. (2,0 điểm)}
\vspace{0.5mm}

\noindent\textit{Quy tắc chấm: Đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng 4 ý được 1,0đ.}

\vspace{1mm}
\noindent
\begin{tabularx}{\linewidth}{|c|c|c|X|}
\hline
\textbf{Câu} & \textbf{Ý} & \textbf{Đáp án} & \textbf{Giải thích tóm tắt} \\ \hline
\multirow{4}{*}{\textbf{13}} & a) & \textbf{Đúng} & 7 không là bình phương của số hữu tỉ nên $\sqrt{7}$ và $x$ là số vô tỉ. \\ \cline{2-4}
& b) & \textbf{Sai} & $\dfrac{7}{11} = 0,(63)$, không phải $0,6(3)$. \\ \cline{2-4}
& c) & \textbf{Sai} & $x \approx -2,646 < z = -2,6 \Rightarrow x < z < t$. Khẳng định $z < x < t$ là sai. \\ \cline{2-4}
& d) & \textbf{Đúng} & $m + 1 = 2,5 \Rightarrow m = 1,5$ hoặc $m + 1 = -2,5 \Rightarrow m = -3,5$; tổng $= -2$. \\ \hline
\multirow{4}{*}{\textbf{14}} & a) & \textbf{Đúng} & $\widehat{M}_1$ và $\widehat{M}_2$ là hai góc kề bù (chung cạnh, hai cạnh kia đối nhau). \\ \cline{2-4}
& b) & \textbf{Sai} & $\widehat{M}_1$ và $\widehat{N}_1$ là cặp góc đồng vị, không phải so le trong. \\ \cline{2-4}
& c) & \textbf{Đúng} & $\widehat{M}_1 = 180^\circ - 115^\circ = 65^\circ = \widehat{N}_1$, hai góc đồng vị bằng nhau nên $a \parallel b$. \\ \cline{2-4}
& d) & \textbf{Đúng} & $\widehat{M}_3 = \widehat{M}_1 = 65^\circ$; tia phân giác tạo góc $32,5^\circ \Rightarrow \widehat{MPN} = 32,5^\circ$ (so le trong). \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textbf{\large PHẦN III. (2,0 điểm) Mỗi câu đúng được 0,5 điểm.}
\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|c|c|X|}
\hline
\textbf{Câu} & \textbf{Đáp án} & \textbf{Hướng dẫn giải tóm tắt} \\ \hline
\textbf{15} & \textbf{1} & $3\sqrt{16} - \sqrt{121} = 3 \cdot 4 - 11 = 1$. \\ \hline
\textbf{16} & \textbf{2} & $\dfrac{2}{3}x = \dfrac{1}{2} + \dfrac{5}{6} = \dfrac{4}{3} \Rightarrow x = 2$. \\ \hline
\textbf{17} & \textbf{55} & $a \parallel b \Rightarrow \widehat{K}_2 = \widehat{H}_2 = 125^\circ$ (đồng vị); $\widehat{K}_1 = 180^\circ - 125^\circ = 55^\circ$ (kề bù). \\ \hline
\textbf{18} & \textbf{35} & Cạnh tấm bìa: $\sqrt{75} \approx 8,66\text{ cm}$. Ruy băng: $4\sqrt{75} \approx 34,64 \approx 35\text{ cm}$. \\ \hline
\end{tabularx}

\vspace{2.5mm}
\noindent\textbf{\large PHẦN IV. Tự luận (3,0 điểm)}
\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|c|c|X|c|}
\hline
\textbf{Câu} & \textbf{Ý} & \textbf{Nội dung lời giải} & \textbf{Điểm} \\ \hline
\multirow{4}{*}{\textbf{19}} & \multirow{2}{*}{a)} & $\dfrac{4}{9} \cdot \dfrac{13}{5} - \dfrac{4}{9} \cdot \dfrac{8}{5} + \dfrac{5}{9} = \dfrac{4}{9} \cdot \left(\dfrac{13}{5} - \dfrac{8}{5}\right) + \dfrac{5}{9}$ & 0,25 đ \\ \cline{3-4}
& & $= \dfrac{4}{9} \cdot 1 + \dfrac{5}{9} = \dfrac{9}{9} = 1$. & 0,25 đ \\ \cline{2-4}
& \multirow{2}{*}{b)} & $\left(2x + \dfrac{1}{3}\right)^2 = \dfrac{25}{9} \Rightarrow 2x + \dfrac{1}{3} = \dfrac{5}{3}$ hoặc $2x + \dfrac{1}{3} = -\dfrac{5}{3}$. & 0,25 đ \\ \cline{3-4}
& & Với $2x + \dfrac{1}{3} = \dfrac{5}{3} \Rightarrow x = \dfrac{2}{3}$; với $2x + \dfrac{1}{3} = -\dfrac{5}{3} \Rightarrow x = -1$. Vậy $x \in \left\{\dfrac{2}{3}; -1\right\}$. & 0,25 đ \\ \hline

\multirow{4}{*}{\textbf{20}} & \multirow{2}{*}{a)} & Lớp 7A mượn: $240 \cdot \dfrac{1}{3} = 80\text{ (quyển)}$. Còn lại: $240 - 80 = 160\text{ (quyển)}$.\newline Lớp 7B mượn: $160 \cdot \dfrac{3}{8} = 60\text{ (quyển)}$. & 0,25 đ \\ \cline{3-4}
& & Sau hai lớp mượn, thư viện còn lại: $160 - 60 = 100\text{ (quyển)}$. & 0,25 đ \\ \cline{2-4}
& \multirow{2}{*}{b)} & Số truyện mua thêm: $100 \cdot \dfrac{2}{5} = 40\text{ (quyển)}$.\newline Giá mỗi quyển sau giảm 12\%: $50\,000 \cdot (100\% - 12\%) = 44\,000\text{ (đồng/quyển)}$. & 0,25 đ \\ \cline{3-4}
& & Số tiền nhà trường phải trả: $40 \cdot 44\,000 = 1\,760\,000\text{ (đồng)}$. & 0,25 đ \\ \hline

\multirow{4}{*}{\textbf{21}} & \multirow{2}{*}{a)} & Ta có $\widehat{ABn'} = 180^\circ - \widehat{ABn} = 180^\circ - 70^\circ = 110^\circ$ (hai góc kề bù). & 0,25 đ \\ \cline{3-4}
& & Mà $\widehat{mAB} = \widehat{ABn'} = 110^\circ$, hai góc này ở vị trí so le trong nên $mm' \parallel nn'$. & 0,25 đ \\ \cline{2-4}
& \multirow{2}{*}{b)} & Vì $d \perp mm'$ mà $mm' \parallel nn'$ nên $d \perp nn'$ (từ vuông góc đến song song). & 0,25 đ \\ \cline{3-4}
& & Ta có $\widehat{mAC} = 90^\circ$ (do $d \perp mm'$). Vì tia $AC$ nằm giữa hai tia $Am, AB$ nên:\newline $\widehat{BAC} = \widehat{mAB} - \widehat{mAC} = 110^\circ - 90^\circ = 20^\circ$. & 0,25 đ \\ \hline
\end{tabularx}

\end{document}
'''

files_to_write = {
    "ma_tran_va_dac_ta.tex": MA_TRAN_TEX,
    "de_01.tex": DE_01_TEX,
    "dap_an_de_01.tex": DAP_AN_01_TEX,
    "de_02.tex": DE_02_TEX,
    "dap_an_de_02.tex": DAP_AN_02_TEX,
}

for fname, content in files_to_write.items():
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"-> Đã ghi file: {fname}")

print("\nĐang tiến hành biên dịch pdflatex cho 5 file...")
for fname in files_to_write.keys():
    tex_path = os.path.join(OUT_DIR, fname)
    cmd = ["pdflatex", "-interaction=nonstopmode", fname]
    print(f"Biên dịch {fname}...", end=" ", flush=True)
    res = subprocess.run(cmd, cwd=OUT_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pdf_name = fname.replace(".tex", ".pdf")
    pdf_path = os.path.join(OUT_DIR, pdf_name)
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        print(f"THÀNH CÔNG! ({pdf_name} - {len(reader.pages)} trang)")
    else:
        print(f"THẤT BẠI! Lỗi biên dịch:")
        print(res.stdout[-400:])

print("\nHoàn tất toàn bộ quy trình xuất file LaTeX!")
