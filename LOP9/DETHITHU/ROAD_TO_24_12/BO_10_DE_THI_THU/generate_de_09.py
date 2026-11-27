import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

folder_09 = os.path.join(BASE_DIR, 'DE_09')
os.makedirs(folder_09, exist_ok=True)

tex_exam_09 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 09)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 09} & \textbf{MÔN: TOÁN -- LỚP 9} \\
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
\textbf{Câu 1.} Giá trị của biểu thức $2\sqrt{50} - 3\sqrt{18} + \sqrt{32}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $5\sqrt{2}$. & \textbf{B.} $6\sqrt{2}$. & \textbf{C.} $4\sqrt{2}$. & \textbf{D.} $3\sqrt{2}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Trong các khẳng định sau về tỉ số lượng giác của góc nhọn, khẳng định nào đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\cos 60^\circ = \dfrac{1}{2}$. & \textbf{B.} $\sin 60^\circ = \dfrac{1}{2}$. & \textbf{C.} $\tan 45^\circ = \dfrac{\sqrt{2}}{2}$. & \textbf{D.} $\cot 30^\circ = \dfrac{\sqrt{3}}{3}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào dưới đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $7x + 21 > 0$. & \textbf{B.} $0x - 9 \le 0$. & \textbf{C.} $x^2 + 5x \ge 0$. & \textbf{D.} $\dfrac{2}{x+1} < 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Cho hai số thực $m$ và $n$ thỏa mãn $m > n$. Khẳng định nào sau đây là luôn đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $m - 3 > n - 3$. & \textbf{B.} $-2m > -2n$. & \textbf{C.} $3 - m > 3 - n$. & \textbf{D.} $5m < 5n$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của 324 bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $18$. & \textbf{B.} $-18$. & \textbf{C.} $18$ và $-18$. & \textbf{D.} $104976$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Biểu thức $\sqrt{3x - 15}$ xác định khi và chỉ khi\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \ge 5$. & \textbf{B.} $x \le 5$. & \textbf{C.} $x > 5$. & \textbf{D.} $x \ne 5$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x > 4$, giá trị rút gọn của biểu thức $\sqrt{(4 - x)^2}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x - 4$. & \textbf{B.} $4 - x$. & \textbf{C.} $-(x - 4)$. & \textbf{D.} $16 - x^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của biểu thức căn bậc ba $\sqrt[3]{-729}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-9$. & \textbf{B.} $9$. & \textbf{C.} $-81$. & \textbf{D.} $81$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Chu vi của một hình tròn có đường kính $d$ được tính theo công thức nào sau đây?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $C = \pi d$. & \textbf{B.} $C = 2\pi d$. & \textbf{C.} $C = \pi d^2$. & \textbf{D.} $C = \dfrac{1}{2}\pi d$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 4\text{ cm})$ và đường thẳng $d$. Khoảng cách từ tâm $O$ đến đường thẳng $d$ bằng $5\text{ cm}$. Vị trí tương đối của đường thẳng $d$ và đường tròn $(O)$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Không giao nhau. & \textbf{B.} Cắt nhau. & \textbf{C.} Tiếp xúc nhau. & \textbf{D.} Trùng nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 8\text{ cm})$ và $(O'; 3\text{ cm})$. Biết khoảng cách giữa hai tâm là $OO' = 4\text{ cm}$. Vị trí tương đối của hai đường tròn $(O)$ và $(O')$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Đường tròn $(O)$ đựng $(O')$. & \textbf{B.} Cắt nhau. & \textbf{C.} Tiếp xúc trong. & \textbf{D.} Ngoài nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Trên đường tròn $(O)$, số đo cung nhỏ $CD$ bằng $70^\circ$. Số đo của cung lớn $CD$ tương ứng bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $290^\circ$. & \textbf{B.} $110^\circ$. & \textbf{C.} $140^\circ$. & \textbf{D.} $220^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Nhân dịp lễ Giáng sinh và chuẩn bị đón năm mới, một cửa hàng thời trang nhập về tổng cộng $300$ chiếc áo ấm gồm hai loại: áo khoác dạ và áo phao ấm. Tổng số tiền vốn nhập hàng là $96$ triệu đồng ($96\,000\,000$ đồng). Giá nhập mỗi chiếc áo khoác dạ là $400\,000$ đồng, giá nhập mỗi chiếc áo phao là $240\,000$ đồng. Gọi số lượng áo khoác dạ và áo phao nhập về lần lượt là $x$ và $y$ ($x, y \in \mathbb{N}^*, x, y < 300$).\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Phương trình biểu thị tổng số lượng áo là: $x + y = 300$. & & \\
\hline
b) Phương trình biểu thị tổng tiền vốn là: $400\,000x + 240\,000y = 96\,000\,000$ (rút gọn thành $5x + 3y = 1200$). & & \\
\hline
c) Số lượng áo khoác dạ nhập về nhiều hơn số lượng áo phao nhập về. & & \\
\hline
d) Cửa hàng bán áo dạ với giá $500\,000$ đ/chiếc và áo phao $320\,000$ đ/chiếc. Khi bán hết cả 300 chiếc áo, cửa hàng thu được tổng tiền lãi là 27 triệu đồng. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Vẽ đường tròn tâm $O$ đường kính $BC$. Kẻ đường cao $AH$ của $\triangle ABC$ ($H \in BC$).\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Bán kính đường tròn ngoại tiếp tam giác $ABC$ bằng $5\text{ cm}$. & & \\
\hline
b) Độ dài đường cao $AH$ bằng $4{,}8\text{ cm}$. & & \\
\hline
c) Khoảng cách từ tâm $O$ đến cạnh $AB$ bằng $3\text{ cm}$. & & \\
\hline
d) Tứ giác có các đỉnh là $A, B, C$ và điểm đối xứng của $A$ qua $BC$ là một hình thoi. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Tập nghiệm của bất phương trình $\dfrac{2x - 1}{3} - \dfrac{x + 2}{2} > 1$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Giá trị của biểu thức $Q = \sqrt{(\sqrt{11} - 4)^2} + \sqrt{11}$ bằng $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Một cần cẩu xây dựng có cánh tay đòn cẩu dài $25\text{ m}$. Khớp quay tay đòn đặt cách mặt đất $2\text{ m}$. Khi làm việc, cánh tay đòn nâng vật liệu tạo với phương nằm ngang một góc $52^\circ$ (xem hình vẽ bên). Tính độ cao tối đa mà đầu móc cẩu đạt được so với mặt đất (làm tròn kết quả đến hàng phần mười của mét, biết $\sin 52^\circ \approx 0{,}7880$).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Mặt đất
  \draw[thick] (-0.5,0) -- (3.8,0);
  % Tháp cẩu
  \draw[thick, fill=gray!30] (0.2,0) rectangle (0.8,1.5);
  \node[left] at (0.2,0.75) {\footnotesize $2\text{ m}$};
  % Cánh tay đòn
  \draw[line width=1.5pt, red!80!black] (0.5,1.5) -- (2.8,3.8);
  \node[above left] at (1.6,2.8) {\footnotesize $25\text{ m}$};
  % Đường nằm ngang gióng góc
  \draw[dashed] (0.5,1.5) -- (3.2,1.5);
  % Góc nâng 52 độ
  \draw (0.5,1.5) ++(0:0.7) arc (0:52:0.7);
  \node at (1.5,1.85) {\footnotesize $52^\circ$};
  % Dây móc hàng
  \draw[thick, blue] (2.8,3.8) -- (2.8,3.0);
  \draw[thick, fill=blue!40] (2.6,2.7) rectangle (3.0,3.0);
  \draw[dashed] (2.8,3.8) -- (2.8,0);
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một hình quạt tròn có bán kính $R = 15\text{ cm}$ và góc ở tâm tương ứng là $72^\circ$. Tính diện tích của hình quạt tròn đó theo $\pi$ và làm tròn đến hàng phần mười (lấy $\pi \approx 3{,}14$, đơn vị: $\text{cm}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 2x + 5y = 11 \\ 3x - 2y = 7 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $P = \left( \dfrac{1}{\sqrt{x}-1} + \dfrac{1}{\sqrt{x}+1} \right) : \dfrac{2\sqrt{x}}{x-1}$ với $x > 0, x \ne 1$. Rút gọn biểu thức $P$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho đường tròn $(O; R)$, từ một điểm $M$ nằm ngoài đường tròn kẻ hai tiếp tuyến $MA, MB$ với $(O)$ ($A$ và $B$ là hai tiếp điểm). Kẻ cát tuyến $MCD$ không đi qua tâm $O$ ($C$ nằm giữa $M$ và $D$). Gọi $H$ là giao điểm của đoạn thẳng $MO$ và dây cung $AB$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng đường thẳng $MO$ vuông góc với dây cung $AB$ tại $H$ và $MA^2 = MH \cdot MO$.
  \item[b)] \textit{(0,75 điểm)} Chứng minh rằng $MC \cdot MD = MH \cdot MO$, từ đó suy ra bốn điểm $C, H, O, D$ cùng thuộc một đường tròn.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Bác Hai có một mảnh vườn hình chữ nhật có diện tích $S = 200\text{ m}^2$. Bác dự định làm hàng rào bao quanh ba phía của mảnh vườn (gồm hai chiều rộng và một chiều dài), phía chiều dài còn lại giáp với bờ tường hoa kiên cố của nhà văn hóa thôn nên không cần rào. Hỏi các kích thước (chiều dài và chiều rộng) của mảnh vườn phải bằng bao nhiêu mét để tổng chiều dài hàng rào cần làm là ngắn nhất?
  \item[b)] \textit{(0,25 điểm)} Cho ba số thực dương $a, b, c$ thỏa mãn điều kiện $ab + bc + ca = 3$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  Q = \dfrac{a^2}{b+c} + \dfrac{b^2}{c+a} + \dfrac{c^2}{a+b}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

tex_sol_09 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐÁP ÁN \& LỜI GIẢI CHI TIẾT (ĐỀ SỐ 09)}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\large HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ THI THỬ SỐ 09}\\
\textbf{MÔN: TOÁN 9 -- HỌC KỲ I -- NĂM HỌC 2026 -- 2027}\\
\textit{(Hướng dẫn chấm gồm 02 trang)}
\end{center}

\vspace{1mm}
\noindent
\rule{\linewidth}{0.8pt}

\vspace{2mm}
\noindent
\textbf{\large A. ĐÁP ÁN TRẮC NGHIỆM (7,0 ĐIỂM)}

\vspace{2mm}
\noindent
\textbf{1. Phần 1: Trắc nghiệm nhiều lựa chọn (3,0 điểm -- Mỗi câu đúng 0,25 điểm)}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{A} \\
\hline
\end{tabular}
\end{center}

\vspace{2mm}
\noindent
\textbf{2. Phần 2: Trắc nghiệm Đúng -- Sai (2,0 điểm)}
\begin{itemize}
  \item \textbf{Câu 13 (1,0 điểm):} a) Đúng \quad b) Đúng \quad c) Sai \quad d) Đúng.
  \item \textbf{Câu 14 (1,0 điểm):} a) Đúng \quad b) Đúng \quad c) Sai \quad d) Sai.
\end{itemize}
\textit{Quy tắc chấm: Đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng 4 ý được 1,0đ.}

\vspace{2mm}
\noindent
\textbf{3. Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm -- Mỗi câu đúng 0,5 điểm)}
\begin{itemize}
  \item \textbf{Câu 15:} $x > 14$.
  \item \textbf{Câu 16:} $4$.
  \item \textbf{Câu 17:} $21{,}7\text{ m}$ (hoặc $21{,}7$).
  \item \textbf{Câu 18:} $141{,}3\text{ cm}^2$ (hoặc $141{,}3$).
\end{itemize}

\vspace{3mm}
\noindent
\textbf{\large B. LỜI GIẢI CHI TIẾT VÀ BAREM ĐIỂM TỰ LUẬN (3,0 ĐIỂM)}

\vspace{2mm}
\noindent
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Hệ phương trình: $\begin{cases} 2x + 5y = 11 \quad (1) \\ 3x - 2y = 7 \quad (2) \end{cases}$.\\
  Nhân (1) với 2 và nhân (2) với 5: $\begin{cases} 4x + 10y = 22 \\ 15x - 10y = 35 \end{cases}$ \dotfill \textbf{(0,25đ)}\\
  Cộng hai phương trình vế theo vế: $19x = 57 \iff x = 3$.\\
  Thay $x = 3$ vào (1): $2(3) + 5y = 11 \iff 5y = 5 \iff y = 1$.\\
  Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; 1)$. \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,5 điểm)} Với $x > 0, x \ne 1$, ta có:
  \[
  \dfrac{1}{\sqrt{x}-1} + \dfrac{1}{\sqrt{x}+1} = \dfrac{\sqrt{x}+1 + \sqrt{x}-1}{(\sqrt{x}-1)(\sqrt{x}+1)} = \dfrac{2\sqrt{x}}{x-1} \quad \text{\textbf{(0,25đ)}}
  \]
  Do đó:
  \[
  P = \dfrac{2\sqrt{x}}{x-1} : \dfrac{2\sqrt{x}}{x-1} = \dfrac{2\sqrt{x}}{x-1} \cdot \dfrac{x-1}{2\sqrt{x}} = 1 \quad \text{\textbf{(0,25đ)}}
  \]
\end{itemize}

\vspace{2mm}
\noindent
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)}
  Vì $MA, MB$ là hai tiếp tuyến của $(O)$ cắt nhau tại $M$ nên $MA = MB$.\\
  Lại có $OA = OB = R$, suy ra $OM$ là đường trung trực của đoạn thẳng $AB$.\\
  Do đó $OM \perp AB$ tại $H$ (đpcm). \dotfill \textbf{(0,5đ)}\\
  Xét tam giác $OAM$ vuông tại $A$, có đường cao $AH \perp OM$.\\
  Áp dụng hệ thức lượng: $MA^2 = MH \cdot MO$ (đpcm). \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,75 điểm)}
  Xét hai tam giác $MAC$ và $MDA$:\\
  Có góc $\widehat{M}$ chung, và $\widehat{MAC} = \widehat{MDA}$ (góc tạo bởi tiếp tuyến và dây cung cùng chắn cung $AC$).\\
  Suy ra $\triangle MAC \backsim \triangle MDA$ (g-g).\\
  Do đó $\dfrac{MA}{MD} = \dfrac{MC}{MA} \implies MA^2 = MC \cdot MD$. \dotfill \textbf{(0,25đ)}\\
  Từ câu a ta có $MA^2 = MH \cdot MO$, suy ra $MC \cdot MD = MH \cdot MO$. \dotfill \textbf{(0,25đ)}\\
  Từ $MC \cdot MD = MH \cdot MO \implies \dfrac{MC}{MO} = \dfrac{MH}{MD}$.\\
  Xét hai tam giác $MCH$ và $MOD$ có góc $\widehat{M}$ chung và $\dfrac{MC}{MO} = \dfrac{MH}{MD}$, nên $\triangle MCH \backsim \triangle MOD$ (c-g-c).\\
  Suy ra $\widehat{MHC} = \widehat{MDO}$. Do đó tứ giác $CHOD$ có góc ngoài bằng góc đối trong, suy ra bốn điểm $C, H, O, D$ cùng thuộc một đường tròn (đpcm). \dotfill \textbf{(0,25đ)}
\end{itemize}

\vspace{2mm}
\noindent
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)}
  Gọi chiều rộng của mảnh vườn là $x$ ($x > 0$, mét), chiều dài là $y$ ($y > 0$, mét).\\
  Diện tích mảnh vườn: $xy = 200 \implies y = \dfrac{200}{x}$.\\
  Chiều dài hàng rào bao quanh ba phía (gồm 2 chiều rộng và 1 chiều dài) là:
  \[
  L = 2x + y = 2x + \dfrac{200}{x}.
  \]
  Áp dụng bất đẳng thức Cô-si cho hai số dương $2x$ và $\dfrac{200}{x}$:
  \[
  L = 2x + \dfrac{200}{x} \ge 2\sqrt{2x \cdot \dfrac{200}{x}} = 2\sqrt{400} = 2 \cdot 20 = 40\text{ (m)}.
  \]
  Dấu ``='' xảy ra khi $2x = \dfrac{200}{x} \iff 2x^2 = 200 \iff x^2 = 100 \iff x = 10\text{ (m)}$ (do $x > 0$).\\
  Khi đó chiều dài là $y = \dfrac{200}{10} = 20\text{ (m)}$.\\
  Vậy để chiều dài hàng rào là ngắn nhất ($40\text{ m}$) thì chiều rộng là $10\text{ m}$ và chiều dài là $20\text{ m}$. \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,25 điểm)}
  Áp dụng bất đẳng thức Cauchy-Schwarz dạng phân thức (BĐT Engel):
  \[
  Q = \dfrac{a^2}{b+c} + \dfrac{b^2}{c+a} + \dfrac{c^2}{a+b} \ge \dfrac{(a+b+c)^2}{(b+c) + (c+a) + (a+b)} = \dfrac{(a+b+c)^2}{2(a+b+c)} = \dfrac{a+b+c}{2}.
  \]
  Mặt khác, với mọi $a, b, c > 0$ ta luôn có:
  \[
  (a+b+c)^2 \ge 3(ab+bc+ca) = 3 \cdot 3 = 9 \implies a+b+c \ge 3.
  \]
  Suy ra:
  \[
  Q \ge \dfrac{3}{2}.
  \]
  Dấu đẳng thức xảy ra khi $\begin{cases} a = b = c \\ ab+bc+ca=3 \end{cases} \iff a = b = c = 1$.\\
  Vậy giá trị nhỏ nhất của $Q$ là $\dfrac{3}{2}$, đạt được khi $a = b = c = 1$. \dotfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

md_sol_09 = '''# ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT - ĐỀ THI THỬ SỐ 09
**MÔN: TOÁN 9 - HỌC KỲ I - NĂM HỌC 2026 - 2027**
**ĐƠN VỊ: CHÙA HƯƠNG SƠN**

---

## A. ĐÁP ÁN TRẮC NGHIỆM (7,0 ĐIỂM)

### 1. Phần 1: Trắc nghiệm nhiều lựa chọn (3,0 điểm - 0,25đ/câu)
* Câu 1: **A** ($5\sqrt{2}$)
* Câu 2: **A** ($\cos 60^\circ = \dfrac{1}{2}$)
* Câu 3: **A** ($7x + 21 > 0$)
* Câu 4: **A** ($m - 3 > n - 3$)
* Câu 5: **A** ($18$)
* Câu 6: **A** ($x \ge 5$)
* Câu 7: **A** ($x - 4$)
* Câu 8: **A** ($-9$)
* Câu 9: **A** ($C = \pi d$)
* Câu 10: **A** (Không giao nhau)
* Câu 11: **A** (Đường tròn $(O)$ đựng $(O')$)
* Câu 12: **A** ($290^\circ$)

### 2. Phần 2: Trắc nghiệm Đúng - Sai (2,0 điểm)
* **Câu 13:** a) Đúng | b) Đúng | c) Sai | d) Đúng
* **Câu 14:** a) Đúng | b) Đúng | c) Sai | d) Sai

### 3. Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm - 0,5đ/câu)
* **Câu 15:** $x > 14$
* **Câu 16:** $4$
* **Câu 17:** $21{,}7\text{ m}$
* **Câu 18:** $141{,}3\text{ cm}^2$

---

## B. LỜI GIẢI CHI TIẾT TỰ LUẬN (3,0 ĐIỂM)

### Câu 19 (1,0 điểm)
* **a) (0,5 điểm)** Giải hệ:
  $$\\begin{cases} 2x + 5y = 11 \\\\ 3x - 2y = 7 \\end{cases} \\iff \\begin{cases} 4x + 10y = 22 \\\\ 15x - 10y = 35 \\end{cases} \\iff \\begin{cases} 19x = 57 \\\\ 2x + 5y = 11 \\end{cases} \\iff \\begin{cases} x = 3 \\\\ y = 1 \\end{cases}$$
  Nghiệm duy nhất: $(x; y) = (3; 1)$.
* **b) (0,5 điểm)** Với $x > 0, x \\ne 1$:
  $$P = \\left(\\dfrac{\\sqrt{x}+1 + \\sqrt{x}-1}{x-1}\\right) : \\dfrac{2\\sqrt{x}}{x-1} = \\dfrac{2\\sqrt{x}}{x-1} \\cdot \\dfrac{x-1}{2\\sqrt{x}} = 1.$$

### Câu 20 (1,5 điểm)
* **a) (0,75 điểm)**
  - $MA = MB$ (tính chất 2 tiếp tuyến cắt nhau), $OA = OB = R \\implies OM$ là trung trực $AB \\implies OM \\perp AB$ tại $H$ (0,5đ).
  - Tam giác $OAM$ vuông tại $A$, đường cao $AH \\implies MA^2 = MH \\cdot MO$ (hệ thức lượng) (0,25đ).
* **b) (0,75 điểm)**
  - $\\triangle MAC \\backsim \\triangle MDA$ (g-g) $\\implies \\dfrac{MA}{MD} = \\dfrac{MC}{MA} \\implies MA^2 = MC \\cdot MD$ (0,25đ).
  - Từ đó $MC \\cdot MD = MH \\cdot MO$ (0,25đ).
  - $\\implies \\dfrac{MC}{MO} = \\dfrac{MH}{MD} \\implies \\triangle MCH \\backsim \\triangle MOD$ (c-g-c) $\\implies \\widehat{MHC} = \\widehat{MDO}$. Suy ra $C, H, O, D$ cùng thuộc một đường tròn (0,25đ).

### Câu 21 (0,5 điểm)
* **a) (0,25 điểm)**
  - $xy = 200 \\implies y = \\dfrac{200}{x}$. Chiều dài rào: $L = 2x + \\dfrac{200}{x} \\ge 2\\sqrt{400} = 40\\text{ m}$.
  - Dấu bằng khi $2x^2 = 200 \\implies x = 10\\text{ m}, y = 20\\text{ m}$.
* **b) (0,25 điểm)**
  - Theo Cauchy-Schwarz dạng Engel: $Q \\ge \\dfrac{(a+b+c)^2}{2(a+b+c)} = \\dfrac{a+b+c}{2}$.
  - Lại có $(a+b+c)^2 \\ge 3(ab+bc+ca) = 9 \\implies a+b+c \\ge 3 \\implies Q \\ge \\dfrac{3}{2}$.
  - Đẳng thức khi $a = b = c = 1$. Giá trị nhỏ nhất là $\\dfrac{3}{2}$.
'''

# Write files
with open(os.path.join(folder_09, 'De_Thi_Thu_Toan_9_De_09.tex'), 'w', encoding='utf-8') as f:
    f.write(tex_exam_09)

with open(os.path.join(folder_09, 'DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_09.tex'), 'w', encoding='utf-8') as f:
    f.write(tex_sol_09)

with open(os.path.join(folder_09, 'DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_09.md'), 'w', encoding='utf-8') as f:
    f.write(md_sol_09)

print("Generated files for DE_09 successfully!")
