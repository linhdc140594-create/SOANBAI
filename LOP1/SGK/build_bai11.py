# -*- coding: utf-8 -*-
import os, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 11: PHÉP TRỪ TRONG PHẠM VI 10 (CHỦ ĐỀ 3 - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ
% =========================================================================

% --- CÁC HÀM VẼ ĐỒ VẬT, CON VẬT TRỰC QUAN CHO PHÉP TRỪ LỚP 1 ---
\providecommand{\VeQuaTaoDo}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.6]
    \fill[red!85!black] (-0.11,0.08) circle (0.22cm);
    \fill[red!85!black] (0.11,0.08) circle (0.22cm);
    \fill[red!85!black] (0,-0.05) circle (0.24cm);
    \draw[line width=1pt, brown!80!black] (0,0.24) to[out=70,in=-110] (0.06,0.42);
    \fill[green!70!black] (0.05,0.36) to[out=20,in=160] (0.24,0.42) to[out=-120,in=-20] cycle;
  \end{scope}
}

\providecommand{\VeQuaTaoGachBo}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.6]
    \fill[red!45!white] (-0.11,0.08) circle (0.22cm);
    \fill[red!45!white] (0.11,0.08) circle (0.22cm);
    \fill[red!45!white] (0,-0.05) circle (0.24cm);
    \draw[line width=1pt, brown!40!white] (0,0.24) to[out=70,in=-110] (0.06,0.42);
    % Dấu gạch chéo đỏ to
    \draw[line width=2.4pt, red!90!black] (-0.3,-0.3) -- (0.3,0.3);
    \draw[line width=2.4pt, red!90!black] (-0.3,0.3) -- (0.3,-0.3);
  \end{scope}
}

\providecommand{\VeBongBay}[3][blue!75!cyan]{% #1=màu, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.55]
    \fill[#1] (0,0.25) ellipse (0.28cm and 0.35cm);
    \fill[#1!85!black] (-0.05,-0.12) -- (0.05,-0.12) -- (0,-0.18) -- cycle;
    \draw[line width=0.8pt, gray!80!black] (0,-0.18) to[out=-80,in=80] (-0.06,-0.55);
  \end{scope}
}

\providecommand{\VeBongBayNo}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.55]
    \draw[dashed, line width=1.2pt, red!70!black] (0,0.25) ellipse (0.28cm and 0.35cm);
    \draw[line width=2.2pt, red!85!black] (-0.3,-0.05) -- (0.3,0.55);
    \draw[line width=2.2pt, red!85!black] (-0.3,0.55) -- (0.3,-0.05);
    \draw[line width=0.8pt, gray!60!black] (0,-0.18) to[out=-80,in=80] (-0.06,-0.55);
  \end{scope}
}

\providecommand{\VeChuChimDau}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.55]
    \fill[cyan!85!blue] (0,0.1) ellipse (0.26cm and 0.2cm);
    \fill[cyan!95!black] (0.18,0.22) circle (0.15cm);
    \fill[orange!95!black] (0.32,0.22) -- (0.45,0.19) -- (0.32,0.15) -- cycle;
    \fill[white] (0.22,0.25) circle (0.04cm);
    \fill[black] (0.24,0.25) circle (0.02cm);
    \fill[blue!80!black] (-0.22,0.1) -- (-0.45,0.18) -- (-0.38,0.04) -- cycle;
  \end{scope}
}

\providecommand{\VeChuChimBayDi}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.55, opacity=0.7]
    \fill[orange!90!red] (0,0.1) ellipse (0.26cm and 0.18cm);
    \fill[orange!95!black] (0.18,0.22) circle (0.14cm);
    \fill[yellow!90!black] (0.31,0.22) -- (0.43,0.19) -- (0.31,0.15) -- cycle;
    \fill[white] (0.22,0.25) circle (0.04cm);
    \fill[black] (0.24,0.25) circle (0.02cm);
    \fill[red!80!black] (-0.05,0.15) -- (-0.2,0.48) -- (0.08,0.2) -- cycle;
  \end{scope}
}

\providecommand{\VeChuEch}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.55]
    \fill[green!75!black] (0,0) ellipse (0.32cm and 0.22cm);
    \fill[green!85!black] (-0.15,0.2) circle (0.11cm);
    \fill[green!85!black] (0.15,0.2) circle (0.11cm);
    \fill[white] (-0.15,0.22) circle (0.05cm);
    \fill[black] (-0.15,0.22) circle (0.025cm);
    \fill[white] (0.15,0.22) circle (0.05cm);
    \fill[black] (0.15,0.22) circle (0.025cm);
    \draw[line width=0.8pt, red!85!black] (-0.12,-0.08) arc (-150:-30:0.14cm);
  \end{scope}
}

% =========================================================================
% PHẦN 1: TRẮC NGHIỆM LỰA CHỌN (12 CÂU)
% =========================================================================
\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- CÂU 1 ---
\begin{ex} %[1D3N11]
Đĩa có 5 quả táo, bạn Nam ăn mất 2 quả (bị gạch chéo đỏ). Hỏi trên đĩa còn lại mấy quả táo?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Đĩa quả
  \draw[fill=orange!15, draw=orange!80!black, line width=1.3pt] (0,-0.2) ellipse (2.8cm and 0.6cm);
  % 3 quả còn lại
  \VeQuaTaoDo{-2.0}{0.05}
  \VeQuaTaoDo{-1.0}{0.05}
  \VeQuaTaoDo{0}{0.05}
  % 2 quả bị gạch bỏ
  \VeQuaTaoGachBo{1.1}{0.05}
  \VeQuaTaoGachBo{2.1}{0.05}
  
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (-1.0,-0.45) {Còn lại: 3 quả};
  \node[below=4pt, font=\small\bfseries\color{red!85!black}] at (1.6,-0.45) {Đã bớt: 2 quả};
\end{tikzpicture}
\end{center}
\choice
{$2$ quả}
{\True $3$ quả}
{$4$ quả}
{$5$ quả}
\loigiai{
Phép tính bớt đi là: $5 - 2 = 3$ quả táo.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 2 ---
\begin{ex} %[1D3N11]
Băng giấy có 7 ô vuông, đã gạch chéo bỏ đi 4 ô như hình vẽ. Hỏi còn lại bao nhiêu ô vuông trắng?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  % 3 ô trắng còn lại
  \foreach \i in {0,1,2} {
    \draw[fill=white, draw=blue!85!black, line width=1.2pt] (\i*1.1 - 3.85, -0.55) rectangle (\i*1.1 - 2.75, 0.55);
    \node[font=\small\bfseries\color{blue!90!black}] at (\i*1.1 - 3.3, 0) {\pgfmathparse{int(\i+1)}\pgfmathresult};
  }
  % 4 ô bị gạch chéo
  \foreach \i in {0,1,2,3} {
    \draw[fill=gray!15, draw=gray!70!black, line width=1.2pt] (\i*1.1 - 0.55, -0.55) rectangle (\i*1.1 + 0.55, 0.55);
    \draw[line width=1.8pt, red!85!black] (\i*1.1 - 0.55, -0.55) -- (\i*1.1 + 0.55, 0.55);
    \draw[line width=1.8pt, red!85!black] (\i*1.1 - 0.55, 0.55) -- (\i*1.1 + 0.55, -0.55);
  }
  \node[below=4pt, font=\small\bfseries\color{blue!85!black}] at (-2.2,-0.65) {Còn lại: 3 ô};
  \node[below=4pt, font=\small\bfseries\color{red!85!black}] at (1.1,-0.65) {Bớt đi: 4 ô};
\end{tikzpicture}
\end{center}
\choice
{$2$ ô}
{\True $3$ ô}
{$4$ ô}
{$5$ ô}
\loigiai{
Phép tính: $7 - 4 = 3$ ô vuông.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 3 ---
\begin{ex} %[1D3H11]
Trên đĩa có 6 chiếc kẹo, em không ăn chiếc nào (bớt đi 0 chiếc). Hỏi trên đĩa còn lại bao nhiêu chiếc kẹo?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=yellow!20, draw=orange!80!black, line width=1.3pt] (0,-0.2) ellipse (2.9cm and 0.6cm);
  \foreach \i in {0,1,2,3,4,5} {
    \draw[fill=magenta!75!red, draw=purple!80!black, line width=0.8pt, rounded corners=2.5pt] (\i*0.85 - 2.15, -0.15) rectangle (\i*0.85 - 1.65, 0.15);
  }
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (0,-0.45) {Có 6 chiếc kẹo, bớt đi 0 chiếc ($6 - 0 = ?$)};
\end{tikzpicture}
\end{center}
\choice
{$0$ chiếc}
{\True $6$ chiếc}
{$5$ chiếc}
{$7$ chiếc}
\loigiai{
Một số trừ đi 0 bằng chính nó: $6 - 0 = 6$ chiếc kẹo.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 4 ---
\begin{ex} %[1D3H11]
Tổ có 8 bạn nhỏ, cả 8 bạn đều đã đi về nhà. Hỏi trong lớp còn lại mấy bạn nhỏ?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Phòng học trống
  \draw[fill=blue!6, draw=blue!70!black, line width=1.3pt, rounded corners=6pt] (-3.5,-0.9) rectangle (3.5,0.9);
  \node[font=\large\bfseries\color{red!85!black}] at (0,0.1) {8 bạn $-$ 8 bạn = ? bạn};
  \node[below=4pt, font=\small\itshape\color{gray!80!black}] at (0,-0.35) {(Tất cả các bạn đều đã về)};
\end{tikzpicture}
\end{center}
\choice
{$8$ bạn}
{\True $0$ bạn}
{$1$ bạn}
{$16$ bạn}
\loigiai{
Hai số bằng nhau trừ cho nhau bằng 0: $8 - 8 = 0$ bạn.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 5 ---
\begin{ex} %[1D3H11]
Khung mười ô có 9 chấm tròn, người ta gạch chéo bỏ đi 5 chấm tròn. Hỏi còn lại bao nhiêu chấm tròn không bị gạch?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  % Khung 10 ô (2x5)
  \draw[fill=white, draw=blue!85!black, line width=1.5pt] (-2.75,-1.1) rectangle (2.75,1.1);
  \foreach \x in {-1.65, -0.55, 0.55, 1.65} {
    \draw[line width=1pt, blue!70!black] (\x,-1.1) -- (\x,1.1);
  }
  \draw[line width=1pt, blue!70!black] (-2.75,0) -- (2.75,0);
  
  % Hàng trên: 5 chấm bị gạch chéo
  \foreach \x in {-2.2, -1.1, 0, 1.1, 2.2} {
    \fill[gray!30] (\x,0.55) circle (0.35cm);
    \draw[line width=2pt, red!85!black] (\x-0.25,0.3) -- (\x+0.25,0.8);
    \draw[line width=2pt, red!85!black] (\x-0.25,0.8) -- (\x+0.25,0.3);
  }
  % Hàng dưới: 4 chấm xanh còn nguyên, 1 ô trống
  \foreach \x in {-2.2, -1.1, 0, 1.1} {
    \fill[cyan!75!blue] (\x,-0.55) circle (0.35cm);
  }
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (0,-1.2) {9 chấm ban đầu, gạch bỏ 5 chấm ($9 - 5 = ?$)};
\end{tikzpicture}
\end{center}
\choice
{$3$ chấm}
{\True $4$ chấm}
{$5$ chấm}
{$6$ chấm}
\loigiai{
Phép tính: $9 - 5 = 4$ chấm tròn.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 6 ---
\begin{ex} %[1D3H11]
Bó hoa có 10 bông, đã cắm vào lọ 7 bông. Hỏi trên bàn còn lại mấy bông hoa chưa cắm?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Lọ hoa đã cắm 7 bông
  \draw[fill=cyan!20, draw=blue!85!black, line width=1.3pt] (-2.2,-0.9) rectangle (-0.6,0.3);
  \node[font=\small\bfseries\color{blue!90!black}] at (-1.4,-0.3) {Đã cắm:};
  \node[font=\large\bfseries\color{red!85!black}] at (-1.4,0.6) {7 bông};
  
  % Dấu hỏi chấm số hoa còn lại
  \draw[fill=yellow!25, draw=orange!90!black, line width=1.3pt, rounded corners=6pt] (0.8,-0.9) rectangle (3.2,0.9);
  \node[font=\small\bfseries\color{orange!90!black}] at (2.0,0.35) {Chưa cắm:};
  \node[font=\LARGE\bfseries\color{red!85!black}] at (2.0,-0.2) {? bông};
  
  \node[below=4pt, font=\small\bfseries\color{purple!85!black}] at (0.3,-1.05) {Tổng cộng có 10 bông ($10 - 7 = ?$)};
\end{tikzpicture}
\end{center}
\choice
{$2$ bông}
{\True $3$ bông}
{$4$ bông}
{$5$ bông}
\loigiai{
Số bông hoa còn lại là: $10 - 7 = 3$ bông.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 7 ---
\begin{ex} %[1D3V11]
Bé có chùm 8 quả bóng bay, bị tuột tay bay mất 3 quả như hình vẽ. Hỏi bé còn lại bao nhiêu quả bóng bay?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % 5 quả bóng còn giữ
  \VeBongBay[blue!75!cyan]{-2.6}{0.2}
  \VeBongBay[blue!75!cyan]{-1.9}{0.5}
  \VeBongBay[blue!75!cyan]{-1.2}{0.1}
  \VeBongBay[blue!75!cyan]{-2.3}{-0.4}
  \VeBongBay[blue!75!cyan]{-1.5}{-0.3}
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (-1.9,-0.8) {Còn lại: 5 quả};
  
  % 3 quả bay đi
  \VeBongBayNo{1.2}{0.4}
  \VeBongBayNo{2.1}{0.8}
  \VeBongBayNo{2.8}{0.3}
  \draw[->, >=stealth, dashed, line width=1.3pt, red!85!black] (0.5,0) -- (3.2,1.1);
  \node[below=4pt, font=\small\bfseries\color{red!85!black}] at (2.0,-0.8) {Bay mất: 3 quả};
\end{tikzpicture}
\end{center}
\choice
{$4$ quả}
{\True $5$ quả}
{$6$ quả}
{$7$ quả}
\loigiai{
Bé còn lại: $8 - 3 = 5$ quả bóng bay.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 8 ---
\begin{ex} %[1D3V11]
Trên cành cây ban đầu có 9 chú chim, sau đó 4 chú chim bay đi. Hỏi trên cành cây còn lại bao nhiêu chú chim?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Cành cây
  \draw[brown!80!black, line width=3.8pt, line cap=round] (-3.8,-0.2) -- (0.8,-0.2);
  % 5 chú chim còn đậu
  \VeChuChimDau{-3.2}{0.1}
  \VeChuChimDau{-2.3}{0.1}
  \VeChuChimDau{-1.4}{0.1}
  \VeChuChimDau{-0.5}{0.1}
  \VeChuChimDau{0.4}{0.1}
  \node[below=4pt, font=\small\bfseries\color{blue!90!black}] at (-1.4,-0.35) {Còn lại: 5 chú chim};
  
  % 4 chú chim bay đi
  \VeChuChimBayDi{1.8}{0.7}
  \VeChuChimBayDi{2.7}{1.1}
  \VeChuChimBayDi{2.2}{0.1}
  \VeChuChimBayDi{3.3}{0.5}
  \draw[->, >=stealth, dashed, line width=1.2pt, orange!90!black] (1.2,0.2) -- (3.6,1.2);
  \node[below=4pt, font=\small\bfseries\color{orange!90!black}] at (2.6,-0.35) {Bay đi: 4 chú chim};
\end{tikzpicture}
\end{center}
\choice
{$4$ chú chim}
{\True $5$ chú chim}
{$6$ chú chim}
{$3$ chú chim}
\loigiai{
Trên cây còn lại: $9 - 4 = 5$ chú chim.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 9 ---
\begin{ex} %[1D3V11]
Hộp có 10 chiếc bút chì, bạn An lấy ra 2 chiếc, sau đó bạn Bình lấy tiếp 3 chiếc nữa. Trong hộp còn lại mấy chiếc bút chì?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=yellow!15, draw=orange!80!black, line width=1.3pt, rounded corners=6pt] (-4.0,-0.8) rectangle (4.0,0.8);
  \node[font=\large\bfseries\color{blue!90!black}] at (0,0.1) {$10 - 2 - 3 = ?$};
  \node[below=4pt, font=\small\bfseries\color{purple!85!black}] at (0,-0.4) {10 bớt 2 rồi bớt tiếp 3};
\end{tikzpicture}
\end{center}
\choice
{$4$ chiếc}
{\True $5$ chiếc}
{$6$ chiếc}
{$7$ chiếc}
\loigiai{
Thực hiện từ trái sang phải: $10 - 2 = 8$, rồi $8 - 3 = 5$ chiếc bút chì.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 10 ---
\begin{ex} %[1D3V11]
Quan sát chiếc cân đĩa thăng bằng ở hình dưới. So sánh hai vế phép tính $9 - 3$ và $10 - 4$:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Trụ cân
  \fill[gray!80!black] (-0.25,-1.2) rectangle (0.25,0);
  \fill[blue!90!black] (0,0) circle (0.15cm);
  \draw[fill=gray!60, draw=gray!90!black, line width=1pt] (-1.2,-1.4) rectangle (1.2,-1.15);
  \draw[line width=2.5pt, blue!90!black] (-3.0,0) -- (3.0,0);
  
  % Đĩa trái (9-3)
  \draw[line width=1pt, gray!70!black] (-3.0,0) -- (-3.8,-0.6);
  \draw[line width=1pt, gray!70!black] (-3.0,0) -- (-2.2,-0.6);
  \draw[fill=orange!25, draw=orange!90!black, line width=1.2pt] (-3.0,-0.6) ellipse (1.1cm and 0.25cm);
  \node[above=2pt, font=\small\bfseries\color{blue!90!black}] at (-3.0,-0.55) {$9 - 3 = 6$};
  
  % Đĩa phải (10-4)
  \draw[line width=1pt, gray!70!black] (3.0,0) -- (2.2,-0.6);
  \draw[line width=1pt, gray!70!black] (3.0,0) -- (3.8,-0.6);
  \draw[fill=orange!25, draw=orange!90!black, line width=1.2pt] (3.0,-0.6) ellipse (1.1cm and 0.25cm);
  \node[above=2pt, font=\small\bfseries\color{blue!90!black}] at (3.0,-0.55) {$10 - 4 = 6$};
  
  \node[below=4pt, font=\small\bfseries\color{purple!85!black}] at (0,-1.4) {Cân thăng bằng: $9 - 3 \dots 10 - 4$};
\end{tikzpicture}
\end{center}
\choice
{$>$}
{\True $=$}
{$<$}
{Không so sánh được}
\loigiai{
Ta có: $9 - 3 = 6$ và $10 - 4 = 6$. Vì $6 = 6$ nên điền dấu $=$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 11 ---
\begin{ex} %[1D3V11]
Mẹ mua 10 quả cam, mẹ đem biếu bà 4 quả. Hỏi mẹ còn lại bao nhiêu quả cam?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Khung cam còn lại (6 quả)
  \draw[fill=orange!15, draw=orange!80!black, line width=1.2pt, rounded corners=6pt] (-3.8,-0.8) rectangle (0.2,0.8);
  \foreach \i in {0,1,2,3,4,5} {
    \fill[orange!90!black] (\i*0.6 - 3.3, 0) circle (0.24cm);
  }
  \node[below=3pt, font=\small\bfseries\color{orange!90!black}] at (-1.8,-0.85) {Mẹ còn lại: 6 quả};
  
  % Mũi tên biếu bà
  \draw[->, >=stealth, line width=1.4pt, red!85!black] (0.4,0) -- (1.2,0);
  
  % 4 quả biếu bà
  \draw[fill=pink!20, draw=red!70!black, line width=1.2pt, rounded corners=6pt] (1.4,-0.8) rectangle (4.0,0.8);
  \foreach \i in {0,1,2,3} {
    \fill[orange!60!white] (\i*0.6 + 1.8, 0) circle (0.24cm);
    \draw[line width=1.4pt, red!85!black] (\i*0.6+1.6,-0.2) -- (\i*0.6+2.0,0.2);
  }
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (2.7,-0.85) {Biếu bà: 4 quả};
\end{tikzpicture}
\end{center}
\choice
{$5$ quả}
{\True $6$ quả}
{$7$ quả}
{$4$ quả}
\loigiai{
Mẹ còn lại: $10 - 4 = 6$ quả cam.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 12 ---
\begin{ex} %[1D3C11]
Tìm số thích hợp điền vào hình ngôi sao để có phép tính đúng: $8 - \bigstar = 6 - 3$.
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Vế phải: 6 - 3 = 3
  \draw[fill=blue!8, draw=blue!70!black, line width=1.2pt, rounded corners=6pt] (-3.6,-0.55) rectangle (3.6,0.55);
  \node[font=\large\bfseries\color{blue!90!black}] at (0,0) {$8 - \bigstar = 6 - 3$};
  \node[below=4pt, font=\small\bfseries\color{orange!90!black}] at (0,-0.65) {Biết rằng: $6 - 3 = 3$};
\end{tikzpicture}
\end{center}
\choice
{$4$}
{\True $5$}
{$6$}
{$3$}
\loigiai{
Ta có $6 - 3 = 3$. Để $8 - \bigstar = 3$ thì $\bigstar = 8 - 3 = 5$.\\
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
\begin{ex} %[1D3H11]
Quan sát bảng các phép tính trừ trong phạm vi 10 và xét tính đúng sai của từng câu:
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=purple!6, draw=purple!70!black, line width=1.3pt, rounded corners=8pt] (-4.5,-1.15) rectangle (4.5,1.15);
  \node[font=\normalsize\bfseries\color{blue!90!black}] at (-3.2,0.45) {A. $7 - 3 = 4$};
  \node[font=\normalsize\bfseries\color{blue!90!black}] at (1.5,0.45) {B. $10 - 5 = 5$};
  \node[font=\normalsize\bfseries\color{red!80!black}] at (-3.2,-0.45) {C. $9 - 4 = 6$};
  \node[font=\normalsize\bfseries\color{green!70!black}] at (1.5,-0.45) {D. $8 - 0 = 8$};
\end{tikzpicture}
\end{center}
\choiceTF
{\True Phép tính $7 - 3 = 4$ là phép tính đúng.}
{\True Phép tính $10 - 5 = 5$ là phép tính đúng.}
{Phép tính $9 - 4 = 6$ là phép tính đúng.}
{\True Phép tính $8 - 0 = 8$ là phép tính đúng.}
\loigiai{
\begin{itemize}
    \item a) \textbf{Đúng}: $7 - 3 = 4$.
    \item b) \textbf{Đúng}: $10 - 5 = 5$.
    \item c) \textbf{Sai}: $9 - 4 = 5$, không phải bằng $6$.
    \item d) \textbf{Đúng}: $8 - 0 = 8$.
\end{itemize}
}
\end{ex}

% --- CÂU 14 ---
\begin{ex} %[1D3V11]
Trên đĩa ban đầu có 8 chiếc bánh quy. Bạn An ăn 3 chiếc, bạn Bình ăn 2 chiếc như hình vẽ:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=yellow!15, draw=orange!80!black, line width=1.3pt] (0,-0.2) ellipse (3.5cm and 0.65cm);
  % 3 bánh còn lại
  \foreach \i in {0,1,2} {
    \fill[brown!80!black] (\i*0.8 - 2.5, 0.05) circle (0.24cm);
  }
  \node[below=2pt, font=\scriptsize\bfseries\color{blue!90!black}] at (-1.7,-0.4) {Còn lại: 3 bánh};
  
  % 3 bánh An ăn
  \foreach \i in {0,1,2} {
    \fill[gray!40] (\i*0.8 - 0.2, 0.05) circle (0.24cm);
    \draw[line width=1.5pt, red!85!black] (\i*0.8-0.35,-0.1) -- (\i*0.8-0.05,0.2);
  }
  \node[below=2pt, font=\scriptsize\bfseries\color{red!85!black}] at (0.6,-0.4) {An ăn: 3};
  
  % 2 bánh Bình ăn
  \foreach \i in {0,1} {
    \fill[gray!40] (\i*0.8 + 1.9, 0.05) circle (0.24cm);
    \draw[line width=1.5pt, red!85!black] (\i*0.8+1.75,-0.1) -- (\i*0.8+2.05,0.2);
  }
  \node[below=2pt, font=\scriptsize\bfseries\color{orange!90!black}] at (2.3,-0.4) {Bình ăn: 2};
\end{tikzpicture}
\end{center}
Xét tính đúng sai của các câu sau:
\choiceTF
{\True Cả hai bạn An và Bình đã ăn tất cả 5 chiếc bánh ($3 + 2 = 5$).}
{\True Số bánh quy còn lại trên đĩa là 3 chiếc ($8 - 5 = 3$).}
{Bạn An ăn ít hơn bạn Bình 1 chiếc bánh.}
{\True Bạn An ăn nhiều hơn bạn Bình 1 chiếc bánh ($3 - 2 = 1$).}
\loigiai{
\begin{itemize}
    \item a) \textbf{Đúng}: Hai bạn đã ăn: $3 + 2 = 5$ chiếc bánh.
    \item b) \textbf{Đúng}: Trên đĩa còn lại: $8 - 5 = 3$ chiếc bánh.
    \item c) \textbf{Sai}: An ăn 3 chiếc, Bình ăn 2 chiếc nên An ăn nhiều hơn Bình, không phải ít hơn.
    \item d) \textbf{Đúng}: $3 - 2 = 1$ chiếc bánh.
\end{itemize}
}
\end{ex}

% =========================================================================
% PHẦN 3: TRẢ LỜI NGẮN (6 CÂU)
% =========================================================================
\textbf{Phần 3. Trả lời ngắn (Quan sát hình vẽ và điền số thích hợp)}
\setcounterpageref{ex}{0}

% --- CÂU 15 ---
\begin{ex} %[1D3H11]
Có 7 quả dâu tây, ăn bớt đi 2 quả (bị gạch chéo). Hỏi còn lại bao nhiêu quả dâu tây?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  % 5 quả còn lại
  \foreach \i in {0,1,2,3,4} {
    \VeQuaTaoDo{\i*1.0 - 2.8}{0}
  }
  % 2 quả bị gạch bỏ
  \VeQuaTaoGachBo{2.6}{0}
  \VeQuaTaoGachBo{3.6}{0}
\end{tikzpicture}
\end{center}
\shortans{5}
\loigiai{
\textbf{Đáp số:} $5$\\
$7 - 2 = 5$.
}
\end{ex}

% --- CÂU 16 ---
\begin{ex} %[1D3H11]
Thanh 10 ô vuông có 4 ô bị gạch chéo bỏ đi. Hỏi còn lại bao nhiêu ô vuông chưa gạch?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \foreach \i in {0,1,2,3,4,5} {
    \draw[fill=white, draw=blue!85!black, line width=1.1pt] (\i*0.9 - 4.5, -0.45) rectangle (\i*0.9 - 3.6, 0.45);
    \node[font=\small\bfseries\color{blue!90!black}] at (\i*0.9 - 4.05, 0) {\pgfmathparse{int(\i+1)}\pgfmathresult};
  }
  \foreach \i in {0,1,2,3} {
    \draw[fill=gray!20, draw=gray!70!black, line width=1.1pt] (\i*0.9 + 0.9, -0.45) rectangle (\i*0.9 + 1.8, 0.45);
    \draw[line width=1.6pt, red!85!black] (\i*0.9+0.9,-0.45) -- (\i*0.9+1.8,0.45);
    \draw[line width=1.6pt, red!85!black] (\i*0.9+0.9,0.45) -- (\i*0.9+1.8,-0.45);
  }
\end{tikzpicture}
\end{center}
\shortans{6}
\loigiai{
\textbf{Đáp số:} $6$\\
$10 - 4 = 6$.
}
\end{ex}

\newpage
% --- CÂU 17 ---
\begin{ex} %[1D3V11]
Tính giá trị biểu thức: $9 - 3 - 2$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=cyan!15, draw=blue!80!black, line width=1.3pt, rounded corners=6pt] (-3.2,-0.6) rectangle (3.2,0.6);
  \node[font=\Large\bfseries\color{blue!95!black}] at (0,0) {$9 - 3 - 2 = ?$};
\end{tikzpicture}
\end{center}
\shortans{4}
\loigiai{
\textbf{Đáp số:} $4$\\
$9 - 3 = 6$; $6 - 2 = 4$.
}
\end{ex}

% --- CÂU 18 ---
\begin{ex} %[1D3V11]
Tìm số thích hợp điền vào dấu hỏi chấm: $10 - ? = 7$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Ô 10
  \draw[fill=blue!15, draw=blue!85!black, line width=1.3pt, rounded corners=5pt] (-3.0,-0.55) rectangle (-1.8,0.55);
  \node[font=\Large\bfseries\color{blue!90!black}] at (-2.4,0) {10};
  
  % Mũi tên trừ ?
  \draw[->, >=stealth, line width=1.4pt, red!85!black] (-1.7,0) -- (-0.3,0);
  \node[above=2pt, font=\small\bfseries\color{red!85!black}] at (-1.0,0.1) {$- \ ?$};
  
  % Ô 7
  \draw[fill=green!20, draw=green!80!black, line width=1.3pt, rounded corners=5pt] (-0.2,-0.55) rectangle (1.0,0.55);
  \node[font=\Large\bfseries\color{green!70!black}] at (0.4,0) {7};
\end{tikzpicture}
\end{center}
\shortans{3}
\loigiai{
\textbf{Đáp số:} $3$\\
$10 - 7 = 3$.
}
\end{ex}

% --- CÂU 19 ---
\begin{ex} %[1D3V11]
Trên bờ ao có 9 chú ếch, có 5 chú ếch nhảy tõm xuống ao như hình vẽ. Hỏi trên bờ ao còn lại bao nhiêu chú ếch?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Bờ ao (4 chú ếch ở lại)
  \draw[fill=green!20, draw=green!70!black, line width=1.2pt, rounded corners=8pt] (-4.2,-1.05) rectangle (-0.2,1.05);
  \VeChuEch{-3.4}{0.4}
  \VeChuEch{-2.2}{0.4}
  \VeChuEch{-3.2}{-0.4}
  \VeChuEch{-2.0}{-0.4}
  \node[below=3pt, font=\small\bfseries\color{green!70!black}] at (-2.2,-0.75) {Còn lại trên bờ: ? chú};
  
  % Mũi tên nhảy xuống ao
  \draw[->, >=stealth, line width=1.5pt, blue!85!black] (0.1,0) to[out=30,in=150] (1.1,0);
  
  % Làn nước ao (5 chú ếch đã nhảy xuống)
  \draw[fill=cyan!15, draw=blue!70!black, line width=1.2pt, rounded corners=8pt] (1.3,-1.05) rectangle (4.5,1.05);
  \VeChuEch{2.1}{0.4}
  \VeChuEch{3.3}{0.4}
  \VeChuEch{2.1}{-0.4}
  \VeChuEch{3.3}{-0.4}
  \VeChuEch{2.7}{0}
  \node[below=3pt, font=\small\bfseries\color{blue!90!black}] at (2.9,-0.75) {Nhảy xuống ao: 5 chú};
\end{tikzpicture}
\end{center}
\shortans{4}
\loigiai{
\textbf{Đáp số:} $4$\\
$9 - 5 = 4$ chú ếch.
}
\end{ex}

% --- CÂU 20 ---
\begin{ex} %[1D3C11]
Tính nhanh kết quả của biểu thức: $10 - 3 - 7$.
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=yellow!25, draw=orange!90!black, line width=1.3pt, rounded corners=6pt] (-3.5,-0.6) rectangle (3.5,0.6);
  \node[font=\Large\bfseries\color{red!85!black}] at (0,0) {$10 - 3 - 7 = ?$};
  \node[below=4pt, font=\small\bfseries\color{blue!85!black}] at (0,-0.65) {Gợi ý: $3 + 7 = 10$};
\end{tikzpicture}
\end{center}
\shortans{0}
\loigiai{
\textbf{Đáp số:} $0$\\
$10 - (3 + 7) = 10 - 10 = 0$.
}
\end{ex}
'''

# 1. Ghi nội dung vào file bài học
lesson_file = r'CHỦ ĐỀ 3 - PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10/Chuong3_Bai11_PhepTruTrongPhamVi10.tex'
with open(lesson_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Wrote {lesson_file} successfully')

# 2. Lắp ráp file test độc lập theo mẫu chuẩn Bai_01_preview.tex
with open('Bai_01_preview.tex', 'r', encoding='utf-8') as f:
    t1 = f.read()

t1 = t1.replace('BÀI 01: CÁC SỐ 0, 1, 2, 3, 4, 5', 'BÀI 11: PHÉP TRỪ TRONG PHẠM VI 10')
t1 = t1.replace('CHỦ ĐỀ 1 -- CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 3 -- PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10')
t1 = t1.replace('bai-01', 'bai-11')
t1 = t1.replace('Chuong1_Bai01_CacSo0_1_2_3_4_5.tex', 'Chuong3_Bai11_PhepTruTrongPhamVi10.tex')
t1 = t1.replace('CHỦ ĐỀ 1 - CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 3 - PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10')

test_file = 'test_bai11.tex'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(t1)
print(f'Created {test_file} successfully')
