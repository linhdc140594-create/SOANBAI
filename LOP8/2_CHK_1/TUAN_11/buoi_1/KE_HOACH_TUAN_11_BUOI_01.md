# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 11 - BUỔI 01 (TOÁN 8)
## CHỦ ĐỀ: BÀI 16: ĐƯỜNG TRUNG BÌNH CỦA TAM GIÁC & TỔNG ÔN PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ
### Bám sát chương trình: SGK Toán 8 - Kết nối tri thức với cuộc sống (Chương IV) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững định nghĩa đường trung bình của tam giác (đoạn nối trung điểm hai cạnh).
   - Nắm vững định lí tính chất đường trung bình: Đường trung bình song song với cạnh thứ ba và bằng một nửa cạnh ấy ($MN \parallel BC$ và $MN = \dfrac{1}{2}BC$).
   - Vận dụng tính độ dài đoạn thẳng, chứng minh hai đường thẳng song song, chứng minh tứ giác là hình bình hành (tứ giác có hai đường chéo cắt nhau tại trung điểm mỗi đường).
   - Củng cố Đại số: Thành thạo 4 phương pháp phân tích đa thức thành nhân tử (đặt nhân tử chung, dùng hằng đẳng thức, nhóm hạng tử, tách hạng tử tam thức bậc hai).
   - Kỹ năng tìm $x$: Giải phương trình tích, phương trình hiệu hai bình phương, bình phương một nhị thức bằng 0.
   - Vận dụng cao: Tìm giá trị nhỏ nhất (GTNN) của tam thức bậc hai $A = x^2 - 2ax + b$.

2. **Kỹ năng & Năng lực:**
   - Vẽ hình chính xác, trực quan với TikZ; ký hiệu đầy đủ trung điểm, đoạn thẳng bằng nhau.
   - Trình bày bài giải hình học rõ ràng, lập luận logic 2 cột (`\dongkeHaiCot{11}`).
   - Kỹ năng biến đổi đại số chính xác, nghiệm nguyên đẹp.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

| STT | Dạng bài | Số câu / Ý | Điểm số | Vị trí trên phiếu | Quy chuẩn định dạng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Trả lời ngắn (Short Answer) | 10 câu | 2,5 đ | Trang 1 (Đầu trang) | Lệnh `\shortans`, ô bo góc `KQ: [   ]` sát mép phải. |
| **2** | Phân tích đa thức thành nhân tử | 6 ý ($a \to f$) | 3,0 đ | Trang 1 (Cuối trang) | Bảng $3 \times 2$, dùng `\oBaiTap[5]` lấp kín 100% lề dưới. |
| **3** | Tìm $x$ | 4 ý ($a \to d$) | 2,0 đ | Trang 2 (Đầu trang) | Bảng $2 \times 2$, dùng `\oBaiTap[5]`. |
| **4** | Hình học Đường trung bình | 2 ý ($a, b$) | 2,0 đ | Trang 2 (Giữa trang) | Ghép box `tabularx` có hình TikZ, bài giải `\dongkeHaiCot{11}`. |
| **5** | Vận dụng cao điểm 10 | 1 bài | 0,5 đ | Trang 2 (Cuối trang) | Ghép box `tabularx`, bài giải `\dongkeHaiCot{6}` sát lề dưới. |
| **TỔNG** | | **23 mục** | **10,0 đ** | **2 mặt A4** | **Chính xác 8 trang PDF cho 4 mã đề (101-104)** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Định nghĩa đường trung bình | $\Delta ABC$, $M, N$ là trung điểm $AB, AC \to$ **Đường trung bình** | $\Delta MNP$, $E, F$ là trung điểm $MN, MP \to$ **Đường trung bình** | $\Delta DEF$, $I, K$ là trung điểm $DE, DF \to$ **Đường trung bình** | $\Delta ABC$, $D, E$ là trung điểm $AB, BC \to$ **Đường trung bình** |
| **2** | Tính cạnh đáy từ đường TB | $MN=6\text{ cm} \implies BC =$ **$12\text{ cm}$** | $MN=7\text{ cm} \implies BC =$ **$14\text{ cm}$** | $IK=8\text{ cm} \implies EF =$ **$16\text{ cm}$** | $EF=9\text{ cm} \implies NP =$ **$18\text{ cm}$** |
| **3** | Chu vi tam giác trung điểm | $C_{\Delta ABC}=24\text{ cm} \implies C =$ **$12\text{ cm}$** | $C_{\Delta ABC}=30\text{ cm} \implies C =$ **$15\text{ cm}$** | $C_{\Delta DEF}=28\text{ cm} \implies C =$ **$14\text{ cm}$** | $C_{\Delta MNP}=36\text{ cm} \implies C =$ **$18\text{ cm}$** |
| **4** | Đặt nhân tử chung đơn giản | Phân tích $3x^2 - 6x \to$ **$3x(x - 2)$** | Phân tích $4x^2 - 8x \to$ **$4x(x - 2)$** | Phân tích $5x^2 - 10x \to$ **$5x(x - 2)$** | Phân tích $2x^2 - 6x \to$ **$2x(x - 3)$** |
| **5** | Tính nhanh $a^2 - b^2$ | $65^2 - 35^2 =$ **$3\,000$** | $75^2 - 25^2 =$ **$5\,000$** | $85^2 - 15^2 =$ **$7\,000$** | $95^2 - 5^2 =$ **$9\,000$** |
| **6** | Khai triển hằng đẳng thức | $(x+3)^2 = x^2+ax+9 \implies a =$ **$6$** | $(x-4)^2 = x^2-bx+16 \implies b =$ **$8$** | $(2x+1)^2 = 4x^2+cx+1 \implies c =$ **$4$** | $(x+5)^2 = x^2+dx+25 \implies d =$ **$10$** |
| **7** | Bậc của đa thức thu gọn | $P = 4x^3 y^2 - 5x^2 y^4 + 7 \to$ Bậc **$6$** | $Q = 5x^2 y^4 - 3x^3 y^2 + 2 \to$ Bậc **$6$** | $R = 2x^5 y - 6x^2 y^3 + 9 \to$ Bậc **$6$** | $T = 7xy^5 - 4x^3 y^2 + 5 \to$ Bậc **$6$** |
| **8** | Tính giá trị biểu thức | $x+y=5 \implies x(x+y)+y(x+y) =$ **$25$** | $x+y=6 \implies x(x+y)+y(x+y) =$ **$36$** | $x+y=7 \implies x(x+y)+y(x+y) =$ **$49$** | $x+y=8 \implies x(x+y)+y(x+y) =$ **$64$** |
| **9** | Thực tế đo qua hồ nước | $MN = 45\text{ m} \implies AB =$ **$90\text{ m}$** | $MN = 55\text{ m} \implies AB =$ **$110\text{ m}$** | $MN = 38\text{ m} \implies AB =$ **$76\text{ m}$** | $MN = 62\text{ m} \implies AB =$ **$124\text{ m}$** |
| **10** | Dấu hiệu hình học | Hai cặp cạnh đối song song $\to$ **Hình bình hành** | Hình bình hành có 1 góc vuông $\to$ **Hình chữ nhật** | Hình bình hành có 2 cạnh kề bằng nhau $\to$ **Hình thoi** | Hình chữ nhật có 2 cạnh kề bằng nhau $\to$ **Hình vuông** |

---

### 2. CÂU 11 (3,0 ĐIỂM - PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ - 6 Ý $A \to F$)

* **Mã đề 101:**
  - $a)$ $3x^2 - 6x = 3x(x - 2)$
  - $b)$ $x^2 - 16 = (x - 4)(x + 4)$
  - $c)$ $x^2 - 6x + 9 = (x - 3)^2$
  - $d)$ $xy + 2y + 3x + 6 = (x + 2)(y + 3)$
  - $e)$ $x^2 - 2xy + y^2 - 16 = (x - y - 4)(x - y + 4)$
  - $f)$ $x^2 - 5x + 6 = (x - 2)(x - 3)$

* **Mã đề 102:**
  - $a)$ $4x^2 - 8x = 4x(x - 2)$
  - $b)$ $x^2 - 25 = (x - 5)(x + 5)$
  - $c)$ $x^2 + 8x + 16 = (x + 4)^2$
  - $d)$ $xy + 3y + 2x + 6 = (x + 3)(y + 2)$
  - $e)$ $x^2 - 2xy + y^2 - 25 = (x - y - 5)(x - y + 5)$
  - $f)$ $x^2 - 7x + 12 = (x - 3)(x - 4)$

* **Mã đề 103:**
  - $a)$ $5x^2 - 15x = 5x(x - 3)$
  - $b)$ $4x^2 - 9 = (2x - 3)(2x + 3)$
  - $c)$ $x^2 - 10x + 25 = (x - 5)^2$
  - $d)$ $xy + 4y + 2x + 8 = (x + 4)(y + 2)$
  - $e)$ $x^2 + 2xy + y^2 - 9 = (x + y - 3)(x + y + 3)$
  - $f)$ $x^2 + 5x + 6 = (x + 2)(x + 3)$

* **Mã đề 104:**
  - $a)$ $2x^2 - 8x = 2x(x - 4)$
  - $b)$ $9x^2 - 16 = (3x - 4)(3x + 4)$
  - $c)$ $x^2 + 12x + 36 = (x + 6)^2$
  - $d)$ $xy + 5y + 3x + 15 = (x + 5)(y + 3)$
  - $e)$ $x^2 + 2xy + y^2 - 49 = (x + y - 7)(x + y + 7)$
  - $f)$ $x^2 - 8x + 15 = (x - 3)(x - 5)$

---

### 3. CÂU 12 (2,0 ĐIỂM - TÌM $x$ - 4 Ý $A \to D$)

| Ý | Dạng phương trình | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **a** | Nhân tử chung cơ bản | $x^2 - 4x = 0 \to x \in \{0; 4\}$ | $x^2 - 5x = 0 \to x \in \{0; 5\}$ | $x^2 + 3x = 0 \to x \in \{0; -3\}$ | $x^2 + 6x = 0 \to x \in \{0; -6\}$ |
| **b** | Hiệu hai bình phương | $x^2 - 36 = 0 \to x = \pm 6$ | $x^2 - 49 = 0 \to x = \pm 7$ | $x^2 - 81 = 0 \to x = \pm 9$ | $x^2 - 64 = 0 \to x = \pm 8$ |
| **c** | Bình phương bằng 0 | $x^2 - 8x + 16 = 0 \to x = 4$ | $x^2 - 10x + 25 = 0 \to x = 5$ | $x^2 + 6x + 9 = 0 \to x = -3$ | $x^2 + 10x + 25 = 0 \to x = -5$ |
| **d** | Phương trình tích | $(x-2)(x+3)-2(x+3)=0 \to x \in \{-3; 4\}$ | $(x-1)(x+4)-3(x+4)=0 \to x = \pm 4$ | $(x-3)(x+2)-2(x+2)=0 \to x \in \{-2; 5\}$ | $(x-2)(x+5)-3(x+5)=0 \to x = \pm 5$ |

---

### 4. CÂU 13 (2,0 ĐIỂM - HÌNH HỌC ĐƯỜNG TRUNG BÌNH & HÌNH BÌNH HÀNH)

* **Mã đề 101:** Cho tam giác $ABC$ nhọn ($AB < AC$). Gọi $D, E$ lần lượt là trung điểm của $AB$ và $AC$.
  - $a)$ (1,0 điểm): Chứng minh $DE$ là đường trung bình của tam giác $ABC$. Biết $BC = 12\text{ cm}$, tính độ dài đoạn thẳng $DE$.
  - $b)$ (1,0 điểm): Trên tia đối của tia $ED$ lấy điểm $F$ sao cho $EF = ED$. Chứng minh tứ giác $ADCF$ là hình bình hành.
* **Mã đề 102:** Cho tam giác $MNP$ nhọn ($MN < MP$). Gọi $D, E$ lần lượt là trung điểm của $MN$ và $MP$.
  - $a)$ (1,0 điểm): Chứng minh $DE$ là đường trung bình của tam giác $MNP$. Biết $NP = 14\text{ cm}$, tính độ dài đoạn thẳng $DE$.
  - $b)$ (1,0 điểm): Trên tia đối của tia $ED$ lấy điểm $F$ sao cho $EF = ED$. Chứng minh tứ giác $MDFP$ là hình bình hành.
* **Mã đề 103:** Cho tam giác $ABC$ nhọn ($AB < AC$). Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$.
  - $a)$ (1,0 điểm): Chứng minh $MN$ là đường trung bình của tam giác $ABC$. Biết $BC = 16\text{ cm}$, tính độ dài đoạn thẳng $MN$.
  - $b)$ (1,0 điểm): Trên tia đối của tia $NM$ lấy điểm $P$ sao cho $NP = NM$. Chứng minh tứ giác $AMCP$ là hình bình hành.
* **Mã đề 104:** Cho tam giác $DEF$ nhọn ($DE < DF$). Gọi $M, N$ lần lượt là trung điểm của $DE$ và $DF$.
  - $a)$ (1,0 điểm): Chứng minh $MN$ là đường trung bình của tam giác $DEF$. Biết $EF = 18\text{ cm}$, tính độ dài đoạn thẳng $MN$.
  - $b)$ (1,0 điểm): Trên tia đối của tia $NM$ lấy điểm $P$ sao cho $NP = NM$. Chứng minh tứ giác $DMFP$ là hình bình hành.

---

### 5. CÂU 14 (0,5 ĐIỂM - VẬN DỤNG CAO ĐIỂM 10)

* **Mã đề 101:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 6x + 14$.
  - *Lời giải:* $A = (x^2 - 6x + 9) + 5 = (x - 3)^2 + 5$. Vì $(x - 3)^2 \ge 0$ với mọi $x$ nên $A \ge 5$. Dấu "$=$" xảy ra khi $x = 3$. Vậy $\min A = 5$ khi $x = 3$.
* **Mã đề 102:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 8x + 21$.
  - *Lời giải:* $A = (x - 4)^2 + 5 \ge 5$. Dấu "$=$" xảy ra khi $x = 4$. Vậy $\min A = 5$ khi $x = 4$.
* **Mã đề 103:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 4x + 11$.
  - *Lời giải:* $A = (x - 2)^2 + 7 \ge 7$. Dấu "$=$" xảy ra khi $x = 2$. Vậy $\min A = 7$ khi $x = 2$.
* **Mã đề 104:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 10x + 31$.
  - *Lời giải:* $A = (x - 5)^2 + 6 \ge 6$. Dấu "$=$" xảy ra khi $x = 5$. Vậy $\min A = 6$ khi $x = 5$.

