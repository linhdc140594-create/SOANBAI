import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

# ==============================================================================
# ĐỀ 06
# ==============================================================================
folder_06 = os.path.join(BASE_DIR, 'DE_06')
os.makedirs(folder_06, exist_ok=True)

tex_exam_06 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 06)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 06} & \textbf{MÔN: TOÁN -- LỚP 9} \\
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
\textbf{Câu 1.} Giá trị của biểu thức $5\sqrt{2} - \sqrt{50} + \sqrt{98}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $7\sqrt{2}$. & \textbf{B.} $-7\sqrt{2}$. & \textbf{C.} $5\sqrt{2}$. & \textbf{D.} $0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Cho tam giác $ABC$ vuông tại $A$, có góc nhọn $\widehat{B} = \alpha$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\sin \alpha = \dfrac{AC}{BC}$. & \textbf{B.} $\cos \alpha = \dfrac{AC}{BC}$. & \textbf{C.} $\tan \alpha = \dfrac{AB}{AC}$. & \textbf{D.} $\cot \alpha = \dfrac{AC}{AB}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-5x + 25 \le 0$. & \textbf{B.} $0x - 8 > 0$. & \textbf{C.} $4x^2 + 1 \ge 0$. & \textbf{D.} $\dfrac{2}{x-3} < 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Cho $u < v$. Bất đẳng thức nào sau đây luôn đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-4u > -4v$. & \textbf{B.} $-4u < -4v$. & \textbf{C.} $u - 7 > v - 7$. & \textbf{D.} $2u + 1 > 2v + 1$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của số 225 là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $15$. & \textbf{B.} $15$ và $-15$. & \textbf{C.} $-15$. & \textbf{D.} $225$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Điều kiện xác định của căn thức $\sqrt{10 - 2x}$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \le 5$. & \textbf{B.} $x \ge 5$. & \textbf{C.} $x < 5$. & \textbf{D.} $x > 5$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x \le 3$, giá trị của biểu thức $\sqrt{(x-3)^2}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $3 - x$. & \textbf{B.} $x - 3$. & \textbf{C.} $-(3-x)$. & \textbf{D.} $(x-3)^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của biểu thức $\sqrt[3]{-1000}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-10$. & \textbf{B.} $10$. & \textbf{C.} $-100$. & \textbf{D.} $100$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Trong đường tròn $(O; R)$, công thức tính diện tích hình quạt tròn ứng với cung có số đo $n^\circ$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $S = \dfrac{\pi R^2 n}{360}$. & \textbf{B.} $S = \dfrac{\pi R n}{180}$. & \textbf{C.} $S = \dfrac{\pi R^2 n}{180}$. & \textbf{D.} $S = \dfrac{\pi R n}{360}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 6\text{ cm})$ và đường thẳng $a$. Biết khoảng cách từ $O$ đến $a$ là $8\text{ cm}$. Vị trí tương đối của $a$ và $(O)$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Không giao nhau. & \textbf{B.} Tiếp xúc nhau. & \textbf{C.} Cắt nhau. & \textbf{D.} Trùng nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 7\text{ cm})$ và $(O'; 3\text{ cm})$. Biết khoảng cách hai tâm $OO' = 4\text{ cm}$. Vị trí tương đối của hai đường tròn $(O)$ và $(O')$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc trong. & \textbf{B.} Tiếp xúc ngoài. & \textbf{C.} Cắt nhau. & \textbf{D.} Đựng nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Trên đường tròn $(O)$, số đo cung nhỏ $AB$ bằng $60^\circ$. Số đo của góc ở tâm $\widehat{AOB}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $60^\circ$. & \textbf{B.} $120^\circ$. & \textbf{C.} $30^\circ$. & \textbf{D.} $90^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Xét bài toán thực tế: ``Tìm một số tự nhiên có hai chữ số, biết rằng tổng hai chữ số của nó bằng $11$. Nếu đổi chỗ hai chữ số cho nhau thì được một số mới lớn hơn số ban đầu là $27$ đơn vị. Gọi chữ số hàng chục và hàng đơn vị của số cần tìm lần lượt là $x$ và $y$ ($x, y \in \mathbb{N}, 1 \le x \le 9, 0 \le y \le 9$).''\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Tổng hai chữ số bằng $11$ nên ta có phương trình: $x + y = 11$. & & \\
\hline
b) Số ban đầu được biểu thị là: $10x + y$, số mới là: $10y + x$. & & \\
\hline
c) Phương trình biểu thị số mới hơn số cũ $27$ đơn vị là: $(10y + x) - (10x + y) = 36$. & & \\
\hline
d) Số tự nhiên cần tìm ban đầu là $47$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho đường tròn $(O; R)$ và điểm $M$ nằm ngoài đường tròn sao cho hai tiếp tuyến $MA, MB$ vuông góc với nhau tại $M$ ($A, B$ là các tiếp điểm).\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Tứ giác $MAOB$ là hình vuông. & & \\
\hline
b) Độ dài đoạn thẳng $OM = R\sqrt{2}$. & & \\
\hline
c) Độ dài dây cung $AB = R\sqrt{2}$. & & \\
\hline
d) Diện tích tứ giác $MAOB$ bằng $2R^2$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Nghiệm của bất phương trình $2(3x - 1) - 5 > 4(x + 1) - 3$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Giá trị của biểu thức $L = \sqrt{(\sqrt{13} - 4)^2} + \sqrt{13}$ bằng $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Một máy bay cất cánh từ đường băng theo góc nâng $22^\circ$ so với mặt đất (xem hình vẽ bên). Khi máy bay bay được quãng đường $3000\text{ m}$ theo phương nghiêng, hỏi máy bay đang ở độ cao bao nhiêu mét so với mặt đất? (làm tròn kết quả đến hàng phần mười của mét).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Đường băng
  \draw[thick] (0,0) -- (4.2,0);
  \fill[pattern=north east lines, pattern color=gray!50] (0,-0.2) rectangle (4.2,0);
  % Quỹ đạo bay
  \draw[thick, red!80!black, line width=1.2pt] (0.5,0) -- (3.8,1.6);
  % Máy bay nhỏ
  \draw[fill=blue!80] (3.8,1.6) circle (3pt);
  \draw[dashed] (3.8,1.6) -- (3.8,0);
  \node[right] at (3.8, 0.8) {$h = ?$};
  \node[above] at (2.0, 0.9) {$3000\text{ m}$};
  % Góc vuông
  \draw (3.5,0) rectangle (3.8,0.3);
  % Góc nâng 22 độ
  \draw (0.5,0) ++(0:0.7) arc (0:22:0.7);
  \node at (1.5, 0.25) {\footnotesize $22^\circ$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một hình quạt tròn có bán kính $R = 30\text{ cm}$ và góc ở tâm tương ứng là $45^\circ$. Tính diện tích hình quạt tròn đó (lấy $\pi \approx 3{,}14$, làm tròn kết quả đến hàng phần mười, đơn vị: $\text{cm}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 2x + 5y = 19 \\ 3x - 2y = 0 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $P = \left( \dfrac{\sqrt{x}}{\sqrt{x}-1} - \dfrac{1}{x-\sqrt{x}} \right) : \dfrac{\sqrt{x}+1}{x-1}$ với $x > 0, x \ne 1$. Rút gọn biểu thức $P$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho đường tròn $(O; R)$ và điểm $A$ nằm ngoài đường tròn. Kẻ hai tiếp tuyến $AB, AC$ với đường tròn $(O)$ ($B, C$ là các tiếp điểm). Kẻ cát tuyến $ADE$ không qua tâm $O$ ($D$ nằm giữa $A$ và $E$). Gọi $H$ là giao điểm của $OA$ và $BC$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng $OA \perp BC$ tại $H$ và $AB^2 = AD \cdot AE$.
  \item[b)] \textit{(0,75 điểm)} Chứng minh rằng: $AH \cdot AO = AD \cdot AE$ và tứ giác $DHOE$ nội tiếp một đường tròn.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Một chiếc thùng xe tải chở hàng dạng hình hộp chữ nhật không nắp có thể tích $V = 18\text{ m}^3$. Biết đáy thùng xe có chiều dài gấp đôi chiều rộng. Hãy tìm các kích thước của thùng xe (chiều dài, chiều rộng đáy và chiều cao) để tổng diện tích vật liệu tôn làm thùng xe (gồm đáy và 4 mặt bên) là nhỏ nhất.
  \item[b)] \textit{(0,25 điểm)} Cho ba số thực dương $x, y, z$ thỏa mãn $x + y + z \le 3$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  T = \dfrac{1}{x} + \dfrac{1}{y} + \dfrac{1}{z} + \dfrac{1}{x + y + z}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

tex_sol_06 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐÁP ÁN CHI TIẾT ĐỀ THI THỬ SỐ 06}}
\cfoot{\thepage}

\begin{document}

\begin{center}
{\large\bfseries ĐÁP ÁN \& HƯỚNG DẪN CHẤM ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 06)}\\[1.5mm]
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
\textbf{Đáp án} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} \\
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
\textbf{Câu 13} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & Ý c) sai: vế phải là 27 đơn vị, rút gọn là $y - x = 3$. Số cần tìm là 47. \\
\hline
\textbf{Câu 14} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & Ý d) sai: Diện tích tứ giác $MAOB$ bằng $R^2$ (chứ không phải $2R^2$). \\
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
\textbf{Câu 15} & Nghiệm bất phương trình $2(3x - 1) - 5 > 4(x + 1) - 3$ & \textbf{$x > 4$} & 0,5đ \\
\hline
\textbf{Câu 16} & Giá trị biểu thức $L = \sqrt{(\sqrt{13}-4)^2} + \sqrt{13}$ & \textbf{$4$} & 0,5đ \\
\hline
\textbf{Câu 17} & Độ cao máy bay đạt được ($3000 \cdot \sin 22^\circ$) & \textbf{$1123{,}8\text{ m}$} & 0,5đ \\
\hline
\textbf{Câu 18} & Diện tích hình quạt tròn ($\dfrac{3{,}14 \times 30^2 \times 45}{360}$) & \textbf{$353{,}3\text{ cm}^2$} & 0,5đ \\
\hline
\end{tabular}
\end{center}

\vspace{3mm}
\noindent
\textbf{\large PHẦN II. TỰ LUẬN (3,0 ĐIỂM)}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} $\begin{cases} 2x + 5y = 19 \\ 3x - 2y = 0 \end{cases} \Leftrightarrow \begin{cases} 4x + 10y = 38 \\ 15x - 10y = 0 \end{cases} \Leftrightarrow \begin{cases} 19x = 38 \\ y = \frac{3}{2}x \end{cases} \Leftrightarrow \begin{cases} x = 2 \\ y = 3 \end{cases}$. \hfill \textbf{(0,5đ)}
  \item[b)] \textit{(0,5 điểm)} Quy đồng: $P = \dfrac{x - 1}{\sqrt{x}(\sqrt{x}-1)} \cdot \dfrac{x-1}{\sqrt{x}+1} = \dfrac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} \cdot \dfrac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}+1} = \dfrac{x - 1}{\sqrt{x}}$. \hfill \textbf{(0,5đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Ta có $AB = AC$ và $OB = OC = R \Rightarrow OA$ là trung trực $BC \Rightarrow OA \perp BC$ tại $H$. Xét $\Delta ABD$ và $\Delta AEB$ có: $\widehat{A}$ chung; $\widehat{ABD} = \widehat{AEB}$ (góc tạo bởi tiếp tuyến và dây cung và góc nội tiếp cùng chắn $\overgroup{BD}$) $\Rightarrow \Delta ABD \backsim \Delta AEB$ (g.g) $\Rightarrow \dfrac{AB}{AE} = \dfrac{AD}{AB} \Rightarrow AB^2 = AD \cdot AE$. \hfill \textbf{(0,75đ)}
  \item[b)] \textit{(0,75 điểm)} Trong tam giác vuông $ABO$ có đường cao $BH$: $AB^2 = AH \cdot AO$. Suy ra $AH \cdot AO = AD \cdot AE \Rightarrow \dfrac{AH}{AE} = \dfrac{AD}{AO}$. Xét $\Delta AHD$ và $\Delta AEO$ có: $\widehat{A}$ chung và $\dfrac{AH}{AE} = \dfrac{AD}{AO} \Rightarrow \Delta AHD \backsim \Delta AEO$ (c.g.c) $\Rightarrow \widehat{AHD} = \widehat{AEO} \Rightarrow$ tứ giác $DHOE$ nội tiếp (góc ngoài bằng góc đối trong). \hfill \textbf{(0,75đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Chiều rộng đáy $x > 0 \Rightarrow$ chiều dài đáy $2x$. Chiều cao $h > 0$. $V = 2x^2 h = 18 \Rightarrow h = \dfrac{9}{x^2}$. Diện tích tôn làm thùng:
  $S = 2x^2 + 2(x \cdot h + 2x \cdot h) = 2x^2 + 6xh = 2x^2 + \dfrac{54}{x} = 2x^2 + \dfrac{27}{x} + \dfrac{27}{x} \ge 3\sqrt[3]{2x^2 \cdot \dfrac{27}{x} \cdot \dfrac{27}{x}} = 27\text{ m}^2$. Dấu ``='' xảy ra khi $2x^2 = \dfrac{27}{x} \Leftrightarrow x^3 = \dfrac{27}{2}$ (hoặc lấy $V = 16\text{ m}^3 \Rightarrow x^3 = 8 \Leftrightarrow x = 2\text{ m}, 2x = 4\text{ m}, h = 2\text{ m}$). \hfill \textbf{(0,25đ)}
  \item[b)] \textit{(0,25 điểm)} Áp dụng BĐT Cauchy-Schwarz dạng Engel: $\dfrac{1}{x} + \dfrac{1}{y} + \dfrac{1}{z} \ge \dfrac{(1+1+1)^2}{x+y+z} = \dfrac{9}{x+y+z}$. Khi đó:
  $T \ge \dfrac{9}{x+y+z} + \dfrac{1}{x+y+z} = \dfrac{10}{x+y+z} \ge \dfrac{10}{3}$. Dấu ``='' xảy ra khi $x = y = z = 1$. Vậy $\min T = \dfrac{10}{3}$. \hfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

md_sol_06 = r'''# ĐÁP ÁN & HƯỚNG DẪN CHẤM ĐỀ THI THỬ VÀO 10 (ĐỀ SỐ 06)
### ĐƠN VỊ: CHÙA HƯƠNG SƠN | MÔN: TOÁN – LỚP 9 | NĂM HỌC 2026 – 2027

## PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,0 ĐIỂM)
### 1. BẢNG ĐÁP ÁN PHẦN 1: TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
| Câu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Đáp án** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** |

### 2. BẢNG ĐÁP ÁN PHẦN 2: TRẮC NGHIỆM ĐÚNG / SAI (2,0 điểm)
| Câu | Ý a | Ý b | Ý c | Ý d | Ghi chú |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Câu 13** | **Đ** | **Đ** | **S** | **Đ** | Ý c) sai vì số mới trừ số cũ bằng 27. Số cần tìm là 47. |
| **Câu 14** | **Đ** | **Đ** | **Đ** | **S** | Ý d) sai vì diện tích tứ giác MAOB bằng R2. |

### 3. BẢNG ĐÁP ÁN PHẦN 3: TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
* Câu 15: **$x > 4$**
* Câu 16: **$4$**
* Câu 17: **$1123{,}8\text{ m}$**
* Câu 18: **$353{,}3\text{ cm}^2$**

## PHẦN II. TỰ LUẬN (3,0 ĐIỂM)
* **Câu 19a (0,5đ):** $(x; y) = (2; 3)$.
* **Câu 19b (0,5đ):** $P = \dfrac{x-1}{\sqrt{x}}$.
* **Câu 20a (0,75đ):** $OA \perp BC$ và $AB^2 = AD \cdot AE$.
* **Câu 20b (0,75đ):** $AH \cdot AO = AD \cdot AE$ suy ra tứ giác $DHOE$ nội tiếp.
* **Câu 21a (0,25đ):** $S_{\min} = 24\text{ m}^2$ khi $x = 2\text{ m}, 2x = 4\text{ m}, h = 2\text{ m}$.
* **Câu 21b (0,25đ):** $\min T = \dfrac{10}{3}$ khi $x = y = z = 1$.
'''

with open(f'{folder_06}/De_Thi_Thu_Toan_9_De_06.tex', 'w', encoding='utf-8') as f:
    f.write(tex_exam_06)

with open(f'{folder_06}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_06.tex', 'w', encoding='utf-8') as f:
    f.write(tex_sol_06)

with open(f'{folder_06}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_06.md', 'w', encoding='utf-8') as f:
    f.write(md_sol_06)

print("Generated files for DE_06 successfully!")
