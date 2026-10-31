# HƯỚNG DẪN SỬ DỤNG VÀ BIÊN DỊCH BỘ ĐỀ KIỂM TRA TOÁN 1 THEO TỪNG BÀI

Bộ tài liệu được xây dựng hoàn chỉnh cho **41 đề kiểm tra Toán lớp 1** theo 10 chủ đề chuẩn chương trình GDPT 2018 (SGK Kết nối tri thức với cuộc sống / Cánh diều / Chân trời sáng tạo).

---

## 📁 CẤU TRÚC HỆ THỐNG TÀI LIỆU

```
1.SACH/SGK/KiemTra_Toan1_TheoBai/
├── Main_KiemTra_Toan1_TheoBai.tex       <-- File LaTeX chính tổng hợp toàn bộ
├── Preamble_Toan1.tex                    <-- Cấu hình font, TikZ, tcolorbox, qrcode, macro header & chế độ ẩn/hiện giải
├── PhuLuc_DauSach.tex                    <-- Phụ lục tra cứu ma trận 41 bài kiểm tra & hướng dẫn QR đầu sách
├── ex_test.sty                           <-- Gói soạn đề trắc nghiệm chuẩn BTTeX Pro
├── README_HuongDanSuDung.md              <-- Tài liệu hướng dẫn chi tiết này
│
├── CHỦ ĐỀ 1 - CÁC SỐ TỪ 0 ĐẾN 10/       (Bài 01 -> Bài 06)
├── CHỦ ĐỀ 2 - LÀM QUEN VỚI HÌNH PHẲNG/ (Bài 07 -> Bài 09)
├── CHỦ ĐỀ 3 - PHÉP CỘNG, TRỪ PV 10/     (Bài 10 -> Bài 13)
├── CHỦ ĐỀ 4 - LÀM QUEN VỚI HÌNH KHỐI/   (Bài 14 -> Bài 16)
├── CHỦ ĐỀ 5 - ÔN TẬP HỌC KÌ 1/          (Bài 17 -> Bài 20)
├── CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100/           (Bài 21 -> Bài 24)
├── CHỦ ĐỀ 7 - ĐỘ DÀI VÀ ĐO ĐỘ DÀI/      (Bài 25 -> Bài 28)
├── CHỦ ĐỀ 8 - PHÉP TÍNH PV 100/         (Bài 29 -> Bài 33)
├── CHỦ ĐỀ 9 - THỜI GIAN. GIỜ VÀ LỊCH/   (Bài 34 -> Bài 37)
└── CHỦ ĐỀ 10 - ÔN TẬP CUỐI NĂM/         (Bài 38 -> Bài 41)
```

---

## 🌟 ĐẶC ĐIỂM NỔI BẬT CỦA BỘ TÀI LIỆU

1. **Phần Đầu Sách (Front Matter)**:
   - **Trang bìa chính**: Phong cách Lớp Toán Thầy Lĩnh hiện đại.
   - **Phụ lục & Ma trận phân phối (`PhuLuc_DauSach.tex`)**: Thống kê chi tiết 10 chủ đề, 41 bài kiểm tra, số câu, thời lượng và mã ID thi online.
   - **Khung QR Code toàn khóa**: Dẫn trực tiếp tới Cổng khảo thí trực tuyến Toán 1 `loptoanthaylinh.vn/thi-online/toan-1`.
   - **Hướng dẫn quét QR & Quy chế chấm điểm**: Dành cho học sinh và phụ huynh.
   - **Mục lục tự động (`\tableofcontents`)**: Phân nhánh rõ ràng theo từng chủ đề.

2. **PHẦN 1: BỘ ĐỀ BÀI KIỂM TRA TỰ LUYỆN (41 ĐỀ)**:
   - Mỗi đề bắt đầu ở trang mới, là 1 phiếu bài tập chuẩn A4.
   - **Header nhận diện**: Logo Lớp Toán Thầy Lĩnh, Website `loptoanthaylinh.vn`.
   - **Khung thông tin học sinh**: Họ và tên, Lớp, Trường, Ngày kiểm tra.
   - **Khung Chấm Điểm**: Ô điểm số chuẩn (`... / 10`) và lời nhận xét.
   - **Mã QR Code động cho từng bài**: Quét camera là mở ngay đề thi online của bài đó (Ví dụ: `https://loptoanthaylinh.vn/thi-online/toan-1/bai-01`).
   - **Ẩn hoàn toàn lời giải**: Giúp học sinh tự giác làm bài như bài thi thật.

3. **PHẦN 2: ĐÁP ÁN VÀ HƯỚNG DẪN GIẢI CHI TIẾT (ĐẶT Ở CUỐI TÀI LIỆU)**:
   - Lời giải chi tiết được gom toàn bộ về cuối sách.
   - Hiển thị từng bước giải, hình vẽ minh họa và nhận xét sư phạm để phụ huynh/giáo viên dễ dàng đối soát kết quả.

---

## 🛠️ HƯỚNG DẪN BIÊN DỊCH RA PDF

Bạn có thể sử dụng bất kỳ phần mềm LaTeX nào (TeXStudio, VS Code LaTeX Workshop, Overleaf, hoặc dòng lệnh PowerShell):

### Cách 1: Biên dịch bằng dòng lệnh (Terminal / PowerShell)
Mở Terminal tại thư mục `1.SACH/SGK/KiemTra_Toan1_TheoBai` và chạy lệnh:

```powershell
pdflatex -synctex=1 -interaction=nonstopmode Main_KiemTra_Toan1_TheoBai.tex
```

> **Gợi ý:** Để cập nhật đầy đủ Mục lục và Bookmark siêu liên kết, nên chạy lệnh trên **2 lần liên tiếp**.

### Cách 2: Biên dịch bằng XeLaTeX (nếu cần font hệ thống mở rộng)
```powershell
xelatex -synctex=1 -interaction=nonstopmode Main_KiemTra_Toan1_TheoBai.tex
```

---

## ⚙️ HƯỚNG DẪN TÙY BIẾN LINK QR & THÔNG TIN TRUNG TÂM

### 1. Thay đổi đường link thi online của từng bài
Mở file `Main_KiemTra_Toan1_TheoBai.tex` và thay đổi tham số thứ 4 trong lệnh `\TaoPhieuKiemTra`:
```latex
\TaoPhieuKiemTra{Chủ đề 1 -- Các số từ 0 đến 10}{01}{Các số 0, 1, 2, 3, 4, 5}{https://loptoanthaylinh.vn/thi-online/toan-1/bai-01}
```

### 2. Thay đổi thông tin trung tâm / hotline / thời gian làm bài
Mở file `Preamble_Toan1.tex` hoặc `main.tex` và chỉnh sửa tại macro `\TaoPhieuKiemTra`.

---

## 📋 PROMPT KẾ HOẠCH MẪU ĐỂ TÁI SỬ DỤNG
Toàn bộ đặc tả, cấu hình Preamble, macro khung đề thi gọn đẹp (không phần thông tin/điểm số, kèm Hotline 0866976878 và mã QR) đã được lưu thành tài liệu độc lập:
👉 Xem chi tiết tại: [`PROMPT_KE_HOACH_TAO_DE_THI.md`](./PROMPT_KE_HOACH_TAO_DE_THI.md)
