import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

folder_07 = os.path.join(BASE_DIR, 'DE_07')
os.makedirs(folder_07, exist_ok=True)

tex_exam_07 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 07)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 07} & \textbf{MÔN: TOÁN -- LỚP 9} \\
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
\textbf{Câu 1.} Giá trị của biểu thức $3\sqrt{18} - \sqrt{72} + 2\sqrt{8}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $7\sqrt{2}$. & \textbf{B.} $-7\sqrt{2}$. & \textbf{C.} $5\sqrt{2}$. & \textbf{D.} $0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Cho tam giác $ABC$ vuông tại $A$, có góc nhọn $\widehat{B} = \alpha$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\cot \alpha = \dfrac{AB}{AC}$. & \textbf{B.} $\sin \alpha = \dfrac{AB}{BC}$. & \textbf{C.} $\cos \alpha = \dfrac{AC}{BC}$. & \textbf{D.} $\tan \alpha = \dfrac{AB}{AC}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-6x + 18 \ge 0$. & \textbf{B.} $0x + 5 < 0$. & \textbf{C.} $5x^2 - 2 \le 0$. & \textbf{D.} $\dfrac{3}{x} + 1 > 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Cho $x > y$. Bất đẳng thức nào sau đây luôn đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-6x < -6y$. & \textbf{B.} $-6x > -6y$. & \textbf{C.} $x - 5 < y - 5$. & \textbf{D.} $4x + 1 < 4y + 1$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của số 256 là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $16$. & \textbf{B.} $16$ và $-16$. & \textbf{C.} $-16$. & \textbf{D.} $256$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Điều kiện xác định của căn thức $\sqrt{2x - 8}$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \ge 4$. & \textbf{B.} $x \le 4$. & \textbf{C.} $x > 4$. & \textbf{D.} $x < 4$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x \ge 6$, giá trị của biểu thức $\sqrt{(x-6)^2}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x - 6$. & \textbf{B.} $6 - x$. & \textbf{C.} $-(x-6)$. & \textbf{D.} $(x-6)^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của biểu thức $\sqrt[3]{-1331}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-11$. & \textbf{B.} $11$. & \textbf{C.} $-121$. & \textbf{D.} $121$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Trong đường tròn $(O; R)$, công thức tính chu vi hình tròn bán kính $R$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $C = 2\pi R$. & \textbf{B.} $C = \pi R$. & \textbf{C.} $C = \pi R^2$. & \textbf{D.} $C = 2\pi R^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 5\text{ cm})$ và đường thẳng $b$. Biết khoảng cách từ $O$ đến $b$ là $5\text{ cm}$. Vị trí tương đối của đường thẳng $b$ và đường tròn $(O)$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc nhau. & \textbf{B.} Cắt nhau. & \textbf{C.} Không giao nhau. & \textbf{D.} Trùng nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 8\text{ cm})$ và $(O'; 2\text{ cm})$. Biết khoảng cách hai tâm $OO' = 6\text{ cm}$. Vị trí tương đối của hai đường tròn $(O)$ và $(O')$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc trong. & \textbf{B.} Tiếp xúc ngoài. & \textbf{C.} Cắt nhau. & \textbf{D.} Không giao nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Trên đường tròn $(O)$, số đo cung nhỏ $AB$ bằng $100^\circ$. Số đo của góc ở tâm $\widehat{AOB}$ tương ứng bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $100^\circ$. & \textbf{B.} $50^\circ$. & \textbf{C.} $200^\circ$. & \textbf{D.} $80^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Xét bài toán thực tế: ``Hai thửa ruộng cùng thu hoạch được tổng cộng $780\text{ tạ}$ thóc. Vụ mùa năm nay, nhờ áp dụng giống lúa thuần mới, thửa ruộng thứ nhất tăng năng suất $15\%$, thửa ruộng thứ hai tăng năng suất $10\%$ so với vụ trước, nên cả hai thửa ruộng đã thu hoạch được $882\text{ tạ}$ thóc. Gọi sản lượng thóc thu hoạch vụ trước của thửa ruộng thứ nhất và thứ hai lần lượt là $x$ và $y$ (tạ, $x, y \in \mathbb{N}^*, x, y < 780$).''\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Tổng sản lượng vụ trước là $780\text{ tạ}$ nên ta có phương trình: $x + y = 780$. & & \\
\hline
b) Sản lượng vụ này của thửa ruộng 1 là $1{,}15x$ tạ và thửa ruộng 2 là $1{,}1y$ tạ. & & \\
\hline
c) Phương trình biểu thị sản lượng vụ mùa năm nay là: $1{,}15x + 1{,}1y = 800$. & & \\
\hline
d) Vụ trước, thửa ruộng thứ nhất thu hoạch được $480\text{ tạ}$ và thửa thứ hai thu được $300\text{ tạ}$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho đường tròn $(O; 13\text{ cm})$, hai dây cung song song $AB$ và $CD$ cùng nằm về một phía đối với tâm $O$. Biết $AB = 24\text{ cm}$ và $CD = 10\text{ cm}$.\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Khoảng cách từ tâm $O$ đến dây cung $AB$ là $5\text{ cm}$. & & \\
\hline
b) Khoảng cách từ tâm $O$ đến dây cung $CD$ là $12\text{ cm}$. & & \\
\hline
c) Khoảng cách giữa hai dây cung song song $AB$ và $CD$ bằng $7\text{ cm}$. & & \\
\hline
d) Diện tích tứ giác $ABDC$ bằng $140\text{ cm}^2$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Nghiệm của bất phương trình $3(x - 4) + 5 > 2(2x + 1) - 15$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Giá trị của biểu thức $E = \sqrt{(\sqrt{15} - 4)^2} + \sqrt{15}$ bằng $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Một cột phát sóng truyền hình cao $100\text{ m}$ được cố định bởi các sợi dây cáp thép neo từ đỉnh cột xuống các mấu neo trên mặt đất. Biết sợi dây cáp tạo với mặt đất một góc nghiêng $60^\circ$ (xem hình vẽ bên). Tính chiều dài của sợi dây cáp neo đó (làm tròn kết quả đến chữ số thập phân thứ hai của mét).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Mặt đất
  \draw[thick] (-0.5,0) -- (3.5,0);
  \fill[pattern=north east lines, pattern color=gray!50] (-0.5,-0.2) rectangle (3.5,0);
  % Cột phát sóng
  \draw[thick, fill=gray!40] (0,0) rectangle (0.2,3.6);
  \draw[thick] (0.2, 3.6) -- (-0.2, 3.6) -- (0.1, 4.0) -- cycle; % Đỉnh anten
  \node[left] at (0, 1.8) {$100\text{ m}$};
  % Dây cáp neo
  \draw[thick, red!80!black, line width=1.2pt] (0.2,3.6) -- (2.3,0);
  \node[above right] at (1.1, 1.8) {$L = ?$};
  % Góc vuông
  \draw (0.2,0) rectangle (0.5,0.3);
  % Góc nghiêng 60 độ
  \draw (2.3,0) ++(180:0.6) arc (180:120:0.6);
  \node at (1.7, 0.35) {\footnotesize $60^\circ$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một chiếc quạt tròn có bán kính $R = 10\text{ cm}$ và góc ở tâm tương ứng là $108^\circ$. Tính diện tích của hình quạt tròn đó (lấy $\pi \approx 3{,}14$, đơn vị: $\text{cm}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 3x - 4y = 2 \\ 2x + y = 5 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $A = \left( \dfrac{\sqrt{x}}{\sqrt{x}+2} + \dfrac{2}{\sqrt{x}-2} \right) : \dfrac{x+4}{x-4}$ với $x > 0, x \ne 4$. Rút gọn biểu thức $A$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho đường tròn $(O; R)$, đường kính $AB$. Trên tiếp tuyến của đường tròn $(O)$ tại $A$, lấy điểm $C$ ($C \ne A$). Từ $C$ vẽ tiếp tuyến thứ hai $CD$ với $(O)$ ($D$ là tiếp điểm). Gọi $I$ là giao điểm của $AD$ và $OC$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng bốn điểm $A, C, D, O$ cùng thuộc một đường tròn và $OC \perp AD$ tại $I$.
  \item[b)] \textit{(0,75 điểm)} Kẻ đường kính $DE$ của đường tròn $(O)$. Chứng minh rằng $EB \parallel OC$ và $AC \cdot EB = R^2$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Một công ty sữa cần thiết kế một hộp sữa tươi hình hộp chữ nhật có nắp đậy với thể tích $V = 500\text{ cm}^3$. Đáy hộp có dạng hình chữ nhật với chiều dài gấp đôi chiều rộng. Hãy tìm các kích thước của hộp sữa (chiều dài, chiều rộng đáy và chiều cao) để tổng diện tích vỏ hộp là nhỏ nhất (nhằm tiết kiệm chi phí bao bì nhất).
  \item[b)] \textit{(0,25 điểm)} Cho ba số thực dương $a, b, c$ thỏa mãn điều kiện $a + b + c = 1$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  P = \dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

tex_sol_07 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐÁP ÁN CHI TIẾT ĐỀ THI THỬ SỐ 07}}
\cfoot{\thepage}

\begin{document}

\begin{center}
{\large\bfseries ĐÁP ÁN \& HƯỚNG DẪN CHẤM ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 07)}\\[1.5mm]
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
\textbf{Câu 13} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & Ý c) sai vì sản lượng năm nay là 882 tạ (đề ghi 800 tạ). \\
\hline
\textbf{Câu 14} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & Ý d) sai: Diện tích hình thang $S = \dfrac{(24+10) \times 7}{2} = 119\text{ cm}^2$ (đề ghi 140). \\
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
\textbf{Câu 15} & Nghiệm bất phương trình $3(x - 4) + 5 > 2(2x + 1) - 15$ & \textbf{$x < 6$} & 0,5đ \\
\hline
\textbf{Câu 16} & Giá trị biểu thức $E = \sqrt{(\sqrt{15}-4)^2} + \sqrt{15}$ & \textbf{$4$} & 0,5đ \\
\hline
\textbf{Câu 17} & Chiều dài dây cáp neo ($100 / \sin 60^\circ$) & \textbf{$115{,}47\text{ m}$} & 0,5đ \\
\hline
\textbf{Câu 18} & Diện tích hình quạt tròn ($\dfrac{3{,}14 \times 10^2 \times 108}{360}$) & \textbf{$94{,}2\text{ cm}^2$} & 0,5đ \\
\hline
\end{tabular}
\end{center}

\vspace{3mm}
\noindent
\textbf{\large PHẦN II. TỰ LUẬN (3,0 ĐIỂM)}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} $\begin{cases} 3x - 4y = 2 \\ 2x + y = 5 \end{cases} \Leftrightarrow \begin{cases} 3x - 4(5 - 2x) = 2 \\ y = 5 - 2x \end{cases} \Leftrightarrow \begin{cases} 11x = 22 \\ y = 5 - 2x \end{cases} \Leftrightarrow \begin{cases} x = 2 \\ y = 1 \end{cases}$. \hfill \textbf{(0,5đ)}
  \item[b)] \textit{(0,5 điểm)} $A = \dfrac{\sqrt{x}(\sqrt{x}-2) + 2(\sqrt{x}+2)}{x - 4} : \dfrac{x+4}{x-4} = \dfrac{x - 2\sqrt{x} + 2\sqrt{x} + 4}{x - 4} \cdot \dfrac{x - 4}{x + 4} = \dfrac{x + 4}{x + 4} = 1$. \hfill \textbf{(0,5đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Vì $CA \perp OA, CD \perp OD \Rightarrow \widehat{CAO} = \widehat{CDO} = 90^\circ \Rightarrow A, C, D, O$ cùng thuộc đường tròn đường kính $OC$. Lại có $CA = CD$ và $OA = OD \Rightarrow OC$ là đường trung trực của $AD \Rightarrow OC \perp AD$ tại $I$. \hfill \textbf{(0,75đ)}
  \item[b)] \textit{(0,75 điểm)} Vì $DE$ là đường kính của $(O) \Rightarrow \widehat{DBE} = 90^\circ \Rightarrow EB \perp AD$. Lại có $OC \perp AD \Rightarrow EB \parallel OC$. Tam giác vuông $ACD \backsim \Delta EBD \Rightarrow AC \cdot EB = R^2$ (hoặc dùng hệ thức lượng trong tam giác vuông $ACO$). \hfill \textbf{(0,75đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Gọi chiều rộng đáy $x > 0 \Rightarrow$ chiều dài đáy $2x$. Chiều cao $h > 0$. $V = 2x^2 h = 500 \Rightarrow h = \dfrac{250}{x^2}$. Diện tích toàn phần:
  $S_{tp} = 2(2x^2) + 2(x \cdot h + 2x \cdot h) = 4x^2 + 6xh = 4x^2 + \dfrac{1500}{x} = 4x^2 + \dfrac{750}{x} + \dfrac{750}{x} \ge 3\sqrt[3]{4x^2 \cdot \dfrac{750}{x} \cdot \dfrac{750}{x}} = 3\sqrt[3]{2250000} \approx 393\text{ cm}^2$. Dấu ``='' khi $4x^2 = \dfrac{750}{x} \Leftrightarrow x^3 = \dfrac{750}{4} = 187{,}5$. \hfill \textbf{(0,25đ)}
  \item[b)] \textit{(0,25 điểm)} Áp dụng BĐT Cauchy-Schwarz dạng Engel:
  \[
  P = \dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c} \ge \dfrac{(1+1+1)^2}{a+b+c} = \dfrac{9}{1} = 9.
  \]
  Dấu ``='' xảy ra khi $a = b = c = \dfrac{1}{3}$. Vậy $\min P = 9$. \hfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

md_sol_07 = r'''# ĐÁP ÁN & HƯỚNG DẪN CHẤM ĐỀ THI THỬ VÀO 10 (ĐỀ SỐ 07)
### ĐƠN VỊ: CHÙA HƯƠNG SƠN | MÔN: TOÁN – LỚP 9 | NĂM HỌC 2026 – 2027

## PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,0 ĐIỂM)
### 1. BẢNG ĐÁP ÁN PHẦN 1: TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
| Câu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Đáp án** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** |

### 2. BẢNG ĐÁP ÁN PHẦN 2: TRẮC NGHIỆM ĐÚNG / SAI (2,0 điểm)
| Câu | Ý a | Ý b | Ý c | Ý d | Ghi chú |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Câu 13** | **Đ** | **Đ** | **S** | **Đ** | Ý c) sai vì sản lượng năm nay là 882 tạ. |
| **Câu 14** | **Đ** | **Đ** | **Đ** | **S** | Ý d) sai vì diện tích hình thang bằng 119 cm2 (đề ghi 140). |

### 3. BẢNG ĐÁP ÁN PHẦN 3: TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
* Câu 15: **$x < 6$**
* Câu 16: **$4$**
* Câu 17: **$115{,}47\text{ m}$**
* Câu 18: **$94{,}2\text{ cm}^2$**

## PHẦN II. TỰ LUẬN (3,0 ĐIỂM)
* **Câu 19a (0,5đ):** $(x; y) = (2; 1)$.
* **Câu 19b (0,5đ):** $A = 1$.
* **Câu 20a (0,75đ):** $A, C, D, O$ cùng nằm trên đường tròn đường kính $OC$; $OC \perp AD$.
* **Câu 20b (0,75đ):** $EB \parallel OC$ và $AC \cdot EB = R^2$.
* **Câu 21a (0,25đ):** Tối ưu hóa vỏ hộp sữa.
* **Câu 21b (0,25đ):** $\min P = 9$ khi $a = b = c = \dfrac{1}{3}$.
'''

with open(f'{folder_07}/De_Thi_Thu_Toan_9_De_07.tex', 'w', encoding='utf-8') as f:
    f.write(tex_exam_07)

with open(f'{folder_07}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_07.tex', 'w', encoding='utf-8') as f:
    f.write(tex_sol_07)

with open(f'{folder_07}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_07.md', 'w', encoding='utf-8') as f:
    f.write(md_sol_07)

print("Generated files for DE_07 successfully!")
