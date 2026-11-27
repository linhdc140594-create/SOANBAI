# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import pymupdf

DIR = r"d:\GitHub\SOANBAI-main\THONG_BAO_THI_THU"
BRAIN_DIR = r"C:\Users\Admin\.gemini\antigravity\brain\0c8f089e-0c5d-4300-ba60-02f73af7a436"

tex_source = r'''\documentclass[border=0pt]{standalone}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{calc,shapes.geometric,shadows,decorations.pathmorphing}
\usepackage{xcolor}

\definecolor{primary}{RGB}{20, 35, 75}       % Xanh navy trang nhã
\definecolor{secondary}{RGB}{195, 135, 30}   % Vàng kim hổ phách
\definecolor{goldlight}{RGB}{250, 243, 225}  % Nền kem vàng nhạt
\definecolor{accentred}{RGB}{190, 45, 35}    % Đỏ gạch thiện nguyện
\definecolor{cardbg}{RGB}{255, 255, 255}     % Trắng thẻ thông tin
\definecolor{textdark}{RGB}{30, 40, 55}      % Chữ đậm
\definecolor{softgreen}{RGB}{35, 135, 75}    % Xanh lá miễn phí

\begin{document}
\begin{tikzpicture}[x=1cm, y=1cm]

  % 1. NỀN POSTER
  \clip (0, 0) rectangle (14, 20);
  \fill[goldlight] (0, 0) rectangle (14, 20);

  % Họa tiết nền trang trí góc
  \fill[secondary!15] (0, 20) circle (4.5cm);
  \fill[primary!10] (14, 0) circle (5cm);

  % Dải viền đỉnh
  \fill[primary] (0, 18.7) rectangle (14, 20);
  \fill[secondary] (0, 18.5) rectangle (14, 18.7);

  % 2. BANNER ĐỈNH
  \node[white, font=\large\bfseries] at (7, 19.35) {KHÓA HỌC THIỆN NGUYỆN -- ĐỒNG HÀNH CÙNG HỌC SINH};

  % 3. TIÊU ĐỀ CHÍNH
  \node[primary, font=\fontsize{22pt}{26pt}\selectfont\bfseries, align=center] at (7, 17.5) {
    LỚP THI THỬ \& ÔN THI MÔN TOÁN
  };
  \node[accentred, font=\fontsize{12.5pt}{15pt}\selectfont\bfseries, align=center] at (7, 16.65) {
    CHUẨN BỊ CHO KỲ THI THỬ CỦA SỞ GD\&ĐT (24/12/2026)
  };

  % 4. BADGE MIỄN PHÍ HOÀN TOÀN
  \node[draw=secondary, line width=1.5pt, fill=secondary!15, rounded corners=6pt, inner sep=6pt] at (7, 15.65) {
    \bfseries\color{accentred}\Large \hspace{6pt} \checkmark\ HOÀN TOÀN MIỄN PHÍ -- 100\% HỌC PHÍ 0 ĐỒNG \hspace{6pt}
  };

  % 5. CÁC THẺ THÔNG TIN (CARDS)
  % Card 1: Thời gian
  \draw[fill=cardbg, draw=secondary!50, line width=1pt, rounded corners=8pt] (0.8, 13.6) rectangle (13.2, 14.85);
  \node[anchor=west, textdark] at (1.2, 14.22) {
    \begin{tabular}{ll}
      \bfseries\color{primary}\large Lịch học: & \large\bfseries Sáng Chủ Nhật hàng tuần \\
      \bfseries\color{primary}\large Thời gian: & \large\bfseries 8h15 -- 11h00 (Bắt đầu từ Chủ Nhật tuần này)
    \end{tabular}
  };

  % Card 2: Địa điểm
  \draw[fill=cardbg, draw=secondary!50, line width=1pt, rounded corners=8pt] (0.8, 12.05) rectangle (13.2, 13.3);
  \node[anchor=west, textdark] at (1.2, 12.67) {
    \begin{tabular}{ll}
      \bfseries\color{primary}\large Địa điểm: & \large\bfseries Tại Chùa \textit{(Không gian thanh tịnh, an lành, tập trung cao)} \\
      \bfseries\color{primary}\large Môn thi: & \large\bfseries Môn Toán \textit{(Bám sát đề thi chuẩn của Sở GD\&ĐT)}
    \end{tabular}
  };

  % Card 3: Mục tiêu & Quyền lợi học sinh
  \draw[fill=cardbg, draw=secondary!50, line width=1pt, rounded corners=8pt] (0.8, 9.4) rectangle (13.2, 11.75);
  \node[anchor=north west, textdark] at (1.1, 11.55) {
    \begin{minipage}{11.8cm}
      {\color{primary}\bfseries\large QUYỀN LỢI CỦA CÁC EM KHI THAM GIA:}
      \vspace{2mm}
      \begin{itemize}\setlength{\itemsep}{1mm}\setlength{\parskip}{0pt}
        \item \textbf{Thi thử áp lực thật:} Rèn luyện căn chuẩn thời gian, chống run phòng thi.
        \item \textbf{Đề thi chất lượng:} Bám sát cấu trúc phân hóa của Sở, sát đề thi thực tế.
        \item \textbf{Chữa bài chi tiết từng câu:} Phân tích lỗi sai, bù đắp lỗ hổng kiến thức ngay.
        \item \textbf{Được kèm cặp tận tình:} Hướng dẫn phương pháp trình bày lấy trọn điểm số.
      \end{itemize}
    \end{minipage}
  };

  % 6. KHUNG CẢNH BÁO / GIỚI HẠN SỐ LƯỢNG
  \draw[fill=accentred!10, draw=accentred, line width=1.2pt, rounded corners=8pt] (0.8, 7.3) rectangle (13.2, 9.05);
  \node[align=center, textdark] at (7, 8.18) {
    {\bfseries\color{accentred}\large \textbullet\ SỐ LƯỢNG HỌC SINH ĐĂNG KÝ CÓ HẠN \textbullet}\\[2mm]
    \large Do diện tích phòng học tại chùa có hạn để bảo đảm chất lượng kèm cặp,\\
    \bfseries Thầy sẽ chốt danh sách khi đủ số lượng học sinh đăng ký!
  };

  % 7. HƯỚNG DẪN THAM GIA
  \draw[fill=primary!8, draw=primary!60, line width=1pt, rounded corners=8pt] (0.8, 4.4) rectangle (13.2, 6.95);
  \node[align=center, textdark] at (7, 5.68) {
    {\bfseries\color{primary}\Large CÁCH THỨC THAM GIA NHÓM ÔN THI}\\[2.5mm]
    \large Quý Phụ huynh \& các em Học sinh bấm vào liên kết nhóm Zalo bên dưới\\
    hoặc liên hệ trực tiếp với Thầy qua Zalo / Số điện thoại để ghi danh.\\[2mm]
    \bfseries\color{accentred}\large \textit{(Hãy tham gia nhóm sớm để nhận lịch thi thử \& tài liệu ôn tập)}
  };

  % 8. DẢI FOOTER CHÂN TRANG
  \fill[primary] (0, 0) rectangle (14, 3.8);
  \fill[secondary] (0, 3.8) rectangle (14, 4.0);

  \node[white, align=center] at (7, 2.5) {
    {\fontsize{13pt}{15pt}\selectfont\bfseries LỚP HỌC TOÁN THẦY LĨNH -- GIEO DUYÊN TRI THỨC}\\[1.5mm]
    {\normalsize \textit{Đồng hành cùng các em vượt qua kỳ thi với kết quả cao nhất!}}\\[2mm]
    {\bfseries\color{secondary!90}\large Hotline / Zalo: Thầy Lĩnh \hspace{8pt}|\hspace{8pt} Website: loptoanthaylinh.vn}
  };

  \node[white!70, font=\footnotesize] at (7, 0.7) {
    Chúc các em học sinh ôn tập thật tốt và đạt kết quả xuất sắc trong kỳ thi sắp tới!
  };

\end{tikzpicture}
\end{document}
'''

def main():
    tex_path = os.path.join(DIR, "poster_thi_thu.tex")
    pdf_path = os.path.join(DIR, "poster_thi_thu.pdf")
    png_path = os.path.join(DIR, "poster_thi_thu.png")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_source)
    print("Wrote tex source:", tex_path)

    cmd = ["pdflatex", "-interaction=nonstopmode", "poster_thi_thu.tex"]
    subprocess.run(cmd, cwd=DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if os.path.exists(pdf_path):
        print("Compiled PDF successfully!")
        doc = pymupdf.open(pdf_path)
        page = doc[0]
        # Render high quality 300 dpi image
        pix = page.get_pixmap(dpi=300)
        pix.save(png_path)
        print("Exported PNG successfully:", png_path)
        doc.close()

        # Copy to brain artifact dir
        if os.path.exists(BRAIN_DIR):
            shutil.copy(png_path, os.path.join(BRAIN_DIR, "poster_thi_thu.png"))
            print("Copied to brain artifact directory.")
    else:
        print("Failed to compile PDF! Check log.")

if __name__ == "__main__":
    main()
