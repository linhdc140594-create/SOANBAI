# KẾ HOẠCH NỘI DUNG & THI CÔNG CHI TIẾT TOÁN 6 - TUẦN 07 - BUỔI 02
## CHỦ ĐỀ: ĐỀ ÔN TẬP KIỂM TRA GIỮA HỌC KỲ 1 (ĐỀ SỐ 02) - TỔNG HỢP SỐ HỌC & HÌNH PHẲNG THỰC TẾ
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)
### Áp dụng: Phiếu kiểm tra định kỳ 45 phút - Cấu trúc Tối ưu Mới (10 câu ngắn + 4 bài tự luận) - 4 mã đề: 101, 102, 103, 104

---

## 🎯 I. NGUYÊN TẮC THIẾT KẾ BỐ CỤC MỚI (TỐI ƯU HẾT CỠ)

1. **Bỏ phần Chủ đề, Thời gian:**
   - Dòng tiêu đề trên cùng chỉ là 1 bảng duy nhất 1 hàng: `Tên phiếu` và `Mã đề - Trang`.
   - Học sinh tự ghi tên lên lề trên cùng (top margin) của tờ giấy A4.
2. **Bỏ hoàn toàn bảng điền đáp án:** 
   - Dùng lệnh `\shortans` ở cuối mỗi câu hỏi (với `\SAOPTN{widthSA=2.8,heightSA=0.62}`).
   - Tự động sinh ô `KQ: [     ]` bo góc thẩm mỹ ở mép phải của câu hỏi.
3. **Bỏ phân chia "Phần I", "Phần II":**
   - Đánh số câu liền mạch từ **Câu 1 đến Câu 14**.
   - Bỏ các dòng tiêu đề rườm rà chiếm diện tích.
4. **10 câu trắc nghiệm trả lời ngắn (Câu 1 đến Câu 10):**
   - Quét toàn bộ kiến thức Giữa HK1: Tập hợp & số phần tử, Số La Mã, Chia hai lũy thừa cùng cơ số, Thứ tự thực hiện phép tính, Tính chất chia hết của một tổng, Dấu hiệu chia hết cho 9, Nhận biết số nguyên tố, Đặc điểm hình phẳng (trục đối xứng/góc/cạnh), Chu vi hình vuông, Diện tích hình bình hành.
5. **Bảo toàn quy chuẩn in ấn (Layout Gold Standard):**
   - Đúng **2 trang A4 / mã đề** (Trang 1: Mặt trước; Trang 2: Mặt sau).
   - Đóng gói trọn vẹn **4 mã đề (101, 102, 103, 104)** trong 1 file `.tex` $\rightarrow$ Biên dịch ra **chính xác 8 trang PDF**.
   - Dòng kẻ chấm mờ (`\oBaiTap` và `\dongke`) được tính toán chuẩn xác để chạm sát lề đáy giấy cả 2 mặt.

---

## 📐 II. MA TRẬN THANG ĐIỂM & BỐ CỤC TRANG IN (TỔNG 10 ĐIỂM)

### 1. Phân bổ điểm chi tiết
* **Câu 1 $\to$ Câu 10 (2,5 điểm):** 10 câu trả lời ngắn (`\shortans`), mỗi câu $0{,}25$ điểm.
* **Câu 11 (2,0 điểm):** Thực hiện phép tính (4 ý $a, b, c, d$), mỗi ý $0{,}5$ điểm.
* **Câu 12 (2,0 điểm):** Tìm số tự nhiên $x$ (4 ý $a, b, c, d$), mỗi ý $0{,}5$ điểm.
* **Câu 13 (2,5 điểm):** Bài toán thực tế Chu vi & Diện tích lát gạch nền (2 ý $a, b$), mỗi ý $1{,}25$ điểm.
* **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết của tổng lũy thừa (1,0 điểm).
$$\implies \text{TỔNG ĐIỂM: } 2{,}5 + 2{,}0 + 2{,}0 + 2{,}5 + 1{,}0 = 10{,}0\text{ ĐIỂM}$$

---

### 2. Bố cục 2 trang A4
* **Mặt trước (Trang 1/2):**
  * Khung tiêu đề ngắn gọn (1 dòng): `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 07 - BUỔI 02 | Mã đề: <MÃ> - Trang 1/2`.
  * Bảng Điểm số & Lời nhận xét: Chiều cao chuẩn `\rule{0pt}{1.8cm}`.
  * **Câu 1 đến Câu 10:** 10 câu trả lời ngắn kèm ô `\shortans`.
  * **Câu 11 (2,0 điểm):** Thực hiện phép tính ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[10]`** (10 dòng kẻ chấm mờ).
  * *(Vừa vặn 100% chạm sát mép dưới trang 1).*

* **Mặt sau (Trang 2/2):**
  * Khung tiêu đề rút gọn (1 dòng): `TOÁN 6 - TUẦN 07 - BUỔI 02 | Mã đề: <MÃ> - Trang 2/2`.
  * **Câu 12 (2,0 điểm):** Tìm số tự nhiên $x$ ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[5]`**.
  * **Câu 13 (2,5 điểm):** Bài toán thực tế hình học phẳng (2 ý $a, b$) đóng khung box kèm **`\dongke{11}`**.
  * **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết đóng khung box kèm **`\dongke{8}`**.
  * *(Vừa vặn 100% chạm sát mép dưới trang 2).*

---

## 🗺️ III. MA TRẬN NỘI DUNG CHI TIẾT 4 MÃ ĐỀ TƯƠNG ĐƯƠNG

### 1. CÂU 1 ĐẾN CÂU 10: TRẢ LỜI NGẮN (2,5 ĐIỂM - MỖI CÂU 0,25 ĐIỂM)

| Câu | Mức độ & Dạng kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Câu 1** | Số phần tử của tập hợp | Tập hợp $B = \{x \in \mathbb{N} \mid 16 \le x \le 55\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $40$** | Tập hợp $B = \{x \in \mathbb{N} \mid 18 \le x \le 67\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $50$** | Tập hợp $B = \{x \in \mathbb{N} \mid 12 \le x \le 71\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $60$** | Tập hợp $B = \{x \in \mathbb{N} \mid 15 \le x \le 84\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $70$** |
| **Câu 2** | Đọc chữ số La Mã | Số La Mã $\text{XIX}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $19$** | Số La Mã $\text{XXIII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $23$** | Số La Mã $\text{XXVIII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $28$** | Số La Mã $\text{XVI}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $16$** |
| **Câu 3** | Chia hai lũy thừa cùng cơ số | Viết gọn thương $3^8 : 3^3$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $3^5$** | Viết gọn thương $5^7 : 5^4$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $5^3$** | Viết gọn thương $2^9 : 2^5$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $2^4$** | Viết gọn thương $7^6 : 7^2$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $7^4$** |
| **Câu 4** | Thứ tự thực hiện phép tính | Giá trị của biểu thức $50 - 3 \cdot 3^2$ bằng bao nhiêu?<br>$\to$ **KQ: $23$** | Giá trị của biểu thức $70 - 4 \cdot 3^2$ bằng bao nhiêu?<br>$\to$ **KQ: $34$** | Giá trị của biểu thức $80 - 2 \cdot 4^2$ bằng bao nhiêu?<br>$\to$ **KQ: $48$** | Giá trị của biểu thức $90 - 3 \cdot 4^2$ bằng bao nhiêu?<br>$\to$ **KQ: $42$** |
| **Câu 5** | Tính chất chia hết của tổng | Số dư của phép chia tổng $(36 + 180 + 22)$ cho $9$ là bao nhiêu?<br>$\to$ **KQ: $4$** | Số dư của phép chia tổng $(45 + 270 + 32)$ cho $9$ là bao nhiêu?<br>$\to$ **KQ: $5$** | Số dư của phép chia tổng $(54 + 360 + 25)$ cho $9$ là bao nhiêu?<br>$\to$ **KQ: $7$** | Số dư của phép chia tổng $(63 + 180 + 42)$ cho $9$ là bao nhiêu?<br>$\to$ **KQ: $6$** |
| **Câu 6** | Dấu hiệu chia hết cho 9 | Tìm chữ số $x$ để số $\overline{3x5}$ chia hết cho $9$.<br>$\to$ **KQ: $1$** | Tìm chữ số $x$ để số $\overline{4x3}$ chia hết cho $9$.<br>$\to$ **KQ: $2$** | Tìm chữ số $x$ để số $\overline{5x1}$ chia hết cho $9$.<br>$\to$ **KQ: $3$** | Tìm chữ số $x$ để số $\overline{2x3}$ chia hết cho $9$.<br>$\to$ **KQ: $4$** |
| **Câu 7** | Nhận biết số nguyên tố | Trong các số $17; 21; 25; 27$, số nguyên tố là số nào?<br>$\to$ **KQ: $17$** | Trong các số $23; 33; 35; 39$, số nguyên tố là số nào?<br>$\to$ **KQ: $23$** | Trong các số $29; 39; 49; 51$, số nguyên tố là số nào?<br>$\to$ **KQ: $29$** | Trong các số $31; 45; 55; 57$, số nguyên tố là số nào?<br>$\to$ **KQ: $31$** |
| **Câu 8** | Đặc điểm hình phẳng | Một hình tam giác đều có bao nhiêu trục đối xứng?<br>$\to$ **KQ: $3$** | Một hình vuông có bao nhiêu trục đối xứng?<br>$\to$ **KQ: $4$** | Một hình lục giác đều có bao nhiêu đường chéo chính?<br>$\to$ **KQ: $3$** | Một hình thoi có bao nhiêu cạnh bằng nhau?<br>$\to$ **KQ: $4$** |
| **Câu 9** | Chu vi hình vuông | Một mảnh đất hình vuông có cạnh $15\text{ m}$. Chu vi mảnh đất là:<br>$\to$ **KQ: $60\text{ m}$** | Một mảnh đất hình vuông có cạnh $18\text{ m}$. Chu vi mảnh đất là:<br>$\to$ **KQ: $72\text{ m}$** | Một mảnh đất hình vuông có cạnh $25\text{ m}$. Chu vi mảnh đất là:<br>$\to$ **KQ: $100\text{ m}$** | Một mảnh đất hình vuông có cạnh $16\text{ m}$. Chu vi mảnh đất là:<br>$\to$ **KQ: $64\text{ m}$** |
| **Câu 10** | Diện tích hình bình hành | Hình bình hành có đáy $12\text{ cm}$, chiều cao $6\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $72\text{ cm}^2$** | Hình bình hành có đáy $15\text{ cm}$, chiều cao $8\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $120\text{ cm}^2$** | Hình bình hành có đáy $14\text{ cm}$, chiều cao $5\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $70\text{ cm}^2$** | Hình bình hành có đáy $16\text{ cm}$, chiều cao $7\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $112\text{ cm}^2$** |

---

### 2. CÂU 11: THỰC HIỆN PHÉP TÍNH (2,0 ĐIỂM - MỖI Ý 0,5 ĐIỂM)

* **Ý a (Tính trực tiếp có lũy thừa):**
  * **Mã 101:** $135 - 3^2 \cdot 4 + 2^4 \cdot 5 = 135 - 36 + 80 = 179$.
  * **Mã 102:** $145 - 2^4 \cdot 3 + 3^3 \cdot 2 = 145 - 48 + 54 = 151$.
  * **Mã 103:** $165 - 4^2 \cdot 3 + 2^5 \cdot 2 = 165 - 48 + 64 = 181$.
  * **Mã 104:** $185 - 5^2 \cdot 2 + 3^2 \cdot 6 = 185 - 50 + 54 = 189$.
* **Ý b (Tính nhanh đặt thừa số chung tròn trăm):**
  * **Mã 101:** $37 \cdot 64 + 37 \cdot 36 - 700 = 37 \cdot 100 - 700 = 3000$.
  * **Mã 102:** $43 \cdot 78 + 43 \cdot 22 - 300 = 43 \cdot 100 - 300 = 4000$.
  * **Mã 103:** $52 \cdot 83 + 52 \cdot 17 - 200 = 52 \cdot 100 - 200 = 5000$.
  * **Mã 104:** $61 \cdot 74 + 61 \cdot 26 - 100 = 61 \cdot 100 - 100 = 6000$.
* **Ý c (Biểu thức ngoặc tròn và lũy thừa trong ngoặc vuông):**
  * **Mã 101:** $200 : [66 - (19 - 15)^2] = 200 : [66 - 16] = 200 : 50 = 4$.
  * **Mã 102:** $240 : [76 - (18 - 14)^2] = 240 : [76 - 16] = 240 : 60 = 4$.
  * **Mã 103:** $280 : [86 - (17 - 13)^2] = 280 : [86 - 16] = 280 : 70 = 4$.
  * **Mã 104:** $320 : [96 - (16 - 12)^2] = 320 : [96 - 16] = 320 : 80 = 4$.
* **Ý d (Biểu thức lồng 3 tầng ngoặc $\{ \ [ \ ( \ ) \ ] \ \}$):**
  * **Mã 101:** $180 : \{ 75 - [22 + (16 - 14)^3] \} = 180 : \{ 75 - [22 + 8] \} = 180 : 45 = 4$.
  * **Mã 102:** $220 : \{ 85 - [22 + (17 - 15)^3] \} = 220 : \{ 85 - [22 + 8] \} = 220 : 55 = 4$.
  * **Mã 103:** $260 : \{ 95 - [22 + (18 - 16)^3] \} = 260 : \{ 95 - [22 + 8] \} = 260 : 65 = 4$.
  * **Mã 104:** $300 : \{ 105 - [22 + (19 - 17)^3] \} = 300 : \{ 105 - [22 + 8] \} = 300 : 75 = 4$.

---

### 3. CÂU 12: TÌM SỐ TỰ NHIÊN $x$ (2,0 ĐIỂM - MỖI Ý 0,5 ĐIỂM)

* **Ý a (Chuyển vế cơ bản với phép trừ):**
  * **Mã 101:** $3 \cdot x - 14 = 34 \implies 3x = 48 \implies x = 16$.
  * **Mã 102:** $4 \cdot x - 17 = 39 \implies 4x = 56 \implies x = 14$.
  * **Mã 103:** $5 \cdot x - 16 = 49 \implies 5x = 65 \implies x = 13$.
  * **Mã 104:** $6 \cdot x - 19 = 53 \implies 6x = 72 \implies x = 12$.
* **Ý b (Phương trình chứa ngoặc):**
  * **Mã 101:** $75 - 4 \cdot (x - 2) = 43 \implies 4(x-2) = 32 \implies x-2 = 8 \implies x = 10$.
  * **Mã 102:** $85 - 5 \cdot (x - 3) = 45 \implies 5(x-3) = 40 \implies x-3 = 8 \implies x = 11$.
  * **Mã 103:** $95 - 6 \cdot (x - 1) = 47 \implies 6(x-1) = 48 \implies x-1 = 8 \implies x = 9$.
  * **Mã 104:** $90 - 7 \cdot (x - 2) = 41 \implies 7(x-2) = 49 \implies x-2 = 7 \implies x = 9$.
* **Ý c (Tìm số mũ lũy thừa):**
  * **Mã 101:** $4 \cdot 3^{x-1} + 14 = 50 \implies 4 \cdot 3^{x-1} = 36 \implies 3^{x-1} = 9 = 3^2 \implies x = 3$.
  * **Mã 102:** $3 \cdot 2^{x+2} + 16 = 64 \implies 3 \cdot 2^{x+2} = 48 \implies 2^{x+2} = 16 = 2^4 \implies x = 2$.
  * **Mã 103:** $5 \cdot 2^{x+1} - 18 = 62 \implies 5 \cdot 2^{x+1} = 80 \implies 2^{x+1} = 16 = 2^4 \implies x = 3$.
  * **Mã 104:** $2 \cdot 5^{x-1} + 10 = 60 \implies 2 \cdot 5^{x-1} = 50 \implies 5^{x-1} = 25 = 5^2 \implies x = 3$.
* **Ý d (Dạng tìm ƯCLN của hai số):**
  * **Mã 101:** Tìm số tự nhiên $x$ lớn nhất, biết $36 \ \vdots \ x$ và $54 \ \vdots \ x \implies x = \text{ƯCLN}(36, 54) = 18$.
  * **Mã 102:** Tìm số tự nhiên $x$ lớn nhất, biết $40 \ \vdots \ x$ và $60 \ \vdots \ x \implies x = \text{ƯCLN}(40, 60) = 20$.
  * **Mã 103:** Tìm số tự nhiên $x$ lớn nhất, biết $42 \ \vdots \ x$ và $70 \ \vdots \ x \implies x = \text{ƯCLN}(42, 70) = 14$.
  * **Mã 104:** Tìm số tự nhiên $x$ lớn nhất, biết $48 \ \vdots \ x$ và $72 \ \vdots \ x \implies x = \text{ƯCLN}(48, 72) = 24$.

---

### 4. CÂU 13: BÀI TOÁN THỰC TẾ HÌNH HỌC PHẲNG (2,5 ĐIỂM - MỖI Ý 1,25 ĐIỂM)

* **Bối cảnh:** Bác Hải có một căn phòng hình chữ nhật và dự định dùng gạch men hình vuông để lát kín toàn bộ nền phòng.
* **Mã đề 101:** Căn phòng có chiều dài $12\text{ m}$, chiều rộng $8\text{ m}$. Gạch lát hình vuông cạnh $40\text{ cm}$, giá $22\ 000$ đồng/viên.
  * $a)$ (1,25đ) Chu vi căn phòng: $(12 + 8) \times 2 = 40\text{ m}$. Diện tích căn phòng: $12 \times 8 = 96\text{ m}^2$.
  * $b)$ (1,25đ) Diện tích một viên gạch: $40 \times 40 = 1600\text{ cm}^2 = 0{,}16\text{ m}^2$. Số viên gạch cần dùng: $96 : 0{,}16 = 600$ viên. Số tiền mua gạch: $600 \times 22\ 000 = 13\ 200\ 000$ đồng.
* **Mã đề 102:** Căn phòng có chiều dài $15\text{ m}$, chiều rộng $8\text{ m}$. Gạch lát hình vuông cạnh $50\text{ cm}$, giá $32\ 000$ đồng/viên.
  * $a)$ Chu vi: $(15 + 8) \times 2 = 46\text{ m}$. Diện tích: $15 \times 8 = 120\text{ m}^2$.
  * $b)$ Diện tích một viên gạch: $50 \times 50 = 2500\text{ cm}^2 = 0{,}25\text{ m}^2$. Số viên gạch: $120 : 0{,}25 = 480$ viên. Số tiền mua gạch: $480 \times 32\ 000 = 15\ 360\ 000$ đồng.
* **Mã đề 103:** Căn phòng có chiều dài $16\text{ m}$, chiều rộng $9\text{ m}$. Gạch lát hình vuông cạnh $40\text{ cm}$, giá $24\ 000$ đồng/viên.
  * $a)$ Chu vi: $(16 + 9) \times 2 = 50\text{ m}$. Diện tích: $16 \times 9 = 144\text{ m}^2$.
  * $b)$ Diện tích một viên gạch: $0{,}16\text{ m}^2$. Số viên gạch: $144 : 0{,}16 = 900$ viên. Số tiền mua gạch: $900 \times 24\ 000 = 21\ 600\ 000$ đồng.
* **Mã đề 104:** Căn phòng có chiều dài $20\text{ m}$, chiều rộng $9\text{ m}$. Gạch lát hình vuông cạnh $50\text{ cm}$, giá $35\ 000$ đồng/viên.
  * $a)$ Chu vi: $(20 + 9) \times 2 = 58\text{ m}$. Diện tích: $20 \times 9 = 180\text{ m}^2$.
  * $b)$ Diện tích một viên gạch: $0{,}25\text{ m}^2$. Số viên gạch: $180 : 0{,}25 = 720$ viên. Số tiền mua gạch: $720 \times 35\ 000 = 25\ 200\ 000$ đồng.

---

### 5. CÂU 14: BÀI TOÁN PHÂN LOẠI HỌC SINH GIỎI (1,0 ĐIỂM)

* **Mã đề 101:** Cho tổng $A = 2 + 2^2 + 2^3 + 2^4 + \dots + 2^{20}$. Chứng minh rằng $A$ chia hết cho $3$.
  * *Lời giải:* Tổng $A$ có $20$ số hạng, ta ghép thành $10$ nhóm, mỗi nhóm $2$ số hạng:
    $$A = (2 + 2^2) + 2^2(2 + 2^2) + \dots + 2^{18}(2 + 2^2) = 6 \cdot (1 + 2^2 + \dots + 2^{18})$$
    Vì $6 \ \vdots \ 3$ nên $A \ \vdots \ 3$.
* **Mã đề 102:** Cho tổng $B = 3 + 3^2 + 3^3 + 3^4 + \dots + 3^{20}$. Chứng minh rằng $B$ chia hết cho $4$.
  * *Lời giải:* Tổng $B$ có $20$ số hạng, ghép nhóm tương tự:
    $$B = (3 + 3^2) + 3^2(3 + 3^2) + \dots + 3^{18}(3 + 3^2) = 12 \cdot (1 + 3^2 + \dots + 3^{18})$$
    Vì $12 \ \vdots \ 4$ nên $B \ \vdots \ 4$.
* **Mã đề 103:** Cho tổng $C = 4 + 4^2 + 4^3 + 4^4 + \dots + 4^{20}$. Chứng minh rằng $C$ chia hết cho $5$.
  * *Lời giải:* Tổng $C$ có $20$ số hạng, ghép nhóm tương tự:
    $$C = (4 + 4^2) + 4^2(4 + 4^2) + \dots + 4^{18}(4 + 4^2) = 20 \cdot (1 + 4^2 + \dots + 4^{18})$$
    Vì $20 \ \vdots \ 5$ nên $C \ \vdots \ 5$.
* **Mã đề 104:** Cho tổng $D = 5 + 5^2 + 5^3 + 5^4 + \dots + 5^{20}$. Chứng minh rằng $D$ chia hết cho $6$.
  * *Lời giải:* Tổng $D$ có $20$ số hạng, ghép nhóm tương tự:
    $$D = (5 + 5^2) + 5^2(5 + 5^2) + \dots + 5^{18}(5 + 5^2) = 30 \cdot (1 + 5^2 + \dots + 5^{18})$$
    Vì $30 \ \vdots \ 6$ nên $D \ \vdots \ 6$.
