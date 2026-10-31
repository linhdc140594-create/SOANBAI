# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 38: ÔN TẬP CÁC SỐ VÀ PHÉP TÍNH TRONG PHẠM VI 10
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D
% =========================================================================

% --- ĐỊNH NGHĨA MÀU SẮC AN TOÀN ---
\colorlet{myteal}{cyan!70!blue}
\colorlet{myorange}{orange}
\colorlet{mypurple}{purple}
\colorlet{myblue}{blue}
\colorlet{myred}{red}

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 38 ---

% 1. Vẽ quả táo đỏ xinh xắn
\providecommand{\VeBamiTamQuaTao}[2]{% #1=(x,y), #2=scale
  \begin{scope}[shift={(#1)}, scale=#2]
    \draw[fill=red!85!black, draw=red!90!black, line width=0.5pt] 
      (-0.25,0) .. controls (-0.35,0.35) and (-0.1,0.5) .. (0,0.3) 
      .. controls (0.1,0.5) and (0.35,0.35) .. (0.25,0) 
      .. controls (0.35,-0.4) and (-0.35,-0.4) .. (-0.25,0);
    \draw[line width=1.1pt, brown!80!black] (0,0.3) .. controls (0.05,0.5) .. (0.1,0.6);
    \draw[fill=green!70!black, draw=green!60!black] (0.05,0.45) .. controls (0.2,0.55) and (0.25,0.45) .. (0.05,0.45);
  \end{scope}
}

% 2. Vẽ tia số từ 0 đến 10
\providecommand{\VeBamiTamTiaSoPVMuoi}[3]{% #1=(x,y), #2=vị trí ẩn/đặc biệt (-1 nếu không), #3=ký tự ẩn
  \begin{scope}[shift={(#1)}, scale=0.7]
    \draw[->, >=stealth, line width=1.2pt, blue!85!black] (-0.3,0) -- (10.7,0);
    \foreach \n in {0,...,10} {
      \draw[line width=1.0pt, blue!85!black] (\n, 0.15) -- (\n, -0.15);
      \ifnum\n=#2
        \draw[fill=yellow!30, draw=red!85, line width=1.1pt, rounded corners=2pt] (\n-0.35,-0.75) rectangle (\n+0.35,-0.25);
        \node[font=\bfseries\small, color=red!90!black] at (\n,-0.5) {#3};
      \else
        \node[below, font=\bfseries\small, color=black!85] at (\n,-0.18) {\n};
      \fi
    }
  \end{scope}
}

% 3. Vẽ khung 10 ô (Ten-frame)
\providecommand{\VeBamiTamKhungMuoiO}[3]{% #1=(x,y), #2=số chấm màu 1, #3=số chấm màu 2
  \begin{scope}[shift={(#1)}, scale=0.55]
    \draw[fill=white, draw=blue!85, line width=1.2pt, rounded corners=3pt] (-2.6,-1.1) rectangle (2.6,1.1);
    \draw[line width=1.0pt, blue!75] (-2.6,0) -- (2.6,0);
    \foreach \x in {-1.56, -0.52, 0.52, 1.56} {
      \draw[line width=0.8pt, blue!75] (\x,-1.1) -- (\x,1.1);
    }
    % Vẽ chấm màu 1 (xanh)
    \foreach \i in {1,...,#2} {
      \pgfmathsetmacro{\col}{mod(\i-1, 5)}
      \pgfmathsetmacro{\row}{(\i-1 < 5) ? 0.55 : -0.55}
      \pgfmathsetmacro{\cx}{-2.08 + \col * 1.04}
      \fill[blue!80!black, draw=blue!95, line width=0.5pt] (\cx, \row) circle (0.33cm);
    }
    % Vẽ chấm màu 2 (đỏ)
    \foreach \j in {1,...,#3} {
      \pgfmathtruncatemacro{\idx}{#2 + \j}
      \pgfmathsetmacro{\col}{mod(\idx-1, 5)}
      \pgfmathsetmacro{\row}{(\idx-1 < 5) ? 0.55 : -0.55}
      \pgfmathsetmacro{\cx}{-2.08 + \col * 1.04}
      \fill[red!85!black, draw=red!95, line width=0.5pt] (\cx, \row) circle (0.33cm);
    }
  \end{scope}
}

% 4. Sơ đồ tách gộp số (Part-Part-Whole)
\providecommand{\VeBamiTamSoDoTachGop}[4]{% #1=(x,y), #2=tổng, #3=phần 1, #4=phần 2
  \begin{scope}[shift={(#1)}, scale=0.65]
    \draw[fill=orange!15, draw=orange!90!black, line width=1.2pt] (0,1.2) circle (0.55cm) node[font=\bfseries\large, color=orange!95!black] {#2};
    \draw[line width=1.1pt, gray!80] (-0.2,0.7) -- (-1.1,-0.1);
    \draw[line width=1.1pt, gray!80] (0.2,0.7) -- (1.1,-0.1);
    \draw[fill=blue!15, draw=blue!85, line width=1.1pt] (-1.3,-0.5) circle (0.52cm) node[font=\bfseries\large, color=blue!90!black] {#3};
    \draw[fill=teal!15, draw=teal!85, line width=1.1pt] (1.3,-0.5) circle (0.52cm) node[font=\bfseries\large, color=teal!90!black] {#4};
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Đếm số lượng quả táo
\begin{ex} %[1D10N38]
Quan sát rổ táo ngon lành vừa thu hoạch trong vườn:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=yellow!15, draw=orange!80, line width=1.1pt, rounded corners=6pt] (-3.8,-0.65) rectangle (3.8,0.75);
  \foreach \i in {1,...,9} {
    \pgfmathsetmacro{\x}{(\i-5)*0.78}
    \VeBamiTamQuaTao{\x,0}{0.8}
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Trong rổ có tất cả bao nhiêu quả táo?
\begin{multicols}{4}
\choice
{$8$ quả}
{\True $9$ quả}
{$10$ quả}
{$7$ quả}
\end{multicols}
\loigiai{
Đếm lần lượt từng quả táo từ trái sang phải: $1, 2, 3, 4, 5, 6, 7, 8, 9$. Có tất cả $9$ quả táo.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Tia số tìm số ở giữa
\begin{ex} %[1D10N38]
Quan sát dãy số trên tia số dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeBamiTamTiaSoPVMuoi{0,0}{8}{?}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số thích hợp điền vào ô có dấu hỏi chấm $[?]$ là
\begin{multicols}{4}
\choice
{$7$}
{\True $8$}
{$9$}
{$10$}
\end{multicols}
\loigiai{
Trên tia số theo thứ tự từ bé đến lớn: $0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$. Số đứng liền sau $7$ và liền trước $9$ là số $8$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Số liền sau trên tia số
\begin{ex} %[1D10H38]
Chú thỏ nhảy thêm một bước sang số liền sau của số 8:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[->, >=stealth, line width=1.1pt, blue!80] (5.5,0) -- (10.5,0);
  \foreach \n in {6,7,8,9,10} {
    \draw[line width=1pt, blue!80] (\n, 0.12) -- (\n, -0.12);
    \node[below, font=\bfseries\small] at (\n,-0.15) {\n};
  }
  \draw[->, >=stealth, line width=1.3pt, red!85!black] (8,0.2) .. controls (8.5,0.7) .. (9,0.2);
  \node[above=2pt, font=\bfseries\tiny, color=red!90!black] at (8.5,0.6) {+1 bước};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số liền sau của số $8$ là số nào?
\begin{multicols}{4}
\choice
{$7$}
{\True $9$}
{$10$}
{$6$}
\end{multicols}
\loigiai{
Muốn tìm số liền sau của một số, ta lấy số đó cộng thêm $1$: $8 + 1 = 9$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: So sánh hai nhóm đồ vật
\begin{ex} %[1D10H38]
Quan sát hai hàng chấm tròn màu sắc:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.65]
  \node[font=\bfseries\footnotesize, color=blue!90!black] at (-3.5,0.4) {Hàng A:};
  \foreach \i in {1,...,7} {
    \fill[blue!75!black] (-2.2 + \i*0.65, 0.4) circle (0.24cm);
  }
  \node[font=\bfseries\footnotesize, color=orange!90!black] at (-3.5,-0.4) {Hàng B:};
  \foreach \i in {1,...,5} {
    \fill[orange!85!black] (-2.2 + \i*0.65, -0.4) circle (0.24cm);
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
So sánh số chấm tròn ở hàng A và hàng B:
\begin{multicols}{2}
\choice
{Hàng A ít hơn hàng B}
{\True Hàng A nhiều hơn hàng B ($7 > 5$)}
{Hai hàng có số chấm bằng nhau}
{Hàng B nhiều hơn hàng A}
\end{multicols}
\loigiai{
Hàng A có $7$ chấm tròn, hàng B có $5$ chấm tròn. Vì $7 > 5$ nên hàng A nhiều hơn hàng B.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Phép cộng trên khung 10 ô
\begin{ex} %[1D10H38]
Quan sát khung mười ô gồm $4$ chấm xanh và $5$ chấm đỏ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeBamiTamKhungMuoiO{0,0}{4}{5}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Phép tính thích hợp biểu thị tổng số chấm tròn là
\begin{multicols}{2}
\choice
{$4 + 4 = 8$}
{\True $4 + 5 = 9$}
{$5 + 5 = 10$}
{$4 + 3 = 7$}
\end{multicols}
\loigiai{
Có $4$ chấm xanh và thêm $5$ chấm đỏ, tổng số chấm tròn là: $4 + 5 = 9$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Phép trừ trực quan quả cam gạch chéo
\begin{ex} %[1D10H38]
Trên bàn có $10$ quả cam, đã ăn hết $4$ quả (bị gạch chéo):
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.62]
  \foreach \i in {1,...,10} {
    \pgfmathsetmacro{\x}{(\i-5.5)*1.1}
    \draw[fill=orange!80, draw=orange!95!black, line width=0.6pt] (\x,0) circle (0.38cm);
    \fill[green!70!black] (\x+0.05,0.42) circle (0.06cm);
    \ifnum\i>6
      \draw[line width=1.5pt, red!85!black] (\x-0.3,-0.3) -- (\x+0.3,0.3);
      \draw[line width=1.5pt, red!85!black] (\x-0.3,0.3) -- (\x+0.3,-0.3);
    \fi
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi trên bàn còn lại bao nhiêu quả cam?
\begin{multicols}{4}
\choice
{$5$ quả}
{\True $6$ quả}
{$7$ quả}
{$8$ quả}
\end{multicols}
\loigiai{
Phép tính trừ: $10 - 4 = 6$ quả cam còn lại.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Sơ đồ tách gộp số 10
\begin{ex} %[1D10V38]
Quan sát sơ đồ tách gộp số $10$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeBamiTamSoDoTachGop{0,0}{10}{3}{?}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số thích hợp điền vào dấu hỏi chấm $[?]$ là
\begin{multicols}{4}
\choice
{$6$}
{\True $7$}
{$8$}
{$5$}
\end{multicols}
\loigiai{
Số $10$ gồm $3$ và $7$ (vì $3 + 7 = 10$). Vậy số cần điền là $7$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Biểu thức 3 số đón khách
\begin{ex} %[1D10H38]
Chiếc xe buýt chở học sinh: ban đầu có $3$ bạn, trạm 1 đón $4$ bạn, trạm 2 đón thêm $3$ bạn:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[fill=blue!12, draw=blue!80, line width=1pt, rounded corners=3pt] (-4.0,-0.4) rectangle (-2.0,0.4);
  \node[font=\bfseries\small] at (-3.0,0) {3 bạn};
  \draw[->, >=stealth, line width=1.2pt, orange!85] (-1.9,0) -- (-1.1,0) node[midway, above=1pt, font=\bfseries\tiny] {+4};
  \draw[fill=orange!15, draw=orange!80, line width=1pt, rounded corners=3pt] (-1.0,-0.4) rectangle (1.0,0.4);
  \node[font=\bfseries\small] at (0,0) {7 bạn};
  \draw[->, >=stealth, line width=1.2pt, teal!85] (1.1,0) -- (1.9,0) node[midway, above=1pt, font=\bfseries\tiny] {+3};
  \draw[fill=green!15, draw=green!80!black, line width=1pt, rounded corners=3pt] (2.0,-0.4) rectangle (4.0,0.4);
  \node[font=\bfseries\small, color=red!85!black] at (3.0,0) {?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị của biểu thức $3 + 4 + 3$ là bao nhiêu?
\begin{multicols}{4}
\choice
{$9$}
{\True $10$}
{$8$}
{$7$}
\end{multicols}
\loigiai{
Thực hiện tính từ trái sang phải: $3 + 4 = 7$, sau đó $7 + 3 = 10$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Cân thăng bằng so sánh phép tính
\begin{ex} %[1D10V38]
Chiếc cân thăng bằng có hai đĩa cân đặt hai phép tính:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[line width=1.5pt, black!75] (0,0) -- (0,1.4);
  \draw[line width=1.3pt, black!75] (-0.8,0) -- (0.8,0);
  \draw[line width=1.4pt, orange!90!black] (-2.2,1.4) -- (2.2,1.4);
  \fill[red!85!black] (0,1.4) circle (0.1cm);
  % Đĩa trái
  \draw[line width=0.8pt, gray!80] (-2.2,1.4) -- (-2.7,0.7);
  \draw[line width=0.8pt, gray!80] (-2.2,1.4) -- (-1.7,0.7);
  \draw[fill=blue!15, draw=blue!80, line width=1.1pt, rounded corners=2pt] (-3.1,0.2) rectangle (-1.3,0.7) node[midway, font=\bfseries\small, color=blue!90!black] {$6 + 3$};
  % Đĩa phải
  \draw[line width=0.8pt, gray!80] (2.2,1.4) -- (1.7,0.7);
  \draw[line width=0.8pt, gray!80] (2.2,1.4) -- (2.7,0.7);
  \draw[fill=teal!15, draw=teal!80, line width=1.1pt, rounded corners=2pt] (1.3,0.2) rectangle (3.1,0.7) node[midway, font=\bfseries\small, color=teal!90!black] {$10 - 1$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Dấu thích hợp để điền vào chỗ chấm $6 + 3 \dots 10 - 1$ là
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{$+$}
\end{multicols}
\loigiai{
Ta có $6 + 3 = 9$ và $10 - 1 = 9$. Vì $9 = 9$ nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Toa tàu sắp xếp số
\begin{ex} %[1D10V38]
Các toa tàu hỏa mang các số: $5, 0, 9, 2, 7$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.62]
  \foreach \i/\num in {1/5, 2/0, 3/9, 4/2, 5/7} {
    \pgfmathsetmacro{\x}{(\i-3)*1.9}
    \draw[fill=blue!15, draw=blue!85, line width=1pt, rounded corners=3pt] (\x-0.75,-0.45) rectangle (\x+0.75,0.45);
    \node[font=\bfseries\large, color=blue!90!black] at (\x,0) {\num};
    \fill[black!80] (\x-0.45,-0.55) circle (0.12cm);
    \fill[black!80] (\x+0.45,-0.55) circle (0.12cm);
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Sắp xếp các số trên các toa tàu theo thứ tự từ bé đến lớn:
\begin{multicols}{2}
\choice
{$9, 7, 5, 2, 0$}
{\True $0, 2, 5, 7, 9$}
{$0, 5, 2, 7, 9$}
{$2, 0, 5, 7, 9$}
\end{multicols}
\loigiai{
So sánh các số: $0 < 2 < 5 < 7 < 9$. Thứ tự từ bé đến lớn là $0, 2, 5, 7, 9$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Tìm số chưa biết x + 4 = 10
\begin{ex} %[1D10V38]
Lọ hoa có tất cả $10$ bông hoa, gồm một số bông hoa vàng và $4$ bông hoa đỏ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=orange!80, fill=yellow!15, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (V) at (-2.0,0) {\bfseries\small\color{orange!90!black} ? hoa vàng};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=red!80, fill=red!15, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (D) at (2.0,0) {\bfseries\small\color{red!85!black} 4 hoa đỏ};
  \node[above=3pt, font=\bfseries\footnotesize, color=blue!90!black] at (0,0.45) {Tất cả: 10 bông hoa};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tìm số bông hoa vàng thích hợp:
\begin{multicols}{4}
\choice
{$5$}
{\True $6$}
{$7$}
{$8$}
\end{multicols}
\loigiai{
Muốn tìm số bông hoa vàng, ta lấy tổng trừ đi số hoa đỏ: $10 - 4 = 6$ bông hoa.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Bóng bay bị nổ
\begin{ex} %[1D10V38]
Bé cầm chùm $9$ quả bóng bay, không may bị nổ $3$ quả:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.55]
  \foreach \i in {1,...,9} {
    \pgfmathsetmacro{\x}{(\i-5)*1.25}
    \ifnum\i>6
      \draw[fill=gray!25, draw=gray!70, line width=0.8pt, dashed] (\x,0) circle (0.42cm);
      \draw[line width=1.4pt, red!85!black] (\x-0.3,-0.3) -- (\x+0.3,0.3);
      \draw[line width=1.4pt, red!85!black] (\x-0.3,0.3) -- (\x+0.3,-0.3);
    \else
      \draw[fill=red!75, draw=red!90!black, line width=0.8pt] (\x,0) circle (0.42cm);
      \draw[line width=0.6pt, gray!70] (\x,-0.42) -- (\x-0.1,-0.9);
    \fi
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi bé còn lại bao nhiêu quả bóng bay nguyên vẹn?
\begin{multicols}{4}
\choice
{$5$ quả}
{\True $6$ quả}
{$7$ quả}
{$8$ quả}
\end{multicols}
\loigiai{
Số quả bóng bay còn lại là: $9 - 3 = 6$ quả.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Các phép tính phạm vi 10
\begin{ex} %[1D10H38]
Quan sát bảng các phép tính trong phạm vi 10:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=blue!8, draw=blue!75, line width=1pt, rounded corners=3pt] (-4.5,-0.45) rectangle (-1.0,0.45) node[midway, font=\bfseries\small] {$7 + 3 = 10$};
  \draw[fill=orange!8, draw=orange!75, line width=1pt, rounded corners=3pt] (-0.5,-0.45) rectangle (3.0,0.45) node[midway, font=\bfseries\small] {$10 - 5 = 5$};
  \draw[fill=teal!8, draw=teal!75, line width=1pt, rounded corners=3pt] (3.5,-0.45) rectangle (7.0,0.45) node[midway, font=\bfseries\small] {$8 - 2 = 6$};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Phép tính $7 + 3 = 10$ là đúng.}
{\True Phép tính $10 - 5 = 5$ là đúng.}
{Phép tính $8 - 2 = 5$ là đúng.}
{\True Phép tính $4 + 6 = 10$ là đúng.}
\loigiai{\textbf{a)} Đúng ($7 + 3 = 10$). \textbf{b)} Đúng ($10 - 5 = 5$). \textbf{c)} Sai (Vì $8 - 2 = 6 \neq 5$). \textbf{d)} Đúng ($4 + 6 = 10$).}
\end{ex}

% CÂU 14: Hai hộp bi của Bình
\begin{ex} %[1D10V38]
Bình có hai hộp bi gồm $7$ viên bi xanh và $3$ viên bi đỏ:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=blue!12, draw=blue!80, line width=1pt, rounded corners=3pt] (-3.8,-0.5) rectangle (-0.6,0.5);
  \node[font=\bfseries\small, color=blue!90!black] at (-2.2,0) {7 bi xanh};
  \draw[fill=red!12, draw=red!80, line width=1pt, rounded corners=3pt] (0.6,-0.5) rectangle (3.8,0.5);
  \node[font=\bfseries\small, color=red!90!black] at (2.2,0) {3 bi đỏ};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Bình có tất cả 10 viên bi vì $7 + 3 = 10$.}
{\True Số bi xanh nhiều hơn số bi đỏ là 4 viên vì $7 - 3 = 4$.}
{Bình có tất cả 11 viên bi.}
{\True Nếu Bình cho bạn 2 viên bi thì Bình còn lại 8 viên bi.}
\loigiai{\textbf{a)} Đúng ($7 + 3 = 10$). \textbf{b)} Đúng ($7 - 3 = 4$). \textbf{c)} Sai (Bình có 10 viên bi). \textbf{d)} Đúng ($10 - 2 = 8$).}
\end{ex}

% CÂU 15: Dãy số và tia số từ 0 đến 10
\begin{ex} %[1D10H38]
Quan sát tia số hoàn chỉnh từ 0 đến 10:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \VeBamiTamTiaSoPVMuoi{0,0}{-1}{}
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định dưới đây:
\choiceTF
{\True Số bé nhất trong các số từ 0 đến 10 là số 0.}
{Số lớn nhất có một chữ số là số 10.}
{\True Số 8 đứng liền sau số 7 và đứng liền trước số 9.}
{\True Dãy số từ 0 đến 10 có tất cả 11 số.}
\loigiai{\textbf{a)} Đúng. \textbf{b)} Sai (Số 10 là số có hai chữ số; số lớn nhất có 1 chữ số là 9). \textbf{c)} Đúng. \textbf{d)} Đúng (Từ 0 đến 10 có 11 số).}
\end{ex}

% CÂU 16: Phép tính chuỗi ba số và tách gộp
\begin{ex} %[1D10H38]
Sơ đồ tính chuỗi: $10 \xrightarrow{-3} 7 \xrightarrow{-2} 5$:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=blue!15, draw=blue!85, line width=1pt] (0,0) circle (0.45cm) node[font=\bfseries\small] {10};
  \draw[->, >=stealth, line width=1.2pt, orange!85] (0.5,0) -- (1.5,0) node[midway, above=1pt, font=\bfseries\tiny] {-3};
  \draw[fill=orange!15, draw=orange!85, line width=1pt] (2.0,0) circle (0.45cm) node[font=\bfseries\small] {7};
  \draw[->, >=stealth, line width=1.2pt, teal!85] (2.5,0) -- (3.5,0) node[midway, above=1pt, font=\bfseries\tiny] {-2};
  \draw[fill=teal!15, draw=teal!85, line width=1pt] (4.0,0) circle (0.45cm) node[font=\bfseries\small] {5};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True Giá trị của biểu thức $10 - 3 - 2 = 5$.}
{\True Giá trị của biểu thức $2 + 5 + 3 = 10$.}
{Giá trị của biểu thức $9 - 4 + 2 = 6$.}
{\True Số 10 có thể tách thành hai số bằng nhau là 5 và 5.}
\loigiai{\textbf{a)} Đúng ($10 - 3 - 2 = 5$). \textbf{b)} Đúng ($2 + 5 + 3 = 10$). \textbf{c)} Sai (Vì $9 - 4 + 2 = 5 + 2 = 7 \neq 6$). \textbf{d)} Đúng ($5 + 5 = 10$).}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Phép cộng quả cam hai đĩa
\begin{ex} %[1D10N38]
Đĩa bên trái có $3$ quả cam, đĩa bên phải có $7$ quả cam:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-1.8,0) {\bfseries\small\color{orange!90!black} 3 quả cam};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (1.8,0) {\bfseries\small\color{orange!90!black} 7 quả cam};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi cả hai đĩa có tất cả bao nhiêu quả cam?
\shortans{10}
\loigiai{
Cả hai đĩa có số quả cam là: $3 + 7 = 10$ quả.\\
\textbf{Đáp số:} $10$.
}
\end{ex}

% CÂU 18: Phép trừ chim bay đi
\begin{ex} %[1D10H38]
Trên cành cây có $9$ chú chim, sau đó có $4$ chú chim cất cánh bay đi:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.2,0) {\bfseries\small\color{blue!90!black} 9 chú chim};
  \node[draw=red!80, fill=yellow!20, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (2.2,0) {\bfseries\small\color{red!90!black} Còn lại: ?};
  \draw[->, >=stealth, line width=1.3pt, red!85!black] (A) -- (B) node[midway, above=2pt, font=\bfseries\tiny, color=red!90!black] {Bay đi 4 chú};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi trên cành cây còn lại bao nhiêu chú chim?
\shortans{5}
\loigiai{
Số chú chim còn lại trên cành là: $9 - 4 = 5$ chú chim.\\
\textbf{Đáp số:} $5$.
}
\end{ex}

% CÂU 19: Bài toán đàn vịt dưới ao và trên bờ
\begin{ex} %[1D10V38]
Trong nông trại có $4$ con vịt đang bơi dưới ao và $5$ con vịt đang kiếm ăn trên bờ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=blue!80, fill=cyan!15, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-2.2,0) {\bfseries\small\color{blue!90!black} 4 con dưới ao};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=green!70!black, fill=green!15, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (2.2,0) {\bfseries\small\color{green!80!black} 5 con trên bờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi nông trại đó có tất cả bao nhiêu con vịt?
\shortans{9}
\loigiai{
Nông trại có tất cả số con vịt là: $4 + 5 = 9$ con vịt.\\
\textbf{Đáp số:} $9$.
}
\end{ex}

% CÂU 20: Tính nhanh chuỗi 4 số liên tiếp
\begin{ex} %[1D10C38]
Tính giá trị biểu thức gồm chuỗi bốn số liên tiếp:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \foreach \i/\num/\mau in {1/1/myblue, 2/2/myorange, 3/3/myteal, 4/4/mypurple} {
    \pgfmathsetmacro{\x}{(\i-2.5)*1.5}
    \node[draw=\mau!85, fill=\mau!15, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (\x,0) {\bfseries\large\color{\mau!90!black} \num};
    \ifnum\i<4
      \node[font=\bfseries\large, color=black!60] at (\x+0.75,0) {$+$};
    \fi
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị của biểu thức $1 + 2 + 3 + 4$ là bao nhiêu?
\shortans{10}
\loigiai{
Tính nhanh bằng cách nhóm: $(1 + 4) + (2 + 3) = 5 + 5 = 10$.\\
\textbf{Đáp số:} $10$.
}
\end{ex}
'''

# Template wrapper để biên dịch độc lập xem trước
preview_tex = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{geometry}
\geometry{a4paper, top=14mm, bottom=14mm, left=14mm, right=14mm}
\usepackage{tikz}
\usetikzlibrary{arrows.meta, calc, shapes.geometric}
\usepackage{multicol}
\usepackage{tcolorbox}
\usepackage{fontawesome5}
\usepackage{qrcode}
\usepackage{enumitem}

% Setup ex/choice counters & commands
\newcounter{ex}
\newcounter{choice}[ex]
\newenvironment{ex}{\refstepcounter{ex}\noindent\textbf{Câu \theex.} }{\par\vspace{2.5mm}}
\newcommand{\choice}[4]{%
  \begin{enumerate}[label=\textbf{\Alph*.}, leftmargin=1.8em, itemsep=1pt, topsep=1pt]
    \item #1 \item #2 \item #3 \item #4
  \end{enumerate}
}
\newcommand{\True}{}
\newcommand{\choiceTF}[4]{%
  \begin{enumerate}[label=\textbf{\alph*)}, leftmargin=1.6em, itemsep=0.8pt, topsep=0.8pt]
    \item #1 \item #2 \item #3 \item #4
  \end{enumerate}
}
\newcommand{\loigiai}[1]{\par\noindent\textit{\footnotesize Lời giải: #1}}
\newcommand{\shortans}[1]{\hfill\textbf{[Đáp số: #1]}}
\newcommand{\setcounterpageref}[2]{}

\begin{document}
% HEADER BÀI KIỂM TRA
\begin{tcolorbox}[colback=white, colframe=blue!85!black, boxrule=1.0pt, arc=2mm, left=2mm, right=2mm, top=1.5mm, bottom=1.5mm]
  \begin{minipage}[c]{0.26\textwidth}
    \begin{tcolorbox}[colback=blue!8, colframe=blue!80!black, boxrule=0.6pt, arc=1.5mm, halign=center, top=1.2mm, bottom=1.2mm, left=1mm, right=1mm]
      {\bfseries\color{blue!95!black}\small LỚP TOÁN THẦY LĨNH}\\[1.5pt]
      {\scriptsize\color{blue!70!black}\faGlobe~loptoanthaylinh.vn}\\[1.5pt]
      {\scriptsize\bfseries\color{blue!85!black}\faPhone~Hotline: 0866976878}
    \end{tcolorbox}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.56\textwidth}
    \centering
    {\footnotesize\bfseries\color{blue!80!black}CHỦ ĐỀ 10 -- ÔN TẬP CUỐI NĂM}\\[2pt]
    {\large\bfseries\color{red!85!black}BÀI 38: ÔN TẬP CÁC SỐ VÀ PHÉP TÍNH PV 10}\\[2pt]
    {\scriptsize\itshape Thời gian làm bài: 35 phút -- Đề gồm 20 câu chuẩn 5 trang}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.14\textwidth}
    \centering
    \qrcode[height=1.35cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-38}\\[2pt]
    {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
  \end{minipage}
\end{tcolorbox}
\vspace{1mm}

''' + content + r'''
\end{document}
'''

with open("Bai_38_preview.tex", "w", encoding="utf-8") as f:
    f.write(preview_tex)

# Lưu nội dung vào file chương chính
target_chapter = r"CHỦ ĐỀ 10 - ÔN TẬP CUỐI NĂM\Chuong10_Bai38_OnTapCacSoVaPhepTinhPhamVi10.tex"
with open(target_chapter, "w", encoding="utf-8") as f:
    f.write(content)

print("Đã tạo Bai_38_preview.tex và cập nhật " + target_chapter)
