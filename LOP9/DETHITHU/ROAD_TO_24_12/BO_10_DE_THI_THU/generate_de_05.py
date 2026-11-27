import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

# ==============================================================================
# ĐỀ 05
# ==============================================================================
folder_05 = os.path.join(BASE_DIR, 'DE_05')
os.makedirs(folder_05, exist_ok=True)

tex_exam_05 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 05)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 05} & \textbf{MÔN: TOÁN -- LỚP 9} \\
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
\textbf{Câu 1.} Giá trị của biểu thức $\sqrt{32} - 2\sqrt{8} + \sqrt{18}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $3\sqrt{2}$. & \textbf{B.} $-3\sqrt{2}$. & \textbf{C.} $5\sqrt{2}$. & \textbf{D.} $0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Cho tam giác $MNP$ vuông tại $N$, góc nhọn $\widehat{P} = \alpha$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\tan \alpha = \dfrac{MN}{NP}$. & \textbf{B.} $\sin \alpha = \dfrac{NP}{MP}$. & \textbf{C.} $\cos \alpha = \dfrac{MN}{MP}$. & \textbf{D.} $\cot \alpha = \dfrac{MN}{NP}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $4x + 12 < 0$. & \textbf{B.} $0x + 7 \ge 0$. & \textbf{C.} $2x^2 + 3 > 0$. & \textbf{D.} $\dfrac{1}{x+1} > 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Nếu $a > b$ thì bất đẳng thức nào sau đây luôn đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-5a < -5b$. & \textbf{B.} $-5a > -5b$. & \textbf{C.} $a - 4 < b - 4$. & \textbf{D.} $2a + 3 < 2b + 3$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của số 196 là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $14$. & \textbf{B.} $14$ và $-14$. & \textbf{C.} $-14$. & \textbf{D.} $98$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Điều kiện xác định của căn thức $\sqrt{8 - 4x}$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \le 2$. & \textbf{B.} $x \ge 2$. & \textbf{C.} $x < 2$. & \textbf{D.} $x > 2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x \ge 9$, giá trị của biểu thức $\sqrt{(x-9)^2}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x - 9$. & \textbf{B.} $9 - x$. & \textbf{C.} $-(x-9)$. & \textbf{D.} $(x-9)^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của biểu thức $\sqrt[3]{-729}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-9$. & \textbf{B.} $9$. & \textbf{C.} $-81$. & \textbf{D.} $81$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Độ dài của cung tròn có số đo $90^\circ$ trong đường tròn bán kính $R$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\dfrac{\pi R}{2}$. & \textbf{B.} $\pi R$. & \textbf{C.} $\dfrac{\pi R^2}{2}$. & \textbf{D.} $2\pi R$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 8\text{ cm})$ và đường thẳng $d$. Biết khoảng cách từ $O$ đến $d$ là $5\text{ cm}$. Vị trí tương đối của $d$ và $(O)$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Cắt nhau. & \textbf{B.} Tiếp xúc nhau. & \textbf{C.} Không giao nhau. & \textbf{D.} Trùng nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 10\text{ cm})$ và $(O'; 4\text{ cm})$. Biết khoảng cách hai tâm $OO' = 6\text{ cm}$. Vị trí tương đối của $(O)$ và $(O')$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc trong. & \textbf{B.} Tiếp xúc ngoài. & \textbf{C.} Cắt nhau. & \textbf{D.} Ở ngoài nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Trên đường tròn $(O)$, cho góc ở tâm $\widehat{EOF} = 120^\circ$. Số đo của cung nhỏ $EF$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $120^\circ$. & \textbf{B.} $60^\circ$. & \textbf{C.} $240^\circ$. & \textbf{D.} $180^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Xét bài toán thực tế: ``Tháng trước, hai hộ gia đình nhà bác An và bác Bình đã dùng hết tổng cộng $85\text{ m}^3$ nước sinh hoạt. Tháng này, nhờ có ý thức tiết kiệm nước, nhà bác An đã giảm được $10\%$ lượng nước tiêu thụ, nhà bác Bình giảm được $15\%$ lượng nước tiêu thụ so với tháng trước, nên cả hai nhà chỉ dùng hết $74\text{ m}^3$ nước. Gọi lượng nước tiêu thụ trong tháng trước của nhà bác An và nhà bác Bình lần lượt là $x$ và $y$ ($\text{m}^3, x, y \in \mathbb{N}^*, x, y < 85$).''\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Tháng trước cả hai nhà dùng $85\text{ m}^3$ nên ta có phương trình: $x + y = 85$. & & \\
\hline
b) Lượng nước tiêu thụ tháng này của nhà bác An là $0{,}9x$ và nhà bác Bình là $0{,}85y$. & & \\
\hline
c) Phương trình biểu thị lượng nước tiêu thụ tháng này là: $0{,}9x + 0{,}85y = 80$. & & \\
\hline
d) Tháng trước, nhà bác An đã dùng $50\text{ m}^3$ và nhà bác Bình đã dùng $35\text{ m}^3$ nước. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho tam giác nhọn $ABC$ nội tiếp đường tròn $(O; R)$. Các đường cao $AD, BE, CF$ của tam giác $ABC$ cắt nhau tại trực tâm $H$.\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Bốn điểm $B, F, H, D$ cùng nằm trên đường tròn đường kính $BH$. & & \\
\hline
b) Tứ giác $BCEF$ là tứ giác có bốn điểm cùng thuộc một đường tròn. & & \\
\hline
c) Bán kính đường tròn ngoại tiếp tứ giác $BCEF$ là $\dfrac{BC}{2}$. & & \\
\hline
d) Đường thẳng nối tâm $O$ và đỉnh $A$ song song với đoạn thẳng $EF$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Nghiệm của bất phương trình $3(2x - 1) + 4 > 4(x + 2) - 1$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Giá trị của biểu thức $H = \sqrt{(\sqrt{11} - 4)^2} + \sqrt{11}$ bằng $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Một cây xanh bị bão làm gãy ngang thân. Ngọn cây gãy chạm đất cách gốc cây một khoảng $6\text{ m}$ và tạo với mặt đất một góc $35^\circ$ (xem hình vẽ bên). Tính chiều cao ban đầu của cây xanh trước khi bị gãy (làm tròn kết quả đến chữ số thập phân thứ hai của mét).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Mặt đất
  \draw[thick] (-0.5,0) -- (4.0,0);
  \fill[pattern=north east lines, pattern color=gray!50] (-0.5,-0.2) rectangle (4.0,0);
  % Gốc và thân đứng
  \draw[thick, fill=brown!70] (0,0) rectangle (0.3,1.8);
  % Điểm gãy và thân gãy chạm đất
  \draw[thick, line width=1.5pt, brown!80!black] (0.3,1.8) -- (2.8,0);
  % Tán lá ngọn cây
  \draw[fill=green!60!black] (2.8,0) circle (0.35);
  \node[above] at (0.3, 1.8) {\footnotesize Điểm gãy};
  \node[left] at (0, 0.9) {$h_1$};
  \node[above right] at (1.5, 0.9) {$h_2$};
  % Góc vuông
  \draw (0.3,0) rectangle (0.6,0.3);
  % Góc 35 độ
  \draw (2.8,0) ++(180:0.6) arc (180:145:0.6);
  \node at (2.2, 0.3) {\footnotesize $35^\circ$};
  \node[below] at (1.4, 0) {$6\text{ m}$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một hình quạt tròn có bán kính $R = 12\text{ cm}$ và góc ở tâm tương ứng là $60^\circ$. Tính diện tích của hình quạt tròn đó (lấy $\pi \approx 3{,}14$, làm tròn kết quả đến hàng phần mười, đơn vị: $\text{cm}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 3x + 2y = 12 \\ x - 2y = -4 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $Q = \left( \dfrac{1}{\sqrt{x}+2} + \dfrac{1}{\sqrt{x}-2} \right) \cdot \dfrac{x - 4}{2\sqrt{x}}$ với $x > 0, x \ne 4$. Rút gọn biểu thức $Q$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho tam giác nhọn $ABC$ nội tiếp đường tròn $(O; R)$. Các đường cao $AD, BE$ của tam giác $ABC$ cắt nhau tại $H$. Kẻ đường kính $AK$ của đường tròn $(O)$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng bốn điểm $A, E, H, D$ cùng nằm trên một đường tròn.
  \item[b)] \textit{(0,75 điểm)} Chứng minh rằng: Tứ giác $BHCK$ là hình bình hành.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Một trang trại cần thiết kế một bồn chứa nước hình trụ bằng inox có thể tích $V = 16\pi\text{ m}^3$ có nắp đậy. Hãy tìm bán kính đáy $R$ và chiều cao $h$ của hình trụ để tổng diện tích vật liệu inox toàn phần là nhỏ nhất.
  \item[b)] \textit{(0,25 điểm)} Cho ba số thực dương $a, b, c$ thỏa mãn điều kiện $ab + bc + ca = 3$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  P = \dfrac{a}{b^2 + 1} + \dfrac{b}{c^2 + 1} + \dfrac{c}{a^2 + 1}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

tex_sol_05 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐÁP ÁN CHI TIẾT ĐỀ THI THỬ SỐ 05}}
\cfoot{\thepage}

\begin{document}

\begin{center}
{\large\bfseries ĐÁP ÁN \& HƯỚNG DẪN CHẤM ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 05)}\\[1.5mm]
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
\textbf{Câu 13} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Đ} & Ý c) sai vì lượng nước tháng này bằng $74\text{ m}^3$ (đề ghi $80$). \\
\hline
\textbf{Câu 14} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & Ý d) sai vì $OA \perp EF$ (chứ không song song). \\
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
\textbf{Câu 15} & Nghiệm bất phương trình $3(2x - 1) + 4 > 4(x + 2) - 1$ & \textbf{$x > 3$} & 0,5đ \\
\hline
\textbf{Câu 16} & Giá trị biểu thức $H = \sqrt{(\sqrt{11}-4)^2} + \sqrt{11}$ & \textbf{$4$} & 0,5đ \\
\hline
\textbf{Câu 17} & Chiều cao cây trước khi gãy ($6 \cdot \tan 35^\circ + \dfrac{6}{\cos 35^\circ}$) & \textbf{$11{,}52\text{ m}$} & 0,5đ \\
\hline
\textbf{Câu 18} & Diện tích hình quạt tròn ($\dfrac{3{,}14 \times 12^2 \times 60}{360}$) & \textbf{$75{,}4\text{ cm}^2$} & 0,5đ \\
\hline
\end{tabular}
\end{center}

\vspace{3mm}
\noindent
\textbf{\large PHẦN II. TỰ LUẬN (3,0 ĐIỂM)}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Cộng hai phương trình: $4x = 8 \Leftrightarrow x = 2$. Thay vào phương trình thứ hai: $2 - 2y = -4 \Leftrightarrow 2y = 6 \Leftrightarrow y = 3$. Hệ có nghiệm duy nhất: $(x; y) = (2; 3)$. \hfill \textbf{(0,5đ)}
  \item[b)] \textit{(0,5 điểm)} Quy đồng: $Q = \dfrac{\sqrt{x}-2+\sqrt{x}+2}{(\sqrt{x}+2)(\sqrt{x}-2)} \cdot \dfrac{x-4}{2\sqrt{x}} = \dfrac{2\sqrt{x}}{x-4} \cdot \dfrac{x-4}{2\sqrt{x}} = 1$. \hfill \textbf{(0,5đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Vì $AD \perp BC \Rightarrow \widehat{ADH} = 90^\circ$; $BE \perp AC \Rightarrow \widehat{AEH} = 90^\circ$. Gọi $I$ là trung điểm $AH \Rightarrow IA = IE = IH = ID = \dfrac{AH}{2} \Rightarrow A, E, H, D$ cùng nằm trên đường tròn đường kính $AH$. \hfill \textbf{(0,75đ)}
  \item[b)] \textit{(0,75 điểm)} Vì $AK$ là đường kính của $(O) \Rightarrow \widehat{ABK} = 90^\circ \Rightarrow BK \perp AB$. Lại có $CH \perp AB \Rightarrow CH \parallel BK$. Tương tự: $\widehat{ACK} = 90^\circ \Rightarrow CK \perp AC$. Lại có $BH \perp AC \Rightarrow BH \parallel CK$. Tứ giác $BHCK$ có các cặp cạnh đối song song nên là hình bình hành (đpcm). \hfill \textbf{(0,75đ)}
\end{itemize}

\vspace{1mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Thể tích $V = \pi R^2 h = 16\pi \Rightarrow h = \dfrac{16}{R^2}$. Diện tích toàn phần:
  $S_{tp} = 2\pi R^2 + 2\pi R h = 2\pi R^2 + \dfrac{32\pi}{R} = 2\pi R^2 + \dfrac{16\pi}{R} + \dfrac{16\pi}{R} \ge 3\sqrt[3]{2\pi R^2 \cdot \dfrac{16\pi}{R} \cdot \dfrac{16\pi}{R}} = 3\sqrt[3]{512\pi^3} = 24\pi\text{ m}^2$. Dấu ``='' xảy ra khi $2\pi R^2 = \dfrac{16\pi}{R} \Leftrightarrow R^3 = 8 \Leftrightarrow R = 2\text{ m} \Rightarrow h = 4\text{ m}$. \hfill \textbf{(0,25đ)}
  \item[b)] \textit{(0,25 điểm)} Kỹ thuật Cauchy ngược dấu: $\dfrac{a}{b^2+1} = a - \dfrac{ab^2}{b^2+1} \ge a - \dfrac{ab^2}{2b} = a - \dfrac{ab}{2}$. Tương tự: $\dfrac{b}{c^2+1} \ge b - \dfrac{bc}{2}$ và $\dfrac{c}{a^2+1} \ge c - \dfrac{ca}{2}$. Cộng lại: $P \ge (a+b+c) - \dfrac{ab+bc+ca}{2} \ge \sqrt{3(ab+bc+ca)} - \dfrac{3}{2} = 3 - \dfrac{3}{2} = \dfrac{3}{2}$. Dấu ``='' xảy ra khi $a = b = c = 1$. Vậy $\min P = \dfrac{3}{2}$. \hfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

md_sol_05 = r'''# ĐÁP ÁN & HƯỚNG DẪN CHẤM ĐỀ THI THỬ VÀO 10 (ĐỀ SỐ 05)
### ĐƠN VỊ: CHÙA HƯƠNG SƠN | MÔN: TOÁN – LỚP 9 | NĂM HỌC 2026 – 2027

## PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,0 ĐIỂM)
### 1. BẢNG ĐÁP ÁN PHẦN 1: TRẮC NGHIỆM NHIỀU LỰA CHỌN (3,0 điểm)
| Câu | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Đáp án** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** | **A** |

### 2. BẢNG ĐÁP ÁN PHẦN 2: TRẮC NGHIỆM ĐÚNG / SAI (2,0 điểm)
| Câu | Ý a | Ý b | Ý c | Ý d | Ghi chú |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Câu 13** | **Đ** | **Đ** | **S** | **Đ** | Ý c) sai vì lượng nước thực tế là 74 m3. |
| **Câu 14** | **Đ** | **Đ** | **Đ** | **S** | Ý d) sai vì $OA \perp EF$. |

### 3. BẢNG ĐÁP ÁN PHẦN 3: TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 điểm)
* Câu 15: **$x > 3$**
* Câu 16: **$4$**
* Câu 17: **$11{,}52\text{ m}$**
* Câu 18: **$75{,}4\text{ cm}^2$**

## PHẦN II. TỰ LUẬN (3,0 ĐIỂM)
* **Câu 19a (0,5đ):** $(x; y) = (2; 3)$.
* **Câu 19b (0,5đ):** $Q = 1$.
* **Câu 20a (0,75đ):** $A, E, H, D$ cùng thuộc đường tròn đường kính $AH$.
* **Câu 20b (0,75đ):** $BHCK$ là hình bình hành vì có các cặp cạnh đối song song.
* **Câu 21a (0,25đ):** $R = 2\text{ m}, h = 4\text{ m}$, $S_{\min} = 24\pi\text{ m}^2$.
* **Câu 21b (0,25đ):** $\min P = \dfrac{3}{2}$ khi $a = b = c = 1$.
'''

with open(f'{folder_05}/De_Thi_Thu_Toan_9_De_05.tex', 'w', encoding='utf-8') as f:
    f.write(tex_exam_05)

with open(f'{folder_05}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_05.tex', 'w', encoding='utf-8') as f:
    f.write(tex_sol_05)

with open(f'{folder_05}/DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_05.md', 'w', encoding='utf-8') as f:
    f.write(md_sol_05)

print("Generated files for DE_05 successfully!")
