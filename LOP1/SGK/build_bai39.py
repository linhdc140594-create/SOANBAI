# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 39: ÔN TẬP CÁC SỐ VÀ PHÉP TÍNH TRONG PHẠM VI 100
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D
% =========================================================================

% --- ĐỊNH NGHĨA MÀU SẮC AN TOÀN ---
\colorlet{myteal}{cyan!70!blue}
\colorlet{myorange}{orange}
\colorlet{mypurple}{purple}
\colorlet{myblue}{blue}
\colorlet{myred}{red}

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 39 ---

% 1. Vẽ thanh chục (thanh 10 khối vuông nhỏ)
\providecommand{\VeBamiChinThanhChuc}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}]
    \foreach \k in {0,...,9} {
      \draw[fill=blue!15, draw=blue!80, line width=0.5pt] (0, \k*0.14) rectangle (0.28, \k*0.14 + 0.14);
    }
  \end{scope}
}

% 2. Vẽ khối vuông đơn vị
\providecommand{\VeBamiChinKhoiDonVi}[2]{% #1=x, #2=y
  \draw[fill=orange!25, draw=orange!85, line width=0.5pt] (#1,#2) rectangle (#1+0.28, #2+0.28);
}

% 3. Vẽ ô tính đặt dọc (phép cộng/trừ 2 chữ số thẳng cột)
\providecommand{\VeBamiChinDatTinh}[5]{% #1=(x,y), #2=so1, #3=dau, #4=so2, #5=ketqua
  \begin{scope}[shift={(#1)}]
    \draw[fill=blue!5, draw=blue!70, line width=0.8pt, rounded corners=3pt] (-0.85,-0.9) rectangle (0.85,0.9);
    \node[font=\bfseries\small] at (0.25, 0.5) {#2};
    \node[font=\bfseries\small, color=red!80!black] at (-0.5, 0.05) {#3};
    \node[font=\bfseries\small] at (0.25, 0.05) {#4};
    \draw[line width=1.1pt, black!75] (-0.65,-0.22) -- (0.65,-0.22);
    \node[font=\bfseries\small, color=blue!90!black] at (0.25, -0.55) {#5};
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Cấu tạo số gồm 7 chục và 5 đơn vị
\begin{ex} %[1D10N39]
Quan sát hình biểu diễn gồm các thanh chục và khối đơn vị:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.85]
  % 7 thanh chục
  \foreach \i in {0,...,6} {
    \VeBamiChinThanhChuc{\i*0.42 - 2.8}{-0.7}
  }
  \node[below=2pt, font=\bfseries\scriptsize, color=blue!85!black] at (-1.55,-0.75) {7 chục};
  \draw[dashed, gray!70] (0.3,-0.8) -- (0.3,0.85);
  % 5 khối đơn vị
  \foreach \j in {0,...,4} {
    \VeBamiChinKhoiDonVi{0.65 + \j*0.45}{-0.14}
  }
  \node[below=2pt, font=\bfseries\scriptsize, color=orange!90!black] at (1.55,-0.75) {5 đơn vị};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số gồm $7$ chục và $5$ đơn vị được viết là
\begin{multicols}{4}
\choice
{$57$}
{\True $75$}
{$705$}
{$70$}
\end{multicols}
\loigiai{
Số gồm $7$ chục và $5$ đơn vị là số $75$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Số liền sau trên tia số
\begin{ex} %[1D10N39]
Quan sát dãy số liên tiếp trên tia số dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \draw[->, >=stealth, line width=1.2pt, blue!85!black] (86.5,0) -- (92.5,0);
  \foreach \n in {87,88,89,90,91,92} {
    \draw[line width=1pt, blue!85!black] (\n, 0.15) -- (\n, -0.15);
    \ifnum\n=90
      \node[draw=red!80, fill=yellow!25, line width=1pt, rounded corners=2pt, inner sep=2.5pt] at (\n,-0.55) {\bfseries\small\color{red!90!black} ?};
    \else
      \node[below, font=\bfseries\small, color=black!85] at (\n,-0.18) {\n};
    \fi
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số liền sau của số $89$ là số thích hợp điền vào dấu $[?]$, đó là số
\begin{multicols}{4}
\choice
{$88$}
{\True $90$}
{$91$}
{$80$}
\end{multicols}
\loigiai{
Số liền sau của một số bằng số đó cộng thêm $1$: $89 + 1 = 90$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: So sánh 4 số
\begin{ex} %[1D10H39]
Bốn chú vịt đeo biển số: $48, 84, 39, 93$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \foreach \i/\num/\mau in {1/48/myteal, 2/84/myorange, 3/39/mypurple, 4/93/myblue} {
    \pgfmathsetmacro{\x}{(\i-2.5)*1.9}
    \node[draw=\mau!85, fill=\mau!12, line width=1pt, rounded corners=4pt, inner xsep=8pt, inner ysep=4pt] at (\x,0) {\bfseries\normalsize\color{\mau!90!black} \num};
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Trong các số trên, số lớn nhất là
\begin{multicols}{4}
\choice
{$84$}
{\True $93$}
{$48$}
{$39$}
\end{multicols}
\loigiai{
So sánh các chữ số hàng chục: $3 < 4 < 8 < 9$. Số có chữ số hàng chục lớn nhất là $93$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Phép cộng đặt tính thẳng cột 42 + 35
\begin{ex} %[1D10H39]
Quan sát phép tính cộng đặt tính thẳng cột:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.9]
  \VeBamiChinDatTinh{0,0}{42}{+}{35}{77}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $42 + 35$ là
\begin{multicols}{4}
\choice
{$76$}
{\True $77$}
{$78$}
{$79$}
\end{multicols}
\loigiai{
Cộng từ phải sang trái: $2 + 5 = 7$, $4 + 3 = 7$. Vậy $42 + 35 = 77$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Phép trừ đặt tính thẳng cột 86 - 32
\begin{ex} %[1D10H39]
Quan sát phép tính trừ đặt tính thẳng cột:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.9]
  \VeBamiChinDatTinh{0,0}{86}{-}{32}{54}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $86 - 32$ là
\begin{multicols}{4}
\choice
{$53$}
{\True $54$}
{$55$}
{$56$}
\end{multicols}
\loigiai{
Trừ từ phải sang trái: $6 - 2 = 4$, $8 - 3 = 5$. Vậy $86 - 32 = 54$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Chiếc cân thăng bằng so sánh phép tính
\begin{ex} %[1D10H39]
Chiếc cân thăng bằng có hai đĩa cân mang hai phép tính:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[line width=1.5pt, black!75] (0,0) -- (0,1.4);
  \draw[line width=1.3pt, black!75] (-0.8,0) -- (0.8,0);
  \draw[line width=1.4pt, orange!90!black] (-2.5,1.4) -- (2.5,1.4);
  \fill[red!85!black] (0,1.4) circle (0.1cm);
  % Đĩa trái
  \draw[line width=0.8pt, gray!80] (-2.5,1.4) -- (-3.1,0.7);
  \draw[line width=0.8pt, gray!80] (-2.5,1.4) -- (-1.9,0.7);
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (-2.5,0.45) {\bfseries\small\color{blue!90!black} $56 + 21$};
  % Đĩa phải
  \draw[line width=0.8pt, gray!80] (2.5,1.4) -- (1.9,0.7);
  \draw[line width=0.8pt, gray!80] (2.5,1.4) -- (3.1,0.7);
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (2.5,0.45) {\bfseries\small\color{teal!90!black} $98 - 21$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Dấu thích hợp để điền vào chỗ chấm $56 + 21 \dots 98 - 21$ là
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{$+$}
\end{multicols}
\loigiai{
Ta có $56 + 21 = 77$ và $98 - 21 = 77$. Vì $77 = 77$ nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Biểu thức cộng 3 số
\begin{ex} %[1D10V39]
Sơ đồ tính toán chuỗi phép cộng ba số:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (A) at (-3.2,0) {\bfseries\small\color{blue!90!black} 34};
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (B) at (0,0) {\bfseries\small\color{orange!90!black} 49};
  \node[draw=teal!80, fill=yellow!25, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=3.5pt] (C) at (3.2,0) {\bfseries\small\color{red!90!black} ?};
  \draw[->, >=stealth, line width=1.2pt, orange!85] (A) -- (B) node[midway, above=1pt, font=\bfseries\scriptsize] {+15};
  \draw[->, >=stealth, line width=1.2pt, teal!85] (B) -- (C) node[midway, above=1pt, font=\bfseries\scriptsize] {+20};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị của biểu thức $34 + 15 + 20$ là
\begin{multicols}{4}
\choice
{$68$}
{\True $69$}
{$70$}
{$71$}
\end{multicols}
\loigiai{
Thực hiện lần lượt từ trái sang phải: $34 + 15 = 49$, sau đó $49 + 20 = 69$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Biểu thức trừ 3 số
\begin{ex} %[1D10V39]
Sơ đồ tính toán chuỗi phép trừ ba số:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (A) at (-3.2,0) {\bfseries\small\color{blue!90!black} 78};
  \node[draw=purple!80, fill=purple!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (B) at (0,0) {\bfseries\small\color{purple!90!black} 53};
  \node[draw=teal!80, fill=yellow!25, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=3.5pt] (C) at (3.2,0) {\bfseries\small\color{red!90!black} ?};
  \draw[->, >=stealth, line width=1.2pt, purple!85] (A) -- (B) node[midway, above=1pt, font=\bfseries\scriptsize] {-25};
  \draw[->, >=stealth, line width=1.2pt, teal!85] (B) -- (C) node[midway, above=1pt, font=\bfseries\scriptsize] {-13};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị của biểu thức $78 - 25 - 13$ là
\begin{multicols}{4}
\choice
{$39$}
{\True $40$}
{$41$}
{$42$}
\end{multicols}
\loigiai{
Thực hiện lần lượt từ trái sang phải: $78 - 25 = 53$, sau đó $53 - 13 = 40$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Tìm số chưa biết x - 34 = 45
\begin{ex} %[1D10V39]
Chiếc hộp bí mật chứa một số, khi bớt đi $34$ thì còn lại $45$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=orange!80, fill=yellow!20, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.3,0) {\bfseries\small\color{red!90!black} [ ? ]};
  \node[draw=blue!80, fill=blue!10, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (2.3,0) {\bfseries\small\color{blue!90!black} Còn lại: 45};
  \draw[->, >=stealth, line width=1.2pt, red!85!black] (A) -- (B) node[midway, above=2pt, font=\bfseries\tiny, color=red!90!black] {Bớt đi 34};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số thích hợp điền vào ô $[?]$ là
\begin{multicols}{4}
\choice
{$78$}
{\True $79$}
{$80$}
{$81$}
\end{multicols}
\loigiai{
Muốn tìm số ban đầu, ta lấy số còn lại cộng với số đã bớt: $45 + 34 = 79$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Đàn gà có gà mái và gà trống
\begin{ex} %[1D10V39]
Trang trại có hai khu nuôi gà gồm $45$ con gà mái và $23$ con gà trống:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-2.2,0) {\bfseries\small\color{orange!90!black} 45 con gà mái};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (2.2,0) {\bfseries\small\color{teal!90!black} 23 con gà trống};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tổng số con gà trong trang trại là
\begin{multicols}{4}
\choice
{$67$ con}
{\True $68$ con}
{$69$ con}
{$70$ con}
\end{multicols}
\loigiai{
Tổng số con gà là: $45 + 23 = 68$ con gà.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Đọc sách còn lại
\begin{ex} %[1D10V39]
Thanh tiến trình đọc sách: quyển truyện dài $96$ trang, Lan đã đọc $52$ trang:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.85]
  % Đoạn đã đọc
  \draw[fill=green!25, draw=green!70!black, line width=1pt, rounded corners=2pt] (-3.0,-0.35) rectangle (0.2,0.35);
  \node[font=\bfseries\scriptsize, color=green!70!black] at (-1.4,0) {Đã đọc 52 trang};
  % Đoạn còn lại
  \draw[fill=orange!20, draw=orange!80, line width=1pt, rounded corners=2pt] (0.3,-0.35) rectangle (3.0,0.35);
  \node[font=\bfseries\scriptsize, color=orange!90!black] at (1.65,0) {Còn lại: ? trang};
  % Tổng thể
  \node[above=3pt, font=\bfseries\footnotesize, color=blue!90!black] at (0,0.4) {Cả quyển truyện: 96 trang};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi Lan còn phải đọc bao nhiêu trang nữa để hết quyển truyện?
\begin{multicols}{4}
\choice
{$43$ trang}
{\True $44$ trang}
{$45$ trang}
{$46$ trang}
\end{multicols}
\loigiai{
Số trang truyện Lan còn phải đọc là: $96 - 52 = 44$ trang.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Tính nhanh nhóm tròn chục
\begin{ex} %[1D10C39]
Bốn thẻ số cần ghép cặp để tính nhanh:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (N1) at (-3.0,0) {\bfseries\small\color{blue!90!black} 25};
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (N2) at (-1.0,0) {\bfseries\small\color{orange!90!black} 32};
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (N3) at (1.0,0) {\bfseries\small\color{blue!90!black} 15};
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (N4) at (3.0,0) {\bfseries\small\color{orange!90!black} 28};
  \draw[<->, >=stealth, line width=1pt, blue!80] (N1.south) to[bend right=35] node[midway, below=1pt, font=\tiny\bfseries, color=blue!80] {40} (N3.south);
  \draw[<->, >=stealth, line width=1pt, orange!80] (N2.north) to[bend left=35] node[midway, above=1pt, font=\tiny\bfseries, color=orange!80] {60} (N4.north);
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị của biểu thức $25 + 32 + 15 + 28$ là
\begin{multicols}{4}
\choice
{$90$}
{\True $100$}
{$95$}
{$85$}
\end{multicols}
\loigiai{
Nhóm các số có chữ số tận cùng cộng lại tròn chục:\\
$(25 + 15) + (32 + 28) = 40 + 60 = 100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Các phép tính phạm vi 100
\begin{ex} %[1D10H39]
Quan sát bảng các phép tính trong phạm vi 100:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \node[draw=blue!75, fill=blue!8, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-3.4,0) {\bfseries\small $35 + 43 = 78$};
  \node[draw=orange!75, fill=orange!8, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (0,0) {\bfseries\small $89 - 45 = 44$};
  \node[draw=teal!75, fill=teal!8, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (3.4,0) {\bfseries\small $60 + 30 = 90$};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Phép tính $35 + 43 = 78$ là đúng.}
{\True Phép tính $89 - 45 = 44$ là đúng.}
{Phép tính $60 + 30 = 80$ là đúng.}
{\True Phép tính $76 - 20 = 56$ là đúng.}
\loigiai{\textbf{a)} Đúng ($35 + 43 = 78$). \textbf{b)} Đúng ($89 - 45 = 44$). \textbf{c)} Sai (Vì $60 + 30 = 90 \neq 80$). \textbf{d)} Đúng ($76 - 20 = 56$).}
\end{ex}

% CÂU 14: Tính chất các số 25, 82, 49, 60
\begin{ex} %[1D10V39]
Bốn chú chim mang các số: $25, 82, 49, 60$:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \draw[->, >=stealth, line width=1pt, blue!70] (-0.3,0) -- (7.5,0);
  \foreach \n in {20, 30, 40, 50, 60, 70, 80, 90} {
    \pgfmathsetmacro{\x}{(\n - 20)*0.1}
    \draw[line width=0.6pt, blue!50] (\x, 0.08) -- (\x, -0.08);
    \node[below, font=\tiny, color=gray!80] at (\x,-0.08) {\n};
  }
  \foreach \n/\lbl/\mau in {25/25/myteal, 49/49/myorange, 60/60/mypurple, 82/82/myblue} {
    \pgfmathsetmacro{\x}{(\n - 20)*0.1}
    \draw[line width=1.1pt, \mau!85] (\x, 0.15) -- (\x, -0.15);
    \node[draw=\mau!80, fill=\mau!12, line width=0.8pt, rounded corners=2pt, inner sep=2pt] at (\x, 0.45) {\bfseries\scriptsize \lbl};
  }
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True Số lớn nhất trong các số đã cho là 82.}
{\True Số bé nhất trong các số đã cho là 25.}
{Sắp xếp các số theo thứ tự từ bé đến lớn là $82, 60, 49, 25$.}
{\True Hiệu giữa số lớn nhất và số bé nhất là $82 - 25 = 57$.}
\loigiai{\textbf{a)} Đúng (82 lớn nhất). \textbf{b)} Đúng (25 bé nhất). \textbf{c)} Sai (Thứ tự từ bé đến lớn đúng là $25, 49, 60, 82$). \textbf{d)} Đúng ($82 - 25 = 57$).}
\end{ex}

% CÂU 15: Độ dài và đơn vị đo cm
\begin{ex} %[1D10H39]
Thước đo cm dùng để đo độ dài các đoạn thẳng:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.85]
  \draw[fill=yellow!15, draw=orange!85, line width=1.1pt, rounded corners=2pt] (-0.4,-0.35) rectangle (7.6,0.35);
  \foreach \x in {0,1,...,7} {
    \draw[line width=0.8pt, orange!90!black] (\x,0.15) -- (\x,0.35);
    \pgfmathtruncatemacro{\cm}{\x * 10}
    \node[font=\tiny\bfseries, color=brown!80!black] at (\x,-0.08) {\cm};
  }
  \node[font=\bfseries\tiny, color=orange!90!black] at (7.2,0.18) {cm};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True $45\text{ cm} + 34\text{ cm} = 79\text{ cm}$.}
{\True $98\text{ cm} - 43\text{ cm} = 55\text{ cm}$.}
{$1\text{ m} = 10\text{ cm}$.}
{\True $50\text{ cm} + 50\text{ cm} = 100\text{ cm}$.}
\loigiai{\textbf{a)} Đúng ($45 + 34 = 79\text{ cm}$). \textbf{b)} Đúng ($98 - 43 = 55\text{ cm}$). \textbf{c)} Sai (Vì $1\text{ m} = 100\text{ cm} \neq 10\text{ cm}$). \textbf{d)} Đúng ($50\text{ cm} + 50\text{ cm} = 100\text{ cm}$).}
\end{ex}

% CÂU 16: Cấu tạo số có hai chữ số
\begin{ex} %[1D10H39]
Ngôi nhà số mang các đặc điểm về số tròn chục và số có hai chữ số:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \node[draw=purple!75, fill=purple!8, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (-3.6,0) {\bfseries\scriptsize 99 liền trước 100};
  \node[draw=blue!75, fill=blue!8, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (0,0) {\bfseries\scriptsize 70 = 7 chục};
  \node[draw=teal!75, fill=teal!8, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (3.6,0) {\bfseries\scriptsize 90 tròn chục lớn nhất};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True Số liền trước của số 100 là số 99.}
{\True Số 70 gồm 7 chục và 0 đơn vị.}
{\True Số tròn chục lớn nhất có hai chữ số là 90.}
{Số có hai chữ số giống nhau bé nhất là 22.}
\loigiai{\textbf{a)} Đúng ($100 - 1 = 99$). \textbf{b)} Đúng (Hàng chục là 7, hàng đơn vị là 0). \textbf{c)} Đúng ($90$ là số tròn chục lớn nhất $< 100$). \textbf{d)} Sai (Số có hai chữ số giống nhau bé nhất là 11, không phải 22).}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Phép cộng quả táo hai cây
\begin{ex} %[1D10N39]
Vườn nhà bác An có hai cây táo, cây thứ nhất có $53$ quả, cây thứ hai có $34$ quả:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-1.8,0) {\bfseries\small\color{orange!90!black} 53 quả táo};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (1.8,0) {\bfseries\small\color{orange!90!black} 34 quả táo};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi cả hai cây táo có tất cả bao nhiêu quả?
\shortans{87}
\loigiai{
Cả hai cây có tất cả số quả táo là: $53 + 34 = 87$ quả.\\
\textbf{Đáp số:} $87$.
}
\end{ex}

% CÂU 18: Tìm x: x + 23 = 78
\begin{ex} %[1D10H39]
Chiếc cân thăng bằng có hai đĩa cân đặt hai bên:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[line width=1.5pt, black!75] (0,0) -- (0,1.3);
  \draw[line width=1.3pt, black!75] (-0.8,0) -- (0.8,0);
  \draw[line width=1.4pt, orange!90!black] (-2.2,1.3) -- (2.2,1.3);
  \fill[red!85!black] (0,1.3) circle (0.1cm);
  % Đĩa trái
  \draw[line width=0.8pt, gray!80] (-2.2,1.3) -- (-2.8,0.65);
  \draw[line width=0.8pt, gray!80] (-2.2,1.3) -- (-1.6,0.65);
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (-2.2,0.4) {\bfseries\small\color{blue!90!black} $[ ? ] + 23$};
  % Đĩa phải
  \draw[line width=0.8pt, gray!80] (2.2,1.3) -- (1.6,0.65);
  \draw[line width=0.8pt, gray!80] (2.2,1.3) -- (2.8,0.65);
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=3pt] at (2.2,0.4) {\bfseries\small\color{teal!90!black} 78};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tìm số thích hợp điền vào ô $[?]$ để cân thăng bằng:
\shortans{55}
\loigiai{
Số cần điền là: $78 - 23 = 55$.\\
\textbf{Đáp số:} $55$.
}
\end{ex}

% CÂU 19: Bán bò trang trại
\begin{ex} %[1D10V39]
Trang trại có $56$ con bò, bác nông dân đã bán đi $24$ con:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.3,0) {\bfseries\small\color{blue!90!black} 56 con bò};
  \node[draw=red!80, fill=yellow!20, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (2.3,0) {\bfseries\small\color{red!90!black} Còn lại: ?};
  \draw[->, >=stealth, line width=1.3pt, red!85!black] (A) -- (B) node[midway, above=2pt, font=\bfseries\tiny, color=red!90!black] {Bán đi 24 con};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi trong trang trại còn lại bao nhiêu con bò?
\shortans{32}
\loigiai{
Số con bò còn lại trong trang trại là: $56 - 24 = 32$ con bò.\\
\textbf{Đáp số:} $32$.
}
\end{ex}

% CÂU 20: Tính nhanh 4 số
\begin{ex} %[1D10C39]
Tính nhanh giá trị biểu thức gồm bốn số:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=blue!85, fill=blue!15, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (A) at (-3.0,0) {\bfseries\normalsize\color{blue!90!black} 12};
  \node[draw=orange!85, fill=orange!15, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (B) at (-1.0,0) {\bfseries\normalsize\color{orange!90!black} 34};
  \node[draw=blue!85, fill=blue!15, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (C) at (1.0,0) {\bfseries\normalsize\color{blue!90!black} 48};
  \node[draw=orange!85, fill=orange!15, line width=1pt, rounded corners=3pt, inner xsep=7pt, inner ysep=3.5pt] (D) at (3.0,0) {\bfseries\normalsize\color{orange!90!black} 6};
  \draw[<->, >=stealth, line width=1.1pt, blue!80] (A.south) to[bend right=35] node[midway, below=1pt, font=\tiny\bfseries, color=blue!80] {60} (C.south);
  \draw[<->, >=stealth, line width=1.1pt, orange!80] (B.north) to[bend left=35] node[midway, above=1pt, font=\tiny\bfseries, color=orange!80] {40} (D.north);
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị của biểu thức $12 + 34 + 48 + 6$ là bao nhiêu?
\shortans{100}
\loigiai{
Tính nhanh bằng cách nhóm các số tròn chục:\\
$(12 + 48) + (34 + 6) = 60 + 40 = 100$.\\
\textbf{Đáp số:} $100$.
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
    {\large\bfseries\color{red!85!black}BÀI 39: ÔN TẬP CÁC SỐ VÀ PHÉP TÍNH PV 100}\\[2pt]
    {\scriptsize\itshape Thời gian làm bài: 35 phút -- Đề gồm 20 câu chuẩn 5 trang}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.14\textwidth}
    \centering
    \qrcode[height=1.35cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-39}\\[2pt]
    {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
  \end{minipage}
\end{tcolorbox}
\vspace{1mm}

''' + content + r'''
\end{document}
'''

with open("Bai_39_preview.tex", "w", encoding="utf-8") as f:
    f.write(preview_tex)

# Lưu nội dung vào file chương chính
target_chapter = r"CHỦ ĐỀ 10 - ÔN TẬP CUỐI NĂM\Chuong10_Bai39_OnTapCacSoVaPhepTinhPhamVi100.tex"
with open(target_chapter, "w", encoding="utf-8") as f:
    f.write(content)

print("Đã tạo Bai_39_preview.tex và cập nhật " + target_chapter)
