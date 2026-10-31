# -*- coding: utf-8 -*-
import os, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 13: LUYỆN TẬP CHUNG (PHÉP CỘNG, PHÉP TRỪ PV 10 - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ
% =========================================================================

% --- CÁC HÀM VẼ ĐỒ VẬT, CON VẬT TRỰC QUAN CHO BÀI 13 ---
\providecommand{\VeQuaTaoDo}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.6]
    \fill[red!85!black] (-0.11,0.08) circle (0.22cm);
    \fill[red!85!black] (0.11,0.08) circle (0.22cm);
    \fill[red!85!black] (0,-0.05) circle (0.24cm);
    \draw[line width=1pt, brown!80!black] (0,0.24) to[out=70,in=-110] (0.06,0.42);
    \fill[green!70!black] (0.05,0.36) to[out=20,in=160] (0.24,0.42) to[out=-120,in=-20] cycle;
  \end{scope}
}

\providecommand{\VeChuChimDau}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.52]
    \fill[cyan!85!blue] (0,0.1) ellipse (0.26cm and 0.2cm);
    \fill[cyan!95!black] (0.18,0.22) circle (0.15cm);
    \fill[orange!95!black] (0.32,0.22) -- (0.45,0.19) -- (0.32,0.15) -- cycle;
    \fill[white] (0.22,0.25) circle (0.04cm);
    \fill[black] (0.24,0.25) circle (0.02cm);
    \fill[blue!80!black] (-0.22,0.1) -- (-0.45,0.18) -- (-0.38,0.04) -- cycle;
  \end{scope}
}

\providecommand{\VeChuChimBayDi}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.52, opacity=0.7]
    \fill[orange!90!red] (0,0.1) ellipse (0.26cm and 0.18cm);
    \fill[orange!95!black] (0.18,0.22) circle (0.14cm);
    \fill[yellow!90!black] (0.31,0.22) -- (0.43,0.19) -- (0.31,0.15) -- cycle;
    \fill[white] (0.22,0.25) circle (0.04cm);
    \fill[black] (0.24,0.25) circle (0.02cm);
    \fill[red!80!black] (-0.05,0.15) -- (-0.2,0.48) -- (0.08,0.2) -- cycle;
  \end{scope}
}

\providecommand{\VeChuChimBayToi}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.52]
    \fill[orange!90!red] (0,0.1) ellipse (0.26cm and 0.18cm);
    \fill[orange!95!black] (-0.18,0.22) circle (0.14cm);
    \fill[yellow!90!black] (-0.31,0.22) -- (-0.43,0.19) -- (-0.31,0.15) -- cycle;
    \fill[white] (-0.22,0.25) circle (0.04cm);
    \fill[black] (-0.24,0.25) circle (0.02cm);
    \fill[red!80!black] (0.05,0.15) -- (0.2,0.48) -- (-0.08,0.2) -- cycle;
  \end{scope}
}

\providecommand{\VeBanNho}[3][blue!70]{% #1=màu áo, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.55]
    \fill[orange!22] (0, 0.55) circle (0.22cm);
    \fill[brown!80!black] (-0.22,0.6) arc (180:0:0.22cm) -- cycle;
    \fill[black] (-0.08,0.56) circle (0.025cm);
    \fill[black] (0.08,0.56) circle (0.025cm);
    \draw[line width=0.6pt, red!70!black] (-0.06,0.48) arc (-150:-30:0.07cm);
    \fill[#1] (-0.16,0.1) rectangle (0.16,0.38);
    \draw[line width=1.3pt, blue!90!black] (-0.08,0.1) -- (-0.08,-0.12);
    \draw[line width=1.3pt, blue!90!black] (0.08,0.1) -- (0.08,-0.12);
  \end{scope}
}

\providecommand{\VeVienBiVe}[3][blue!80!cyan]{% #1=màu, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.5]
    \shade[ball color=#1] (0,0) circle (0.35cm);
  \end{scope}
}

% =========================================================================
% PHẦN 1: TRẮC NGHIỆM LỰA CHỌN (12 CÂU)
% =========================================================================
\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- CÂU 1 ---
\begin{ex} %[1D3N13]
Quan sát hai đĩa táo dưới đây. Cả hai đĩa có tất cả bao nhiêu quả táo?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Đĩa 1 (6 quả)
  \draw[fill=orange!15, draw=orange!80!black, line width=1.2pt] (-2.5,-0.2) ellipse (1.8cm and 0.5cm);
  \foreach \i in {0,1,2,3,4,5} {
    \VeQuaTaoDo{\i*0.6 - 4.0}{0.05}
  }
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (-2.5,-0.35) {6 quả táo};
  
  \node[font=\LARGE\bfseries\color{blue!90!black}] at (0,0.1) {$+$};
  
  % Đĩa 2 (3 quả)
  \draw[fill=orange!15, draw=orange!80!black, line width=1.2pt] (2.3,-0.2) ellipse (1.3cm and 0.45cm);
  \VeQuaTaoDo{1.7}{0.05}
  \VeQuaTaoDo{2.3}{0.05}
  \VeQuaTaoDo{2.9}{0.05}
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (2.3,-0.35) {3 quả táo};
\end{tikzpicture}
\end{center}
\choice
{$8$ quả}
{\True $9$ quả}
{$10$ quả}
{$7$ quả}
\loigiai{
Có tất cả: $6 + 3 = 9$ quả táo.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 2 ---
\begin{ex} %[1D3N13]
Băng giấy có 9 ô vuông, người ta gạch chéo bỏ đi 6 ô vuông. Hỏi còn lại bao nhiêu ô vuông trắng?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  % 3 ô trắng còn lại
  \foreach \i in {0,1,2} {
    \draw[fill=white, draw=blue!85!black, line width=1.1pt] (\i*0.9 - 4.05, -0.45) rectangle (\i*0.9 - 3.15, 0.45);
    \node[font=\small\bfseries\color{blue!90!black}] at (\i*0.9 - 3.6, 0) {\pgfmathparse{int(\i+1)}\pgfmathresult};
  }
  % 6 ô bị gạch chéo
  \foreach \i in {0,1,2,3,4,5} {
    \draw[fill=gray!18, draw=gray!70!black, line width=1.1pt] (\i*0.9 - 1.35, -0.45) rectangle (\i*0.9 - 0.45, 0.45);
    \draw[line width=1.6pt, red!85!black] (\i*0.9-1.35,-0.45) -- (\i*0.9-0.45,0.45);
    \draw[line width=1.6pt, red!85!black] (\i*0.9-1.35,0.45) -- (\i*0.9-0.45,-0.45);
  }
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (-1.35,-0.55) {9 ô bớt 6 ô ($9 - 6 = ?$)};
\end{tikzpicture}
\end{center}
\choice
{$2$ ô}
{\True $3$ ô}
{$4$ ô}
{$5$ ô}
\loigiai{
Phép tính: $9 - 6 = 3$ ô vuông.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 3 ---
\begin{ex} %[1D3H13]
Khung mười ô (Ten-frame) có 5 chấm đỏ và 5 chấm xanh. Tính kết quả phép cộng $5 + 5$:
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=white, draw=blue!85!black, line width=1.4pt] (-2.75,-1.1) rectangle (2.75,1.1);
  \foreach \x in {-1.65, -0.55, 0.55, 1.65} {
    \draw[line width=1pt, blue!70!black] (\x,-1.1) -- (\x,1.1);
  }
  \draw[line width=1pt, blue!70!black] (-2.75,0) -- (2.75,0);
  
  % Hàng 1: 5 chấm đỏ
  \foreach \x in {-2.2, -1.1, 0, 1.1, 2.2} {
    \fill[red!85!black] (\x,0.55) circle (0.33cm);
  }
  % Hàng 2: 5 chấm xanh
  \foreach \x in {-2.2, -1.1, 0, 1.1, 2.2} {
    \fill[cyan!75!blue] (\x,-0.55) circle (0.33cm);
  }
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (0,-1.2) {5 chấm đỏ $+$ 5 chấm xanh};
\end{tikzpicture}
\end{center}
\choice
{$9$}
{\True $10$}
{$8$}
{$7$}
\loigiai{
Ta có: $5 + 5 = 10$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 4 ---
\begin{ex} %[1D3H13]
Bé có chùm 10 quả bóng bay, bị tuột tay bay mất 8 quả. Hỏi bé còn lại mấy quả bóng bay?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=yellow!20, draw=orange!80!black, line width=1.3pt, rounded corners=6pt] (-3.5,-0.65) rectangle (3.5,0.65);
  \node[font=\large\bfseries\color{blue!90!black}] at (0,0.05) {$10 - 8 = ?$};
  \node[below=3pt, font=\small\bfseries\color{purple!85!black}] at (0,-0.65) {10 quả bóng bay bớt đi 8 quả};
\end{tikzpicture}
\end{center}
\choice
{$1$ quả}
{\True $2$ quả}
{$3$ quả}
{$4$ quả}
\loigiai{
Bé còn lại: $10 - 8 = 2$ quả bóng bay.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 5 ---
\begin{ex} %[1D3H13]
Tính giá trị của biểu thức gồm 3 số: $3 + 4 + 2$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=cyan!12, draw=blue!80!black, line width=1.3pt, rounded corners=6pt] (-3.5,-0.6) rectangle (3.5,0.6);
  \node[font=\Large\bfseries\color{blue!90!black}] at (0,0) {$3 + 4 + 2 = ?$};
  \node[below=4pt, font=\small\bfseries\color{orange!90!black}] at (0,-0.65) {Thực hiện từ trái sang phải: $3 + 4 = 7$, rồi $7 + 2 = ?$};
\end{tikzpicture}
\end{center}
\choice
{$8$}
{\True $9$}
{$10$}
{$7$}
\loigiai{
Thực hiện từ trái sang phải: $3 + 4 = 7$; $7 + 2 = 9$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 6 ---
\begin{ex} %[1D3H13]
Tính giá trị biểu thức: $10 - 3 - 4$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=pink!20, draw=red!75!black, line width=1.3pt, rounded corners=6pt] (-3.5,-0.6) rectangle (3.5,0.6);
  \node[font=\Large\bfseries\color{red!90!black}] at (0,0) {$10 - 3 - 4 = ?$};
  \node[below=4pt, font=\small\bfseries\color{blue!85!black}] at (0,-0.65) {Thực hiện: $10 - 3 = 7$, rồi $7 - 4 = ?$};
\end{tikzpicture}
\end{center}
\choice
{$2$}
{\True $3$}
{$4$}
{$5$}
\loigiai{
Thực hiện: $10 - 3 = 7$; $7 - 4 = 3$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 7 ---
\begin{ex} %[1D3V13]
Tính giá trị biểu thức gồm cả phép trừ và phép cộng: $8 - 5 + 4$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=green!15, draw=green!70!black, line width=1.3pt, rounded corners=6pt] (-3.5,-0.6) rectangle (3.5,0.6);
  \node[font=\Large\bfseries\color{blue!90!black}] at (0,0) {$8 - 5 + 4 = ?$};
  \node[below=4pt, font=\small\bfseries\color{green!70!black}] at (0,-0.65) {Thực hiện: $8 - 5 = 3$, rồi $3 + 4 = ?$};
\end{tikzpicture}
\end{center}
\choice
{$6$}
{\True $7$}
{$8$}
{$9$}
\loigiai{
Thực hiện từ trái sang phải: $8 - 5 = 3$; $3 + 4 = 7$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 8 ---
\begin{ex} %[1D3V13]
Quan sát chiếc cân đĩa thăng bằng dưới đây. So sánh hai vế phép tính: $4 + 5$ và $10 - 1$:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Trụ cân
  \fill[gray!80!black] (-0.25,-1.2) rectangle (0.25,0);
  \fill[blue!90!black] (0,0) circle (0.15cm);
  \draw[fill=gray!60, draw=gray!90!black, line width=1pt] (-1.2,-1.4) rectangle (1.2,-1.15);
  \draw[line width=2.5pt, blue!90!black] (-3.0,0) -- (3.0,0);
  
  % Đĩa trái (4+5)
  \draw[line width=1pt, gray!70!black] (-3.0,0) -- (-3.8,-0.6);
  \draw[line width=1pt, gray!70!black] (-3.0,0) -- (-2.2,-0.6);
  \draw[fill=orange!25, draw=orange!90!black, line width=1.2pt] (-3.0,-0.6) ellipse (1.1cm and 0.25cm);
  \node[above=2pt, font=\small\bfseries\color{blue!90!black}] at (-3.0,-0.55) {$4 + 5 = 9$};
  
  % Đĩa phải (10-1)
  \draw[line width=1pt, gray!70!black] (3.0,0) -- (2.2,-0.6);
  \draw[line width=1pt, gray!70!black] (3.0,0) -- (3.8,-0.6);
  \draw[fill=orange!25, draw=orange!90!black, line width=1.2pt] (3.0,-0.6) ellipse (1.1cm and 0.25cm);
  \node[above=2pt, font=\small\bfseries\color{blue!90!black}] at (3.0,-0.55) {$10 - 1 = 9$};
  
  \node[below=4pt, font=\small\bfseries\color{purple!85!black}] at (0,-1.4) {Cân thăng bằng: $4 + 5 \dots 10 - 1$};
\end{tikzpicture}
\end{center}
\choice
{$>$}
{\True $=$}
{$<$}
{Không so sánh được}
\loigiai{
Ta có $4 + 5 = 9$ và $10 - 1 = 9$. Vì $9 = 9$ nên điền dấu $=$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 9 ---
\begin{ex} %[1D3V13]
Bạn Mai có 5 chiếc nhãn vở, bạn Lan có 4 chiếc nhãn vở như hình vẽ. Hỏi cả hai bạn có tất cả bao nhiêu chiếc nhãn vở?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % 5 nhãn vở Mai
  \draw[fill=yellow!15, draw=orange!80!black, line width=1.2pt, rounded corners=6pt] (-4.0,-0.8) rectangle (-0.5,0.8);
  \foreach \i in {0,1,2,3,4} {
    \draw[fill=cyan!30, draw=blue!85!black, line width=0.8pt] (\i*0.65-3.7,-0.4) rectangle (\i*0.65-3.2,0.4);
  }
  \node[below=3pt, font=\small\bfseries\color{orange!90!black}] at (-2.25,-0.85) {Mai có: 5 nhãn vở};
  
  \node[font=\LARGE\bfseries\color{blue!90!black}] at (0,0) {$+$};
  
  % 4 nhãn vở Lan
  \draw[fill=pink!20, draw=magenta!70!black, line width=1.2pt, rounded corners=6pt] (0.5,-0.8) rectangle (3.8,0.8);
  \foreach \i in {0,1,2,3} {
    \draw[fill=pink!50, draw=magenta!85!black, line width=0.8pt] (\i*0.7+1.0,-0.4) rectangle (\i*0.7+1.5,0.4);
  }
  \node[below=3pt, font=\small\bfseries\color{magenta!85!black}] at (2.15,-0.85) {Lan có: 4 nhãn vở};
\end{tikzpicture}
\end{center}
\choice
{$8$ cái}
{\True $9$ cái}
{$10$ cái}
{$7$ cái}
\loigiai{
Cả hai bạn có tất cả: $5 + 4 = 9$ cái nhãn vở.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 10 ---
\begin{ex} %[1D3V13]
Bình có 10 viên bi ve, Bình cho bạn Dũng 4 viên bi. Hỏi Bình còn lại bao nhiêu viên bi ve?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Hộp bi của Bình (6 viên còn lại)
  \draw[fill=blue!8, draw=blue!80!black, line width=1.3pt, rounded corners=8pt] (-4.2,-0.9) rectangle (0.5,0.9);
  \foreach \i in {0,1,2,3,4,5} {
    \VeVienBiVe[blue!80!cyan]{\i*0.7 - 3.6}{0}
  }
  \node[below=3pt, font=\small\bfseries\color{blue!90!black}] at (-1.55,-0.95) {Bình còn lại: ? viên};
  
  % Mũi tên cho Dũng
  \draw[->, >=stealth, line width=1.5pt, red!85!black] (0.7,0) -- (1.5,0);
  
  % 4 viên cho Dũng
  \draw[fill=orange!15, draw=orange!80!black, line width=1.3pt, rounded corners=8pt] (1.7,-0.9) rectangle (4.5,0.9);
  \foreach \i in {0,1,2,3} {
    \VeVienBiVe[orange!85!black]{\i*0.65 + 2.2}{0}
  }
  \node[below=3pt, font=\small\bfseries\color{orange!90!black}] at (3.1,-0.95) {Cho Dũng: 4 viên};
\end{tikzpicture}
\end{center}
\choice
{$5$ viên}
{\True $6$ viên}
{$7$ viên}
{$8$ viên}
\loigiai{
Bình còn lại: $10 - 4 = 6$ viên bi ve.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 11 ---
\begin{ex} %[1D3V13]
Tìm số thích hợp điền vào dấu hỏi chấm: $? + 3 = 8$.
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Sơ đồ tách gộp số 8
  \draw[line width=1.4pt, orange!80!black] (0,0.8) -- (-1.1,-0.5);
  \draw[line width=1.4pt, orange!80!black] (0,0.8) -- (1.1,-0.5);
  \draw[fill=orange!25, draw=orange!90!black, line width=1.3pt] (0,0.8) circle (0.55cm);
  \node[font=\large\bfseries\color{orange!95!black}] at (0,0.8) {8};
  \draw[fill=yellow!35, draw=orange!90!black, line width=1.2pt] (-1.1,-0.5) circle (0.5cm);
  \node[font=\large\bfseries\color{red!85!black}] at (-1.1,-0.5) {?};
  \draw[fill=cyan!25, draw=blue!90!black, line width=1.2pt] (1.1,-0.5) circle (0.5cm);
  \node[font=\large\bfseries\color{blue!95!black}] at (1.1,-0.5) {3};
\end{tikzpicture}
\end{center}
\choice
{$4$}
{\True $5$}
{$6$}
{$7$}
\loigiai{
Ta có: $8 - 3 = 5$. Vậy số cần tìm là \textbf{5}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 12 ---
\begin{ex} %[1D3C13]
Trên cành cây ban đầu có 8 chú chim. Lúc đầu có 2 chú bay đi, lúc sau có thêm 3 chú bay đến đậu cùng. Hỏi trên cành cây hiện có tất cả bao nhiêu chú chim?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \draw[fill=blue!6, draw=blue!70!black, line width=1.3pt, rounded corners=8pt] (-3.8,-0.6) rectangle (3.8,0.6);
  \node[font=\large\bfseries\color{blue!90!black}] at (0,0) {$8 - 2 + 3 = ?$};
  \node[below=4pt, font=\small\bfseries\color{orange!90!black}] at (0,-0.65) {8 chú, bay đi 2 chú, rồi bay đến 3 chú};
\end{tikzpicture}
\end{center}
\choice
{$8$ chú}
{\True $9$ chú}
{$10$ chú}
{$7$ chú}
\loigiai{
Thực hiện: $8 - 2 = 6$, sau đó $6 + 3 = 9$ chú chim.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% =========================================================================
% PHẦN 2: TRẮC NGHIỆM ĐÚNG SAI (2 CÂU)
% =========================================================================
\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% --- CÂU 13 ---
\begin{ex} %[1D3H13]
Quan sát bảng các phép tính trong phạm vi 10 và xét tính đúng sai của từng câu:
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=blue!6, draw=blue!70!black, line width=1.3pt, rounded corners=8pt] (-4.5,-1.15) rectangle (4.5,1.15);
  \node[font=\normalsize\bfseries\color{blue!90!black}] at (-3.2,0.45) {A. $4 + 4 = 8$};
  \node[font=\normalsize\bfseries\color{blue!90!black}] at (1.5,0.45) {B. $8 - 4 = 4$};
  \node[font=\normalsize\bfseries\color{red!80!black}] at (-3.2,-0.45) {C. $10 - 5 = 6$};
  \node[font=\normalsize\bfseries\color{green!70!black}] at (1.5,-0.45) {D. $10 - 5 = 5$};
\end{tikzpicture}
\end{center}
\choiceTF
{\True Phép tính $4 + 4 = 8$ là phép tính đúng.}
{\True Phép tính $8 - 4 = 4$ là phép tính đúng.}
{Phép tính $10 - 5 = 6$ là phép tính đúng.}
{\True Kết quả đúng của $10 - 5$ phải bằng $5$.}
\loigiai{
\begin{itemize}
    \item a) \textbf{Đúng}: $4 + 4 = 8$.
    \item b) \textbf{Đúng}: $8 - 4 = 4$.
    \item c) \textbf{Sai}: $10 - 5 = 5$, không phải bằng 6.
    \item d) \textbf{Đúng}: $10 - 5 = 5$.
\end{itemize}
}
\end{ex}

% --- CÂU 14 ---
\begin{ex} %[1D3V13]
Tổ 1 có 6 bạn nhỏ mặc áo xanh, tổ 2 có 4 bạn nhỏ mặc áo đỏ như hình vẽ:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Tổ 1 (6 bạn)
  \draw[fill=cyan!12, draw=blue!75!black, line width=1.2pt, rounded corners=6pt] (-4.2,-0.7) rectangle (-0.3,0.7);
  \foreach \i in {0,1,2,3,4,5} {
    \VeBanNho[blue!80]{\i*0.6 - 3.8}{-0.1}
  }
  \node[below=3pt, font=\small\bfseries\color{blue!90!black}] at (-2.25,-0.75) {Tổ 1: 6 bạn};
  
  % Tổ 2 (4 bạn)
  \draw[fill=pink!18, draw=red!75!black, line width=1.2pt, rounded corners=6pt] (0.3,-0.7) rectangle (3.5,0.7);
  \foreach \i in {0,1,2,3} {
    \VeBanNho[red!80]{\i*0.65 + 0.8}{-0.1}
  }
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (1.9,-0.75) {Tổ 2: 4 bạn};
\end{tikzpicture}
\end{center}
Xét tính đúng sai của các câu sau:
\choiceTF
{\True Cả hai tổ có tất cả 10 bạn nhỏ ($6 + 4 = 10$).}
{\True Tổ 1 có nhiều hơn tổ 2 là 2 bạn nhỏ ($6 - 4 = 2$).}
{Nếu tổ 1 chuyển sang tổ 2 một bạn thì tổ 2 có 6 bạn.}
{\True Khi chuyển 1 bạn từ tổ 1 sang thì tổ 2 có 5 bạn ($4 + 1 = 5$).}
\loigiai{
\begin{itemize}
    \item a) \textbf{Đúng}: $6 + 4 = 10$ bạn.
    \item b) \textbf{Đúng}: $6 - 4 = 2$ bạn.
    \item c) \textbf{Sai}: Tổ 2 ban đầu có 4 bạn, thêm 1 bạn thì có 5 bạn, không phải 6 bạn.
    \item d) \textbf{Đúng}: $4 + 1 = 5$ bạn.
\end{itemize}
}
\end{ex}

% =========================================================================
% PHẦN 3: TRẢ LỜI NGẮN (6 CÂU)
% =========================================================================
\textbf{Phần 3. Trả lời ngắn (Quan sát hình vẽ và điền số thích hợp)}
\setcounterpageref{ex}{0}

% --- CÂU 15 ---
\begin{ex} %[1D3H13]
Tính kết quả phép tính: $2 + 7$.
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  % 2 que đỏ
  \draw[line width=3pt, red!85!black, line cap=round] (-2.8,-0.5) -- (-2.8,0.5);
  \draw[line width=3pt, red!85!black, line cap=round] (-2.2,-0.5) -- (-2.2,0.5);
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (-2.5,-0.6) {2 que};
  
  \node[font=\LARGE\bfseries\color{blue!90!black}] at (-1.2,0) {$+$};
  
  % 7 que xanh
  \foreach \i in {0,1,2,3,4,5,6} {
    \draw[line width=3pt, blue!80!black, line cap=round] (\i*0.5 - 0.2,-0.5) -- (\i*0.5 - 0.2,0.5);
  }
  \node[below=3pt, font=\small\bfseries\color{blue!85!black}] at (1.3,-0.6) {7 que};
\end{tikzpicture}
\end{center}
\shortans{9}
\loigiai{
\textbf{Đáp số:} $9$\\
$2 + 7 = 9$.
}
\end{ex}

% --- CÂU 16 ---
\begin{ex} %[1D3H13]
Tính kết quả phép tính: $10 - 5$.
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=yellow!20, draw=orange!90!black, line width=1.3pt, rounded corners=6pt] (-3.0,-0.55) rectangle (3.0,0.55);
  \node[font=\Large\bfseries\color{blue!90!black}] at (0,0) {$10 - 5 = ?$};
\end{tikzpicture}
\end{center}
\shortans{5}
\loigiai{
\textbf{Đáp số:} $5$\\
$10 - 5 = 5$.
}
\end{ex}

\newpage
% --- CÂU 17 ---
\begin{ex} %[1D3V13]
Tính giá trị biểu thức: $3 + 5 - 4$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=cyan!15, draw=blue!80!black, line width=1.3pt, rounded corners=6pt] (-3.2,-0.55) rectangle (3.2,0.55);
  \node[font=\Large\bfseries\color{blue!95!black}] at (0,0) {$3 + 5 - 4 = ?$};
\end{tikzpicture}
\end{center}
\shortans{4}
\loigiai{
\textbf{Đáp số:} $4$\\
$3 + 5 = 8$; $8 - 4 = 4$.
}
\end{ex}

% --- CÂU 18 ---
\begin{ex} %[1D3V13]
Tính giá trị biểu thức: $10 - 7 + 6$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=pink!25, draw=purple!80!black, line width=1.3pt, rounded corners=6pt] (-3.2,-0.55) rectangle (3.2,0.55);
  \node[font=\Large\bfseries\color{purple!90!black}] at (0,0) {$10 - 7 + 6 = ?$};
\end{tikzpicture}
\end{center}
\shortans{9}
\loigiai{
\textbf{Đáp số:} $9$\\
$10 - 7 = 3$; $3 + 6 = 9$.
}
\end{ex}

% --- CÂU 19 ---
\begin{ex} %[1D3V13]
Tìm số thích hợp điền vào dấu hỏi chấm: $? - 3 = 6$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=yellow!30, draw=orange!90!black, line width=1.3pt, rounded corners=5pt] (-2.5,-0.55) rectangle (-1.3,0.55);
  \node[font=\Large\bfseries\color{red!85!black}] at (-1.9,0) {?};
  
  \draw[->, >=stealth, line width=1.4pt, blue!85!black] (-1.2,0) -- (0.2,0);
  \node[above=2pt, font=\small\bfseries\color{blue!85!black}] at (-0.5,0.1) {$- \ 3$};
  
  \draw[fill=green!20, draw=green!80!black, line width=1.3pt, rounded corners=5pt] (0.3,-0.55) rectangle (1.5,0.55);
  \node[font=\Large\bfseries\color{green!70!black}] at (0.9,0) {6};
\end{tikzpicture}
\end{center}
\shortans{9}
\loigiai{
\textbf{Đáp số:} $9$\\
$6 + 3 = 9$.
}
\end{ex}

% --- CÂU 20 ---
\begin{ex} %[1D3C13]
Mẹ có 10 quả cam, mẹ chia đều vào 2 đĩa sao cho đĩa thứ nhất có 6 quả. Hỏi đĩa thứ hai có bao nhiêu quả cam?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  % Đĩa 1: 6 quả
  \draw[fill=orange!15, draw=orange!80!black, line width=1.2pt] (-2.5,-0.2) ellipse (1.8cm and 0.5cm);
  \foreach \i in {0,1,2,3,4,5} {
    \fill[orange!90!black] (\i*0.55 - 3.85, 0.05) circle (0.22cm);
  }
  \node[below=3pt, font=\small\bfseries\color{orange!90!black}] at (-2.5,-0.35) {Đĩa 1: 6 quả};
  
  % Đĩa 2: ? quả
  \draw[fill=orange!15, draw=orange!80!black, line width=1.2pt] (2.5,-0.2) ellipse (1.8cm and 0.5cm);
  \node[font=\Large\bfseries\color{red!85!black}] at (2.5,0.1) {? quả};
  \node[below=3pt, font=\small\bfseries\color{blue!85!black}] at (2.5,-0.35) {Tổng cộng có 10 quả};
\end{tikzpicture}
\end{center}
\shortans{4}
\loigiai{
\textbf{Đáp số:} $4$\\
Đĩa thứ hai có: $10 - 6 = 4$ quả cam.
}
\end{ex}
'''

# 1. Ghi nội dung vào file bài học
lesson_file = r'CHỦ ĐỀ 3 - PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10/Chuong3_Bai13_LuyenTapChung.tex'
with open(lesson_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Wrote {lesson_file} successfully')

# 2. Lắp ráp file test độc lập theo mẫu chuẩn Bai_01_preview.tex
with open('Bai_01_preview.tex', 'r', encoding='utf-8') as f:
    t1 = f.read()

t1 = t1.replace('BÀI 01: CÁC SỐ 0, 1, 2, 3, 4, 5', 'BÀI 13: LUYỆN TẬP CHUNG')
t1 = t1.replace('CHỦ ĐỀ 1 -- CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 3 -- PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10')
t1 = t1.replace('bai-01', 'bai-13')
t1 = t1.replace('Chuong1_Bai01_CacSo0_1_2_3_4_5.tex', 'Chuong3_Bai13_LuyenTapChung.tex')
t1 = t1.replace('CHỦ ĐỀ 1 - CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 3 - PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10')

test_file = 'test_bai13.tex'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(t1)
print(f'Created {test_file} successfully')
