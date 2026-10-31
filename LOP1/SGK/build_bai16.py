# -*- coding: utf-8 -*-
import os, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 16: LUYỆN TẬP CHUNG (HÌNH KHỐI VÀ VỊ TRÍ KHÔNG GIAN - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 3D
% =========================================================================

% --- CÁC HÀM VẼ KHỐI 3D VÀ HÌNH MINH HỌA CHO BÀI 16 ---

\providecommand{\VeKhoiLapPhuong}[4][yellow!60]{% #1=màu, #2=x, #3=y, #4=cạnh
  \begin{scope}[shift={(#2,#3)}]
    \pgfmathsetmacro{\s}{#4}
    \pgfmathsetmacro{\dx}{\s*0.42}
    \pgfmathsetmacro{\dy}{\s*0.32}
    \draw[fill=#1, draw=black!75, line width=1.1pt] (0,0) rectangle (\s,\s);
    \draw[fill=white!35!#1, draw=black!75, line width=1.1pt] (0,\s) -- (\s,\s) -- (\s+\dx,\s+\dy) -- (\dx,\s+\dy) -- cycle;
    \draw[fill=black!25!#1, draw=black!75, line width=1.1pt] (\s,0) -- (\s+\dx,\dy) -- (\s+\dx,\s+\dy) -- (\s,\s) -- cycle;
  \end{scope}
}

\providecommand{\VeKhoiHopChuNhat}[6][cyan!50]{% #1=màu, #2=x, #3=y, #4=rộng, #5=cao, #6=sâu
  \begin{scope}[shift={(#2,#3)}]
    \pgfmathsetmacro{\w}{#4}
    \pgfmathsetmacro{\h}{#5}
    \pgfmathsetmacro{\dx}{#6*0.42}
    \pgfmathsetmacro{\dy}{#6*0.32}
    \draw[fill=#1, draw=black!75, line width=1.1pt] (0,0) rectangle (\w,\h);
    \draw[fill=white!35!#1, draw=black!75, line width=1.1pt] (0,\h) -- (\w,\h) -- (\w+\dx,\h+\dy) -- (\dx,\h+\dy) -- cycle;
    \draw[fill=black!25!#1, draw=black!75, line width=1.1pt] (\w,0) -- (\w+\dx,\dy) -- (\w+\dx,\h+\dy) -- (\w,\h) -- cycle;
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

% =========================================================================
% PHẦN 1: TRẮC NGHIỆM LỰA CHỌN (12 CÂU)
% =========================================================================
\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- CÂU 1 ---
\begin{ex} %[1H4N16]
Hộp quà sinh nhật hình khối dưới đây có dạng hình gì?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[yellow!60]{-0.7}{-0.7}{1.4}
  \draw[line width=2pt, red!85!black] (0,-0.7) -- (0,0.7) -- (0.3,1.15);
  \draw[line width=2pt, red!85!black] (-0.7,0) -- (0.7,0) -- (1.0,0.45);
  \fill[red!85!black] (0.3,1.15) circle (0.1cm);
  \node[below=4pt, font=\small\bfseries\color{orange!90!black}] at (0,-0.7) {Hộp quà hình khối};
\end{tikzpicture}
\end{center}
\choice
{Khối hộp chữ nhật}
{\True Khối lập phương}
{Khối cầu}
{Khối trụ}
\loigiai{
Hộp quà có các mặt đều là hình vuông bằng nhau nên có dạng \textbf{khối lập phương}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 2 ---
\begin{ex} %[1H4N16]
Bao diêm dưới đây có dạng hình khối gì?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeKhoiHopChuNhat[yellow!60]{-1.3}{-0.5}{2.3}{1.0}{0.9}
  \node[font=\footnotesize\bfseries\color{red!85!black}] at (-0.15,0) {DIÊM};
  \draw[fill=brown!60!black] (1.0,-0.5) -- (1.38,-0.22) -- (1.38,0.78) -- (1.0,0.5) -- cycle;
  \node[below=4pt, font=\small\bfseries\color{brown!80!black}] at (0,-0.5) {Hộp bao diêm};
\end{tikzpicture}
\end{center}
\choice
{Khối lập phương}
{\True Khối hộp chữ nhật}
{Hình chữ nhật phẳng}
{Khối cầu}
\loigiai{
Bao diêm có dạng \textbf{khối hộp chữ nhật}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 3 ---
\begin{ex} %[1H4H16]
Khối lập phương có bao nhiêu mặt vuông bằng nhau?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[cyan!50]{-0.6}{-0.6}{1.2}
\end{tikzpicture}
\end{center}
\choice
{$4$ mặt}
{\True $6$ mặt vuông bằng nhau}
{$8$ mặt}
{$5$ mặt}
\loigiai{
Khối lập phương có \textbf{6 mặt vuông bằng nhau}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 4 ---
\begin{ex} %[1H4H16]
Khi xếp hàng dọc, bạn đứng sau lưng em gọi là bạn đứng ở vị trí nào?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \draw[->, >=stealth, line width=1.3pt, orange!90!black] (-3.0,0.4) -- (-3.8,0.4);
  \node[above=2pt, font=\scriptsize\bfseries\color{orange!90!black}] at (-3.4,0.4) {Phía trước};
  
  \VeBanNho[blue!75]{-2.0}{0}
  \node[below=3pt, font=\small\bfseries\color{blue!85!black}] at (-2.0,-0.1) {Em};
  
  \VeBanNho[red!75]{0}{0}
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (0,-0.1) {Bạn đứng sau lưng};
\end{tikzpicture}
\end{center}
\choice
{Ở trước}
{\True Ở sau}
{Ở trên}
{Ở dưới}
\loigiai{
Bạn đứng sau lưng là ở vị trí \textbf{ở sau}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 5 ---
\begin{ex} %[1H4H16]
Cái mũ đội trên đầu. Cái mũ ở vị trí nào so với đầu của bạn nhỏ?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeBanNho[yellow!85!orange]{0}{0}
  \fill[red!85!black] (-0.2,0.4) -- (0,0.7) -- (0.2,0.4) -- cycle;
  \draw[line width=1.5pt, red!90!black] (-0.3,0.4) -- (0.3,0.4);
  \node[right=8pt, font=\small\bfseries\color{red!85!black}] at (0.2,0.55) {Chiếc mũ};
\end{tikzpicture}
\end{center}
\choice
{Ở dưới}
{\True Ở trên}
{Ở sau}
{Bên trái}
\loigiai{
Chiếc mũ ở vị trí \textbf{ở trên} đầu.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 6 ---
\begin{ex} %[1H4H16]
Đôi dép đi dưới chân. Đôi dép ở vị trí nào so với cơ thể bạn nhỏ?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeBanNho[cyan!75]{0}{0.4}
  \draw[fill=blue!85!black, line width=0.6pt, rounded corners=2pt] (-0.18,-0.18) rectangle (-0.02,-0.08);
  \draw[fill=blue!85!black, line width=0.6pt, rounded corners=2pt] (0.02,-0.18) rectangle (0.18,-0.08);
  \node[right=6pt, font=\small\bfseries\color{blue!90!black}] at (0.2,-0.12) {Đôi dép};
\end{tikzpicture}
\end{center}
\choice
{Ở trên}
{\True Ở dưới}
{Ở giữa}
{Ở sau}
\loigiai{
Đôi dép ở vị trí \textbf{ở dưới} chân.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 7 ---
\begin{ex} %[1H4V16]
Bé xếp các khối lập phương thành hình tháp đồ chơi như hình vẽ: tầng dưới có 3 khối, tầng trên có 1 khối. Hỏi có tất cả bao nhiêu khối lập phương?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[orange!45]{-1.5}{-0.7}{1.0}
  \VeKhoiLapPhuong[orange!45]{-0.5}{-0.7}{1.0}
  \VeKhoiLapPhuong[orange!45]{0.5}{-0.7}{1.0}
  \VeKhoiLapPhuong[yellow!60]{-0.5}{0.3}{1.0}
\end{tikzpicture}
\end{center}
\choice
{$3$ khối}
{\True $4$ khối}
{$5$ khối}
{$6$ khối}
\loigiai{
Số khối lập phương là: $3 + 1 = \textbf{4 khối}$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 8 ---
\begin{ex} %[1H4V16]
Đoàn tàu hỏa đồ chơi gồm đầu tàu là 1 khối hộp chữ nhật và 2 toa xe là các khối lập phương. Có bao nhiêu \textbf{khối lập phương} trong đoàn tàu?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \VeKhoiHopChuNhat[red!45]{-3.2}{-0.5}{1.8}{1.1}{0.8}
  \node[font=\tiny\bfseries\color{white}] at (-2.3,0) {Đầu tàu};
  
  \VeKhoiLapPhuong[yellow!60]{-0.8}{-0.5}{1.0}
  \node[font=\tiny\bfseries\color{orange!90!black}] at (-0.3,0) {Toa 1};
  
  \VeKhoiLapPhuong[cyan!50]{0.8}{-0.5}{1.0}
  \node[font=\tiny\bfseries\color{blue!90!black}] at (1.3,0) {Toa 2};
\end{tikzpicture}
\end{center}
\choice
{$1$ khối}
{\True $2$ khối}
{$3$ khối}
{$4$ khối}
\loigiai{
Có \textbf{2 khối lập phương} làm toa xe.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 9 ---
\begin{ex} %[1H4V16]
Quan sát ngã tư đường: xe ô tô màu đỏ đang rẽ về phía bên nào theo chiều mũi tên?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=gray!20, draw=gray!70!black, line width=1pt] (-2.5,-1.2) rectangle (2.5,1.2);
  \draw[fill=red!75!black, draw=red!90!black, line width=1pt, rounded corners=3pt] (-0.4,-0.8) rectangle (0.4,-0.2);
  \draw[->, >=stealth, line width=2pt, red!85!black] (0,-0.2) to[out=90,in=180] (1.6,0.3);
  \node[above=3pt, font=\small\bfseries\color{red!85!black}] at (1.6,0.3) {Rẽ sang phải};
\end{tikzpicture}
\end{center}
\choice
{Bên trái}
{\True Bên phải}
{Đi thẳng}
{Lùi lại sau}
\loigiai{
Chiếc xe ô tô đang rẽ về phía \textbf{bên phải}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 10 ---
\begin{ex} %[1H4V16]
Trên kệ đồ chơi có 3 chú gấu bông: gấu vàng bên trái, gấu hồng ở giữa, gấu xanh bên phải. Chú gấu hồng nằm ở vị trí nào?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=brown!35, draw=brown!85!black, line width=1.1pt] (-3.5,-0.6) rectangle (3.5,-0.3);
  \fill[yellow!90!orange] (-2.2,0.1) circle (0.35cm);
  \node[below=3pt, font=\small\bfseries\color{orange!90!black}] at (-2.2,-0.65) {Gấu vàng};
  
  \fill[pink!80!red] (0,0.1) circle (0.35cm);
  \node[below=3pt, font=\small\bfseries\color{magenta!85!black}] at (0,-0.65) {Gấu hồng};
  
  \fill[cyan!80!blue] (2.2,0.1) circle (0.35cm);
  \node[below=3pt, font=\small\bfseries\color{blue!90!black}] at (2.2,-0.65) {Gấu xanh};
\end{tikzpicture}
\end{center}
\choice
{Bên trái}
{\True Ở giữa}
{Bên phải}
{Ở trên cao}
\loigiai{
Chú gấu hồng nằm \textbf{ở giữa} gấu vàng và gấu xanh.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 11 ---
\begin{ex} %[1H4V16]
Trong hình tháp dưới đây, khối lập phương màu đỏ nằm ở vị trí nào so với các khối khác?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[cyan!50]{-1.0}{-0.6}{1.0}
  \VeKhoiLapPhuong[cyan!50]{0.2}{-0.6}{1.0}
  \VeKhoiLapPhuong[red!60]{-0.4}{0.4}{1.0}
  \node[right=12pt, font=\small\bfseries\color{red!85!black}] at (0.6,0.9) {Khối đỏ};
\end{tikzpicture}
\end{center}
\choice
{Ở dưới cùng}
{\True Ở trên cùng (cao nhất)}
{Ở đằng sau}
{Ở bên dưới bàn}
\loigiai{
Khối lập phương màu đỏ nằm \textbf{ở trên cùng} (vị trí cao nhất).\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 12 ---
\begin{ex} %[1H4C16]
Khối lập phương lớn gồm 2 tầng, mỗi tầng có 4 khối lập phương nhỏ như hình vẽ. Tổng số khối lập phương nhỏ là bao nhiêu?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[orange!45]{-0.9}{-0.9}{0.9}
  \VeKhoiLapPhuong[orange!45]{0}{-0.9}{0.9}
  \VeKhoiLapPhuong[orange!45]{-0.5}{-0.6}{0.9}
  \VeKhoiLapPhuong[orange!45]{0.4}{-0.6}{0.9}
  \VeKhoiLapPhuong[yellow!60]{-0.9}{0}{0.9}
  \VeKhoiLapPhuong[yellow!60]{0}{0}{0.9}
  \VeKhoiLapPhuong[yellow!60]{-0.5}{0.3}{0.9}
  \VeKhoiLapPhuong[yellow!60]{0.4}{0.3}{0.9}
\end{tikzpicture}
\end{center}
\choice
{$6$ khối}
{\True $8$ khối}
{$10$ khối}
{$4$ khối}
\loigiai{
Mỗi tầng có 4 khối, 2 tầng có: $4 + 4 = \textbf{8 khối lập phương nhỏ}$.\\
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
\begin{ex} %[1H4H16]
Quan sát khối lập phương và khối hộp chữ nhật dưới đây:
\begin{center}
\setlength{\tabcolsep}{15pt}
\begin{tabular}{cc}
  \begin{tikzpicture}[scale=0.8]
    \VeKhoiLapPhuong[yellow!60]{-0.6}{-0.6}{1.2}
    \node[below=3pt, font=\small\bfseries\color{orange!90!black}] at (0,-0.6) {Khối lập phương};
  \end{tikzpicture}
  &
  \begin{tikzpicture}[scale=0.8]
    \VeKhoiHopChuNhat[cyan!50]{-1.0}{-0.6}{2.0}{1.2}{0.8}
    \node[below=3pt, font=\small\bfseries\color{blue!90!black}] at (0,-0.6) {Khối hộp chữ nhật};
  \end{tikzpicture}
\end{tabular}
\end{center}
Xét tính đúng sai của các câu sau:
\choiceTF
{\True Khối lập phương có 6 mặt đều là các hình vuông bằng nhau.}
{\True Khối hộp chữ nhật có 6 mặt.}
{Khối hộp chữ nhật chỉ có 4 mặt.}
{\True Cả khối lập phương và khối hộp chữ nhật đều có đúng 6 mặt.}
\loigiai{
\begin{itemize}
    \item a) \textbf{Đúng}: Khối lập phương có 6 mặt vuông bằng nhau.
    \item b) \textbf{Đúng}: Khối hộp chữ nhật có 6 mặt.
    \item c) \textbf{Sai}: Khối hộp chữ nhật có 6 mặt, không phải 4 mặt.
    \item d) \textbf{Đúng}: Cả hai khối đều có đúng 6 mặt.
\end{itemize}
}
\end{ex}

% --- CÂU 14 ---
\begin{ex} %[1H4V16]
Quan sát bức tranh phong cảnh thiên nhiên:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \fill[brown!75!black] (-2.6,-0.8) rectangle (-2.4,0);
  \fill[green!65!black] (-2.5,0.4) circle (0.45cm);
  \fill[cyan!85!blue] (-2.2,0.4) circle (0.14cm);
  \node[above=2pt, font=\tiny\bfseries\color{blue!90!black}] at (-2.2,0.55) {Chim};
  
  \fill[gray!60] (-0.8,-0.8) circle (0.25cm);
  \fill[orange!35] (0,-0.75) ellipse (0.25cm and 0.16cm);
  \node[above=2pt, font=\tiny\bfseries\color{orange!90!black}] at (0,-0.6) {Thỏ};
  \fill[gray!60] (0.8,-0.8) circle (0.25cm);
  
  \draw[fill=cyan!20, draw=blue!70!black, line width=1pt, rounded corners=4pt] (1.6,-0.9) rectangle (3.4,-0.3);
  \fill[orange!90!black] (2.5,-0.6) ellipse (0.2cm and 0.1cm);
  \node[above=2pt, font=\tiny\bfseries\color{blue!90!black}] at (2.5,-0.3) {Cá};
\end{tikzpicture}
\end{center}
Xét tính đúng sai của các câu sau:
\choiceTF
{\True Chú chim ở trên cành cây.}
{\True Chú cá bơi ở dưới nước.}
{Chú thỏ đang bơi ở trên mặt nước.}
{\True Chú thỏ ở giữa hai tảng đá.}
\loigiai{
\begin{itemize}
    \item a) \textbf{Đúng}: Chú chim đậu trên cành cây.
    \item b) \textbf{Đúng}: Chú cá bơi dưới nước.
    \item c) \textbf{Sai}: Chú thỏ ở trên mặt đất giữa hai tảng đá, không bơi dưới nước.
    \item d) \textbf{Đúng}: Chú thỏ ở giữa hai tảng đá.
\end{itemize}
}
\end{ex}

% =========================================================================
% PHẦN 3: TRẢ LỜI NGẮN (6 CÂU)
% =========================================================================
\textbf{Phần 3. Trả lời ngắn (Quan sát hình vẽ và điền số thích hợp)}
\setcounterpageref{ex}{0}

% --- CÂU 15 ---
\begin{ex} %[1H4H16]
Khối lập phương có tất cả bao nhiêu mặt?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[yellow!60]{-0.6}{-0.6}{1.2}
\end{tikzpicture}
\end{center}
\shortans{6}
\loigiai{
\textbf{Đáp số:} $6$\\
Khối lập phương có $6$ mặt.
}
\end{ex}

% --- CÂU 16 ---
\begin{ex} %[1H4H16]
Khối hộp chữ nhật có tất cả bao nhiêu mặt?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \VeKhoiHopChuNhat[cyan!50]{-1.0}{-0.6}{2.0}{1.2}{0.8}
\end{tikzpicture}
\end{center}
\shortans{6}
\loigiai{
\textbf{Đáp số:} $6$\\
Khối hộp chữ nhật có $6$ mặt.
}
\end{ex}

\newpage
% --- CÂU 17 ---
\begin{ex} %[1H4V16]
Hình chữ T dưới đây được ghép bởi bao nhiêu khối lập phương nhỏ bằng nhau?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \VeKhoiLapPhuong[green!50]{-1.5}{0.2}{1.0}
  \VeKhoiLapPhuong[green!50]{-0.5}{0.2}{1.0}
  \VeKhoiLapPhuong[green!50]{0.5}{0.2}{1.0}
  \VeKhoiLapPhuong[green!50]{-0.5}{-0.8}{1.0}
\end{tikzpicture}
\end{center}
\shortans{4}
\loigiai{
\textbf{Đáp số:} $4$\\
Gồm 3 khối hàng ngang và 1 khối ở dưới: $3 + 1 = 4$ khối.
}
\end{ex}

% --- CÂU 18 ---
\begin{ex} %[1H4V16]
Mô hình chiếc xe tải đồ chơi gồm phần cabin xe và phần thùng xe đều là các khối hộp chữ nhật. Có tất cả bao nhiêu khối hộp chữ nhật trong mô hình?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \VeKhoiHopChuNhat[blue!40]{-2.2}{-0.5}{2.2}{1.3}{0.8}
  \node[font=\tiny\bfseries\color{blue!90!black}] at (-1.1,0.15) {Thùng xe};
  
  \VeKhoiHopChuNhat[red!45]{0.2}{-0.5}{1.2}{1.0}{0.8}
  \node[font=\tiny\bfseries\color{red!85!black}] at (0.8,0) {Cabin};
\end{tikzpicture}
\end{center}
\shortans{2}
\loigiai{
\textbf{Đáp số:} $2$\\
Gồm 1 khối thùng xe và 1 khối cabin: $1 + 1 = 2$ khối hộp chữ nhật.
}
\end{ex}

% --- CÂU 19 ---
\begin{ex} %[1H4V16]
Có bao nhiêu bạn nhỏ xếp hàng đứng \textbf{ở trước} bạn Nam?
\begin{center}
\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]
  \draw[->, >=stealth, line width=1.3pt, orange!90!black] (-5.0,0.4) -- (-5.8,0.4);
  \foreach \i in {0,1,2,3,4} {
    \VeBanNho[cyan!75]{\i*1.1 - 4.5}{0}
  }
  \node[below=3pt, font=\small\bfseries\color{blue!90!black}] at (-2.3,-0.1) {Các bạn đứng trước};
  
  \VeBanNho[red!75]{1.5}{0}
  \node[below=3pt, font=\small\bfseries\color{red!85!black}] at (1.5,-0.1) {Bạn Nam};
\end{tikzpicture}
\end{center}
\shortans{5}
\loigiai{
\textbf{Đáp số:} $5$\\
Có $5$ bạn nhỏ đứng trước bạn Nam.
}
\end{ex}

% --- CÂU 20 ---
\begin{ex} %[1H4C16]
Trong rổ có 10 khối đồ chơi gồm khối lập phương và khối hộp chữ nhật. Biết có 7 khối lập phương, hỏi có bao nhiêu khối hộp chữ nhật?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=blue!6, draw=blue!70!black, line width=1.3pt, rounded corners=6pt] (-3.8,-0.6) rectangle (3.8,0.6);
  \node[font=\large\bfseries\color{blue!90!black}] at (0,0) {10 khối $-$ 7 khối lập phương = ? khối hộp chữ nhật};
\end{tikzpicture}
\end{center}
\shortans{3}
\loigiai{
\textbf{Đáp số:} $3$\\
$10 - 7 = 3$ khối hộp chữ nhật.
}
\end{ex}
'''

# 1. Ghi nội dung vào file bài học
lesson_file = r'CHỦ ĐỀ 4 - LÀM QUEN VỚI MỘT SỐ HÌNH KHỐI/Chuong4_Bai16_LuyenTapChung.tex'
with open(lesson_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Wrote {lesson_file} successfully')

# 2. Lắp ráp file test độc lập theo mẫu chuẩn Bai_01_preview.tex
with open('Bai_01_preview.tex', 'r', encoding='utf-8') as f:
    t1 = f.read()

t1 = t1.replace('BÀI 01: CÁC SỐ 0, 1, 2, 3, 4, 5', 'BÀI 16: LUYỆN TẬP CHUNG')
t1 = t1.replace('CHỦ ĐỀ 1 -- CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 4 -- LÀM QUEN VỚI MỘT SỐ HÌNH KHỐI')
t1 = t1.replace('bai-01', 'bai-16')
t1 = t1.replace('Chuong1_Bai01_CacSo0_1_2_3_4_5.tex', 'Chuong4_Bai16_LuyenTapChung.tex')
t1 = t1.replace('CHỦ ĐỀ 1 - CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 4 - LÀM QUEN VỚI MỘT SỐ HÌNH KHỐI')

test_file = 'test_bai16.tex'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(t1)
print(f'Created {test_file} successfully')
