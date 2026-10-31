# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 30: PHÉP CỘNG SỐ CÓ HAI CHỮ SỐ VỚI SỐ CÓ HAI CHỮ SỐ (KHÔNG NHỚ)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 30 ---

% 1. Mô hình đặt tính cột dọc hai số có hai chữ số
\providecommand{\VeDatTinhHaiSo}[4]{% #1=(x,y), #2=số trên, #3=số dưới, #4=kết quả
  \begin{scope}[shift={(#1)}, scale=0.7]
    \draw[fill=blue!5, draw=blue!70, line width=0.8pt, rounded corners=3pt] (-1.2,-1.2) rectangle (1.2,1.2);
    \node[font=\bfseries\Large, color=black] at (0.3,0.6) {#2};
    \node[font=\bfseries\Large, color=red!85] at (-0.7,0.0) {$+$};
    \node[font=\bfseries\Large, color=black] at (0.3,0.0) {#3};
    \draw[line width=1.2pt, black!80] (-0.9,-0.3) -- (0.9,-0.3);
    \node[font=\bfseries\Large, color=blue!90!black] at (0.3,-0.75) {#4};
  \end{scope}
}

% 2. Khối lập phương biểu diễn phép cộng 2 số
\providecommand{\VeKhoiCongHaiSo}[5]{% #1=(x,y), #2=chục 1, #3=đv 1, #4=chục 2, #5=đv 2
  \begin{scope}[shift={(#1)}, scale=0.42]
    % Nhóm số 1
    \foreach \c in {1,...,#2} {
      \draw[fill=orange!60, draw=black!80, line width=0.4pt] (\c*0.7-0.7,0) rectangle (\c*0.7-0.2,2.8);
      \foreach \y in {0.28,0.56,...,2.52} {
        \draw[black!50, line width=0.2pt] (\c*0.7-0.7,\y) -- (\c*0.7-0.2,\y);
      }
    }
    \pgfmathsetmacro{\xstart}{#2*0.7 + 0.2}
    \foreach \u in {1,...,#3} {
      \draw[fill=cyan!50, draw=black!80, line width=0.4pt] (\xstart,\u*0.45-0.45) rectangle (\xstart+0.4,\u*0.45-0.05);
    }
    % Dấu cộng
    \node[font=\bfseries\Large, color=red!85] at (\xstart+0.9, 1.2) {$+$};
    % Nhóm số 2
    \pgfmathsetmacro{\xgroup}{\xstart + 1.5}
    \foreach \c in {1,...,#4} {
      \draw[fill=green!60, draw=black!80, line width=0.4pt] (\xgroup+\c*0.7-0.7,0) rectangle (\xgroup+\c*0.7-0.2,2.8);
      \foreach \y in {0.28,0.56,...,2.52} {
        \draw[black!50, line width=0.2pt] (\xgroup+\c*0.7-0.7,\y) -- (\xgroup+\c*0.7-0.2,\y);
      }
    }
    \pgfmathsetmacro{\xend}{\xgroup + #4*0.7 + 0.2}
    \foreach \v in {1,...,#5} {
      \draw[fill=yellow!70, draw=black!80, line width=0.4pt] (\xend,\v*0.45-0.45) rectangle (\xend+0.4,\v*0.45-0.05);
    }
  \end{scope}
}

% 3. Xe tải chở phép cộng
\providecommand{\VeXePhepTinhHaiSo}[4]{% #1=(x,y), #2=màu xe, #3=phép tính, #4=kết quả
  \begin{scope}[shift={(#1)}, scale=0.6]
    \draw[fill=#2!40, draw=black!80, line width=0.7pt, rounded corners=3pt] (-1.6,0) rectangle (1.6,0.9);
    \draw[fill=white, draw=black!70, line width=0.5pt, rounded corners=2pt] (-1.4,0.15) rectangle (1.4,0.75);
    \node[font=\bfseries\small, color=blue!90!black] at (0,0.45) {#3 = #4};
    \fill[black!85] (-1.0,-0.12) circle (0.2cm);
    \fill[gray!40] (-1.0,-0.12) circle (0.09cm);
    \fill[black!85] (1.0,-0.12) circle (0.2cm);
    \fill[gray!40] (1.0,-0.12) circle (0.09cm);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: 32 + 25 bằng mô hình khối
\begin{ex} %[1D8N30]
Quan sát mô hình khối lập phương biểu diễn phép tính $32 + 25$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeKhoiCongHaiSo{0,0}{3}{2}{2}{5}
  \node[below, font=\bfseries\tiny, color=blue!90!black] at (1.1,-0.2) {$32$ ($3$ chục $2$ đv)};
  \node[below, font=\bfseries\tiny, color=green!70!black] at (3.8,-0.2) {$25$ ($2$ chục $5$ đv)};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $32 + 25$ là:
\begin{multicols}{4}
\choice
{$56$}
{\True $57$}
{$58$}
{$59$}
\end{multicols}
\loigiai{
Cộng hàng đơn vị: $2 + 5 = 7$. Cộng hàng chục: $3 + 2 = 5$. Kết quả là $57$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: 40 + 30
\begin{ex} %[1D8N30]
Ghép các thanh chục tròn chục:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=blue!30, draw=black] (0,0) rectangle (3.2,0.6) node[midway, font=\tiny\bfseries] {$40$ ($4$ chục)};
  \draw[fill=orange!40, draw=black] (3.2,0) rectangle (5.6,0.6) node[midway, font=\tiny\bfseries] {$30$ ($3$ chục)};
  \draw[line width=0.8pt, stealth-stealth, red!85] (0,-0.35) -- (5.6,-0.35) node[midway, below, font=\bfseries\tiny] {Tổng số = ?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $40 + 30$ là:
\begin{multicols}{4}
\choice
{$60$}
{\True $70$}
{$80$}
{$90$}
\end{multicols}
\loigiai{
$4$ chục $+ 3$ chục $= 7$ chục $= 70$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Đặt tính 54 + 23
\begin{ex} %[1D8H30]
Quan sát phép tính đặt theo cột dọc:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDatTinhHaiSo{0,0}{54}{23}{77}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $54 + 23$ là:
\begin{multicols}{4}
\choice
{$76$}
{\True $77$}
{$78$}
{$79$}
\end{multicols}
\loigiai{
$4 + 3 = 7$; $5 + 2 = 7$. Vậy $54 + 23 = 77$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Phép tính 61 + 38
\begin{ex} %[1D8H30]
Toa xe lửa chở phép tính $61 + 38$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeXePhepTinhHaiSo{0,0}{cyan}{$61 + 38$}{~?~}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $61 + 38$ là:
\begin{multicols}{4}
\choice
{$98$}
{\True $99$}
{$97$}
{$100$}
\end{multicols}
\loigiai{
$1 + 8 = 9$; $6 + 3 = 9$. Vậy $61 + 38 = 99$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Tìm x: x - 24 = 35
\begin{ex} %[1D8H30]
Mảnh ghép chứa phép tính tìm số ban đầu:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=purple!80, fill=pink!20, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {
    $? - 24 = 35$
  };
\end{tikzpicture}
\end{center}
Số thích hợp điền vào dấu \textbf{?} là:
\begin{multicols}{4}
\choice
{$58$}
{\True $59$}
{$60$}
{$69$}
\end{multicols}
\loigiai{
Số cần tìm là: $35 + 24 = 59$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: So sánh hai phép cộng 34 + 25 và 41 + 18
\begin{ex} %[1D8H30]
Cân đĩa so sánh hai vế phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-2.2,0) {$34 + 25$};
  \node[draw=orange!90, fill=yellow!30, rounded corners=2pt, font=\bfseries\normalsize, inner sep=3pt] at (0.2,0) {~?~};
  \node[draw=red!80, fill=pink!20, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (2.2,0) {$41 + 18$};
\end{tikzpicture}
\end{center}
Dấu thích hợp để điền vào ô trống là:
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{$+$}
\end{multicols}
\loigiai{
Vế trái: $34 + 25 = 59$. Vế phải: $41 + 18 = 59$. Hai vế bằng nhau nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Bài toán hai lớp 1A và 1B
\begin{ex} %[1D8V30]
Lớp 1A có $34$ học sinh, lớp 1B có $35$ học sinh:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=blue!25, draw=blue!80, line width=0.6pt] (0,0) rectangle (3.2,0.6) node[midway, font=\bfseries\tiny] {Lớp 1A: $34$ bạn};
  \draw[fill=green!25, draw=green!80, line width=0.6pt] (3.2,0) rectangle (6.5,0.6) node[midway, font=\bfseries\tiny] {Lớp 1B: $35$ bạn};
  \draw[line width=0.8pt, stealth-stealth, red!85] (0,-0.35) -- (6.5,-0.35) node[midway, below, font=\bfseries\tiny] {Cả hai lớp = ? bạn};
\end{tikzpicture}
\end{center}
Cả hai lớp có tất cả số học sinh là:
\begin{multicols}{4}
\choice
{$68$ bạn}
{\True $69$ bạn}
{$70$ bạn}
{$71$ bạn}
\end{multicols}
\loigiai{
Cả hai lớp có số học sinh là: $34 + 35 = 69$ bạn.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Bài toán gà và vịt
\begin{ex} %[1D8V30]
Trang trại có $45$ con gà và $32$ con vịt:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!35, draw=black] (0,0) rectangle (3.6,0.6) node[midway, font=\bfseries\tiny] {$45$ con gà};
  \draw[fill=cyan!35, draw=black] (3.6,0) rectangle (6.2,0.6) node[midway, font=\bfseries\tiny] {$32$ con vịt};
  \draw[line width=0.8pt, stealth-stealth, blue!85] (0,-0.35) -- (6.2,-0.35) node[midway, below, font=\bfseries\tiny] {Tổng số con = ?};
\end{tikzpicture}
\end{center}
Tổng số con gà và vịt của trang trại là:
\begin{multicols}{4}
\choice
{$76$ con}
{\True $77$ con}
{$78$ con}
{$79$ con}
\end{multicols}
\loigiai{
Tổng số con là: $45 + 32 = 77$ con.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Tính biểu thức 23 + 14 + 31
\begin{ex} %[1D8V30]
Băng giấy chứa dãy tính ba số có hai chữ số:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \node[draw=blue!80, fill=cyan!10, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {
    $23 + 14 + 31 = \dots$
  };
\end{tikzpicture}
\end{center}
Giá trị của biểu thức trên là:
\begin{multicols}{4}
\choice
{$67$}
{\True $68$}
{$69$}
{$70$}
\end{multicols}
\loigiai{
Thực hiện từ trái sang phải: $23 + 14 = 37$; sau đó $37 + 31 = 68$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Ghép hai đoạn dây đo cm
\begin{ex} %[1D8V30]
Đoạn dây đỏ dài $35\text{ cm}$, đoạn dây xanh dài $42\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=red!35, draw=black] (0,0) rectangle (3.2,0.6) node[midway, font=\tiny\bfseries] {Đỏ $35\text{ cm}$};
  \draw[fill=cyan!35, draw=black] (3.2,0) rectangle (7.0,0.6) node[midway, font=\tiny\bfseries] {Xanh $42\text{ cm}$};
  \draw[line width=0.8pt, stealth-stealth, black!70] (0,-0.35) -- (7.0,-0.35) node[midway, below, font=\bfseries\tiny] {Cả hai đoạn = ? cm};
\end{tikzpicture}
\end{center}
Cả hai đoạn dây dài tất cả là:
\begin{multicols}{4}
\choice
{$76\text{ cm}$}
{\True $77\text{ cm}$}
{$78\text{ cm}$}
{$79\text{ cm}$}
\end{multicols}
\loigiai{
Cả hai đoạn dây dài tất cả: $35 + 42 = 77\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Tìm số thích hợp: 42 + ? = 86
\begin{ex} %[1D8V30]
Tìm số thích hợp để điền vào ô trống:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-1.8,0) {$42$};
  \node[font=\bfseries\Large, color=red!85] at (-0.8,0) {$+$};
  \node[draw=red!80, fill=yellow!30, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {?};
  \node[font=\bfseries\Large, color=blue!80] at (0.8,0) {$=$};
  \node[draw=green!80, fill=lime!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (1.8,0) {$86$};
\end{tikzpicture}
\end{center}
Số thích hợp để điền vào ô trống là:
\begin{multicols}{4}
\choice
{$43$}
{\True $44$}
{$45$}
{$46$}
\end{multicols}
\loigiai{
Hàng đơn vị: $2 + 4 = 6$. Hàng chục: $4 + 4 = 8$. Vậy số cần điền là $44$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Vận dụng cao - Tính nhanh nhóm tròn chục
\begin{ex} %[1D8C30]
Tính nhanh tổng bốn số trên các cánh hoa:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!15, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3.8,-0.5) rectangle (3.8,0.5);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0,0) {
    $24 + 35 + 16 + 25 = \dots$
  };
\end{tikzpicture}
\end{center}
Kết quả của phép tính nhanh trên là:
\begin{multicols}{4}
\choice
{$90$}
{\True $100$}
{$95$}
{$80$}
\end{multicols}
\loigiai{
Nhóm các cặp số có hàng đơn vị cộng lại bằng 10:\\
$(24 + 16) + (35 + 25) = 40 + 60 = 100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Các phép cộng 2 chữ số
\begin{ex} %[1D8H30]
Bảng con ghi các phép cộng:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=blue!10, draw=blue!80, line width=1pt, rounded corners=3pt] (-4,-0.6) rectangle (4,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (-2,0) {$43 + 34 = 77$};
  \node[font=\bfseries\scriptsize, color=red!90!black] at (2,0) {$50 + 28 = 78$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép tính sau:
\choiceTF
{\True Phép tính $43 + 34 = 77$ là đúng.}
{\True Phép tính $50 + 28 = 78$ là đúng.}
{Phép tính $36 + 42 = 88$ là đúng.}
{\True Phép tính $36 + 42 = 78$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $43 + 34 = 77$.
  \item b) \textbf{Đúng}: $50 + 28 = 78$.
  \item c) \textbf{Sai}: $36 + 42 = 78$ (chứ không phải $88$).
  \item d) \textbf{Đúng}: $36 + 42 = 78$.
\end{itemize}
}
\end{ex}

% CÂU 14: Bài toán kẹo của Bình và An
\begin{ex} %[1D8V30]
Bình có $25$ cái kẹo, An có $32$ cái kẹo:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=pink!40, draw=black] (-3,-0.4) rectangle (-0.5,0.4) node[midway, font=\bfseries\tiny] {Bình: $25$ kẹo};
  \draw[fill=cyan!35, draw=black] (0.5,-0.4) rectangle (3,-0.4+0.8) node[midway, font=\bfseries\tiny] {An: $32$ kẹo};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Cả hai bạn có tất cả $57$ cái kẹo.}
{\True Bạn An có nhiều hơn bạn Bình $7$ cái kẹo.}
{Cả hai bạn có tất cả $60$ cái kẹo.}
{\True Cần thêm $3$ cái kẹo nữa mới đủ $60$ cái kẹo.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $25 + 32 = 57$ cái kẹo.
  \item b) \textbf{Đúng}: $32 - 25 = 7$ cái kẹo.
  \item c) \textbf{Sai}: Tổng là $57$ cái kẹo.
  \item d) \textbf{Đúng}: $60 - 57 = 3$ cái kẹo.
\end{itemize}
}
\end{ex}

% CÂU 15: Quy tắc cộng cột dọc hai số có 2 chữ số
\begin{ex} %[1D8H30]
Hình minh họa cách đặt tính cột dọc:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \VeDatTinhHaiSo{0,0}{34}{43}{77}
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phát biểu về quy tắc:
\choiceTF
{\True Đặt các chữ số ở cùng một hàng thẳng cột với nhau.}
{\True Hàng đơn vị thẳng hàng đơn vị, hàng chục thẳng hàng chục.}
{Thực hiện cộng từ trái sang phải (cộng hàng chục trước).}
{\True Thực hiện cộng từ phải sang trái (cộng hàng đơn vị trước).}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Thẳng hàng cột.
  \item b) \textbf{Đúng}: Đơn vị thẳng đơn vị, chục thẳng chục.
  \item c) \textbf{Sai}: Phải cộng từ phải sang trái.
  \item d) \textbf{Đúng}: Cộng hàng đơn vị trước rồi đến hàng chục.
\end{itemize}
}
\end{ex}

% CÂU 16: So sánh các tổng
\begin{ex} %[1D8V30]
Bốn thẻ ghi các phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-3,0) {$22 + 33 = 55$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-1,0) {$45 + 14 = 59$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (1,0) {$51 + 26 = 87$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (3,0) {$30 + 40 = 70$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép tính sau:
\choiceTF
{\True $22 + 33 = 55$ là đúng.}
{\True $45 + 14 = 59$ là đúng.}
{Phép tính $51 + 26 = 87$ là đúng.}
{\True $30 + 40 = 70$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $22 + 33 = 55$.
  \item b) \textbf{Đúng}: $45 + 14 = 59$.
  \item c) \textbf{Sai}: $51 + 26 = 77$ (chứ không phải $87$).
  \item d) \textbf{Đúng}: $30 + 40 = 70$.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN / ĐIỀN SỐ) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tính 34 + 43
\begin{ex} %[1D8H30]
Tính kết quả phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!30, draw=blue!80, line width=0.7pt, rounded corners=2pt] (-2.0,-0.4) rectangle (2.0,0.4);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0,0) {$34 + 43 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$77$}}
\loigiai{
$34 + 43 = 77$.\\
\textbf{Đáp số: $77$.}
}
\end{ex}

% CÂU 18: Tính 52 + 27
\begin{ex} %[1D8H30]
Tính kết quả phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=pink!30, draw=red!80, line width=0.7pt, rounded corners=2pt] (-2.0,-0.4) rectangle (2.0,0.4);
  \node[font=\bfseries\normalsize, color=red!90!black] at (0,0) {$52 + 27 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$79$}}
\loigiai{
$52 + 27 = 79$.\\
\textbf{Đáp số: $79$.}
}
\end{ex}

% CÂU 19: Bài toán vườn cây cam và xoài
\begin{ex} %[1D8V30]
Vườn có $35$ cây cam và $24$ cây xoài:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=orange!30, draw=black] (0,0) rectangle (3.5,0.55) node[midway, font=\tiny\bfseries] {$35$ cây cam};
  \draw[fill=yellow!40, draw=black] (3.5,0) rectangle (6.0,0.55) node[midway, font=\tiny\bfseries] {$24$ cây xoài};
  \draw[line width=0.8pt, stealth-stealth, blue!85] (0,-0.35) -- (6.0,-0.35) node[midway, below, font=\bfseries\tiny] {Tổng số cây = ?};
\end{tikzpicture}
\end{center}
Hỏi trong vườn có tất cả bao nhiêu cây cam và xoài?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$59$}}
\loigiai{
Tổng số cây là: $35 + 24 = 59$ cây.\\
\textbf{Đáp số: $59$ cây.}
}
\end{ex}

% CÂU 20: Vận dụng cao - Tính nhanh ba số tròn chục
\begin{ex} %[1D8C30]
Tính nhanh phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!70!orange, draw=black, line width=0.8pt, rounded corners=3pt] (-3.0,-0.45) rectangle (3.0,0.45);
  \node[font=\bfseries\normalsize, color=blue!95!black] at (0,0) {
    $20 + 30 + 40 = \text{\textbf{?}}$
  };
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$90$}}
\loigiai{
$20 + 30 = 50$; sau đó $50 + 40 = 90$.\\
\textbf{Đáp số: $90$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 8 Bai 30
tex_path = os.path.abspath('CHỦ ĐỀ 8 - PHÉP CỘNG, PHÉP TRỪ (KHÔNG NHỚ) TRONG PHẠM VI 100/Chuong8_Bai30_PhepCongSoCoHaiChuSoVoiSoCoHaiChuSo.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_30_preview.tex độc lập 5 trang
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 30: CỘNG SỐ CÓ HAI CHỮ SỐ VỚI SỐ CÓ HAI CHỮ SỐ},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 8: Phép cộng, phép trừ PV 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-30}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_30_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_30_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_30_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_30_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_30_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_30_Cong_so_2_chu_so_voi_so_2_chu_so.pdf')
    import shutil
    shutil.copy2('Bai_30_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
