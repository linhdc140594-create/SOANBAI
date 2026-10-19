# BỘ ĐỀ KIỂM TRA GIỮA HỌC KÌ I – TOÁN 7 (CÔNG VĂN 7991/BGDĐT-GDTrH)

Thư mục lưu trữ bộ đề kiểm tra, ma trận, bản đặc tả và đáp án chuẩn theo cấu trúc Công văn 7991/BGDĐT-GDTrH (Áp dụng cho chương trình SGK Kết nối tri thức với cuộc sống – Năm học 2026 – 2027).

---

## 📂 CẤU TRÚC THƯ MỤC

```text
DE_KIEM_TRA_CV7991/
├── de_kiem_tra_7991.json        # Dữ liệu JSON toàn diện (metadata, ma trận, đặc tả, đề 1, đề 2, tikz)
├── export_latex_files.py        # Script Python tự động sinh file TeX và biên dịch ra PDF
├── ma_tran_va_dac_ta.tex        # Mã nguồn LaTeX Khung Ma trận và Bản đặc tả (Khổ ngang)
├── ma_tran_va_dac_ta.pdf        # File PDF Ma trận & Bản đặc tả (3 trang)
├── de_01.tex                    # Mã nguồn LaTeX Đề 01 (Chuẩn 2 trang A4 in 2 mặt)
├── de_01.pdf                    # File PDF Đề 01 (Chính xác 2 trang A4)
├── dap_an_de_01.tex             # Mã nguồn LaTeX Đáp án & Hướng dẫn chấm Đề 01
├── dap_an_de_01.pdf             # File PDF Đáp án Đề 01 (1 trang A4)
├── de_02.tex                    # Mã nguồn LaTeX Đề 02 (Chuẩn 2 trang A4 in 2 mặt)
├── de_02.pdf                    # File PDF Đề 02 (Chính xác 2 trang A4)
├── dap_an_de_02.tex             # Mã nguồn LaTeX Đáp án & Hướng dẫn chấm Đề 02
├── dap_an_de_02.pdf             # File PDF Đáp án Đề 02 (1 trang A4)
└── README.md                    # Tài liệu hướng dẫn này
```

---

## 📊 MA TRẬN & ĐẶC TẢ THEO CÔNG VĂN 7991

- **Thời gian làm bài:** 90 phút (Tổng điểm: 10,0 điểm).
- **Phân bổ phân môn:** 
  - Đại số (Chương I: Số hữu tỉ + Chương II: Số thực): **6,5 điểm (65%)**.
  - Hình học (Chương III: Góc và hai đường thẳng song song): **3,5 điểm (35%)**.
- **Tỉ lệ mức độ nhận thức:**
  - Nhận biết: **4,0 điểm (40%)**.
  - Thông hiểu: **3,0 điểm (30%)**.
  - Vận dụng: **3,0 điểm (30%)**.
- **Cấu trúc 4 phần của đề thi:**
  - **Phần I:** 12 câu trắc nghiệm nhiều phương án lựa chọn (3,0 điểm – 0,25đ/câu).
  - **Phần II:** 2 câu trắc nghiệm Đúng / Sai (2,0 điểm – gồm 4 ý a, b, c, d mỗi câu; tính điểm lũy tiến 0,1đ – 0,25đ – 0,5đ – 1,0đ).
  - **Phần III:** 4 câu trắc nghiệm trả lời ngắn (2,0 điểm – 0,5đ/câu).
  - **Phần IV:** 3 câu tự luận (3,0 điểm – Câu 19: 1,0đ; Câu 20: 1,0đ; Câu 21: 1,0đ).

---

## 🎨 HÌNH VẼ TIKZ
- Tất cả hình vẽ hình học (góc kề bù, tia phân giác, cát tuyến cắt hai đường thẳng song song, đường vuông góc, tia phân giác trong tam giác/góc) đều được vẽ bằng **TikZ thuần**, tỷ lệ chuẩn xác học thuật, số đo góc và nhãn chữ được bố trí cách xa đường nét, không bị chồng đè khi in ấn.

---

## 🚀 HƯỚNG DẪN BIÊN DỊCH LẠI
Nếu có chỉnh sửa nội dung, chỉ cần chạy lệnh:
```bash
python export_latex_files.py
```
Script sẽ tự động cập nhật cả 5 file `.tex` và biên dịch ra các file `.pdf` tương ứng bằng `pdflatex`.
