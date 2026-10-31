# BỘ 20 ĐỀ KIỂM TRA GIỮA HỌC KỲ 1 -- TOÁN LỚP 2
## CHƯƠNG TRÌNH GDPT 2018 (KẾT NỐI TRI THỨC / CÁNH DIỀU / CHÂN TRỜI SÁNG TẠO)
### Hệ sinh thái Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 📌 1. Giới thiệu tổng quan
Bộ **20 đề kiểm tra Giữa Học kỳ 1 Toán 2** được biên soạn chuẩn hóa theo khung ma trận đánh giá năng lực của Chương trình Giáo dục phổ thông 2018 và Thông tư 27/2020/TT-BGDĐT.

- **Thời gian làm bài:** 40 phút / đề.
- **Thang điểm:** 10,0 điểm (Trắc nghiệm 3,0 điểm + Tự luận 7,0 điểm).
- **Cấu trúc:** 12 câu hỏi chuẩn chia đều theo 3 mức độ nhận thức (Mức 1: 40%, Mức 2: 40%, Mức 3: 20%).
- **Lời giải:** 100% câu hỏi và bài toán đều có lời giải chi tiết `\loigiai{...}` từng bước.

---

## 📊 2. Bảng Ma trận cấu trúc chuẩn từng đề thi

| Phần | Câu | Dạng bài | Phạm vi kiến thức | Mức độ | Điểm |
| :--- | :---: | :--- | :--- | :---: | :---: |
| **Phần I: Trắc nghiệm**<br>*(3,0 điểm)* | **Câu 1** | Số & Tia số | Đọc, viết, so sánh số phạm vi 100, số liền trước/sau, tia số | Mức 1 | 0,5 đ |
| | **Câu 2** | Thành phần phép tính | Nhận biết Số hạng, Tổng, Số bị trừ, Số trừ, Hiệu | Mức 1 | 0,5 đ |
| | **Câu 3** | Đo lường thực tế | Nhận biết và tính toán đơn vị $\text{kg}$, lít ($l$), $\text{dm}$, $\text{cm}$ | Mức 1 | 0,5 đ |
| | **Câu 4** | Hình học phẳng | Nhận biết điểm, đoạn thẳng, ba điểm thẳng hàng, đường thẳng/cong | Mức 1 | 0,5 đ |
| | **Câu 5** | So sánh số / Biểu thức | So sánh hai số có 2 chữ số hoặc so sánh hai biểu thức | Mức 2 | 0,5 đ |
| | **Câu 6** | Tính nhẩm 2 phép tính | Thực hiện biểu thức cộng trừ qua 10 phạm vi 20 | Mức 2 | 0,5 đ |
| **Phần II: Tự luận**<br>*(7,0 điểm)* | **Bài 1** | Tính nhẩm bảng tính | Bảng cộng, trừ qua 10 trong phạm vi 20 (4 phép tính) | Mức 1 | 1,0 đ |
| | **Bài 2** | Đặt tính rồi tính | Cộng, trừ không nhớ trong phạm vi 100 (3 phép tính) | Mức 2 | 1,5 đ |
| | **Bài 3** | Tính kèm đơn vị đo | Biểu thức 2 bước tính kèm đơn vị $\text{kg}$, lít | Mức 2 | 1,0 đ |
| | **Bài 4** | Toán có lời văn | Bài toán về nhiều hơn hoặc ít hơn một số đơn vị | Mức 2 | 1,5 đ |
| | **Bài 5** | Toán thực tế đời sống | Bài toán tình huống thực tế (cân đo, rót nước, thu hoạch) | Mức 3 | 1,0 đ |
| | **Bài 6** | Tư duy logic / Tìm số | Tìm số theo quy luật, bài toán bi, bài toán que tính, đếm hình | Mức 3 | 1,0 đ |

---

## 📂 3. Danh mục tập tin

```text
1.SACH/LOP2/DE_THI_GIUA_HK1/
├── ex_test.sty                       # Style LaTeX chuẩn của Lớp Toán Thầy Lĩnh
├── Main_GHK1_Toan2.tex               # Master file LaTeX tổng hợp kèm lời giải (61 trang)
├── Main_GHK1_Toan2.pdf               # Master PDF bản kèm lời giải chi tiết
├── Main_GHK1_Toan2_DeThi.tex         # Master file LaTeX bản đề thi học sinh (41 trang)
├── Main_GHK1_Toan2_DeThi.pdf         # Master PDF bản in đề thi cho học sinh
├── README.md                         # Bảng ma trận & tài liệu hướng dẫn
├── De_01.tex ... De_20.tex           # 20 file đề thi TeX độc lập
└── PDF_DeThi_TungBai/
    ├── DE_RIENG/                     # 20 đề thi riêng cho học sinh (2 trang/đề, khổ A4 in 2 mặt)
    │   ├── De_01_DeThi.pdf
    │   └── ...
    └── GIAI_RIENG/                   # 20 lời giải riêng chi tiết (3 trang/đề)
        ├── De_01_LoiGiai.pdf
        └── ...
```

---

## 🛠️ 4. Hướng dẫn biên dịch sang PDF

1. **In đề thi cho học sinh (ẩn lời giải):**
   Trong file `Main_GHK1_Toan2.tex` (hoặc từng file `De_XX.tex`), cấu hình:
   ```latex
   \usepackage[dethi]{ex_test}
   %\usepackage[loigiai]{ex_test}
   ```
2. **In kèm đáp án chi tiết (dành cho giáo viên & phụ huynh):**
   ```latex
   %\usepackage[dethi]{ex_test}
   \usepackage[loigiai]{ex_test}
   ```
