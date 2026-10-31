# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 21: SỐ CÓ HAI CHỮ SỐ (CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100 - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 21 ---

% 1. Bó 10 que tính (1 chục) buộc dây nơ
\providecommand{\VeBoQueTinh}[2][red]{% #1=màu nơ, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.75]
    \foreach \i in {-0.24, -0.18, -0.12, -0.06, 0, 0.06, 0.12, 0.18, 0.24} {
      \draw[fill=yellow!35!brown, draw=brown!80!black, line width=0.4pt, rounded corners=0.5pt] 
        (\i-0.03, -0.7) rectangle (\i+0.03, 0.7);
    }
    \draw[fill=#1, draw=black!80, line width=0.6pt] (-0.32,-0.1) rectangle (0.32,0.1);
    \fill[#1!90!black] (-0.12,0) circle (0.08cm);
    \fill[#1!90!black] (0.12,0) circle (0.08cm);
    \fill[yellow!90!orange] (0,0) circle (0.05cm);
  \end{scope}
}

% 2. Que tính đơn lẻ (đơn vị)
\providecommand{\VeQueRoi}[4][30]{% #1=góc nghiêng, #2=x, #3=y, #4=màu
  \begin{scope}[shift={(#2,#3)}, rotate=#1, scale=0.75]
    \draw[fill=#4, draw=brown!80!black, line width=0.4pt, rounded corners=0.5pt] 
      (-0.03,-0.7) rectangle (0.03,0.7);
  \end{scope}
}

% 3. Thanh 10 khối lập phương (1 chục) 3D
\providecommand{\VeThanhChucKhoi}[2][orange!65]{% #1=màu, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.48]
    \foreach \k in {0,1,2,3,4,5,6,7,8,9} {
      \pgfmathsetmacro{\yy}{\k*0.35}
      \draw[fill=#1, draw=black!75, line width=0.4pt] (0,\yy) rectangle (0.35,\yy+0.35);
      \draw[fill=black!25!#1, draw=black!75, line width=0.4pt] 
        (0.35,\yy) -- (0.50,\yy+0.12) -- (0.50,\yy+0.47) -- (0.35,\yy+0.35) -- cycle;
    }
    \draw[fill=white!40!#1, draw=black!75, line width=0.4pt] 
      (0,3.5) -- (0.35,3.5) -- (0.50,3.62) -- (0.15,3.62) -- cycle;
  \end{scope}
}

% 4. Khối lập phương 3D đơn lẻ
\providecommand{\VeKhoiRoi}[4][orange!65]{% #1=màu, #2=x, #3=y, #4=scale
  \begin{scope}[shift={(#2,#3)}, scale=#4]
    \draw[fill=#1, draw=black!75, line width=0.4pt] (0,0) rectangle (0.35,0.35);
    \draw[fill=white!40!#1, draw=black!75, line width=0.4pt] (0,0.35) -- (0.35,0.35) -- (0.50,0.47) -- (0.15,0.47) -- cycle;
    \draw[fill=black!25!#1, draw=black!75, line width=0.4pt] (0.35,0) -- (0.50,0.12) -- (0.50,0.47) -- (0.35,0.35) -- cycle;
  \end{scope}
}

% 5. Túi kẹo 10 chiếc và kẹo rời
\providecommand{\VeTuiKeoMuoi}[2][pink!70!purple]{% #1=màu túi, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.6]
    \shadedraw[left color=#1!80!white, right color=#1!90!black, draw=purple!80!black, line width=0.6pt, rounded corners=5pt]
      (-0.55,-0.65) rectangle (0.55,0.5);
    \draw[fill=yellow, draw=orange!90!black, line width=0.5pt] (-0.3,0.5) .. controls (0,0.4) .. (0.3,0.5) -- (0.4,0.75) -- (-0.4,0.75) -- cycle;
    \node[font=\bfseries\small, color=white] at (0,-0.05) {10};
  \end{scope}
}

\providecommand{\VeKeoRoi}[3][cyan]{% #1=màu kẹo, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.42]
    \fill[#1!85!black] (0,0) circle (0.22cm);
    \fill[white!30!#1] (0,0) circle (0.14cm);
    \fill[#1!70!black] (-0.18,0) -- (-0.36,0.14) -- (-0.36,-0.14) -- cycle;
    \fill[#1!70!black] (0.18,0) -- (0.36,0.14) -- (0.36,-0.14) -- cycle;
  \end{scope}
}

% 6. Vỉ 10 quả trứng
\providecommand{\VeViMuoiTrung}[1]{% #1=(x,y)
  \begin{scope}[shift={(#1)}, scale=0.52]
    \draw[fill=blue!10, draw=blue!70!black, line width=0.7pt, rounded corners=3pt] (-1.2,-0.55) rectangle (1.2,0.55);
    \foreach \col in {-0.9, -0.45, 0, 0.45, 0.9} {
      \foreach \row in {-0.22, 0.22} {
        \draw[fill=orange!25!yellow, draw=brown!80!black, line width=0.4pt] 
          (\col, \row) ellipse (0.16cm and 0.2cm);
      }
    }
  \end{scope}
}

\providecommand{\VeTrungRoi}[2]{% #1=x, #2=y
  \begin{scope}[shift={(#1,#2)}, scale=0.52]
    \draw[fill=orange!30!yellow, draw=brown!80!black, line width=0.5pt] (0,0) ellipse (0.16cm and 0.22cm);
  \end{scope}
}

% 7. Vòng 10 hạt ngọc xâu chuỗi
\providecommand{\VeVongMuoiHat}[2][cyan!70]{% #1=màu hạt, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.52]
    \draw[gray!60, line width=0.7pt] (0,0) circle (0.7cm);
    \foreach \a in {0,36,72,108,144,180,216,252,288,324} {
      \fill[#1, draw=black!70, line width=0.35pt] (\a:0.7cm) circle (0.13cm);
      \fill[white!60!#1] ({\a+15}:0.68cm) circle (0.035cm);
    }
  \end{scope}
}

\providecommand{\VeHatRoi}[3][cyan!70]{% #1=màu, #2=x, #3=y
  \begin{scope}[shift={(#2,#3)}, scale=0.52]
    \fill[#1, draw=black!70, line width=0.4pt] (0,0) circle (0.14cm);
    \fill[white!70!#1] (0.04,0.04) circle (0.035cm);
  \end{scope}
}

% 8. Bạn nhỏ cầm bảng số
\providecommand{\VeBanNhoCamBang}[4][teal]{% #1=màu áo, #2=(x,y), #3=tên, #4=số
  \begin{scope}[shift={(#2)}, scale=0.75]
    \fill[orange!25!yellow] (0,1.15) circle (0.3cm);
    \fill[brown!70!black] (0,1.35) arc (40:220:0.32cm) -- cycle;
    \fill[black] (-0.09,1.15) circle (0.025cm);
    \fill[black] (0.09,1.15) circle (0.025cm);
    \draw[red!80!black, line width=0.5pt] (-0.07,1.03) arc (190:350:0.07cm);
    \draw[fill=#1, draw=black!70, line width=0.5pt] (-0.28,0.4) rectangle (0.28,0.85);
    \draw[orange!25!yellow, line width=1.6pt] (-0.28,0.68) -- (-0.42,0.4);
    \draw[orange!25!yellow, line width=1.6pt] (0.28,0.68) -- (0.42,0.4);
    \draw[blue!70!black, line width=2pt] (-0.13,0.4) -- (-0.13,0);
    \draw[blue!70!black, line width=2pt] (0.13,0.4) -- (0.13,0);
    \node[below, font=\bfseries\scriptsize] at (0,-0.05) {#3};
    \draw[fill=yellow!20, draw=orange!90!black, line width=0.8pt, rounded corners=2pt] (-0.45,0.2) rectangle (0.45,0.72);
    \node[font=\bfseries\large, color=red!85!black] at (0,0.46) {#4};
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Đọc và viết số có hai chữ số từ que tính
\begin{ex} %[1D6N21]
Quan sát hình ảnh các bó que tính và que tính rời dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \VeBoQueTinh[red]{0,0}
  \node[below, font=\scriptsize\bfseries, color=blue!80!black] at (0,-0.7) {1 chục};
  \node[font=\bfseries\normalsize, color=purple] at (1.1,0) {và};
  \begin{scope}[shift={(2.2,0)}]
    \VeQueRoi[-10]{-0.3}{0}{yellow!40!brown}
    \VeQueRoi[5]{-0.15}{0}{yellow!40!brown}
    \VeQueRoi[0]{0}{0}{yellow!40!brown}
    \VeQueRoi[-8]{0.15}{0}{yellow!40!brown}
    \VeQueRoi[12]{0.3}{0}{yellow!40!brown}
    \node[below, font=\scriptsize\bfseries, color=brown!80!black] at (0,-0.7) {5 que rời};
  \end{scope}
\end{tikzpicture}
\end{center}
Hình trên gồm có 1 chục và 5 que tính rời. Số này được đọc và viết là:
\begin{multicols}{2}
\choice
{Năm mươi mốt (viết là $51$)}
{\True Mười lăm (viết là $15$)}
{Một trăm linh năm (viết là $105$)}
{Năm mươi (viết là $50$)}
\end{multicols}
\loigiai{
Có 1 chục và 5 đơn vị tạo thành số 15, đọc là "mười lăm".\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 2: Đọc số 24 và viết chữ số
\begin{ex} %[1D6N21]
Bạn Nam cầm tấm bảng ghi số dưới đây:
\begin{center}
\begin{tikzpicture}
  \VeBanNhoCamBang[blue!60!cyan]{0,0}{Nam}{$24$}
  \node[right, align=left, font=\normalsize] at (0.8,0.45) {
    Gồm: \textbf{2 chục} và \textbf{4 đơn vị} $\to$ Đọc là: \textbf{?}
  };
\end{tikzpicture}
\end{center}
Số $24$ trên bảng của bạn Nam được đọc đúng là:
\begin{multicols}{2}
\choice
{Hai mươi}
{\True Hai mươi tư (hoặc hai mươi bốn)}
{Bốn mươi hai}
{Hai mươi mốt}
\end{multicols}
\loigiai{
Số $24$ gồm 2 chục và 4 đơn vị, đọc là "hai mươi tư" hoặc "hai mươi bốn".\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 3: Cấu tạo số gồm 3 chục và 5 đơn vị qua thanh khối lập phương
\begin{ex} %[1D6H21]
Hình ảnh dưới đây gồm 3 thanh chục và 5 khối lập phương rời:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \VeThanhChucKhoi[orange!75]{0,0}
  \VeThanhChucKhoi[orange!75]{0.45,0}
  \VeThanhChucKhoi[orange!75]{0.9,0}
  \node[below, font=\scriptsize\bfseries, color=orange!90!black] at (0.65,-0.05) {3 chục (30 khối)};
  \node[font=\bfseries\normalsize, color=purple] at (1.8,0.8) {và};
  \begin{scope}[shift={(2.5,0.15)}]
    \VeKhoiRoi[cyan!65]{0}{0}{0.45}
    \VeKhoiRoi[cyan!65]{0.35}{0}{0.45}
    \VeKhoiRoi[cyan!65]{0.7}{0}{0.45}
    \VeKhoiRoi[cyan!65]{0.18}{0.32}{0.45}
    \VeKhoiRoi[cyan!65]{0.53}{0.32}{0.45}
    \node[below, font=\scriptsize\bfseries, color=cyan!80!black] at (0.35,-0.25) {5 đơn vị};
  \end{scope}
\end{tikzpicture}
\end{center}
Số gồm $3$ chục và $5$ đơn vị là số nào?
\begin{multicols}{4}
\choice
{$53$}
{\True $35$}
{$305$}
{$30$}
\end{multicols}
\loigiai{
Số gồm 3 chục và 5 đơn vị được viết là $35$ (đọc là ba mươi lăm).\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 4: Vị trí hàng chục và hàng đơn vị của số 48
\begin{ex} %[1D6H21]
\noindent
\begin{minipage}{0.42\textwidth}
  \centering
  \begin{tikzpicture}[scale=0.55]
    \draw[fill=red!70, draw=black!80, line width=0.8pt] (0,1.3) -- (1.6,2.2) -- (3.2,1.3) -- cycle;
    \node[font=\bfseries\scriptsize, color=white] at (1.6,1.7) {SỐ 48};
    \draw[fill=yellow!15, draw=black!80, line width=0.8pt] (0,0) rectangle (3.2,1.3);
    \draw[black!70, line width=0.7pt, dashed] (1.6,0) -- (1.6,1.3);
    \node[font=\bfseries\scriptsize, color=blue!80!black] at (0.8,0.95) {Hàng chục};
    \node[font=\bfseries\scriptsize, color=green!60!black] at (2.4,0.95) {Hàng ĐV};
    \node[font=\bfseries\Large, color=red!80!black] at (0.8,0.4) {4};
    \node[font=\bfseries\Large, color=green!60!black] at (2.4,0.4) {8};
  \end{tikzpicture}
\end{minipage}%
\begin{minipage}{0.57\textwidth}
  Trong số $48$, chữ số $4$ đứng ở hàng nào?
  \begin{multicols}{2}
  \choice
  {Hàng đơn vị}
  {\True Hàng chục}
  {Hàng trăm}
  {Hàng phần mười}
  \end{multicols}
\end{minipage}
\loigiai{
Trong số có hai chữ số, chữ số đầu tiên bên trái là chữ số hàng chục. Vậy chữ số 4 ở hàng chục.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Số liền sau của số 39 qua tia số đoàn tàu
\begin{ex} %[1D6H21]
Đoàn tàu hỏa đang chạy trên đường ray mang các số liên tiếp:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[fill=purple!60, draw=black!80, line width=0.7pt, rounded corners=3pt] (-2.2,0) rectangle (-1.2,1.1);
  \draw[fill=cyan!30, draw=black!80, line width=0.5pt] (-2.0,0.55) rectangle (-1.4,0.95);
  \draw[fill=black!80] (-1.9,-0.12) circle (0.15cm);
  \draw[fill=black!80] (-1.4,-0.12) circle (0.15cm);
  \draw[line width=1.2pt] (-1.2,0.35) -- (-0.8,0.35);
  \draw[fill=orange!50, draw=black!80, line width=0.7pt, rounded corners=2pt] (-0.8,0) rectangle (0.6,0.95);
  \node[font=\bfseries\large, color=black] at (-0.1,0.45) {38};
  \draw[fill=black!80] (-0.5,-0.12) circle (0.14cm);
  \draw[fill=black!80] (0.3,-0.12) circle (0.14cm);
  \draw[line width=1.2pt] (0.6,0.35) -- (1.0,0.35);
  \draw[fill=yellow!50, draw=black!80, line width=0.7pt, rounded corners=2pt] (1.0,0) rectangle (2.4,0.95);
  \node[font=\bfseries\large, color=black] at (1.7,0.45) {39};
  \draw[fill=black!80] (1.3,-0.12) circle (0.14cm);
  \draw[fill=black!80] (2.1,-0.12) circle (0.14cm);
  \draw[line width=1.2pt] (2.4,0.35) -- (2.8,0.35);
  \draw[fill=red!25, draw=red!80!black, line width=1pt, rounded corners=2pt] (2.8,0) rectangle (4.2,0.95);
  \node[font=\bfseries\LARGE, color=red!85!black] at (3.5,0.45) {?};
  \draw[fill=black!80] (3.1,-0.12) circle (0.14cm);
  \draw[fill=black!80] (3.9,-0.12) circle (0.14cm);
\end{tikzpicture}
\end{center}
Số liền sau của số $39$ cần điền vào toa tàu có dấu ``$?$'' là số nào?
\begin{multicols}{4}
\choice
{$38$}
{\True $40$}
{$41$}
{$30$}
\end{multicols}
\loigiai{
Số liền sau của $39$ là $39 + 1 = 40$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 6: Số liền trước của số 50
\begin{ex} %[1D6H21]
Bạn Mai xếp các thẻ số theo thứ tự tăng dần từ trái sang phải:
\begin{center}
\begin{tikzpicture}
  \VeBanNhoCamBang[pink!70!purple]{0,0}{Mai}{?}
  \begin{scope}[shift={(1.8,0.3)}]
    \node[draw=orange!80!black, fill=yellow!30, rounded corners=3pt, inner sep=5pt, align=center] (the50) {
      \textbf{\Large\textcolor{blue!80!black}{50}}\\
      \scriptsize\textbf{Số đã cho}
    };
  \end{scope}
  \node[right=0.3cm of the50, align=left, font=\normalsize] {
    Thẻ của Mai là \textbf{số liền trước}\\
    ngay trước số $50$.
  };
\end{tikzpicture}
\end{center}
Số liền trước của số $50$ là số nào?
\begin{multicols}{4}
\choice
{$51$}
{\True $49$}
{$48$}
{$40$}
\end{multicols}
\loigiai{
Số liền trước của $50$ là số đứng ngay trước nó, bớt đi 1: $50 - 1 = 49$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 7: Số tròn chục liền sau số 60
\begin{ex} %[1D6V21]
Các chú ếch nhảy qua các lá sen tròn chục từ bé đến lớn:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[fill=green!45!lime, draw=green!70!black, line width=0.8pt] (0,0) ellipse (0.7cm and 0.35cm);
  \node[font=\bfseries\small, color=white] at (0,0) {40};
  \draw[->, >=stealth, line width=0.8pt, blue!70] (0.75,0.15) to[bend left=30] (1.45,0.15);
  \draw[fill=green!50!lime, draw=green!70!black, line width=0.8pt] (2.2,0) ellipse (0.7cm and 0.35cm);
  \node[font=\bfseries\small, color=white] at (2.2,0) {50};
  \draw[->, >=stealth, line width=0.8pt, blue!70] (2.95,0.15) to[bend left=30] (3.65,0.15);
  \draw[fill=green!55!lime, draw=green!70!black, line width=0.8pt] (4.4,0) ellipse (0.7cm and 0.35cm);
  \node[font=\bfseries\small, color=white] at (4.4,0) {60};
  \draw[->, >=stealth, line width=1pt, red!70] (5.15,0.15) to[bend left=30] (5.85,0.15);
  \draw[fill=yellow!30, draw=red!80!black, line width=1pt] (6.6,0) ellipse (0.7cm and 0.35cm);
  \node[font=\bfseries\large, color=red!80!black] at (6.6,0) {?};
\end{tikzpicture}
\end{center}
Số tròn chục liền sau của số $60$ cần điền vào lá sen có dấu ``$?$'' là:
\begin{multicols}{4}
\choice
{$61$}
{\True $70$}
{$50$}
{$80$}
\end{multicols}
\loigiai{
Các số tròn chục đếm tiếp thêm 10: $40, 50, 60, 70$. Vậy số tròn chục liền sau 60 là 70.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 8: Số lớn nhất có hai chữ số
\begin{ex} %[1D6V21]
Một chiếc bảng đố vui có hình vẽ chứa số lớn nhất có hai chữ số:
\begin{center}
\begin{tikzpicture}
  \node[draw=orange!90!black, fill=yellow!20, rounded corners=6pt, inner sep=6pt, align=center] {
    \textbf{\small\textcolor{blue!85!black}{ĐỐ BẠN TÌM ĐƯỢC}}\\[1mm]
    \footnotesize Số lớn nhất có 2 chữ số là:\\[1mm]
    \tikz{\node[draw=red!70!black, fill=white, rounded corners=2pt, inner sep=2pt, font=\bfseries\large, text=red!80!black] {~?~};}
  };
\end{tikzpicture}
\end{center}
Số lớn nhất có hai chữ số là số nào dưới đây?
\begin{multicols}{4}
\choice
{$90$}
{\True $99$}
{$100$}
{$98$}
\end{multicols}
\loigiai{
Số có hai chữ số lớn nhất là số gồm 9 chục và 9 đơn vị: $99$ (sau 99 là 100 có 3 chữ số).\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Đếm vỉ 10 quả trứng và quả rời
\begin{ex} %[1D6N21]
Mẹ mua các vỉ trứng và một số quả trứng lẻ để làm bánh:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \VeViMuoiTrung{0,0}
  \VeViMuoiTrung{2.6,0}
  \node[below, font=\scriptsize\bfseries, color=blue!80!black] at (1.3,-0.6) {2 vỉ (mỗi vỉ 10 quả)};
  \node[font=\bfseries\normalsize, color=purple] at (4.1,0) {và};
  \begin{scope}[shift={(5.0,0)}]
    \VeTrungRoi{-0.35}{0}
    \VeTrungRoi{0}{0.2}
    \VeTrungRoi{0.35}{-0.08}
    \node[below, font=\scriptsize\bfseries, color=brown!80!black] at (0,-0.4) {3 quả lẻ};
  \end{scope}
\end{tikzpicture}
\end{center}
Tổng số quả trứng mẹ đã mua là:
\begin{multicols}{4}
\choice
{$32$ quả trứng}
{\True $23$ quả trứng}
{$20$ quả trứng}
{$5$ quả trứng}
\end{multicols}
\loigiai{
Mẹ có 2 vỉ (tức là 2 chục quả trứng = 20) và 3 quả lẻ. Tổng cộng: $20 + 3 = 23$ quả trứng.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 10: Túi kẹo 10 viên và kẹo lẻ
\begin{ex} %[1D6H21]
Trong ngày sinh nhật, cô giáo phát kẹo cho các bạn:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \VeTuiKeoMuoi[pink!80!purple]{0,0}
  \VeTuiKeoMuoi[pink!80!purple]{1.2,0}
  \VeTuiKeoMuoi[pink!80!purple]{2.4,0}
  \VeTuiKeoMuoi[pink!80!purple]{3.6,0}
  \node[below, font=\scriptsize\bfseries, color=purple!80!black] at (1.8,-0.65) {4 túi kẹo (mỗi túi 10 viên)};

  \node[font=\bfseries\normalsize, color=purple] at (4.7,0) {và};

  \begin{scope}[shift={(5.6,0)}]
    \VeKeoRoi[cyan]{-0.25}{0.25}
    \VeKeoRoi[orange]{0.25}{0.25}
    \VeKeoRoi[yellow]{-0.25}{-0.1}
    \VeKeoRoi[green]{0.25}{-0.1}
    \VeKeoRoi[purple]{-0.25}{-0.45}
    \VeKeoRoi[red]{0.25}{-0.45}
    \node[below, font=\scriptsize\bfseries, color=blue!80!black] at (0,-0.65) {6 viên kẹo rời};
  \end{scope}
\end{tikzpicture}
\end{center}
Tổng cộng cô giáo có bao nhiêu viên kẹo?
\begin{multicols}{4}
\choice
{$64$ viên kẹo}
{\True $46$ viên kẹo}
{$40$ viên kẹo}
{$10$ viên kẹo}
\end{multicols}
\loigiai{
Có 4 túi kẹo (4 chục = 40 viên) và 6 viên kẹo rời. Số kẹo gồm 4 chục và 6 đơn vị là $46$ viên.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 11: Chuỗi hạt vòng 10 hạt
\begin{ex} %[1D6H21]
Bạn Lan xâu các chuỗi vòng hạt ngọc lấp lánh:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \VeVongMuoiHat[cyan!70]{0,0}
  \VeVongMuoiHat[cyan!70]{1.7,0}
  \VeVongMuoiHat[cyan!70]{3.4,0}
  \node[below, font=\scriptsize\bfseries, color=blue!70!black] at (1.7,-0.8) {3 chuỗi hạt (mỗi chuỗi 10 hạt)};
  \node[font=\bfseries\normalsize, color=purple] at (4.6,0) {và};
  \begin{scope}[shift={(5.5,0)}]
    \VeHatRoi[cyan!70]{-0.2}{0.3}
    \VeHatRoi[cyan!70]{0.2}{0.3}
    \VeHatRoi[cyan!70]{-0.3}{0}
    \VeHatRoi[cyan!70]{0}{0}
    \VeHatRoi[cyan!70]{0.3}{0}
    \VeHatRoi[cyan!70]{-0.18}{-0.3}
    \VeHatRoi[cyan!70]{0.18}{-0.3}
    \node[below, font=\scriptsize\bfseries, color=blue!80!black] at (0,-0.5) {7 hạt rời};
  \end{scope}
\end{tikzpicture}
\end{center}
Số hạt ngọc của bạn Lan gồm mấy chục và mấy đơn vị?
\begin{multicols}{2}
\choice
{$7$ chục và $3$ đơn vị}
{\True $3$ chục và $7$ đơn vị}
{$3$ chục và $0$ đơn vị}
{$37$ chục và $0$ đơn vị}
\end{multicols}
\loigiai{
Có 3 chuỗi 10 hạt (tức 3 chục) và 7 hạt rời (7 đơn vị). Vậy số hạt gồm 3 chục và 7 đơn vị (số 37).\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 12: Đọc số có đuôi 1 (mốt) và 5 (lăm)
\begin{ex} %[1D6V21]
Hai chú gấu mang hai hũ mật ong có ghi số:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[fill=orange!35, draw=orange!80!black, line width=0.8pt, rounded corners=4pt] (-2.0,-0.6) rectangle (-0.6,0.6);
  \draw[fill=brown!60, draw=black!80, line width=0.7pt] (-1.8,0.6) rectangle (-0.8,0.85);
  \node[font=\bfseries\LARGE, color=red!85!black] at (-1.3,0) {31};
  \node[below, font=\bfseries\scriptsize, color=blue!80!black] at (-1.3,-0.65) {Hũ thứ nhất};

  \draw[fill=yellow!35, draw=orange!80!black, line width=0.8pt, rounded corners=4pt] (0.6,-0.6) rectangle (2.0,0.6);
  \draw[fill=brown!60, draw=black!80, line width=0.7pt] (0.8,0.6) rectangle (1.8,0.85);
  \node[font=\bfseries\LARGE, color=red!85!black] at (1.3,0) {75};
  \node[below, font=\bfseries\scriptsize, color=blue!80!black] at (1.3,-0.65) {Hũ thứ hai};
\end{tikzpicture}
\end{center}
Cách đọc đúng tên hai số trên hai hũ mật ong lần lượt là:
\begin{multicols}{2}
\choice
{Ba mươi một và Bảy mươi năm}
{\True Ba mươi mốt và Bảy mươi lăm}
{Mười ba và Năm mươi bảy}
{Ba một và Bảy năm}
\end{multicols}
\loigiai{
Chữ số 1 đứng ở hàng đơn vị (từ 21 trở đi) đọc là "mốt" (ba mươi mốt); chữ số 5 đứng ở hàng đơn vị đọc là "lăm" (bảy mươi lăm).\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 VÀ CÂU 14 (ĐÚNG / SAI) ---

\textbf{Phần 2. Câu trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Bảng cấu tạo chục và đơn vị
\begin{ex} %[1D6H21]
Quan sát hình ảnh các bó que tính và que tính rời dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.85]
  \begin{scope}[shift={(0,0)}]
    \VeBoQueTinh[blue]{-1.4,0}
    \VeBoQueTinh[blue]{-0.7,0}
    \VeBoQueTinh[blue]{0,0}
    \VeBoQueTinh[blue]{0.7,0}
    \VeBoQueTinh[blue]{1.4,0}
    \node[below, font=\scriptsize\bfseries, color=blue!80!black] at (0,-0.75) {5 bó (5 chục que tính)};
  \end{scope}
  \node[font=\bfseries\normalsize, color=purple] at (2.4,0) {và};
  \begin{scope}[shift={(3.2,0)}]
    \VeQueRoi[-10]{-0.18}{0}{yellow!40!brown}
    \VeQueRoi[10]{0.18}{0}{yellow!40!brown}
    \node[below, font=\scriptsize\bfseries, color=brown!80!black] at (0,-0.75) {2 que rời};
  \end{scope}
\end{tikzpicture}
\end{center}
Xét tính Đúng hay Sai của mỗi khẳng định sau:
\choiceTF
{\True Hình vẽ trên biểu diễn số gồm $5$ chục và $2$ đơn vị}
{\True Số biểu diễn ở hình trên được viết là $52$}
{Số trên được đọc là: ``Năm mươi hai chục''}
{\True Nếu lấy thêm $1$ que rời nữa thì ta được số $53$}
\loigiai{
\begin{itemize}
  \item Ý a) Đúng: Có 5 bó que tính (5 chục) và 2 que rời (2 đơn vị).
  \item Ý b) Đúng: Số gồm 5 chục và 2 đơn vị viết là 52.
  \item Ý c) Sai: Số 52 đọc là "năm mươi hai" (chứ không phải năm mươi hai chục).
  \item Ý d) Đúng: $52 + 1 = 53$.
\end{itemize}
}
\end{ex}

% CÂU 14: Nhận định về các số có hai chữ số đặc biệt
\begin{ex} %[1D6V21]
Bốn bạn nhỏ mang bốn tấm thẻ số có hai chữ số:
\begin{center}
\begin{tikzpicture}[scale=0.85]
  \VeBanNhoCamBang[red!70]{-3.6,0}{An}{$10$}
  \VeBanNhoCamBang[blue!60]{-1.2,0}{Bình}{$44$}
  \VeBanNhoCamBang[green!60!teal]{1.2,0}{Cúc}{$70$}
  \VeBanNhoCamBang[purple!60]{3.6,0}{Dũng}{$99$}
\end{tikzpicture}
\end{center}
Xét tính Đúng hay Sai của mỗi khẳng định sau:
\choiceTF
{\True Số $10$ trên thẻ của An là số bé nhất có hai chữ số}
{\True Thẻ của Bình có chữ số hàng chục và hàng đơn vị giống nhau (đều là chữ số $4$)}
{Số $70$ trên thẻ của Cúc gồm $0$ chục và $7$ đơn vị}
{\True Số $99$ trên thẻ của Dũng là số lớn nhất có hai chữ số}
\loigiai{
\begin{itemize}
  \item Ý a) Đúng: 10 là số có hai chữ số nhỏ nhất.
  \item Ý b) Đúng: Số 44 có cả hai chữ số đều là 4.
  \item Ý c) Sai: Số 70 gồm 7 chục và 0 đơn vị.
  \item Ý d) Đúng: 99 là số có hai chữ số lớn nhất.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 15 ĐẾN CÂU 20 (ĐIỀN SỐ) ---

\textbf{Phần 3. Câu trắc nghiệm trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 15: Đếm tổng số que tính (bó và rời)
\begin{ex} %[1D6N21]
Quan sát hình ảnh dưới đây và cho biết có tất cả bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \VeBoQueTinh[purple]{0,0}
  \VeBoQueTinh[purple]{0.8,0}
  \node[below, font=\scriptsize\bfseries, color=blue!80!black] at (0.4,-0.75) {2 bó chục};
  \node[font=\bfseries\normalsize, color=purple] at (1.7,0) {và};
  \begin{scope}[shift={(2.6,0)}]
    \VeQueRoi[-8]{-0.35}{0}{yellow!40!brown}
    \VeQueRoi[0]{-0.18}{0}{yellow!40!brown}
    \VeQueRoi[6]{0}{0}{yellow!40!brown}
    \VeQueRoi[-5]{0.18}{0}{yellow!40!brown}
    \VeQueRoi[10]{0.35}{0}{yellow!40!brown}
    \VeQueRoi[-4]{0.52}{0}{yellow!40!brown}
    \node[below, font=\scriptsize\bfseries, color=brown!80!black] at (0.1,-0.75) {6 que rời};
  \end{scope}
\end{tikzpicture}
\end{center}
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$26$}}
\loigiai{
Có 2 bó chục (20 que tính) và 6 que rời: $20 + 6 = 26$ que tính.\\
\textbf{Đáp số: $26$.}
}
\end{ex}

% CÂU 16: Đếm số khối lập phương
\begin{ex} %[1D6H21]
Đếm tổng số khối lập phương nhỏ trong hình sau:
\begin{center}
\begin{tikzpicture}[scale=0.75]
  \VeThanhChucKhoi[cyan!65]{0,0}
  \VeThanhChucKhoi[cyan!65]{0.55,0}
  \VeThanhChucKhoi[cyan!65]{1.1,0}
  \VeThanhChucKhoi[cyan!65]{1.65,0}
  \node[below, font=\scriptsize\bfseries, color=cyan!90!black] at (0.85,-0.05) {4 thanh chục};
  \node[font=\bfseries\normalsize, color=purple] at (2.5,0.9) {và};
  \begin{scope}[shift={(3.2,0.55)}]
    \VeKhoiRoi[orange!75]{0}{0}{0.5}
    \VeKhoiRoi[orange!75]{0.4}{0}{0.5}
    \VeKhoiRoi[orange!75]{0.2}{0.35}{0.5}
    \node[below, font=\scriptsize\bfseries, color=orange!90!black] at (0.2,-0.2) {3 khối rời};
  \end{scope}
\end{tikzpicture}
\end{center}
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$43$}}
\loigiai{
Có 4 thanh chục (40 khối) và 3 khối rời: $40 + 3 = 43$ khối lập phương.\\
\textbf{Đáp số: $43$.}
}
\end{ex}

% CÂU 17: Xác định chữ số hàng chục
\begin{ex} %[1D6H21]
Quan sát bảng cấu tạo số của số $68$:
\begin{center}
\begin{tikzpicture}
  \draw[fill=blue!5, draw=blue!80!black, line width=0.8pt, rounded corners=3pt] (0,0) rectangle (4.8,1.9);
  \draw[blue!80!black, line width=0.7pt] (2.4,0) -- (2.4,1.9);
  \draw[fill=blue!18, draw=blue!80!black, line width=0.7pt] (0,1.2) rectangle (4.8,1.9);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (1.2,1.55) {CHỤC};
  \node[font=\bfseries\normalsize, color=blue!90!black] at (3.6,1.55) {ĐƠN VỊ};
  \node[font=\bfseries\Huge, color=red!80!black] at (1.2,0.6) {6};
  \node[font=\bfseries\Huge, color=green!60!black] at (3.6,0.6) {8};
\end{tikzpicture}
\end{center}
Chữ số hàng chục của số $68$ là chữ số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$6$}}
\loigiai{
Trong số $68$, chữ số đứng trước là chữ số hàng chục, tức là chữ số $6$.\\
\textbf{Đáp số: $6$.}
}
\end{ex}

% CÂU 18: Điền số thích hợp vào ô trống trên dãy số
\begin{ex} %[1D6H21]
Điền số thích hợp vào ô trống có dấu ``$?$'' trên dây cờ đuôi nheo:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[line width=1pt, brown!80!black] (-0.5,1.0) to[bend right=8] (7.5,1.0);
  \foreach \x/\num/\c in {0/76/red!40, 1.6/77/yellow!50, 3.2/78/green!40, 4.8/?/cyan!40, 6.4/80/orange!50} {
    \draw[fill=\c, draw=black!80, line width=0.7pt] (\x,0.95) -- (\x+1.0,0.95) -- (\x+0.5,0.05) -- cycle;
    \node[font=\bfseries\normalsize, color=black] at (\x+0.5,0.65) {\num};
  }
\end{tikzpicture}
\end{center}
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$79$}}
\loigiai{
Dãy số tăng dần liên tiếp: $76, 77, 78, 79, 80$. Số cần điền là $79$.\\
\textbf{Đáp số: $79$.}
}
\end{ex}

% CÂU 19: Tìm số bí mật
\begin{ex} %[1D6V21]
Bạn Thỏ và bạn Rùa cùng đố nhau một câu đố:
\begin{center}
\begin{tikzpicture}
  \node[draw=orange!80!black, fill=yellow!15, rounded corners=6pt, inner sep=7pt, align=center, font=\normalsize] {
    ``Tôi là số có hai chữ số, chữ số hàng chục là \textbf{8},\\
    chữ số hàng đơn vị là \textbf{4}. Hỏi tôi là số nào?''
  };
\end{tikzpicture}
\end{center}
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$84$}}
\loigiai{
Số gồm 8 chục và 4 đơn vị là số $84$ (đọc là tám mươi tư).\\
\textbf{Đáp số: $84$.}
}
\end{ex}

% CÂU 20: Đếm tổng số quả bóng bay
\begin{ex} %[1D6V21]
Bác bảo vệ mang 5 chùm bóng bay (mỗi chùm có đúng 10 quả) và cầm thêm 8 quả bóng bay rời:
\begin{center}
\begin{tikzpicture}[scale=0.75]
  \foreach \i in {0, 1.1, 2.2, 3.3, 4.4} {
    \draw[gray!70, line width=0.5pt] (\i+0.25,-0.5) -- (\i+0.35,0.25);
    \draw[fill=red!50!pink, draw=red!80!black, line width=0.5pt] (\i+0.35,0.4) circle (0.36cm);
    \node[font=\bfseries\tiny, color=white] at (\i+0.35,0.4) {10};
  }
  \node[below, font=\scriptsize\bfseries, color=red!80!black] at (2.5,-0.65) {5 chùm bóng (mỗi chùm 10 quả)};

  \node[font=\bfseries\normalsize, color=purple] at (5.5,0.15) {và};

  \begin{scope}[shift={(6.3,0)}]
    \node[draw=blue!80!black, fill=blue!10, rounded corners=3pt, font=\bfseries\small, inner sep=4pt] at (0,0.15) {8 quả rời};
  \end{scope}
\end{tikzpicture}
\end{center}
Bác bảo vệ có tất cả bao nhiêu quả bóng bay?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$58$}}
\loigiai{
5 chùm bóng là 5 chục quả bóng = 50 quả bóng. Cùng với 8 quả bóng rời: $50 + 8 = 58$ quả bóng.\\
\textbf{Đáp số: $58$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 6 Bai 21
tex_path = os.path.abspath('CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100/Chuong6_Bai21_SoCoHaiChuSo.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_21_preview.tex độc lập 5 trang
preview_content = r'''\documentclass[14pt,a4paper]{extbook}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,calc,positioning,backgrounds,patterns,decorations.pathreplacing}
\usepackage{tcolorbox}
\tcbuselibrary{skins,theorems}
\usepackage{geometry}
\geometry{a4paper,left=18mm,right=18mm,top=16mm,bottom=16mm}
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
  \par\vspace{0.3ex}%
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 21: SỐ CÓ HAI CHỮ SỐ},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 6: Các số đến 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-21}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_21_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_21_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_21_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_21_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_21_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_21_So_co_hai_chu_so.pdf')
    import shutil
    shutil.copy2('Bai_21_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
