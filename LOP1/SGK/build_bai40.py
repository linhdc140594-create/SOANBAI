# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 40: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D
% =========================================================================

% --- ĐỊNH NGHĨA MÀU SẮC AN TOÀN ---
\colorlet{myteal}{cyan!70!blue}
\colorlet{myorange}{orange}
\colorlet{mypurple}{purple}
\colorlet{myblue}{blue}
\colorlet{myred}{red}

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 40 ---

% 1. Vẽ đồng hồ kim tròn
\providecommand{\VeBamiMuoiDongHo}[3]{% #1=(x,y), #2=giờ, #3=phút
  \begin{scope}[shift={(#1)}, scale=0.48]
    \draw[fill=blue!5, draw=blue!85, line width=1.3pt] (0,0) circle (1.25cm);
    \draw[fill=blue!85] (0,0) circle (0.07cm);
    \foreach \h in {1,...,12} {
      \pgfmathsetmacro{\ang}{90 - \h * 30}
      \draw[line width=0.6pt, blue!70] (\ang:1.1cm) -- (\ang:1.23cm);
      \ifcase\h\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {1};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {2};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {3};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {4};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {5};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {6};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {7};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {8};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {9};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {10};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {11};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {12};\fi
    }
    % Kim giờ (ngắn)
    \pgfmathsetmacro{\hAng}{90 - (#2 + #3/60)*30}
    \draw[->, >=stealth, line width=1.5pt, red!85!black] (0,0) -- (\hAng:0.65cm);
    % Kim phút (dài)
    \pgfmathsetmacro{\mAng}{90 - #3*6}
    \draw[->, >=stealth, line width=1.1pt, blue!90!black] (0,0) -- (\mAng:0.95cm);
  \end{scope}
}

% 2. Vẽ khối lập phương 3D
\providecommand{\VeBamiMuoiKhoiLapPhuong}[2]{% #1=(x,y), #2=scale
  \begin{scope}[shift={(#1)}, scale=#2]
    \draw[fill=blue!15, draw=blue!85, line width=0.8pt] (0,0) rectangle (1.2,1.2);
    \draw[fill=blue!25, draw=blue!85, line width=0.8pt] (0,1.2) -- (0.5,1.6) -- (1.7,1.6) -- (1.2,1.2) -- cycle;
    \draw[fill=blue!10, draw=blue!85, line width=0.8pt] (1.2,0) -- (1.7,0.4) -- (1.7,1.6) -- (1.2,1.2) -- cycle;
  \end{scope}
}

% 3. Vẽ khối hộp chữ nhật 3D
\providecommand{\VeBamiMuoiKhoiHopCN}[2]{% #1=(x,y), #2=scale
  \begin{scope}[shift={(#1)}, scale=#2]
    \draw[fill=teal!15, draw=teal!85, line width=0.8pt] (0,0) rectangle (1.8,1.0);
    \draw[fill=teal!25, draw=teal!85, line width=0.8pt] (0,1.0) -- (0.5,1.4) -- (2.3,1.4) -- (1.8,1.0) -- cycle;
    \draw[fill=teal!10, draw=teal!85, line width=0.8pt] (1.8,0) -- (2.3,0.4) -- (2.3,1.4) -- (1.8,1.0) -- cycle;
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Hình nào có 3 cạnh và 3 đỉnh?
\begin{ex} %[1H10N40]
Quan sát bốn hình phẳng dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  % Hình vuông
  \draw[fill=teal!15, draw=teal!80, line width=1pt] (-4.5,-0.5) rectangle (-3.3,0.7);
  \node[below=2pt, font=\bfseries\tiny, color=teal!90!black] at (-3.9,-0.5) {Hình vuông};
  % Hình tam giác
  \draw[fill=orange!15, draw=orange!80, line width=1pt] (-1.9,-0.5) -- (-0.7,-0.5) -- (-1.3,0.7) -- cycle;
  \node[below=2pt, font=\bfseries\tiny, color=orange!90!black] at (-1.3,-0.5) {Hình tam giác};
  % Hình tròn
  \draw[fill=purple!15, draw=purple!80, line width=1pt] (1.3,0.1) circle (0.6cm);
  \node[below=2pt, font=\bfseries\tiny, color=purple!90!black] at (1.3,-0.5) {Hình tròn};
  % Hình chữ nhật
  \draw[fill=blue!15, draw=blue!80, line width=1pt] (3.0,-0.5) rectangle (4.6,0.7);
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (3.8,-0.5) {Hình chữ nhật};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hình nào sau đây có $3$ cạnh và $3$ đỉnh?
\begin{multicols}{4}
\choice
{Hình vuông}
{\True Hình tam giác}
{Hình chữ nhật}
{Hình tròn}
\end{multicols}
\loigiai{
Hình tam giác có $3$ cạnh và $3$ đỉnh.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Khối lập phương có bao nhiêu mặt vuông?
\begin{ex} %[1H10N40]
Quan sát khối lập phương đồ chơi dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeBamiMuoiKhoiLapPhuong{-0.85,-0.8}{1.0}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Khối lập phương có tất cả bao nhiêu mặt vuông?
\begin{multicols}{4}
\choice
{$4$ mặt}
{\True $6$ mặt}
{$8$ mặt}
{$12$ mặt}
\end{multicols}
\loigiai{
Khối lập phương có $6$ mặt và tất cả đều là các hình vuông bằng nhau.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Phép cộng đoạn thẳng xăng-ti-mét 35 cm + 24 cm
\begin{ex} %[1H10H40]
Ghép hai thanh thước đo độ dài:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-2.0,0) {\bfseries\small\color{orange!90!black} $35\text{ cm}$};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (2.0,0) {\bfseries\small\color{teal!90!black} $24\text{ cm}$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $35\text{ cm} + 24\text{ cm}$ là
\begin{multicols}{4}
\choice
{$58\text{ cm}$}
{\True $59\text{ cm}$}
{$60\text{ cm}$}
{$61\text{ cm}$}
\end{multicols}
\loigiai{
Cộng số đo kèm theo đơn vị: $35 + 24 = 59\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Phép trừ độ dài xăng-ti-mét 68 cm - 25 cm
\begin{ex} %[1H10H40]
Đoạn dây dài $68\text{ cm}$, cắt bớt đi một đoạn $25\text{ cm}$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.2,0) {\bfseries\small\color{blue!90!black} $68\text{ cm}$};
  \node[draw=red!80, fill=yellow!20, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (2.2,0) {\bfseries\small\color{red!90!black} Còn lại: ?};
  \draw[->, >=stealth, line width=1.2pt, red!85!black] (A) -- (B) node[midway, above=2pt, font=\bfseries\tiny, color=red!90!black] {Cắt bớt $25\text{ cm}$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Độ dài của đoạn dây còn lại là
\begin{multicols}{4}
\choice
{$42\text{ cm}$}
{\True $43\text{ cm}$}
{$44\text{ cm}$}
{$45\text{ cm}$}
\end{multicols}
\loigiai{
Thực hiện phép trừ kèm theo đơn vị: $68\text{ cm} - 25\text{ cm} = 43\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Đồng hồ chỉ 9 giờ đúng
\begin{ex} %[1H10H40]
Quan sát mặt chiếc đồng hồ treo tường dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeBamiMuoiDongHo{0,0}{9}{0}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Khi đồng hồ chỉ $9$ giờ đúng thì kim dài (kim phút) chỉ vào số nào?
\begin{multicols}{4}
\choice
{Số 9}
{\True Số 12}
{Số 6}
{Số 3}
\end{multicols}
\loigiai{
Khi đồng hồ chỉ giờ đúng, kim ngắn chỉ vào số giờ ($9$), còn kim dài luôn chỉ thẳng vào số $12$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Một tuần lễ có bao nhiêu ngày
\begin{ex} %[1H10H40]
Quan sát các tờ lịch ghi các ngày trong một tuần lễ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.7]
  \foreach \i/\thu/\mau in {1/T2/blue, 2/T3/teal, 3/T4/teal, 4/T5/teal, 5/T6/teal, 6/T7/orange, 7/CN/red} {
    \pgfmathsetmacro{\x}{(\i-4)*1.45}
    \node[draw=\mau!80, fill=\mau!12, line width=1pt, rounded corners=3pt, inner xsep=4pt, inner ysep=3pt] at (\x,0) {\bfseries\scriptsize \thu};
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Một tuần lễ gồm có bao nhiêu ngày?
\begin{multicols}{4}
\choice
{$5$ ngày}
{\True $7$ ngày}
{$6$ ngày}
{$8$ ngày}
\end{multicols}
\loigiai{
Một tuần lễ gồm $7$ ngày: Thứ Hai, Thứ Ba, Thứ Tư, Thứ Năm, Thứ Sáu, Thứ Bảy, Chủ nhật.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Xếp que tính tạo hình vuông và tam giác
\begin{ex} %[1H10V40]
Dùng các que tính riêng biệt để xếp một hình vuông và một hình tam giác:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.7]
  % Hình vuông: 4 que tính
  \draw[line width=2pt, blue!80] (-3.0,-0.6) -- (-1.6,-0.6);
  \draw[line width=2pt, blue!80] (-1.6,-0.6) -- (-1.6,0.8);
  \draw[line width=2pt, blue!80] (-1.6,0.8) -- (-3.0,0.8);
  \draw[line width=2pt, blue!80] (-3.0,0.8) -- (-3.0,-0.6);
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (-2.3,-0.6) {Hình vuông (4 que)};
  % Dấu cộng
  \node[font=\bfseries\large, color=black!60] at (0,0.1) {$+$};
  % Hình tam giác: 3 que tính
  \draw[line width=2pt, orange!85] (1.6,-0.6) -- (3.0,-0.6);
  \draw[line width=2pt, orange!85] (3.0,-0.6) -- (2.3,0.8);
  \draw[line width=2pt, orange!85] (2.3,0.8) -- (1.6,-0.6);
  \node[below=2pt, font=\bfseries\tiny, color=orange!90!black] at (2.3,-0.6) {Hình tam giác (3 que)};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Cần tất cả bao nhiêu que tính để xếp được hai hình riêng biệt đó?
\begin{multicols}{4}
\choice
{$6$ que}
{\True $7$ que}
{$8$ que}
{$9$ que}
\end{multicols}
\loigiai{
Hình vuông cần $4$ que tính, hình tam giác cần $3$ que tính: $4 + 3 = 7$ que tính.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Đoạn thẳng AB và CD
\begin{ex} %[1H10V40]
Đoạn thẳng $AB$ dài $45\text{ cm}$, đoạn thẳng $CD$ dài $32\text{ cm}$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-2.2,0) {\bfseries\small\color{orange!90!black} $AB = 45\text{ cm}$};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (2.2,0) {\bfseries\small\color{teal!90!black} $CD = 32\text{ cm}$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Cả hai đoạn thẳng dài tất cả là
\begin{multicols}{4}
\choice
{$76\text{ cm}$}
{\True $77\text{ cm}$}
{$78\text{ cm}$}
{$79\text{ cm}$}
\end{multicols}
\loigiai{
Tổng độ dài của hai đoạn thẳng là: $45 + 32 = 77\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Cuộn dây dài 80 cm cắt bớt 30 cm
\begin{ex} %[1H10V40]
Cuộn dây đo dài $80\text{ cm}$, người ta cắt bớt đi một đoạn dài $30\text{ cm}$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.85]
  % Đoạn đã cắt
  \draw[fill=red!20, draw=red!80, line width=1pt, rounded corners=2pt] (-3.0,-0.35) rectangle (-0.7,0.35);
  \node[font=\bfseries\scriptsize, color=red!85!black] at (-1.85,0) {Cắt $30\text{ cm}$};
  % Đoạn còn lại
  \draw[fill=green!20, draw=green!70!black, line width=1pt, rounded corners=2pt] (-0.6,-0.35) rectangle (3.0,0.35);
  \node[font=\bfseries\scriptsize, color=green!70!black] at (1.2,0) {Còn lại: ? cm};
  % Tổng
  \node[above=3pt, font=\bfseries\footnotesize, color=blue!90!black] at (0,0.4) {Cả cuộn dây: $80\text{ cm}$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đoạn dây còn lại dài bao nhiêu xăng-ti-mét?
\begin{multicols}{4}
\choice
{$40\text{ cm}$}
{\True $50\text{ cm}$}
{$60\text{ cm}$}
{$70\text{ cm}$}
\end{multicols}
\loigiai{
Đoạn dây còn lại dài: $80 - 30 = 50\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Hôm nay là Thứ Năm, 3 ngày sau là thứ mấy?
\begin{ex} %[1H10V40]
Sơ đồ tiến trình ngày trong tuần từ Thứ Năm:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N0) at (-4.2,0) {\bfseries\scriptsize Thứ Năm};
  \node[draw=gray!70, fill=gray!10, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N1) at (-1.4,0) {\bfseries\scriptsize Thứ Sáu};
  \node[draw=gray!70, fill=gray!10, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N2) at (1.4,0) {\bfseries\scriptsize Thứ Bảy};
  \node[draw=red!80, fill=yellow!25, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N3) at (4.2,0) {\bfseries\scriptsize\color{red!90!black} ?};
  \draw[->, >=stealth, line width=1pt, blue!70] (N0) -- (N1) node[midway, above=1pt, font=\tiny] {1 ngày};
  \draw[->, >=stealth, line width=1pt, blue!70] (N1) -- (N2) node[midway, above=1pt, font=\tiny] {2 ngày};
  \draw[->, >=stealth, line width=1pt, red!85] (N2) -- (N3) node[midway, above=1pt, font=\tiny] {3 ngày};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Nếu hôm nay là Thứ Năm thì $3$ ngày sau sẽ là thứ mấy?
\begin{multicols}{4}
\choice
{Thứ Bảy}
{\True Chủ nhật}
{Thứ Sáu}
{Thứ Hai}
\end{multicols}
\loigiai{
Đếm thêm 3 ngày: Thứ Sáu (1 ngày sau), Thứ Bảy (2 ngày sau), Chủ nhật (3 ngày sau).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Nam đi ngủ 9 giờ tối, dậy 6 giờ sáng
\begin{ex} %[1H10V40]
Hai mốc thời gian biểu trong đêm của Nam:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.85]
  \VeBamiMuoiDongHo{-2.4,0}{9}{0}
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (-2.4,-0.65) {Đi ngủ: 9 giờ tối};
  \draw[->, >=stealth, line width=1.2pt, purple!85] (-1.0,0) -- (1.0,0) node[midway, above=1pt, font=\bfseries\tiny, color=purple!90!black] {Thời gian ngủ: ?};
  \VeBamiMuoiDongHo{2.4,0}{6}{0}
  \node[below=2pt, font=\bfseries\tiny, color=orange!90!black] at (2.4,-0.65) {Thức dậy: 6 giờ sáng};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi Nam đã ngủ trong tất cả bao nhiêu giờ?
\begin{multicols}{4}
\choice
{$8$ giờ}
{\True $9$ giờ}
{$10$ giờ}
{$7$ giờ}
\end{multicols}
\loigiai{
Từ 9 giờ tối đến 12 giờ đêm là $3$ giờ; từ 12 giờ đêm đến 6 giờ sáng là $6$ giờ. Tổng thời gian ngủ: $3 + 6 = 9$ giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Có 10 que tính, xếp được nhiều nhất bao nhiêu hình vuông
\begin{ex} %[1H10C40]
Dùng 10 que tính xếp các hình vuông riêng biệt (mỗi hình cần 4 que):
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  % Hình vuông 1
  \draw[line width=1.8pt, blue!85] (-3.0,-0.5) rectangle (-1.8,0.7);
  \node[below=2pt, font=\tiny\bfseries, color=blue!85] at (-2.4,-0.5) {Hình 1};
  % Hình vuông 2
  \draw[line width=1.8pt, teal!85] (-0.6,-0.5) rectangle (0.6,0.7);
  \node[below=2pt, font=\tiny\bfseries, color=teal!85] at (0,-0.5) {Hình 2};
  % 2 que dư
  \draw[line width=1.8pt, red!85] (1.8,-0.5) -- (1.8,0.7);
  \draw[line width=1.8pt, red!85] (2.4,-0.5) -- (2.4,0.7);
  \node[below=2pt, font=\tiny\bfseries, color=red!85] at (2.1,-0.5) {Dư 2 que};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Có 10 que tính, xếp được nhiều nhất bao nhiêu hình vuông riêng biệt?
\begin{multicols}{4}
\choice
{$1$ hình}
{\True $2$ hình (dư $2$ que)}
{$3$ hình}
{$4$ hình}
\end{multicols}
\loigiai{
Xếp 2 hình vuông cần $4 + 4 = 8$ que tính. Còn thừa $10 - 8 = 2$ que tính (không đủ xếp thêm hình vuông thứ 3).\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Đặc điểm hình học
\begin{ex} %[1H10H40]
Quan sát hình ảnh các hình và khối hình học:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.75]
  % 1. Hình vuông
  \draw[fill=teal!15, draw=teal!80, line width=0.8pt] (-5.4,-0.4) rectangle (-4.2,0.6);
  \node[below=2pt, font=\tiny\bfseries, color=teal!90!black] at (-4.8,-0.4) {Hình vuông};
  % 2. Khối hộp chữ nhật
  \VeBamiMuoiKhoiHopCN{-2.35,-0.4}{0.65}
  \node[below=2pt, font=\tiny\bfseries, color=teal!90!black] at (-1.6,-0.4) {Khối hộp CN};
  % 3. Hình tròn
  \draw[fill=purple!15, draw=purple!80, line width=0.8pt] (1.6,0.1) circle (0.5cm);
  \node[below=2pt, font=\tiny\bfseries, color=purple!90!black] at (1.6,-0.4) {Hình tròn};
  % 4. Khối lập phương
  \VeBamiMuoiKhoiLapPhuong{4.25,-0.4}{0.65}
  \node[below=2pt, font=\tiny\bfseries, color=blue!90!black] at (4.8,-0.4) {Khối lập phương};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Hình vuông có 4 cạnh bằng nhau.}
{\True Khối hộp chữ nhật có 6 mặt.}
{Hình tròn có 4 đỉnh.}
{\True Khối lập phương có tất cả 6 mặt đều là hình vuông.}
\loigiai{\textbf{a)} Đúng (Hình vuông có 4 cạnh dài bằng nhau). \textbf{b)} Đúng (Khối hộp chữ nhật có 6 mặt). \textbf{c)} Sai (Hình tròn là đường cong tròn khép kín, không có cạnh và không có đỉnh). \textbf{d)} Đúng (Cả 6 mặt đều là hình vuông).}
\end{ex}

% CÂU 14: Đoạn thẳng thứ nhất và thứ hai
\begin{ex} %[1H10V40]
Hai đoạn thẳng đặt song song so sánh độ dài:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.75]
  \draw[line width=3pt, blue!80] (-3.0,0.3) -- (0,0.3) node[midway, above=1pt, font=\bfseries\tiny, color=blue!85] {Đoạn 1: $30\text{ cm}$};
  \draw[line width=3pt, orange!85] (-3.0,-0.3) -- (2.0,-0.3) node[midway, below=1pt, font=\bfseries\tiny, color=orange!85] {Đoạn 2: $50\text{ cm}$};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True Cả hai đoạn dài tất cả $80\text{ cm}$ ($30 + 50 = 80$).}
{\True Đoạn thứ hai dài hơn đoạn thứ nhất $20\text{ cm}$ ($50 - 30 = 20$).}
{Tổng độ dài hai đoạn ngắn hơn $70\text{ cm}$.}
{\True Đoạn thứ nhất ngắn hơn đoạn thứ hai $20\text{ cm}$.}
\loigiai{\textbf{a)} Đúng ($30 + 50 = 80\text{ cm}$). \textbf{b)} Đúng ($50 - 30 = 20\text{ cm}$). \textbf{c)} Sai (Vì $80\text{ cm} > 70\text{ cm}$, không ngắn hơn). \textbf{d)} Đúng ($50 - 30 = 20\text{ cm}$).}
\end{ex}

% CÂU 15: Thời gian và lịch
\begin{ex} %[1H10H40]
Thời gian một tuần lễ và mặt đồng hồ chỉ $3$ giờ:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.8]
  \node[draw=teal!75, fill=teal!8, line width=0.8pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-2.5,0) {\bfseries\scriptsize Một tuần = 7 ngày};
  \VeBamiMuoiDongHo{2.2,0}{3}{0}
  \node[below=1pt, font=\bfseries\tiny, color=blue!85] at (2.2,-0.65) {3 giờ đúng};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True Một tuần lễ có 7 ngày.}
{\True Ngày đầu tuần là Thứ Hai, ngày cuối tuần là Chủ nhật.}
{Một ngày có 12 giờ.}
{\True Lúc 3 giờ đúng, kim ngắn chỉ số 3 và kim dài chỉ số 12.}
\loigiai{\textbf{a)} Đúng (7 ngày). \textbf{b)} Đúng (Thứ Hai đến Chủ nhật). \textbf{c)} Sai (Một ngày có 24 giờ, không phải 12 giờ). \textbf{d)} Đúng (Giờ đúng thì kim dài luôn chỉ số 12).}
\end{ex}

% CÂU 16: Đổi đơn vị và so sánh độ dài
\begin{ex} %[1H10H40]
Thước dây cuộn đo độ dài $1\text{ m}$ (mét) và xăng-ti-mét ($\text{cm}$):
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \node[draw=purple!75, fill=purple!8, line width=0.8pt, rounded corners=3pt, inner xsep=5pt, inner ysep=3pt] at (-3.6,0) {\bfseries\scriptsize $1\text{ m} = 100\text{ cm}$};
  \node[draw=blue!75, fill=blue!8, line width=0.8pt, rounded corners=3pt, inner xsep=5pt, inner ysep=3pt] at (0,0) {\bfseries\scriptsize $100\text{ cm} - 40\text{ cm} = 60\text{ cm}$};
  \node[draw=teal!75, fill=teal!8, line width=0.8pt, rounded corners=3pt, inner xsep=5pt, inner ysep=3pt] at (3.6,0) {\bfseries\scriptsize $20\text{ cm} + 80\text{ cm} = 1\text{ m}$};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True $1\text{ m} = 100\text{ cm}$.}
{\True $100\text{ cm} - 40\text{ cm} = 60\text{ cm}$.}
{\True $20\text{ cm} + 80\text{ cm} = 100\text{ cm} = 1\text{ m}$.}
{Độ dài $10\text{ cm}$ dài hơn $1\text{ m}$.}
\loigiai{\textbf{a)} Đúng ($1\text{ m} = 100\text{ cm}$). \textbf{b)} Đúng ($100 - 40 = 60\text{ cm}$). \textbf{c)} Đúng ($20 + 80 = 100\text{ cm} = 1\text{ m}$). \textbf{d)} Sai (Vì $10\text{ cm} < 100\text{ cm} = 1\text{ m}$).}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Hình tam giác có bao nhiêu cạnh
\begin{ex} %[1H10H40]
Quan sát hình tam giác với các cạnh được tô màu:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[line width=2pt, blue!85] (-1.6,-0.6) -- (1.6,-0.6) node[midway, below=1pt, font=\bfseries\tiny, color=blue!85] {cạnh 1};
  \draw[line width=2pt, orange!85] (1.6,-0.6) -- (0,1.2) node[midway, right=1pt, font=\bfseries\tiny, color=orange!85] {cạnh 2};
  \draw[line width=2pt, teal!85] (0,1.2) -- (-1.6,-0.6) node[midway, left=1pt, font=\bfseries\tiny, color=teal!85] {cạnh 3};
  \fill[red!85] (-1.6,-0.6) circle (0.1cm);
  \fill[red!85] (1.6,-0.6) circle (0.1cm);
  \fill[red!85] (0,1.2) circle (0.1cm);
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hình tam giác có tất cả bao nhiêu cạnh?
\shortans{3}
\loigiai{
Hình tam giác có $3$ cạnh và $3$ đỉnh.\\
\textbf{Đáp số:} $3$.
}
\end{ex}

% CÂU 18: Tính 40 cm + 30 cm
\begin{ex} %[1H10H40]
Hai thanh gỗ ghép nối tiếp nhau:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-1.8,0) {\bfseries\small\color{orange!90!black} $40\text{ cm}$};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=orange!80, fill=orange!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (1.8,0) {\bfseries\small\color{orange!90!black} $30\text{ cm}$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tính giá trị của phép tính: $40\text{ cm} + 30\text{ cm}$ (theo xăng-ti-mét).
\shortans{70}
\loigiai{
Thực hiện phép tính: $40 + 30 = 70\text{ cm}$.\\
\textbf{Đáp số:} $70$.
}
\end{ex}

% CÂU 19: Tính 95 cm - 42 cm
\begin{ex} %[1H10V40]
Sợi dây vải dài $95\text{ cm}$, đã cắt bớt một đoạn dài $42\text{ cm}$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.3,0) {\bfseries\small\color{blue!90!black} $95\text{ cm}$};
  \node[draw=red!80, fill=yellow!20, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (2.3,0) {\bfseries\small\color{red!90!black} Còn lại: ?};
  \draw[->, >=stealth, line width=1.3pt, red!85!black] (A) -- (B) node[midway, above=2pt, font=\bfseries\tiny, color=red!90!black] {Bớt $42\text{ cm}$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đoạn dây vải còn lại dài bao nhiêu xăng-ti-mét?
\shortans{53}
\loigiai{
Đoạn dây còn lại dài: $95 - 42 = 53\text{ cm}$.\\
\textbf{Đáp số:} $53$.
}
\end{ex}

% CÂU 20: Cần bao nhiêu que tính để xếp 3 hình tam giác riêng biệt
\begin{ex} %[1H10C40]
Xếp ba hình tam giác hoàn toàn riêng biệt:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \foreach \i/\mau in {1/blue, 2/teal, 3/orange} {
    \pgfmathsetmacro{\x}{(\i-2)*2.4}
    \draw[line width=1.8pt, \mau!85] (\x-0.7,-0.5) -- (\x+0.7,-0.5) -- (\x,0.8) -- cycle;
    \node[below=2pt, font=\tiny\bfseries, color=\mau!90!black] at (\x,-0.5) {3 que};
  }
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Cần bao nhiêu que tính để xếp được 3 hình tam giác riêng biệt như trên?
\shortans{9}
\loigiai{
Mỗi hình tam giác cần $3$ que tính: $3 + 3 + 3 = 9$ que tính.\\
\textbf{Đáp số:} $9$.
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
    {\large\bfseries\color{red!85!black}BÀI 40: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG}\\[2pt]
    {\scriptsize\itshape Thời gian làm bài: 35 phút -- Đề gồm 20 câu chuẩn 5 trang}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.14\textwidth}
    \centering
    \qrcode[height=1.35cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-40}\\[2pt]
    {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
  \end{minipage}
\end{tcolorbox}
\vspace{1mm}

''' + content + r'''
\end{document}
'''

with open("Bai_40_preview.tex", "w", encoding="utf-8") as f:
    f.write(preview_tex)

# Lưu nội dung vào file chương chính
target_chapter = r"CHỦ ĐỀ 10 - ÔN TẬP CUỐI NĂM\Chuong10_Bai40_OnTapHinhHocVaDoLuong.tex"
with open(target_chapter, "w", encoding="utf-8") as f:
    f.write(content)

print("Đã tạo Bai_40_preview.tex và cập nhật " + target_chapter)
