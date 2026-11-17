import os
import subprocess
import pymupdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def create_tex():
    tex = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{array}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage[top=0.55cm, bottom=0.55cm, left=0.75cm, right=0.75cm]{geometry}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\fboxsep}{3pt}
\setlength{\fboxrule}{0.5pt}

% Dòng kẻ chấm mờ cự ly chuẩn viết tay học sinh THPT (18.5pt)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{0.7mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!55}\dotfill}\par%
  }%
  \vspace{0.2mm}%
  \endgroup%
}

% Ô bài tập có dòng kẻ
\newcommand{\oBaiTap}[3][5]{%
  \vspace{0.5mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

% Khung ghi nhớ / phương pháp nổi bật đầu trang
\newcommand{\khungGhiNho}[2]{%
  \noindent\fbox{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \textbf{\color{blue!80!black}#1: }#2%
    }%
  }%
  \vspace{0.8mm}%
}

\begin{document}
\pagestyle{empty}

% =============================================================================
% TRANG 1: RÈN PHẢN XẠ CÔNG THỨC MỞ RỘNG BẬC NHẤT ax + b
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 1/8} \\
\textit{Trung tâm Toán Thầy Lĩnh -- Chuyên đề Lớp 12 GDPT 2018} & \textit{Tập 2: Rèn phản xạ \& kỹ năng biến đổi} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\noindent
\begin{tabularx}{\linewidth}{|X|p{3.5cm}|p{3.5cm}|}
\hline
\rule[-1.2mm]{0pt}{6.0mm}\textbf{Họ và tên:} \dotfill & \textbf{Lớp:} \makebox[2cm]{\dotfill} & \textbf{Điểm số:} \makebox[2cm]{\dotfill} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{CÔNG THỨC VÀNG BẬC NHẤT $ax + b$}{%
$\displaystyle\int f(ax+b)\,dx = \frac{1}{a}F(ax+b) + C \; (a \ne 0)$. \textit{Khẩu quyết: "Ruột bậc nhất $ax+b \implies$ BẮT BUỘC có $\dfrac{1}{a}$ ở đầu!"}\\
Cảnh báo lỗi sai: Học sinh thường quên nhân hệ số $\dfrac{1}{a}$ hoặc nhầm dấu: $\displaystyle\int \frac{1}{3-2x}dx = -\frac{1}{2}\ln|3-2x| + C$.
}

\noindent\textbf{Bài 1 (3,0 điểm). Tính nguyên hàm của các lũy thừa bậc nhất sau (chú ý hệ số $a$):}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[3]{a)}{$\displaystyle\int (2x - 5)^4 \, dx$} & 
\oBaiTap[3]{b)}{$\displaystyle\int (3 - 4x)^5 \, dx$} \\
\hline
\oBaiTap[3]{c)}{$\displaystyle\int (5x + 2)^3 \, dx$} & 
\oBaiTap[3]{d)}{$\displaystyle\int (1 - 2x)^6 \, dx$} \\
\hline
\oBaiTap[3]{e)}{$\displaystyle\int 3(2x + 1)^4 \, dx$} & 
\oBaiTap[3]{f)}{$\displaystyle\int (4 - x)^7 \, dx$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 2 (4,0 điểm). Tính nguyên hàm của các phân thức mẫu bậc nhất sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[4]{a)}{$\displaystyle\int \frac{1}{2x + 3} \, dx$} & 
\oBaiTap[4]{b)}{$\displaystyle\int \frac{1}{3x - 5} \, dx$} \\
\hline
\oBaiTap[4]{c)}{$\displaystyle\int \frac{1}{4 - 5x} \, dx$} & 
\oBaiTap[4]{d)}{$\displaystyle\int \frac{6}{2x - 1} \, dx$} \\
\hline
\oBaiTap[4]{e)}{$\displaystyle\int \frac{1}{(2x + 1)^2} \, dx$} & 
\oBaiTap[4]{f)}{$\displaystyle\int \frac{1}{(3x - 2)^2} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 2: CĂN THỨC VÀ SỐ MŨ PHÂN SỐ / MŨ ÂM
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 2/8} \\
\textit{Chuyên đề: Căn thức và số mũ phân số / mũ âm của biểu thức bậc nhất} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{CÔNG THỨC CĂN THỨC BẬC NHẤT}{%
$\bullet$ Đổi căn về lũy thừa: $\sqrt[n]{(ax+b)^m} = (ax+b)^{\frac{m}{n}} \implies \displaystyle\int (ax+b)^\alpha dx = \frac{1}{a} \cdot \frac{(ax+b)^{\alpha+1}}{\alpha+1} + C \; (\alpha \ne -1)$.\\
$\bullet$ Thuộc lòng: $\displaystyle\int \sqrt{ax+b} \, dx = \frac{1}{a} \cdot \frac{2}{3}(ax+b)\sqrt{ax+b} + C$; \quad $\displaystyle\int \frac{1}{\sqrt{ax+b}} \, dx = \frac{1}{a} \cdot 2\sqrt{ax+b} + C$.
}

\noindent\textbf{Bài 3 (4,0 điểm). Tính các nguyên hàm chứa căn thức bậc nhất sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \sqrt{2x + 1} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \sqrt{3x - 2} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{4}{\sqrt{2x + 5}} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \sqrt[3]{3x + 1} \, dx$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 4 (4,0 điểm). Rút gọn căn thức kết hợp đa thức rồi tính nguyên hàm:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{x^2 - 3x\sqrt{x} + 2}{\sqrt{x}} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \sqrt{x}(2x^2 - 4x + 3) \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \left(\frac{2}{x^3} - \frac{3}{x^2} + \sqrt{x}\right) dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{(x + \sqrt{x})^2}{x} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 3: PHÂN THỨC HỮU TỈ (DẠNG 1: CHIA ĐA THỨC BẬC TỬ >= BẬC MẪU)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 3/8} \\
\textit{Chuyên đề: Biến đổi phân thức hữu tỉ -- Phương pháp chia đa thức} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{QUY TẮC VÀNG CHIA ĐA THỨC}{%
Khi tính nguyên hàm phân thức $\displaystyle\int \frac{P(x)}{Q(x)} \, dx$ mà $\text{bậc}(P) \ge \text{bậc}(Q)$, \textbf{BẮT BUỘC} chia tử cho mẫu để tách:\\
$\displaystyle\frac{P(x)}{Q(x)} = \text{Thương } C(x) + \frac{\text{Dư } R(x)}{Q(x)}$ rồi mới áp dụng bảng nguyên hàm!
}

\noindent\textbf{Bài 5 (4,0 điểm). Tách phân thức (tử bậc 1, mẫu bậc 1) rồi tính nguyên hàm:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \frac{2x + 5}{x + 1} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{3x - 2}{x - 2} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{4x + 1}{2x - 1} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{6x - 5}{3x + 2} \, dx$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 6 (4,0 điểm). Chia đa thức (tử bậc 2, mẫu bậc 1) rồi tính nguyên hàm:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{x^2 + 3x - 2}{x + 1} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{x^2 - 4x + 5}{x - 2} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{2x^2 + 3x - 1}{2x + 1} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{x^2 + 1}{x - 1} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 4: PHÂN THỨC HỮU TỈ (DẠNG 2: TÁCH MẪU SỐ PHÂN TÍCH THÀNH NHÂN TỬ)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 4/8} \\
\textit{Chuyên đề: Phân tích mẫu số thành tích $(x-a)(x-b)$ -- Tách phân số} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{CÔNG THỨC TÁCH MẪU SỐ NHÂN TỬ}{%
$\bullet$ Tử là hằng số ($a \ne b$): $\displaystyle\frac{1}{(x-a)(x-b)} = \frac{1}{b-a}\left(\frac{1}{x-b} - \frac{1}{x-a}\right)$.\\
$\bullet$ Mẫu bậc 2 hằng đẳng thức: $\displaystyle\frac{1}{x^2 - a^2} = \frac{1}{2a}\left(\frac{1}{x-a} - \frac{1}{x+a}\right) \implies \int \frac{1}{x^2 - a^2} \, dx = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right| + C$.
}

\noindent\textbf{Bài 7 (4,0 điểm). Tách phân thức có mẫu là tích các nhị thức bậc nhất:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{1}{(x + 1)(x + 2)} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{1}{x^2 - 1} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{1}{x^2 - 4} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{1}{x^2 - 5x + 6} \, dx$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 8 (4,0 điểm). Tách phân thức dạng $\displaystyle\int \frac{mx + n}{(x-a)(x-b)} \, dx$ (đồng nhất hệ số):}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{2x + 3}{(x + 1)(x + 2)} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{3x - 1}{x^2 - 1} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{5x - 7}{x^2 - 3x + 2} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{x}{x^2 - 4} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 5: LƯỢNG GIÁC (HẠ BẬC & ĐỒNG NHẤT THỨC)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 5/8} \\
\textit{Chuyên đề: Biến đổi lượng giác -- Công thức hạ bậc \& đồng nhất thức} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{CÔNG THỨC LƯỢNG GIÁC THƯỜNG GẶP}{%
$\bullet$ Hạ bậc: $\sin^2(ax) = \dfrac{1 - \cos(2ax)}{2}$; \quad $\cos^2(ax) = \dfrac{1 + \cos(2ax)}{2}$.\\
$\bullet$ Đồng nhất thức: $\tan^2(ax) = \dfrac{1}{\cos^2(ax)} - 1 \implies \displaystyle\int \tan^2(ax) \, dx = \frac{1}{a}\tan(ax) - x + C$;\\
$\bullet$ $\cot^2(ax) = \dfrac{1}{\sin^2(ax)} - 1 \implies \displaystyle\int \cot^2(ax) \, dx = -\frac{1}{a}\cot(ax) - x + C$.
}

\noindent\textbf{Bài 9 (4,0 điểm). Dùng công thức hạ bậc để tính các nguyên hàm lượng giác sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int 4\sin^2 x \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int 6\cos^2(2x) \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int (2\sin^2 x + 4\cos^2 x) \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int (\sin^4 x - \cos^4 x) \, dx$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 10 (4,0 điểm). Dùng đồng nhất thức lượng giác để tính các nguyên hàm sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int (1 + \tan^2 x + 3\cos x) \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \tan^2(2x) \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \cot^2(3x) \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \left(\frac{1}{\sin^2(2x)} + \frac{1}{\cos^2(3x)}\right) dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 6: LƯỢNG GIÁC TÍCH THÀNH TỔNG & HÀM SỐ MŨ BIẾN ĐỔI LŨY THỪA
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 6/8} \\
\textit{Chuyên đề: Biến đổi tích thành tổng \& các phép biến đổi hàm số mũ} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{CÔNG THỨC TÍCH THÀNH TỔNG \& HÀM SỐ MŨ}{%
$\bullet$ $\cos a \cos b = \frac{1}{2}[\cos(a-b) + \cos(a+b)]$; \quad $\sin a \sin b = \frac{1}{2}[\cos(a-b) - \cos(a+b)]$.\\
$\bullet$ $\sin a \cos b = \frac{1}{2}[\sin(a+b) + \sin(a-b)]$.\\
$\bullet$ Hàm số mũ: $a^x \cdot b^x = (ab)^x$; \quad $\displaystyle\int a^{kx+b} dx = \frac{1}{k}\frac{a^{kx+b}}{\ln a} + C$; \quad $\displaystyle\int e^{kx+b} dx = \frac{1}{k}e^{kx+b} + C$.
}

\noindent\textbf{Bài 11 (4,0 điểm). Biến đổi tích thành tổng rồi tính các nguyên hàm sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int 2\sin(3x)\cos(x) \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int 2\cos(4x)\cos(2x) \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int 2\sin(5x)\sin(x) \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \cos(3x)\sin(2x) \, dx$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 12 (4,0 điểm). Biến đổi lũy thừa rồi tính các nguyên hàm hàm số mũ sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int (2^x \cdot 3^x) \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{8^x - 4^x}{2^x} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int (e^{3x-1} + 3 \cdot 2^{2x+1}) \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int (e^x + 1)^2 \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 7: TÌM NGUYÊN HÀM F(x) VỚI ĐIỀU KIỆN ĐIỂM F(x0) = y0
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 7/8} \\
\textit{Chuyên đề: Xác định hằng số $C$ qua điều kiện điểm $F(x_0) = y_0$} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{PHƯƠNG PHÁP XÁC ĐỊNH HẰNG SỐ $C$}{%
Bước 1: Tính họ nguyên hàm tổng quát $F(x) = \int f(x) \, dx + C$.\\
Bước 2: Thay $x = x_0$ vào biểu thức $F(x)$ và giải phương trình $F(x_0) = y_0$ để tìm ra giá trị $C$.\\
Bước 3: Kết luận hàm số $F(x)$ cụ thể (khi có $\ln|u(x)|$, xét dấu $u(x_0)$ trên khoảng đã cho để bỏ trị tuyệt đối).
}

\noindent\textbf{Bài 13 (4,0 điểm). Tìm nguyên hàm $F(x)$ của hàm đa thức và phân thức hữu tỉ:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{Tìm $F(x)$ của $f(x) = 3x^2 - 4x + 5$, biết $F(1) = 6$.} & 
\oBaiTap[7]{b)}{Tìm $F(x)$ của $f(x) = \dfrac{1}{2x - 3}$ trên $\left(\dfrac{3}{2}; +\infty\right)$, biết $F(2) = 3$.} \\
\hline
\oBaiTap[7]{c)}{Tìm $F(x)$ của $f(x) = \dfrac{2x + 1}{x + 1}$ trên $(-1; +\infty)$, biết $F(0) = 4$.} & 
\oBaiTap[7]{d)}{Tìm $F(x)$ của $f(x) = \dfrac{1}{x^2 - 1}$ trên $(1; +\infty)$, biết $F(2) = \ln 3$.} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 14 (4,0 điểm). Tìm nguyên hàm $F(x)$ của hàm lượng giác và hàm số mũ:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{Tìm $F(x)$ của $f(x) = 2\sin(2x) + 3\cos x$, biết $F(0) = 2$.} & 
\oBaiTap[6]{b)}{Tìm $F(x)$ của $f(x) = 4\cos^2 x$, biết $F\left(\dfrac{\pi}{4}\right) = \dfrac{\pi}{2}$.} \\
\hline
\oBaiTap[6]{c)}{Tìm $F(x)$ của $f(x) = 3e^{3x} - 2x$, biết $F(0) = 5$.} & 
\oBaiTap[6]{d)}{Tìm $F(x)$ của $f(x) = 2^x \ln 2 + e^{2x}$, biết $F(0) = \dfrac{5}{2}$.} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 8: BÀI TOÁN THỰC TẾ LIÊN MÔN (VẬT LÝ - KINH TẾ - SINH HỌC)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 2: RÈN LUYỆN THÀNH THẠO NGUYÊN HÀM} & \textbf{Trang 8/8} \\
\textit{Chuyên đề: Ứng dụng thực tế liên môn (Vật lý 12 -- Sinh học -- Kinh tế)} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{ỨNG DỤNG THỰC TẾ CỦA NGUYÊN HÀM}{%
$\bullet$ Vật lý: Gia tốc $a(t) \xrightarrow{\int} v(t) = \int a(t)dt + C_1 \xrightarrow{\int} s(t) = \int v(t)dt + C_2$.\\
$\bullet$ Tốc độ biến thiên: Số lượng cá thể $N(t) = \int N'(t)dt + N(0)$; Chi phí sản xuất $C(x) = \int C'(x)dx + C(0)$.
}

\noindent\textbf{Bài 15 (4,0 điểm). Bài toán chuyển động học (Vật lý 12):}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|}
\hline
\vspace{0.4mm}
\textbf{a) (2,0 điểm)} Một chiếc ô tô đang chạy với vận tốc đều $v_0 = 20\text{ m/s}$ (khoảng $72\text{ km/h}$) thì người lái phát hiện chướng ngại vật và đạp phanh khẩn cấp. Kể từ lúc đó, ô tô chuyển động chậm dần đều với gia tốc $a(t) = -4\text{ m/s}^2$.\par
\textit{1)} Thiết lập phương trình vận tốc $v(t)$ và tính thời gian từ lúc đạp phanh đến khi ô tô dừng hẳn.\par
\textit{2)} Tính quãng đường xe ô tô trượt được từ lúc đạp phanh đến khi dừng lại hẳn.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{5}
\\ \hline
\vspace{0.4mm}
\textbf{b) (2,0 điểm)} Một đoàn tàu bắt đầu rời ga tại thời điểm $t = 0\text{ (s)}$ chuyển động thẳng nhanh dần với gia tốc $a(t) = 0{,}6t\text{ (m/s}^2\text{)}$. Biết vận tốc ban đầu của tàu là $v(0) = 0$.\par
\textit{1)} Tìm phương trình biểu diễn vận tốc $v(t)$ của đoàn tàu.\par
\textit{2)} Tính quãng đường đoàn tàu di chuyển được trong 10 giây đầu tiên kể từ khi rời ga.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{5}
\\ \hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 16 (4,0 điểm). Bài toán thực tế Sinh học và Kinh tế học:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|}
\hline
\vspace{0.4mm}
\textbf{a) (2,0 điểm) [Sinh học]} Trong một môi trường nuôi cấy nhân tạo, số lượng vi khuẩn tăng trưởng với tốc độ $N'(t) = 150 e^{0{,}3t}$ (con/giờ). Biết rằng lúc bắt đầu cấy ($t = 0$), mẻ cấy có $500$ con vi khuẩn.\par
\textit{1)} Tìm hàm số $N(t)$ biểu thị số lượng vi khuẩn sau $t$ giờ.\par
\textit{2)} Hãy ước tính số lượng vi khuẩn có trong mẻ cấy sau $4$ giờ (làm tròn kết quả đến hàng đơn vị).
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{5}
\\ \hline
\vspace{0.4mm}
\textbf{b) (2,0 điểm) [Kinh tế]} Một doanh nghiệp sản xuất thiết bị điện tử xác định chi phí cận biên để sản xuất $x$ sản phẩm mỗi ngày là $C'(x) = 3x^2 - 12x + 40$ (nghìn đồng/sản phẩm). Biết chi phí cố định ban đầu của công ty là $500$ nghìn đồng ($C(0) = 500$).\par
\textit{1)} Xác định hàm tổng chi phí $C(x)$ để sản xuất $x$ sản phẩm.\par
\textit{2)} Tính tổng chi phí khi doanh nghiệp sản xuất $10$ sản phẩm trong ngày.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{5}
\\ \hline
\end{tabularx}

\end{document}
'''
    tex_path = os.path.join(CUR_DIR, 'Phieu_Luyen_Tap_Nguyen_Ham_Buoi_02.tex')
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex)
    print("Wrote", tex_path)

def compile_and_check():
    tex_file = 'Phieu_Luyen_Tap_Nguyen_Ham_Buoi_02.tex'
    pdf_file = 'Phieu_Luyen_Tap_Nguyen_Ham_Buoi_02.pdf'
    
    cmd = ['pdflatex', '-interaction=nonstopmode', tex_file]
    p = subprocess.run(cmd, cwd=CUR_DIR, capture_output=True)
    
    pdf_path = os.path.join(CUR_DIR, pdf_file)
    if os.path.exists(pdf_path):
        doc = pymupdf.open(pdf_path)
        print(f"Total pages: {len(doc)}")
        for i, page in enumerate(doc):
            text_rects = page.get_text('blocks')
            max_y = max(b[3] for b in text_rects) if text_rects else 0
            margin = page.rect.height - max_y
            print(f"Page {i+1}: height {page.rect.height:.1f}, max_y = {max_y:.1f}, bottom margin = {margin:.1f} pt ({margin*25.4/72:.1f} mm)")
    else:
        print("PDF not found!")

if __name__ == '__main__':
    create_tex()
    compile_and_check()
