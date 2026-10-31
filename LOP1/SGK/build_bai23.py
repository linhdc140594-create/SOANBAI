# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 23: BẢNG CÁC SỐ TỪ 1 ĐẾN 100 (CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100 - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 23 ---

% 1. Tấm bách 100 khối lập phương nhỏ (10 hàng x 10 cột)
\providecommand{\VeTamBachTram}[2]{% #1=màu khối, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.15]
    \foreach \r in {0,1,...,9} {
      \foreach \c in {0,1,...,9} {
        \draw[fill=#1, draw=black!70, line width=0.3pt] (\c, \r) rectangle (\c+0.9, \r+0.9);
      }
    }
    % Hiệu ứng 3D viền trên và phải của cả tấm
    \draw[fill=white!50!#1, draw=black!75, line width=0.4pt] 
      (0,9.9) -- (10,9.9) -- (10.6,10.5) -- (0.6,10.5) -- cycle;
    \draw[fill=black!30!#1, draw=black!75, line width=0.4pt] 
      (10,0) -- (10.6,0.6) -- (10.6,10.5) -- (10,9.9) -- cycle;
  \end{scope}
}

% 2. Mảnh ghép chữ thập bảng 100
\providecommand{\VeManhGhepDauThap}[6]{% #1=(x,y), #2=trung tâm, #3=trên, #4=dưới, #5=trái, #6=phải
  \begin{scope}[shift={(#1)}, scale=0.52]
    % Ô trung tâm
    \draw[fill=yellow!30, draw=blue!80!black, line width=0.8pt, rounded corners=2pt] (-0.5,-0.5) rectangle (0.5,0.5);
    \node[font=\bfseries\normalsize, color=red!80!black] at (0,0) {#2};
    % Ô trên
    \draw[fill=cyan!20, draw=blue!80!black, line width=0.8pt, rounded corners=2pt] (-0.5,0.6) rectangle (0.5,1.6);
    \node[font=\bfseries\normalsize, color=blue!90!black] at (0,1.1) {#3};
    % Ô dưới
    \draw[fill=cyan!20, draw=blue!80!black, line width=0.8pt, rounded corners=2pt] (-0.5,-1.6) rectangle (0.5,-0.6);
    \node[font=\bfseries\normalsize, color=blue!90!black] at (0,-1.1) {#4};
    % Ô trái
    \draw[fill=cyan!20, draw=blue!80!black, line width=0.8pt, rounded corners=2pt] (-1.6,-0.5) rectangle (-0.6,0.5);
    \node[font=\bfseries\normalsize, color=blue!90!black] at (-1.1,0) {#5};
    % Ô phải
    \draw[fill=cyan!20, draw=blue!80!black, line width=0.8pt, rounded corners=2pt] (0.6,-0.5) rectangle (1.6,0.5);
    \node[font=\bfseries\normalsize, color=blue!90!black] at (1.1,0) {#6};
  \end{scope}
}

% 3. Toa tàu hỏa mang số
\providecommand{\VeToaTauSo}[4]{% #1=(x,y), #2=màu toa, #3=số, #4=có móc nối (0/1)
  \begin{scope}[shift={(#1)}, scale=0.55]
    \ifnum#4=1
      \draw[black!80, line width=1.6pt] (1.1,0.2) -- (1.5,0.2);
    \fi
    \draw[fill=#2!40, draw=black!80, line width=0.7pt, rounded corners=3pt] (-1.1,0) rectangle (1.1,0.9);
    \draw[fill=white, draw=black!70, line width=0.6pt, rounded corners=2pt] (-0.85,0.15) rectangle (0.85,0.75);
    \node[font=\bfseries\large, color=blue!90!black] at (0,0.45) {#3};
    \fill[black!85] (-0.6,-0.12) circle (0.2cm);
    \fill[gray!40] (-0.6,-0.12) circle (0.09cm);
    \fill[black!85] (0.6,-0.12) circle (0.2cm);
    \fill[gray!40] (0.6,-0.12) circle (0.09cm);
  \end{scope}
}

% 4. Chú ếch nhảy lá sen
\providecommand{\VeLaSen}[3]{% #1=(x,y), #2=màu, #3=số
  \begin{scope}[shift={(#1)}, scale=0.6]
    \draw[fill=#2!60!teal, draw=green!60!black, line width=0.8pt] (0,0) ellipse (0.85cm and 0.42cm);
    \draw[green!90!black, line width=0.5pt] (0,0) -- (0.5,0.2);
    \draw[green!90!black, line width=0.5pt] (0,0) -- (-0.5,0.2);
    \draw[green!90!black, line width=0.5pt] (0,0) -- (0,-0.3);
    \node[draw=green!90!black, fill=white, rounded corners=2pt, font=\bfseries\normalsize, inner sep=2pt] at (0,0.5) {#3};
  \end{scope}
}

\providecommand{\VeChuEchMini}[1]{% #1=(x,y)
  \begin{scope}[shift={(#1)}, scale=0.45]
    \fill[green!70!teal] (0,0) ellipse (0.55cm and 0.4cm);
    \fill[green!80!black] (-0.28,0.3) circle (0.16cm);
    \fill[green!80!black] (0.28,0.3) circle (0.16cm);
    \fill[white] (-0.28,0.3) circle (0.1cm);
    \fill[white] (0.28,0.3) circle (0.1cm);
    \fill[black] (-0.26,0.3) circle (0.05cm);
    \fill[black] (0.26,0.3) circle (0.05cm);
    \draw[black!80, line width=0.6pt] (-0.2,-0.1) arc (190:350:0.2cm and 0.1cm);
  \end{scope}
}

% 5. Đốt sâu bướm mang số
\providecommand{\VeDotSau}[4]{% #1=(x,y), #2=màu, #3=số, #4=đầu sâu (0/1)
  \begin{scope}[shift={(#1)}, scale=0.55]
    \draw[fill=#2!60!yellow, draw=black!80, line width=0.8pt] (0,0) circle (0.52cm);
    \node[font=\bfseries\normalsize, color=black] at (0,0) {#3};
    \ifnum#4=1
      \fill[black] (0.2,0.25) circle (0.07cm);
      \fill[black] (0.45,0.2) circle (0.07cm);
      \draw[black!80, line width=1pt] (0.2,0.5) .. controls (0.2,0.8) and (0.1,0.9) .. (0.05,1.0);
      \fill[red] (0.05,1.0) circle (0.08cm);
      \draw[black!80, line width=1pt] (0.4,0.45) .. controls (0.5,0.75) and (0.6,0.85) .. (0.65,0.95);
      \fill[red] (0.65,0.95) circle (0.08cm);
      \draw[red!80!black, line width=0.8pt] (0.3,-0.15) arc (200:340:0.18cm and 0.12cm);
    \fi
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Nhận biết số 100 qua tấm bách 100 ô
\begin{ex} %[1D6N23]
Hình dưới đây là tấm bách gồm $10$ thanh chục ghép lại ($10$ chục):
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeTamBachTram{cyan!65}{0,0}
  \draw[line width=1pt, stealth-stealth, blue!80!black] (-0.2,0) -- (-0.2,1.6) node[midway, left, font=\bfseries\tiny] {$10$ hàng};
  \draw[line width=1pt, stealth-stealth, blue!80!black] (0,-0.2) -- (1.6,-0.2) node[midway, below, font=\bfseries\tiny] {$10$ cột};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Tấm bách này gồm tất cả bao nhiêu ô vuông nhỏ? Số một trăm viết là:
\begin{multicols}{2}
\choice
{$10$ ô; viết là $10$}
{\True $100$ ô; viết là $100$}
{$1000$ ô; viết là $1000$}
{$99$ ô; viết là $99$}
\end{multicols}
\loigiai{
Mỗi hàng có $10$ ô vuông, $10$ hàng như vậy có tất cả: $10$ chục $= 100$ ô vuông nhỏ. Số một trăm viết là $100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Số lớn nhất và số cuối cùng trong bảng 100
\begin{ex} %[1D6N23]
Quan sát bảng các số từ $1$ đến $100$ thu nhỏ:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.55]
  \draw[fill=blue!5, draw=blue!70, line width=0.7pt, rounded corners=3pt] (0,0) rectangle (6.8,1.4);
  % Ô số 1
  \draw[fill=yellow!40, draw=orange!90, line width=0.6pt, rounded corners=2pt] (0.25,0.75) rectangle (1.05,1.25);
  \node[font=\bfseries\small, color=blue!90!black] at (0.65,1.0) {$1$};
  \node[right, font=\scriptsize\itshape, color=gray!90!black] at (1.1,1.0) {(Số đầu tiên)};
  % Dấu chấm liên tiếp
  \node[font=\bfseries\normalsize, color=blue!70] at (3.4,0.7) {$\dots\dots$};
  % Ô số 100
  \draw[fill=red!25, draw=red!80, line width=0.7pt, rounded corners=2pt] (5.7,0.15) rectangle (6.55,0.65);
  \node[font=\bfseries\small, color=red!90!black] at (6.12,0.4) {$100$};
  \node[left, font=\scriptsize\itshape, color=gray!90!black] at (5.65,0.4) {(Số cuối cùng)};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Trong bảng các số từ $1$ đến $100$, số cuối cùng đồng thời là số lớn nhất là số nào?
\begin{multicols}{4}
\choice
{Số $10$}
{\True Số $100$}
{Số $99$}
{Số $1$}
\end{multicols}
\loigiai{
Trong bảng các số từ $1$ đến $100$, số đầu tiên là $1$ và số cuối cùng lớn nhất là $100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Số đứng liền trước số 100
\begin{ex} %[1D6H23]
Đoàn tàu hỏa chở các toa cuối cùng về ga số $100$:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeToaTauSo{-2.6,0}{teal}{98}{1}
  \VeToaTauSo{0,0}{orange}{~?~}{1}
  \VeToaTauSo{2.6,0}{red}{100}{0}
  \node[above, font=\bfseries\tiny, color=red!80!black] at (0,0.6) {Liền trước $100$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số đứng liền trước số $100$ cần điền vào dấu \textbf{?} là:
\begin{multicols}{4}
\choice
{$101$}
{\True $99$}
{$98$}
{$90$}
\end{multicols}
\loigiai{
Số đứng liền trước số $100$ là số đứng ngay phía trước nó: $100 - 1 = 99$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Mảnh ghép bảng số 100 hình dấu thập
\begin{ex} %[1D6H23]
Một mảnh ghép hình dấu thập được cắt ra từ bảng các số từ $1$ đến $100$:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeManhGhepDauThap{0,0}{45}{35}{~?~}{44}{46}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số thích hợp để điền vào ô dấu \textbf{?} (ngay dưới số $45$) là:
\begin{multicols}{4}
\choice
{$54$}
{\True $55$}
{$47$}
{$65$}
\end{multicols}
\loigiai{
Trong bảng các số từ $1$ đến $100$, ô ngay phía dưới số $45$ là: $45 + 10 = 55$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Các số tròn chục trong bảng 100
\begin{ex} %[1D6V23]
Quan sát hàng xe tải chở toàn bộ các số tròn chục từ $10$ đến $100$:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \foreach \i/\num in {0/10, 1.3/20, 2.6/30, 3.9/40, 5.2/50} {
    \draw[fill=blue!30, draw=black!80, line width=0.5pt, rounded corners=2pt] (\i,0) rectangle (\i+1.05,0.65);
    \node[font=\bfseries\tiny, color=blue!90!black] at (\i+0.52,0.32) {\num};
    \fill[black] (\i+0.25,-0.08) circle (0.08cm);
    \fill[black] (\i+0.8,-0.08) circle (0.08cm);
  }
  \begin{scope}[shift={(6.8,0)}]
    \foreach \i/\num in {0/60, 1.3/70, 2.6/80, 3.9/90, 5.2/100} {
      \draw[fill=green!30, draw=black!80, line width=0.5pt, rounded corners=2pt] (\i,0) rectangle (\i+1.05,0.65);
      \node[font=\bfseries\tiny, color=green!90!black] at (\i+0.52,0.32) {\num};
      \fill[black] (\i+0.25,-0.08) circle (0.08cm);
      \fill[black] (\i+0.8,-0.08) circle (0.08cm);
    }
  \end{scope}
\end{tikzpicture}
\end{center}
Dãy các số tròn chục từ $10$ đến $100$ trong bảng gồm tất cả bao nhiêu số?
\begin{multicols}{4}
\choice
{$9$ số}
{\True $10$ số}
{$8$ số}
{$11$ số}
\end{multicols}
\loigiai{
Có tất cả $10$ số tròn chục: $10, 20, 30, 40, 50, 60, 70, 80, 90, 100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Chú ếch nhảy thêm 5 đơn vị
\begin{ex} %[1D6V23]
Chú ếch xanh nhảy trên các lá sen theo quy luật đếm thêm $5$ đơn vị:
\begin{center}
\begin{tikzpicture}
  \VeLaSen{-4.2,0}{green}{80}
  \VeLaSen{-2.1,0}{green}{85}
  \VeLaSen{0,0}{green}{90}
  \VeLaSen{2.1,0}{green}{95}
  \VeLaSen{4.2,0}{orange}{~?~}
  % Các bước nhảy
  \draw[line width=1.1pt, red!85, dashed, ->] (-4.2,0.65) to[bend left=35] (-2.1,0.65);
  \draw[line width=1.1pt, red!85, dashed, ->] (-2.1,0.65) to[bend left=35] (0,0.65);
  \draw[line width=1.1pt, red!85, dashed, ->] (0,0.65) to[bend left=35] (2.1,0.65);
  \draw[line width=1.1pt, red!85, dashed, ->] (2.1,0.65) to[bend left=35] (4.2,0.65);
  \VeChuEchMini{2.1,1.15}
\end{tikzpicture}
\end{center}
Số tiếp theo chú ếch sẽ nhảy tới (trên lá sen dấu \textbf{?}) là:
\begin{multicols}{4}
\choice
{$96$}
{\True $100$}
{$98$}
{$99$}
\end{multicols}
\loigiai{
Quy luật đếm thêm $5$: $80, 85, 90, 95$. Số tiếp theo là: $95 + 5 = 100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Số có hai chữ số giống nhau
\begin{ex} %[1D6V23]
Các bông hoa dưới đây ghi các số có hai chữ số giống nhau trong bảng $100$:
\begin{center}
\begin{tikzpicture}[scale=0.68]
  \foreach \i/\num in {0/11, 1.15/22, 2.3/33, 3.45/44, 4.6/55, 5.75/66, 6.9/77, 8.05/88, 9.2/99} {
    \draw[fill=pink!60, draw=red!70, line width=0.5pt] (\i,0) circle (0.45cm);
    \node[font=\bfseries\scriptsize, color=red!90!black] at (\i,0) {\num};
  }
\end{tikzpicture}
\end{center}
Trong bảng các số từ $1$ đến $100$, có tất cả bao nhiêu số có hai chữ số giống nhau?
\begin{multicols}{4}
\choice
{$8$ số}
{\True $9$ số}
{$10$ số}
{$11$ số}
\end{multicols}
\loigiai{
Các số có hai chữ số giống nhau gồm: $11, 22, 33, 44, 55, 66, 77, 88, 99$. Tổng cộng có $9$ số.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Phân loại số có 1, 2, 3 chữ số trong bảng 100
\begin{ex} %[1D6V23]
Ba chiếc hộp dưới đây đựng các thẻ số được lấy từ bảng $100$:
\begin{center}
\begin{tikzpicture}[scale=0.72]
  % Hộp 1 chữ số
  \draw[fill=blue!15, draw=blue!80, line width=0.7pt, rounded corners=3pt] (-3.8,0) rectangle (-1.2,1.2);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (-2.5,0.85) {Số có $1$ chữ số};
  \node[font=\tiny, color=black] at (-2.5,0.35) {Từ $1$ đến $9$ ($9$ số)};
  % Hộp 2 chữ số
  \draw[fill=green!15, draw=green!80, line width=0.7pt, rounded corners=3pt] (-1,0) rectangle (1.6,1.2);
  \node[font=\bfseries\scriptsize, color=green!90!black] at (0.3,0.85) {Số có $2$ chữ số};
  \node[font=\tiny, color=black] at (0.3,0.35) {Từ $10$ đến $99$ ($90$ số)};
  % Hộp 3 chữ số
  \draw[fill=red!15, draw=red!80, line width=0.7pt, rounded corners=3pt] (1.8,0) rectangle (4.4,1.2);
  \node[font=\bfseries\scriptsize, color=red!90!black] at (3.1,0.85) {Số có $3$ chữ số};
  \node[font=\bfseries\small, color=red!90!black] at (3.1,0.35) {Số $100$};
\end{tikzpicture}
\end{center}
Trong bảng các số từ $1$ đến $100$, có bao nhiêu số có $3$ chữ số?
\begin{multicols}{2}
\choice
{$0$ số}
{\True $1$ số (chính là số $100$)}
{$2$ số}
{$10$ số}
\end{multicols}
\loigiai{
Từ $1$ đến $99$ chỉ gồm các số có $1$ và $2$ chữ số. Chỉ có duy nhất số $100$ là số có $3$ chữ số.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Mảnh ghép hình chữ L
\begin{ex} %[1D6V23]
Cho một mảnh ghép hình chữ L được cắt ra từ bảng $100$:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  % Ô trên: 28
  \draw[fill=yellow!30, draw=blue!80, line width=0.8pt] (0,0.95) rectangle (1.1,1.9);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0.55,1.42) {$28$};
  % Ô dưới: 38
  \draw[fill=yellow!30, draw=blue!80, line width=0.8pt] (0,0) rectangle (1.1,0.95);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0.55,0.47) {$38$};
  % Ô phải của 38: ?
  \draw[fill=cyan!30, draw=blue!80, line width=0.8pt] (1.1,0) rectangle (2.2,0.95);
  \node[font=\bfseries\normalsize, color=red!90!black] at (1.65,0.47) {?};
\end{tikzpicture}
\end{center}
Số thích hợp điền vào ô dấu \textbf{?} (ngay bên phải số $38$) là:
\begin{multicols}{4}
\choice
{$37$}
{\True $39$}
{$48$}
{$49$}
\end{multicols}
\loigiai{
Trong bảng $100$, số đứng liền sau ở bên phải một số hơn số đó $1$ đơn vị. Bên phải số $38$ là: $38 + 1 = 39$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Chú sâu bướm tìm số liền sau
\begin{ex} %[1D6H23]
Chú sâu bướm ngộ nghĩnh mang các số liên tiếp:
\begin{center}
\begin{tikzpicture}
  \VeDotSau{-3.2,0}{cyan}{67}{0}
  \VeDotSau{-2.1,0}{green}{68}{0}
  \VeDotSau{-1.0,0}{yellow}{69}{0}
  \VeDotSau{0.1,0}{orange}{70}{0}
  \VeDotSau{1.2,0}{pink}{71}{1}
  \draw[line width=1pt, blue!80, ->] (-1.0,-0.55) to[bend right=30] (0.1,-0.55) node[midway, below, font=\tiny\bfseries] {Liền sau};
\end{tikzpicture}
\end{center}
Số đứng liền sau của số $69$ là số nào?
\begin{multicols}{4}
\choice
{$68$}
{\True $70$}
{$79$}
{$60$}
\end{multicols}
\loigiai{
Số đứng liền sau của $69$ là: $69 + 1 = 70$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Đếm lùi từ 100
\begin{ex} %[1D6V23]
Màn hình đếm ngược của phi thuyền vũ trụ hiển thị dãy số đếm bớt $1$:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \foreach \i/\num in {-3.6/100, -1.8/99, 0/98, 1.8/97} {
    \draw[fill=blue!85!black, draw=cyan!80, line width=1pt, rounded corners=3pt] (\i,-0.45) rectangle (\i+1.35,0.45);
    \node[font=\bfseries\normalsize, color=yellow] at (\i+0.67,0) {\num};
  }
  \draw[fill=red!85!black, draw=yellow, line width=1.1pt, rounded corners=3pt] (3.6,-0.45) rectangle (4.95,0.45);
  \node[font=\bfseries\large, color=white] at (4.27,0) {?};
\end{tikzpicture}
\end{center}
Số tiếp theo trong dãy đếm bớt trên là:
\begin{multicols}{4}
\choice
{$95$}
{\True $96$}
{$94$}
{$98$}
\end{multicols}
\loigiai{
Dãy số đếm lùi từng đơn vị: $100, 99, 98, 97$. Số tiếp theo là: $97 - 1 = 96$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Đố vui tìm số tròn chục
\begin{ex} %[1D6C23]
Bức thư bí mật đưa ra câu đố:
\begin{center}
\begin{tikzpicture}
  \draw[fill=yellow!15, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3.8,-0.6) rectangle (3.8,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black, align=center] at (0,0) {
    ``Tôi là số tròn chục lớn hơn $70$,\\
    nhưng đứng liền trước số $90$ trong hàng các số tròn chục. Tôi là số nào?''
  };
\end{tikzpicture}
\end{center}
Số bí mật được nhắc tới trong bức thư là:
\begin{multicols}{4}
\choice
{$75$}
{\True $80$}
{$85$}
{$90$}
\end{multicols}
\loigiai{
Các số tròn chục từ $70$ đến $90$ là: $70, 80, 90$. Số tròn chục lớn hơn $70$ và liền trước $90$ chính là số $80$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Toàn cảnh cấu trúc bảng 100
\begin{ex} %[1D6H23]
Quan sát mô hình cấu trúc bảng các số từ $1$ đến $100$:
\begin{center}
\begin{tikzpicture}[scale=0.55]
  \draw[fill=gray!10, draw=blue!80, line width=0.8pt] (0,0) rectangle (10,4.6);
  \node[above, font=\bfseries\scriptsize, color=blue!90!black] at (5,4.6) {Gồm $10$ cột};
  \node[left, font=\bfseries\scriptsize, color=blue!90!black] at (0,2.3) {$10$ hàng};
  % Hàng 1
  \node[font=\scriptsize\bfseries] at (1.5,4.1) {$1, 2, \dots, 10$};
  % Cột cuối
  \draw[fill=red!15, draw=red!70, line width=0.6pt] (8.8,0) rectangle (10,4.6);
  \node[font=\tiny\bfseries, color=red!90!black, rotate=90] at (9.4,2.3) {Cột số tròn chục};
  % Hàng 10
  \node[font=\scriptsize\bfseries] at (4.5,0.5) {$91, 92, \dots, 99, 100$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Bảng các số từ $1$ đến $100$ gồm đúng $10$ hàng và $10$ cột.}
{\True Cột cuối cùng bên phải gồm toàn bộ các số tròn chục từ $10$ đến $100$.}
{Số bé nhất có hai chữ số trong bảng là số $01$.}
{\True Hàng cuối cùng của bảng gồm các số từ $91$ đến $100$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Bảng có $10$ hàng $\times 10$ cột $= 100$ số.
  \item b) \textbf{Đúng}: Cột cuối bên phải là: $10, 20, 30, \dots, 100$.
  \item c) \textbf{Sai}: Số bé nhất có hai chữ số là $10$ (số $1$ là số có một chữ số, không viết là $01$).
  \item d) \textbf{Đúng}: Hàng thứ $10$ gồm các số $91, 92, 93, 94, 95, 96, 97, 98, 99, 100$.
\end{itemize}
}
\end{ex}

% CÂU 14: Quy luật các ô liền kề trong bảng
\begin{ex} %[1D6H23]
Sơ đồ quan hệ vị trí của một số trong bảng $100$:
\begin{center}
\begin{tikzpicture}[scale=0.55]
  \node[draw=blue!80, fill=yellow!30, rounded corners=2pt, font=\bfseries\normalsize, inner sep=3pt] at (0,0) {Số $56$};
  \node[draw=black!70, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize, inner sep=2pt] at (0,1.2) {Hàng trên: $46$};
  \node[draw=black!70, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize, inner sep=2pt] at (0,-1.2) {Hàng dưới: $66$};
  \node[draw=black!70, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize, inner sep=2pt] at (-2.6,0) {Bên trái: $55$};
  \node[draw=black!70, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize, inner sep=2pt] at (2.6,0) {Bên phải: $57$};
  \draw[line width=0.8pt, ->] (-0.8,0) -- (-1.7,0);
  \draw[line width=0.8pt, ->] (0.8,0) -- (1.7,0);
  \draw[line width=0.8pt, ->] (0,0.5) -- (0,0.85);
  \draw[line width=0.8pt, ->] (0,-0.5) -- (0,-0.85);
\end{tikzpicture}
\end{center}
Xét vị trí số $56$ trong bảng, đúng hay sai:
\choiceTF
{\True Số đứng liền trước (bên trái) số $56$ là $55$.}
{\True Số đứng liền sau (bên phải) số $56$ là $57$.}
{Số ở ô ngay phía trên cùng một cột với số $56$ là $66$.}
{\True Số ở ô ngay phía dưới cùng một cột với số $56$ là $66$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Bên trái là $56 - 1 = 55$.
  \item b) \textbf{Đúng}: Bên phải là $56 + 1 = 57$.
  \item c) \textbf{Sai}: Ô ngay trên là $56 - 10 = 46$ (chứ không phải $66$).
  \item d) \textbf{Đúng}: Ô ngay dưới là $56 + 10 = 66$.
\end{itemize}
}
\end{ex}

% CÂU 15: Số lượng các loại số
\begin{ex} %[1D6V23]
Phân chia $100$ số trong bảng thành các nhóm:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=pink!25, draw=red!70, line width=0.6pt, rounded corners=2pt] (-4,0) rectangle (-1.2,0.85);
  \node[font=\bfseries\scriptsize, color=red!90!black] at (-2.6,0.42) {$9$ số có $1$ chữ số};
  \draw[fill=blue!25, draw=blue!70, line width=0.6pt, rounded corners=2pt] (-0.9,0) rectangle (2.3,0.85);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (0.7,0.42) {$90$ số có $2$ chữ số};
  \draw[fill=green!25, draw=green!70, line width=0.6pt, rounded corners=2pt] (2.6,0) rectangle (4.6,0.85);
  \node[font=\bfseries\scriptsize, color=green!90!black] at (3.6,0.42) {$1$ số có $3$ chữ số};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Từ số $1$ đến số $9$ có tất cả $9$ số có một chữ số.}
{\True Từ số $10$ đến số $99$ có tất cả $90$ số có hai chữ số.}
{\True Trong bảng chỉ có duy nhất $1$ số có ba chữ số là số $100$.}
{Số $100$ là số lớn nhất có hai chữ số.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Các số $1, 2, 3, 4, 5, 6, 7, 8, 9$ (tổng cộng $9$ số).
  \item b) \textbf{Đúng}: Số lượng các số có hai chữ số là: $99 - 10 + 1 = 90$ số.
  \item c) \textbf{Đúng}: Số $100$ là số duy nhất có 3 chữ số trong bảng.
  \item d) \textbf{Sai}: Số $100$ có ba chữ số, số lớn nhất có hai chữ số là $99$.
\end{itemize}
}
\end{ex}

% CÂU 16: Dãy số đếm tiến và đếm lùi
\begin{ex} %[1D6V23]
Dãy số trên đường chạy thi đấu:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[line width=1.5pt, gray!70] (-4.5,0) -- (4.5,0);
  \foreach \i/\num in {-4/92, -2/94, 0/96, 2/98, 4/100} {
    \fill[blue!80] (\i,0) circle (0.12cm);
    \draw[fill=yellow!30, draw=blue!80, line width=0.6pt, rounded corners=2pt] (\i-0.45,0.2) rectangle (\i+0.45,0.75);
    \node[font=\bfseries\scriptsize, color=blue!90!black] at (\i,0.47) {\num};
  }
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các nhận xét sau:
\choiceTF
{\True Dãy $92, 94, 96, 98, 100$ là dãy số đếm thêm $2$ đơn vị.}
{\True Ở giữa số $98$ và số $100$ là số $99$.}
{Số liền trước của số $99$ là số $100$.}
{\True Số liền sau của số $99$ là số $100$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Mỗi số cách nhau $2$ đơn vị.
  \item b) \textbf{Đúng}: Thứ tự là $98, 99, 100$.
  \item c) \textbf{Sai}: Số liền trước của $99$ là $98$ (không phải $100$).
  \item d) \textbf{Đúng}: Số đứng ngay sau $99$ là $100$.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN / ĐIỀN SỐ) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tìm số liền trước của số 100
\begin{ex} %[1D6H23]
Ngôi nhà số $100$ có cửa sổ bên trái là số liền trước:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  % Mái nhà
  \draw[fill=red!70, draw=black!80, line width=0.8pt] (-2,1.2) -- (0,2.3) -- (2,1.2) -- cycle;
  % Thân nhà
  \draw[fill=yellow!25, draw=black!80, line width=0.8pt] (-1.8,-0.5) rectangle (1.8,1.2);
  % Cửa chính số 100
  \draw[fill=brown!60, draw=black!80, line width=0.6pt] (-0.5,-0.5) rectangle (0.5,0.7);
  \node[font=\bfseries\large, color=white] at (0,0.1) {$100$};
  % Cửa sổ liền trước
  \draw[fill=cyan!30, draw=blue!80, line width=0.7pt] (-1.5,0.1) rectangle (-0.7,0.8);
  \node[font=\bfseries\normalsize, color=red!90!black] at (-1.1,0.45) {?};
  \node[below, font=\tiny\bfseries, color=blue!80!black] at (-1.1,0.1) {Liền trước};
\end{tikzpicture}
\end{center}
Số đứng liền trước số $100$ là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$99$}}
\loigiai{
Số đứng liền trước số $100$ là: $100 - 1 = 99$.\\
\textbf{Đáp số: $99$.}
}
\end{ex}

% CÂU 18: Mảnh ghép hình vuông 2x2
\begin{ex} %[1D6V23]
Một mảnh ghép $4$ ô vuông được cắt ra từ bảng $100$:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=yellow!30, draw=blue!80, line width=0.8pt] (0,0.95) rectangle (1.1,1.9);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0.55,1.42) {$73$};
  \draw[fill=yellow!30, draw=blue!80, line width=0.8pt] (1.1,0.95) rectangle (2.2,1.9);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (1.65,1.42) {$74$};
  \draw[fill=yellow!30, draw=blue!80, line width=0.8pt] (0,0) rectangle (1.1,0.95);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0.55,0.47) {$83$};
  \draw[fill=pink!40, draw=blue!80, line width=0.8pt] (1.1,0) rectangle (2.2,0.95);
  \node[font=\bfseries\normalsize, color=red!90!black] at (1.65,0.47) {?};
\end{tikzpicture}
\end{center}
Số cần điền vào ô có dấu \textbf{?} là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$84$}}
\loigiai{
Ô dấu ? nằm ngay bên phải số $83$ ($83 + 1 = 84$) và nằm ngay dưới số $74$ ($74 + 10 = 84$).\\
\textbf{Đáp số: $84$.}
}
\end{ex}

% CÂU 19: Đếm số tròn chục
\begin{ex} %[1D6V23]
Các bó hoa hồng, mỗi bó có $10$ bông, được cắm từ $1$ bó đến $10$ bó:
\begin{center}
\begin{tikzpicture}[scale=0.55]
  \foreach \k/\num in {1/10, 2/20, 3/30, 4/40, 5/50, 6/60, 7/70, 8/80, 9/90, 10/100} {
    \draw[fill=red!25, draw=red!80, line width=0.5pt, rounded corners=2pt] (\k*1.15-0.5,0) rectangle (\k*1.15+0.5,0.65);
    \node[font=\bfseries\tiny, color=red!90!black] at (\k*1.15,0.32) {\num};
  }
\end{tikzpicture}
\end{center}
Trong bảng các số từ $1$ đến $100$, có tất cả bao nhiêu số tròn chục?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$10$}}
\loigiai{
Có tất cả $10$ số tròn chục: $10, 20, 30, 40, 50, 60, 70, 80, 90, 100$.\\
\textbf{Đáp số: $10$ số.}
}
\end{ex}

% CÂU 20: Vận dụng cao - Tìm số theo điều kiện chữ số
\begin{ex} %[1D6C23]
Mật mã mở rương kho báu là một số trong bảng $100$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  % Hòm kho báu
  \draw[fill=brown!80!black, draw=black, line width=0.8pt, rounded corners=3pt] (-1.8,-0.45) rectangle (1.8,0.55);
  \draw[fill=yellow!70!orange, draw=black, line width=0.7pt] (-0.25,-0.1) rectangle (0.25,0.25);
  \fill[black] (0,0.08) circle (0.04cm);
  \node[below, font=\bfseries\scriptsize, color=blue!90!black, align=center] at (0,-0.55) {
    ``Số lớn nhất có hai chữ số mà\\chữ số hàng chục gấp $3$ lần chữ số hàng đơn vị.''
  };
\end{tikzpicture}
\end{center}
Số bí mật để mở hòm kho báu là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$93$}}
\loigiai{
Số có hai chữ số lớn nhất thì chữ số hàng chục phải bằng $9$.\\
Vì hàng chục gấp $3$ lần hàng đơn vị nên chữ số hàng đơn vị là: $9 : 3 = 3$.\\
Vậy số bí mật là $93$.\\
\textbf{Đáp số: $93$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 6 Bai 23
tex_path = os.path.abspath('CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100/Chuong6_Bai23_BangCacSoTu1Den100.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_23_preview.tex độc lập 5 trang
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 23: BẢNG CÁC SỐ TỪ 1 ĐẾN 100},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 6: Các số đến 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-23}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_23_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_23_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_23_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_23_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_23_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_23_Bang_cac_so_tu_1_den_100.pdf')
    import shutil
    shutil.copy2('Bai_23_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
