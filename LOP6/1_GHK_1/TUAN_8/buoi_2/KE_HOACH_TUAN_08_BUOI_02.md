# KẾ HOẠCH NỘI DUNG & THI CÔNG CHI TIẾT TOÁN 6 - TUẦN 08 - BUỔI 02
## CHỦ ĐỀ: ĐỀ THI THỬ GIỮA HỌC KỲ 1 TOÀN DIỆN (ĐỀ SỐ 04) - CHUẨN MA TRẬN PHÒNG GD&ĐT
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
   - Quét toàn bộ kiến thức Giữa HK1: Tập hợp $\mathbb{N}^*$, Số La Mã, Chia hai lũy thừa cùng cơ số, Thứ tự phép tính có lũy thừa, Dấu hiệu chia hết cho cả 2 và 5, Dấu hiệu chia hết cho 3, Phân tích ra thừa số nguyên tố, Đặc điểm hình bình hành, Chu vi hình chữ nhật, Diện tích hình bình hành.
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
* **Câu 13 (1,5 điểm):** Bài toán thực tế ứng dụng ƯCLN chia tổ / chia nhóm (2 ý $a, b$), mỗi ý $0{,}75$ điểm.
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
  * Khung tiêu đề rút gọn (1 dòng): `TOÁN 6 - TUẦN 08 - BUỔI 02 | Mã đề: <MÃ> - Trang 2/2`.
  * **Câu 12 (2,0 điểm):** Tìm số tự nhiên $x$ ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[5]`**.
  * **Câu 13 (1,5 điểm):** Bài toán thực tế chia tổ học sinh (2 ý $a, b$) đóng khung box kèm **`\dongke{10}`**.
  * **Câu 14 (1,0 điểm):** Bài toán nâng cao chia hết đóng khung box kèm **`\dongke{7}`**.
  * *(Vừa vặn 100% chạm sát mép dưới trang 2).*

---

## 🗺️ III. MA TRẬN NỘI DUNG CHI TIẾT 4 MÃ ĐỀ TƯƠNG ĐƯƠNG

### 1. CÂU 1 ĐẾN CÂU 10: TRẢ LỜI NGẮN (2,5 ĐIỂM - MỖI CÂU 0,25 ĐIỂM)

| Câu | Mức độ & Dạng kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Câu 1** | Số phần tử tập hợp $\mathbb{N}^*$ | Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 48\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $48$** | Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 56\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $56$** | Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 64\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $64$** | Tập hợp $B = \{x \in \mathbb{N}^* \mid x \le 75\}$ có bao nhiêu phần tử?<br>$\to$ **KQ: $75$** |
| **Câu 2** | Đọc chữ số La Mã | Số La Mã $\text{XXVI}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $26$** | Số La Mã $\text{XXIII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $23$** | Số La Mã $\text{XXV}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $25$** | Số La Mã $\text{XXII}$ có giá trị trong hệ thập phân là bao nhiêu?<br>$\to$ **KQ: $22$** |
| **Câu 3** | Chia hai lũy thừa cùng cơ số | Viết gọn kết quả của phép chia $5^8 : 5^3$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $5^5$** | Viết gọn kết quả của phép chia $6^9 : 6^4$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $6^5$** | Viết gọn kết quả của phép chia $7^7 : 7^2$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $7^5$** | Viết gọn kết quả của phép chia $8^8 : 8^3$ dưới dạng một lũy thừa.<br>$\to$ **KQ: $8^5$** |
| **Câu 4** | Thứ tự thực hiện phép tính | Giá trị của biểu thức $40 + 20 : 2^2$ bằng bao nhiêu?<br>$\to$ **KQ: $45$** | Giá trị của biểu thức $50 + 36 : 3^2$ bằng bao nhiêu?<br>$\to$ **KQ: $54$** | Giá trị của biểu thức $60 + 48 : 2^4$ bằng bao nhiêu?<br>$\to$ **KQ: $63$** | Giá trị của biểu thức $70 + 75 : 5^2$ bằng bao nhiêu?<br>$\to$ **KQ: $73$** |
| **Câu 5** | Dấu hiệu chia hết cho cả 2 và 5 | Chữ số tận cùng của một số tự nhiên chia hết cho cả $2$ và $5$ là chữ số nào?<br>$\to$ **KQ: $0$** | Số dư của một số có chữ số tận cùng bằng $3$ khi chia cho $5$ là bao nhiêu?<br>$\to$ **KQ: $3$** | Số dư của một số có chữ số tận cùng bằng $7$ khi chia cho $5$ là bao nhiêu?<br>$\to$ **KQ: $2$** | Số dư của một số có chữ số tận cùng bằng $8$ khi chia cho $5$ là bao nhiêu?<br>$\to$ **KQ: $3$** |
| **Câu 6** | Dấu hiệu chia hết cho 3 | Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{5x2}$ chia hết cho $3$.<br>$\to$ **KQ: $2$** | Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{4x5}$ chia hết cho $3$.<br>$\to$ **KQ: $3$** | Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{6x1}$ chia hết cho $3$.<br>$\to$ **KQ: $2$** | Tìm chữ số $x$ nhỏ nhất khác $0$ để số $\overline{7x3}$ chia hết cho $3$.<br>$\to$ **KQ: $2$** |
| **Câu 7** | Phân tích ra thừa số nguyên tố | Phân tích số $24$ ra thừa số nguyên tố có kết quả là gì?<br>$\to$ **KQ: $2^3 \cdot 3$** | Phân tích số $36$ ra thừa số nguyên tố có kết quả là gì?<br>$\to$ **KQ: $2^2 \cdot 3^2$** | Phân tích số $40$ ra thừa số nguyên tố có kết quả là gì?<br>$\to$ **KQ: $2^3 \cdot 5$** | Phân tích số $48$ ra thừa số nguyên tố có kết quả là gì?<br>$\to$ **KQ: $2^4 \cdot 3$** |
| **Câu 8** | Đặc điểm hình bình hành | Hai đường chéo của hình bình hành cắt nhau tại vị trí nào của mỗi đường?<br>$\to$ **KQ: Trung điểm** | Hai cạnh đối diện của hình bình hành có tính chất gì về phương và độ dài?<br>$\to$ **KQ: Song song và bằng nhau** | Hai góc đối diện của một hình bình hành có số đo như thế nào với nhau?<br>$\to$ **KQ: Bằng nhau** | Hai đường chéo của hình thoi có tính chất gì với nhau?<br>$\to$ **KQ: Vuông góc** |
| **Câu 9** | Chu vi hình chữ nhật | Một hình chữ nhật có chiều dài $14\text{ m}$, chiều rộng $6\text{ m}$. Chu vi là:<br>$\to$ **KQ: $40\text{ m}$** | Một hình chữ nhật có chiều dài $15\text{ m}$, chiều rộng $7\text{ m}$. Chu vi là:<br>$\to$ **KQ: $44\text{ m}$** | Một hình chữ nhật có chiều dài $16\text{ m}$, chiều rộng $8\text{ m}$. Chu vi là:<br>$\to$ **KQ: $48\text{ m}$** | Một hình chữ nhật có chiều dài $18\text{ m}$, chiều rộng $9\text{ m}$. Chu vi là:<br>$\to$ **KQ: $54\text{ m}$** |
| **Câu 10** | Diện tích hình bình hành | Một hình bình hành có độ dài đáy $15\text{ cm}$, chiều cao tương ứng $8\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $120\text{ cm}^2$** | Một hình bình hành có độ dài đáy $16\text{ cm}$, chiều cao tương ứng $7\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $112\text{ cm}^2$** | Một hình bình hành có độ dài đáy $18\text{ cm}$, chiều cao tương ứng $6\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $108\text{ cm}^2$** | Một hình bình hành có độ dài đáy $20\text{ cm}$, chiều cao tương ứng $8\text{ cm}$. Diện tích là:<br>$\to$ **KQ: $160\text{ cm}^2$** |

---

### 2. CÂU 11: THỰC HIỆN PHÉP TÍNH (3,0 ĐIỂM - 6 Ý, MỖI Ý 0,5 ĐIỂM)

* **Ý a (Tính trực tiếp có lũy thừa):**
  * **Mã 101:** $185 - 3^2 \cdot 6 + 2^4 \cdot 3 = 185 - 54 + 48 = 179$.
  * **Mã 102:** $195 - 4^2 \cdot 4 + 3^3 \cdot 2 = 195 - 64 + 54 = 185$.
  * **Mã 103:** $175 - 2^5 \cdot 3 + 5^2 \cdot 3 = 175 - 96 + 75 = 154$.
  * **Mã 104:** $165 - 3^3 \cdot 3 + 4^3 \cdot 1 = 165 - 81 + 64 = 148$.
* **Ý b (Tính nhanh nhóm tròn trăm):**
  * **Mã 101:** $125 + 74 + 175 + 26 = (125 + 175) + (74 + 26) = 300 + 100 = 400$.
  * **Mã 102:** $135 + 68 + 165 + 32 = (135 + 165) + (68 + 32) = 300 + 100 = 400$.
  * **Mã 103:** $145 + 57 + 155 + 43 = (145 + 155) + (57 + 43) = 300 + 100 = 400$.
  * **Mã 104:** $115 + 86 + 185 + 14 = (115 + 185) + (86 + 14) = 300 + 100 = 400$.
* **Ý c (Tính nhanh đặt thừa số chung):**
  * **Mã 101:** $37 \cdot 64 + 37 \cdot 36 + 300 = 37 \cdot (64 + 36) + 300 = 37 \cdot 100 + 300 = 4000$.
  * **Mã 102:** $43 \cdot 78 + 43 \cdot 22 + 700 = 43 \cdot (78 + 22) + 700 = 43 \cdot 100 + 700 = 5000$.
  * **Mã 103:** $52 \cdot 83 + 52 \cdot 17 + 800 = 52 \cdot (83 + 17) + 800 = 52 \cdot 100 + 800 = 6000$.
  * **Mã 104:** $61 \cdot 74 + 61 \cdot 26 + 900 = 61 \cdot (74 + 26) + 900 = 61 \cdot 100 + 900 = 7000$.
* **Ý d (Biểu thức ngoặc tròn và lũy thừa):**
  * **Mã 101:** $240 : (35 - 11) + 2^3 \cdot 5 = 240 : 24 + 8 \cdot 5 = 10 + 40 = 50$.
  * **Mã 102:** $260 : (38 - 12) + 3^2 \cdot 6 = 260 : 26 + 9 \cdot 6 = 10 + 54 = 64$.
  * **Mã 103:** $280 : (42 - 14) + 4^2 \cdot 3 = 280 : 28 + 16 \cdot 3 = 10 + 48 = 58$.
  * **Mã 104:** $300 : (45 - 15) + 5^2 \cdot 2 = 300 : 30 + 25 \cdot 2 = 10 + 50 = 60$.
* **Ý e (Biểu thức ngoặc vuông $[ ]$):**
  * **Mã 101:** $160 : [52 - (15 - 9)^2] = 160 : [52 - 36] = 160 : 16 = 10$.
  * **Mã 102:** $180 : [67 - (17 - 10)^2] = 180 : [67 - 49] = 180 : 18 = 10$.
  * **Mã 103:** $200 : [84 - (19 - 11)^2] = 200 : [84 - 64] = 200 : 20 = 10$.
  * **Mã 104:** $220 : [103 - (21 - 12)^2] = 220 : [103 - 81] = 220 : 22 = 10$.
* **Ý f (Biểu thức lồng 3 tầng ngoặc $\{ \ [ \ ( \ ) \ ] \ \}$):**
  * **Mã 101:** $500 : \{ 130 - [53 + (17 - 14)^3] \} = 500 : \{ 130 - [53 + 27] \} = 500 : 50 = 10$.
  * **Mã 102:** $600 : \{ 140 - [53 + (18 - 15)^3] \} = 600 : \{ 140 - 80 \} = 600 : 60 = 10$.
  * **Mã 103:** $700 : \{ 150 - [53 + (19 - 16)^3] \} = 700 : \{ 150 - 80 \} = 700 : 70 = 10$.
  * **Mã 104:** $800 : \{ 160 - [53 + (20 - 17)^3] \} = 800 : \{ 160 - 80 \} = 800 : 80 = 10$.

---

### 3. CÂU 12: TÌM SỐ TỰ NHIÊN $x$ (2,0 ĐIỂM - 4 Ý, MỖI Ý 0,5 ĐIỂM)

* **Ý a (Chuyển vế phép chia):**
  * **Mã 101:** $(x - 12) : 4 = 15 \implies x - 12 = 60 \implies x = 72$.
  * **Mã 102:** $(x - 15) : 5 = 14 \implies x - 15 = 70 \implies x = 85$.
  * **Mã 103:** $(x - 14) : 6 = 12 \implies x - 14 = 72 \implies x = 86$.
  * **Mã 104:** $(x - 16) : 7 = 11 \implies x - 16 = 77 \implies x = 93$.
* **Ý b (Phương trình chứa ngoặc vuông):**
  * **Mã 101:** $120 - [45 - (x - 3)] = 85 \implies 45 - (x-3) = 35 \implies x-3 = 10 \implies x = 13$.
  * **Mã 102:** $130 - [55 - (x - 4)] = 90 \implies 55 - (x-4) = 40 \implies x-4 = 15 \implies x = 19$.
  * **Mã 103:** $140 - [65 - (x - 5)] = 95 \implies 65 - (x-5) = 45 \implies x-5 = 20 \implies x = 25$.
  * **Mã 104:** $150 - [75 - (x - 6)] = 100 \implies 75 - (x-6) = 50 \implies x-6 = 25 \implies x = 31$.
* **Ý c (Dạng cơ số lũy thừa bậc 3):**
  * **Mã 101:** $(x - 2)^3 = 27 \implies x - 2 = 3 \implies x = 5$.
  * **Mã 102:** $(x - 3)^3 = 64 \implies x - 3 = 4 \implies x = 7$.
  * **Mã 103:** $(x - 1)^3 = 125 \implies x - 1 = 5 \implies x = 6$.
  * **Mã 104:** $(x - 4)^3 = 8 \implies x - 4 = 2 \implies x = 6$.
* **Ý d (Dạng tìm $x \in \text{BC}(a, b)$ có điều kiện):**
  * **Mã 101:** Tìm số tự nhiên $x$, biết $x \ \vdots \ 12$, $x \ \vdots \ 18$ và $50 < x < 100 \implies \text{BCNN}(12, 18) = 36 \implies x \in \{36, 72, 108, \dots\} \implies x = 72$.
  * **Mã 102:** Tìm số tự nhiên $x$, biết $x \ \vdots \ 15$, $x \ \vdots \ 20$ và $80 < x < 150 \implies \text{BCNN}(15, 20) = 60 \implies x \in \{60, 120, 180, \dots\} \implies x = 120$.
  * **Mã 103:** Tìm số tự nhiên $x$, biết $x \ \vdots \ 14$, $x \ \vdots \ 21$ và $60 < x < 100 \implies \text{BCNN}(14, 21) = 42 \implies x \in \{42, 84, 126, \dots\} \implies x = 84$.
  * **Mã 104:** Tìm số tự nhiên $x$, biết $x \ \vdots \ 16$, $x \ \vdots \ 24$ và $70 < x < 120 \implies \text{BCNN}(16, 24) = 48 \implies x \in \{48, 96, 144, \dots\} \implies x = 96$.

---

### 4. CÂU 13: BÀI TOÁN THỰC TẾ ỨNG DỤNG ƯCLN CHIA TỔ (1,5 ĐIỂM - 2 Ý, MỖI Ý 0,75 ĐIỂM)

* **Bối cảnh:** Một chi đội hoặc lớp học có số học sinh nam và học sinh nữ cần chia đều vào các tổ (hoặc nhóm học tập) sao cho số nam và số nữ ở mỗi tổ là như nhau.
* **Mã đề 101:** Chi đội có $24$ bạn nam và $36$ bạn nữ.
  * $a)$ (0,75đ) Cô giáo có thể chia được nhiều nhất bao nhiêu tổ?
    * Giải: Số tổ nhiều nhất có thể chia được là $\text{ƯCLN}(24, 36)$. Ta có $24 = 2^3 \cdot 3$, $36 = 2^2 \cdot 3^2 \implies \text{ƯCLN}(24, 36) = 2^2 \cdot 3 = 12$. Vậy cô giáo chia được nhiều nhất $12$ tổ.
  * $b)$ (0,75đ) Khi đó, mỗi tổ có bao nhiêu bạn nam và bao nhiêu bạn nữ?
    * Giải: Số nam ở mỗi tổ là $24 : 12 = 2$ (bạn). Số nữ ở mỗi tổ là $36 : 12 = 3$ (bạn).
* **Mã đề 102:** Chi đội có $28$ bạn nam và $42$ bạn nữ chia đều vào các tổ sao cho số tổ là nhiều nhất.
  * $a)$ (0,75đ) Số tổ nhiều nhất là $\text{ƯCLN}(28, 42) = 14$ tổ.
  * $b)$ (0,75đ) Mỗi tổ có $28 : 14 = 2$ bạn nam và $42 : 14 = 3$ bạn nữ.
* **Mã đề 103:** Chi đội có $32$ bạn nam và $48$ bạn nữ chia đều vào các nhóm học tập sao cho số nhóm là nhiều nhất.
  * $a)$ (0,75đ) Số nhóm nhiều nhất là $\text{ƯCLN}(32, 48) = 16$ nhóm.
  * $b)$ (0,75đ) Mỗi nhóm có $32 : 16 = 2$ bạn nam và $48 : 16 = 3$ bạn nữ.
* **Mã đề 104:** Chi đội có $30$ bạn nam và $45$ bạn nữ chia đều vào các tổ sao cho số tổ là nhiều nhất.
  * $a)$ (0,75đ) Số tổ nhiều nhất là $\text{ƯCLN}(30, 45) = 15$ tổ.
  * $b)$ (0,75đ) Mỗi tổ có $30 : 15 = 2$ bạn nam và $45 : 15 = 3$ bạn nữ.

---

### 5. CÂU 14: BÀI TOÁN PHÂN LOẠI HỌC SINH GIỎI (1,0 ĐIỂM)

* **Mã đề 101:** Cho biểu thức $A = 2 + 2^2 + 2^3 + \dots + 2^{60}$. Chứng minh rằng $A$ chia hết cho $7$.
  * *Lời giải:* Tổng $A$ có $60$ số hạng. Ghép thành $20$ nhóm, mỗi nhóm $3$ số hạng:
    $$A = (2 + 2^2 + 2^3) + 2^3(2 + 2^2 + 2^3) + \dots + 2^{57}(2 + 2^2 + 2^3)$$
    $$= 14 + 2^3 \cdot 14 + \dots + 2^{57} \cdot 14 = 14 \cdot (1 + 2^3 + \dots + 2^{57})$$
    Vì $14 \ \vdots \ 7$ nên $A \ \vdots \ 7$.
* **Mã đề 102:** Cho biểu thức $B = 3 + 3^2 + 3^3 + \dots + 3^{60}$. Chứng minh rằng $B$ chia hết cho $13$.
  * *Lời giải:* Tổng $B$ có $60$ số hạng. Ghép thành $20$ nhóm, mỗi nhóm $3$ số hạng:
    $$B = (3 + 3^2 + 3^3) + 3^3(3 + 3^2 + 3^3) + \dots + 3^{57}(3 + 3^2 + 3^3)$$
    $$= 39 + 3^3 \cdot 39 + \dots + 3^{57} \cdot 39 = 39 \cdot (1 + 3^3 + \dots + 3^{57})$$
    Vì $39 \ \vdots \ 13$ nên $B \ \vdots \ 13$.
* **Mã đề 103:** Cho biểu thức $C = 4 + 4^2 + 4^3 + \dots + 4^{60}$. Chứng minh rằng $C$ chia hết cho $21$.
  * *Lời giải:* Tổng $C$ có $60$ số hạng. Ghép thành $20$ nhóm, mỗi nhóm $3$ số hạng:
    $$C = (4 + 4^2 + 4^3) + 4^3(4 + 4^2 + 4^3) + \dots + 4^{57}(4 + 4^2 + 4^3)$$
    $$= 84 + 4^3 \cdot 84 + \dots + 4^{57} \cdot 84 = 84 \cdot (1 + 4^3 + \dots + 4^{57})$$
    Vì $84 \ \vdots \ 21$ nên $C \ \vdots \ 21$.
* **Mã đề 104:** Cho biểu thức $D = 5 + 5^2 + 5^3 + \dots + 5^{60}$. Chứng minh rằng $D$ chia hết cho $31$.
  * *Lời giải:* Tổng $D$ có $60$ số hạng. Ghép thành $20$ nhóm, mỗi nhóm $3$ số hạng:
    $$D = (5 + 5^2 + 5^3) + 5^3(5 + 5^2 + 5^3) + \dots + 5^{57}(5 + 5^2 + 5^3)$$
    $$= 155 + 5^3 \cdot 155 + \dots + 5^{57} \cdot 155 = 155 \cdot (1 + 5^3 + \dots + 5^{57})$$
    Vì $155 \ \vdots \ 31$ nên $D \ \vdots \ 31$.
