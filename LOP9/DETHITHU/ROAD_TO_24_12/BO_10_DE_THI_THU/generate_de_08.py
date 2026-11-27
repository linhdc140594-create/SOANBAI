import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

folder_08 = os.path.join(BASE_DIR, 'DE_08')
os.makedirs(folder_08, exist_ok=True)

tex_exam_08 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 08)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 08} & \textbf{MÔN: TOÁN -- LỚP 9} \\
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
\textbf{Câu 1.} Giá trị của biểu thức $4\sqrt{12} - 3\sqrt{27} + \sqrt{75}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $4\sqrt{3}$. & \textbf{B.} $5\sqrt{3}$. & \textbf{C.} $3\sqrt{3}$. & \textbf{D.} $6\sqrt{3}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Cho tam giác $ABC$ vuông tại $A$ có góc $\widehat{B} = \beta$. Khi đó $\tan \beta$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\dfrac{AC}{AB}$. & \textbf{B.} $\dfrac{AB}{AC}$. & \textbf{C.} $\dfrac{AC}{BC}$. & \textbf{D.} $\dfrac{AB}{BC}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $4x - 12 \le 0$. & \textbf{B.} $0x + 8 > 0$. & \textbf{C.} $2x^2 + 3 \ge 0$. & \textbf{D.} $\dfrac{5}{x} - 2 < 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Cho hai số thực $a$ và $b$ thỏa mãn $a < b$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-3a > -3b$. & \textbf{B.} $-3a < -3b$. & \textbf{C.} $2a + 1 > 2b + 1$. & \textbf{D.} $a - 4 > b - 4$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của 196 là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $14$. & \textbf{B.} $-14$. & \textbf{C.} $14$ và $-14$. & \textbf{D.} $38416$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Điều kiện xác định của căn thức $\sqrt{5 - x}$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \le 5$. & \textbf{B.} $x \ge 5$. & \textbf{C.} $x < 5$. & \textbf{D.} $x > 5$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x < 3$, biểu thức $\sqrt{(x-3)^2}$ có giá trị rút gọn bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $3 - x$. & \textbf{B.} $x - 3$. & \textbf{C.} $-(3 - x)$. & \textbf{D.} $(x-3)^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của biểu thức $\sqrt[3]{-512}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-8$. & \textbf{B.} $8$. & \textbf{C.} $-64$. & \textbf{D.} $64$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Công thức tính diện tích hình tròn có bán kính $R$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $S = \pi R^2$. & \textbf{B.} $S = 2\pi R$. & \textbf{C.} $S = 4\pi R^2$. & \textbf{D.} $S = \pi R$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 6\text{ cm})$ và đường thẳng $a$. Khoảng cách từ $O$ đến đường thẳng $a$ bằng $4\text{ cm}$. Vị trí tương đối của $a$ và $(O)$ là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Cắt nhau. & \textbf{B.} Tiếp xúc nhau. & \textbf{C.} Không giao nhau. & \textbf{D.} Song song.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 7\text{ cm})$ và $(O'; 3\text{ cm})$. Biết đoạn nối tâm $OO' = 10\text{ cm}$. Vị trí tương đối của hai đường tròn là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Tiếp xúc ngoài. & \textbf{B.} Tiếp xúc trong. & \textbf{C.} Cắt nhau. & \textbf{D.} Ngoài nhau.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Trên đường tròn $(O)$, góc ở tâm $\widehat{AOB} = 60^\circ$ chắn cung nhỏ $AB$. Số đo của cung nhỏ $AB$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $60^\circ$. & \textbf{B.} $30^\circ$. & \textbf{C.} $120^\circ$. & \textbf{D.} $300^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Một ca nô chạy trên một khúc sông từ bến A đến bến B cách nhau $90\text{ km}$ rồi quay trở lại từ B về A. Thời gian ca nô đi xuôi dòng ít hơn thời gian đi ngược dòng là $45\text{ phút}$ ($= \dfrac{3}{4}\text{ giờ}$). Biết vận tốc của dòng nước là $3\text{ km/h}$. Gọi vận tốc riêng của ca nô trong nước yên lặng là $v$ ($v > 3$, đơn vị: $\text{km/h}$).\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Vận tốc khi xuôi dòng là $v + 3$ (km/h) và khi ngược dòng là $v - 3$ (km/h). & & \\
\hline
b) Thời gian ca nô đi xuôi dòng từ A đến B là $\dfrac{90}{v+3}$ (giờ). & & \\
\hline
c) Phương trình biểu thị mối quan hệ thời gian đi là: $\dfrac{90}{v-3} - \dfrac{90}{v+3} = \dfrac{3}{4}$. & & \\
\hline
d) Vận tốc riêng của ca nô trong nước yên lặng là $25\text{ km/h}$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho đường tròn $(O; 10\text{ cm})$, đường kính $AB$. Dây cung $CD$ vuông góc với đường kính $AB$ tại điểm $H$ sao cho khoảng cách từ tâm $O$ đến dây $CD$ là $OH = 6\text{ cm}$.\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Điểm $H$ là trung điểm của dây cung $CD$. & & \\
\hline
b) Độ dài đoạn thẳng $CH = 8\text{ cm}$. & & \\
\hline
c) Độ dài dây cung $CD = 14\text{ cm}$. & & \\
\hline
d) Diện tích tứ giác $ACBD$ bằng $160\text{ cm}^2$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Tập nghiệm của bất phương trình $2(x - 3) + 7 > 5x - 8$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Rút gọn biểu thức $K = \sqrt{(\sqrt{7} - 3)^2} + \sqrt{7}$ ta được kết quả là $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Một người đứng cách chân ngọn hải đăng một khoảng nằm ngang $d = 40\text{ m}$. Từ vị trí đặt máy đo cao $1{,}5\text{ m}$ so với mặt đất, người đó đo được góc nâng nhìn lên đỉnh ngọn hải đăng là $35^\circ$ (xem hình vẽ bên). Tính chiều cao của ngọn hải đăng (làm tròn kết quả đến hàng phần mười của mét).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Mặt đất
  \draw[thick] (-0.5,0) -- (4.2,0);
  % Ngọn hải đăng
  \draw[thick, fill=orange!20] (3.2,0) -- (3.4,3.5) -- (3.8,3.5) -- (4.0,0) -- cycle;
  \draw[thick, fill=yellow!60] (3.3,3.5) rectangle (3.9,4.0);
  \draw[thick] (3.3,4.0) -- (3.6,4.4) -- (3.9,4.0) -- cycle;
  % Điểm quan sát và máy ngắm
  \draw[thick] (0,0) -- (0,1.2);
  \node[left] at (0,0.6) {\footnotesize $1{,}5\text{ m}$};
  \draw[dashed] (0,1.2) -- (3.5,1.2);
  \draw[thick, blue, line width=1.1pt] (0,1.2) -- (3.6,4.0);
  % Ký hiệu khoảng cách nằm ngang
  \draw[<->] (0,-0.3) -- (3.6,-0.3);
  \node[below] at (1.8,-0.3) {\footnotesize $40\text{ m}$};
  % Góc nâng 35 độ
  \draw (0,1.2) ++(0:0.8) arc (0:35:0.8);
  \node at (1.2,1.55) {\footnotesize $35^\circ$};
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một bồn hoa hình quạt tròn có bán kính $R = 6\text{ m}$ và góc ở tâm tương ứng bằng $60^\circ$. Tính diện tích của bồn hoa đó (lấy $\pi \approx 3{,}14$, đơn vị: $\text{m}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 4x - 3y = 7 \\ 3x + 2y = 1 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $B = \left( \dfrac{\sqrt{x}}{\sqrt{x}-3} - \dfrac{3}{\sqrt{x}+3} \right) : \dfrac{x+9}{x-9}$ với $x \ge 0, x \ne 9$. Rút gọn biểu thức $B$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho đường tròn $(O; R)$, đường kính $AB$. Lấy điểm $M$ bất kỳ trên $(O)$ ($M \ne A, B$). Tiếp tuyến tại $M$ cắt các tiếp tuyến tại $A$ và $B$ của $(O)$ lần lượt ở $C$ và $D$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng $CD = AC + BD$ và $\widehat{COD} = 90^\circ$.
  \item[b)] \textit{(0,75 điểm)} Chứng minh rằng $AC \cdot BD = R^2$ và đường tròn đường kính $CD$ tiếp xúc với đường thẳng $AB$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Bác Ba muốn làm một bể chứa nước bằng tôn dạng hình trụ không có nắp đậy với thể tích $V = 27\pi\text{ m}^3$. Hỏi bán kính đáy $R$ và chiều cao $h$ bằng bao nhiêu mét để lượng tôn dùng làm bể (diện tích toàn phần không nắp) là nhỏ nhất?
  \item[b)] \textit{(0,25 điểm)} Cho hai số thực dương $x, y$ thỏa mãn điều kiện $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  P = \dfrac{1}{x^2 + y^2} + \dfrac{1}{xy}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

tex_sol_08 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐÁP ÁN \& LỜI GIẢI CHI TIẾT (ĐỀ SỐ 08)}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\large HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ THI THỬ SỐ 08}\\
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
  \item \textbf{Câu 13 (1,0 điểm):} a) Đúng \quad b) Đúng \quad c) Đúng \quad d) Sai.
  \item \textbf{Câu 14 (1,0 điểm):} a) Đúng \quad b) Đúng \quad c) Sai \quad d) Đúng.
\end{itemize}
\textit{Quy tắc chấm: Đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng 4 ý được 1,0đ.}

\vspace{2mm}
\noindent
\textbf{3. Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm -- Mỗi câu đúng 0,5 điểm)}
\begin{itemize}
  \item \textbf{Câu 15:} $x < 3$.
  \item \textbf{Câu 16:} $3$.
  \item \textbf{Câu 17:} $29{,}5\text{ m}$ (hoặc $29{,}5$).
  \item \textbf{Câu 18:} $18{,}84\text{ m}^2$ (hoặc $18{,}84$).
\end{itemize}

\vspace{3mm}
\noindent
\textbf{\large B. LỜI GIẢI CHI TIẾT VÀ BAREM ĐIỂM TỰ LUẬN (3,0 ĐIỂM)}

\vspace{2mm}
\noindent
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Hệ phương trình: $\begin{cases} 4x - 3y = 7 \quad (1) \\ 3x + 2y = 1 \quad (2) \end{cases}$.\\
  Nhân phương trình $(1)$ với $2$ và nhân phương trình $(2)$ với $3$, ta được:
  $\begin{cases} 8x - 6y = 14 \\ 9x + 6y = 3 \end{cases}$ \dotfill \textbf{(0,25đ)}\\
  Cộng hai phương trình vế theo vế: $17x = 17 \iff x = 1$.\\
  Thay $x = 1$ vào phương trình $(2)$: $3(1) + 2y = 1 \iff 2y = -2 \iff y = -1$.\\
  Vậy hệ phương trình có nghiệm duy nhất là $(x; y) = (1; -1)$. \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,5 điểm)} Với $x \ge 0, x \ne 9$, ta có:
  \[
  \dfrac{\sqrt{x}}{\sqrt{x}-3} - \dfrac{3}{\sqrt{x}+3} = \dfrac{\sqrt{x}(\sqrt{x}+3) - 3(\sqrt{x}-3)}{(\sqrt{x}-3)(\sqrt{x}+3)} = \dfrac{x + 3\sqrt{x} - 3\sqrt{x} + 9}{x - 9} = \dfrac{x+9}{x-9} \quad \text{\textbf{(0,25đ)}}
  \]
  Do đó:
  \[
  B = \dfrac{x+9}{x-9} : \dfrac{x+9}{x-9} = \dfrac{x+9}{x-9} \cdot \dfrac{x-9}{x+9} = 1 \quad \text{\textbf{(0,25đ)}}
  \]
\end{itemize}

\vspace{2mm}
\noindent
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)}
  Theo tính chất của hai tiếp tuyến cắt nhau:
  $CA = CM$ và $DB = DM$. Suy ra $CD = CM + DM = CA + BD$ (đpcm). \dotfill \textbf{(0,25đ)}\\
  Mặt khác, $OC$ là tia phân giác của $\widehat{AOM}$ nên $\widehat{COM} = \dfrac{1}{2}\widehat{AOM}$.\\
  $OD$ là tia phân giác của $\widehat{BOM}$ nên $\widehat{DOM} = \dfrac{1}{2}\widehat{BOM}$. \dotfill \textbf{(0,25đ)}\\
  Do hai góc $\widehat{AOM}$ và $\widehat{BOM}$ kề bù nên:
  $\widehat{COD} = \widehat{COM} + \widehat{DOM} = \dfrac{1}{2}(\widehat{AOM} + \widehat{BOM}) = \dfrac{1}{2} \cdot 180^\circ = 90^\circ$ (đpcm). \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,75 điểm)}
  Xét tam giác $COD$ vuông tại $O$, có đường cao $OM \perp CD$ (vì $CD$ là tiếp tuyến tại $M$).\\
  Áp dụng hệ thức lượng: $CM \cdot MD = OM^2 = R^2$.\\
  Mà $CM = AC$ và $MD = BD$, suy ra $AC \cdot BD = R^2$ (đpcm). \dotfill \textbf{(0,5đ)}\\
  Gọi $I$ là trung điểm của $CD$. Khi đó $I$ là tâm của đường tròn đường kính $CD$, bán kính $r = \dfrac{CD}{2}$.\\
  Tứ giác $ABDC$ là hình thang vuông ($AC \parallel BD \perp AB$) có $O$ là trung điểm $AB$ và $I$ là trung điểm $CD$, nên $OI$ là đường trung bình của hình thang $ABDC$.\\
  Suy ra $OI \parallel AC \implies OI \perp AB$ tại $O$, và $OI = \dfrac{AC + BD}{2} = \dfrac{CD}{2} = r$.\\
  Vậy đường tròn $(I; r)$ đường kính $CD$ tiếp xúc với đường thẳng $AB$ tại $O$. \dotfill \textbf{(0,25đ)}
\end{itemize}

\vspace{2mm}
\noindent
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)}
  Thể tích bể hình trụ không nắp là $V = \pi R^2 h = 27\pi \implies h = \dfrac{27}{R^2}$.\\
  Diện tích tôn cần dùng (diện tích toàn phần không nắp) là:
  \[
  S = \pi R^2 + 2\pi R h = \pi R^2 + 2\pi R \cdot \dfrac{27}{R^2} = \pi \left( R^2 + \dfrac{54}{R} \right) = \pi \left( R^2 + \dfrac{27}{R} + \dfrac{27}{R} \right).
  \]
  Áp dụng bất đẳng thức Cô-si cho 3 số dương $R^2, \dfrac{27}{R}, \dfrac{27}{R}$:
  \[
  R^2 + \dfrac{27}{R} + \dfrac{27}{R} \ge 3\sqrt[3]{R^2 \cdot \dfrac{27}{R} \cdot \dfrac{27}{R}} = 3\sqrt[3]{729} = 3 \cdot 9 = 27.
  \]
  Dấu ``='' xảy ra khi $R^2 = \dfrac{27}{R} \iff R^3 = 27 \iff R = 3\text{ (m)}$. Khi đó $h = \dfrac{27}{3^2} = 3\text{ (m)}$.\\
  Vậy để tốn ít tôn nhất thì $R = 3\text{ m}$ và $h = 3\text{ m}$. \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,25 điểm)}
  Với $x, y > 0$, ta có:
  \[
  P = \dfrac{1}{x^2 + y^2} + \dfrac{1}{xy} = \left( \dfrac{1}{x^2 + y^2} + \dfrac{1}{2xy} \right) + \dfrac{1}{2xy}.
  \]
  Áp dụng bất đẳng thức $\dfrac{1}{a} + \dfrac{1}{b} \ge \dfrac{4}{a+b}$ cho hai số dương $x^2+y^2$ và $2xy$:
  \[
  \dfrac{1}{x^2 + y^2} + \dfrac{1}{2xy} \ge \dfrac{4}{x^2 + y^2 + 2xy} = \dfrac{4}{(x+y)^2} = \dfrac{4}{2^2} = 1.
  \]
  Mặt khác, $xy \le \dfrac{(x+y)^2}{4} = \dfrac{4}{4} = 1 \implies \dfrac{1}{2xy} \ge \dfrac{1}{2 \cdot 1} = \dfrac{1}{2}$.\\
  Suy ra: $P \ge 1 + \dfrac{1}{2} = \dfrac{3}{2}$.\\
  Dấu đẳng thức xảy ra khi $\begin{cases} x^2 + y^2 = 2xy \\ x = y \\ x + y = 2 \end{cases} \iff x = y = 1$.\\
  Vậy giá trị nhỏ nhất của $P$ bằng $\dfrac{3}{2}$, đạt được khi $x = y = 1$. \dotfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

md_sol_08 = '''# ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT - ĐỀ THI THỬ SỐ 08
**MÔN: TOÁN 9 - HỌC KỲ I - NĂM HỌC 2026 - 2027**
**ĐƠN VỊ: CHÙA HƯƠNG SƠN**

---

## A. ĐÁP ÁN TRẮC NGHIỆM (7,0 ĐIỂM)

### 1. Phần 1: Trắc nghiệm nhiều lựa chọn (3,0 điểm - 0,25đ/câu)
* Câu 1: **A** ($4\sqrt{3}$)
* Câu 2: **A** ($\tan \beta = \dfrac{AC}{AB}$)
* Câu 3: **A** ($4x - 12 \le 0$)
* Câu 4: **A** ($-3a > -3b$)
* Câu 5: **A** ($14$)
* Câu 6: **A** ($x \le 5$)
* Câu 7: **A** ($3 - x$)
* Câu 8: **A** ($-8$)
* Câu 9: **A** ($S = \pi R^2$)
* Câu 10: **A** (Cắt nhau)
* Câu 11: **A** (Tiếp xúc ngoài)
* Câu 12: **A** ($60^\circ$)

### 2. Phần 2: Trắc nghiệm Đúng - Sai (2,0 điểm)
* **Câu 13:** a) Đúng | b) Đúng | c) Đúng | d) Sai
* **Câu 14:** a) Đúng | b) Đúng | c) Sai | d) Đúng

### 3. Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm - 0,5đ/câu)
* **Câu 15:** $x < 3$
* **Câu 16:** $3$
* **Câu 17:** $29{,}5\text{ m}$
* **Câu 18:** $18{,}84\text{ m}^2$

---

## B. LỜI GIẢI CHI TIẾT TỰ LUẬN (3,0 ĐIỂM)

### Câu 19 (1,0 điểm)
* **a) (0,5 điểm)** Giải hệ phương trình:
  $$\\begin{cases} 4x - 3y = 7 \\\\ 3x + 2y = 1 \\end{cases} \\iff \\begin{cases} 8x - 6y = 14 \\\\ 9x + 6y = 3 \\end{cases} \\iff \\begin{cases} 17x = 17 \\\\ 2y = 1 - 3x \\end{cases} \\iff \\begin{cases} x = 1 \\\\ y = -1 \\end{cases}$$
  Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (1; -1)$.
* **b) (0,5 điểm)** Rút gọn với $x \\ge 0, x \\ne 9$:
  $$B = \\left(\\dfrac{\\sqrt{x}(\\sqrt{x}+3) - 3(\\sqrt{x}-3)}{x-9}\\right) : \\dfrac{x+9}{x-9} = \\dfrac{x+9}{x-9} \\cdot \\dfrac{x-9}{x+9} = 1.$$

### Câu 20 (1,5 điểm)
* **a) (0,75 điểm)**
  - Theo tính chất hai tiếp tuyến cắt nhau: $CA = CM$ và $DB = DM \\implies CD = AC + BD$ (0,25đ).
  - $OC, OD$ lần lượt là tia phân giác của $\\widehat{AOM}$ và $\\widehat{BOM}$ (0,25đ).
  - Vì $\\widehat{AOM}$ và $\\widehat{BOM}$ là hai góc kề bù nên $\\widehat{COD} = 90^\\circ$ (0,25đ).
* **b) (0,75 điểm)**
  - Tam giác $COD$ vuông tại $O$, đường cao $OM = R \\implies CM \\cdot MD = OM^2 = R^2 \\implies AC \\cdot BD = R^2$ (0,5đ).
  - Gọi $I$ là trung điểm $CD$, $OI$ là đường trung bình hình thang $ABDC \\implies OI \\perp AB$ và $OI = \\dfrac{CD}{2} = r$. Vậy đường tròn đường kính $CD$ tiếp xúc với $AB$ tại $O$ (0,25đ).

### Câu 21 (0,5 điểm)
* **a) (0,25 điểm)**
  - $V = \\pi R^2 h = 27\\pi \\implies h = \\dfrac{27}{R^2}$.
  - $S = \\pi R^2 + 2\\pi Rh = \\pi \\left(R^2 + \\dfrac{27}{R} + \\dfrac{27}{R}\\right) \\ge 3\\pi \\sqrt[3]{R^2 \\cdot \\dfrac{27}{R} \\cdot \\dfrac{27}{R}} = 27\\pi$.
  - Dấu bằng khi $R^3 = 27 \\implies R = 3\\text{ m}, h = 3\\text{ m}$.
* **b) (0,25 điểm)**
  - $P = \\left(\\dfrac{1}{x^2+y^2} + \\dfrac{1}{2xy}\\right) + \\dfrac{1}{2xy} \\ge \\dfrac{4}{(x+y)^2} + \\dfrac{1}{2 \\cdot \\frac{(x+y)^2}{4}} = \\dfrac{4}{4} + \\dfrac{1}{2} = \\dfrac{3}{2}$.
  - Đẳng thức xảy ra khi $x = y = 1$. Giá trị nhỏ nhất là $\\dfrac{3}{2}$.
'''

# Write files
with open(os.path.join(folder_08, 'De_Thi_Thu_Toan_9_De_08.tex'), 'w', encoding='utf-8') as f:
    f.write(tex_exam_08)

with open(os.path.join(folder_08, 'DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_08.tex'), 'w', encoding='utf-8') as f:
    f.write(tex_sol_08)

with open(os.path.join(folder_08, 'DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_08.md'), 'w', encoding='utf-8') as f:
    f.write(md_sol_08)

print("Generated files for DE_08 successfully!")
