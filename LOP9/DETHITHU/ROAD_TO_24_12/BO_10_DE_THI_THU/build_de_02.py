import os
import subprocess
import fitz

folder = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU/DE_02'
os.makedirs(folder, exist_ok=True)

# 1. TEX EXAM
tex_exam = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[top=1.8cm, bottom=2.0cm, left=1.8cm, right=1.8cm]{geometry}

\setlength{\parskip}{3pt}
\setlength{\parindent}{0pt}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\lhead{\footnotesize \textbf{CHÙA HƯƠNG SƠN -- ÔN THI VÀO 10}}
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 02)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 02} & \textbf{MÔN: TOÁN -- LỚP 9} \\
\textit{(Đề thi gồm 03 trang)} & \textit{Thời gian làm bài: 90 phút (không kể thời gian phát đề)} \\
\end{tabular*}

\vspace{2mm}
\noindent
\rule{\linewidth}{0.8pt}

\vspace{1mm}
\noindent
Họ và tên thí sinh: \dotfill Số báo danh: \dotfill

\vspace{2mm}
\noindent
\textbf{\large I. TRẮC NGHIỆM KHÁCH QUAN (7,0 điểm)}

\vspace{1mm}
\noindent
\textbf{Phần 1. Trắc nghiệm nhiều lựa chọn (3,0 điểm).} \textit{Từ câu 1 đến câu 12, thí sinh chọn đáp án đúng nhất trong 4 đáp án A, B, C, D rồi ghi vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 1.} Giá trị của biểu thức $2\sqrt{27} - 3\sqrt{12} + \sqrt{75}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $5\sqrt{3}$. & \textbf{B.} $-5\sqrt{3}$. & \textbf{C.} $3\sqrt{3}$. & \textbf{D.} $0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Cho tam giác $DEF$ vuông tại $D$, góc nhọn $\widehat{F} = \alpha$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\sin \alpha = \dfrac{DE}{EF}$. & \textbf{B.} $\cos \alpha = \dfrac{DE}{EF}$. & \textbf{C.} $\tan \alpha = \dfrac{DF}{DE}$. & \textbf{D.} $\cot \alpha = \dfrac{DE}{DF}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x^2 - 4 \le 0$. & \textbf{B.} $0x + 8 > 0$. & \textbf{C.} $-3x + 9 \ge 0$. & \textbf{D.} $\dfrac{1}{x} + 2 < 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Nếu $x > y$ thì bất đẳng thức nào sau đây luôn đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-2x < -2y$. & \textbf{B.} $-2x > -2y$. & \textbf{C.} $x - 3 < y - 3$. & \textbf{D.} $3x + 1 < 3y + 1$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của số 100 là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $10$ và $-10$. & \textbf{B.} $10$. & \textbf{C.} $-10$. & \textbf{D.} $50$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Điều kiện xác định của căn thức $\sqrt{3x - 12}$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \ge 4$. & \textbf{B.} $x > 4$. & \textbf{C.} $x \le 4$. & \textbf{D.} $x < 4$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x < 2$, giá trị của biểu thức $\sqrt{(x-2)^2}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x - 2$. & \textbf{B.} $2 - x$. & \textbf{C.} $-(2-x)$. & \textbf{D.} $(x-2)^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của $\sqrt[3]{-216}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $6$. & \textbf{B.} $-6$. & \textbf{C.} $36$. & \textbf{D.} $-36$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Trong đường tròn $(O; R)$, công thức tính chu vi (độ dài) của đường tròn là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $C = 2\pi R$. & \textbf{B.} $C = \pi R$. & \textbf{C.} $C = \pi R^2$. & \textbf{D.} $C = 2\pi R^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 4\text{ cm})$ và đường thẳng $a$. Biết khoảng cách từ $O$ đến $a$ là $3\text{ cm}$. Vị trí tương đối của đường thẳng $a$ và đường tròn $(O)$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc nhau. & \textbf{B.} Cắt nhau. & \textbf{C.} Không giao nhau. & \textbf{D.} Trùng nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 6\text{ cm})$ và $(O'; 2\text{ cm})$. Biết khoảng cách giữa hai tâm $OO' = 8\text{ cm}$. Vị trí tương đối của hai đường tròn $(O)$ và $(O')$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc ngoài. & \textbf{B.} Tiếp xúc trong. & \textbf{C.} Cắt nhau. & \textbf{D.} Ở ngoài nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Trên đường tròn $(O)$, cho góc ở tâm $\widehat{COD} = 110^\circ$. Số đo của cung nhỏ $CD$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $55^\circ$. & \textbf{B.} $220^\circ$. & \textbf{C.} $110^\circ$. & \textbf{D.} $70^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Xét bài toán thực tế: ``Quãng đường $AB$ dài $180\text{ km}$. Lúc 7 giờ sáng, một ô tô khởi hành từ $A$ đi về $B$ với vận tốc $50\text{ km/h}$. Cùng lúc đó, một xe máy khởi hành từ $B$ đi về $A$ với vận tốc $40\text{ km/h}$. Coi hai xe chuyển động thẳng đều trên đoạn đường $AB$.''\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Sau 1 giờ kể từ lúc khởi hành, ô tô đi được quãng đường là $50\text{ km}$. & & \\
\hline
b) Hai xe gặp nhau tại thời điểm lúc 9 giờ sáng cùng ngày. & & \\
\hline
c) Địa điểm hai xe gặp nhau cách điểm $A$ một khoảng là $80\text{ km}$. & & \\
\hline
d) Sau 1,5 giờ kể từ lúc khởi hành, khoảng cách giữa hai xe là $45\text{ km}$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho đường tròn $(O; 5\text{ cm})$ và dây cung $AB = 8\text{ cm}$ không đi qua tâm $O$. Qua $O$ kẻ đường thẳng vuông góc với $AB$ tại $H$, đường thẳng này cắt tiếp tuyến tại $A$ của đường tròn $(O)$ tại điểm $C$.\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Điểm $H$ là trung điểm của đoạn thẳng $AB$ và $AH = 4\text{ cm}$. & & \\
\hline
b) Khoảng cách từ tâm $O$ đến dây cung $AB$ là $OH = 3\text{ cm}$. & & \\
\hline
c) Đoạn thẳng $CB$ là tiếp tuyến của đường tròn $(O)$. & & \\
\hline
d) Độ dài đoạn thẳng $OC$ bằng $8\text{ cm}$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Nghiệm của bất phương trình $2(x - 3) + 7 < 3(x + 1) - 4$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Giá trị của biểu thức $M = \sqrt{(\sqrt{5} - 3)^2} + \sqrt{5}$ bằng $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Từ đỉnh một ngọn hải đăng cao $50\text{ m}$ so với mực nước biển, một người quan sát nhìn thấy một con tàu dưới một góc hạ $30^\circ$ so với phương nằm ngang (xem hình vẽ bên). Hỏi khoảng cách từ chân ngọn hải đăng đến con tàu là bao nhiêu mét? (làm tròn kết quả đến hàng phần mười của mét).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Vách đá và hải đăng
  \fill[gray!30] (0,0) -- (0,2.5) -- (0.8,2.5) -- (0.8,0) -- cycle;
  \draw[thick] (0,0) -- (0,2.5) -- (0.8,2.5) -- (0.8,0);
  % Ngọn hải đăng
  \draw[thick, fill=orange!30] (0.2,2.5) rectangle (0.6,3.8);
  \node[left] at (0, 3.1) {$50\text{ m}$};
  % Mực nước biển
  \draw[thick, blue!80] (0.8,0) -- (4.8,0);
  \fill[blue!10] (0.8,-0.2) rectangle (4.8,0);
  % Con thuyền
  \draw[thick, fill=brown] (4.0,0) -- (4.4,0) -- (4.5,0.2) -- (3.9,0.2) -- cycle;
  \draw[thick] (4.2,0.2) -- (4.2,0.6);
  \draw[fill=white] (4.2,0.3) -- (4.5,0.4) -- (4.2,0.6) -- cycle;
  % Tia quan sát và phương ngang
  \draw[dashed] (0.6,3.8) -- (4.2,3.8);
  \draw[thick, red!80] (0.6,3.8) -- (4.2,0.2);
  \draw (1.5,3.8) arc (0:-35:0.9);
  \node at (1.9, 3.5) {\footnotesize $30^\circ$};
  % Góc vuông
  \draw (0.8,0) rectangle (1.1,0.3);
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một chiếc bánh pizza hình tròn có bán kính $R = 18\text{ cm}$ được cắt thành 8 miếng bằng nhau hình quạt tròn. Tính diện tích bề mặt của một miếng bánh pizza đó (lấy $\pi \approx 3{,}14$, làm tròn kết quả đến hàng phần mười, đơn vị: $\text{cm}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 2x - 3y = 1 \\ 3x + 2y = 8 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $B = \left( \dfrac{\sqrt{x}}{\sqrt{x}-2} - \dfrac{4}{x - 2\sqrt{x}} \right) : \dfrac{\sqrt{x}+2}{\sqrt{x}}$ với $x > 0, x \ne 4$. Rút gọn biểu thức $B$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho đường tròn $(O; R)$ và dây cung $AB$ không đi qua tâm $O$. Qua $O$ kẻ đường thẳng vuông góc với $AB$ tại $H$, đường thẳng này cắt tiếp tuyến tại $A$ của đường tròn $(O)$ tại điểm $C$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng đường thẳng $CB$ là tiếp tuyến của đường tròn $(O)$.
  \item[b)] \textit{(0,75 điểm)} Cho biết bán kính $R = 5\text{ cm}$ và dây cung $AB = 8\text{ cm}$. Tính độ dài đoạn thẳng $OC$ và $AC$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Một bể bơi không nắp có dạng hình hộp chữ nhật với đáy là hình vuông, có thể tích bằng $32\text{ m}^3$. Người ta cần lát gạch men toàn bộ mặt đáy và bốn mặt xung quanh bên trong bể. Hãy xác định kích thước cạnh đáy và chiều sâu của bể để tổng diện tích gạch lát cần dùng là nhỏ nhất (nhằm tiết kiệm chi phí thi công nhất).
  \item[b)] \textit{(0,25 điểm)} Cho ba số thực dương $a, b, c$ thỏa mãn điều kiện $a + b + c = 6$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  P = \dfrac{1}{a} + \dfrac{4}{b} + \dfrac{9}{c}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

# 2. TEX SOL
tex_sol = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[top=1.8cm, bottom=2.0cm, left=1.8cm, right=1.8cm]{geometry}

\setlength{\parskip}{3pt}
\setlength{\parindent}{0pt}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\lhead{\footnotesize \textbf{CHÙA HƯƠNG SƠN -- HƯỚNG DẪN CHẤM THI}}
\rhead{\footnotesize \textbf{ĐÁP ÁN CHI TIẾT ĐỀ THI THỬ SỐ 02}}
\cfoot{\thepage}

\begin{document}

\begin{center}
{\large\bfseries ĐÁP ÁN \& HƯỚNG DẪN CHẤM ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 02)}\\[1.5mm]
{\bfseries ĐƠN VỊ: CHÙA HƯƠNG SƠN \quad|\quad MÔN: TOÁN -- LỚP 9 \quad|\quad NĂM HỌC 2026 -- 2027}\\[1mm]
\textit{(Chuẩn cấu trúc định dạng mới của Sở Giáo dục và Đào tạo)}
\end{center}

\vspace{1mm}
\hrule
\vspace{3mm}

\noindent
\textbf{\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,0 ĐIỂM)}

\vspace{2mm}
\noindent
\textbf{1. Bảng đáp án Phần 1: Trắc nghiệm nhiều lựa chọn (3,0 điểm)} \textit{(Mỗi câu đúng được 0,25 điểm)}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Đáp án} & \textbf{A} & \textbf{A} & \textbf{C} & \textbf{A} & \textbf{B} & \textbf{A} & \textbf{B} & \textbf{B} & \textbf{A} & \textbf{B} & \textbf{A} & \textbf{C} \\
\hline
\end{tabular}
\end{center}

\vspace{2mm}
\noindent
\textbf{2. Bảng đáp án Phần 2: Trắc nghiệm Đúng -- Sai (2,0 điểm)}
\begin{center}
\begin{tabular}{|c|c|c|c|c|l|}
\hline
\textbf{Câu} & \textbf{Ý a} & \textbf{Ý b} & \textbf{Ý c} & \textbf{Ý d} & \textbf{Ghi chú đáp án chuẩn} \\
\hline
\textbf{Câu 13} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & Ý c) sai: Chỗ gặp cách A là $50 \times 2 = 100\text{ km}$ (cách B là $80\text{ km}$). \\
\hline
\textbf{Câu 14} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & Ý d) sai: Áp dụng HTL $OA^2 = OH \cdot OC \Rightarrow OC = \frac{25}{3}\text{ cm}$. \\
\hline
\end{tabular}
\end{center}

\vspace{2mm}
\noindent
\textbf{3. Bảng đáp án Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm)} \textit{(Mỗi câu đúng được 0,5 điểm)}
\begin{center}
\begin{tabular}{|c|l|c|c|}
\hline
\textbf{Câu} & \textbf{Nội dung câu hỏi} & \textbf{Kết quả bài làm} & \textbf{Điểm} \\
\hline
\textbf{Câu 15} & Nghiệm bất phương trình $2(x - 3) + 7 < 3(x + 1) - 4$ & \textbf{$x > 2$} & 0,5đ \\
\hline
\textbf{Câu 16} & Giá trị biểu thức $M = \sqrt{(\sqrt{5}-3)^2} + \sqrt{5}$ & \textbf{$3$} & 0,5đ \\
\hline
\textbf{Câu 17} & Khoảng cách từ chân hải đăng đến tàu ($50 / \tan 30^\circ$) & \textbf{$86{,}6\text{ m}$} & 0,5đ \\
\hline
\textbf{Câu 18} & Diện tích bề mặt miếng pizza ($\frac{3{,}14 \times 18^2}{8}$) & \textbf{$127{,}2\text{ cm}^2$} & 0,5đ \\
\hline
\end{tabular}
\end{center}

\vspace{3mm}
\noindent
\textbf{\large PHẦN II. TỰ LUẬN (3,0 ĐIỂM)}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ: $\begin{cases} 2x - 3y = 1 \\ 3x + 2y = 8 \end{cases} \Leftrightarrow \begin{cases} 4x - 6y = 2 \\ 9x + 6y = 24 \end{cases} \Leftrightarrow \begin{cases} 13x = 26 \\ 2x - 3y = 1 \end{cases} \Leftrightarrow \begin{cases} x = 2 \\ y = 1 \end{cases}$. \hfill \textbf{(0,5đ)}
  \item[b)] \textit{(0,5 điểm)} Quy đồng: $B = \dfrac{x - 4}{\sqrt{x}(\sqrt{x}-2)} : \dfrac{\sqrt{x}+2}{\sqrt{x}} = \dfrac{(\sqrt{x}-2)(\sqrt{x}+2)}{\sqrt{x}(\sqrt{x}-2)} \cdot \dfrac{\sqrt{x}}{\sqrt{x}+2} = 1$. \hfill \textbf{(0,5đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Vì $OH \perp AB$ tại $H \Rightarrow H$ là trung điểm của $AB \Rightarrow CH$ là đường trung trực của $AB \Rightarrow CA = CB$. Xét $\Delta OAC$ và $\Delta OBC$ có: $OA = OB = R$, $CA = CB$, $OC$ chung $\Rightarrow \Delta OAC = \Delta OBC$ (c.c.c) $\Rightarrow \widehat{OBC} = \widehat{OAC} = 90^\circ \Rightarrow CB \perp OB$ tại $B \in (O) \Rightarrow CB$ là tiếp tuyến của $(O)$. \hfill \textbf{(0,75đ)}
  \item[b)] \textit{(0,75 điểm)} Vì $H$ là trung điểm $AB \Rightarrow AH = 4\text{ cm}$. $\Delta OAH$ vuông tại $H \Rightarrow OH = \sqrt{OA^2 - AH^2} = 3\text{ cm}$. Tam giác $OAC$ vuông tại $A$, đường cao $AH$:
  $OA^2 = OH \cdot OC \Rightarrow OC = \dfrac{OA^2}{OH} = \dfrac{25}{3}\text{ cm}$. Lại có $AC = \sqrt{OC^2 - OA^2} = \dfrac{20}{3}\text{ cm}$. \hfill \textbf{(0,75đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Cạnh đáy $x > 0$, chiều sâu $h > 0$. $x^2 h = 32 \Rightarrow h = \dfrac{32}{x^2}$. Diện tích lát gạch: $S = x^2 + 4xh = x^2 + \dfrac{128}{x} = x^2 + \dfrac{64}{x} + \dfrac{64}{x} \ge 3\sqrt[3]{x^2 \cdot \dfrac{64}{x} \cdot \dfrac{64}{x}} = 48\text{ m}^2$. Dấu ``='' xảy ra khi $x^2 = \dfrac{64}{x} \Leftrightarrow x = 4\text{ m} \Rightarrow h = 2\text{ m}$. Vậy diện tích nhỏ nhất là $48\text{ m}^2$ khi cạnh đáy $4\text{ m}$, chiều sâu $2\text{ m}$. \hfill \textbf{(0,25đ)}
  \item[b)] \textit{(0,25 điểm)} Ta có $P = \dfrac{1^2}{a} + \dfrac{2^2}{b} + \dfrac{3^2}{c}$. Áp dụng BĐT Cauchy-Schwarz dạng Engel:
  \[
  P \ge \dfrac{(1+2+3)^2}{a+b+c} = \dfrac{36}{6} = 6.
  \]
  Dấu ``='' xảy ra khi $\dfrac{a}{1} = \dfrac{b}{2} = \dfrac{c}{3} = \dfrac{a+b+c}{6} = 1 \Leftrightarrow a = 1, b = 2, c = 3$. Vậy $\min P = 6$. \hfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

# 3. MD SOL
md_sol = r'''# ĐÁP ÁN & HƯỚNG DẪN CHẤM ĐỀ THI THỬ VÀO 10 (ĐỀ SỐ 02)
### ĐƠN VỊ: CHÙA HƯƠNG SƠN | MÔN: TOÁN – LỚP 9 | NĂM HỌC 2026 – 2027
*(Khung ma trận định dạng mới theo cấu trúc Sở GD&ĐT)*

---

## PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,0 ĐIỂM)

### 1. BẢNG ĐÁP ÁN PHẦN 1: TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
| Câu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Đáp án** | **A** | **A** | **C** | **A** | **B** | **A** | **B** | **B** | **A** | **B** | **A** | **C** |

---

### 2. BẢNG ĐÁP ÁN PHẦN 2: TRẮC NGHIỆM ĐÚNG / SAI (2,0 điểm)
| Câu | Ý a | Ý b | Ý c | Ý d | Hướng dẫn chi tiết / Ghi chú |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Câu 13** | **Đ** | **Đ** | **S** | **Đ** | Chỗ gặp cách A là $50 \times 2 = 100\text{ km}$ (cách B là $80\text{ km}$). |
| **Câu 14** | **Đ** | **Đ** | **Đ** | **S** | Áp dụng HTL $OA^2 = OH \cdot OC \Rightarrow OC = \frac{25}{3}\text{ cm}$. |

---

### 3. BẢNG ĐÁP ÁN PHẦN 3: TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
| Câu | Nội dung câu hỏi | Kết quả điền vào bài làm | Điểm |
| :---: | :--- | :---: | :---: |
| **Câu 15** | Nghiệm của bất phương trình $2(x - 3) + 7 < 3(x + 1) - 4$ | **$x > 2$** | 0,5đ |
| **Câu 16** | Giá trị của biểu thức $M = \sqrt{(\sqrt{5} - 3)^2} + \sqrt{5}$ | **$3$** | 0,5đ |
| **Câu 17** | Khoảng cách từ chân hải đăng đến tàu ($50 / \tan 30^\circ$) | **$86{,}6\text{ m}$** | 0,5đ |
| **Câu 18** | Diện tích bề mặt một miếng pizza ($\frac{3{,}14 \times 18^2}{8}$) | **$127{,}2\text{ cm}^2$** | 0,5đ |

---

## PHẦN II. TỰ LUẬN (3,0 ĐIỂM)

### CÂU 19 (1,0 điểm)
* **a) (0,5đ):** Giải hệ phương trình:
  $$\begin{cases} 2x - 3y = 1 \\ 3x + 2y = 8 \end{cases} \Leftrightarrow \begin{cases} 4x - 6y = 2 \\ 9x + 6y = 24 \end{cases} \Leftrightarrow \begin{cases} 13x = 26 \\ 2x - 3y = 1 \end{cases} \Leftrightarrow \begin{cases} x = 2 \\ y = 1 \end{cases}$$
* **b) (0,5đ):** Rút gọn:
  $$B = \left( \frac{\sqrt{x}}{\sqrt{x}-2} - \frac{4}{\sqrt{x}(\sqrt{x}-2)} \right) : \frac{\sqrt{x}+2}{\sqrt{x}} = \frac{x - 4}{\sqrt{x}(\sqrt{x}-2)} \cdot \frac{\sqrt{x}}{\sqrt{x}+2} = 1.$$

### CÂU 20 (1,5 điểm)
* **a) (0,75đ):** $OH \perp AB \Rightarrow H$ là trung điểm $AB \Rightarrow CA = CB$. $\Delta OAC = \Delta OBC$ (c.c.c) $\Rightarrow \widehat{OBC} = \widehat{OAC} = 90^\circ \Rightarrow CB$ là tiếp tuyến.
* **b) (0,75đ):** $AH = 4\text{ cm} \Rightarrow OH = \sqrt{5^2 - 4^2} = 3\text{ cm}$. $OA^2 = OH \cdot OC \Rightarrow OC = \frac{25}{3}\text{ cm}$. $AC = \sqrt{OC^2 - OA^2} = \frac{20}{3}\text{ cm}$.

### CÂU 21 (0,5 điểm)
* **a) (0,25đ):** Thể tích $x^2 h = 32 \Rightarrow h = \frac{32}{x^2}$. Diện tích lát:
  $$S = x^2 + \frac{64}{x} + \frac{64}{x} \ge 3\sqrt[3]{x^2 \cdot \frac{64}{x} \cdot \frac{64}{x}} = 48\text{ m}^2$$
  Dấu ``='' khi $x = 4\text{ m}, h = 2\text{ m}$.
* **b) (0,25đ):** Áp dụng Cauchy-Schwarz Engel:
  $$P = \frac{1^2}{a} + \frac{2^2}{b} + \frac{3^2}{c} \ge \frac{(1+2+3)^2}{a+b+c} = \frac{36}{6} = 6$$
  Dấu ``='' khi $a = 1, b = 2, c = 3$. Vậy $\min P = 6$.
'''

with open(f'{folder}/De_Thi_Thu_Toan_9_De_02.tex', 'w', encoding='utf-8') as f:
    f.write(tex_exam)

with open(f'{folder}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_02.tex', 'w', encoding='utf-8') as f:
    f.write(tex_sol)

with open(f'{folder}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_02.md', 'w', encoding='utf-8') as f:
    f.write(md_sol)

print("Files for DE_02 written successfully!")
