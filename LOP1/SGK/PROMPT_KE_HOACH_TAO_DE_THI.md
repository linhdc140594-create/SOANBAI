# PROMPT KẾ HOẠCH: TẠO TUYỂN TẬP ĐỀ KIỂM TRA TOÁN THEO TỪNG BÀI HỌC (LATEX PDF)

Tài liệu này lưu lại toàn bộ đặc tả, cấu trúc Preamble, macro khung tiêu đề và quy trình biên dịch để nhân bản hoặc tái sử dụng cho các khối lớp khác (Toán 2, Toán 3, Toán 4, Toán 5,...).

---

## 1. Cấu Hình Khung LaTeX & Preamble Chuẩn

```latex
\documentclass[14pt,a4paper,oneside]{extbook} % Dùng extbook để nhận cỡ chữ 14pt chuẩn Tiểu học
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb,mathrsfs,fancyhdr,enumerate,multirow,makecell,venndiagram}
\usepackage{tkz-euclide,tikz-3dplot,tikz,tkz-tab}
\usetikzlibrary{arrows,calc,intersections,angles,quotes,backgrounds,shapes.geometric,patterns,through}
\usepackage{yhmath}
\usepackage{pgfplots}
\pgfplotsset{compat=1.9}
\usepgfplotslibrary{fillbetween}
\usepackage[tikz]{bclogo}
\usepackage[top=1.8cm, bottom=1.8cm, left=1.8cm, right=1.8cm, headheight=16pt]{geometry}
\usepackage[hidelinks,unicode]{hyperref}
\usepackage{qrcode}

% BẮT BUỘC: Nạp tcolorbox TRƯỚC ex_test để ex_test không sinh trang cảnh báo đỏ ở trang đầu
\usepackage[many]{tcolorbox}

% Gói ex_test (Chọn [dethi] để in đề làm bài hoặc [loigiai] để in cả lời giải)
%\usepackage[loigiai]{ex_test}
\usepackage[dethi]{ex_test}

\def\colorEX{\color{blue}}
\everymath{\color{blue}}

\usepackage{fontawesome}
\usepackage{framed}
\usepackage{polynom}

% Định dạng Header & Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape\color{gray} Tuyển tập Đề kiểm tra Toán [X] theo từng bài}
\fancyhead[R]{\small\bfseries\color{blue!80!black} Lớp Toán Thầy Lĩnh -- loptoanthaylinh.vn}
\fancyfoot[C]{\bfseries\thepage}
\renewcommand{\headrulewidth}{0.4pt}
```

---

## 2. Macro Khung Tiêu Đề Phiếu Kiểm Tra Gọn Đẹp (`\TaoPhieuKiemTra`)

> **Đặc điểm:** Thiết kế 1 hàng ngang duy nhất (3 cột cân đối trong `tcolorbox`), không dòng kẻ ngăn cách thừa, không chứa phần điền họ tên/điểm số, tối ưu diện tích để đề bài bắt đầu ngay bên dưới.

```latex
% -------------------------------------------------------------------------
% KHUNG TIÊU ĐỀ PHIẾU KIỂM TRA KÈM MÃ QR CODE CHO TỪNG BÀI
% Cú pháp: \TaoPhieuKiemTra{Chủ đề}{Số bài}{Tên bài}{Link QR thi online}
% -------------------------------------------------------------------------
\newcommand{\TaoPhieuKiemTra}[4]{%
  \refstepcounter{subsection}%
  \addcontentsline{toc}{subsection}{Bài #2. #3}%
  \noindent
  \begin{tcolorbox}[
    colback=white,
    colframe=blue!85!black,
    arc=2.5mm,
    boxrule=1pt,
    left=2.5mm, right=2.5mm, top=1.8mm, bottom=1.8mm
  ]
    % LOGO TRUNG TÂM & HOTLINE | TIÊU ĐỀ BÀI KIỂM TRA | MÃ QR CODE
    \begin{minipage}[c]{0.27\textwidth}
      \centering
      \begin{tcolorbox}[colback=blue!8, colframe=blue!80!black, boxrule=0.6pt, arc=1.5mm, halign=center, top=1.2mm, bottom=1.2mm, left=1mm, right=1mm]
        {\bfseries\color{blue!95!black}\small LỚP TOÁN THẦY LĨNH}\\[1.5pt]
        {\scriptsize\color{blue!70!black}\faGlobe~loptoanthaylinh.vn}\\[1.5pt]
        {\scriptsize\bfseries\color{blue!85!black}\faPhone~Hotline: 0866976878}
      \end{tcolorbox}
    \end{minipage}%
    \hfill
    \begin{minipage}[c]{0.56\textwidth}
      \centering
      {\footnotesize\bfseries\color{blue!80!black}\MakeUppercase{#1}}\\[2pt]
      {\large\bfseries\color{red!85!black}\MakeUppercase{BÀI #2: #3}}\\[2pt]
      {\scriptsize\itshape Thời gian làm bài: 35 phút -- Cấu trúc 3 phần chuẩn}
    \end{minipage}%
    \hfill
    \begin{minipage}[c]{0.14\textwidth}
      \centering
      \qrcode[height=1.35cm]{#4}\\[2pt]
      {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
    \end{minipage}
  \end{tcolorbox}
  \vspace{1.5mm}
}
```

---

## 3. Cấu Trúc File Chính (`main.tex`)

- Bắt đầu trực tiếp từ **Trang 1: Mục lục** (`\tableofcontents`), không thêm trang bìa phụ.
- Chia nhóm Chủ đề bằng `\section{...}`.
- Mỗi bài thi được gọi tuần tự:
```latex
\begin{document}

\tableofcontents
\newpage

\section{Các số từ 0 đến 10}

\TaoPhieuKiemTra{Chủ đề 1 -- Các số từ 0 đến 10}{01}{Các số 0, 1, 2, 3, 4, 5}{https://loptoanthaylinh.vn/thi-online/toan-1/bai-01}
\input{CHỦ ĐỀ 1 - CÁC SỐ TỪ 0 ĐẾN 10/Chuong1_Bai01_CacSo0_1_2_3_4_5.tex}
\newpage

\TaoPhieuKiemTra{Chủ đề 1 -- Các số từ 0 đến 10}{02}{Các số 6, 7, 8, 9, 10}{https://loptoanthaylinh.vn/thi-online/toan-1/bai-02}
\input{CHỦ ĐỀ 1 - CÁC SỐ TỪ 0 ĐẾN 10/Chuong1_Bai02_CacSo6_7_8_9_10.tex}
\newpage

...
\end{document}
```

---

## 4. Lệnh Biên Dịch & Đồng Bộ File PDF

Tại thư mục chứa file TeX, mở PowerShell và chạy:
```powershell
# Bước 1: Biên dịch lần 1
pdflatex -interaction=nonstopmode main.tex

# Bước 2: Biên dịch lần 2 (để cập nhật chính xác Mục lục & Bookmarks outline)
pdflatex -interaction=nonstopmode main.tex

# Bước 3: Đồng bộ sang tên file PDF chính thức
Copy-Item -Path "main.pdf" -Destination "Main_KiemTra_Toan1_TheoBai.pdf" -Force
```

---

## 5. Quy Trình Tách Từng Đề Thành File PDF Độc Lập

Để phục vụ việc gửi đề riêng lẻ từng bài cho học sinh hoặc in ấn độc lập từng buổi học, toàn bộ đề thi có thể được tự động tách ra thành từng file PDF riêng biệt bằng script Python:

```powershell
# Tách tất cả các khối lớp (Toán 1 đến Toán 9)
python scripts/tach_de_thi_pdf.py

# Hoặc chỉ tách riêng cho 1 khối lớp cụ thể (ví dụ Toán 1)
python scripts/tach_de_thi_pdf.py --grade 1
```

- **Thư mục đầu ra:** `1.SACH/SGK/KiemTra_Toan[X]_TheoBai/PDF_DeThi_TungBai/`
- **Quy cách đặt tên file:** `Bai_[Số bài]_[Tên_bài_không_dấu].pdf` (ví dụ: `Bai_01_Cac_so_0_1_2_3_4_5.pdf`).
