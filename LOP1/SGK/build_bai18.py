# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 18: ÔN TẬP PHÉP CỘNG, PHÉP TRỪ TRONG PHẠM VI 10 (TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN CHO BÀI 18 ---

\providecommand{\VeChuVit}[3]{% #1=x, #2=y, #3=màu lông
  \begin{scope}[shift={(#1,#2)}, scale=0.42]
    \fill[#3] (0,0) ellipse (0.45cm and 0.3cm);
    \fill[#3] (0.28,0.25) circle (0.22cm);
    \fill[orange] (0.45,0.23) -- (0.68,0.21) -- (0.45,0.15) -- cycle;
    \fill[black] (0.33,0.3) circle (0.04cm);
    \fill[white] (0.32,0.32) circle (0.015cm);
    \draw[line width=0.8pt, black!30!#3] (-0.1,0.05) arc (140:220:0.25cm);
  \end{scope}
}

\providecommand{\VeBongBay}[3][orange]{% #1=màu bóng, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.42]
    \shadedraw[ball color=#1, draw=black!60, line width=0.6pt] (0,0.4) circle (0.4cm);
    \fill[black!25!#1] (-0.05,-0.04) -- (0.05,-0.04) -- (0,-0.12) -- cycle;
    \draw[gray!80, line width=0.7pt] (0,-0.12) .. controls (-0.08,-0.4) and (0.08,-0.6) .. (0,-0.8);
  \end{scope}
}

\providecommand{\VeChuCa}[3]{% #1=x, #2=y, #3=màu
  \begin{scope}[shift={(#1,#2)}, scale=0.4]
    \fill[#3] (0,0) ellipse (0.45cm and 0.25cm);
    \fill[#3] (-0.4,0) -- (-0.65,0.2) -- (-0.65,-0.2) -- cycle;
    \fill[white] (0.25,0.08) circle (0.06cm);
    \fill[black] (0.27,0.08) circle (0.035cm);
    \draw[line width=0.8pt, white] (-0.05,0.12) arc (60:-60:0.18cm);
  \end{scope}
}

\providecommand{\VeOTo}[3]{% #1=x, #2=y, #3=màu xe
  \begin{scope}[shift={(#1,#2)}, scale=0.45]
    \draw[fill=#3, draw=black!80, rounded corners=3pt, line width=0.8pt] (0,0) rectangle (1.5,0.6);
    \draw[fill=white!25!#3, draw=black!80, rounded corners=2pt] (0.3,0.6) -- (0.5,1.0) -- (1.1,1.0) -- (1.3,0.6) -- cycle;
    \draw[fill=cyan!30, draw=black!70] (0.52,0.68) rectangle (0.8,0.92);
    \draw[fill=cyan!30, draw=black!70] (0.86,0.68) rectangle (1.14,0.92);
    \fill[black!80] (0.3,-0.08) circle (0.16cm);
    \fill[gray!30] (0.3,-0.08) circle (0.07cm);
    \fill[black!80] (1.2,-0.08) circle (0.16cm);
    \fill[gray!30] (1.2,-0.08) circle (0.07cm);
  \end{scope}
}

% =========================================================================
% PHẦN 1: TRẮC NGHIỆM LỰA CHỌN (12 CÂU)
% =========================================================================
\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Đàn vịt 3 + 4 = 7
\begin{ex} %[1D5N18]
Dưới ao có $3$ chú vịt màu vàng và $4$ chú vịt màu trắng:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=cyan!15, draw=blue!40, rounded corners=6pt, line width=0.8pt] (-0.3,-0.5) rectangle (7.5,1.2);
  \node[font=\bfseries\footnotesize, text=blue!80!black] at (3.6,0.9) {$3 + 4 = ?$ chú vịt};
  \VeChuVit{0.5}{0.1}{yellow!90!orange}
  \VeChuVit{1.5}{0.25}{yellow!90!orange}
  \VeChuVit{2.5}{0.05}{yellow!90!orange}
  \node[font=\bfseries\large, text=blue!80!black] at (3.5,0.15) {$+$};
  \VeChuVit{4.4}{0.15}{white}
  \VeChuVit{5.3}{0.05}{white}
  \VeChuVit{6.2}{0.25}{white}
  \VeChuVit{7.1}{0.1}{white}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Có tất cả bao nhiêu chú vịt dưới ao?
\begin{multicols}{4}
\choice
{$6$}
{\True $7$}
{$8$}
{$9$}
\end{multicols}
\loigiai{
Phép tính: $3 + 4 = 7$ (chú vịt).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Bóng bay bay mất 8 - 5 = 3
\begin{ex} %[1D5N18]
Bạn An có $8$ quả bóng bay, bị gió thổi bay mất $5$ quả:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=orange!10, draw=orange!40, rounded corners=6pt, line width=0.8pt] (-0.2,-0.5) rectangle (6.8,1.3);
  \foreach \i in {0,...,2}{
    \VeBongBay[orange]{\i*0.8+0.4}{0.25}
  }
  \foreach \i in {0,...,4}{
    \begin{scope}[shift={(3.0+\i*0.75, 0.25)}]
      \VeBongBay[gray!50]{0}{0}
      \draw[line width=1.1pt, red!85] (-0.2,0.15) -- (0.2,0.65);
      \draw[line width=1.1pt, red!85] (-0.2,0.65) -- (0.2,0.15);
    \end{scope}
  }
  \node[below, font=\bfseries\tiny, color=blue!90!black] at (1.2,-0.1) {Còn lại: $?$ quả};
  \node[below, font=\bfseries\tiny, color=red!85] at (4.5,-0.1) {Bay mất $5$ quả};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Bạn An còn lại số quả bóng bay là:
\begin{multicols}{4}
\choice
{$2$}
{\True $3$}
{$4$}
{$5$}
\end{multicols}
\loigiai{
Số bóng còn lại là: $8 - 5 = 3$ (quả bóng).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Ô tô chở phép tính 6 + 2 = 8
\begin{ex} %[1D5N18]
Chiếc ô tô chở phép tính cộng:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeOTo{0}{0}{cyan!70!blue}
  \node[font=\bfseries\normalsize, text=red!85!black] at (0.75,0.75) {$6 + 2 = ?$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Kết quả của phép tính trên chiếc ô tô là:
\begin{multicols}{4}
\choice
{$7$}
{\True $8$}
{$9$}
{$10$}
\end{multicols}
\loigiai{
Ta có: $6 + 2 = 8$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Dâu tây ăn bớt 10 - 6 = 4
\begin{ex} %[1D5N18]
Đĩa có $10$ quả dâu tây, bạn Nam đã ăn $6$ quả:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[draw=pink!80, fill=pink!10, rounded corners=6pt, line width=0.8pt] (-0.2,-0.4) rectangle (7.0,1.2);
  \foreach \i in {0,...,3}{
    \fill[red!85!black] (\i*0.75+0.3, 0.4) circle (0.23cm);
    \fill[green!70!black] (\i*0.75+0.3, 0.65) rectangle (\i*0.75+0.34, 0.8);
  }
  \node[font=\bfseries\tiny, text=blue!80!black] at (1.4, -0.15) {Còn lại (? quả)};
  \foreach \i in {0,...,5}{
    \begin{scope}[shift={(3.2+\i*0.62, 0.4)}]
      \fill[gray!40] (0, 0) circle (0.23cm);
      \draw[line width=1.1pt, red!85] (-0.18,-0.18) -- (0.18,0.18);
      \draw[line width=1.1pt, red!85] (-0.18,0.18) -- (0.18,-0.18);
    \end{scope}
  }
  \node[font=\bfseries\tiny, text=red!80!black] at (4.8, -0.15) {Đã ăn ($6$ quả)};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Trên đĩa còn lại số quả dâu tây là:
\begin{multicols}{4}
\choice
{$3$}
{\True $4$}
{$5$}
{$6$}
\end{multicols}
\loigiai{
Phép tính: $10 - 6 = 4$ (quả dâu).\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Ba nhóm đồ vật 4 + 3 + 2 = 9
\begin{ex} %[1D5H18]
Tính giá trị biểu thức gồm ba nhóm đồ vật: $4 + 3 + 2 = ?$
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=yellow!20, draw=orange!70, rounded corners=3pt] (0,0) rectangle (1.7,1.0);
  \node at (0.85,0.65) {\bfseries\footnotesize 4 quả};
  \node[text=orange!80!black] at (0.85,0.25) {$\bullet\bullet\bullet\bullet$};
  \node[font=\bfseries\normalsize] at (2.0,0.5) {$+$};
  \draw[fill=yellow!20, draw=orange!70, rounded corners=3pt] (2.3,0) rectangle (3.8,1.0);
  \node at (3.05,0.65) {\bfseries\footnotesize 3 quả};
  \node[text=orange!80!black] at (3.05,0.25) {$\bullet\bullet\bullet$};
  \node[font=\bfseries\normalsize] at (4.1,0.5) {$+$};
  \draw[fill=yellow!20, draw=orange!70, rounded corners=3pt] (4.4,0) rectangle (5.7,1.0);
  \node at (5.05,0.65) {\bfseries\footnotesize 2 quả};
  \node[text=orange!80!black] at (5.05,0.25) {$\bullet\bullet$};
  \node[font=\bfseries\normalsize] at (6.0,0.5) {$=$};
  \node[draw=red!80, fill=red!10, rounded corners=3pt, font=\bfseries\normalsize, minimum size=0.6cm] at (6.6,0.5) {?};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Giá trị của biểu thức là:
\begin{multicols}{4}
\choice
{$8$}
{\True $9$}
{$10$}
{$7$}
\end{multicols}
\loigiai{
Tính từ trái sang phải: $4 + 3 = 7$, rồi $7 + 2 = 9$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Chim trên dây điện 9 - 4 - 3 = 2
\begin{ex} %[1D5H18]
Lúc đầu có $9$ chú chim, sau đó $4$ chú bay đi, rồi lại thêm $3$ chú bay đi nữa:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[line width=1.3pt, gray!80] (0,0.4) -- (8.0,0.4);
  \node[above, font=\bfseries\tiny, color=blue!90!black] at (1.0,0.5) {Còn $2$ con};
  \fill[blue!70!black] (0.7,0.55) circle (0.16cm); \fill[blue!70!black] (1.3,0.55) circle (0.16cm);
  \node[above, font=\bfseries\tiny, text=red!80!black] at (3.8,0.5) {Bay đi $4$ con};
  \foreach \i in {0,...,3}{ \draw[red!85, line width=1pt] (2.8+\i*0.6, 0.5) -- (3.2+\i*0.6, 0.85); }
  \node[above, font=\bfseries\tiny, text=orange!90!black] at (6.6,0.5) {Bay tiếp $3$ con};
  \foreach \i in {0,...,2}{ \draw[orange!90!black, line width=1pt] (5.8+\i*0.6, 0.5) -- (6.2+\i*0.6, 0.85); }
\end{tikzpicture}
\vspace{-2mm}\end{center}
Trên dây điện còn lại số chú chim là:
\begin{multicols}{4}
\choice
{$1$}
{\True $2$}
{$3$}
{$4$}
\end{multicols}
\loigiai{
Phép tính: $9 - 4 - 3 = 5 - 3 = 2$ chú chim.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Phép tính liên hoàn 7 + 3 - 5 = 5
\begin{ex} %[1D5V18]
Thực hiện phép tính liên hoàn theo sơ đồ mũi tên:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \node[draw=blue!70, circle, fill=blue!15, line width=1pt, font=\bfseries\normalsize, inner sep=4pt] (A) at (0,0) {7};
  \node[draw=purple!70, circle, fill=purple!15, line width=1pt, font=\bfseries\normalsize, inner sep=3pt] (B) at (3.0,0) {10};
  \node[draw=red!70, circle, fill=yellow!30, line width=1pt, font=\bfseries\normalsize, inner sep=4pt] (C) at (6.0,0) {?};
  \draw[->, >=stealth, line width=1.1pt, blue!80] (A) -- node[above, font=\bfseries\footnotesize] {$+ 3$} (B);
  \draw[->, >=stealth, line width=1.1pt, red!80] (B) -- node[above, font=\bfseries\footnotesize] {$- 5$} (C);
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số thích hợp điền vào dấu hỏi chấm ($?$) là:
\begin{multicols}{4}
\choice
{$4$}
{\True $5$}
{$6$}
{$7$}
\end{multicols}
\loigiai{
Thực hiện: $7 + 3 = 10$, sau đó $10 - 5 = 5$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Cân thăng bằng 5 + 3 = 10 - 2
\begin{ex} %[1D5V18]
Quan sát hai đĩa cân thăng bằng:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=brown!80!black] (3.85,-0.6) -- (4.15,-0.6) -- (4.05,0.4) -- (3.95,0.4) -- cycle;
  \draw[fill=gray!80] (3.3,-0.6) rectangle (4.7,-0.45);
  \draw[line width=2pt, gray!70!black] (1.2,0.4) -- (6.8,0.4);
  \fill[black] (4,0.4) circle (0.1cm);
  \draw[line width=0.8pt] (1.6,0.4) -- (1.6,-0.05);
  \draw[fill=teal!20, draw=teal!80, line width=0.8pt, rounded corners=2pt] (0.7,-0.05) rectangle (2.5,0.35);
  \node[font=\bfseries\footnotesize] at (1.6,0.15) {$5 + 3$};
  \draw[line width=0.8pt] (6.4,0.4) -- (6.4,-0.05);
  \draw[fill=teal!20, draw=teal!80, line width=0.8pt, rounded corners=2pt] (5.5,-0.05) rectangle (7.3,0.35);
  \node[font=\bfseries\footnotesize] at (6.4,0.15) {$10 - 2$};
  \node[draw=red!80, fill=yellow!30, line width=1pt, rounded corners=2pt, font=\bfseries\normalsize] at (4,0.9) {?};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Dấu thích hợp điền vào dấu hỏi chấm là:
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{$+$}
\end{multicols}
\loigiai{
Ta có $5 + 3 = 8$ và $10 - 2 = 8$. Vì $8 = 8$ nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Hộp kẹo bí mật ? + 4 = 9
\begin{ex} %[1D5V18]
Hộp quà bí mật có mấy viên kẹo để khi cộng thêm $4$ viên kẹo thì vừa đủ $9$ viên?
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=red!20, draw=red!70, rounded corners=3pt, line width=0.8pt] (0,0) rectangle (1.6,1.1);
  \node[font=\bfseries\Large, text=red!80!black] at (0.8,0.55) {?};
  \node[font=\bfseries\large] at (2.1,0.55) {$+$};
  \draw[fill=blue!15, draw=blue!60, rounded corners=3pt] (2.6,0.15) rectangle (4.4,0.95);
  \node[font=\bfseries\footnotesize] at (3.5,0.55) {$4$ viên};
  \node[font=\bfseries\large] at (4.9,0.55) {$=$};
  \draw[fill=green!15, draw=green!60!black, rounded corners=3pt] (5.4,0.15) rectangle (7.2,0.95);
  \node[font=\bfseries\footnotesize] at (6.3,0.55) {$9$ viên};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Trong hộp có số viên kẹo là:
\begin{multicols}{4}
\choice
{$4$}
{\True $5$}
{$6$}
{$3$}
\end{multicols}
\loigiai{
Phép tính: $? + 4 = 9 \implies ? = 9 - 4 = 5$ viên kẹo.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Nhảy lùi trục số 10 - ? = 3
\begin{ex} %[1D5V18]
Chú ếch nhảy lùi từ lá sen số $10$ về lá sen số $3$:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[->, >=stealth, line width=1pt] (0,0) -- (10.5,0);
  \foreach \x in {0,...,10}{
    \draw (\x,0.1) -- (\x,-0.1);
    \node[below, font=\bfseries\tiny] at (\x,-0.1) {\x};
  }
  \draw[->, >=stealth, line width=1.2pt, green!60!black, dashed] (10,0.25) arc (30:150:4.05cm);
  \node[font=\bfseries\tiny, text=green!70!black] at (6.5,1.8) {Nhảy lùi: $10 - ? = 3$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số bước chú ếch đã nhảy lùi là:
\begin{multicols}{4}
\choice
{$6$}
{\True $7$}
{$8$}
{$5$}
\end{multicols}
\loigiai{
Ta có $10 - 7 = 3$, nên số cần tìm là $7$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Ô tô chở phép tính lớn nhất
\begin{ex} %[1D5V18]
Trong các chiếc ô tô dưới đây, chiếc ô tô nào chở kết quả \textbf{lớn nhất}?
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \VeOTo{0}{0}{cyan!60}
  \node[font=\bfseries\tiny] at (0.75,0.8) {$4 + 4$};
  \node[below, font=\bfseries\tiny] at (0.75,-0.15) {Xe A};
  
  \VeOTo{2.6}{0}{yellow!70!orange}
  \node[font=\bfseries\tiny] at (3.35,0.8) {$3 + 7$};
  \node[below, font=\bfseries\tiny] at (3.35,-0.15) {Xe B};
  
  \VeOTo{5.2}{0}{pink!70}
  \node[font=\bfseries\tiny] at (5.95,0.8) {$9 - 1$};
  \node[below, font=\bfseries\tiny] at (5.95,-0.15) {Xe C};
  
  \VeOTo{7.8}{0}{green!50}
  \node[font=\bfseries\tiny] at (8.55,0.8) {$2 + 6$};
  \node[below, font=\bfseries\tiny] at (8.55,-0.15) {Xe D};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Chiếc ô tô chở phép tính có kết quả lớn nhất là:
\begin{multicols}{4}
\choice
{Xe A ($4+4$)}
{\True Xe B ($3+7$)}
{Xe C ($9-1$)}
{Xe D ($2+6$)}
\end{multicols}
\loigiai{
Xe A: $4+4=8$; Xe B: $3+7=10$; Xe C: $9-1=8$; Xe D: $2+6=8$. Xe B lớn nhất ($10$).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Đổi chỗ trong phép cộng
\begin{ex} %[1D5V18]
Khẳng định nào dưới đây là \textbf{đúng} khi đổi chỗ các số trong phép cộng?
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=yellow!15, draw=orange!70, rounded corners=3pt, line width=0.8pt] (0,0) rectangle (3.2,1.0);
  \node[font=\bfseries\normalsize] at (1.6,0.5) {$2 + 6 = 8$};
  \node[font=\bfseries\Large] at (4.0,0.5) {$\longleftrightarrow$};
  \draw[fill=yellow!15, draw=orange!70, rounded corners=3pt, line width=0.8pt] (4.8,0) rectangle (8.0,1.0);
  \node[font=\bfseries\normalsize] at (6.4,0.5) {$6 + 2 = 8$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Khẳng định đúng là:
\begin{multicols}{4}
\choice
{$2 + 6 > 6 + 2$}
{\True $2 + 6 = 6 + 2$}
{$2 + 6 < 6 + 2$}
{$2 + 6 = 6 - 2$}
\end{multicols}
\loigiai{
Khi đổi chỗ hai số trong phép cộng thì kết quả không đổi: $2 + 6 = 6 + 2 = 8$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: PHẦN 2 - TRẮC NGHIỆM ĐÚNG SAI (4 CÂU) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Ngôi nhà số 8
\begin{ex} %[1D5H18]
Quan sát ngôi nhà số $8$ (gia đình phép tính của số 8):
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.7, baseline=(current bounding box.center)]
  \draw[fill=red!60, draw=black!80, line width=1pt] (0,2.5) -- (3.5,4.0) -- (7,2.5) -- cycle;
  \node[font=\bfseries\Huge, text=yellow!30] at (3.5,3.1) {8};
  \draw[fill=yellow!15, draw=black!80, line width=1pt] (0,0) rectangle (7,2.5);
  \draw[line width=0.8pt, black!60] (3.5,0) -- (3.5,2.5);
  \draw[line width=0.8pt, black!60] (0,1.25) -- (7,1.25);
  \node[font=\bfseries\normalsize] at (1.75,1.85) {$5 + 3 = 8$};
  \node[font=\bfseries\normalsize] at (5.25,1.85) {$3 + 5 = 8$};
  \node[font=\bfseries\normalsize] at (1.75,0.65) {$8 - 3 = 5$};
  \node[font=\bfseries\normalsize] at (5.25,0.65) {$8 - 5 = 3$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính Đúng hay Sai của các khẳng định sau:
\choiceTF
{\True Phép cộng $5 + 3$ có kết quả bằng $8$.}
{Phép trừ $8 - 3$ có kết quả bằng $4$.}
{\True Khi biết $3 + 5 = 8$, ta có thể suy ra ngay $8 - 5 = 3$.}
{Nếu đổi $5 + 3$ thành $5 - 3$ thì kết quả vẫn bằng $8$.}
\loigiai{
\begin{itemize}
  \item a) Đúng: $5 + 3 = 8$.
  \item b) Sai: $8 - 3 = 5$ (chứ không phải $4$).
  \item c) Đúng: Phép trừ là phép tính ngược của phép cộng.
  \item d) Sai: $5 - 3 = 2 \neq 8$.
\end{itemize}
}
\end{ex}

% CÂU 14: Trang trại nuôi thỏ chuồng A và B
\begin{ex} %[1D5V18]
Trang trại nuôi hai chuồng thỏ: Chuồng A có $6$ con, chuồng B có $4$ con:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.7, baseline=(current bounding box.center)]
  \draw[fill=blue!10, draw=blue!70, rounded corners=4pt, line width=0.8pt] (0,0) rectangle (4.2,1.5);
  \node[font=\bfseries\tiny, text=blue!90!black] at (2.1,1.2) {Chuồng A: $6$ con thỏ};
  \foreach \i in {0,...,5}{
    \fill[orange!80!black] (0.5+\i*0.62, 0.5) circle (0.18cm);
    \draw[line width=1pt, orange!80!black] (0.42+\i*0.62, 0.65) -- (0.42+\i*0.62, 0.85);
    \draw[line width=1pt, orange!80!black] (0.58+\i*0.62, 0.65) -- (0.58+\i*0.62, 0.85);
  }
  \begin{scope}[shift={(4.8,0)}]
    \draw[fill=green!10, draw=green!70!black, rounded corners=4pt, line width=0.8pt] (0,0) rectangle (4.2,1.5);
    \node[font=\bfseries\tiny, text=green!80!black] at (2.1,1.2) {Chuồng B: $4$ con thỏ};
    \foreach \i in {0,...,3}{
      \fill[orange!80!black] (0.8+\i*0.8, 0.5) circle (0.18cm);
      \draw[line width=1pt, orange!80!black] (0.72+\i*0.8, 0.65) -- (0.72+\i*0.8, 0.85);
      \draw[line width=1pt, orange!80!black] (0.88+\i*0.8, 0.65) -- (0.88+\i*0.8, 0.85);
    }
  \end{scope}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính Đúng hay Sai của các khẳng định sau:
\choiceTF
{\True Cả hai chuồng có tất cả $10$ con thỏ.}
{Chuồng A có ít hơn chuồng B $2$ con thỏ.}
{\True Chuồng A nhiều hơn chuồng B là $6 - 4 = 2$ con thỏ.}
{Nếu chuyển $1$ con thỏ từ chuồng A sang chuồng B thì chuồng B có $6$ con.}
\loigiai{
\begin{itemize}
  \item a) Đúng: $6 + 4 = 10$ con.
  \item b) Sai: Chuồng A ($6$) nhiều hơn chuồng B ($4$).
  \item c) Đúng: $6 - 4 = 2$ con.
  \item d) Sai: Chuyển $1$ con sang B thì B có $4 + 1 = 5$ con.
\end{itemize}
}
\end{ex}

% CÂU 15: Xét tính đúng sai 4 phép tính cộng trừ PV 10
\begin{ex} %[1D5H18]
Bốn thẻ ghi các phép tính cộng, trừ trong phạm vi $10$:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.7]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\footnotesize] at (-4.2,0) {$4 + 6 = 10$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\footnotesize] at (-1.4,0) {$9 - 3 = 6$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\footnotesize] at (1.4,0) {$7 + 0 = 7$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\footnotesize] at (4.2,0) {$10 - 2 = 7$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính Đúng hay Sai của các phép tính sau:
\choiceTF
{\True Phép tính $4 + 6 = 10$ là đúng.}
{\True Phép tính $9 - 3 = 6$ là đúng.}
{\True Phép tính $7 + 0 = 7$ là đúng.}
{Phép tính $10 - 2 = 7$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) Đúng: $4 + 6 = 10$.
  \item b) Đúng: $9 - 3 = 6$.
  \item c) Đúng: Một số cộng với $0$ bằng chính nó ($7 + 0 = 7$).
  \item d) Sai: $10 - 2 = 8 \neq 7$.
\end{itemize}
}
\end{ex}

% CÂU 16: Táo của Mai, Lan, An
\begin{ex} %[1D5V18]
Ba bạn Mai, Lan và An thu hoạch táo trong vườn:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75]
  \draw[fill=red!15, draw=red!70, rounded corners=3pt] (-3.6,0) rectangle (-1.3,0.7) node[midway, font=\bfseries\footnotesize] {Mai: $5$ quả đỏ};
  \draw[fill=green!15, draw=green!70!black, rounded corners=3pt] (-1.1,0) rectangle (1.2,0.7) node[midway, font=\bfseries\footnotesize] {Lan: $4$ quả xanh};
  \draw[fill=yellow!25, draw=orange!80, rounded corners=3pt] (1.4,0) rectangle (3.7,0.7) node[midway, font=\bfseries\footnotesize] {An: $9$ quả vàng};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính Đúng hay Sai của các nhận xét sau:
\choiceTF
{\True Cả hai bạn Mai và Lan có tất cả $5 + 4 = 9$ quả táo.}
{\True Số táo của An bằng tổng số táo của Mai và Lan.}
{\True Mai thu hoạch được nhiều hơn Lan là $1$ quả táo.}
{Cả ba bạn thu hoạch được tất cả $15$ quả táo.}
\loigiai{
\begin{itemize}
  \item a) Đúng: $5 + 4 = 9$ quả táo.
  \item b) Đúng: An có $9$ quả, bằng tổng số táo của Mai và Lan ($9 = 9$).
  \item c) Đúng: $5 - 4 = 1$ quả táo.
  \item d) Sai: Cả ba bạn có $9 + 9 = 18$ quả táo (không phải $15$).
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: PHẦN 3 - CÂU HỎI TRẢ LỜI NGẮN (4 CÂU) ---

\textbf{Phần 3. Câu hỏi trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tháp số cộng 4 + 6 = 10
\begin{ex} %[1D5H18]
Quan sát tháp số cộng (số ở ô trên bằng tổng hai số liền kề bên dưới):
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=cyan!20, draw=blue!70, line width=0.8pt] (0,0) rectangle (1.4,0.8); \node[font=\bfseries\Large] at (0.7,0.4) {4};
  \draw[fill=cyan!20, draw=blue!70, line width=0.8pt] (1.6,0) rectangle (3.0,0.8); \node[font=\bfseries\Large] at (2.3,0.4) {6};
  \draw[fill=red!20, draw=red!70, line width=1pt] (0.8,0.95) rectangle (2.2,1.75);
  \node[font=\bfseries\LARGE, text=red!80!black] at (1.5,1.35) {?};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số thích hợp ở ô trên cùng là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$10$}}
\loigiai{
Số ở ô trên cùng là: $4 + 6 = 10$.\\
\textbf{Đáp số: $10$.}
}
\end{ex}

% CÂU 18: Xe buýt 7 bạn lên thêm 2
\begin{ex} %[1D5V18]
Trên xe buýt có $7$ bạn, đến trạm dừng có thêm $2$ bạn bước lên xe:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=yellow!80, draw=black!80, rounded corners=5pt, line width=1pt] (0,0) rectangle (5.0,2.0);
  \node[font=\bfseries\footnotesize, text=red!85!black] at (2.5,1.7) {XE BUÝT: $7$ bạn};
  \draw[fill=cyan!30] (0.4,0.6) rectangle (1.5,1.35);
  \draw[fill=cyan!30] (1.9,0.6) rectangle (3.0,1.35);
  \draw[fill=cyan!30] (3.4,0.6) rectangle (4.5,1.35);
  \fill[black] (1.0,-0.15) circle (0.28cm);
  \fill[black] (3.9,-0.15) circle (0.28cm);
  \node[font=\bfseries\small, text=blue!80!black] at (7.0,1.0) {Lên thêm: $2$ bạn};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Lúc này trên xe buýt có tất cả bao nhiêu bạn học sinh?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$9$}}
\loigiai{
Số bạn trên xe buýt là: $7 + 2 = 9$ (bạn).\\
\textbf{Đáp số: $9$ bạn.}
}
\end{ex}

% CÂU 19: Bể cá 10 con vớt 5 con
\begin{ex} %[1D5V18]
Bể cá ban đầu có $10$ con cá, bạn Nam vớt ra $3$ con cá đỏ và $2$ con cá vàng:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \node[font=\bfseries\tiny, text=blue!90!black] at (2.5,2.0) {Bể cá ban đầu: $10$ con};
  \draw[fill=cyan!15, draw=blue!60, rounded corners=6pt, line width=1pt] (0,0) rectangle (5.0,1.8);
  \VeChuCa{0.8}{1.0}{red!80}
  \VeChuCa{2.1}{0.6}{red!80}
  \VeChuCa{3.5}{1.1}{red!80}
  \VeChuCa{1.5}{1.4}{yellow!90!black}
  \VeChuCa{4.2}{0.7}{yellow!90!black}
  \node[right, font=\bfseries\tiny, text=red!80!black] at (5.2,0.9) {Đã vớt: $3 + 2 = 5$ con};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Hỏi trong bể còn lại bao nhiêu con cá?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$5$}}
\loigiai{
Số cá vớt ra là $3 + 2 = 5$ con. Trong bể còn lại: $10 - 5 = 5$ (con cá).\\
\textbf{Đáp số: $5$ con cá.}
}
\end{ex}

% CÂU 20: Tính nhanh 1 + 2 + 3 + 4 = 10
\begin{ex} %[1D5V18]
Tính nhanh giá trị của biểu thức gộp cặp:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[fill=teal!15, draw=teal!70, rounded corners=4pt, line width=0.8pt] (0,0) rectangle (5.5,1.1);
  \node[font=\bfseries\large, text=teal!90!black] at (2.75,0.55) {$1 + 2 + 3 + 4 = \text{\textbf{?}}$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Kết quả của biểu thức là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$10$}}
\loigiai{
Gộp cặp: $(1 + 4) + (2 + 3) = 5 + 5 = 10$.\\
\textbf{Đáp số: $10$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 5 Bai 18
tex_path = os.path.abspath('CHỦ ĐỀ 5 - ÔN TẬP HỌC KÌ 1/Chuong5_Bai18_OnTapPhepCongPhepTruTrongPhamVi10.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_18_preview.tex độc lập 5 trang
preview_content = r'''\documentclass[14pt,a4paper]{extbook}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,calc,positioning,backgrounds,patterns,decorations.pathreplacing}
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 18: ÔN TẬP PHÉP CỘNG, PHÉP TRỪ PV 10},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 1 -- Chủ đề 5: Ôn tập học kì 1}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-18}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_18_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_18_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_18_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_18_preview.pdf'):
    import pypdf, shutil
    reader = pypdf.PdfReader('Bai_18_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    if num_pages == 5:
        out_dir = os.path.abspath('PDF_DeThi_TungBai')
        os.makedirs(out_dir, exist_ok=True)
        # Đồng bộ cả 2 tên file để không còn file 2 trang cũ
        out_pdf1 = os.path.join(out_dir, 'Bai_18_On_tap_phep_cong_phep_tru_trong_pham_vi_10.pdf')
        out_pdf2 = os.path.join(out_dir, 'Bai_18_On_tap_phep_cong_phep_tru_PV_10.pdf')
        shutil.copy2('Bai_18_preview.pdf', out_pdf1)
        shutil.copy2('Bai_18_preview.pdf', out_pdf2)
        print(f"ĐÃ XUẤT THÀNH CÔNG:")
        print(f" - {out_pdf1} ({num_pages} trang)")
        print(f" - {out_pdf2} ({num_pages} trang)")
    else:
        print(f"CẢNH BÁO: Số trang hiện tại là {num_pages}, chưa khớp chuẩn 5 trang!")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
