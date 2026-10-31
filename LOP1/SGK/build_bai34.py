# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 34: XEM GIỜ ĐÚNG TRÊN ĐỒNG HỒ
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D
% =========================================================================

% --- ĐỊNH NGHĨA MÀU SẮC AN TOÀN ---
\colorlet{myteal}{cyan!70!blue}
\colorlet{myorange}{orange}
\colorlet{mypurple}{purple}
\colorlet{myblue}{blue}
\colorlet{myred}{red}

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 34 ---

% 1. Vẽ đồng hồ kim (mặt tròn có chân đế xinh xắn)
\providecommand{\VeDongHoKim}[4]{% #1=scale, #2=(x,y), #3=gio, #4=mau
  \begin{scope}[shift={(#2)}, scale=#1]
    % Chân đế đồng hồ
    \draw[line width=1.4pt, #4!80] (-0.45,-0.92) -- (-0.72,-1.18);
    \draw[line width=1.4pt, #4!80] (0.45,-0.92) -- (0.72,-1.18);
    % Vỏ và mặt đồng hồ
    \draw[fill=#4!12, draw=#4!85, line width=1.1pt] (0,0) circle (1.14cm);
    \draw[fill=white, draw=black!60, line width=0.6pt] (0,0) circle (0.98cm);
    % 12 vạch và các số từ 1 đến 12
    \foreach \n in {1,...,12} {
      \pgfmathsetmacro{\goc}{90 - \n * 30}
      \draw[line width=0.5pt, black!50] (\goc:0.88cm) -- (\goc:0.96cm);
      \node[font=\bfseries\scriptsize, color=black!90] at (\goc:0.75cm) {\n};
    }
    % Kim phút (chỉ số 12)
    \draw[line width=1.4pt, -{Latex[length=2.0mm, width=1.3mm]}, blue!85!black] (0,-0.06) -- (0,0.64);
    % Kim giờ (chỉ số #3)
    \pgfmathsetmacro{\gocht}{90 - #3 * 30}
    \draw[line width=2.0pt, -{Latex[length=2.2mm, width=1.8mm]}, red!85!black] (0,-0.04) -- (\gocht:0.45cm);
    % Chốt tâm đồng hồ
    \fill[orange!90!black, draw=black!80, line width=0.4pt] (0,0) circle (0.09cm);
  \end{scope}
}

% 2. Đồng hồ điện tử để bàn
\providecommand{\VeDongHoDienTu}[3]{% #1=(x,y), #2=thời gian, #3=màu
  \begin{scope}[shift={(#1)}, scale=0.62]
    \draw[fill=#3!15, draw=#3!85, line width=0.9pt, rounded corners=3pt] (-1.3,-0.48) rectangle (1.3,0.48);
    \draw[fill=black!92, draw=black, rounded corners=2pt] (-1.12,-0.34) rectangle (1.12,0.34);
    \node[font=\bfseries\small, color=green!85!white] at (0,0) {#2};
  \end{scope}
}

% 3. Mũi tên chuyển tiếp thời gian
\providecommand{\VeMuiTenThoiGian}[3]{% #1=(x,y), #2=độ dài, #3=nhãn
  \begin{scope}[shift={(#1)}]
    \draw[->, >=stealth, line width=1.2pt, orange!90!black] (0,0) -- (#2,0);
    \node[above, font=\bfseries\tiny, color=blue!90!black] at (#2*0.5, 0.06) {#3};
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Nhận biết kim dài chỉ số 12
\begin{ex} %[1H9N34]
Quan sát chiếc đồng hồ treo tường bên dưới:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeDongHoKim{0.88}{0,0}{8}{blue}
  \draw[<-, >=stealth, line width=0.8pt, blue!85!black] (0.05,0.48) -- (1.5,0.58) node[right, font=\bfseries\tiny, color=blue!85!black] {Kim dài};
  \draw[<-, >=stealth, line width=0.8pt, red!85!black] (-0.28,-0.16) -- (-1.5,-0.35) node[left, font=\bfseries\tiny, color=red!85!black] {Kim ngắn};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Khi đồng hồ chỉ giờ đúng, kim dài luôn chỉ vào số nào?
\begin{multicols}{4}
\choice
{Số $8$}
{\True Số $12$}
{Số $6$}
{Số $10$}
\end{multicols}
\loigiai{
Khi đồng hồ chỉ giờ đúng, kim dài luôn luôn chỉ thẳng vào số 12.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Đọc giờ trên đồng hồ kim (7 giờ)
\begin{ex} %[1H9N34]
Chiếc đồng hồ để bàn tai chuông màu cam đang chạy:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeDongHoKim{0.88}{0,0}{7}{orange}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Đồng hồ đang chỉ mấy giờ?
\begin{multicols}{4}
\choice
{$6$ giờ}
{\True $7$ giờ}
{$8$ giờ}
{$12$ giờ}
\end{multicols}
\loigiai{
Kim ngắn chỉ số 7, kim dài chỉ số 12. Vậy đồng hồ đang chỉ $7$ giờ đúng.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Vị trí kim ngắn khi chỉ 4 giờ
\begin{ex} %[1H9H34]
Chiếc đồng hồ treo tường màu xanh ngọc chỉ $4$ giờ đúng:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeDongHoKim{0.88}{0,0}{4}{myteal}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Khi đồng hồ chỉ $4$ giờ đúng thì kim ngắn chỉ vào số mấy?
\begin{multicols}{4}
\choice
{Số $12$}
{\True Số $4$}
{Số $3$}
{Số $5$}
\end{multicols}
\loigiai{
Kim ngắn là kim chỉ giờ. Khi đồng hồ chỉ 4 giờ thì kim ngắn chỉ vào số 4.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Hai kim cùng chỉ số 12
\begin{ex} %[1H9H34]
Quan sát chiếc đồng hồ lúc giữa trưa:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeDongHoKim{0.88}{0,0}{12}{purple}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Khi cả kim ngắn và kim dài cùng chỉ vào số 12 thì đồng hồ chỉ mấy giờ?
\begin{multicols}{4}
\choice
{$1$ giờ}
{\True $12$ giờ}
{$6$ giờ}
{$11$ giờ}
\end{multicols}
\loigiai{
Cả kim ngắn và kim dài cùng chỉ thẳng vào số 12 thì đồng hồ chỉ $12$ giờ đúng.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Nối đồng hồ kim với đồng hồ điện tử (9 giờ)
\begin{ex} %[1H9H34]
Chiếc đồng hồ kim và các đồng hồ điện tử:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.78}{-3.2,0}{9}{blue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-3.2,-1.2) {Đồng hồ kim};
  
  \VeDongHoDienTu{-0.8,0.55}{08:00}{orange}
  \node[font=\bfseries\tiny, color=black] at (-0.8,0.05) {Đồng hồ A};
  
  \VeDongHoDienTu{1.8,0.55}{09:00}{myteal}
  \node[font=\bfseries\tiny, color=black] at (1.8,0.05) {Đồng hồ B};
  
  \VeDongHoDienTu{-0.8,-0.75}{10:00}{purple}
  \node[font=\bfseries\tiny, color=black] at (-0.8,-1.25) {Đồng hồ C};
  
  \VeDongHoDienTu{1.8,-0.75}{12:00}{red}
  \node[font=\bfseries\tiny, color=black] at (1.8,-1.25) {Đồng hồ D};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đồng hồ điện tử nào chỉ cùng giờ với đồng hồ kim?
\begin{multicols}{4}
\choice
{Đồng hồ A}
{\True Đồng hồ B}
{Đồng hồ C}
{Đồng hồ D}
\end{multicols}
\loigiai{
Đồng hồ kim chỉ 9 giờ, khớp với đồng hồ điện tử B hiển thị 09:00.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Hoạt động buổi sáng của Mai
\begin{ex} %[1H9H34]
Buổi sáng, bạn Mai nhìn đồng hồ trước khi bước vào cổng trường:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.82}{0,0}{7}{myteal}
  \node[font=\bfseries\tiny, color=blue!90!black] at (0,-1.15) {Trường Tiểu học};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Bạn Mai đến trường lúc mấy giờ sáng?
\begin{multicols}{4}
\choice
{$6$ giờ sáng}
{\True $7$ giờ sáng}
{$8$ giờ sáng}
{$9$ giờ sáng}
\end{multicols}
\loigiai{
Đồng hồ có kim ngắn chỉ số 7 và kim dài chỉ số 12, tức là $7$ giờ sáng.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Thời gian đọc sách của Nam (8 giờ -> 10 giờ)
\begin{ex} %[1H9V34]
Nam bắt đầu đọc sách và đọc xong sách theo hai mốc thời gian:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.72}{-2.4,0}{8}{blue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-2.4,-1.1) {Bắt đầu: $8$ giờ};
  
  \VeMuiTenThoiGian{-1.0,0}{2.0}{Đọc sách}
  
  \VeDongHoKim{0.72}{2.4,0}{10}{blue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (2.4,-1.1) {Xong: $10$ giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Nam đã đọc sách trong khoảng thời gian là bao nhiêu giờ?
\begin{multicols}{4}
\choice
{$1$ giờ}
{\True $2$ giờ}
{$3$ giờ}
{$4$ giờ}
\end{multicols}
\loigiai{
Thời gian Nam đọc sách là: $10 - 8 = 2$ giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Bữa trưa gia đình (11 giờ + 1 giờ)
\begin{ex} %[1H9V34]
Gia đình bạn An bắt đầu ăn cơm trưa lúc $11$ giờ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.72}{-2.2,0}{11}{orange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (-2.2,-1.1) {Bắt đầu: $11$ giờ};
  
  \VeMuiTenThoiGian{-0.8,0}{1.6}{Sau $1$ giờ}
  
  \draw[fill=yellow!25, draw=orange!80, line width=0.8pt, rounded corners=3pt] (1.3,-0.65) rectangle (3.1,0.65);
  \node[font=\bfseries\small, color=red!85] at (2.2,0.1) {$? \text{ giờ}$};
  \node[font=\bfseries\tiny, color=black!70] at (2.2,-0.35) {Ăn xong};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Sau $1$ giờ ăn cơm và nghỉ ngơi, đồng hồ sẽ chỉ mấy giờ?
\begin{multicols}{4}
\choice
{$11$ giờ}
{\True $12$ giờ}
{$1$ giờ}
{$10$ giờ}
\end{multicols}
\loigiai{
Đồng hồ sẽ chỉ: $11 + 1 = 12$ giờ trưa.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Lớp học bóng rổ (3 giờ -> 5 giờ chiều)
\begin{ex} %[1H9V34]
Buổi chiều, Huy tham gia lớp học bóng rổ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.72}{-2.4,0}{3}{myteal}
  \node[font=\bfseries\tiny, color=cyan!85!black] at (-2.4,-1.1) {Bắt đầu: $3$ giờ};
  
  \VeMuiTenThoiGian{-1.0,0}{2.0}{Tập luyện}
  
  \VeDongHoKim{0.72}{2.4,0}{5}{myteal}
  \node[font=\bfseries\tiny, color=cyan!85!black] at (2.4,-1.1) {Kết thúc: $5$ giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Buổi tập bóng rổ diễn ra trong mấy giờ?
\begin{multicols}{4}
\choice
{$1$ giờ}
{\True $2$ giờ}
{$3$ giờ}
{$4$ giờ}
\end{multicols}
\loigiai{
Thời gian buổi tập bóng rổ là: $5 - 3 = 2$ giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Đồng hồ chỉ giờ muộn nhất buổi chiều
\begin{ex} %[1H9V34]
Bốn chiếc đồng hồ chỉ thời gian các hoạt động buổi chiều:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.58}{-3.6,0}{2}{blue}
  \node[font=\bfseries\tiny, color=black] at (-3.6,-0.9) {A ($2$ giờ)};
  
  \VeDongHoKim{0.58}{-1.2,0}{4}{orange}
  \node[font=\bfseries\tiny, color=black] at (-1.2,-0.9) {B ($4$ giờ)};
  
  \VeDongHoKim{0.58}{1.2,0}{6}{red}
  \node[font=\bfseries\tiny, color=black] at (1.2,-0.9) {C ($6$ giờ)};
  
  \VeDongHoKim{0.58}{3.6,0}{3}{myteal}
  \node[font=\bfseries\tiny, color=black] at (3.6,-0.9) {D ($3$ giờ)};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Chiếc đồng hồ nào chỉ thời gian muộn nhất trong buổi chiều?
\begin{multicols}{4}
\choice
{Đồng hồ B}
{\True Đồng hồ C}
{Đồng hồ D}
{Đồng hồ A}
\end{multicols}
\loigiai{
So sánh các số giờ buổi chiều: $2 < 3 < 4 < 6$. Chiếc đồng hồ C ($6$ giờ chiều) chỉ giờ muộn nhất.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Dự đoán giờ đi ngủ của Hoa (6 giờ + 3 giờ)
\begin{ex} %[1H9V34]
Buổi tối, đồng hồ phòng khách chỉ $6$ giờ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.78}{-1.8,0}{6}{purple}
  \node[font=\bfseries\tiny, color=purple!90!black] at (-1.8,-1.15) {Hiện tại: $6$ giờ tối};
  
  \draw[fill=blue!5, draw=blue!75, line width=0.8pt, rounded corners=3pt] (0.2,-0.65) rectangle (3.4,0.65);
  \node[align=center, font=\bfseries\tiny, color=blue!90!black] at (1.8,0.05) {Bạn Hoa nói:\\``Còn $3$ giờ nữa là\\đến giờ đi ngủ!''};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Bạn Hoa đi ngủ lúc mấy giờ tối?
\begin{multicols}{4}
\choice
{$8$ giờ tối}
{\True $9$ giờ tối}
{$10$ giờ tối}
{$7$ giờ tối}
\end{multicols}
\loigiai{
Thời điểm Hoa đi ngủ là: $6 + 3 = 9$ giờ tối.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Đồng hồ chạy nhanh 1 giờ (10 - 1 = 9 giờ)
\begin{ex} %[1H9C34]
Một chiếc đồng hồ treo tường bị chạy nhanh hơn giờ thực tế đúng $1$ giờ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.78}{-1.5,0}{10}{red}
  \node[font=\bfseries\tiny, color=red!85!black] at (-1.5,-1.15) {Đồng hồ chỉ: $10$ giờ};
  
  \draw[fill=orange!10, draw=orange!85, line width=0.8pt, rounded corners=3pt] (0.4,-0.65) rectangle (3.5,0.65);
  \node[align=center, font=\bfseries\tiny, color=orange!90!black] at (1.95,0.05) {CẢNH BÁO:\\Đồng hồ bị chạy\\nhanh hơn $1$ giờ!};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giờ đúng thực tế lúc này là mấy giờ?
\begin{multicols}{4}
\choice
{$11$ giờ}
{\True $9$ giờ}
{$8$ giờ}
{$10$ giờ}
\end{multicols}
\loigiai{
Vì đồng hồ chạy nhanh hơn 1 giờ nên giờ thực tế đúng là: $10 - 1 = 9$ giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: PHẦN 2 - CÂU HỎI ĐÚNG / SAI (4 CÂU) ---

\textbf{Phần 2. Câu trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Cấu tạo mặt đồng hồ
\begin{ex} %[1H9N34]
Quan sát chiếc đồng hồ mẫu chỉ $3$ giờ đúng:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.85}{0,0}{3}{blue}
  \draw[<-, >=stealth, line width=0.7pt, blue!85!black] (0.05,0.45) -- (1.5,0.58) node[right, font=\bfseries\tiny, color=blue!85!black] {Kim dài (chỉ phút)};
  \draw[<-, >=stealth, line width=0.7pt, red!85!black] (0.38,0.02) -- (1.5,-0.25) node[right, font=\bfseries\tiny, color=red!85!black] {Kim ngắn (chỉ giờ)};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Kim ngắn của đồng hồ dùng để chỉ giờ, kim dài dùng để chỉ phút.}
{\True Khi đồng hồ chỉ giờ đúng, kim dài luôn luôn chỉ vào số $12$.}
{Chiếc đồng hồ ở hình trên đang chỉ $12$ giờ $3$ phút.}
{\True Khi đồng hồ chỉ $5$ giờ đúng, kim ngắn chỉ số $5$ và kim dài chỉ số $12$.}
\loigiai{
\begin{itemize}
    \item a) Đúng: Kim ngắn chỉ giờ, kim dài chỉ phút.
    \item b) Đúng: Giờ đúng thì kim dài luôn chỉ số 12.
    \item c) Sai: Đồng hồ ở hình trên đang chỉ 3 giờ đúng.
    \item d) Đúng: Khi 5 giờ đúng, kim ngắn chỉ số 5, kim dài chỉ số 12.
\end{itemize}
}
\end{ex}

% CÂU 14: Đối chiếu đồng hồ kim và điện tử
\begin{ex} %[1H9H34]
Quan sát ba cặp đồng hồ đối chiếu bên dưới:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  % Cặp 1
  \begin{scope}[shift={(-3.2,0)}]
    \VeDongHoKim{0.58}{0,0.58}{7}{blue}
    \VeDongHoDienTu{0,-0.68}{07:00}{blue}
    \node[font=\bfseries\tiny, color=blue!90!black] at (0,-1.2) {Cặp 1};
  \end{scope}
  % Cặp 2
  \begin{scope}[shift={(0,0)}]
    \VeDongHoKim{0.58}{0,0.58}{11}{myteal}
    \VeDongHoDienTu{0,-0.68}{11:00}{myteal}
    \node[font=\bfseries\tiny, color=cyan!85!black] at (0,-1.2) {Cặp 2};
  \end{scope}
  % Cặp 3
  \begin{scope}[shift={(3.2,0)}]
    \VeDongHoKim{0.58}{0,0.58}{4}{red}
    \VeDongHoDienTu{0,-0.68}{05:00}{red}
    \node[font=\bfseries\tiny, color=red!85!black] at (0,-1.2) {Cặp 3};
  \end{scope}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Ở Cặp 1, cả hai đồng hồ đều cùng chỉ $7$ giờ đúng.}
{Ở Cặp 3, hai chiếc đồng hồ chỉ cùng một giờ với nhau.}
{\True Đồng hồ ở Cặp 2 chỉ giờ muộn hơn đồng hồ ở Cặp 1 là $4$ giờ.}
{\True Để Cặp 3 chỉ cùng một giờ, ta cần chỉnh đồng hồ điện tử thành 04:00.}
\loigiai{
\begin{itemize}
    \item a) Đúng: Cặp 1 đều chỉ 7 giờ.
    \item b) Sai: Cặp 3 đồng hồ kim chỉ 4 giờ, đồng hồ điện tử chỉ 5 giờ (khác nhau).
    \item c) Đúng: $11 - 7 = 4$ giờ.
    \item d) Đúng: Đồng hồ kim chỉ 4 giờ nên cần chỉnh điện tử về 04:00.
\end{itemize}
}
\end{ex}

% CÂU 15: Hoạt động chủ nhật của Rô-bốt
\begin{ex} %[1H9V34]
Lịch trình hoạt động ngày Chủ nhật của bạn Rô-bốt:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \begin{scope}[shift={(-3.0,0)}]
    \VeDongHoKim{0.58}{0,0}{8}{myteal}
    \node[align=center, font=\bfseries\tiny, color=black] at (0,-0.95) {Tưới cây\\($8$ giờ sáng)};
  \end{scope}
  \draw[->, >=stealth, line width=0.8pt, gray] (-1.9,0) -- (-1.1,0);
  
  \begin{scope}[shift={(0,0)}]
    \VeDongHoKim{0.58}{0,0}{10}{blue}
    \node[align=center, font=\bfseries\tiny, color=black] at (0,-0.95) {Đọc sách\\($10$ giờ sáng)};
  \end{scope}
  \draw[->, >=stealth, line width=0.8pt, gray] (1.1,0) -- (1.9,0);
  
  \begin{scope}[shift={(3.0,0)}]
    \VeDongHoKim{0.58}{0,0}{4}{orange}
    \node[align=center, font=\bfseries\tiny, color=black] at (0,-0.95) {Thả diều\\($4$ giờ chiều)};
  \end{scope}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Rô-bốt bắt đầu tưới cây lúc $8$ giờ sáng.}
{\True Khoảng thời gian từ lúc tưới cây đến lúc đọc sách là $2$ giờ.}
{Rô-bốt đi thả diều vào buổi trưa.}
{\True Trong ba hoạt động trên, hoạt động diễn ra muộn nhất là thả diều.}
\loigiai{
\begin{itemize}
    \item a) Đúng: Đồng hồ tưới cây chỉ 8 giờ sáng.
    \item b) Đúng: $10 - 8 = 2$ giờ.
    \item c) Sai: Thả diều lúc 4 giờ chiều (không phải buổi trưa).
    \item d) Đúng: Thả diều lúc 4 giờ chiều là hoạt động muộn nhất trong ngày.
\end{itemize}
}
\end{ex}

% CÂU 16: So sánh giờ học và ngủ của Nam và Bình
\begin{ex} %[1H9V34]
Thời gian biểu buổi tối của hai bạn Nam và Bình:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \begin{scope}[shift={(-2.8,0)}]
    \draw[fill=blue!8, draw=blue!75, line width=0.7pt, rounded corners=3pt] (-1.8,-1.18) rectangle (1.8,1.18);
    \node[font=\bfseries\footnotesize, color=blue!90!black] at (0,0.85) {Bạn Nam};
    \VeDongHoKim{0.48}{-0.8,0}{7}{blue}
    \node[font=\bfseries\tiny, color=black] at (-0.8,-0.78) {Học: $7$h};
    \VeDongHoKim{0.48}{0.8,0}{9}{blue}
    \node[font=\bfseries\tiny, color=black] at (0.8,-0.78) {Ngủ: $9$h};
  \end{scope}
  
  \begin{scope}[shift={(2.8,0)}]
    \draw[fill=orange!8, draw=orange!75, line width=0.7pt, rounded corners=3pt] (-1.8,-1.18) rectangle (1.8,1.18);
    \node[font=\bfseries\footnotesize, color=orange!90!black] at (0,0.85) {Bạn Bình};
    \VeDongHoKim{0.48}{-0.8,0}{8}{orange}
    \node[font=\bfseries\tiny, color=black] at (-0.8,-0.78) {Học: $8$h};
    \VeDongHoKim{0.48}{0.8,0}{10}{orange}
    \node[font=\bfseries\tiny, color=black] at (0.8,-0.78) {Ngủ: $10$h};
  \end{scope}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Bạn Nam bắt đầu học bài sớm hơn bạn Bình $1$ giờ.}
{\True Bạn Nam đi ngủ lúc $9$ giờ tối.}
{Bạn Bình đi ngủ sớm hơn bạn Nam $1$ giờ.}
{\True Cả hai bạn đều học bài trong khoảng thời gian là $2$ giờ trước khi ngủ.}
\loigiai{
\begin{itemize}
    \item a) Đúng: Nam học lúc 7h, Bình lúc 8h $\Rightarrow$ Nam sớm hơn: $8 - 7 = 1$ giờ.
    \item b) Đúng: Nam đi ngủ lúc 9 giờ tối.
    \item c) Sai: Bình ngủ lúc 10h, muộn hơn Nam 1 giờ.
    \item d) Đúng: Nam: $9 - 7 = 2$ giờ; Bình: $10 - 8 = 2$ giờ.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: PHẦN 3 - CÂU HỎI TRẢ LỜI NGẮN (4 CÂU) ---

\textbf{Phần 3. Câu hỏi trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Đọc giờ trên đồng hồ để bàn (5 giờ)
\begin{ex} %[1H9N34]
Quan sát chiếc đồng hồ để bàn hình ngôi sao màu tím:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.85}{0,0}{5}{purple}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Chiếc đồng hồ trên đang chỉ mấy giờ?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$5$}}
\loigiai{
Kim ngắn chỉ số 5, kim dài chỉ số 12 nên đồng hồ chỉ $5$ giờ.\\
\textbf{Đáp số: $5$.}
}
\end{ex}

% CÂU 18: Tính khoảng cách thời gian buổi sáng (8h đến 11h)
\begin{ex} %[1H9H34]
Buổi sáng, Lan vào lớp học lúc $8$ giờ và tan học buổi sáng lúc $11$ giờ trưa:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.75}{-2.4,0}{8}{myteal}
  \node[font=\bfseries\tiny, color=cyan!85!black] at (-2.4,-1.15) {Vào học: $8$ giờ};
  
  \VeMuiTenThoiGian{-1.0,0}{2.0}{Thời gian ở trường}
  
  \VeDongHoKim{0.75}{2.4,0}{11}{myteal}
  \node[font=\bfseries\tiny, color=cyan!85!black] at (2.4,-1.15) {Tan học: $11$ giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi buổi học sáng của Lan kéo dài trong mấy giờ?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$3$}}
\loigiai{
Thời gian buổi học sáng của Lan là: $11 - 8 = 3$ giờ.\\
\textbf{Đáp số: $3$.}
}
\end{ex}

% CÂU 19: Dự đoán giờ ăn cơm chiều (2h + 4h = 6h)
\begin{ex} %[1H9V34]
Bây giờ đồng hồ chỉ $2$ giờ chiều:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.75}{-2.0,0}{2}{orange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (-2.0,-1.15) {Hiện tại: $2$ giờ};
  
  \VeMuiTenThoiGian{-0.6,0}{1.6}{Sau $4$ giờ}
  
  \draw[fill=yellow!25, draw=orange!80, line width=0.8pt, rounded corners=3pt] (1.5,-0.65) rectangle (3.3,0.65);
  \node[font=\bfseries\small, color=red!85] at (2.4,0.1) {$? \text{ giờ}$};
  \node[font=\bfseries\tiny, color=black!70] at (2.4,-0.35) {Ăn cơm chiều};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Sau $4$ giờ nữa gia đình sẽ ăn cơm chiều. Lúc đó đồng hồ chỉ mấy giờ?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$6$}}
\loigiai{
Đồng hồ sẽ chỉ: $2 + 4 = 6$ giờ chiều.\\
\textbf{Đáp số: $6$.}
}
\end{ex}

% CÂU 20: Bé My ngủ qua đêm (9 giờ tối đến 6 giờ sáng = 9 giờ)
\begin{ex} %[1H9C34]
Buổi tối, bé My lên giường đi ngủ lúc $9$ giờ tối và thức dậy lúc $6$ giờ sáng hôm sau:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.65}{-2.8,0}{9}{blue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-2.8,-0.95) {Đi ngủ: $9$ giờ tối};
  
  \draw[->, >=stealth, line width=1.1pt, purple!85] (-1.4,0.3) -- (1.4,0.3);
  \node[above, font=\bfseries\tiny, color=purple!85!black] at (0,0.35) {Qua đêm ($12$ giờ)};
  \node[below, font=\bfseries\tiny, color=red!85] at (0,-0.1) {$3\text{h} + 6\text{h} = ?\text{ giờ}$};
  
  \VeDongHoKim{0.65}{2.8,0}{6}{orange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (2.8,-0.95) {Thức dậy: $6$ giờ sáng};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi bé My đã ngủ được tất cả bao nhiêu giờ?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$9$}}
\loigiai{
Từ $9$ giờ tối đến $12$ giờ đêm là: $12 - 9 = 3$ giờ.\\
Từ $12$ giờ đêm đến $6$ giờ sáng là: $6$ giờ.\\
Tổng số giờ bé My đã ngủ là: $3 + 6 = 9$ giờ.\\
\textbf{Đáp số: $9$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 9 Bai 34
tex_path = os.path.abspath('CHỦ ĐỀ 9 - THỜI GIAN. GIỜ VÀ LỊCH/Chuong9_Bai34_XemGioDungTrenDongHo.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_34_preview.tex độc lập 5 trang
preview_content = r'''\documentclass[14pt,a4paper]{extbook}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,calc,positioning,backgrounds,patterns,decorations.pathreplacing,arrows.meta}
\usepackage{tcolorbox}
\tcbuselibrary{skins,theorems}
\usepackage{geometry}
\geometry{a4paper,left=15mm,right=15mm,top=11mm,bottom=12mm}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{qrcode}
\usepackage{fontawesome5}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}

\newcounter{ex}
\newcommand{\setcounterpageref}[2]{}

\newenvironment{ex}[1][]{%
  \refstepcounter{ex}%
  \par\noindent\textbf{Câu \theex.}%
  \hspace{0.5em}%
}{%
  \par\vspace{0.2ex}%
}

\newcommand{\choice}[4]{%
  \begin{enumerate}[label=\Alph*.,leftmargin=2.2em,itemsep=0.1ex,parsep=0pt,topsep=0.2ex]
    \item #1
    \item #2
    \item #3
    \item #4
  \end{enumerate}
}

\newcommand{\choiceTF}[4]{%
  \begin{enumerate}[label=\alph*),leftmargin=2.2em,itemsep=0.15ex,parsep=0pt,topsep=0.25ex]
    \item #1
    \item #2
    \item #3
    \item #4
  \end{enumerate}
}

\newcommand{\True}{}
\newcommand{\loigiai}[1]{}

\begin{document}

% --- KHUNG TIÊU ĐỀ TRANG 1 KÈM QR CODE ---
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 34: XEM GIỜ ĐÚNG TRÊN ĐỒNG HỒ},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.80\textwidth}
  \textbf{Học kì 2 -- Chủ đề 9: Thời gian. Giờ và lịch}\\
  \textbf{Thời gian:} 40 phút \quad | \quad \textbf{Đề thi 100\% hình vẽ trực quan}\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.18\textwidth}
  \centering
  \qrcode[height=1.45cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-34}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_34_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_34_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_34_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_34_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_34_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    if num_pages == 5:
        # Sao chép vào PDF_DeThi_TungBai
        out_dir = os.path.abspath('PDF_DeThi_TungBai')
        os.makedirs(out_dir, exist_ok=True)
        out_pdf = os.path.join(out_dir, 'Bai_34_Xem_gio_dung_tren_dong_ho.pdf')
        import shutil
        shutil.copy2('Bai_34_preview.pdf', out_pdf)
        print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
    else:
        print(f"CẢNH BÁO: Số trang hiện tại là {num_pages}, chưa khớp chuẩn 5 trang!")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
