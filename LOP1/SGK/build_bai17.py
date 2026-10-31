# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 17: ÔN TẬP CÁC SỐ TRONG PHẠM VI 10 (TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN CHO BÀI 17 ---

\providecommand{\VeTao}[3][red]{% #1=màu quả, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.45]
    \shadedraw[left color=#1!80!black, right color=orange!80!yellow, draw=red!90!black, line width=0.8pt]
      (-0.35,0.1) .. controls (-0.5,0.7) and (-0.1,0.9) .. (0,0.65)
      .. controls (0.1,0.9) and (0.5,0.7) .. (0.35,0.1)
      .. controls (0.3,-0.5) and (-0.3,-0.5) .. (-0.35,0.1);
    \draw[brown!70!black, line width=1.5pt] (0,0.65) .. controls (0.05,0.85) .. (0.15,1.0);
    \fill[green!70!black] (0.08,0.82) .. controls (0.3,0.95) and (0.35,0.75) .. (0.1,0.75) -- cycle;
  \end{scope}
}

\providecommand{\VeBongBay}[3][orange]{% #1=màu bóng, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.45]
    \shadedraw[ball color=#1, draw=black!60, line width=0.6pt] (0,0.4) circle (0.42cm);
    \fill[black!25!#1] (-0.05,-0.04) -- (0.05,-0.04) -- (0,-0.12) -- cycle;
    \draw[gray!80, line width=0.7pt] (0,-0.12) .. controls (-0.08,-0.4) and (0.08,-0.6) .. (0,-0.85);
  \end{scope}
}

\providecommand{\VeToaTau}[4][blue!60]{% #1=màu toa, #2=x, #3=y, #4=số
  \begin{scope}[shift={(#2,#3)}, scale=0.6]
    \draw[fill=#1, draw=black!80, rounded corners=2pt, line width=1pt] (0,0) rectangle (1.2,0.8);
    \draw[fill=white, draw=black!60] (0.2,0.2) rectangle (1.0,0.65);
    \node at (0.6, 0.42) {\bfseries\large #4};
    \fill[black!70] (0.25,-0.1) circle (0.15cm);
    \fill[gray!30] (0.25,-0.1) circle (0.07cm);
    \fill[black!70] (0.95,-0.1) circle (0.15cm);
    \fill[gray!30] (0.95,-0.1) circle (0.07cm);
    \draw[line width=1.5pt, black!70] (-0.15,0.2) -- (0,0.2);
  \end{scope}
}

\providecommand{\VeDauTau}[3]{% #1=x, #2=y, #3=số/chữ
  \begin{scope}[shift={(#1,#2)}, scale=0.6]
    \draw[fill=red!70, draw=black!80, rounded corners=2pt, line width=1pt] (0,0) rectangle (1.3,0.85);
    \draw[fill=yellow!80, draw=black!80] (0.8,0.85) rectangle (1.25,1.25);
    \draw[fill=black!70] (0.2,0.85) rectangle (0.4,1.1);
    \draw[fill=white, draw=black!60] (0.15,0.25) rectangle (0.65,0.7);
    \node at (0.4, 0.47) {\bfseries\footnotesize #3};
    \fill[black!70] (0.3,-0.1) circle (0.16cm);
    \fill[gray!30] (0.3,-0.1) circle (0.08cm);
    \fill[black!70] (1.0,-0.1) circle (0.16cm);
    \fill[gray!30] (1.0,-0.1) circle (0.08cm);
  \end{scope}
}

\providecommand{\VeKeo}[3][magenta]{% #1=màu, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.42]
    \draw[fill=#1!60!white, draw=purple!80, line width=0.8pt] (0,0) circle (0.32cm);
    \draw[fill=#1!40!white, draw=purple!80, line width=0.6pt] (-0.3,0) -- (-0.55,0.2) -- (-0.55,-0.2) -- cycle;
    \draw[fill=#1!40!white, draw=purple!80, line width=0.6pt] (0.3,0) -- (0.55,0.2) -- (0.55,-0.2) -- cycle;
    \draw[white, line width=1pt] (-0.1,0.1) arc (120:60:0.2cm);
  \end{scope}
}

\providecommand{\VeCaRot}[3]{% #1=x, #2=y, #3=scale
  \begin{scope}[shift={(#1,#2)}, scale=#3]
    \shadedraw[left color=orange!90!black, right color=yellow!80!orange, draw=orange!95!black, line width=0.7pt]
      (0,0.7) .. controls (0.22,0.65) and (0.15,-0.4) .. (0,-0.65)
      .. controls (-0.15,-0.4) and (-0.22,0.65) .. (0,0.7);
    \draw[line width=0.5pt, brown!70!black] (-0.08,0.3) -- (0.08,0.3);
    \draw[line width=0.5pt, brown!70!black] (-0.06,-0.1) -- (0.06,-0.1);
    \fill[green!70!black] (-0.05,0.7) .. controls (-0.15,1.0) .. (-0.02,0.9) -- cycle;
    \fill[green!75!black] (0,0.7) .. controls (0,1.1) .. (0.06,0.95) -- cycle;
    \fill[green!70!black] (0.05,0.7) .. controls (0.15,1.0) .. (0.02,0.9) -- cycle;
  \end{scope}
}

% =========================================================================
% PHẦN 1: TRẮC NGHIỆM LỰA CHỌN (12 CÂU) - ĐÁP ÁN ĐÚNG LUÔN LÀ B
% =========================================================================
\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- CÂU 1 ---
\begin{ex} %[1D5N17]
Đoàn tàu chở các toa số từ $5$ đến $8$. Số ở toa liền sau của toa mang số $7$ là số nào?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \VeDauTau{0}{0}{ĐẦU}
  \VeToaTau[teal!40]{1.5}{0}{5}
  \VeToaTau[cyan!40]{2.7}{0}{6}
  \VeToaTau[yellow!60!orange]{3.9}{0}{7}
  \VeToaTau[red!35]{5.1}{0}{?}
\end{tikzpicture}
\end{center}
\choice
{$6$}
{\True $8$}
{$9$}
{$10$}
\loigiai{
Toa liền sau toa số $7$ là toa mang số $8$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 2 ---
\begin{ex} %[1D5N17]
Trên cành cây có các quả táo đánh số thứ tự giảm dần từ $10$. Quả táo liền trước quả số $10$ ghi số nào?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \draw[line width=3.5pt, brown!70!black] (0,0.5) .. controls (3,0.8) and (5,0.3) .. (7,0.6);
  \VeTao[red]{1.5}{0.3} \node[white, font=\bfseries] at (1.5,0.2) {?};
  \VeTao[red]{3.5}{0.45} \node[white, font=\bfseries] at (3.5,0.35) {10};
  \node[font=\footnotesize\itshape, text=brown!80!black] at (3.5,-0.6) {(Số liền trước của 10 là ?)};
\end{tikzpicture}
\end{center}
\choice
{$8$}
{\True $9$}
{$7$}
{$6$}
\loigiai{
Số liền trước của số $10$ là số $9$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 3 ---
\begin{ex} %[1D5H17]
So sánh số lượng quả bóng màu cam và quả bóng màu xanh dưới đây. Dấu so sánh thích hợp điền vào ô trống là dấu nào?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \node[font=\bfseries] at (1.8, 1.2) {8 quả bóng cam};
  \foreach \i in {0,...,7}{
    \VeBongBay[orange]{\i*0.5}{0.3}
  }
  \node[draw, rounded corners=3pt, line width=1.2pt, fill=yellow!20, minimum width=0.9cm, minimum height=0.7cm, font=\bfseries\Large] at (4.7, 0.3) {?};
  \node[font=\bfseries] at (7.3, 1.2) {6 quả bóng xanh};
  \foreach \i in {0,...,5}{
    \VeBongBay[teal]{6.0+\i*0.5}{0.3}
  }
\end{tikzpicture}
\end{center}
\choice
{$<$}
{\True $>$}
{$=$}
{$+$}
\loigiai{
Có $8$ quả bóng cam và $6$ quả bóng xanh. Vì $8 > 6$ nên dấu cần điền là $>$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 4 ---
\begin{ex} %[1D5H17]
Sơ đồ tách gộp số $9$ gồm $5$ viên kẹo hồng và mấy viên kẹo xanh?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \node[draw=purple!80, circle, fill=pink!30, line width=1.2pt, font=\bfseries\Large, inner sep=5pt] (tong) at (3, 1.8) {9};
  \node[draw=blue!70, rounded corners=4pt, fill=blue!10, line width=1pt, inner sep=4pt] (nhanh1) at (1.2, 0) {
    \begin{tikzpicture}[scale=0.7]
      \foreach \i in {0,...,4}{ \VeKeo[magenta]{\i*0.6}{0} }
      \node[below, font=\bfseries] at (1.2, -0.4) {5 viên};
    \end{tikzpicture}
  };
  \node[draw=green!70!black, rounded corners=4pt, fill=green!10, line width=1pt, inner sep=4pt] (nhanh2) at (4.8, 0) {
    \begin{tikzpicture}[scale=0.7]
      \node[font=\bfseries\Large, text=green!60!black] at (0,0) {? viên};
    \end{tikzpicture}
  };
  \draw[->, >=stealth, line width=1.3pt, purple!80] (tong) -- (nhanh1);
  \draw[->, >=stealth, line width=1.3pt, purple!80] (tong) -- (nhanh2);
\end{tikzpicture}
\end{center}
\choice
{$3$}
{\True $4$}
{$5$}
{$2$}
\loigiai{
Ta có $9$ gồm $5$ và $4$ (vì $5 + 4 = 9$).\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage

% --- CÂU 5 ---
\begin{ex} %[1D5H17]
Trong các số được ghi trên các bông hoa dưới đây, bông hoa nào ghi số \textbf{lớn nhất}?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \foreach \x/\val/\col in {0/4/pink, 2/9/yellow, 4/2/cyan, 6/7/orange, 8/10/red}{
    \begin{scope}[shift={(\x, 0)}]
      \foreach \a in {0,60,...,300}{
        \fill[\col!70] (\a:0.45) circle (0.25cm);
      }
      \fill[white] (0,0) circle (0.35cm);
      \draw[line width=1pt, black!70] (0,0) circle (0.35cm);
      \node[font=\bfseries\large] at (0,0) {\val};
      \draw[line width=2pt, green!60!black] (0,-0.35) -- (0,-1.0);
    \end{scope}
  }
\end{tikzpicture}
\end{center}
\choice
{$9$}
{\True $10$}
{$7$}
{$4$}
\loigiai{
So sánh các số $4, 9, 2, 7, 10$, số lớn nhất là $10$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 6 ---
\begin{ex} %[1D5H17]
Trong các chiếc lá dưới đây, chiếc lá nào ghi số \textbf{bé nhất}?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \foreach \x/\val in {0/6, 2/1, 4/8, 6/3, 8/5}{
    \begin{scope}[shift={(\x, 0)}]
      \draw[fill=green!40!lime, draw=green!60!black, line width=1pt, rounded corners=8pt]
        (-0.6,0) .. controls (-0.5,0.7) and (0.5,0.7) .. (0.6,0)
        .. controls (0.5,-0.7) and (-0.5,-0.7) .. (-0.6,0);
      \draw[green!60!black, line width=0.8pt] (-0.5,0) -- (0.5,0);
      \node[draw=black!70, circle, fill=white, inner sep=2pt, font=\bfseries] at (0,0) {\val};
    \end{scope}
  }
\end{tikzpicture}
\end{center}
\choice
{$3$}
{\True $1$}
{$5$}
{$6$}
\loigiai{
Trong các số $6, 1, 8, 3, 5$, số bé nhất là $1$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 7 ---
\begin{ex} %[1D5V17]
Bốn chú chim mang các tấm thẻ số $7, 2, 9, 4$. Sắp xếp các số theo thứ tự từ \textbf{bé đến lớn} là:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \foreach \x/\val/\c in {0/7/yellow!35, 2.5/2/cyan!30, 5/9/pink!40, 7.5/4/green!30}{
    \begin{scope}[shift={(\x, 0)}]
      \draw[fill=\c, draw=black!70, line width=1.1pt, rounded corners=4pt] (0,0) rectangle (1.4,1.1);
      \node[font=\bfseries\LARGE] at (0.7,0.55) {\val};
    \end{scope}
  }
\end{tikzpicture}
\end{center}
\choice
{$9, 7, 4, 2$}
{\True $2, 4, 7, 9$}
{$2, 7, 4, 9$}
{$4, 2, 7, 9$}
\loigiai{
So sánh: $2 < 4 < 7 < 9$. Thứ tự từ bé đến lớn là $2, 4, 7, 9$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 8 ---
\begin{ex} %[1D5V17]
Bác nông dân thu hoạch $4$ giỏ cà rốt ghi các số $3, 10, 6, 8$. Sắp xếp các số theo thứ tự từ \textbf{lớn đến bé} là:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \foreach \x/\val in {0/3, 2.3/10, 4.6/6, 6.9/8}{
    \begin{scope}[shift={(\x, 0)}]
      \draw[fill=orange!35!yellow, draw=brown!80!black, line width=1.2pt] (0,0) -- (0.2,-0.7) -- (1.0,-0.7) -- (1.2,0) -- cycle;
      \draw[brown!80!black, line width=1pt] (0.1,0) arc (180:0:0.5cm);
      \node[font=\bfseries\large, text=brown!90!black] at (0.6,-0.38) {\val};
      \VeCaRot{0.6}{0.2}{0.3}
    \end{scope}
  }
\end{tikzpicture}
\end{center}
\choice
{$3, 6, 8, 10$}
{\True $10, 8, 6, 3$}
{$10, 6, 8, 3$}
{$8, 10, 6, 3$}
\loigiai{
So sánh: $10 > 8 > 6 > 3$. Thứ tự từ lớn đến bé là $10, 8, 6, 3$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage

% --- CÂU 9 ---
\begin{ex} %[1D5V17]
Trên tia số dưới đây, hai ô vuông còn thiếu lần lượt là những số nào?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \draw[->, >=stealth, line width=1.3pt] (0,0) -- (8.5,0);
  \foreach \x in {0,1,...,8}{
    \draw[line width=1.1pt] (\x, 0.15) -- (\x, -0.15);
  }
  \node[below] at (0,-0.2) {$0$};
  \node[below] at (1,-0.2) {$1$};
  \node[below] at (2,-0.2) {$2$};
  \node[draw=red, fill=yellow!20, rounded corners=2pt, line width=1pt, minimum size=0.45cm] at (3, -0.45) {\bfseries ?};
  \node[below] at (4,-0.2) {$4$};
  \node[below] at (5,-0.2) {$5$};
  \node[draw=red, fill=yellow!20, rounded corners=2pt, line width=1pt, minimum size=0.45cm] at (6, -0.45) {\bfseries ?};
  \node[below] at (7,-0.2) {$7$};
  \node[below] at (8,-0.2) {$8$};
\end{tikzpicture}
\end{center}
\choice
{$2$ và $5$}
{\True $3$ và $6$}
{$3$ và $5$}
{$4$ và $7$}
\loigiai{
Đếm xuôi trên tia số: $0, 1, 2, \mathbf{3}, 4, 5, \mathbf{6}, 7, 8$. Hai số còn thiếu là $3$ và $6$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 10 ---
\begin{ex} %[1D5V17]
Có tất cả bao nhiêu quả táo màu đỏ trong khung dưới đây?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \draw[draw=blue!60, fill=blue!5, rounded corners=6pt, line width=1.2pt] (-0.5,-0.5) rectangle (6.5,1.7);
  \foreach \i in {0,...,4}{ \VeTao[red]{\i*1.3+0.2}{1.0} }
  \foreach \i in {0,...,3}{ \VeTao[red]{\i*1.3+0.8}{0.1} }
\end{tikzpicture}
\end{center}
\choice
{$8$ quả}
{\True $9$ quả}
{$10$ quả}
{$7$ quả}
\loigiai{
Hàng trên có $5$ quả, hàng dưới có $4$ quả. Tất cả có: $5 + 4 = 9$ quả táo.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 11 ---
\begin{ex} %[1D5V17]
So sánh số viên kẹo trong hai hộp. Khẳng định nào sau đây là \textbf{đúng}?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \draw[draw=purple!70, fill=purple!5, rounded corners=4pt, line width=1.1pt] (0,0) rectangle (2.8,1.8);
  \node[font=\bfseries, text=purple!80!black] at (1.4,1.5) {Hộp A};
  \VeKeo[magenta]{0.6}{0.9} \VeKeo[magenta]{1.4}{0.9} \VeKeo[magenta]{2.2}{0.9}
  \VeKeo[magenta]{0.6}{0.4} \VeKeo[magenta]{1.4}{0.4} \VeKeo[magenta]{2.2}{0.4}
  \VeKeo[magenta]{1.4}{-0.1}
  
  \begin{scope}[shift={(4.5,0)}]
    \draw[draw=teal!70, fill=teal!5, rounded corners=4pt, line width=1.1pt] (0,0) rectangle (2.8,1.8);
    \node[font=\bfseries, text=teal!80!black] at (1.4,1.5) {Hộp B};
    \VeKeo[cyan]{0.7}{0.9} \VeKeo[cyan]{1.4}{0.9} \VeKeo[cyan]{2.1}{0.9}
    \VeKeo[cyan]{0.7}{0.4} \VeKeo[cyan]{2.1}{0.4}
  \end{scope}
\end{tikzpicture}
\end{center}
\choice
{Hộp A có ít kẹo hơn Hộp B}
{\True Hộp A có nhiều kẹo hơn Hộp B}
{Hai hộp có số kẹo bằng nhau}
{Hộp B có 7 viên kẹo}
\loigiai{
Hộp A có $7$ viên kẹo, Hộp B có $5$ viên kẹo. Vì $7 > 5$ nên Hộp A có nhiều kẹo hơn Hộp B.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 12 ---
\begin{ex} %[1D5V17]
Điền số thích hợp vào ô trống: Số lớn hơn $7$ và nhỏ hơn $9$ là số nào?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \node[draw=blue!70, fill=blue!10, rounded corners=3pt, font=\bfseries\Large, minimum size=0.8cm] at (0,0) {7};
  \node[font=\bfseries\Large] at (1,0) {$<$};
  \node[draw=red!80, fill=yellow!30, rounded corners=3pt, line width=1.2pt, font=\bfseries\Large, minimum size=0.8cm] at (2,0) {?};
  \node[font=\bfseries\Large] at (3,0) {$<$};
  \node[draw=blue!70, fill=blue!10, rounded corners=3pt, font=\bfseries\Large, minimum size=0.8cm] at (4,0) {9};
\end{tikzpicture}
\end{center}
\choice
{$6$}
{\True $8$}
{$10$}
{$7$}
\loigiai{
Số tự nhiên ở giữa $7$ và $9$ là $8$, vì $7 < 8 < 9$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage

% =========================================================================
% PHẦN 2: CÂU ĐÚNG / SAI (2 CÂU, MỖI CÂU 4 Ý)
% =========================================================================
\textbf{Phần 2. Câu trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% --- CÂU 13 ---
\begin{ex} %[1D5H17]
Quan sát hình vẽ các giỏ trái cây của bạn Lan:
\begin{center}
\begin{tikzpicture}[scale=0.78, baseline=(current bounding box.center)]
  % Giỏ dâu
  \draw[fill=pink!20, draw=purple!60, rounded corners=4pt, line width=1pt] (-0.2,-0.6) rectangle (3.2,1.6);
  \node[font=\bfseries\footnotesize, text=red!80!black] at (1.5,1.25) {Giỏ A: 6 quả};
  \foreach \i in {0,...,5}{ \VeTao[red]{0.3+\i*0.48}{0.3} }
  
  % Giỏ cam
  \draw[fill=orange!15, draw=orange!70, rounded corners=4pt, line width=1pt] (4.2,-0.6) rectangle (7.8,1.6);
  \node[font=\bfseries\footnotesize, text=orange!90!black] at (6.0,1.25) {Giỏ B: 8 quả};
  \foreach \i in {0,...,7}{ \VeBongBay[orange]{4.5+\i*0.42}{0.2} }
  
  % Giỏ táo
  \draw[fill=green!15, draw=green!70!black, rounded corners=4pt, line width=1pt] (8.8,-0.6) rectangle (12.2,1.6);
  \node[font=\bfseries\footnotesize, text=green!70!black] at (10.5,1.25) {Giỏ C: 10 quả};
  \foreach \i in {0,...,4}{ \VeTao[green]{9.1+\i*0.6}{0.55} }
  \foreach \i in {0,...,4}{ \VeTao[green]{9.1+\i*0.6}{-0.1} }
\end{tikzpicture}
\end{center}
Xét tính Đúng hay Sai của các khẳng định sau:
\choiceTF
{\True Số quả ở giỏ B nhiều hơn số quả ở giỏ A}
{Số quả ở giỏ C ít hơn số quả ở giỏ B}
{\True Giỏ C có nhiều quả nhất trong ba giỏ}
{Sắp xếp số quả theo thứ tự từ lớn đến bé là: Giỏ A, Giỏ B, Giỏ C}
\loigiai{
Số quả ở các giỏ là: A có $6$, B có $8$, C có $10$.\\
a) Vì $8 > 6$ nên giỏ B nhiều hơn giỏ A là \textbf{Đúng}.\\
b) Giỏ C ($10$) nhiều hơn giỏ B ($8$), nên phát biểu ít hơn là \textbf{Sai}.\\
c) Vì $10$ lớn nhất nên giỏ C có nhiều quả nhất là \textbf{Đúng}.\\
d) Thứ tự từ lớn đến bé là Giỏ C ($10$), Giỏ B ($8$), Giỏ A ($6$), do đó phát biểu d là \textbf{Sai}.
}
\end{ex}

% --- CÂU 14 ---
\begin{ex} %[1D5V17]
Cho dãy số trên các bậc thang đi lên từ dưới đất lên đỉnh đồi:
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \foreach \i/\val in {0/1, 1/3, 2/5, 3/7, 4/9}{
    \draw[fill=yellow!30, draw=orange!80, line width=1pt] (\i*1.5, \i*0.7) rectangle (\i*1.5+1.5, \i*0.7+0.7);
    \node[font=\bfseries\Large] at (\i*1.5+0.75, \i*0.7+0.35) {\val};
  }
  \node[font=\bfseries, text=red!80!black] at (3.5, 4.2) {Dãy số trên các bậc thang};
\end{tikzpicture}
\end{center}
Xét tính Đúng hay Sai của các khẳng định sau:
\choiceTF
{\True Dãy số trên được sắp xếp theo thứ tự tăng dần}
{Số ở bậc thang cao nhất là số 10}
{\True Giữa số 3 và số 7 có số 5}
{Nếu thêm một bậc thang tiếp theo có cùng quy luật thì số ghi trên đó là 10}
\loigiai{
Dãy số: $1, 3, 5, 7, 9$.\\
a) Dãy số tăng dần: $1 < 3 < 5 < 7 < 9$ $\to$ \textbf{Đúng}.\\
b) Số ở bậc cao nhất là $9$ chứ không phải $10$ $\to$ \textbf{Sai}.\\
c) Giữa $3$ và $7$ có số $5$ $\to$ \textbf{Đúng}.\\
d) Dãy số cách đều $2$ đơn vị ($1, 3, 5, 7, 9$), nên số tiếp theo phải là $11$ (không phải $10$) $\to$ \textbf{Sai}.
}
\end{ex}

\newpage

% =========================================================================
% PHẦN 3: CÂU TRẢ LỜI NGẮN (6 CÂU)
% =========================================================================
\textbf{Phần 3. Câu trắc nghiệm trả lời ngắn}
\setcounterpageref{ex}{0}

% --- CÂU 15 ---
\begin{ex} %[1D5H17]
Quan sát chùm bóng bay dưới đây. Hỏi có tất cả bao nhiêu quả bóng bay?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \VeBongBay[red]{0}{0.8}
  \VeBongBay[blue]{0.6}{1.2}
  \VeBongBay[green]{1.2}{0.9}
  \VeBongBay[orange]{1.8}{1.3}
  \VeBongBay[purple]{2.4}{0.8}
  \VeBongBay[cyan]{0.3}{0.2}
  \VeBongBay[yellow]{1.5}{0.3}
  \draw[gray!70, line width=1pt] (0.2,-0.6) -- (1.2,-1.3);
  \draw[gray!70, line width=1pt] (1.2,-0.4) -- (1.2,-1.3);
  \draw[gray!70, line width=1pt] (2.2,-0.6) -- (1.2,-1.3);
  \fill[brown!80!black] (1.1,-1.4) rectangle (1.3,-1.2);
\end{tikzpicture}
\end{center}
\textbf{Trả lời:} \raisebox{-2pt}{\framebox[1.5cm]{\phantom{1}}}
\loigiai{
Đếm số quả bóng bay: $1, 2, 3, 4, 5, 6, 7$ quả bóng.\\
\textbf{Đáp số:} 7
}
\end{ex}

% --- CÂU 16 ---
\begin{ex} %[1D5H17]
Điền số thích hợp vào dấu hỏi chấm: Số $8$ gồm $3$ và mấy?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \node[circle, draw=orange!80, fill=yellow!30, line width=1.3pt, font=\bfseries\Large, inner sep=6pt] (root) at (2,1.5) {8};
  \node[circle, draw=blue!70, fill=blue!15, line width=1.1pt, font=\bfseries\large, inner sep=5pt] (left) at (0.7,0) {3};
  \node[circle, draw=red!70, fill=red!15, line width=1.2pt, font=\bfseries\Large, inner sep=5pt] (right) at (3.3,0) {?};
  \draw[->, >=stealth, line width=1.2pt, gray!80] (root) -- (left);
  \draw[->, >=stealth, line width=1.2pt, gray!80] (root) -- (right);
\end{tikzpicture}
\end{center}
\textbf{Trả lời:} \raisebox{-2pt}{\framebox[1.5cm]{\phantom{1}}}
\loigiai{
Số $8$ gồm $3$ và $5$ (vì $3 + 5 = 8$).\\
\textbf{Đáp số:} 5
}
\end{ex}

% --- CÂU 17 ---
\begin{ex} %[1D5V17]
Trên bàn có $10$ củ cà rốt, chú thỏ đã ăn mất $4$ củ. Hỏi trên bàn còn lại bao nhiêu củ cà rốt?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \foreach \i in {0,...,5}{
    \VeCaRot{\i*1.1}{0}{0.4}
  }
  \foreach \i in {0,...,3}{
    \begin{scope}[shift={(7+\i*1.1, 0)}]
      \VeCaRot{0}{0}{0.4}
      \draw[line width=1.8pt, red!85!black] (-0.3,-0.3) -- (0.3,0.3);
      \draw[line width=1.8pt, red!85!black] (-0.3,0.3) -- (0.3,-0.3);
    \end{scope}
  }
  \node[font=\footnotesize\itshape, text=blue!80!black] at (3, -0.9) {Còn lại};
  \node[font=\footnotesize\itshape, text=red!80!black] at (8.5, -0.9) {Đã ăn ($4$ củ)};
\end{tikzpicture}
\end{center}
\textbf{Trả lời:} \raisebox{-2pt}{\framebox[1.5cm]{\phantom{1}}}
\loigiai{
Số củ cà rốt còn lại là: $10 - 4 = 6$ (củ).\\
\textbf{Đáp số:} 6
}
\end{ex}

% --- CÂU 18 ---
\begin{ex} %[1D5V17]
Cho các số: $2, 8, 5, 0, 9$. Hỏi có bao nhiêu số \textbf{lớn hơn 4}?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \foreach \x/\val in {0/2, 1.6/8, 3.2/5, 4.8/0, 6.4/9}{
    \draw[fill=teal!20, draw=teal!70, rounded corners=4pt, line width=1.1pt] (\x,0) rectangle (\x+1.1,0.9);
    \node[font=\bfseries\Large] at (\x+0.55,0.45) {\val};
  }
\end{tikzpicture}
\end{center}
\textbf{Trả lời:} \raisebox{-2pt}{\framebox[1.5cm]{\phantom{1}}}
\loigiai{
Các số lớn hơn $4$ là: $8, 5, 9$. Có tất cả $3$ số.\\
\textbf{Đáp số:} 3
}
\end{ex}

% --- CÂU 19 ---
\begin{ex} %[1D5V17]
Hình dưới đây có bao nhiêu chấm tròn màu xanh?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \draw[draw=blue!70, fill=blue!5, rounded corners=5pt, line width=1.1pt] (0,0) rectangle (5.5,2.4);
  \foreach \row in {0.5, 1.2, 1.9}{
    \foreach \col in {0.7, 1.8, 2.9, 4.0, 4.9}{
      \fill[blue!70!cyan] (\col, \row) circle (0.22cm);
      \fill[white] (\col-0.06, \row+0.06) circle (0.06cm);
    }
  }
  % Xoá 5 chấm để còn lại 10 chấm
  \fill[blue!5] (4.0, 1.9) circle (0.26cm);
  \fill[blue!5] (4.9, 1.9) circle (0.26cm);
  \fill[blue!5] (2.9, 1.2) circle (0.26cm);
  \fill[blue!5] (4.0, 1.2) circle (0.26cm);
  \fill[blue!5] (4.9, 1.2) circle (0.26cm);
\end{tikzpicture}
\end{center}
\textbf{Trả lời:} \raisebox{-2pt}{\framebox[1.5cm]{\phantom{1}}}
\loigiai{
Hàng dưới có $5$ chấm, hàng giữa có $2$ chấm, hàng trên có $3$ chấm. Tổng cộng: $5 + 2 + 3 = 10$ chấm tròn.\\
\textbf{Đáp số:} 10
}
\end{ex}

% --- CÂU 20 ---
\begin{ex} %[1D5V17]
Tìm số thích hợp điền vào ô trống cuối cùng của toa tàu:
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeToaTau[teal!45]{0}{0}{2}
  \VeToaTau[teal!45]{1.4}{0}{4}
  \VeToaTau[teal!45]{2.8}{0}{6}
  \VeToaTau[teal!45]{4.2}{0}{8}
  \VeToaTau[yellow!60!orange]{5.6}{0}{?}
\end{tikzpicture}
\end{center}
\textbf{Trả lời:} \raisebox{-2pt}{\framebox[1.5cm]{\phantom{1}}}
\loigiai{
Quy luật dãy số cách đều $2$: $2, 4, 6, 8, 10$. Số cần điền là $10$.\\
\textbf{Đáp số:} 10
}
\end{ex}
'''

tex_path = r'd:\GitHub\quanlytrungtamthaylinh-main\1.SACH\LOP1\SGK\CHỦ ĐỀ 5 - ÔN TẬP HỌC KÌ 1\Chuong5_Bai17_OnTapCacSoTrongPhamVi10.tex'
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Chuong5_Bai17 successfully.")

# Tạo preview tex và biên dịch
preview_tex = r'''\documentclass[14pt,a4paper,oneside]{extbook}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb,mathrsfs,fancyhdr,enumerate,multirow,makecell}
\usepackage{tikz}
\usetikzlibrary{arrows,calc,intersections,angles,quotes,backgrounds,shapes.geometric,patterns}
\usepackage[top=1.8cm, bottom=1.8cm, left=1.8cm, right=1.8cm, headheight=16pt]{geometry}
\usepackage[hidelinks,unicode]{hyperref}
\usepackage{qrcode}
\usepackage{fontawesome}
\usepackage[many]{tcolorbox}
\usepackage[dethi]{ex_test}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape\color{gray} Tuyển tập Đề kiểm tra Toán 1 theo từng bài}
\fancyhead[R]{\small\bfseries\color{blue!80!black} Lớp Toán Thầy Lĩnh -- loptoanthaylinh.vn}
\fancyfoot[C]{\bfseries\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\newcommand{\TaoPhieuKiemTra}[4]{%
  \noindent
  \begin{tcolorbox}[
    colback=white,
    colframe=blue!85!black,
    arc=2.5mm,
    boxrule=1pt,
    left=2.5mm, right=2.5mm, top=1.8mm, bottom=1.8mm
  ]
    \begin{minipage}[c]{0.27\textwidth}
      \centering
      \begin{tcolorbox}[colback=blue!8, colframe=blue!80!black, boxrule=0.6pt, arc=1.5mm, halign=center, top=1.2mm, bottom=1.2mm, left=1mm, right=1mm]
        {\bfseries\color{blue!95!black}\small LỚP TOÁN THẦY LĨNH}\\[1.5pt]
        {\scriptsize\color{blue!70!black}\faGlobe~loptoanthaylinh.vn}\\[1.5pt]
        {\scriptsize\bfseries\color{blue!85!black}\faPhone~Hotline: 0866976878}
      \end{tcolorbox}
    \end{minipage}%
    \hfill
    \begin{minipage}[c]{0.56\textwidth}
      \centering
      {\footnotesize\bfseries\color{blue!80!black}\MakeUppercase{#1}}\\[2pt]
      {\large\bfseries\color{red!85!black}\MakeUppercase{BÀI #2: #3}}\\[2pt]
      {\scriptsize\itshape Thời gian làm bài: 35 phút -- Trực quan sinh động}
    \end{minipage}%
    \hfill
    \begin{minipage}[c]{0.14\textwidth}
      \centering
      \qrcode[height=1.35cm]{#4}\\[2pt]
      {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
    \end{minipage}
  \end{tcolorbox}
  \vspace{2mm}
}

\begin{document}
\TaoPhieuKiemTra{Chủ đề 5 -- Ôn tập học kì 1}{17}{Ôn tập các số trong phạm vi 10}{https://loptoanthaylinh.vn/thi-online/toan-1/bai-17}
\input{CHỦ ĐỀ 5 - ÔN TẬP HỌC KÌ 1/Chuong5_Bai17_OnTapCacSoTrongPhamVi10.tex}
\end{document}
'''

with open('Bai_17_preview.tex', 'w', encoding='utf-8') as f:
    f.write(preview_tex)

cmd = 'pdflatex -interaction=nonstopmode Bai_17_preview.tex'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print("pdflatex Bai 17 return code:", res.returncode)

if os.path.exists('Bai_17_preview.pdf'):
    import pypdf, shutil
    reader = pypdf.PdfReader('Bai_17_preview.pdf')
    print("Bai 17 Page count:", len(reader.pages))
    os.makedirs('PDF_DeThi_TungBai', exist_ok=True)
    dest = os.path.join('PDF_DeThi_TungBai', 'Bai_17_On_tap_cac_so_trong_pham_vi_10.pdf')
    shutil.copyfile('Bai_17_preview.pdf', dest)
    print(f"Copied to {dest} successfully!")
else:
    print("PDF generation failed!")
