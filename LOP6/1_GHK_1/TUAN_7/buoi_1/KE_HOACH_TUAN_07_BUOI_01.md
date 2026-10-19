# KẾ HOẠCH NỘI DUNG & THI CÔNG CHI TIẾT TOÁN 6 - TUẦN 07 - BUỔI 01
## CHỦ ĐỀ: ĐỀ ÔN TẬP KIỂM TRA GIỮA HỌC KỲ 1 (ĐỀ SỐ 01) - TỔNG HỢP SỐ HỌC & HÌNH PHẲNG THỰC TẾ
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)
### Áp dụng: Phiếu kiểm tra định kỳ 45 phút - Cấu trúc Tối ưu Mới (10 câu ngắn + 4 bài tự luận) - 4 mã đề: 101, 102, 103, 104

---

## 🎯 I. NGUYÊN TẮC THIẾT KẾ BỐ CỤC MỚI (TỐI ƯU HẾT CỠ)

1. **Bỏ phần Chủ đề, Thời gian:**
   - Dòng tiêu đề trên cùng chỉ là 1 bảng duy nhất 1 hàng: `Tên phiếu` và `Mã đề - Trang`.
   - Học sinh tự ghi tên lên lề trên cùng (top margin) của tờ giấy A4.
2. **Bỏ hoàn toàn bảng điền đáp án:** 
   - Dùng lệnh `\shortans` ở cuối mỗi câu hỏi (với `\SAOPTN{widthSA=3.2,heightSA=0.62}`).
   - Tự động sinh ô `KQ: [     ]` bo góc thẩm mỹ ở mép phải của câu hỏi.
3. **Bỏ phân chia "Phần I", "Phần II":**
   - Đánh số câu liền mạch từ **Câu 1 đến Câu 14**.
   - Bỏ các dòng tiêu đề rườm rà chiếm diện tích.
4. **10 câu trắc nghiệm trả lời ngắn (Câu 1 đến Câu 10):**
   - Quét toàn bộ kiến thức Giữa HK1: Tập hợp, Số La Mã, Lũy thừa, Thứ tự phép tính, Tính chất chia hết của một tổng, Dấu hiệu chia hết (2, 5, 3, 9), Số nguyên tố, Chu vi & Diện tích các hình phẳng.
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
* **Câu 13 (2,5 điểm):** Bài toán thực tế Chu vi & Diện tích lát gạch (2 ý $a, b$), mỗi ý $1{,}25$ điểm.
* **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết của tổng lũy thừa (1,0 điểm).
$$\implies \text{TỔNG ĐIỂM: } 2{,}5 + 2{,}0 + 2{,}0 + 2{,}5 + 1{,}0 = 10{,}0\text{ ĐIỂM}$$

---

### 2. Bố cục 2 trang A4
* **Mặt trước (Trang 1/2):**
  * Khung tiêu đề ngắn gọn (1 dòng).
  * Bảng Điểm số & Lời nhận xét: Chiều cao chuẩn `\rule{0pt}{1.8cm}`.
  * **Câu 1 đến Câu 10:** 10 câu trả lời ngắn kèm ô `\shortans`.
  * **Câu 11 (2,0 điểm):** Thực hiện phép tính ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[8]`** (8 dòng kẻ chấm mờ).
  * *(Vừa vặn 100% chạm sát mép dưới trang 1).*

* **Mặt sau (Trang 2/2):**
  * Khung tiêu đề rút gọn (1 dòng): `TOÁN 6 - TUẦN 07 - BUỔI 01 | Mã đề: <MÃ> - Trang 2/2`.
  * **Câu 12 (2,0 điểm):** Tìm số tự nhiên $x$ ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[5]`**.
  * **Câu 13 (2,5 điểm):** Bài toán thực tế hình học phẳng (2 ý $a, b$) đóng khung box kèm **`\dongke{11}`**.
  * **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết đóng khung box kèm **`\dongke{7}`**.
  * *(Vừa vặn 100% chạm sát mép dưới trang 2).*

---

## 🗺️ III. MA TRẬN NỘI DUNG CHI TIẾT 4 MÃ ĐỀ TƯƠNG ĐƯƠNG

### 1. CÂU 1 ĐẾN CÂU 10: TRẢ LỜI NGẮN (2,5 ĐIỂM - MỖI CÂU 0,25 ĐIỂM)

| Câu | Mức độ & Dạng kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Câu 1** | Số phần tử của tập hợp | Tập hợp $A = \{x \in \mathbb{N} \mid 12 \le x \le 45\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $34$** | Tập hợp $A = \{x \in \mathbb{N} \mid 15 \le x \le 58\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $44$** | Tập hợp $A = \{x \in \mathbb{N} \mid 18 \le x \le 62\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $45$** | Tập hợp $A = \{x \in \mathbb{N} \mid 14 \le x \le 69\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $56$** |
| **Câu 2** | Đọc chữ số La Mã | Số La Mã $\text{XXIV}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $24$** | Số La Mã $\text{XXVII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $27$** | Số La Mã $\text{XXIX}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $29$** | Số La Mã $\text{XXVI}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $26$** |
| **Câu 3** | Nhân chia cùng cơ số | Viết gọn tích $2^3 \cdot 2^5$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $2^8$** | Viết gọn tích $3^2 \cdot 3^4$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $3^6$** | Viết gọn tích $5^2 \cdot 5^3$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $5^5$** | Viết gọn tích $2^4 \cdot 2^3$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $2^7$** |
| **Câu 4** | Thứ tự thực hiện phép tính | Giá trị của biểu thức $30 - 2 \cdot 3^2$ bằng bao nhiêu?<br>$\to$ **KQ: $12$** | Giá trị của biểu thức $40 - 3 \cdot 2^3$ bằng bao nhiêu?<br>$\to$ **KQ: $16$** | Giá trị của biểu thức $50 - 4 \cdot 2^3$ bằng bao nhiêu?<br>$\to$ **KQ: $18$** | Giá trị của biểu thức $60 - 5 \cdot 2^3$ bằng bao nhiêu?<br>$\to$ **KQ: $20$** |
| **Câu 5** | Tính chất chia hết của tổng | Số dư của phép chia tổng $(45 + 120 + 23)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $3$** | Số dư của phép chia tổng $(35 + 150 + 24)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $4$** | Số dư của phép chia tổng $(65 + 140 + 32)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $2$** | Số dư của phép chia tổng $(75 + 160 + 41)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $1$** |
| **Câu 6** | Dấu hiệu chia hết cho 3 | Tìm chữ số $x$ lớn nhất để số $\overline{23x}$ chia hết cho $3$.<br>$\to$ **KQ: $7$** | Tìm chữ số $x$ lớn nhất để số $\overline{34x}$ chia hết cho $3$.<br>$\to$ **KQ: $8$** | Tìm chữ số $x$ lớn nhất để số $\overline{45x}$ chia hết cho $3$.<br>$\to$ **KQ: $9$** | Tìm chữ số $x$ lớn nhất để số $\overline{16x}$ chia hết cho $3$.<br>$\to$ **KQ: $8$** |
| **Câu 7** | Nhận biết số nguyên tố | Trong các số $11; 15; 21; 27$, số nguyên tố là số nào?<br>$\to$ **KQ: $11$** | Trong các số $13; 25; 33; 35$, số nguyên tố là số nào?<br>$\to$ **KQ: $13$** | Trong các số $17; 27; 39; 49$, số nguyên tố là số nào?<br>$\to$ **KQ: $17$** | Trong các số $19; 35; 45; 51$, số nguyên tố là số nào?<br>$\to$ **KQ: $19$** |
| **Câu 8** | Đặc điểm lục giác đều | Một hình lục giác đều có bao nhiêu đường chéo chính?<br>$\to$ **KQ: $3$** | Một hình lục giác đều có bao nhiêu cạnh bằng nhau?<br>$\to$ **KQ: $6$** | Một hình lục giác đều có bao nhiêu góc ở các đỉnh bằng nhau?<br>$\to$ **KQ: $6$** | Một hình thoi có bao nhiêu cặp cạnh đối diện song song?<br>$\to$ **KQ: $2$** |
| **Câu 9** | Chu vi hình chữ nhật | Một mảnh đất hình chữ nhật có dài $15\text{ m}$, rộng $8\text{ m}$. Chu vi là:<br>$\to$ **KQ: $46\text{ m}$** | Một mảnh đất hình chữ nhật có dài $16\text{ m}$, rộng $7\text{ m}$. Chu vi là:<br>$\to$ **KQ: $46\text{ m}$** | Một mảnh đất hình chữ nhật có dài $18\text{ m}$, rộng $6\text{ m}$. Chu vi là:<br>$\to$ **KQ: $48\text{ m}$** | Một mảnh đất hình chữ nhật có dài $20\text{ m}$, rộng $7\text{ m}$. Chu vi là:<br>$\to$ **KQ: $54\text{ m}$** |
| **Câu 10** | Diện tích hình thoi | Mảnh bìa hình thoi có hai đường chéo là $8\text{ cm}$ và $10\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $40\text{ cm}^2$** | Mảnh bìa hình thoi có hai đường chéo là $6\text{ cm}$ và $12\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $36\text{ cm}^2$** | Mảnh bìa hình thoi có hai đường chéo là $8\text{ cm}$ và $14\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $56\text{ cm}^2$** | Mảnh bìa hình thoi có hai đường chéo là $10\text{ cm}$ và $12\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $60\text{ cm}^2$** |

---

### 2. CÂU 11: THỰC HIỆN PHÉP TÍNH (2,0 ĐIỂM - MỖI Ý 0,5 ĐIỂM)

* **Ý a (Tính trực tiếp có lũy thừa):**
  * **Mã 101:** $145 - 2^3 \cdot 5 + 3^2 \cdot 4 = 145 - 40 + 36 = 141$.
  * **Mã 102:** $155 - 2^4 \cdot 3 + 4^2 \cdot 2 = 155 - 48 + 32 = 139$.
  * **Mã 103:** $165 - 3^3 \cdot 2 + 5^2 \cdot 3 = 165 - 54 + 75 = 186$.
  * **Mã 104:** $175 - 2^5 \cdot 2 + 3^3 \cdot 3 = 175 - 64 + 81 = 192$.
* **Ý b (Tính nhanh đặt thừa số chung tròn trăm):**
  * **Mã 101:** $48 \cdot 67 + 48 \cdot 33 - 800 = 48 \cdot 100 - 800 = 4000$.
  * **Mã 102:** $56 \cdot 72 + 56 \cdot 28 - 600 = 56 \cdot 100 - 600 = 5000$.
  * **Mã 103:** $64 \cdot 75 + 64 \cdot 25 - 400 = 64 \cdot 100 - 400 = 6000$.
  * **Mã 104:** $72 \cdot 81 + 72 \cdot 19 - 200 = 72 \cdot 100 - 200 = 7000$.
* **Ý c (Biểu thức ngoặc tròn và lũy thừa):**
  * **Mã 101:** $180 : [45 - (18 - 15)^2] = 180 : [45 - 9] = 180 : 36 = 5$.
  * **Mã 102:** $210 : [58 - (19 - 15)^2] = 210 : [58 - 16] = 210 : 42 = 5$.
  * **Mã 103:** $220 : [69 - (21 - 16)^2] = 220 : [69 - 25] = 220 : 44 = 5$.
  * **Mã 104:** $240 : [84 - (23 - 17)^2] = 240 : [84 - 36] = 240 : 48 = 5$.
* **Ý d (Biểu thức lồng 3 tầng ngoặc $\{ \ [ \ ( \ ) \ ] \ \}$):**
  * **Mã 101:** $250 : \{ 90 - [32 + (14 - 12)^3] \} = 250 : \{ 90 - [32 + 8] \} = 250 : 50 = 5$.
  * **Mã 102:** $300 : \{ 100 - [32 + (15 - 13)^3] \} = 300 : \{ 100 - [32 + 8] \} = 300 : 60 = 5$.
  * **Mã 103:** $350 : \{ 110 - [32 + (16 - 14)^3] \} = 350 : \{ 110 - [32 + 8] \} = 350 : 70 = 5$.
  * **Mã 104:** $400 : \{ 120 - [32 + (17 - 15)^3] \} = 400 : \{ 120 - [32 + 8] \} = 400 : 80 = 5$.

---

### 3. CÂU 12: TÌM SỐ TỰ NHIÊN $x$ (2,0 ĐIỂM - MỖI Ý 0,5 ĐIỂM)

* **Ý a (Chuyển vế cơ bản):**
  * **Mã 101:** $4 \cdot x + 15 = 47 \implies 4x = 32 \implies x = 8$.
  * **Mã 102:** $5 \cdot x + 18 = 53 \implies 5x = 35 \implies x = 7$.
  * **Mã 103:** $6 \cdot x + 14 = 56 \implies 6x = 42 \implies x = 7$.
  * **Mã 104:** $7 \cdot x + 16 = 65 \implies 7x = 49 \implies x = 7$.
* **Ý b (Phương trình chứa ngoặc):**
  * **Mã 101:** $85 - 3 \cdot (x + 4) = 40 \implies 3(x+4) = 45 \implies x+4 = 15 \implies x = 11$.
  * **Mã 102:** $95 - 4 \cdot (x + 3) = 47 \implies 4(x+3) = 48 \implies x+3 = 12 \implies x = 9$.
  * **Mã 103:** $90 - 5 \cdot (x + 2) = 45 \implies 5(x+2) = 45 \implies x+2 = 9 \implies x = 7$.
  * **Mã 104:** $100 - 6 \cdot (x + 1) = 52 \implies 6(x+1) = 48 \implies x+1 = 8 \implies x = 7$.
* **Ý c (Tìm số mũ lũy thừa):**
  * **Mã 101:** $3 \cdot 2^{x+1} - 12 = 36 \implies 3 \cdot 2^{x+1} = 48 \implies 2^{x+1} = 16 = 2^4 \implies x = 3$.
  * **Mã 102:** $2 \cdot 3^{x+1} - 15 = 39 \implies 2 \cdot 3^{x+1} = 54 \implies 3^{x+1} = 27 = 3^3 \implies x = 2$.
  * **Mã 103:** $4 \cdot 2^{x+2} - 18 = 46 \implies 4 \cdot 2^{x+2} = 64 \implies 2^{x+2} = 16 = 2^4 \implies x = 2$.
  * **Mã 104:** $5 \cdot 3^{x-1} + 15 = 60 \implies 5 \cdot 3^{x-1} = 45 \implies 3^{x-1} = 9 = 3^2 \implies x = 3$.
* **Ý d (Dạng tìm ƯCLN của hai số):**
  * **Mã 101:** Tìm số tự nhiên $x$ lớn nhất, biết $24 \ \vdots \ x$ và $36 \ \vdots \ x \implies x = \text{ƯCLN}(24, 36) = 12$.
  * **Mã 102:** Tìm số tự nhiên $x$ lớn nhất, biết $30 \ \vdots \ x$ và $45 \ \vdots \ x \implies x = \text{ƯCLN}(30, 45) = 15$.
  * **Mã 103:** Tìm số tự nhiên $x$ lớn nhất, biết $28 \ \vdots \ x$ và $42 \ \vdots \ x \implies x = \text{ƯCLN}(28, 42) = 14$.
  * **Mã 104:** Tìm số tự nhiên $x$ lớn nhất, biết $32 \ \vdots \ x$ và $48 \ \vdots \ x \implies x = \text{ƯCLN}(32, 48) = 16$.

---

### 4. CÂU 13: BÀI TOÁN THỰC TẾ HÌNH HỌC PHẲNG (2,5 ĐIỂM - MỖI Ý 1,25 ĐIỂM)

* **Bối cảnh:** Bác An có một mảnh sân hình chữ nhật dùng làm sân chơi và dự định lát gạch hình vuông.
* **Mã đề 101:** Mảnh sân dài $16\text{ m}$, rộng $10\text{ m}$. Gạch hình vuông cạnh $40\text{ cm}$, giá $25.000$ đ/viên.
  * $a)$ (1,25đ) Chu vi mảnh sân là: $(16 + 10) \times 2 = 52\text{ m}$. Diện tích mảnh sân là: $16 \times 10 = 160\text{ m}^2$.
  * $b)$ (1,25đ) Diện tích một viên gạch là: $40 \times 40 = 1600\text{ cm}^2 = 0{,}16\text{ m}^2$. Số viên gạch cần dùng là: $160 : 0{,}16 = 1000$ viên. Số tiền mua gạch là: $1000 \times 25.000 = 25.000.000$ đồng.
* **Mã đề 102:** Mảnh sân dài $18\text{ m}$, rộng $10\text{ m}$. Gạch hình vuông cạnh $50\text{ cm}$, giá $35.000$ đ/viên.
  * $a)$ Chu vi: $(18 + 10) \times 2 = 56\text{ m}$. Diện tích: $18 \times 10 = 180\text{ m}^2$.
  * $b)$ Diện tích 1 viên gạch: $0{,}25\text{ m}^2$. Số viên gạch: $180 : 0{,}25 = 720$ viên. Số tiền mua gạch: $720 \times 35.000 = 25.200.000$ đồng.
* **Mã đề 103:** Mảnh sân dài $20\text{ m}$, rộng $12\text{ m}$. Gạch hình vuông cạnh $40\text{ cm}$, giá $20.000$ đ/viên.
  * $a)$ Chu vi: $(20 + 12) \times 2 = 64\text{ m}$. Diện tích: $20 \times 12 = 240\text{ m}^2$.
  * $b)$ Diện tích 1 viên gạch: $0{,}16\text{ m}^2$. Số viên gạch: $240 : 0{,}16 = 1500$ viên. Số tiền mua gạch: $1500 \times 20.000 = 30.000.000$ đồng.
* **Mã đề 104:** Mảnh sân dài $25\text{ m}$, rộng $10\text{ m}$. Gạch hình vuông cạnh $50\text{ cm}$, giá $30.000$ đ/viên.
  * $a)$ Chu vi: $(25 + 10) \times 2 = 70\text{ m}$. Diện tích: $25 \times 10 = 250\text{ m}^2$.
  * $b)$ Diện tích 1 viên gạch: $0{,}25\text{ m}^2$. Số viên gạch: $250 : 0{,}25 = 1000$ viên. Số tiền mua gạch: $1000 \times 30.000 = 30.000.000$ đồng.

---

### 5. CÂU 14: BÀI TOÁN PHÂN LOẠI HỌC SINH GIỎI (1,0 ĐIỂM)

* **Mã đề 101:** Cho tổng $A = 1 + 3 + 3^2 + 3^3 + \dots + 3^{21}$. Chứng minh rằng $A$ chia hết cho $4$.
  * *Lời giải:* Tổng $A$ có $22$ số hạng, ta ghép thành $11$ nhóm, mỗi nhóm $2$ số hạng:
    $$A = (1 + 3) + 3^2(1 + 3) + 3^4(1 + 3) + \dots + 3^{20}(1 + 3) = 4 \cdot (1 + 3^2 + 3^4 + \dots + 3^{20})$$
    Vì $4 \ \vdots \ 4$ nên $A \ \vdots \ 4$.
* **Mã đề 102:** Cho tổng $B = 1 + 4 + 4^2 + 4^3 + \dots + 4^{21}$. Chứng minh rằng $B$ chia hết cho $5$.
  * *Lời giải:* $B = (1 + 4) + 4^2(1 + 4) + \dots + 4^{20}(1 + 4) = 5 \cdot (1 + 4^2 + \dots + 4^{20}) \ \vdots \ 5$.
* **Mã đề 103:** Cho tổng $C = 1 + 5 + 5^2 + 5^3 + \dots + 5^{21}$. Chứng minh rằng $C$ chia hết cho $6$.
  * *Lời giải:* $C = (1 + 5) + 5^2(1 + 5) + \dots + 5^{20}(1 + 5) = 6 \cdot (1 + 5^2 + \dots + 5^{20}) \ \vdots \ 6$.
* **Mã đề 104:** Cho tổng $D = 1 + 2 + 2^2 + 2^3 + \dots + 2^{21}$. Chứng minh rằng $D$ chia hết cho $3$.
  * *Lời giải:* $D = (1 + 2) + 2^2(1 + 2) + \dots + 2^{20}(1 + 2) = 3 \cdot (1 + 2^2 + \dots + 2^{20}) \ \vdots \ 3$.
