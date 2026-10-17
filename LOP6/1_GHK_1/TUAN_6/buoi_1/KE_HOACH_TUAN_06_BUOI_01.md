# KẾ HOẠCH NỘI DUNG & THI CÔNG CHI TIẾT TOÁN 6 - TUẦN 06 - BUỔI 01
## CHỦ ĐỀ: BÀI 20 - CHU VI VÀ DIỆN TÍCH CÁC TỨ GIÁC ĐÃ HỌC
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)
### Áp dụng: Phiếu kiểm tra định kỳ 45 phút - Cấu trúc Tối ưu Mới (10 câu ngắn + 4 bài tự luận) - 4 mã đề: 101, 102, 103, 104

---

## 🎯 I. NGUYÊN TẮC THIẾT KẾ BỐ CỤC MỚI (TỐI ƯU HẾT CỠ)

1. **Bỏ phần Chủ đề, Thời gian:**
   - Dòng tiêu đề trên cùng chỉ là 1 bảng duy nhất 1 hàng: `Tên phiếu` và `Mã đề - Trang`.
   - Học sinh tự ghi tên lên lề trên cùng (top margin) của tờ giấy A4.
2. **Bỏ hoàn toàn bảng điền đáp án:** 
   - Dùng lệnh `\shortans` (hoặc `\SA`) ở cuối mỗi câu hỏi.
   - Tự động sinh ô `KQ: [     ]` bo góc thẩm mỹ ở mép phải của câu hỏi.
3. **Bỏ phân chia "Phần I", "Phần II":**
   - Đánh số câu liền mạch từ **Câu 1 đến Câu 14**.
   - Bỏ các dòng tiêu đề rườm rà chiếm diện tích.
4. **Tăng lên 10 câu trả lời ngắn:**
   - Đánh giá nhanh nhận biết và thông hiểu toàn diện các kiến thức hình học tứ giác và số học bổ trợ.
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
* **Câu 13 (2,5 điểm):** Bài toán thực tế Chu vi & Diện tích (2 ý $a, b$), mỗi ý $1{,}25$ điểm.
* **Câu 14 (1,0 điểm):** Bài toán nâng cao dãy tổng lũy thừa (1,0 điểm).
$$\implies \text{TỔNG ĐIỂM: } 2{,}5 + 2{,}0 + 2{,}0 + 2{,}5 + 1{,}0 = 10{,}0\text{ ĐIỂM}$$

---

### 2. Bố cục 2 trang A4
* **Mặt trước (Trang 1/2):**
  * Khung tiêu đề ngắn gọn (1 dòng).
  * Bảng Điểm số & Lời nhận xét: Chiều cao chuẩn `\rule{0pt}{1.8cm}`.
  * **Câu 1 đến Câu 10:** 10 dòng câu trả lời ngắn kèm ô `\shortans`.
  * **Câu 11 (2,0 điểm):** Thực hiện phép tính ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[8]`** (8 dòng kẻ chấm mờ).
  * *(Vừa vặn 100% chạm sát mép dưới trang 1).*

* **Mặt sau (Trang 2/2):**
  * Khung tiêu đề rút gọn (1 dòng): `TOÁN 6 - TUẦN 06 - BUỔI 01 | MÃ ĐỀ: <MÃ> - TRANG 2/2`.
  * **Câu 12 (2,0 điểm):** Tìm $x$ ($a, b, c, d$) xếp dạng bảng $2 \times 2$, mỗi ô dùng **`\oBaiTap[6]`**.
  * **Câu 13 (2,5 điểm):** Bài toán thực tế (2 ý $a, b$) kèm **`\dongke{9}`**.
  * **Câu 14 (1,0 điểm):** Bài toán nâng cao dãy tổng lũy thừa kèm **`\dongke{6}`**.
  * *(Vừa vặn 100% chạm sát mép dưới trang 2).*

---

## 🗺️ III. MA TRẬN NỘI DUNG CHI TIẾT 4 MÃ ĐỀ TƯƠNG ĐƯƠNG

### 1. CÂU 1 ĐẾN CÂU 10: TRẢ LỜI NGẮN (2,5 ĐIỂM - MỖI CÂU 0,25 ĐIỂM)

| Câu | Mức độ & Dạng kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Câu 1** | Chu vi hình vuông | Cạnh $a = 9\text{ cm}$. Chu vi?<br>$\to$ **KQ: $36\text{ cm}$** | Cạnh $a = 8\text{ cm}$. Chu vi?<br>$\to$ **KQ: $32\text{ cm}$** | Cạnh $a = 7\text{ cm}$. Chu vi?<br>$\to$ **KQ: $28\text{ cm}$** | Cạnh $a = 11\text{ cm}$. Chu vi?<br>$\to$ **KQ: $44\text{ cm}$** |
| **Câu 2** | Diện tích HCN | Dài $12\text{ m}$, rộng $5\text{ m}$.<br>$\to$ **KQ: $60\text{ m}^2$** | Dài $15\text{ m}$, rộng $4\text{ m}$.<br>$\to$ **KQ: $60\text{ m}^2$** | Dài $14\text{ m}$, rộng $5\text{ m}$.<br>$\to$ **KQ: $70\text{ m}^2$** | Dài $16\text{ m}$, rộng $5\text{ m}$.<br>$\to$ **KQ: $80\text{ m}^2$** |
| **Câu 3** | Diện tích hình thoi | Hai đường chéo $8\text{ cm}$ và $10\text{ cm}$.<br>$\to$ **KQ: $40\text{ cm}^2$** | Hai đường chéo $6\text{ cm}$ và $12\text{ cm}$.<br>$\to$ **KQ: $36\text{ cm}^2$** | Hai đường chéo $8\text{ cm}$ và $14\text{ cm}$.<br>$\to$ **KQ: $56\text{ cm}^2$** | Hai đường chéo $10\text{ cm}$ và $12\text{ cm}$.<br>$\to$ **KQ: $60\text{ cm}^2$** |
| **Câu 4** | Diện tích HBH | Đáy $12\text{ cm}$, chiều cao $6\text{ cm}$.<br>$\to$ **KQ: $72\text{ cm}^2$** | Đáy $15\text{ cm}$, chiều cao $4\text{ cm}$.<br>$\to$ **KQ: $60\text{ cm}^2$** | Đáy $14\text{ cm}$, chiều cao $5\text{ cm}$.<br>$\to$ **KQ: $70\text{ cm}^2$** | Đáy $18\text{ cm}$, chiều cao $5\text{ cm}$.<br>$\to$ **KQ: $90\text{ cm}^2$** |
| **Câu 5** | Tính giá trị lũy thừa | $2^4 \cdot 5 - 3^2 \cdot 4$<br>$\to$ **KQ: $44$** | $3^3 \cdot 2 - 2^4 \cdot 3$<br>$\to$ **KQ: $6$** | $2^5 \cdot 3 - 5^2 \cdot 2$<br>$\to$ **KQ: $46$** | $3^2 \cdot 10 - 2^3 \cdot 5$<br>$\to$ **KQ: $50$** |
| **Câu 6** | Bài toán ngược hình vuông | Hình vuông có $S = 64\text{ cm}^2$. Cạnh?<br>$\to$ **KQ: $8\text{ cm}$** | Hình vuông có $S = 81\text{ cm}^2$. Cạnh?<br>$\to$ **KQ: $9\text{ cm}$** | Hình vuông có $S = 49\text{ cm}^2$. Cạnh?<br>$\to$ **KQ: $7\text{ cm}$** | Hình vuông có $S = 100\text{ cm}^2$. Cạnh?<br>$\to$ **KQ: $10\text{ cm}$** |
| **Câu 7** | Chu vi hình chữ nhật | Dài $15\text{ cm}$, rộng $8\text{ cm}$. Chu vi?<br>$\to$ **KQ: $46\text{ cm}$** | Dài $16\text{ cm}$, rộng $7\text{ cm}$. Chu vi?<br>$\to$ **KQ: $46\text{ cm}$** | Dài $18\text{ cm}$, rộng $6\text{ cm}$. Chu vi?<br>$\to$ **KQ: $48\text{ cm}$** | Dài $20\text{ cm}$, rộng $6\text{ cm}$. Chu vi?<br>$\to$ **KQ: $52\text{ cm}$** |
| **Câu 8** | Cạnh hình thoi từ chu vi | Chu vi $36\text{ cm}$. Độ dài cạnh?<br>$\to$ **KQ: $9\text{ cm}$** | Chu vi $48\text{ cm}$. Độ dài cạnh?<br>$\to$ **KQ: $12\text{ cm}$** | Chu vi $44\text{ cm}$. Độ dài cạnh?<br>$\to$ **KQ: $11\text{ cm}$** | Chu vi $56\text{ cm}$. Độ dài cạnh?<br>$\to$ **KQ: $14\text{ cm}$** |
| **Câu 9** | Chiều cao HBH từ diện tích | $S = 48\text{ cm}^2$, đáy $8\text{ cm}$. Chiều cao?<br>$\to$ **KQ: $6\text{ cm}$** | $S = 54\text{ cm}^2$, đáy $9\text{ cm}$. Chiều cao?<br>$\to$ **KQ: $6\text{ cm}$** | $S = 63\text{ cm}^2$, đáy $7\text{ cm}$. Chiều cao?<br>$\to$ **KQ: $9\text{ cm}$** | $S = 72\text{ cm}^2$, đáy $8\text{ cm}$. Chiều cao?<br>$\to$ **KQ: $9\text{ cm}$** |
| **Câu 10** | Lũy thừa kết hợp | $5 \cdot 2^3 - 3^3$<br>$\to$ **KQ: $13$** | $4 \cdot 3^2 - 2^4$<br>$\to$ **KQ: $20$** | $6 \cdot 2^3 - 4^2$<br>$\to$ **KQ: $32$** | $7 \cdot 2^3 - 5^2$<br>$\to$ **KQ: $31$** |

---

### 2. CÂU 11: THỰC HIỆN PHÉP TÍNH (2,0 ĐIỂM - MỖI Ý 0,5 ĐIỂM)

* **Ý a:** Tính trực tiếp lũy thừa + nhân chia ($135 - 3^2 \cdot 10 + 2^3 \cdot 5 = 85$).
* **Ý b:** Tính nhanh thừa số chung tròn trăm ($47 \cdot 68 + 47 \cdot 32 - 700 = 4000$).
* **Ý c:** Biểu thức ngoặc vuông $[ \ ]$ và lũy thừa ($160 : [65 - (18 - 11)^2] = 10$).
* **Ý d:** Biểu thức ngoặc lồng $\{ \ [ \ ( \ ) \ ] \ \}$ ($200 : \{ 80 - [22 + (9 - 7)^3] \} = 4$).

---

### 3. CÂU 12: TÌM SỐ TỰ NHIÊN $x$ (2,0 ĐIỂM - MỖI Ý 0,5 ĐIỂM)

* **Ý a:** Bậc nhất có ngoặc: $45 + 5 \cdot (x - 3) = 75 \implies x = 9$.
* **Ý b:** Trừ ngoặc bậc nhất: $95 - (3x + 14) = 45 \implies x = 12$.
* **Ý c:** Tìm số mũ lũy thừa: $2 \cdot 3^{x+1} - 15 = 39 \implies x = 2$.
* **Ý d:** Hình học: Nửa chu vi hình chữ nhật $40 : 2 = 20\text{ cm} \implies x = 8$.

---

### 4. CÂU 13 (2,5 ĐIỂM - Ý a 1,25đ; Ý b 1,25đ)

* **Bối cảnh:** Mảnh vườn hình chữ nhật cần rào xung quanh bằng lưới thép (chừa cổng) và tính chi phí vật liệu.
* **Mã đề 101:** Dài $20\text{ m}$, rộng $12\text{ m}$, cổng rộng $2\text{ m}$, giá $60\ 000$ đ/m.
  * $a)$ Chu vi: $64\text{ m}$; Diện tích: $240\text{ m}^2$.
  * $b)$ Chiều dài rào: $62\text{ m}$; Số tiền: $3\ 720\ 000$ đồng.
* **Mã đề 102:** Dài $25\text{ m}$, rộng $10\text{ m}$, cổng rộng $3\text{ m}$, giá $55\ 000$ đ/m.
* **Mã đề 103:** Dài $18\text{ m}$, rộng $12\text{ m}$, cổng rộng $2\text{ m}$, giá $65\ 000$ đ/m.
* **Mã đề 104:** Dài $22\text{ m}$, rộng $10\text{ m}$, cổng rộng $2\text{ m}$, giá $50\ 000$ đ/m.

---

### 5. CÂU 14 (1,0 ĐIỂM)

* **Mã đề 101:** Cho $A = 1 + 3 + 3^2 + \dots + 3^{100}$. Chứng minh $2A + 1$ là lũy thừa của $3$.
* **Mã đề 102:** Cho $B = 1 + 2 + 2^2 + \dots + 2^{100}$. Chứng minh $B + 1$ là lũy thừa của $2$.
* **Mã đề 103:** Cho $C = 1 + 4 + 4^2 + \dots + 4^{50}$. Chứng minh $3C + 1$ là lũy thừa của $4$.
* **Mã đề 104:** Cho $D = 1 + 5 + 5^2 + \dots + 5^{50}$. Chứng minh $4D + 1$ là lũy thừa của $5$.
