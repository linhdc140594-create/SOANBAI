# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 29: PHÉP CỘNG SỐ CÓ HAI CHỮ SỐ VỚI SỐ CÓ MỘT CHỮ SỐ (KHÔNG NHỚ)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 29 ---

% 1. Mô hình đặt tính cột dọc
\providecommand{\VeDatTinhDoc}[4]{% #1=(x,y), #2=số trên, #3=số dưới (1 chữ số), #4=kết quả
  \begin{scope}[shift={(#1)}, scale=0.7]
    \draw[fill=blue!5, draw=blue!70, line width=0.8pt, rounded corners=3pt] (-1.1,-1.2) rectangle (1.1,1.2);
    \node[font=\bfseries\Large, color=black] at (0.3,0.6) {#2};
    \node[font=\bfseries\Large, color=red!85] at (-0.6,0.0) {$+$};
    \node[font=\bfseries\Large, color=black] at (0.3,0.0) {#3};
    \draw[line width=1.2pt, black!80] (-0.8,-0.3) -- (0.8,-0.3);
    \node[font=\bfseries\Large, color=blue!90!black] at (0.3,-0.75) {#4};
  \end{scope}
}

% 2. Thanh chục và khối rời cộng khối rời
\providecommand{\VeKhoiCongDonVi}[4]{% #1=(x,y), #2=số chục, #3=số đv ban đầu, #4=số đv thêm
  \begin{scope}[shift={(#1)}, scale=0.45]
    % Vẽ các thanh chục
    \foreach \c in {1,...,#2} {
      \draw[fill=orange!60, draw=black!80, line width=0.4pt] (\c*0.7-0.7,0) rectangle (\c*0.7-0.2,3.0);
      \foreach \y in {0.3,0.6,...,2.7} {
        \draw[black!50, line width=0.2pt] (\c*0.7-0.7,\y) -- (\c*0.7-0.2,\y);
      }
    }
    % Các khối đơn vị ban đầu
    \pgfmathsetmacro{\xstart}{#2*0.7 + 0.3}
    \foreach \u in {1,...,#3} {
      \draw[fill=cyan!50, draw=black!80, line width=0.4pt] (\xstart,\u*0.5-0.5) rectangle (\xstart+0.45,\u*0.5-0.05);
    }
    % Dấu cộng
    \node[font=\bfseries\large, color=red!85] at (\xstart+1.0, 1.2) {$+$};
    % Các khối đơn vị thêm vào
    \pgfmathsetmacro{\xadd}{\xstart + 1.6}
    \foreach \a in {1,...,#4} {
      \draw[fill=green!60, draw=black!80, line width=0.4pt] (\xadd,\a*0.5-0.5) rectangle (\xadd+0.45,\a*0.5-0.05);
    }
  \end{scope}
}

% 3. Xe chở phép tính cộng
\providecommand{\VeXePhepTinhCong}[4]{% #1=(x,y), #2=màu xe, #3=phép tính, #4=kết quả
  \begin{scope}[shift={(#1)}, scale=0.6]
    \draw[fill=#2!40, draw=black!80, line width=0.7pt, rounded corners=3pt] (-1.5,0) rectangle (1.5,0.9);
    \draw[fill=white, draw=black!70, line width=0.5pt, rounded corners=2pt] (-1.3,0.15) rectangle (1.3,0.75);
    \node[font=\bfseries\small, color=blue!90!black] at (0,0.45) {#3 = #4};
    \fill[black!85] (-0.9,-0.12) circle (0.2cm);
    \fill[gray!40] (-0.9,-0.12) circle (0.09cm);
    \fill[black!85] (0.9,-0.12) circle (0.2cm);
    \fill[gray!40] (0.9,-0.12) circle (0.09cm);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: 23 + 4 bằng mô hình khối
\begin{ex} %[1D8N29]
Quan sát mô hình $2$ thanh chục và $3$ khối rời, gộp thêm $4$ khối rời:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeKhoiCongDonVi{0,0}{2}{3}{4}
  \node[below, font=\bfseries\tiny, color=blue!90!black] at (0.6,-0.2) {$2$ chục};
  \node[below, font=\bfseries\tiny, color=cyan!90!black] at (1.9,-0.2) {$3$ đv};
  \node[below, font=\bfseries\tiny, color=green!70!black] at (3.5,-0.2) {Thêm $4$ đv};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $23 + 4$ là:
\begin{multicols}{4}
\choice
{$26$}
{\True $27$}
{$28$}
{$29$}
\end{multicols}
\loigiai{
Cộng các chữ số hàng đơn vị: $3 + 4 = 7$, giữ nguyên chữ số hàng chục $2$. Ta được $23 + 4 = 27$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Đặt tính 45 + 3
\begin{ex} %[1D8N29]
Quan sát phép tính đặt tính theo cột dọc:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDatTinhDoc{0,0}{45}{3}{48}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $45 + 3$ là:
\begin{multicols}{4}
\choice
{$47$}
{\True $48$}
{$49$}
{$58$}
\end{multicols}
\loigiai{
Hàng đơn vị: $5 + 3 = 8$. Hạ hàng chục $4$ xuống. Vậy $45 + 3 = 48$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Phép tính 61 + 5
\begin{ex} %[1D8H29]
Chú thỏ nhổ $61$ củ cà rốt, sau đó nhổ thêm $5$ củ nữa:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-2,0) {$61$};
  \node[font=\bfseries\Large, color=red!85] at (-0.8,0) {$+$};
  \node[draw=orange!80, fill=yellow!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0.2,0) {$5$};
  \node[font=\bfseries\Large, color=blue!80] at (1.2,0) {$=$};
  \node[draw=green!80, fill=lime!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (2.2,0) {?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $61 + 5$ là:
\begin{multicols}{4}
\choice
{$65$}
{\True $66$}
{$67$}
{$68$}
\end{multicols}
\loigiai{
$1 + 5 = 6$; hạ $6$. Vậy $61 + 5 = 66$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Phép tính 72 + 6
\begin{ex} %[1D8H29]
Đoàn tàu hỏa mang toa số có phép tính $72 + 6$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeXePhepTinhCong{0,0}{orange}{$72 + 6$}{~?~}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $72 + 6$ là:
\begin{multicols}{4}
\choice
{$77$}
{\True $78$}
{$79$}
{$88$}
\end{multicols}
\loigiai{
$2 + 6 = 8$; hạ $7$. Vậy $72 + 6 = 78$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Tìm x: x - 4 = 32
\begin{ex} %[1D8H29]
Mảnh ghép bí ẩn chứa phép tính tìm số ban đầu:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=purple!80, fill=pink!20, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {
    $? - 4 = 32$
  };
\end{tikzpicture}
\end{center}
Số thích hợp điền vào dấu \textbf{?} là:
\begin{multicols}{4}
\choice
{$35$}
{\True $36$}
{$37$}
{$38$}
\end{multicols}
\loigiai{
Số cần tìm là: $32 + 4 = 36$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: So sánh hai phép cộng 54 + 3 và 52 + 5
\begin{ex} %[1D8H29]
Cân thăng bằng so sánh hai phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-2.2,0) {$54 + 3$};
  \node[draw=orange!90, fill=yellow!30, rounded corners=2pt, font=\bfseries\normalsize, inner sep=3pt] at (0.2,0) {~?~};
  \node[draw=red!80, fill=pink!20, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (2.2,0) {$52 + 5$};
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
Vế trái: $54 + 3 = 57$. Vế phải: $52 + 5 = 57$. Hai vế bằng nhau nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Bài toán lớp 1A thêm bạn
\begin{ex} %[1D8V29]
Lớp 1A có $32$ bạn, sau đó có thêm $3$ bạn mới chuyển vào:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=cyan!30, draw=blue!80, line width=0.6pt, rounded corners=2pt] (0,0) rectangle (3.2,0.6) node[midway, font=\bfseries\tiny] {Có $32$ bạn};
  \draw[fill=green!35, draw=green!80, line width=0.6pt, rounded corners=2pt] (3.2,0) rectangle (4.6,0.6) node[midway, font=\bfseries\tiny] {Thêm $3$};
  \draw[line width=0.8pt, stealth-stealth, red!85] (0,-0.35) -- (4.6,-0.35) node[midway, below, font=\bfseries\tiny] {Tất cả = ? bạn};
\end{tikzpicture}
\end{center}
Lớp 1A có tất cả số bạn là:
\begin{multicols}{4}
\choice
{$34$ bạn}
{\True $35$ bạn}
{$36$ bạn}
{$37$ bạn}
\end{multicols}
\loigiai{
Lớp 1A có tất cả là: $32 + 3 = 35$ bạn.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Bài toán hái cam
\begin{ex} %[1D8V29]
Mẹ hái được $42$ quả cam, bé hái thêm được $6$ quả cam:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=orange!35, draw=black] (0,0) rectangle (3.6,0.6) node[midway, font=\bfseries\tiny] {Mẹ hái $42$ quả};
  \draw[fill=yellow!45, draw=black] (3.6,0) rectangle (5.2,0.6) node[midway, font=\bfseries\tiny] {Bé hái $6$ quả};
  \draw[line width=0.8pt, stealth-stealth, blue!85] (0,-0.35) -- (5.2,-0.35) node[midway, below, font=\bfseries\tiny] {Cả hai mẹ con = ? quả};
\end{tikzpicture}
\end{center}
Cả hai mẹ con hái được tất cả số quả cam là:
\begin{multicols}{4}
\choice
{$47$ quả}
{\True $48$ quả}
{$49$ quả}
{$50$ quả}
\end{multicols}
\loigiai{
Cả hai mẹ con hái được là: $42 + 6 = 48$ quả cam.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Tính biểu thức 31 + 4 + 2
\begin{ex} %[1D8V29]
Băng giấy chứa dãy tính ba số:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \node[draw=blue!80, fill=cyan!10, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {
    $31 + 4 + 2 = \dots$
  };
\end{tikzpicture}
\end{center}
Giá trị của biểu thức trên là:
\begin{multicols}{4}
\choice
{$36$}
{\True $37$}
{$38$}
{$39$}
\end{multicols}
\loigiai{
Thực hiện từ trái sang phải: $31 + 4 = 35$; sau đó $35 + 2 = 37$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Điền số còn thiếu: 63 + ? = 68
\begin{ex} %[1D8V29]
Tìm số thích hợp điền vào dấu hỏi chấm:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-1.8,0) {$63$};
  \node[font=\bfseries\Large, color=red!85] at (-0.8,0) {$+$};
  \node[draw=red!80, fill=yellow!30, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {?};
  \node[font=\bfseries\Large, color=blue!80] at (0.8,0) {$=$};
  \node[draw=green!80, fill=lime!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (1.8,0) {$68$};
\end{tikzpicture}
\end{center}
Số cần điền vào dấu \textbf{?} là:
\begin{multicols}{4}
\choice
{$4$}
{\True $5$}
{$6$}
{$7$}
\end{multicols}
\loigiai{
Vì $3 + 5 = 8$ nên $63 + 5 = 68$. Số cần điền là $5$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Trồng chuối
\begin{ex} %[1D8V29]
Vườn nhà bác Ba có $51$ cây chuối, bác trồng thêm $8$ cây chuối nữa:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=green!35, draw=black] (0,0) rectangle (3.8,0.6) node[midway, font=\bfseries\tiny] {Có $51$ cây chuối};
  \draw[fill=teal!40, draw=black] (3.8,0) rectangle (5.4,0.6) node[midway, font=\bfseries\tiny] {Thêm $8$ cây};
  \draw[line width=0.8pt, stealth-stealth, orange!90!black] (0,-0.35) -- (5.4,-0.35) node[midway, below, font=\bfseries\tiny] {Tổng số cây = ?};
\end{tikzpicture}
\end{center}
Vườn nhà bác Ba có tất cả số cây chuối là:
\begin{multicols}{4}
\choice
{$58$ cây}
{\True $59$ cây}
{$60$ cây}
{$61$ cây}
\end{multicols}
\loigiai{
Vườn nhà bác Ba có tất cả: $51 + 8 = 59$ cây chuối.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Vận dụng cao - Tìm số ban đầu
\begin{ex} %[1D8C29]
Hộp quà bí ẩn chứa câu đố:
\begin{center}
\begin{tikzpicture}
  \draw[fill=yellow!15, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3.8,-0.6) rectangle (3.8,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black, align=center] at (0,0) {
    ``Khi cộng tôi với $5$, ta được kết quả là $89$.\\
    Hỏi tôi là số nào?''
  };
\end{tikzpicture}
\end{center}
Số bí ẩn là:
\begin{multicols}{4}
\choice
{$83$}
{\True $84$}
{$85$}
{$86$}
\end{multicols}
\loigiai{
Số đó là: $89 - 5 = 84$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Các phép tính cộng
\begin{ex} %[1D8H29]
Bảng con ghi các phép tính cộng:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=blue!10, draw=blue!80, line width=1pt, rounded corners=3pt] (-4,-0.6) rectangle (4,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (-2,0) {$34 + 5 = 39$};
  \node[font=\bfseries\scriptsize, color=red!90!black] at (2,0) {$81 + 7 = 88$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép tính sau:
\choiceTF
{\True Phép tính $34 + 5 = 39$ là đúng.}
{\True Phép tính $81 + 7 = 88$ là đúng.}
{Phép tính $53 + 4 = 58$ là đúng.}
{\True Phép tính $53 + 4 = 57$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $34 + 5 = 39$.
  \item b) \textbf{Đúng}: $81 + 7 = 88$.
  \item c) \textbf{Sai}: $53 + 4 = 57$ (không phải $58$).
  \item d) \textbf{Đúng}: $53 + 4 = 57$.
\end{itemize}
}
\end{ex}

% CÂU 14: Cuộn dây nối thêm
\begin{ex} %[1D8V29]
Cuộn dây dài $42\text{ cm}$, nối thêm một đoạn dài $6\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=cyan!35, draw=black] (0,0) rectangle (4.2,0.6) node[midway, font=\tiny\bfseries] {Đoạn $1$: $42\text{ cm}$};
  \draw[fill=green!40, draw=black] (4.2,0) rectangle (5.4,0.6) node[midway, font=\tiny\bfseries] {Thêm $6\text{ cm}$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các nhận xét sau:
\choiceTF
{\True Chiều dài sợi dây sau khi nối là $48\text{ cm}$.}
{\True Sợi dây mới dài hơn $45\text{ cm}$.}
{Chiều dài sợi dây mới là $50\text{ cm}$.}
{\True Cần nối thêm $2\text{ cm}$ nữa mới đủ $50\text{ cm}$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $42 + 6 = 48\text{ cm}$.
  \item b) \textbf{Đúng}: $48\text{ cm} > 45\text{ cm}$.
  \item c) \textbf{Sai}: Chiều dài là $48\text{ cm}$.
  \item d) \textbf{Đúng}: $50 - 48 = 2\text{ cm}$.
\end{itemize}
}
\end{ex}

% CÂU 15: Quy tắc đặt tính
\begin{ex} %[1D8H29]
Hình minh họa quy tắc đặt tính cột dọc phép tính $25 + 3$:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \VeDatTinhDoc{0,0}{25}{3}{28}
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phát biểu về quy tắc đặt tính:
\choiceTF
{\True Chữ số $3$ viết thẳng cột với chữ số $5$ ở hàng đơn vị.}
{\True Thực hiện cộng từ phải sang trái (cộng hàng đơn vị trước).}
{Viết chữ số $3$ thẳng cột với chữ số $2$ ở hàng chục.}
{\True Kết quả của phép tính là $28$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Số có 1 chữ số phải viết thẳng hàng đơn vị.
  \item b) \textbf{Đúng}: Cộng từ phải sang trái.
  \item c) \textbf{Sai}: Viết thẳng hàng chục là sai bản chất.
  \item d) \textbf{Đúng}: $25 + 3 = 28$.
\end{itemize}
}
\end{ex}

% CÂU 16: So sánh các tổng
\begin{ex} %[1D8V29]
Bốn thẻ ghi các phép tính cộng:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-3,0) {$71 + 4 = 75$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-1,0) {$62 + 7 = 69$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (1,0) {$43 + 6 = 50$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (3,0) {$80 + 9 = 89$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép tính sau:
\choiceTF
{\True $71 + 4 = 75$ là đúng.}
{\True $62 + 7 = 69$ là đúng.}
{Phép tính $43 + 6 = 50$ là đúng.}
{\True $80 + 9 = 89$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $71 + 4 = 75$.
  \item b) \textbf{Đúng}: $62 + 7 = 69$.
  \item c) \textbf{Sai}: $43 + 6 = 49$ (chứ không phải $50$).
  \item d) \textbf{Đúng}: $80 + 9 = 89$.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN / ĐIỀN SỐ) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tính 35 + 4
\begin{ex} %[1D8H29]
Tính kết quả phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!30, draw=blue!80, line width=0.7pt, rounded corners=2pt] (-2.0,-0.4) rectangle (2.0,0.4);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0,0) {$35 + 4 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$39$}}
\loigiai{
$35 + 4 = 39$.\\
\textbf{Đáp số: $39$.}
}
\end{ex}

% CÂU 18: Tính 72 + 6
\begin{ex} %[1D8H29]
Tính kết quả phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=pink!30, draw=red!80, line width=0.7pt, rounded corners=2pt] (-2.0,-0.4) rectangle (2.0,0.4);
  \node[font=\bfseries\normalsize, color=red!90!black] at (0,0) {$72 + 6 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$78$}}
\loigiai{
$72 + 6 = 78$.\\
\textbf{Đáp số: $78$.}
}
\end{ex}

% CÂU 19: Tính giá trị biểu thức 41 + 3 + 4
\begin{ex} %[1D8V29]
Tính giá trị của biểu thức:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=cyan!20, draw=blue!80, line width=0.7pt, rounded corners=2pt] (-2.2,-0.4) rectangle (2.2,0.4);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0,0) {$41 + 3 + 4 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của biểu thức trên là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$48$}}
\loigiai{
$41 + 3 = 44$; sau đó $44 + 4 = 48$.\\
\textbf{Đáp số: $48$.}
}
\end{ex}

% CÂU 20: Vận dụng cao - Điền số vào dấu ?
\begin{ex} %[1D8C29]
Tìm số thích hợp để thay thế dấu \textbf{?}:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!70!orange, draw=black, line width=0.8pt, rounded corners=3pt] (-2.5,-0.45) rectangle (2.5,0.45);
  \node[font=\bfseries\normalsize, color=blue!95!black] at (0,0) {
    $43 + \text{\textbf{?}} = 49$
  };
\end{tikzpicture}
\end{center}
Số thích hợp để điền vào dấu \textbf{?} là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$6$}}
\loigiai{
Số cần tìm là: $49 - 43 = 6$.\\
\textbf{Đáp số: $6$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 8 Bai 29
tex_path = os.path.abspath('CHỦ ĐỀ 8 - PHÉP CỘNG, PHÉP TRỪ (KHÔNG NHỚ) TRONG PHẠM VI 100/Chuong8_Bai29_PhepCongSoCoHaiChuSoVoiSoCoMotChuSo.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_29_preview.tex độc lập 5 trang
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 29: CỘNG SỐ CÓ HAI CHỮ SỐ VỚI SỐ CÓ MỘT CHỮ SỐ},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 8: Phép cộng, phép trừ PV 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-29}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_29_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_29_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_29_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_29_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_29_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_29_Cong_so_2_chu_so_voi_so_1_chu_so.pdf')
    import shutil
    shutil.copy2('Bai_29_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
