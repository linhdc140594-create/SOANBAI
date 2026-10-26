# KẾ HOẠCH NỘI DUNG & THI CÔNG CHI TIẾT TOÁN 6 - TUẦN 08 - BUỔI 01
## CHỦ ĐỀ: ĐỀ ÔN TẬP KIỂM TRA GIỮA HỌC KỲ 1 (ĐỀ SỐ 03) - TỔNG HỢP SỐ HỌC & HÌNH PHẲNG THỰC TẾ
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)
### Áp dụng: Phiếu kiểm tra định kỳ 45 phút - Cấu trúc Tối ưu Mới (10 câu ngắn + 4 bài tự luận) - 4 mã đề: 101, 102, 103, 104
### Yêu cầu đặc biệt: Câu 11 (Thực hiện phép tính) gồm 6 ý tương đương 3,0 điểm (0,5 điểm/ý)

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
4. **10 câu trắc nghiệm trả lời ngắn (Câu 1 đến Câu 10 - 2,5 điểm):**
   - Quét toàn bộ kiến thức Giữa HK1: Tập hợp & số phần tử, Số La Mã, Lũy thừa, Thứ tự phép tính, Tính chất chia hết của một tổng, Dấu hiệu chia hết cho 9, Số nguyên tố, Đặc điểm hình lục giác đều, Chu vi hình thoi, Diện tích hình thoi.
5. **ĐẶC BIỆT - Câu 11: 6 ý thực hiện phép tính (3,0 điểm):**
   - Thiết kế dạng bảng $3 \times 2$ (3 hàng $\times$ 2 cột).
   - Mỗi ô dùng **`\oBaiTap[5]`** (5 dòng kẻ chấm mờ), vừa vặn chạm sát mép dưới Trang 1.
6. **Bảo toàn quy chuẩn in ấn (Layout Gold Standard):**
   - Đúng **2 trang A4 / mã đề** (Trang 1: Mặt trước; Trang 2: Mặt sau).
   - Đóng gói trọn vẹn **4 mã đề (101, 102, 103, 104)** trong 1 file `.tex` $\rightarrow$ Biên dịch ra **chính xác 8 trang PDF**.
   - Dòng kẻ chấm mờ (`\oBaiTap` và `\dongke`) được tính toán chuẩn xác để chạm sát lề đáy giấy cả 2 mặt.

---

## 📐 II. MA TRẬN THANG ĐIỂM & BỐ CỤC TRANG IN (TỔNG 10 ĐIỂM)

### 1. Phân bổ điểm chi tiết
* **Câu 1 $\to$ Câu 10 (2,5 điểm):** 10 câu trả lời ngắn (`\shortans`), mỗi câu $0{,}25$ điểm.
* **Câu 11 (3,0 điểm):** Thực hiện phép tính (6 ý $a, b, c, d, e, f$), mỗi ý $0{,}5$ điểm.
* **Câu 12 (2,0 điểm):** Tìm số tự nhiên $x$ (4 ý $a, b, c, d$), mỗi ý $0{,}5$ điểm.
* **Câu 13 (1,5 điểm):** Bài toán thực tế Chu vi & Diện tích khu vườn (2 ý $a, b$), mỗi ý $0{,}75$ điểm.
* **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết của tổng dãy lũy thừa (1,0 điểm).
$$\implies \text{TỔNG ĐIỂM: } 2{,}5 + 3{,}0 + 2{,}0 + 1{,}5 + 1{,}0 = 10{,}0\text{ ĐIỂM}$$

---

### 2. Bố cục 2 trang A4
* **Mặt trước (Trang 1/2):**
  * Khung tiêu đề ngắn gọn (1 dòng).
  * Bảng Điểm số & Lời nhận xét: Chiều cao chuẩn `\rule{0pt}{1.8cm}`.
  * **Câu 1 đến Câu 10:** 10 câu trả lời ngắn kèm ô `\shortans`.
  * **Câu 11 (3,0 điểm):** Thực hiện phép tính ($a, b, c, d, e, f$) xếp dạng bảng $3 \times 2$, mỗi ô dùng **`\oBaiTap[5]`** (5 dòng kẻ chấm mờ).
  * *(Vừa vặn 100% chạm sát mép dưới trang 1).*

* **Mặt sau (Trang 2/2):**
  * Khung tiêu đề rút gọn (1 dòng): `TOÁN 6 - TUẦN 08 - BUỔI 01 | Mã đề: <MÃ> - Trang 2/2`.
  * **Câu 12 (2,0 điểm):** Tìm số tự nhiên $x$ ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[5]`**.
  * **Câu 13 (1,5 điểm):** Bài toán thực tế hình học phẳng (2 ý $a, b$) đóng khung box kèm **`\dongke{10}`**.
  * **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết đóng khung box kèm **`\dongke{7}`**.
  * *(Vừa vặn 100% chạm sát mép dưới trang 2).*

---

## 🗺️ III. MA TRẬN NỘI DUNG CHI TIẾT 4 MÃ ĐỀ TƯƠNG ĐƯƠNG

### 1. CÂU 1 ĐẾN CÂU 10: TRẢ LỜI NGẮN (2,5 ĐIỂM - MỖI CÂU 0,25 ĐIỂM)

| Câu | Mức độ & Dạng kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Câu 1** | Số phần tử của tập hợp | Tập hợp $A = \{x \in \mathbb{N} \mid 10 \le x \le 45\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $36$** | Tập hợp $A = \{x \in \mathbb{N} \mid 12 \le x \le 55\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $44$** | Tập hợp $A = \{x \in \mathbb{N} \mid 15 \le x \le 63\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $49$** | Tập hợp $A = \{x \in \mathbb{N} \mid 18 \le x \le 72\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $55$** |
| **Câu 2** | Đọc chữ số La Mã | Số La Mã $\text{XXVIII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $28$** | Số La Mã $\text{XXIV}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $24$** | Số La Mã $\text{XXIX}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $29$** | Số La Mã $\text{XXVII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $27$** |
| **Câu 3** | Nhân hai lũy thừa cùng cơ số | Viết gọn tích $3^4 \cdot 3^3$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $3^7$** | Viết gọn tích $2^5 \cdot 2^4$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $2^9$** | Viết gọn tích $5^3 \cdot 5^4$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $5^7$** | Viết gọn tích $7^2 \cdot 7^5$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $7^7$** |
| **Câu 4** | Thứ tự thực hiện phép tính | Giá trị của biểu thức $50 - 3 \cdot 2^3$ bằng bao nhiêu?<br>$\to$ **KQ: $26$** | Giá trị của biểu thức $60 - 4 \cdot 3^2$ bằng bao nhiêu?<br>$\to$ **KQ: $24$** | Giá trị của biểu thức $70 - 2 \cdot 4^2$ bằng bao nhiêu?<br>$\to$ **KQ: $38$** | Giá trị của biểu thức $80 - 5 \cdot 2^3$ bằng bao nhiêu?<br>$\to$ **KQ: $40$** |
| **Câu 5** | Tính chất chia hết của tổng | Số dư của phép chia tổng $(35 + 120 + 43)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $3$** | Số dư của phép chia tổng $(45 + 130 + 54)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $4$** | Số dư của phép chia tổng $(55 + 140 + 62)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $2$** | Số dư của phép chia tổng $(65 + 150 + 71)$ cho $5$ là bao nhiêu?<br>$\to$ **KQ: $1$** |
| **Câu 6** | Dấu hiệu chia hết cho 9 | Tìm chữ số $x$ để số $\overline{45x}$ chia hết cho $9$ ($x > 0$).<br>$\to$ **KQ: $9$** | Tìm chữ số $x$ lớn nhất để số $\overline{32x}$ chia hết cho $3$.<br>$\to$ **KQ: $7$** | Tìm chữ số $x$ lớn nhất để số $\overline{51x}$ chia hết cho $3$.<br>$\to$ **KQ: $9$** | Tìm chữ số $x$ để số $\overline{63x}$ chia hết cho $9$ ($x > 0$).<br>$\to$ **KQ: $9$** |
| **Câu 7** | Nhận biết số nguyên tố | Trong các số $13; 21; 27; 35$, số nguyên tố là số nào?<br>$\to$ **KQ: $13$** | Trong các số $17; 25; 33; 49$, số nguyên tố là số nào?<br>$\to$ **KQ: $17$** | Trong các số $19; 39; 51; 57$, số nguyên tố là số nào?<br>$\to$ **KQ: $19$** | Trong các số $23; 35; 45; 63$, số nguyên tố là số nào?<br>$\to$ **KQ: $23$** |
| **Câu 8** | Đặc điểm lục giác đều | Một hình lục giác đều có bao nhiêu đường chéo chính?<br>$\to$ **KQ: $3$** | Một hình lục giác đều có bao nhiêu cạnh bằng nhau?<br>$\to$ **KQ: $6$** | Một hình lục giác đều có bao nhiêu góc ở các đỉnh bằng nhau?<br>$\to$ **KQ: $6$** | Một hình vuông có bao nhiêu trục đối xứng?<br>$\to$ **KQ: $4$** |
| **Câu 9** | Chu vi hình thoi | Một mảnh đất hình thoi có độ dài cạnh là $12\text{ m}$. Chu vi là:<br>$\to$ **KQ: $48\text{ m}$** | Một mảnh đất hình thoi có độ dài cạnh là $15\text{ m}$. Chu vi là:<br>$\to$ **KQ: $60\text{ m}$** | Một mảnh đất hình thoi có độ dài cạnh là $14\text{ m}$. Chu vi là:<br>$\to$ **KQ: $56\text{ m}$** | Một mảnh đất hình thoi có độ dài cạnh là $16\text{ m}$. Chu vi là:<br>$\to$ **KQ: $64\text{ m}$** |
| **Câu 10** | Diện tích hình thoi | Mảnh bìa hình thoi có hai đường chéo là $10\text{ cm}$ và $14\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $70\text{ cm}^2$** | Mảnh bìa hình thoi có hai đường chéo là $12\text{ cm}$ và $15\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $90\text{ cm}^2$** | Mảnh bìa hình thoi có hai đường chéo là $8\text{ cm}$ và $16\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $64\text{ cm}^2$** | Mảnh bìa hình thoi có hai đường chéo là $14\text{ cm}$ và $18\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $126\text{ cm}^2$** |

---

### 2. CÂU 11: THỰC HIỆN PHÉP TÍNH (3,0 ĐIỂM - 6 Ý, MỖI Ý 0,5 ĐIỂM)

* **Ý a (Tính trực tiếp có lũy thừa):**
  * **Mã 101:** $145 - 2^3 \cdot 5 + 3^2 \cdot 4 = 145 - 40 + 36 = 141$.
  * **Mã 102:** $155 - 2^4 \cdot 3 + 4^2 \cdot 2 = 155 - 48 + 32 = 139$.
  * **Mã 103:** $165 - 3^3 \cdot 2 + 5^2 \cdot 3 = 165 - 54 + 75 = 186$.
  * **Mã 104:** $175 - 2^5 \cdot 2 + 3^3 \cdot 3 = 175 - 64 + 81 = 192$.
* **Ý b (Tính nhanh nhóm tròn trăm):**
  * **Mã 101:** $38 + 147 + 62 + 53 = (38 + 62) + (147 + 53) = 100 + 200 = 300$.
  * **Mã 102:** $46 + 138 + 54 + 62 = (46 + 54) + (138 + 62) = 100 + 200 = 300$.
  * **Mã 103:** $29 + 154 + 71 + 46 = (29 + 71) + (154 + 46) = 100 + 200 = 300$.
  * **Mã 104:** $37 + 165 + 63 + 35 = (37 + 63) + (165 + 35) = 100 + 200 = 300$.
* **Ý c (Tính nhanh đặt thừa số chung):**
  * **Mã 101:** $48 \cdot 67 + 48 \cdot 33 - 800 = 48 \cdot (67 + 33) - 800 = 48 \cdot 100 - 800 = 4000$.
  * **Mã 102:** $56 \cdot 72 + 56 \cdot 28 - 600 = 56 \cdot (72 + 28) - 600 = 56 \cdot 100 - 600 = 5000$.
  * **Mã 103:** $64 \cdot 75 + 64 \cdot 25 - 400 = 64 \cdot (75 + 25) - 400 = 64 \cdot 100 - 400 = 6000$.
  * **Mã 104:** $72 \cdot 81 + 72 \cdot 19 - 200 = 72 \cdot (81 + 19) - 200 = 72 \cdot 100 - 200 = 7000$.
* **Ý d (Biểu thức ngoặc tròn và lũy thừa):**
  * **Mã 101:** $180 : (25 - 7) + 3^2 \cdot 5 = 180 : 18 + 9 \cdot 5 = 10 + 45 = 55$.
  * **Mã 102:** $160 : (24 - 8) + 4^2 \cdot 3 = 160 : 16 + 16 \cdot 3 = 10 + 48 = 58$.
  * **Mã 103:** $210 : (27 - 6) + 5^2 \cdot 2 = 210 : 21 + 25 \cdot 2 = 10 + 50 = 60$.
  * **Mã 104:** $240 : (29 - 5) + 6^2 \cdot 2 = 240 : 24 + 36 \cdot 2 = 10 + 72 = 82$.
* **Ý e (Biểu thức ngoặc vuông $[ ]$):**
  * **Mã 101:** $180 : [45 - (18 - 15)^2] = 180 : [45 - 9] = 180 : 36 = 5$.
  * **Mã 102:** $210 : [58 - (19 - 15)^2] = 210 : [58 - 16] = 210 : 42 = 5$.
  * **Mã 103:** $220 : [69 - (21 - 16)^2] = 220 : [69 - 25] = 220 : 44 = 5$.
  * **Mã 104:** $240 : [84 - (23 - 17)^2] = 240 : [84 - 36] = 240 : 48 = 5$.
* **Ý f (Biểu thức lồng 3 tầng ngoặc $\{ \ [ \ ( \ ) \ ] \ \}$):**
  * **Mã 101:** $250 : \{ 90 - [32 + (14 - 12)^3] \} = 250 : \{ 90 - [32 + 8] \} = 250 : 50 = 5$.
  * **Mã 102:** $300 : \{ 100 - [32 + (15 - 13)^3] \} = 300 : \{ 100 - [32 + 8] \} = 300 : 60 = 5$.
  * **Mã 103:** $350 : \{ 110 - [32 + (16 - 14)^3] \} = 350 : \{ 110 - [32 + 8] \} = 350 : 70 = 5$.
  * **Mã 104:** $400 : \{ 120 - [32 + (17 - 15)^3] \} = 400 : \{ 120 - [32 + 8] \} = 400 : 80 = 5$.

---

### 3. CÂU 12: TÌM SỐ TỰ NHIÊN $x$ (2,0 ĐIỂM - 4 Ý, MỖI Ý 0,5 ĐIỂM)

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

### 4. CÂU 13: BÀI TOÁN THỰC TẾ HÌNH HỌC PHẲNG (1,5 ĐIỂM - 2 Ý, MỖI Ý 0,75 ĐIỂM)

* **Bối cảnh:** Bác Ba có một mảnh vườn trồng rau hình chữ nhật. Bác dự định làm hàng rào lưới thép bao quanh khu vườn (chừa lại cổng ra vào rộng $2\text{ m}$).
* **Mã đề 101:** Chiều dài $15\text{ m}$, chiều rộng $8\text{ m}$, chi phí làm hàng rào $120.000$ đồng/mét.
  * $a)$ (0,75đ) Chu vi mảnh vườn: $(15 + 8) \times 2 = 46\text{ m}$. Diện tích mảnh vườn: $15 \times 8 = 120\text{ m}^2$.
  * $b)$ (0,75đ) Chiều dài hàng rào lưới thép: $46 - 2 = 44\text{ m}$. Bác Ba phải trả số tiền làm hàng rào là: $44 \times 120.000 = 5.280.000$ đồng.
* **Mã đề 102:** Chiều dài $16\text{ m}$, chiều rộng $9\text{ m}$, chi phí làm hàng rào $150.000$ đồng/mét.
  * $a)$ (0,75đ) Chu vi mảnh vườn: $(16 + 9) \times 2 = 50\text{ m}$. Diện tích mảnh vườn: $16 \times 9 = 144\text{ m}^2$.
  * $b)$ (0,75đ) Chiều dài hàng rào lưới thép: $50 - 2 = 48\text{ m}$. Bác Ba phải trả số tiền làm hàng rào là: $48 \times 150.000 = 7.200.000$ đồng.
* **Mã đề 103:** Chiều dài $18\text{ m}$, chiều rộng $10\text{ m}$, chi phí làm hàng rào $140.000$ đồng/mét.
  * $a)$ (0,75đ) Chu vi mảnh vườn: $(18 + 10) \times 2 = 56\text{ m}$. Diện tích mảnh vườn: $18 \times 10 = 180\text{ m}^2$.
  * $b)$ (0,75đ) Chiều dài hàng rào lưới thép: $56 - 2 = 54\text{ m}$. Bác Ba phải trả số tiền làm hàng rào là: $54 \times 140.000 = 7.560.000$ đồng.
* **Mã đề 104:** Chiều dài $20\text{ m}$, chiều rộng $11\text{ m}$, chi phí làm hàng rào $130.000$ đồng/mét.
  * $a)$ (0,75đ) Chu vi mảnh vườn: $(20 + 11) \times 2 = 62\text{ m}$. Diện tích mảnh vườn: $20 \times 11 = 220\text{ m}^2$.
  * $b)$ (0,75đ) Chiều dài hàng rào lưới thép: $62 - 2 = 60\text{ m}$. Bác Ba phải trả số tiền làm hàng rào là: $60 \times 130.000 = 7.800.000$ đồng.

---

### 5. CÂU 14: BÀI TOÁN PHÂN LOẠI HỌC SINH GIỎI (1,0 ĐIỂM)

* **Mã đề 101:** Cho tổng $A = 1 + 3 + 3^2 + 3^3 + \dots + 3^{21}$. Chứng minh rằng $A$ chia hết cho $4$.
  * *Lời giải:* Tổng $A$ có $22$ số hạng, ta ghép thành $11$ nhóm, mỗi nhóm $2$ số hạng:
    $$A = (1 + 3) + 3^2(1 + 3) + 3^4(1 + 3) + \dots + 3^{20}(1 + 3) = 4 \cdot (1 + 3^2 + 3^4 + \dots + 3^{20})$$
    Vì $4 \ \vdots \ 4$ nên $A \ \vdots \ 4$.
* **Mã đề 102:** Cho tổng $B = 1 + 4 + 4^2 + 4^3 + \dots + 4^{21}$. Chứng minh rằng $B$ chia hết cho $5$.
  * *Lời giải:* Tổng $B$ có $22$ số hạng, ghép thành $11$ nhóm:
    $$B = (1 + 4) + 4^2(1 + 4) + \dots + 4^{20}(1 + 4) = 5 \cdot (1 + 4^2 + \dots + 4^{20}) \ \vdots \ 5$$
* **Mã đề 103:** Cho tổng $C = 1 + 5 + 5^2 + 5^3 + \dots + 5^{21}$. Chứng minh rằng $C$ chia hết cho $6$.
  * *Lời giải:* Tổng $C$ có $22$ số hạng, ghép thành $11$ nhóm:
    $$C = (1 + 5) + 5^2(1 + 5) + \dots + 5^{20}(1 + 5) = 6 \cdot (1 + 5^2 + \dots + 5^{20}) \ \vdots \ 6$$
* **Mã đề 104:** Cho tổng $D = 1 + 2 + 2^2 + 2^3 + \dots + 2^{23}$. Chứng minh rằng $D$ chia hết cho $3$.
  * *Lời giải:* Tổng $D$ có $24$ số hạng, ghép thành $12$ nhóm:
    $$D = (1 + 2) + 2^2(1 + 2) + \dots + 2^{22}(1 + 2) = 3 \cdot (1 + 2^2 + \dots + 2^{22}) \ \vdots \ 3$$
