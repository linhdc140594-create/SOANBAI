# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 36: THỰC HÀNH XEM LỊCH VÀ GIỜ
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D
% =========================================================================

% --- ĐỊNH NGHĨA MÀU SẮC AN TOÀN ---
\colorlet{myteal}{cyan!70!blue}
\colorlet{myorange}{orange}
\colorlet{mypurple}{purple}
\colorlet{myblue}{blue}
\colorlet{myred}{red}

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 36 ---

% 1. Vẽ đồng hồ kim (mặt tròn có chân đế và kim chỉ số giờ đúng)
\providecommand{\VeDongHoKim}[4]{% #1=scale, #2=(x,y), #3=gio, #4=mau
  \begin{scope}[shift={(#2)}, scale=#1]
    \draw[line width=1.3pt, #4!80] (-0.45,-0.92) -- (-0.72,-1.18);
    \draw[line width=1.3pt, #4!80] (0.45,-0.92) -- (0.72,-1.18);
    \draw[fill=#4!12, draw=#4!85, line width=1.1pt] (0,0) circle (1.14cm);
    \draw[fill=white, draw=black!60, line width=0.6pt] (0,0) circle (0.98cm);
    \foreach \n in {1,...,12} {
      \pgfmathsetmacro{\goc}{90 - \n * 30}
      \draw[line width=0.5pt, black!50] (\goc:0.88cm) -- (\goc:0.96cm);
      \node[font=\bfseries\tiny, color=black!90] at (\goc:0.75cm) {\n};
    }
    % Kim phút (chỉ số 12)
    \draw[line width=1.3pt, -{Latex[length=1.8mm, width=1.2mm]}, blue!85!black] (0,-0.06) -- (0,0.64);
    % Kim giờ (chỉ số #3)
    \pgfmathsetmacro{\gocht}{90 - #3 * 30}
    \draw[line width=1.9pt, -{Latex[length=2.0mm, width=1.6mm]}, red!85!black] (0,-0.04) -- (\gocht:0.45cm);
    \fill[orange!90!black, draw=black!80, line width=0.4pt] (0,0) circle (0.08cm);
  \end{scope}
}

% 2. Vẽ tờ lịch bóc tường / để bàn
\providecommand{\VeToLich}[4]{% #1=(x,y), #2=Thứ, #3=Số/Nội dung, #4=màu
  \begin{scope}[shift={(#1)}]
    \fill[black!70] (-0.45,0.65) circle (0.05cm);
    \fill[black!70] (0.45,0.65) circle (0.05cm);
    \draw[line width=1.0pt, black!50] (-0.45,0.65) -- (-0.45,0.8);
    \draw[line width=1.0pt, black!50] (0.45,0.65) -- (0.45,0.8);
    \draw[fill=white, draw=#4!85, line width=1.0pt, rounded corners=3pt] (-1.0,-0.65) rectangle (1.0,0.65);
    \draw[fill=#4!85, draw=#4!85, rounded corners=2pt] (-1.0,0.22) rectangle (1.0,0.65);
    \node[font=\bfseries\tiny, color=white] at (0,0.44) {#2};
    \node[font=\bfseries\scriptsize, color=#4!90!black] at (0,-0.2) {#3};
  \end{scope}
}

% 3. Đồng hồ điện tử để bàn
\providecommand{\VeDongHoDienTu}[3]{% #1=(x,y), #2=thời gian, #3=màu
  \begin{scope}[shift={(#1)}, scale=0.6]
    \draw[fill=#3!15, draw=#3!85, line width=0.9pt, rounded corners=3pt] (-1.3,-0.48) rectangle (1.3,0.48);
    \draw[fill=black!92, draw=black, rounded corners=2pt] (-1.12,-0.34) rectangle (1.12,0.34);
    \node[font=\bfseries\small, color=green!85!white] at (0,0) {#2};
  \end{scope}
}

% 4. Dải các ngày trong tuần kèm số ngày
\providecommand{\VeDaiTuanCoNgay}[2]{% #1=(x,y), #2=ngày bắt đầu
  \begin{scope}[shift={(#1)}, scale=0.55]
    \foreach \i/\thu/\mau in {0/{Thứ 2}/myblue, 1/{Thứ 3}/myblue, 2/{Thứ 4}/myblue, 3/{Thứ 5}/myblue, 4/{Thứ 6}/myblue, 5/{Thứ 7}/myorange, 6/{CN}/myred} {
      \pgfmathsetmacro{\x}{(\i-3)*1.95}
      \pgfmathtruncatemacro{\ngayso}{#2 + \i}
      \draw[fill=\mau!15, draw=\mau!85, line width=1.0pt, rounded corners=3pt] (\x-0.85,-0.65) rectangle (\x+0.85,0.65);
      \draw[fill=\mau!85, draw=\mau!85, rounded corners=2pt] (\x-0.85,0.2) rectangle (\x+0.85,0.65);
      \node[font=\bfseries\tiny, color=white] at (\x,0.43) {\thu};
      \node[font=\bfseries\small, color=\mau!90!black] at (\x,-0.2) {\ngayso};
    }
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Đọc thông tin trên tờ lịch bóc
\begin{ex} %[1H9N36]
Quan sát tờ lịch treo tường nhà bạn Lan:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{0,0}{THỨ TƯ}{Ngày 15}{myteal}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tờ lịch trên cho biết hôm nay là ngày nào?
\begin{multicols}{2}
\choice
{Thứ Ba, Ngày 15}
{\True Thứ Tư, Ngày 15}
{Thứ Tư, Ngày 16}
{Thứ Năm, Ngày 15}
\end{multicols}
\loigiai{
Quan sát tờ lịch: phần chữ phía trên ghi "THỨ TƯ" và phần số phía dưới ghi "Ngày 15". Vậy hôm nay là Thứ Tư, Ngày 15.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Đọc giờ thức dậy trên đồng hồ kim
\begin{ex} %[1H9N36]
Đồng hồ báo thức reo khi bạn Nam thức dậy tập thể dục buổi sáng:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.6}{0,0}{6}{myorange}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Bạn Nam thức dậy vào lúc mấy giờ?
\begin{multicols}{4}
\choice
{$12$ giờ}
{\True $6$ giờ}
{$7$ giờ}
{$5$ giờ}
\end{multicols}
\loigiai{
Đồng hồ có kim ngắn (kim giờ) chỉ vào số 6 và kim dài (kim phút) chỉ vào số 12. Vậy đồng hồ chỉ đúng 6 giờ sáng.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Lịch ngày kế tiếp
\begin{ex} %[1H9H36]
Quan sát tờ lịch hôm nay và mũi tên chỉ sang tờ lịch ngày mai:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{-2.2,0}{THỨ NĂM}{Ngày 12}{myblue}
  \draw[->, >=stealth, line width=1.3pt, orange!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=blue!90!black] {Ngày mai};
  \VeToLich{2.2,0}{THỨ SÁU}{?}{myred}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hôm nay là Thứ Năm, Ngày 12. Ngày mai là Thứ Sáu, ngày bao nhiêu?
\begin{multicols}{4}
\choice
{Ngày 11}
{\True Ngày 13}
{Ngày 14}
{Ngày 15}
\end{multicols}
\loigiai{
Hôm nay là ngày 12 thì ngày mai kế tiếp sẽ là ngày $12 + 1 = 13$ (Thứ Sáu).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Giờ bắt đầu vào học buổi sáng
\begin{ex} %[1H9H36]
Tiếng trống trường vang lên báo giờ vào học lớp 1:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.6}{0,0}{7}{myblue}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Lớp học của em bắt đầu vào lúc mấy giờ?
\begin{multicols}{4}
\choice
{$6$ giờ}
{\True $7$ giờ}
{$8$ giờ}
{$12$ giờ}
\end{multicols}
\loigiai{
Kim ngắn chỉ số 7, kim dài chỉ số 12. Đồng hồ chỉ đúng 7 giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Kết hợp lịch và đồng hồ cho buổi học đàn
\begin{ex} %[1H9H36]
Lịch và giờ buổi học đàn piano của bạn Mai cuối tuần:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{-1.8,0}{THỨ BẢY}{Ngày 9}{myorange}
  \VeDongHoKim{0.6}{1.8,0}{3}{mypurple}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Buổi học đàn của bạn Mai diễn ra vào thời gian nào?
\begin{multicols}{2}
\choice
{Thứ Bảy, $12$ giờ}
{\True Thứ Bảy, $3$ giờ chiều}
{Chủ nhật, $3$ giờ chiều}
{Thứ Sáu, $9$ giờ}
\end{multicols}
\loigiai{
Tờ lịch ghi Thứ Bảy (ngày 9) và chiếc đồng hồ có kim ngắn chỉ số 3, kim dài chỉ số 12 (3 giờ chiều).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Tính khoảng thời gian giữa 2 đồng hồ
\begin{ex} %[1H9V36]
Bạn An ngồi đọc sách tại thư viện từ lúc đồng hồ A đến lúc đồng hồ B:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.55}{-2.2,0}{8}{myblue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-2.2,-0.85) {Đồng hồ A};
  \draw[->, >=stealth, line width=1.2pt, orange!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=black!80] {Thời gian đọc};
  \VeDongHoKim{0.55}{2.2,0}{10}{myteal}
  \node[font=\bfseries\tiny, color=teal!90!black] at (2.2,-0.85) {Đồng hồ B};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Bạn An đã đọc sách ở thư viện trong khoảng thời gian bao lâu?
\begin{multicols}{4}
\choice
{$1$ giờ}
{\True $2$ giờ}
{$3$ giờ}
{$4$ giờ}
\end{multicols}
\loigiai{
Đồng hồ A chỉ 8 giờ, đồng hồ B chỉ 10 giờ. Thời gian An đọc sách là: $10 - 8 = 2$ giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Xem lịch 1 tuần sau (+7 ngày)
\begin{ex} %[1H9V36]
Hôm nay là Thứ Sáu ngày 8. Thứ Sáu tuần sau là sinh nhật bạn Lan:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{-2.2,0}{THỨ SÁU}{Ngày 8}{myblue}
  \draw[->, >=stealth, line width=1.3pt, purple!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=blue!90!black] {Sau 1 tuần};
  \VeToLich{2.2,0}{THỨ SÁU}{?}{myred}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Sinh nhật của bạn Lan vào ngày mấy?
\begin{multicols}{4}
\choice
{Ngày 14}
{\True Ngày 15}
{Ngày 16}
{Ngày 17}
\end{multicols}
\loigiai{
Một tuần lễ có 7 ngày. Thứ Sáu tuần sau là ngày: $8 + 7 = 15$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: So khớp đồng hồ kim và đồng hồ điện tử
\begin{ex} %[1H9H36]
Chiếc đồng hồ kim treo tường đang chỉ giờ như sau:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.6}{0,0}{9}{myred}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đồng hồ điện tử nào dưới đây chỉ cùng giờ với chiếc đồng hồ trên?
\begin{multicols}{4}
\choice
{\begin{tikzpicture}\VeDongHoDienTu{0,0}{08:00}{gray}\end{tikzpicture}}
{\True \begin{tikzpicture}\VeDongHoDienTu{0,0}{09:00}{blue}\end{tikzpicture}}
{\begin{tikzpicture}\VeDongHoDienTu{0,0}{12:00}{gray}\end{tikzpicture}}
{\begin{tikzpicture}\VeDongHoDienTu{0,0}{06:00}{gray}\end{tikzpicture}}
\end{multicols}
\loigiai{
Đồng hồ kim có kim ngắn chỉ số 9, kim dài chỉ số 12, biểu thị đúng 9 giờ. Đồng hồ điện tử tương ứng hiển thị \textbf{09:00}.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Lịch tuần đi học với các môn học
\begin{ex} %[1H9H36]
Quan sát bảng tuần lễ đi học từ ngày 10 đến ngày 16 của bạn Bình:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDaiTuanCoNgay{0,0}{10}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Biết bạn Bình có tiết học Mỹ thuật vào ngày 12. Hôm đó là thứ mấy?
\begin{multicols}{4}
\choice
{Thứ Ba}
{\True Thứ Tư}
{Thứ Năm}
{Thứ Sáu}
\end{multicols}
\loigiai{
Quan sát dải lịch tuần: Thứ Hai là ngày 10, Thứ Ba là ngày 11, Thứ Tư là ngày 12. Vậy ngày 12 là Thứ Tư.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Chuyến tàu về quê của gia đình
\begin{ex} %[1H9V36]
Gia đình bé xuất phát lúc 7 giờ sáng và tàu tới ga quê lúc 11 giờ trưa:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.55}{-2.2,0}{7}{myorange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (-2.2,-0.85) {Khởi hành: 7 giờ};
  \draw[->, >=stealth, line width=1.3pt, red!85!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=blue!90!black] {Hành trình};
  \VeDongHoKim{0.55}{2.2,0}{11}{myblue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (2.2,-0.85) {Đến nơi: 11 giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Chuyến tàu đi từ nhà về quê kéo dài trong bao nhiêu giờ?
\begin{multicols}{4}
\choice
{$3$ giờ}
{\True $4$ giờ}
{$5$ giờ}
{$6$ giờ}
\end{multicols}
\loigiai{
Chuyến đi kéo dài số giờ là: $11 - 7 = 4$ giờ.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Xem ngày cách tuần theo lịch tháng
\begin{ex} %[1H9V36]
Tờ lịch tháng 4 cho thấy ngày mùng 1 rơi vào Thứ Hai:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{-2.2,0}{THỨ HAI}{Ngày 1}{myblue}
  \draw[->, >=stealth, line width=1.2pt, orange!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=blue!90!black] {+ 7 ngày};
  \VeToLich{2.2,0}{?}{Ngày 8}{myteal}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Ngày 8 tháng 4 sẽ là thứ mấy trong tuần?
\begin{multicols}{4}
\choice
{Chủ nhật}
{\True Thứ Hai}
{Thứ Ba}
{Thứ Tư}
\end{multicols}
\loigiai{
Vì sau đúng 1 tuần lễ (cộng 7 ngày), thứ trong tuần lại lặp lại: $1 + 7 = 8$. Vậy ngày 8 tháng 4 vẫn là ngày Thứ Hai.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Thời gian biểu buổi tối của Minh
\begin{ex} %[1H9C36]
Buổi tối Minh bắt đầu ngồi vào bàn học lúc 7 giờ tối, học trong $2$ giờ rồi đi ngủ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.55}{-2.2,0}{7}{mypurple}
  \node[font=\bfseries\tiny, color=purple!90!black] at (-2.2,-0.85) {Bắt đầu học: 7 giờ};
  \draw[->, >=stealth, line width=1.3pt, teal!85!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=black!80] {Học trong 2 giờ};
  \VeDongHoKim{0.55}{2.2,0}{9}{myblue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (2.2,-0.85) {Đi ngủ: 9 giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Bạn Minh chuẩn bị đi ngủ vào lúc mấy giờ tối?
\begin{multicols}{4}
\choice
{$8$ giờ tối}
{\True $9$ giờ tối}
{$10$ giờ tối}
{$11$ giờ tối}
\end{multicols}
\loigiai{
Minh bắt đầu học lúc 7 giờ tối, học trong 2 giờ: $7 + 2 = 9$ giờ tối. Minh đi ngủ lúc 9 giờ tối.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Đọc 3 đồng hồ kim A, B, C
\begin{ex} %[1H9H36]
Quan sát ba chiếc đồng hồ treo trên tường phòng học:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \VeDongHoKim{0.5}{-3.0,0}{7}{myblue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-3.0,-0.75) {Đồng hồ A};
  \VeDongHoKim{0.5}{0,0}{10}{myorange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (0,-0.75) {Đồng hồ B};
  \VeDongHoKim{0.5}{3.0,0}{12}{myteal}
  \node[font=\bfseries\tiny, color=teal!90!black] at (3.0,-0.75) {Đồng hồ C};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Đồng hồ A đang chỉ 7 giờ đúng.}
{Đồng hồ B đang chỉ 11 giờ đúng.}
{\True Khoảng cách thời gian từ đồng hồ A đến đồng hồ B là 3 giờ.}
{\True Đồng hồ C có cả hai kim cùng chỉ thẳng vào số 12.}
\loigiai{\textbf{a)} Đúng. \textbf{b)} Sai (Đồng hồ B chỉ 10 giờ). \textbf{c)} Đúng ($10 - 7 = 3$ giờ). \textbf{d)} Đúng.}
\end{ex}

% CÂU 14: Lịch tuần và hoạt động của Mai
\begin{ex} %[1H9V36]
Thời khóa biểu một tuần học của bạn Mai từ ngày 12 đến ngày 18:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \VeDaiTuanCoNgay{0,0}{12}
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Thứ Hai là ngày 12 và Chủ nhật là ngày 18.}
{Thứ Năm là ngày 16.}
{\True Thứ Bảy là ngày 17, là một ngày nghỉ cuối tuần của Mai.}
{\True Từ Thứ Hai (ngày 12) đến Thứ Sáu (ngày 16) Mai đi học 5 ngày.}
\loigiai{\textbf{a)} Đúng. \textbf{b)} Sai (Thứ Năm là ngày 15). \textbf{c)} Đúng. \textbf{d)} Đúng (5 ngày: 12, 13, 14, 15, 16).}
\end{ex}

% CÂU 15: Thời gian biểu hoạt động ngày Chủ nhật của Nam
\begin{ex} %[1H9V36]
Các mốc hoạt động ngày Chủ nhật của Nam được biểu thị qua các đồng hồ:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \VeDongHoKim{0.45}{-3.4,0}{8}{myblue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-3.4,-0.7) {8h: Thể thao};
  \VeDongHoKim{0.45}{-1.15,0}{11}{myorange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (-1.15,-0.7) {11h: Ăn trưa};
  \VeDongHoKim{0.45}{1.15,0}{4}{myteal}
  \node[font=\bfseries\tiny, color=teal!90!black] at (1.15,-0.7) {4h: Bơi lội};
  \VeDongHoKim{0.45}{3.4,0}{8}{mypurple}
  \node[font=\bfseries\tiny, color=purple!90!black] at (3.4,-0.7) {8h: Học bài};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Nam chơi thể thao lúc 8 giờ sáng.}
{Nam ăn trưa lúc 12 giờ trưa.}
{\True Nam đi tập bơi lúc 4 giờ chiều.}
{\True Khoảng cách thời gian từ lúc ăn trưa (11h) đến lúc đi bơi (4h chiều) là 5 giờ.}
\loigiai{\textbf{a)} Đúng. \textbf{b)} Sai (Nam ăn trưa lúc 11 giờ). \textbf{c)} Đúng. \textbf{d)} Đúng ($16 - 11 = 5$ giờ).}
\end{ex}

% CÂU 16: Nhận định tổng quát về xem lịch và giờ
\begin{ex} %[1H9H36]
Quan sát đồng hồ kim và tờ lịch bóc hàng ngày:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}
  \VeDongHoKim{0.5}{-1.8,0}{12}{myblue}
  \VeToLich{1.8,0}{CHỦ NHẬT}{Cuối tuần}{myred}
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định dưới đây:
\choiceTF
{\True Kim ngắn chỉ giờ, kim dài chỉ phút trên mặt đồng hồ.}
{Khi kim dài chỉ số 12, kim ngắn chỉ số 5 thì lúc đó là 12 giờ.}
{\True Một tuần lễ luôn có đúng 7 ngày liên tiếp nhau.}
{\True Nếu hôm nay là Thứ Bảy ngày 10 thì Thứ Bảy tuần trước là ngày 3.}
\loigiai{\textbf{a)} Đúng. \textbf{b)} Sai (Khi đó là 5 giờ). \textbf{c)} Đúng. \textbf{d)} Đúng ($10 - 7 = 3$).}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Đọc giờ đồng hồ kim buổi chiều
\begin{ex} %[1H9N36]
Lúc bạn Hoa tan học buổi chiều ở trường, đồng hồ chỉ như hình vẽ dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.65}{0,0}{5}{myteal}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi bạn Hoa tan học lúc mấy giờ chiều?
\shortans{5}
\loigiai{
Kim ngắn chỉ vào số 5 và kim dài chỉ vào số 12. Vậy Hoa tan học lúc 5 giờ chiều.\\
\textbf{Đáp số:} $5$.
}
\end{ex}

% CÂU 18: Tính khoảng thời gian học ở trường
\begin{ex} %[1H9H36]
Buổi sáng em vào lớp học lúc 7 giờ sáng và tan học ăn trưa lúc 11 giờ trưa:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDongHoKim{0.55}{-2.2,0}{7}{myblue}
  \node[font=\bfseries\tiny, color=blue!90!black] at (-2.2,-0.85) {Vào học: 7 giờ};
  \draw[->, >=stealth, line width=1.3pt, orange!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=black!85] {Thời gian học};
  \VeDongHoKim{0.55}{2.2,0}{11}{myorange}
  \node[font=\bfseries\tiny, color=orange!90!black] at (2.2,-0.85) {Tan học: 11 giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi buổi sáng em học tập ở trường trong mấy giờ?
\shortans{4}
\loigiai{
Thời gian học tập ở trường buổi sáng là: $11 - 7 = 4$ giờ.\\
\textbf{Đáp số:} $4$.
}
\end{ex}

% CÂU 19: Tính ngày theo tuần lễ lùi 1 tuần (-7 ngày)
\begin{ex} %[1H9V36]
Chủ nhật tuần này là ngày 14 tháng 5:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{-2.2,0}{CHỦ NHẬT}{?}{myblue}
  \draw[->, >=stealth, line width=1.3pt, purple!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=blue!90!black] {Tuần sau};
  \VeToLich{2.2,0}{CHỦ NHẬT}{Ngày 14}{myred}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi Chủ nhật tuần trước đó là ngày bao nhiêu tháng 5?
\shortans{7}
\loigiai{
Chủ nhật tuần trước cách Chủ nhật tuần này đúng 1 tuần (7 ngày): $14 - 7 = 7$. Vậy là ngày 7 tháng 5.\\
\textbf{Đáp số:} $7$.
}
\end{ex}

% CÂU 20: Tính ngày tiến 1 tuần (+7 ngày)
\begin{ex} %[1H9V36]
Thứ Năm tuần này là ngày 16. Thứ Năm tuần sau gia đình Nam có chuyến dã ngoại:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeToLich{-2.2,0}{THỨ NĂM}{Ngày 16}{myorange}
  \draw[->, >=stealth, line width=1.3pt, teal!90!black] (-0.8,0) -- (0.8,0) node[midway, above=2pt, font=\bfseries\tiny, color=blue!90!black] {Sau 1 tuần};
  \VeToLich{2.2,0}{THỨ NĂM}{?}{myteal}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hỏi chuyến dã ngoại của gia đình Nam diễn ra vào ngày bao nhiêu của tháng đó?
\shortans{23}
\loigiai{
Sau 1 tuần lễ (7 ngày), Thứ Năm tuần sau sẽ là ngày: $16 + 7 = 23$.\\
\textbf{Đáp số:} $23$.
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
    {\footnotesize\bfseries\color{blue!80!black}CHỦ ĐỀ 9 -- THỜI GIAN. GIỜ VÀ LỊCH}\\[2pt]
    {\large\bfseries\color{red!85!black}BÀI 36: THỰC HÀNH XEM LỊCH VÀ GIỜ}\\[2pt]
    {\scriptsize\itshape Thời gian làm bài: 35 phút -- Đề gồm 20 câu chuẩn 5 trang}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.14\textwidth}
    \centering
    \qrcode[height=1.35cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-36}\\[2pt]
    {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
  \end{minipage}
\end{tcolorbox}
\vspace{1mm}

''' + content + r'''
\end{document}
'''

with open("Bai_36_preview.tex", "w", encoding="utf-8") as f:
    f.write(preview_tex)

# Lưu nội dung vào file chương chính
target_chapter = r"CHỦ ĐỀ 9 - THỜI GIAN. GIỜ VÀ LỊCH\Chuong9_Bai36_ThucHanhXemLichVaGio.tex"
with open(target_chapter, "w", encoding="utf-8") as f:
    f.write(content)

print("Đã tạo Bai_36_preview.tex và cập nhật " + target_chapter)
