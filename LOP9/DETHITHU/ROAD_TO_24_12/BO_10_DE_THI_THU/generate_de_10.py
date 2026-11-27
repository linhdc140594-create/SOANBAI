import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

folder_10 = os.path.join(BASE_DIR, 'DE_10')
os.makedirs(folder_10, exist_ok=True)

tex_exam_10 = r'''\documentclass[11pt,a4paper]{article}
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
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ 10)}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ 10} & \textbf{MÔN: TOÁN -- LỚP 9} \\
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
\textbf{Câu 1.} Giá trị của biểu thức $5\sqrt{8} - \sqrt{50} + 2\sqrt{18}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $11\sqrt{2}$. & \textbf{B.} $9\sqrt{2}$. & \textbf{C.} $13\sqrt{2}$. & \textbf{D.} $7\sqrt{2}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 2.} Cho góc nhọn $\alpha$ bất kỳ. Hệ thức lượng giác nào sau đây luôn đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $\sin^2 \alpha + \cos^2 \alpha = 1$. & \textbf{B.} $\sin^2 \alpha - \cos^2 \alpha = 1$. & \textbf{C.} $\tan \alpha \cdot \cot \alpha = -1$. & \textbf{D.} $\sin \alpha = \cos \alpha$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 3.} Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-3x + 15 < 0$. & \textbf{B.} $0x + 7 \ge 0$. & \textbf{C.} $x^2 - 4 > 0$. & \textbf{D.} $\dfrac{1}{x} + 2 \le 0$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 4.} Cho hai số thực $x$ và $y$ thỏa mãn $x < y$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $2x - 7 < 2y - 7$. & \textbf{B.} $-5x < -5y$. & \textbf{C.} $x + 4 > y + 4$. & \textbf{D.} $-2x + 1 < -2y + 1$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 5.} Căn bậc hai số học của 400 bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $20$. & \textbf{B.} $-20$. & \textbf{C.} $20$ và $-20$. & \textbf{D.} $160\,000$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 6.} Biểu thức $\sqrt{7 - 2x}$ có nghĩa khi và chỉ khi\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x \le \dfrac{7}{2}$. & \textbf{B.} $x \ge \dfrac{7}{2}$. & \textbf{C.} $x < \dfrac{7}{2}$. & \textbf{D.} $x > \dfrac{7}{2}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 7.} Với mọi số thực $x \ge 5$, giá trị của biểu thức $\sqrt{(x - 5)^2}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $x - 5$. & \textbf{B.} $5 - x$. & \textbf{C.} $-(x - 5)$. & \textbf{D.} $(x - 5)^2$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 8.} Giá trị của biểu thức căn bậc ba $\sqrt[3]{-1000}$ bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $-10$. & \textbf{B.} $10$. & \textbf{C.} $-100$. & \textbf{D.} $100$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 9.} Một hình tròn có chu vi là $C$. Bán kính $R$ của hình tròn đó được tính bằng công thức\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $R = \dfrac{C}{2\pi}$. & \textbf{B.} $R = \dfrac{C}{\pi}$. & \textbf{C.} $R = \dfrac{2\pi}{C}$. & \textbf{D.} $R = \sqrt{\dfrac{C}{\pi}}$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 10.} Cho đường tròn $(O; 5\text{ cm})$ và một điểm $M$. Biết khoảng cách $OM = 3\text{ cm}$. Khẳng định nào sau đây là đúng?\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Điểm $M$ nằm bên trong $(O)$. & \textbf{B.} Điểm $M$ nằm trên $(O)$. & \textbf{C.} Điểm $M$ nằm bên ngoài $(O)$. & \textbf{D.} Điểm $M$ trùng tâm $O$.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 11.} Cho hai đường tròn $(O; 9\text{ cm})$ và $(O'; 4\text{ cm})$ có đoạn nối tâm $OO' = 15\text{ cm}$. Vị trí tương đối của hai đường tròn là\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} Ở ngoài nhau. & \textbf{B.} Tiếp xúc ngoài. & \textbf{C.} Cắt nhau. & \textbf{D.} Tiếp xúc trong.
\end{tabularx}

\vspace{1.5mm}
\textbf{Câu 12.} Cho đường tròn $(O)$, góc nội tiếp $\widehat{AMB} = 40^\circ$ chắn cung nhỏ $AB$. Số đo của góc ở tâm $\widehat{AOB}$ tương ứng bằng\\
\begin{tabularx}{\linewidth}{XXXX}
\textbf{A.} $80^\circ$. & \textbf{B.} $40^\circ$. & \textbf{C.} $20^\circ$. & \textbf{D.} $160^\circ$.
\end{tabularx}

\vspace{3mm}
\noindent
\textbf{Phần 2. Trắc nghiệm Đúng -- Sai (2,0 điểm).} \textit{Trong mỗi ý a), b), c), d) ở câu 13 và câu 14, thí sinh chọn đúng hoặc sai và ghi chữ ``Đ'' hoặc ``S'' vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 13.} Hai tổ sản xuất cùng may đồng phục học sinh để quyên góp ủng hộ học sinh vùng cao. Nếu hai tổ cùng làm chung thì sau $12\text{ ngày}$ sẽ hoàn thành xong kế hoạch. Nếu tổ 1 làm riêng trong $4\text{ ngày}$ rồi nghỉ, tổ 2 tiếp tục làm riêng trong $14\text{ ngày}$ nữa thì cả hai tổ hoàn thành được $50\%$ khối lượng công việc ($= \dfrac{1}{2}$ kế hoạch). Gọi thời gian tổ 1 và tổ 2 làm một mình hoàn thành toàn bộ công việc lần lượt là $x$ và $y$ (ngày, $x, y > 12$).\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Trong 1 ngày, cả hai tổ cùng làm được $\dfrac{1}{12}$ khối lượng công việc. & & \\
\hline
b) Phương trình biểu thị lượng công việc hai tổ làm nối tiếp theo đề bài là: $\dfrac{4}{x} + \dfrac{14}{y} = \dfrac{1}{2}$. & & \\
\hline
c) Thời gian tổ 1 làm một mình hoàn thành kế hoạch nhanh hơn tổ 2 làm một mình là 30 ngày. & & \\
\hline
d) Nếu tổ 1 làm một mình thì sau 20 ngày sẽ hoàn thành xong toàn bộ công việc. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{2mm}
\textbf{Câu 14.} Cho tam giác $ABC$ vuông tại $A$ có $AB = 9\text{ cm}$ và $AC = 12\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$). Vẽ đường tròn tâm $A$ bán kính $AH$, ký hiệu $(A; AH)$.\\
Xét tính đúng sai của các khẳng định sau:
\begin{center}
\begin{tabularx}{\linewidth}{|X|c|c|}
\hline
\textbf{Khẳng định} & \textbf{Đúng} & \textbf{Sai} \\
\hline
a) Độ dài cạnh huyền $BC = 15\text{ cm}$ và đường cao $AH = 7{,}2\text{ cm}$. & & \\
\hline
b) Đường thẳng $BC$ là tiếp tuyến của đường tròn $(A; AH)$ tại tiếp điểm $H$. & & \\
\hline
c) Điểm $C$ nằm ở bên trong đường tròn $(A; AH)$. & & \\
\hline
d) Từ điểm $B$ kẻ tiếp tuyến thứ hai $BD$ với đường tròn $(A; AH)$ ($D$ là tiếp điểm). Độ dài tiếp tuyến $BD = 5{,}4\text{ cm}$. & & \\
\hline
\end{tabularx}
\end{center}

\vspace{3mm}
\noindent
\textbf{Phần 3. Trắc nghiệm trả lời ngắn (2,0 điểm).} \textit{Từ câu 15 đến câu 18, thí sinh chỉ ghi kết quả cuối cùng vào bài làm.}

\vspace{1.5mm}
\textbf{Câu 15.} Nghiệm của bất phương trình $4(x - 2) - 3 \le 2(3x + 1) - 5$ là $\dots\dots\dots$

\vspace{1.5mm}
\textbf{Câu 16.} Giá trị của biểu thức $T = \sqrt{(\sqrt{13} - 4)^2} + \sqrt{13}$ bằng $\dots\dots\dots$

\vspace{1.5mm}
\noindent
\begin{minipage}[c]{0.65\linewidth}
\textbf{Câu 17.} Một con diều đang bay lượn trên bầu trời được giữ bởi một sợi dây kéo căng thẳng dài $80\text{ m}$. Sợi dây diều tạo với mặt đất một góc nghiêng $48^\circ$ (xem hình vẽ bên). Biết tay bạn học sinh cầm cuộn dây diều cách mặt đất $1{,}2\text{ m}$. Hỏi con diều đang ở độ cao bao nhiêu mét so với mặt đất? (Làm tròn kết quả đến hàng phần mười của mét, biết $\sin 48^\circ \approx 0{,}7431$).
\end{minipage}\hfill
\begin{minipage}[c]{0.32\linewidth}
\centering
\begin{tikzpicture}[scale=0.7]
  % Mặt đất
  \draw[thick] (-0.5,0) -- (3.8,0);
  % Người thả diều
  \draw[thick] (0.3,0) -- (0.3,0.9);
  \node[left] at (0.3,0.45) {\footnotesize $1{,}2\text{ m}$};
  % Dây diều
  \draw[line width=1.1pt, orange!90!black] (0.3,0.9) -- (3.2,3.8);
  \node[above left] at (1.7,2.4) {\footnotesize $80\text{ m}$};
  % Con diều
  \draw[thick, fill=red!70!blue] (3.2,3.8) -- (3.0,4.2) -- (3.5,4.3) -- (3.7,3.9) -- cycle;
  \draw[thick, red] (3.2,3.8) -- (3.1,3.4); % Đuôi diều
  % Đường nằm ngang
  \draw[dashed] (0.3,0.9) -- (3.2,0.9);
  % Góc nghiêng 48 độ
  \draw (0.3,0.9) ++(0:0.7) arc (0:48:0.7);
  \node at (1.2,1.25) {\footnotesize $48^\circ$};
  % Đường gióng độ cao
  \draw[dashed] (3.2,3.8) -- (3.2,0);
\end{tikzpicture}
\end{minipage}

\vspace{1.5mm}
\textbf{Câu 18.} Một bồn hoa hình quạt tròn có bán kính $R = 12\text{ m}$ và góc ở tâm tương ứng là $45^\circ$. Tính diện tích của bồn hoa đó theo $\pi$ và làm tròn đến hàng phần mười (lấy $\pi \approx 3{,}14$, đơn vị: $\text{m}^2$).

\vspace{4mm}
\noindent
\textbf{\large II. TỰ LUẬN (3,0 điểm).} \textit{Thí sinh trình bày lời giải chi tiết vào tờ giấy thi.}

\vspace{2mm}
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Giải hệ phương trình: $\begin{cases} 5x - 2y = 8 \\ 3x + 4y = 10 \end{cases}$.
  \item[b)] \textit{(0,5 điểm)} Cho biểu thức $M = \left( \dfrac{\sqrt{a}+1}{\sqrt{a}-1} - \dfrac{\sqrt{a}-1}{\sqrt{a}+1} \right) : \dfrac{4\sqrt{a}}{a-1}$ với $a > 0, a \ne 1$. Rút gọn biểu thức $M$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 20 (1,5 điểm).} Cho tam giác nhọn $ABC$ nội tiếp đường tròn $(O; R)$ có các đường cao $BD, CE$ cắt nhau tại trực tâm $H$. Kẻ đường kính $AK$ của đường tròn $(O)$.
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)} Chứng minh rằng bốn điểm $B, E, D, C$ cùng thuộc một đường tròn và tứ giác $BHCK$ là hình bình hành.
  \item[b)] \textit{(0,75 điểm)} Gọi $M$ là trung điểm của đoạn thẳng $BC$. Chứng minh rằng ba điểm $H, M, K$ thẳng hàng và $AH = 2 OM$.
\end{itemize}

\vspace{2mm}
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)} Một công ty sản xuất lon nước ngọt hình trụ bằng nhôm có nắp đậy với thể tích $V = 54\pi\text{ cm}^3$. Gọi bán kính đáy lon là $r$ và chiều cao lon là $h$ (cm). Hãy tìm bán kính $r$ và chiều cao $h$ để diện tích toàn phần của lon nước ngọt là nhỏ nhất (nhằm tiết kiệm chi phí vỏ lon nhôm nhất)?
  \item[b)] \textit{(0,25 điểm)} Cho ba số thực dương $x, y, z$ thỏa mãn điều kiện $x + y + z = 3$. Tìm giá trị nhỏ nhất của biểu thức:
  \[
  S = \dfrac{x}{y^2 + 1} + \dfrac{y}{z^2 + 1} + \dfrac{z}{x^2 + 1}.
  \]
\end{itemize}

\vspace{4mm}
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{(Cán bộ coi thi không giải thích gì thêm)}
\end{center}

\end{document}
'''

tex_sol_10 = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[top=1.5cm, bottom=1.5cm, left=1.6cm, right=1.6cm]{geometry}

\setlength{\parskip}{1.5pt}
\setlength{\parindent}{0pt}
\setlength{\abovedisplayskip}{3pt}
\setlength{\belowdisplayskip}{3pt}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\lhead{\footnotesize \textbf{CHÙA HƯƠNG SƠN -- ÔN THI VÀO 10}}
\rhead{\footnotesize \textbf{ĐÁP ÁN \& LỜI GIẢI CHI TIẾT (ĐỀ SỐ 10)}}
\cfoot{\thepage}

\begin{document}

\begin{center}
\textbf{\large HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN ĐỀ THI THỬ SỐ 10}\\
\textbf{MÔN: TOÁN 9 -- HỌC KỲ I -- NĂM HỌC 2026 -- 2027}\\
\textit{(Hướng dẫn chấm gồm 02 trang)}
\end{center}

\vspace{1mm}
\noindent
\rule{\linewidth}{0.8pt}

\vspace{1.5mm}
\noindent
\textbf{\large A. ĐÁP ÁN TRẮC NGHIỆM (7,0 ĐIỂM)}

\vspace{1.5mm}
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

\vspace{1.5mm}
\noindent
\textbf{2. Phần 2: Trắc nghiệm Đúng -- Sai (2,0 điểm)}
\begin{itemize}
  \item \textbf{Câu 13 (1,0 điểm):} a) Đúng \quad b) Đúng \quad c) Sai \quad d) Đúng.
  \item \textbf{Câu 14 (1,0 điểm):} a) Đúng \quad b) Đúng \quad c) Sai \quad d) Đúng.
\end{itemize}
\textit{Quy tắc chấm: Đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng 4 ý được 1,0đ.}

\vspace{1.5mm}
\noindent
\textbf{3. Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm -- Mỗi câu đúng 0,5 điểm)}
\begin{itemize}
  \item \textbf{Câu 15:} $x \ge -4$.
  \item \textbf{Câu 16:} $4$.
  \item \textbf{Câu 17:} $60{,}6\text{ m}$ (hoặc $60{,}6$).
  \item \textbf{Câu 18:} $56{,}5\text{ m}^2$ (hoặc $56{,}52$).
\end{itemize}

\vspace{2mm}
\noindent
\textbf{\large B. LỜI GIẢI CHI TIẾT VÀ BAREM ĐIỂM TỰ LUẬN (3,0 ĐIỂM)}

\vspace{1.5mm}
\noindent
\textbf{Câu 19 (1,0 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,5 điểm)} Hệ phương trình: $\begin{cases} 5x - 2y = 8 \quad (1) \\ 3x + 4y = 10 \quad (2) \end{cases}$.\\
  Nhân (1) với 2: $\begin{cases} 10x - 4y = 16 \\ 3x + 4y = 10 \end{cases}$ \dotfill \textbf{(0,25đ)}\\
  Cộng hai phương trình vế theo vế: $13x = 26 \iff x = 2$.\\
  Thay $x = 2$ vào (1): $5(2) - 2y = 8 \iff 2y = 2 \iff y = 1$.\\
  Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (2; 1)$. \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,5 điểm)} Với $a > 0, a \ne 1$, ta có:
  \[
  \dfrac{\sqrt{a}+1}{\sqrt{a}-1} - \dfrac{\sqrt{a}-1}{\sqrt{a}+1} = \dfrac{(\sqrt{a}+1)^2 - (\sqrt{a}-1)^2}{a - 1} = \dfrac{(a + 2\sqrt{a} + 1) - (a - 2\sqrt{a} + 1)}{a - 1} = \dfrac{4\sqrt{a}}{a - 1} \quad \text{\textbf{(0,25đ)}}
  \]
  Do đó:
  \[
  M = \dfrac{4\sqrt{a}}{a - 1} : \dfrac{4\sqrt{a}}{a - 1} = \dfrac{4\sqrt{a}}{a - 1} \cdot \dfrac{a - 1}{4\sqrt{a}} = 1 \quad \text{\textbf{(0,25đ)}}
  \]
\end{itemize}

\vspace{1.5mm}
\noindent
\textbf{Câu 20 (1,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,75 điểm)}
  Xét tam giác $BEC$ vuông tại $E$ và tam giác $BDC$ vuông tại $D$.\\
  Hai điểm $E, D$ cùng nhìn đoạn $BC$ dưới góc vuông nên $B, E, D, C$ cùng thuộc đường tròn đường kính $BC$ (đpcm). \dotfill \textbf{(0,25đ)}\\
  Vì $AK$ là đường kính của $(O)$ nên $\widehat{ACK} = 90^\circ \implies CK \perp AC$.\\
  Lại có $BH \perp AC$ (đường cao $BD$), suy ra $BH \parallel CK$. \dotfill \textbf{(0,25đ)}\\
  Tương tự, $\widehat{ABK} = 90^\circ \implies BK \perp AB$. Lại có $CH \perp AB$ (đường cao $CE$), suy ra $CH \parallel BK$.\\
  Tứ giác $BHCK$ có các cặp cạnh đối song song nên là hình bình hành (đpcm). \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,75 điểm)}
  Vì $BHCK$ là hình bình hành nên hai đường chéo $HK$ và $BC$ cắt nhau tại trung điểm của mỗi đường.\\
  Mà $M$ là trung điểm của $BC$, suy ra $M$ cũng là trung điểm của $HK$. Do đó ba điểm $H, M, K$ thẳng hàng (đpcm). \dotfill \textbf{(0,25đ)}\\
  Xét tam giác $AHK$: có $O$ là trung điểm của $AK$, $M$ là trung điểm của $HK$.\\
  Suy ra $OM$ là đường trung bình của tam giác $AHK$. \dotfill \textbf{(0,25đ)}\\
  Do đó $OM = \dfrac{1}{2} AH$, hay $AH = 2 OM$ (đpcm). \dotfill \textbf{(0,25đ)}
\end{itemize}

\vspace{1.5mm}
\noindent
\textbf{Câu 21 (0,5 điểm).}
\begin{itemize}
  \item[a)] \textit{(0,25 điểm)}
  Thể tích hình trụ là $V = \pi r^2 h = 54\pi \implies h = \dfrac{54}{r^2}$.\\
  Diện tích toàn phần lon nước ngọt:
  $S_{tp} = 2\pi r^2 + 2\pi r h = 2\pi \left( r^2 + \dfrac{54}{r} \right) = 2\pi \left( r^2 + \dfrac{27}{r} + \dfrac{27}{r} \right)$.\\
  Áp dụng BĐT Cô-si cho ba số dương:
  $r^2 + \dfrac{27}{r} + \dfrac{27}{r} \ge 3\sqrt[3]{r^2 \cdot \dfrac{27}{r} \cdot \dfrac{27}{r}} = 3 \cdot 9 = 27$.\\
  Suy ra $S_{tp} \ge 54\pi\text{ (cm}^2)$. Dấu đẳng thức xảy ra khi $r^2 = \dfrac{27}{r} \iff r^3 = 27 \iff r = 3\text{ cm}$.\\
  Khi đó $h = \dfrac{54}{3^2} = 6\text{ cm}$. Vậy diện tích nhỏ nhất khi $r = 3\text{ cm}$ và $h = 6\text{ cm}$. \dotfill \textbf{(0,25đ)}

  \item[b)] \textit{(0,25 điểm)}
  Áp dụng kỹ thuật Cauchy ngược dấu với $y > 0$: $\dfrac{x}{y^2 + 1} = x - \dfrac{xy^2}{y^2 + 1} \ge x - \dfrac{xy^2}{2y} = x - \dfrac{xy}{2}$.\\
  Tương tự: $\dfrac{y}{z^2 + 1} \ge y - \dfrac{yz}{2}$ và $\dfrac{z}{x^2 + 1} \ge z - \dfrac{zx}{2}$.\\
  Cộng vế theo vế: $S \ge (x + y + z) - \dfrac{xy + yz + zx}{2}$.\\
  Mà $xy + yz + zx \le \dfrac{(x+y+z)^2}{3} = \dfrac{3^2}{3} = 3 \implies S \ge 3 - \dfrac{3}{2} = \dfrac{3}{2}$.\\
  Dấu đẳng thức xảy ra khi $x = y = z = 1$. Giá trị nhỏ nhất của $S$ bằng $\dfrac{3}{2}$. \dotfill \textbf{(0,25đ)}
\end{itemize}

\end{document}
'''

md_sol_10 = '''# ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT - ĐỀ THI THỬ SỐ 10
**MÔN: TOÁN 9 - HỌC KỲ I - NĂM HỌC 2026 - 2027**
**ĐƠN VỊ: CHÙA HƯƠNG SƠN**

---

## A. ĐÁP ÁN TRẮC NGHIỆM (7,0 ĐIỂM)

### 1. Phần 1: Trắc nghiệm nhiều lựa chọn (3,0 điểm - 0,25đ/câu)
* Câu 1: **A** ($11\sqrt{2}$)
* Câu 2: **A** ($\sin^2 \alpha + \cos^2 \alpha = 1$)
* Câu 3: **A** ($-3x + 15 < 0$)
* Câu 4: **A** ($2x - 7 < 2y - 7$)
* Câu 5: **A** ($20$)
* Câu 6: **A** ($x \le \dfrac{7}{2}$)
* Câu 7: **A** ($x - 5$)
* Câu 8: **A** ($-10$)
* Câu 9: **A** ($R = \dfrac{C}{2\pi}$)
* Câu 10: **A** (Điểm $M$ nằm bên trong $(O)$)
* Câu 11: **A** (Ở ngoài nhau)
* Câu 12: **A** ($80^\circ$)

### 2. Phần 2: Trắc nghiệm Đúng - Sai (2,0 điểm)
* **Câu 13:** a) Đúng | b) Đúng | c) Sai | d) Đúng
* **Câu 14:** a) Đúng | b) Đúng | c) Sai | d) Đúng

### 3. Phần 3: Trắc nghiệm trả lời ngắn (2,0 điểm - 0,5đ/câu)
* **Câu 15:** $x \ge -4$
* **Câu 16:** $4$
* **Câu 17:** $60{,}6\text{ m}$
* **Câu 18:** $56{,}5\text{ m}^2$ (hoặc $56{,}52$)

---

## B. LỜI GIẢI CHI TIẾT TỰ LUẬN (3,0 ĐIỂM)

### Câu 19 (1,0 điểm)
* **a) (0,5 điểm)** Giải hệ:
  $$\\begin{cases} 5x - 2y = 8 \\\\ 3x + 4y = 10 \\end{cases} \\iff \\begin{cases} 10x - 4y = 16 \\\\ 3x + 4y = 10 \\end{cases} \\iff \\begin{cases} 13x = 26 \\\\ 5x - 2y = 8 \\end{cases} \\iff \\begin{cases} x = 2 \\\\ y = 1 \\end{cases}$$
  Nghiệm duy nhất: $(x; y) = (2; 1)$.
* **b) (0,5 điểm)** Với $a > 0, a \\ne 1$:
  $$M = \\left(\\dfrac{(a+2\\sqrt{a}+1) - (a-2\\sqrt{a}+1)}{a-1}\\right) : \\dfrac{4\\sqrt{a}}{a-1} = \\dfrac{4\\sqrt{a}}{a-1} \\cdot \\dfrac{a-1}{4\\sqrt{a}} = 1.$$

### Câu 20 (1,5 điểm)
* **a) (0,75 điểm)**
  - $\\widehat{BEC} = \\widehat{BDC} = 90^\\circ \\implies B, E, D, C$ cùng thuộc đường tròn đường kính $BC$ (0,25đ).
  - $CK \\perp AC$ (góc nội tiếp chắn nửa đường tròn), $BH \\perp AC \\implies BH \\parallel CK$ (0,25đ).
  - $BK \\perp AB, CH \\perp AB \\implies CH \\parallel BK$. Suy ra $BHCK$ là hình bình hành (0,25đ).
* **b) (0,75 điểm)**
  - $BHCK$ là hình bình hành $\\implies M$ là trung điểm $HK \\implies H, M, K$ thẳng hàng (0,25đ).
  - Tam giác $AHK$ có $O$ là trung điểm $AK$, $M$ là trung điểm $HK \\implies OM$ là đường trung bình (0,25đ).
  - Do đó $AH = 2 OM$ (0,25đ).

### Câu 21 (0,5 điểm)
* **a) (0,25 điểm)**
  - $h = \\dfrac{54}{r^2}$. $S_{tp} = 2\\pi \\left(r^2 + \\dfrac{27}{r} + \\dfrac{27}{r}\\right) \\ge 2\\pi \\cdot 3\\sqrt[3]{r^2 \\cdot \\dfrac{27}{r} \\cdot \\dfrac{27}{r}} = 54\\pi$.
  - Dấu bằng khi $r^3 = 27 \\iff r = 3\\text{ cm}, h = 6\\text{ cm}$.
* **b) (0,25 điểm)**
  - Cauchy ngược dấu: $\\dfrac{x}{y^2+1} = x - \\dfrac{xy^2}{y^2+1} \\ge x - \\dfrac{xy}{2}$.
  - Tương tự với hai số hạng còn lại, ta được $S \\ge (x+y+z) - \\dfrac{xy+yz+zx}{2}$.
  - Vì $xy+yz+zx \\le \\dfrac{(x+y+z)^2}{3} = 3 \\implies S \\ge 3 - \\dfrac{3}{2} = \\dfrac{3}{2}$.
  - Đẳng thức xảy ra khi $x = y = z = 1$. Giá trị nhỏ nhất là $\\dfrac{3}{2}$.
'''

# Write files
with open(os.path.join(folder_10, 'De_Thi_Thu_Toan_9_De_10.tex'), 'w', encoding='utf-8') as f:
    f.write(tex_exam_10)

with open(os.path.join(folder_10, 'DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_10.tex'), 'w', encoding='utf-8') as f:
    f.write(tex_sol_10)

with open(os.path.join(folder_10, 'DAP_AN_VA_LOI_GIAI_CHI_TIET_DE_10.md'), 'w', encoding='utf-8') as f:
    f.write(md_sol_10)

print("Generated files for DE_10 successfully!")
