# HƯỚNG DẪN DỰ ÁN PHIẾU KIỂM TRA ĐỊNH KỲ THCS (AGENTS.MD)

Kho lưu trữ chuyên dụng biên soạn Phiếu Kiểm Tra Định Kỳ môn Toán THCS (Lớp 6, 7, 8, 9).

---

## 🔄 QUY TRÌNH 3 BƯỚC BIÊN SOẠN PHIẾU KIỂM TRA ĐỊNH KỲ (BẮT BUỘC TUÂN THỦ)

Mỗi khi nhận yêu cầu làm phiếu kiểm tra cho bất kỳ tuần/buổi nào, Agent **bắt buộc thực hiện tuần tự theo đúng 3 bước**, không đốt cháy giai đoạn:

### 📌 BƯỚC 1: TẠO KẾ HOẠCH BUỔI / TUẦN (PLANNING & APPROVAL)
1. Tạo thư mục làm việc: `LOP<K>/1_GHK_1/TUAN_<X>/buoi_<Y>/` (hoặc `LOP<K>/1_GHK_1/TUAN_<X>/`).
2. Sao chép `ex_test.sty` vào thư mục để phục vụ biên dịch.
3. Soạn file `KE_HOACH_TUAN_<X>_BUOI_<Y>.md`:
   - Xác định chủ đề SGK (Kết nối tri thức / Cánh diều).
   - Thiết lập ma trận đề chuẩn 10 điểm (10 câu trả lời ngắn + 4 câu tự luận).
   - Chi tiết hóa số liệu toán học chuẩn xác, nghiệm nguyên đẹp cho cả 4 mã đề tương đương ($101, 102, 103, 104$).
4. **Trình bản kế hoạch cho Thầy duyệt trước khi bắt đầu tạo code.**

### 📌 BƯỚC 2: TẠO ĐỀ & XUẤT FILE PDF (GENERATION & COMPILATION)
1. Sau khi Thầy duyệt kế hoạch, tạo script Python `generate_tuan<X>_buoi<Y>.py` để sinh file `.tex`.
2. Áp dụng chuẩn thiết kế tối ưu mới:
   - Header 1 dòng duy nhất (bỏ chủ đề, thời gian, khung họ tên riêng).
   - Bảng Điểm & Nhận xét cao `\rule{0pt}{1.8cm}`.
   - Bỏ toàn bộ phân cách: bỏ bảng điền đáp án, bỏ "Phần I/II", bỏ nhãn thể loại ("Bài toán thực tế", "Bài toán nâng cao").
   - 10 câu ngắn dùng `\shortans` với `\SAOPTN{widthSA=3.2,heightSA=0.62}`.
   - Ghép trực tiếp số câu + số điểm vào đầu khung đề bài (Câu 13, Câu 14).
3. Biên dịch bằng `pdflatex -interaction=nonstopmode` để kiểm tra cú pháp và xuất file PDF sơ bộ.

### 📌 BƯỚC 3: DÃN DÒNG ĐỂ KÍN TỜ GIẤY & HOÀN THIỆN ĐÁP ÁN (AUTO-FILL & POLISH)
1. **Dãn dòng làm bài sát đáy giấy:**
   - Dùng thông số dòng kẻ chuẩn: `\baselineskip=18.5pt`, `\vspace{1.0mm}` trước, `\vspace{0.6mm}` sau.
   - Trang 1: Tinh chỉnh Câu 11 đạt **`\oBaiTap[8]`** và giãn cách các câu ngắn để lấp kín sát lề dưới Trang 1.
   - Trang 2: Tinh chỉnh Câu 12 (**`\oBaiTap[5]`**), Câu 13 (**`\dongke{11}`**), Câu 14 (**`\dongke{7}`**) để lấp kín sát lề dưới Trang 2.
2. **Kiểm tra số trang tuyệt đối:**
   - Biên dịch lại và kiểm tra bằng `pypdf`: **Bắt buộc chính xác 8 trang PDF** cho 4 mã đề ($101, 102, 103, 104$). Tuyệt đối không để xảy ra tràn sang trang thứ 9 hoặc thiếu trang.
3. **Hoàn thiện file Đáp án & Thang điểm (`DAP_AN_VA_THANG_DIEM.md`):**
   - Bảng đáp án 10 câu trả lời ngắn của cả 4 mã đề.
   - Lời giải chi tiết từng bước cho Câu 11, 12, 13, 14 kèm barem điểm chia nhỏ đến $0{,}25$đ.

---

## 📐 BẢNG THAM CHIẾU QUY CHUẨN KỸ THUẬT LATEX

### 1. Header Đỉnh Trang Siêu Tối Giản
* **Trang 1 (Mặt trước):**
  ```latex
  \noindent
  \begin{tabularx}{\linewidth}{|X|c|}
  \hline
  \textbf{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN <K> - TUẦN <X> - BUỔI <Y>} & \textbf{Mã đề: <MÃ> - Trang 1/2} \\
  \hline
  \end{tabularx}
  ```
* **Trang 2 (Mặt sau):** Khung tiêu đề 1 dòng: `TOÁN <K> - TUẦN <X> - BUỔI <Y> | Mã đề: <MÃ> - Trang 2/2`.

### 2. Kích thước Ô Điểm số & Lời nhận xét
* Bắt buộc dùng `\rule{0pt}{1.8cm}`.

### 3. Ghép Tiêu Đề Câu Trực Tiếp Trong Khung Box
```latex
\noindent
\begin{tabularx}{\linewidth}{|X|}
\hline
\vspace{0.5mm}
\textbf{Câu 13 (2,5 điểm).} Bác An có một mảnh vườn...\par
\textbf{a) (1,25 điểm)} Tính chu vi và diện tích...\par
\textbf{b) (1,25 điểm)} Bác An dự định làm hàng rào...\par
\vspace{0.4mm}
\noindent\textit{Bài giải:}\dongke{11}
\\ \hline
\end{tabularx}
```

### 4. Thông Số Dòng Kẻ Chấm Mờ Chuẩn Viết Tay
```latex
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{1.0mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!60}\dotfill}\par%
  }%
  \vspace{0.6mm}%
  \endgroup%
}
\newcommand{\oBaiTap}[3][6]{%
  \vspace{1.0mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}
```
