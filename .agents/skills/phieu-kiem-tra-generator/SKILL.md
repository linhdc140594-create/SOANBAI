---
name: phieu-kiem-tra-generator
description: >-
  Quy trình tự động hóa tạo Phiếu Kiểm Tra Định Kỳ môn Toán THCS (Lớp 6, 7, 8, 9) chuẩn hóa 2 mặt giấy A4
  (chính xác 8 trang cho 4 mã đề: 101, 102, 103, 104) theo phương pháp Tối Ưu Mới: Bỏ chủ đề/thời gian,
  bỏ khung họ tên, 10 câu trả lời ngắn dùng \shortans, ghép trực tiếp tiêu đề câu, auto-fill dòng kẻ sát mép giấy.
---

# Quy Trình Tự Động Hóa Soạn Phiếu Kiểm Tra Định Kỳ Toán THCS (Phương Pháp Tối Ưu Mới)

Skill này chuẩn hóa toàn bộ quy trình biên soạn Phiếu Kiểm Tra Định Kỳ hàng tuần cho các khối lớp THCS (Toán 6, Toán 7, Toán 8, Toán 9), đảm bảo tính sư phạm chính xác, thẩm mỹ in ấn tuyệt đối và cấu trúc tài liệu đồng nhất theo chuẩn thiết kế tối ưu mới.

---

## 1. Tiêu Chuẩn Thiết Kế Bố Cục Tối Ưu Mới (Layout Gold Standard)

Mỗi buổi kiểm tra bao gồm **4 mã đề (101, 102, 103, 104)**, mỗi mã đề đúng **2 trang A4** (Mặt trước + Mặt sau), tổng cộng **chính xác 8 trang PDF**:

### Trang 1 (Mặt trước - Trang 1/2)
* **Header Đỉnh Trang (1 dòng duy nhất):**
  ```latex
  \noindent
  \begin{tabularx}{\linewidth}{|X|c|}
  \hline
  \textbf{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN <K> - TUẦN <X> - BUỔI <Y>} & \textbf{Mã đề: <MÃ> - Trang 1/2} \\
  \hline
  \end{tabularx}
  ```
  - **BỎ HOÀN TOÀN** dòng ghi "Chủ đề: ...", "Thời gian: 45 phút".
  - **BỎ HOÀN TOÀN** khung riêng "Họ và tên", "Mã HS", "SĐT" (học sinh tự ghi tên lên lề trên cùng - top margin của tờ giấy).
* **Bảng Điểm số & Lời nhận xét:** Chiều cao cố định bắt buộc **`\rule{0pt}{1.8cm}`** (rộng rãi, trang trọng).
* **Bỏ toàn bộ bảng đáp án trắc nghiệm & tiêu đề phân đoạn:**
  - Tuyệt đối không vẽ bảng điền đáp án A, B, C, D ở bất kỳ đâu.
  - Không dùng tiêu đề "PHẦN I. TRẮC NGHIỆM", "PHẦN II. TỰ LUẬN".
* **Phần Trả lời ngắn (Câu 1 đến Câu 10 - 2,5 điểm):**
  - Cấu hình trong preamble: `\SAOPTN{widthSA=3.2,heightSA=0.62}`.
  - Cú pháp từng câu:
    ```latex
    \noindent\textbf{Câu 1 (0,25 điểm).} Đề bài... \shortans{Đáp án}\par\vspace{0.3mm}
    ```
  - Dùng lệnh `\shortans{...}` (hoặc `\SA{...}`) trong `ex_test.sty`. Tự động tạo ô `KQ: [   ]` bo góc ở mép phải câu hỏi.
* **Câu 11 (2,0 điểm - Thực hiện phép tính):**
  - Tiêu đề: `\noindent\textbf{Câu 11 (2,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}`
  - Bảng $2 \times 2$ gồm 4 ý $a, b, c, d$ với **`\oBaiTap[8]`** (8 dòng kẻ mờ/ô), vừa vặn chạm sát mép đáy Trang 1.

### Trang 2 (Mặt sau - Trang 2/2)
* **Header rút gọn 1 dòng:** `TOÁN <K> - TUẦN <X> - BUỔI <Y> | Mã đề: <MÃ> - Trang 2/2`.
* **Câu 12 (2,0 điểm - Tìm số tự nhiên $x$):**
  - Tiêu đề: `\noindent\textbf{Câu 12 (2,0 điểm). Tìm số tự nhiên $x$, biết:}`
  - Bảng $2 \times 2$ gồm 4 ý $a, b, c, d$ với **`\oBaiTap[5]`** (5 dòng kẻ mờ/ô).
* **Câu 13 (2,5 điểm - Bài toán thực tế / lời văn):**
  - **BỎ NHÃN** "Bài toán thực tế:", ghép thẳng vào trong box `tabularx`:
    ```latex
    \noindent
    \begin{tabularx}{\linewidth}{|X|}
    \hline
    \vspace{0.5mm}
    \textbf{Câu 13 (2,5 điểm).} Bối cảnh bài toán...\par
    \textbf{a) (1,25 điểm)} Câu hỏi a...\par
    \textbf{b) (1,25 điểm)} Câu hỏi b...\par
    \vspace{0.4mm}
    \noindent\textit{Bài giải:}\dongke{11}
    \\ \hline
    \end{tabularx}
    ```
* **Câu 14 (1,0 điểm - Bài toán nâng cao):**
  - **BỎ NHÃN** "Bài toán nâng cao:", ghép thẳng vào trong box `tabularx`:
    ```latex
    \noindent
    \begin{tabularx}{\linewidth}{|X|}
    \hline
    \vspace{0.5mm}
    \textbf{Câu 14 (1,0 điểm).} Cho tổng biểu thức / bài toán nâng cao...\par
    \vspace{0.4mm}
    \noindent\textit{Bài giải:}\dongke{7}
    \\ \hline
    \end{tabularx}
    ```
  - Chạm sát mép đáy Trang 2.

---

## 2. Thông Số Dòng Kẻ Chấm Mờ (`\dongke` & `\oBaiTap`)

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

---

## 3. Quy Trình 3 Bước Chuẩn Hóa Thực Hiện Hàng Tuần

Mọi yêu cầu biên soạn phiếu kiểm tra cho bất kỳ tuần hay khối lớp nào đều **bắt buộc tuân thủ tuần tự 3 bước sau đây**:

### 📌 BƯỚC 1: TẠO KẾ HOẠCH BUỔI / TUẦN (PLANNING & APPROVAL)
1. **Quản lý thư mục:**
   - Tạo thư mục tuần: `LOP<K>/PHIEU_KIEM_TRA/1_GHK_1/TUAN_<X>/`.
   - Chia 2 thư mục con: `buoi_1/` và `buoi_2/`.
   - Copy `ex_test.sty` vào từng thư mục con để phục vụ biên dịch.
2. **Soạn file kế hoạch (`KE_HOACH_TUAN_<X>_BUOI_<Y>.md`):**
   - Xác định chủ đề SGK kết nối tri thức / Cánh diều.
   - Thiết lập ma trận đề chuẩn 10 điểm (10 câu trả lời ngắn + 4 bài tự luận).
   - Thiết kế dữ liệu toán học chuẩn xác, số chẵn đẹp, nghiệm nguyên cho 4 mã đề tương đương ($101, 102, 103, 104$).
3. **Duyệt kế hoạch:** Trình bản kế hoạch cho Thầy duyệt trước khi bắt đầu tạo code.

### 📌 BƯỚC 2: TẠO ĐỀ & XUẤT FILE PDF (GENERATION & COMPILATION)
1. **Lắp ráp mã nguồn LaTeX bằng Python Generator:**
   - Sau khi Thầy duyệt kế hoạch, viết script `generate_tuan<X>_buoi<Y>.py` để sinh đồng bộ 4 mã đề vào file `Phieu_Kiem_Tra_Tuan_<X>_Buoi_<Y>.tex`.
   - Áp dụng đầy đủ quy chuẩn tối ưu mới: Header 1 dòng tối giản, bỏ chủ đề/thời gian/khung tên riêng, bỏ phân cách Phần I/II, 10 câu trả lời ngắn dùng `\shortans` với `\SAOPTN{widthSA=3.2,heightSA=0.62}`, ghép trực tiếp số câu + số điểm vào khung bài giải (Câu 13, Câu 14).
2. **Biên dịch sơ bộ:**
   - Chạy lệnh: `pdflatex -interaction=nonstopmode Phieu_Kiem_Tra_Tuan_<X>_Buoi_<Y>.tex`.
   - Kiểm tra mã lỗi và tạo ra file PDF lần đầu.

### 📌 BƯỚC 3: DÃN DÒNG ĐỂ KÍN TỜ GIẤY & HOÀN THIỆN ĐÁP ÁN (AUTO-FILL & POLISH)
1. **Dãn dòng làm bài sát đáy giấy (Auto-fill):**
   - Sử dụng tham số dòng kẻ chấm mờ viết tay: `\baselineskip=18.5pt`, `\vspace{1.0mm}` trước, `\vspace{0.6mm}` sau.
   - **Trang 1 (Mặt trước):** Tinh chỉnh Câu 11 đạt **`\oBaiTap[8]`** (8 dòng kẻ mờ/ô) và điều chỉnh giãn cách câu trả lời ngắn để nội dung lấp kín 100% sát lề đáy Trang 1.
   - **Trang 2 (Mặt sau):** Tinh chỉnh Câu 12 (**`\oBaiTap[5]`**), Câu 13 (**`\dongke{11}`**), Câu 14 (**`\dongke{7}`**) để lấp kín 100% sát lề đáy Trang 2.
2. **Kiểm tra khớp số trang tuyệt đối:**
   - Biên dịch lại và kiểm tra bằng `pypdf`: **Bắt buộc chính xác 8 trang PDF** cho 4 mã đề (101, 102, 103, 104). Không được 7 trang (bị co rúm) hoặc 9 trang (bị tràn).
3. **Hoàn thiện file Đáp án & Thang điểm (`DAP_AN_VA_THANG_DIEM.md`):**
   - Bảng đáp án 10 câu trả lời ngắn cho cả 4 mã đề.
   - Lời giải chi tiết từng bước cho Câu 11, 12, 13, 14 kèm barem điểm chia nhỏ đến $0{,}25$đ.

