# KHO DỮ LIỆU & CÔNG CỤ SOẠN PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN THCS

Kho lưu trữ chuyên biệt, siêu nhẹ dành riêng cho việc biên soạn và quản lý **Phiếu Kiểm Tra Định Kỳ môn Toán THCS** (Lớp 6, 7, 8, 9).

---

## 📂 Cấu Trúc Thư Mục

```text
PHIEU_KIEM_TRA_THCS/
├── .agents/                        # Kỹ năng tự động hóa biên soạn (phieu-kiem-tra-generator)
│   └── skills/
│       └── phieu-kiem-tra-generator/
├── AGENTS.md                       # Hướng dẫn chi tiết & Quy chuẩn kỹ thuật LaTeX
├── LOP6/                           # Phiếu kiểm tra Toán 6
│   ├── 1_GHK_1/
│   │   ├── TUAN_1/ ... TUAN_8/
│   │   └── KE_HOACH_NOI_DUNG_GHK1.md
│   ├── 2_CHK_1/
│   ├── 3_GHK_2/
│   ├── 4_CHK_2/
│   ├── KE_HOACH_NOI_DUNG_35_TUAN.md
│   └── ex_test.sty
├── LOP7/                           # Phiếu kiểm tra Toán 7
├── LOP8/                           # Phiếu kiểm tra Toán 8
├── LOP9/                           # Phiếu kiểm tra Toán 9
├── .gitignore
└── README.md
```

---

## 🎯 Quy Chuẩn Phiếu Đề Chuẩn (Layout Gold Standard)

* **4 Mã đề tương đương:** 101, 102, 103, 104.
* **Quy chuẩn độ dài:** Đúng 2 mặt A4 (8 trang PDF cho cả 4 mã đề).
* **Ma trận 10 điểm:**
  * **Câu 1 – 10 (2,5đ):** Trả lời ngắn, dùng lệnh `\shortans{...}` tạo ô kết quả mép phải.
  * **Câu 11 (2,0đ):** Thực hiện phép tính ($2 \times 2$ ô, `\oBaiTap[8]`).
  * **Câu 12 (2,0đ):** Tìm $x$ ($2 \times 2$ ô, `\oBaiTap[5]`).
  * **Câu 13 (2,5đ):** Bài toán thực tế / Lời văn (`\dongke{11}`).
  * **Câu 14 (1,0đ):** Bài toán nâng cao (`\dongke{7}`).

---

## 🔄 Quy Trình 3 Bước Biên Soạn

1. **Bước 1 (Planning):** Soạn `KE_HOACH_TUAN_<X>_BUOI_<Y>.md` và trình duyệt.
2. **Bước 2 (Generation):** Viết script Python sinh file `.tex` và biên dịch bằng `pdflatex`.
3. **Bước 3 (Auto-fill & Polish):** Canh dòng kẻ chấm mờ phủ kín sát đáy giấy, kiểm tra đúng 8 trang PDF, xuất `DAP_AN_VA_THANG_DIEM.md`.
