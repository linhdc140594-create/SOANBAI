# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ
## TOÁN 7 - TUẦN 08 - BUỔI 02
### CHỦ ĐỀ: ĐỀ THI THỬ GIỮA HỌC KỲ 1 TOÀN DIỆN (CHUẨN MA TRẬN PHÒNG GD&ĐT)
### Bám sát chương trình SGK mới (Kết nối tri thức với cuộc sống, Cánh Diều, Chân Trời Sáng Tạo)
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. QUY CHUẨN ĐẶC BIỆT & BỐ CỤC TỐI ƯU MỚI (CHUẨN LỚP 7)

Theo hướng dẫn chuẩn hóa cấu trúc đề kiểm tra định kỳ Toán THCS (Layout Gold Standard):
1. **Header đỉnh trang siêu tối giản:**
   - Trang 1: `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 08 - BUỔI 02` và `Mã đề: <MÃ> - Trang 1/2`.
   - Trang 2: `TOÁN 7 - TUẦN 08 - BUỔI 02 | Mã đề: <MÃ> - Trang 2/2`.
   - Bỏ hoàn toàn dòng ghi chủ đề, thời gian; bỏ khung riêng họ tên (học sinh tự ghi tên lên lề trên cùng của giấy).
2. **Bảng Điểm số & Lời nhận xét:** Bắt buộc chiều cao `\rule{0pt}{1.8cm}`.
3. **Phần Trả lời ngắn (Câu 1 đến Câu 10 - 2,5 điểm):**
   - Cấu hình preamble: `\SAOPTN{widthSA=3.2,heightSA=0.62}`.
   - Mỗi câu có ô `\shortans{...}` bo góc mép phải câu hỏi.
   - Quét 100% kiến thức trọng tâm Giữa HK1: Lũy thừa số hữu tỉ, số đối của số thực, căn bậc hai số học, giá trị tuyệt đối, làm tròn số thập phân đến hàng phần trăm, hai góc kề bù, hai góc đối đỉnh, định lý từ vuông góc đến song song, Tiên đề Euclid, bài toán thực tế giảm giá %.
4. **Câu 11 (Trang 1 - 3,0 điểm): Thực hiện phép tính (chuẩn cấu trúc đề thi chính thức):**
   - 6 ý $a, b, c, d, e, f$ mỗi ý $0{,}5$ điểm, chia bảng $3 \times 2$.
   - Mỗi ô dùng `\oBaiTap[5]` (5 dòng kẻ mờ/ô) $\to$ vừa vặn chạm sát đáy Trang 1.
5. **Câu 12 (Trang 2 - 2,0 điểm): Tìm số hữu tỉ $x$, biết:**
   - 4 ý $a, b, c, d$ mỗi ý $0{,}5$ điểm, chia bảng $2 \times 2$.
   - Mỗi ô dùng `\oBaiTap[5]` (5 dòng kẻ mờ/ô).
6. **Câu 13 (Trang 2 - 2,0 điểm): Bài toán hình học thi Giữa HK1 (Từ vuông góc đến song song & Tính góc):**
   - Đóng khung box liền mạch `tabularx`, khu vực làm bài **chia 2 cột (`\dongkeHaiCot{10}`)** có vách phân cách mờ ở giữa $\to$ nhân đôi không gian trình bày và vẽ hình cho học sinh.
   - Gồm 2 ý: $a)$ (1,0 điểm) và $b)$ (1,0 điểm).
7. **Câu 14 (Trang 2 - 0,5 điểm): Vận dụng cao điểm 10 (Dãy số lũy thừa có quy luật):**
   - Đóng khung box liền mạch `tabularx`, khu vực làm bài **chia 2 cột (`\dongkeHaiCot{6}`)** $\to$ vừa vặn chạm sát đáy Trang 2.
8. **Kiểm soát số trang tuyệt đối:** Trọn vẹn 4 mã đề hoán vị ($101, 102, 103, 104$) trong file `.tex` $\rightarrow$ Biên dịch chính xác **8 trang PDF** (mỗi mã đề đúng 2 mặt A4).

---

## 📐 II. MA TRẬN THANG ĐIỂM (TỔNG 10,0 ĐIỂM)

| Câu | Thể loại | Nội dung kiến thức kiểm tra | Điểm | Định dạng LaTeX |
| :---: | :---: | :--- | :---: | :--- |
| **Câu 1 $\to$ 10** | **Trả lời ngắn** | 1. Phép tính lũy thừa $\left(-\frac{a}{b}\right)^2$<br>2. Số đối của số thực âm $-\sqrt{a}$<br>3. Khai căn bậc hai số học $\sqrt{a^2}$<br>4. Tính giá trị biểu thức chứa giá trị tuyệt đối<br>5. Làm tròn số thập phân đến hàng phần trăm<br>6. Số đo góc kề bù<br>7. Số đo góc đối đỉnh<br>8. Định lý từ vuông góc đến song song: $a \perp c, b \perp c \implies a \parallel b$<br>9. Tính chất góc so le trong / đồng vị / trong cùng phía<br>10. Bài toán thực tế ngắn (mua sắm giảm giá %) | **2,5 đ**<br>*(0,25 đ/câu)* | Dùng `\shortans{...}`, ô kết quả bo góc mép phải |
| **Câu 11** | **Tự luận (Đại số)** | **Thực hiện phép tính (hợp lý nếu có thể) - 6 ý:**<br>- a) (0,5 đ) Cộng trừ phối hợp nhóm số hữu tỉ cùng mẫu / số đối<br>- b) (0,5 đ) Tính nhanh đặt thừa số chung phân số<br>- c) (0,5 đ) Lũy thừa kết hợp số thập phân và nhân chia<br>- d) (0,5 đ) Căn bậc hai số học và giá trị tuyệt đối<br>- e) (0,5 đ) Thứ tự thực hiện phép tính có ngoặc tròn, ngoặc vuông $\left[ \dots \right]$<br>- f) (0,5 đ) Rút gọn biểu thức phân thức lũy thừa đưa về cơ số $2, 3, 5$ | **3,0 đ** | Bảng $3 \times 2$, mỗi ô `\oBaiTap[5]` $\to$ kín mép đáy Trang 1 |
| **Câu 12** | **Tự luận (Đại số)** | **Tìm số hữu tỉ $x$, biết:**<br>- a) (0,5 đ) Quy tắc chuyển vế cơ bản: $x - \frac{a}{b} = \frac{c}{d}$<br>- b) (0,5 đ) Tìm $x$ có ngoặc và nhân chia: $\frac{a}{b}x + \frac{c}{d} = \frac{e}{f}$<br>- c) (0,5 đ) Phương trình lũy thừa bậc chẵn: $\left(x + \frac{a}{b}\right)^2 = \frac{c^2}{d^2}$<br>- d) (0,5 đ) Phương trình chứa giá trị tuyệt đối: $|ax - b| = c$ | **2,0 đ** | Bảng $2 \times 2$, mỗi ô `\oBaiTap[5]` |
| **Câu 13** | **Tự luận (Hình học)** | **Bài toán hình học thi Giữa HK1 (Từ vuông góc đến song song & Tính góc):**<br>Cho $a \perp AB$ tại $A$ và $b \perp AB$ tại $B$. Cát tuyến $c$ cắt $a$ tại $C$ và cắt $b$ tại $D$ tạo thành góc $\widehat{ACD} = \alpha$:<br>- a) (1,0 đ) Chứng minh $a \parallel b$.<br>- b) (1,0 đ) Tính số đo góc $\widehat{CDB}$ và góc kề bù với nó. | **2,0 đ** | Khung bảng đóng hộp `tabularx`, bài giải chia 2 cột `\dongkeHaiCot{10}` |
| **Câu 14** | **Tự luận (Nâng cao)** | **Vận dụng cao điểm 10 (Dãy số lũy thừa có quy luật):**<br>Cho dãy tổng $S = \frac{1}{a} + \frac{1}{a^2} + \dots + \frac{1}{a^{2026}}$. Chứng minh rằng $S < \frac{1}{a-1}$. | **0,5 đ** | Khung bảng đóng hộp `tabularx`, bài giải chia 2 cột `\dongkeHaiCot{6}` $\to$ kín mép đáy Trang 2 |

---

## 🔢 III. BẢNG DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ TƯƠNG ĐƯƠNG (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiểm tra | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Lũy thừa số hữu tỉ | Giá trị của biểu thức $\left(-\frac{2}{3}\right)^2$ bằng:<br>$\to$ **KQ: $\frac{4}{9}$** | Giá trị của biểu thức $\left(-\frac{3}{2}\right)^2$ bằng:<br>$\to$ **KQ: $\frac{9}{4}$** | Giá trị của biểu thức $\left(-\frac{1}{4}\right)^2$ bằng:<br>$\to$ **KQ: $\frac{1}{16}$** | Giá trị của biểu thức $\left(-\frac{2}{5}\right)^2$ bằng:<br>$\to$ **KQ: $\frac{4}{25}$** |
| **2** | Số đối của số thực | Số đối của số thực $-\sqrt{7}$ là:<br>$\to$ **KQ: $\sqrt{7}$** | Số đối của số thực $-\sqrt{5}$ là:<br>$\to$ **KQ: $\sqrt{5}$** | Số đối của số thực $-\sqrt{11}$ là:<br>$\to$ **KQ: $\sqrt{11}$** | Số đối của số thực $-\sqrt{13}$ là:<br>$\to$ **KQ: $\sqrt{13}$** |
| **3** | Căn bậc hai số học | Giá trị của biểu thức $\sqrt{121}$ bằng:<br>$\to$ **KQ: $11$** | Giá trị của biểu thức $\sqrt{144}$ bằng:<br>$\to$ **KQ: $12$** | Giá trị của biểu thức $\sqrt{169}$ bằng:<br>$\to$ **KQ: $13$** | Giá trị của biểu thức $\sqrt{196}$ bằng:<br>$\to$ **KQ: $14$** |
| **4** | Giá trị tuyệt đối | Giá trị của biểu thức $\lvert -3{,}8\rvert - \lvert 1{,}8\rvert$ là:<br>$\to$ **KQ: $2$** | Giá trị của biểu thức $\lvert -4{,}6\rvert - \lvert 1{,}6\rvert$ là:<br>$\to$ **KQ: $3$** | Giá trị của biểu thức $\lvert -5{,}9\rvert - \lvert 1{,}9\rvert$ là:<br>$\to$ **KQ: $4$** | Giá trị của biểu thức $\lvert -6{,}7\rvert - \lvert 1{,}7\rvert$ là:<br>$\to$ **KQ: $5$** |
| **5** | Làm tròn số thập phân | Làm tròn số $35{,}746$ đến hàng phần trăm:<br>$\to$ **KQ: $35{,}75$** | Làm tròn số $48{,}263$ đến hàng phần trăm:<br>$\to$ **KQ: $48{,}26$** | Làm tròn số $62{,}538$ đến hàng phần trăm:<br>$\to$ **KQ: $62{,}54$** | Làm tròn số $74{,}825$ đến hàng phần trăm:<br>$\to$ **KQ: $74{,}83$** |
| **6** | Hai góc kề bù | Kề bù có một góc $65^\circ$. Góc còn lại là:<br>$\to$ **KQ: $115^\circ$** | Kề bù có một góc $75^\circ$. Góc còn lại là:<br>$\to$ **KQ: $105^\circ$** | Kề bù có một góc $55^\circ$. Góc còn lại là:<br>$\to$ **KQ: $125^\circ$** | Kề bù có một góc $45^\circ$. Góc còn lại là:<br>$\to$ **KQ: $135^\circ$** |
| **7** | Hai góc đối đỉnh | Cắt nhau tạo góc $70^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $70^\circ$** | Cắt nhau tạo góc $80^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $80^\circ$** | Cắt nhau tạo góc $60^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $60^\circ$** | Cắt nhau tạo góc $50^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $50^\circ$** |
| **8** | Từ vuông góc đến song song | Cho $a \perp c$ và $b \perp c$ ($a \ne b$). Quan hệ $a, b$ là:<br>$\to$ **KQ: song song** | Cho $a \parallel b$ và $c \perp a$. Quan hệ giữa $c$ và $b$ là:<br>$\to$ **KQ: vuông góc** | Hai đường cùng song song với đường thứ ba thì:<br>$\to$ **KQ: song song** | Qua điểm $A$ ngoài $d$, có mấy đường song song $d$?<br>$\to$ **KQ: 1** |
| **9** | Góc tạo bởi cát tuyến | Cho $a \parallel b$. Góc so le trong với góc $55^\circ$ là:<br>$\to$ **KQ: $55^\circ$** | Cho $a \parallel b$. Góc đồng vị với góc $70^\circ$ là:<br>$\to$ **KQ: $70^\circ$** | Cho $a \parallel b$. Góc trong cùng phía với góc $60^\circ$ là:<br>$\to$ **KQ: $120^\circ$** | Cho $a \parallel b$. Góc trong cùng phía với góc $75^\circ$ là:<br>$\to$ **KQ: $105^\circ$** |
| **10** | Toán thực tế giảm giá % | Quyển sách giá $60\,000$ đ giảm $10\%$. Tiền giảm:<br>$\to$ **KQ: $6\,000\text{ đ}$** | Cái áo giá $200\,000$ đ giảm $15\%$. Tiền giảm:<br>$\to$ **KQ: $30\,000\text{ đ}$** | Đôi tất giá $40\,000$ đ giảm $20\%$. Tiền giảm:<br>$\to$ **KQ: $8\,000\text{ đ}$** | Chiếc mũ giá $150\,000$ đ giảm $20\%$. Tiền giảm:<br>$\to$ **KQ: $30\,000\text{ đ}$** |

---

### 2. PHẦN TỰ LUẬN (CÂU 11 ĐẾN CÂU 14 - TỔNG CỘNG 7,5 ĐIỂM)

#### CÂU 11 (3,0 ĐIỂM): THỰC HIỆN PHÉP TÍNH (CHUẨN MA TRẬN THI THỬ GHK1) - 6 Ý

* **Mã đề 101:**
  - a) (0,5 đ) $\frac{3}{7} + \left(-\frac{5}{2}\right) + \frac{4}{7} + \frac{3}{2} = \left(\frac{3}{7} + \frac{4}{7}\right) + \left(-\frac{5}{2} + \frac{3}{2}\right) = 1 + (-1) = 0$.
  - b) (0,5 đ) $\frac{21}{25} \cdot \frac{11}{13} + \frac{21}{25} \cdot \frac{2}{13} - \frac{21}{25} = \frac{21}{25}\left(\frac{11}{13} + \frac{2}{13} - 1\right) = \frac{21}{25} \cdot 0 = 0$.
  - c) (0,5 đ) $\left(-\frac{1}{2}\right)^2 \cdot 24 - 1{,}5 \cdot 4 = \frac{1}{4} \cdot 24 - 6 = 6 - 6 = 0$.
  - d) (0,5 đ) $\sqrt{\frac{16}{9}} - \left|-\frac{1}{3}\right| + \sqrt{36} = \frac{4}{3} - \frac{1}{3} + 6 = 1 + 6 = 7$.
  - e) (0,5 đ) $\frac{5}{6} - \left[ \frac{1}{6} + \left( \frac{1}{2} \right)^2 \right] = \frac{5}{6} - \left[ \frac{1}{6} + \frac{1}{4} \right] = \frac{5}{6} - \frac{5}{12} = \frac{10}{12} - \frac{5}{12} = \frac{5}{12}$.
  - f) (0,5 đ) $\frac{9^2 \cdot 2^{10}}{16^2 \cdot 3^3} = \frac{(3^2)^2 \cdot 2^{10}}{(2^4)^2 \cdot 3^3} = \frac{3^4 \cdot 2^{10}}{2^8 \cdot 3^3} = 3 \cdot 2^2 = 12$.

* **Mã đề 102:**
  - a) (0,5 đ) $\frac{2}{9} + \left(-\frac{7}{3}\right) + \frac{7}{9} + \frac{4}{3} = \left(\frac{2}{9} + \frac{7}{9}\right) + \left(-\frac{7}{3} + \frac{4}{3}\right) = 1 + (-1) = 0$.
  - b) (0,5 đ) $\frac{19}{24} \cdot \frac{8}{11} + \frac{19}{24} \cdot \frac{3}{11} - \frac{19}{24} = \frac{19}{24}\left(\frac{8}{11} + \frac{3}{11} - 1\right) = 0$.
  - c) (0,5 đ) $\left(-\frac{1}{3}\right)^2 \cdot 27 - 0{,}75 \cdot 4 = \frac{1}{9} \cdot 27 - 3 = 3 - 3 = 0$.
  - d) (0,5 đ) $\sqrt{\frac{25}{4}} - \left|-\frac{3}{2}\right| + \sqrt{49} = \frac{5}{2} - \frac{3}{2} + 7 = 1 + 7 = 8$.
  - e) (0,5 đ) $\frac{7}{8} - \left[ \frac{1}{8} + \left( \frac{1}{2} \right)^3 \right] = \frac{7}{8} - \left[ \frac{1}{8} + \frac{1}{8} \right] = \frac{7}{8} - \frac{2}{8} = \frac{5}{8}$.
  - f) (0,5 đ) $\frac{4^3 \cdot 27^2}{8^2 \cdot 9^2} = \frac{(2^2)^3 \cdot (3^3)^2}{(2^3)^2 \cdot (3^2)^2} = \frac{2^6 \cdot 3^6}{2^6 \cdot 3^4} = 3^2 = 9$.

* **Mã đề 103:**
  - a) (0,5 đ) $\frac{4}{11} + \left(-\frac{9}{4}\right) + \frac{7}{11} + \frac{5}{4} = \left(\frac{4}{11} + \frac{7}{11}\right) + \left(-\frac{9}{4} + \frac{5}{4}\right) = 1 + (-1) = 0$.
  - b) (0,5 đ) $\frac{16}{29} \cdot \frac{7}{15} + \frac{16}{29} \cdot \frac{8}{15} - \frac{16}{29} = \frac{16}{29}\left(\frac{7}{15} + \frac{8}{15} - 1\right) = 0$.
  - c) (0,5 đ) $\left(-\frac{1}{2}\right)^3 \cdot (-32) - 2{,}5 \cdot 4 = \left(-\frac{1}{8}\right) \cdot (-32) - 10 = 4 - 10 = -6$.
  - d) (0,5 đ) $\sqrt{\frac{49}{25}} - \left|-\frac{2}{5}\right| + \sqrt{81} = \frac{7}{5} - \frac{2}{5} + 9 = 1 + 9 = 10$.
  - e) (0,5 đ) $\frac{11}{12} - \left[ \frac{1}{4} + \left( \frac{1}{3} \right)^2 \cdot 3 \right] = \frac{11}{12} - \left[ \frac{1}{4} + \frac{1}{3} \right] = \frac{11}{12} - \frac{7}{12} = \frac{4}{12} = \frac{1}{3}$.
  - f) (0,5 đ) $\frac{8^3 \cdot 25^2}{4^4 \cdot 125} = \frac{(2^3)^3 \cdot (5^2)^2}{(2^2)^4 \cdot 5^3} = \frac{2^9 \cdot 5^4}{2^8 \cdot 5^3} = 2 \cdot 5 = 10$.

* **Mã đề 104:**
  - a) (0,5 đ) $\frac{5}{13} + \left(-\frac{11}{5}\right) + \frac{8}{13} + \frac{6}{5} = \left(\frac{5}{13} + \frac{8}{13}\right) + \left(-\frac{11}{5} + \frac{6}{5}\right) = 1 + (-1) = 0$.
  - b) (0,5 đ) $\frac{18}{31} \cdot \frac{9}{17} + \frac{18}{31} \cdot \frac{8}{17} - \frac{18}{31} = \frac{18}{31}\left(\frac{9}{17} + \frac{8}{17} - 1\right) = 0$.
  - c) (0,5 đ) $\left(-\frac{2}{3}\right)^2 \cdot 18 - 3{,}5 \cdot 2 = \frac{4}{9} \cdot 18 - 7 = 8 - 7 = 1$.
  - d) (0,5 đ) $\sqrt{\frac{64}{9}} - \left|-\frac{5}{3}\right| + \sqrt{100} = \frac{8}{3} - \frac{5}{3} + 10 = 1 + 10 = 11$.
  - e) (0,5 đ) $\frac{13}{15} - \left[ \frac{1}{5} + \left( \frac{2}{3} \right)^2 : \frac{4}{3} \right] = \frac{13}{15} - \left[ \frac{1}{5} + \frac{4}{9} \cdot \frac{3}{4} \right] = \frac{13}{15} - \left[ \frac{1}{5} + \frac{1}{3} \right] = \frac{13}{15} - \frac{8}{15} = \frac{5}{15} = \frac{1}{3}$.
  - f) (0,5 đ) $\frac{16^2 \cdot 9^3}{32 \cdot 27^2} = \frac{(2^4)^2 \cdot (3^2)^3}{2^5 \cdot (3^3)^2} = \frac{2^8 \cdot 3^6}{2^5 \cdot 3^6} = 2^3 = 8$.

---

#### CÂU 12 (2,0 ĐIỂM): TÌM SỐ HỮU TỈ $x$, BIẾT:

* **Mã đề 101:**
  - a) (0,5 đ) $x - \frac{1}{4} = \frac{3}{4} \implies x = \frac{3}{4} + \frac{1}{4} = 1$.
  - b) (0,5 đ) $\frac{2}{3}x + \frac{1}{6} = \frac{3}{2} \implies \frac{2}{3}x = \frac{9}{6} - \frac{1}{6} = \frac{8}{6} = \frac{4}{3} \implies x = \frac{4}{3} : \frac{2}{3} = 2$.
  - c) (0,5 đ) $\left(x + \frac{1}{2}\right)^2 = \frac{25}{4} \implies x + \frac{1}{2} = \pm\frac{5}{2} \implies x \in \left\{2; -3\right\}$.
  - d) (0,5 đ) $\lvert 2x - 1\rvert = 5 \implies 2x - 1 = 5$ hoặc $2x - 1 = -5 \implies x \in \{3; -2\}$.

* **Mã đề 102:**
  - a) (0,5 đ) $x - \frac{1}{3} = \frac{2}{3} \implies x = 1$.
  - b) (0,5 đ) $\frac{3}{5}x + \frac{1}{10} = \frac{13}{10} \implies \frac{3}{5}x = \frac{12}{10} = \frac{6}{5} \implies x = \frac{6}{5} : \frac{3}{5} = 2$.
  - c) (0,5 đ) $\left(x + \frac{1}{3}\right)^2 = \frac{49}{9} \implies x + \frac{1}{3} = \pm\frac{7}{3} \implies x \in \left\{2; -\frac{8}{3}\right\}$.
  - d) (0,5 đ) $\lvert 3x - 1\rvert = 8 \implies 3x - 1 = 8$ hoặc $3x - 1 = -8 \implies x \in \left\{3; -\frac{7}{3}\right\}$.

* **Mã đề 103:**
  - a) (0,5 đ) $x - \frac{2}{5} = \frac{3}{5} \implies x = 1$.
  - b) (0,5 đ) $\frac{4}{7}x + \frac{3}{14} = \frac{19}{14} \implies \frac{4}{7}x = \frac{16}{14} = \frac{8}{7} \implies x = \frac{8}{7} : \frac{4}{7} = 2$.
  - c) (0,5 đ) $\left(x + \frac{1}{4}\right)^2 = \frac{81}{16} \implies x + \frac{1}{4} = \pm\frac{9}{4} \implies x \in \left\{2; -\frac{5}{2}\right\}$.
  - d) (0,5 đ) $\lvert 2x - 3\rvert = 5 \implies 2x - 3 = 5$ hoặc $2x - 3 = -5 \implies x \in \{4; -1\}$.

* **Mã đề 104:**
  - a) (0,5 đ) $x - \frac{3}{7} = \frac{4}{7} \implies x = 1$.
  - b) (0,5 đ) $\frac{5}{8}x + \frac{3}{16} = \frac{23}{16} \implies \frac{5}{8}x = \frac{20}{16} = \frac{5}{4} \implies x = \frac{5}{4} : \frac{5}{8} = 2$.
  - c) (0,5 đ) $\left(x + \frac{1}{5}\right)^2 = \frac{36}{25} \implies x + \frac{1}{5} = \pm\frac{6}{5} \implies x \in \left\{1; -\frac{7}{5}\right\}$.
  - d) (0,5 đ) $\lvert 3x - 2\rvert = 7 \implies 3x - 2 = 7$ hoặc $3x - 2 = -7 \implies x \in \left\{3; -\frac{5}{3}\right\}$.

---

#### CÂU 13 (2,0 ĐIỂM): BÀI TOÁN HÌNH HỌC (TỪ VUÔNG GÓC ĐẾN SONG SONG & TÍNH GÓC) - BÀI LÀM CHIA 2 CỘT

*(Khu vực làm bài: Chia 2 cột `\dongkeHaiCot{10}` có vách phân cách mờ ở giữa, học sinh vẽ hình hoặc làm ý a ở cột 1 và làm ý b ở cột 2)*

* **Mã đề 101:**
  Cho đường thẳng $a$ vuông góc với đoạn thẳng $AB$ tại $A$, đường thẳng $b$ vuông góc với $AB$ tại $B$. Một đường thẳng $c$ cắt đường thẳng $a$ tại $C$ và cắt đường thẳng $b$ tại $D$ sao cho góc $\widehat{ACD} = 120^\circ$.
  - a) (1,0 đ) Chứng minh rằng $a \parallel b$.
    - *Lời giải:*
      - Ta có: $a \perp AB$ tại $A$ và $b \perp AB$ tại $B$ (theo giả thiết). *(0,5đ)*
      - Áp dụng định lý: Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau.
      - Suy ra $a \parallel b$. *(0,5đ)*
  - b) (1,0 đ) Tính số đo góc $\widehat{CDB}$ và số đo góc kề bù với nó.
    - *Lời giải:*
      - Vì $a \parallel b$, nên $\widehat{ACD}$ và $\widehat{CDB}$ là hai góc trong cùng phía, do đó:
        $$\widehat{ACD} + \widehat{CDB} = 180^\circ \implies \widehat{CDB} = 180^\circ - 120^\circ = 60^\circ \quad (0{,}5\text{đ})$$
      - Gọi góc kề bù với góc $\widehat{CDB}$ là $\widehat{D}_1$, ta có:
        $$\widehat{D}_1 = 180^\circ - \widehat{CDB} = 180^\circ - 60^\circ = 120^\circ \quad (0{,}5\text{đ})$$

* **Mã đề 102:**
  Cho $a \perp AB$ tại $A, b \perp AB$ tại $B$. Đường thẳng $c$ cắt $a, b$ tại $C, D$ với $\widehat{ACD} = 130^\circ$.
  - a) (1,0 đ) Chứng minh $a \parallel b$ (cùng vuông góc với $AB$).
  - b) (1,0 đ) $\widehat{CDB} = 180^\circ - 130^\circ = 50^\circ$ (trong cùng phía bù nhau). Góc kề bù là $130^\circ$.

* **Mã đề 103:**
  Cho $a \perp AB$ tại $A, b \perp AB$ tại $B$. Đường thẳng $c$ cắt $a, b$ tại $C, D$ với $\widehat{ACD} = 115^\circ$.
  - a) (1,0 đ) Chứng minh $a \parallel b$ (cùng vuông góc với $AB$).
  - b) (1,0 đ) $\widehat{CDB} = 180^\circ - 115^\circ = 65^\circ$. Góc kề bù là $115^\circ$.

* **Mã đề 104:**
  Cho $a \perp AB$ tại $A, b \perp AB$ tại $B$. Đường thẳng $c$ cắt $a, b$ tại $C, D$ với $\widehat{ACD} = 125^\circ$.
  - a) (1,0 đ) Chứng minh $a \parallel b$ (cùng vuông góc với $AB$).
  - b) (1,0 đ) $\widehat{CDB} = 180^\circ - 125^\circ = 55^\circ$. Góc kề bù là $125^\circ$.

---

#### CÂU 14 (0,5 ĐIỂM): VẬN DỤNG CAO ĐIỂM 10 (DÃY SỐ LŨY THỪA CÓ QUY LUẬT) - BÀI LÀM CHIA 2 CỘT

*(Khu vực làm bài: Chia 2 cột `\dongkeHaiCot{6}` có vách phân cách mờ ở giữa)*

* **Mã đề 101:**
  Cho biểu thức: $S = \frac{1}{3} + \frac{1}{3^2} + \frac{1}{3^3} + \dots + \frac{1}{3^{2026}}$. Chứng minh rằng $S < \frac{1}{2}$.
  - *Lời giải:*
    - Nhân cả hai vế của $S$ với $3$, ta có:
      $$3S = 1 + \frac{1}{3} + \frac{1}{3^2} + \dots + \frac{1}{3^{2025}}$$
    - Lấy $3S - S$, ta được:
      $$2S = 1 - \frac{1}{3^{2026}} \implies S = \frac{1}{2} - \frac{1}{2 \cdot 3^{2026}} \quad (0{,}25\text{đ})$$
    - Vì $\frac{1}{2 \cdot 3^{2026}} > 0$ nên $S < \frac{1}{2}$ (đpcm). *(0,25đ)*

* **Mã đề 102:**
  Cho $S = \frac{1}{4} + \frac{1}{4^2} + \dots + \frac{1}{4^{2026}}$. Chứng minh rằng $S < \frac{1}{3}$.
  - $4S = 1 + \frac{1}{4} + \dots + \frac{1}{4^{2025}} \implies 3S = 1 - \frac{1}{4^{2026}} \implies S = \frac{1}{3} - \frac{1}{3 \cdot 4^{2026}} < \frac{1}{3}$.

* **Mã đề 103:**
  Cho $S = \frac{1}{5} + \frac{1}{5^2} + \dots + \frac{1}{5^{2026}}$. Chứng minh rằng $S < \frac{1}{4}$.
  - $5S = 1 + \frac{1}{5} + \dots + \frac{1}{5^{2025}} \implies 4S = 1 - \frac{1}{5^{2026}} \implies S = \frac{1}{4} - \frac{1}{4 \cdot 5^{2026}} < \frac{1}{4}$.

* **Mã đề 104:**
  Cho $S = \frac{1}{2} + \frac{1}{2^2} + \dots + \frac{1}{2^{2026}}$. Chứng minh rằng $S < 1$.
  - $2S = 1 + \frac{1}{2} + \dots + \frac{1}{2^{2025}} \implies S = 1 - \frac{1}{2^{2026}} < 1$.
