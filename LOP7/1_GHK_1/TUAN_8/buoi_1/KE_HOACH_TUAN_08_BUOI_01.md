# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ
## TOÁN 7 - TUẦN 08 - BUỔI 01
### CHỦ ĐỀ: ÔN TẬP CHƯƠNG 3 (GÓC & ĐƯỜNG THẲNG SONG SONG) & TỔNG ÔN ĐẠI SỐ GHK1
### Bám sát chương trình SGK mới (Kết nối tri thức với cuộc sống, Cánh Diều, Chân Trời Sáng Tạo)
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. QUY CHUẨN ĐẶC BIỆT & BỐ CỤC TỐI ƯU MỚI (CHUẨN LỚP 7)

Theo hướng dẫn chuẩn hóa cấu trúc đề kiểm tra định kỳ Toán THCS (Layout Gold Standard):
1. **Header đỉnh trang siêu tối giản:**
   - Trang 1: `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 08 - BUỔI 01` và `Mã đề: <MÃ> - Trang 1/2`.
   - Trang 2: `TOÁN 7 - TUẦN 08 - BUỔI 01 | Mã đề: <MÃ> - Trang 2/2`.
   - Bỏ hoàn toàn dòng ghi chủ đề, thời gian; bỏ khung riêng họ tên (học sinh tự ghi tên lên lề trên cùng của giấy).
2. **Bảng Điểm số & Lời nhận xét:** Bắt buộc chiều cao `\rule{0pt}{1.8cm}`.
3. **Phần Trả lời ngắn (Câu 1 đến Câu 10 - 2,5 điểm):**
   - Cấu hình preamble: `\SAOPTN{widthSA=3.2,heightSA=0.62}`.
   - Mỗi câu có ô `\shortans{...}` bo góc mép phải câu hỏi.
   - Quét toàn diện kiến thức Giữa HK1: Số đối của số hữu tỉ, căn bậc hai số học, giá trị tuyệt đối của số thực, làm tròn số thập phân, hai góc đối đỉnh, hai góc kề bù, tia phân giác của một góc, các góc tạo bởi một cát tuyến cắt hai đường thẳng song song, quan hệ từ vuông góc đến song song / Tiên đề Euclid, bài toán thực tế tỉ số phần trăm.
4. **Câu 11 (Trang 1 - 3,0 điểm): Thực hiện phép tính (hợp lý nếu có thể):**
   - 6 ý $a, b, c, d, e, f$ mỗi ý $0{,}5$ điểm, chia bảng $3 \times 2$.
   - Mỗi ô dùng `\oBaiTap[5]` (5 dòng kẻ mờ/ô) $\to$ vừa vặn chạm sát đáy Trang 1.
5. **Câu 12 (Trang 2 - 2,0 điểm): Tìm số hữu tỉ $x$, biết:**
   - 4 ý $a, b, c, d$ mỗi ý $0{,}5$ điểm, chia bảng $2 \times 2$.
   - Mỗi ô dùng `\oBaiTap[5]` (5 dòng kẻ mờ/ô).
6. **Câu 13 (Trang 2 - 2,0 điểm): Bài toán hình học tổng hợp (Góc gãy khúc & Tiên đề Euclid):**
   - Đóng khung box liền mạch `tabularx`, khu vực làm bài **chia 2 cột (`\dongkeHaiCot{10}`)** có vách phân cách mờ ở giữa $\to$ nhân đôi không gian trình bày và vẽ hình cho học sinh.
   - Gồm 2 ý: $a)$ (1,0 điểm) và $b)$ (1,0 điểm).
7. **Câu 14 (Trang 2 - 0,5 điểm): Vận dụng cao phân loại 10 điểm (BĐT Giá trị tuyệt đối tìm Min):**
   - Đóng khung box liền mạch `tabularx`, khu vực làm bài **chia 2 cột (`\dongkeHaiCot{6}`)** $\to$ vừa vặn chạm sát đáy Trang 2.
8. **Kiểm soát số trang tuyệt đối:** Trọn vẹn 4 mã đề hoán vị ($101, 102, 103, 104$) trong file `.tex` $\rightarrow$ Biên dịch chính xác **8 trang PDF** (mỗi mã đề đúng 2 mặt A4).

---

## 📐 II. MA TRẬN THANG ĐIỂM (TỔNG 10,0 ĐIỂM)

| Câu | Thể loại | Nội dung kiến thức kiểm tra | Điểm | Định dạng LaTeX |
| :---: | :---: | :--- | :---: | :--- |
| **Câu 1 $\to$ 10** | **Trả lời ngắn** | 1. Số đối của số hữu tỉ âm<br>2. Căn bậc hai số học $\sqrt{\frac{a}{b}}$<br>3. Giá trị tuyệt đối của số thực<br>4. Làm tròn số thập phân đến hàng phần mười<br>5. Số đo góc đối đỉnh<br>6. Số đo góc kề bù<br>7. Tính chất tia phân giác của một góc<br>8. Tính chất góc so le trong / đồng vị khi có hai đường thẳng song song<br>9. Quan hệ từ vuông góc đến song song / Tiên đề Euclid<br>10. Bài toán thực tế ngắn (mua sắm giảm giá %) | **2,5 đ**<br>*(0,25 đ/câu)* | Dùng `\shortans{...}`, ô kết quả bo góc mép phải |
| **Câu 11** | **Tự luận (Đại số)** | **Thực hiện phép tính (hợp lý nếu có thể) - 6 ý:**<br>- a) (0,5 đ) Nhóm phân số cùng mẫu / triệt tiêu số đối<br>- b) (0,5 đ) Tính nhanh đặt thừa số chung<br>- c) (0,5 đ) Lũy thừa kết hợp số nguyên và số thập phân<br>- d) (0,5 đ) Phối hợp căn bậc hai số học và giá trị tuyệt đối<br>- e) (0,5 đ) Biểu thức phối hợp số hữu tỉ, số thập phân và phép chia<br>- f) (0,5 đ) Rút gọn biểu thức tích thương lũy thừa đưa về cơ số nguyên tố | **3,0 đ** | Bảng $3 \times 2$, mỗi ô `\oBaiTap[5]` $\to$ kín mép đáy Trang 1 |
| **Câu 12** | **Tự luận (Đại số)** | **Tìm số hữu tỉ $x$, biết:**<br>- a) (0,5 đ) Chuyển vế cơ bản: $x + \frac{a}{b} = \frac{c}{d}$<br>- b) (0,5 đ) Nhân chia có ngoặc / hai bước tính: $\frac{a}{b}x - \frac{c}{d} = \frac{e}{f}$<br>- c) (0,5 đ) Phương trình lũy thừa bậc hai: $\left(x - \frac{a}{b}\right)^2 = \frac{c^2}{d^2}$<br>- d) (0,5 đ) Phương trình chứa giá trị tuyệt đối: $|ax \pm b| = c$ | **2,0 đ** | Bảng $2 \times 2$, mỗi ô `\oBaiTap[5]` |
| **Câu 13** | **Tự luận (Hình học)** | **Bài toán hình học tổng hợp (Góc gãy khúc & Tiên đề Euclid):**<br>Cho $Ax \parallel By$, điểm $O$ tạo với hai tia thành góc gãy $\widehat{AOB}$:<br>- a) (1,0 đ) Kẻ tia $Oz \parallel Ax$, chứng minh $Oz \parallel By$.<br>- b) (1,0 đ) Dùng tính chất góc so le trong tính số đo góc $\widehat{AOB}$. | **2,0 đ** | Khung bảng đóng hộp `tabularx`, bài giải chia 2 cột `\dongkeHaiCot{10}` |
| **Câu 14** | **Tự luận (Nâng cao)** | **Vận dụng cao điểm 10 (Bất đẳng thức giá trị tuyệt đối):**<br>Tìm giá trị nhỏ nhất của biểu thức dạng $A = |x - a| + |x - b|$ ($a < b$) áp dụng $|A| + |B| \ge |A + B|$. | **0,5 đ** | Khung bảng đóng hộp `tabularx`, bài giải chia 2 cột `\dongkeHaiCot{6}` $\to$ kín mép đáy Trang 2 |

---

## 🔢 III. BẢNG DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ TƯƠNG ĐƯƠNG (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiểm tra | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Số đối của số hữu tỉ | Số đối của số hữu tỉ $-\frac{5}{14}$ là:<br>$\to$ **KQ: $\frac{5}{14}$** | Số đối của số hữu tỉ $-\frac{7}{18}$ là:<br>$\to$ **KQ: $\frac{7}{18}$** | Số đối của số hữu tỉ $-\frac{9}{16}$ là:<br>$\to$ **KQ: $\frac{9}{16}$** | Số đối của số hữu tỉ $-\frac{11}{20}$ là:<br>$\to$ **KQ: $\frac{11}{20}$** |
| **2** | Căn bậc hai số học | Giá trị của biểu thức $\sqrt{\frac{49}{100}}$ bằng:<br>$\to$ **KQ: $\frac{7}{10}$** | Giá trị của biểu thức $\sqrt{\frac{64}{81}}$ bằng:<br>$\to$ **KQ: $\frac{8}{9}$** | Giá trị của biểu thức $\sqrt{\frac{81}{121}}$ bằng:<br>$\to$ **KQ: $\frac{9}{11}$** | Giá trị của biểu thức $\sqrt{\frac{121}{144}}$ bằng:<br>$\to$ **KQ: $\frac{11}{12}$** |
| **3** | Giá trị tuyệt đối | Giá trị của biểu thức $\lvert -4{,}7\rvert + \lvert 3{,}3\rvert$ là:<br>$\to$ **KQ: $8$** | Giá trị của biểu thức $\lvert -5{,}6\rvert + \lvert 3{,}4\rvert$ là:<br>$\to$ **KQ: $9$** | Giá trị của biểu thức $\lvert -6{,}8\rvert + \lvert 3{,}2\rvert$ là:<br>$\to$ **KQ: $10$** | Giá trị của biểu thức $\lvert -7{,}5\rvert + \lvert 3{,}5\rvert$ là:<br>$\to$ **KQ: $11$** |
| **4** | Làm tròn số thập phân | Làm tròn số $19{,}462$ đến hàng phần mười:<br>$\to$ **KQ: $19{,}5$** | Làm tròn số $28{,}371$ đến hàng phần mười:<br>$\to$ **KQ: $28{,}4$** | Làm tròn số $37{,}584$ đến hàng phần mười:<br>$\to$ **KQ: $37{,}6$** | Làm tròn số $46{,}293$ đến hàng phần mười:<br>$\to$ **KQ: $46{,}3$** |
| **5** | Hai góc đối đỉnh | Cắt nhau tạo góc $55^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $55^\circ$** | Cắt nhau tạo góc $65^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $65^\circ$** | Cắt nhau tạo góc $75^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $75^\circ$** | Cắt nhau tạo góc $85^\circ$. Góc đối đỉnh với nó là:<br>$\to$ **KQ: $85^\circ$** |
| **6** | Hai góc kề bù | $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, $\widehat{xOy}=60^\circ$. $\widehat{yOz}=$\<br>$\to$ **KQ: $120^\circ$** | $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, $\widehat{xOy}=70^\circ$. $\widehat{yOz}=$\<br>$\to$ **KQ: $110^\circ$** | $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, $\widehat{xOy}=50^\circ$. $\widehat{yOz}=$\<br>$\to$ **KQ: $130^\circ$** | $\widehat{xOy}$ và $\widehat{yOz}$ kề bù, $\widehat{xOy}=80^\circ$. $\widehat{yOz}=$\<br>$\to$ **KQ: $100^\circ$** |
| **7** | Tia phân giác của góc | Tia $Ot$ là phân giác $\widehat{xOy}=130^\circ$. $\widehat{xOt}=$\<br>$\to$ **KQ: $65^\circ$** | Tia $Ot$ là phân giác $\widehat{xOy}=150^\circ$. $\widehat{xOt}=$\<br>$\to$ **KQ: $75^\circ$** | Tia $Ot$ là phân giác $\widehat{xOy}=140^\circ$. $\widehat{xOt}=$\<br>$\to$ **KQ: $70^\circ$** | Tia $Ot$ là phân giác $\widehat{xOy}=160^\circ$. $\widehat{xOt}=$\<br>$\to$ **KQ: $80^\circ$** |
| **8** | Góc so le trong / đồng vị | Cho $a \parallel b$. Góc so le trong với góc $45^\circ$ là:<br>$\to$ **KQ: $45^\circ$** | Cho $a \parallel b$. Góc đồng vị với góc $60^\circ$ là:<br>$\to$ **KQ: $60^\circ$** | Cho $a \parallel b$. Góc trong cùng phía với góc $70^\circ$ là:<br>$\to$ **KQ: $110^\circ$** | Cho $a \parallel b$. Góc trong cùng phía với góc $80^\circ$ là:<br>$\to$ **KQ: $100^\circ$** |
| **9** | Từ vuông góc đến song song | Cho $a \parallel b$ và $c \perp a$. Quan hệ giữa $c$ và $b$ là:<br>$\to$ **KQ: vuông góc** | Qua điểm $M$ ngoài $d$, có mấy đường song song $d$?<br>$\to$ **KQ: 1** | Hai đường thẳng cùng song song với đường thứ ba thì:<br>$\to$ **KQ: song song** | Hai đường thẳng cùng vuông góc với đường thứ ba thì:<br>$\to$ **KQ: song song** |
| **10** | Toán thực tế giảm giá % | Cặp sách giá $250\,000$ đ giảm $20\%$. Số tiền giảm:<br>$\to$ **KQ: $50\,000\text{ đ}$** | Hộp bút giá $80\,000$ đ giảm $25\%$. Số tiền giảm:<br>$\to$ **KQ: $20\,000\text{ đ}$** | Đôi giày giá $300\,000$ đ giảm $15\%$. Số tiền giảm:<br>$\to$ **KQ: $45\,000\text{ đ}$** | Áo khoác giá $400\,000$ đ giảm $10\%$. Số tiền giảm:<br>$\to$ **KQ: $40\,000\text{ đ}$** |

---

### 2. PHẦN TỰ LUẬN (CÂU 11 ĐẾN CÂU 14 - TỔNG CỘNG 7,5 ĐIỂM)

#### CÂU 11 (3,0 ĐIỂM): THỰC HIỆN PHÉP TÍNH (HỢP LÝ NẾU CÓ THỂ) - 6 Ý

* **Mã đề 101:**
  - a) (0,5 đ) $\frac{7}{15} - \frac{5}{8} + \frac{8}{15} - \frac{3}{8} = \left(\frac{7}{15} + \frac{8}{15}\right) - \left(\frac{5}{8} + \frac{3}{8}\right) = 1 - 1 = 0$.
  - b) (0,5 đ) $\frac{12}{19} \cdot \frac{5}{7} + \frac{12}{19} \cdot \frac{2}{7} - \frac{12}{19} = \frac{12}{19}\left(\frac{5}{7} + \frac{2}{7} - 1\right) = \frac{12}{19} \cdot 0 = 0$.
  - c) (0,5 đ) $\left(-\frac{1}{2}\right)^3 \cdot 16 + \left(\frac{2}{3}\right)^2 \cdot 9 = -\frac{1}{8} \cdot 16 + \frac{4}{9} \cdot 9 = -2 + 4 = 2$.
  - d) (0,5 đ) $\sqrt{\frac{49}{16}} - \left|-\frac{3}{4}\right| + \sqrt{64} = \frac{7}{4} - \frac{3}{4} + 8 = 1 + 8 = 9$.
  - e) (0,5 đ) $\left(\frac{3}{4} - 0{,}2\right) : \frac{11}{20} + \frac{5}{11} \cdot 1{,}1 = \left(\frac{15}{20} - \frac{4}{20}\right) \cdot \frac{20}{11} + \frac{5}{11} \cdot \frac{11}{10} = \frac{11}{20} \cdot \frac{20}{11} + \frac{1}{2} = 1 + \frac{1}{2} = \frac{3}{2}$.
  - f) (0,5 đ) $\frac{4^2 \cdot 9^3}{6^4} = \frac{(2^2)^2 \cdot (3^2)^3}{(2 \cdot 3)^4} = \frac{2^4 \cdot 3^6}{2^4 \cdot 3^4} = 3^2 = 9$.

* **Mã đề 102:**
  - a) (0,5 đ) $\frac{5}{13} - \frac{7}{10} + \frac{8}{13} - \frac{3}{10} = \left(\frac{5}{13} + \frac{8}{13}\right) - \left(\frac{7}{10} + \frac{3}{10}\right) = 1 - 1 = 0$.
  - b) (0,5 đ) $\frac{15}{23} \cdot \frac{4}{9} + \frac{15}{23} \cdot \frac{5}{9} - \frac{15}{23} = \frac{15}{23}\left(\frac{4}{9} + \frac{5}{9} - 1\right) = 0$.
  - c) (0,5 đ) $\left(-\frac{1}{3}\right)^2 \cdot 18 + \left(-\frac{1}{2}\right)^3 \cdot 24 = \frac{1}{9} \cdot 18 - \frac{1}{8} \cdot 24 = 2 - 3 = -1$.
  - d) (0,5 đ) $\sqrt{\frac{81}{25}} - \left|-\frac{4}{5}\right| + \sqrt{49} = \frac{9}{5} - \frac{4}{5} + 7 = 1 + 7 = 8$.
  - e) (0,5 đ) $\left(\frac{4}{5} - 0{,}25\right) : \frac{11}{20} + \frac{3}{11} \cdot 2{,}2 = \left(\frac{16}{20} - \frac{5}{20}\right) \cdot \frac{20}{11} + \frac{3}{11} \cdot \frac{22}{10} = 1 + \frac{3}{5} = \frac{8}{5}$.
  - f) (0,5 đ) $\frac{8^2 \cdot 27^2}{6^5} = \frac{(2^3)^2 \cdot (3^3)^2}{(2 \cdot 3)^5} = \frac{2^6 \cdot 3^6}{2^5 \cdot 3^5} = 2 \cdot 3 = 6$.

* **Mã đề 103:**
  - a) (0,5 đ) $\frac{9}{17} - \frac{4}{9} + \frac{8}{17} - \frac{5}{9} = \left(\frac{9}{17} + \frac{8}{17}\right) - \left(\frac{4}{9} + \frac{5}{9}\right) = 1 - 1 = 0$.
  - b) (0,5 đ) $\frac{17}{21} \cdot \frac{3}{8} + \frac{17}{21} \cdot \frac{5}{8} - \frac{17}{21} = \frac{17}{21}\left(\frac{3}{8} + \frac{5}{8} - 1\right) = 0$.
  - c) (0,5 đ) $\left(-\frac{1}{2}\right)^4 \cdot 32 + \left(-\frac{2}{3}\right)^2 \cdot 18 = \frac{1}{16} \cdot 32 + \frac{4}{9} \cdot 18 = 2 + 8 = 10$.
  - d) (0,5 đ) $\sqrt{\frac{64}{9}} - \left|-\frac{5}{3}\right| + \sqrt{100} = \frac{8}{3} - \frac{5}{3} + 10 = 1 + 10 = 11$.
  - e) (0,5 đ) $\left(\frac{2}{3} - 0{,}25\right) : \frac{5}{12} + \frac{4}{7} \cdot 1{,}4 = \left(\frac{8}{12} - \frac{3}{12}\right) \cdot \frac{12}{5} + \frac{4}{7} \cdot \frac{7}{5} = 1 + \frac{4}{5} = \frac{9}{5}$.
  - f) (0,5 đ) $\frac{4^3 \cdot 9^2}{6^4} = \frac{(2^2)^3 \cdot (3^2)^2}{(2 \cdot 3)^4} = \frac{2^6 \cdot 3^4}{2^4 \cdot 3^4} = 2^2 = 4$.

* **Mã đề 104:**
  - a) (0,5 đ) $\frac{6}{19} - \frac{5}{11} + \frac{13}{19} - \frac{6}{11} = \left(\frac{6}{19} + \frac{13}{19}\right) - \left(\frac{5}{11} + \frac{6}{11}\right) = 1 - 1 = 0$.
  - b) (0,5 đ) $\frac{14}{25} \cdot \frac{7}{10} + \frac{14}{25} \cdot \frac{3}{10} - \frac{14}{25} = \frac{14}{25}\left(\frac{7}{10} + \frac{3}{10} - 1\right) = 0$.
  - c) (0,5 đ) $\left(-\frac{3}{2}\right)^2 \cdot 8 - \left(-\frac{1}{3}\right)^3 \cdot 54 = \frac{9}{4} \cdot 8 - \left(-\frac{1}{27}\right) \cdot 54 = 18 - (-2) = 20$.
  - d) (0,5 đ) $\sqrt{\frac{121}{36}} - \left|-\frac{5}{6}\right| + \sqrt{121} = \frac{11}{6} - \frac{5}{6} + 11 = 1 + 11 = 12$.
  - e) (0,5 đ) $\left(\frac{3}{5} - 0{,}25\right) : \frac{7}{20} + \frac{5}{9} \cdot 1{,}8 = \left(\frac{12}{20} - \frac{5}{20}\right) \cdot \frac{20}{7} + \frac{5}{9} \cdot \frac{9}{5} = 1 + 1 = 2$.
  - f) (0,5 đ) $\frac{25^2 \cdot 4^3}{10^4} = \frac{(5^2)^2 \cdot (2^2)^3}{(2 \cdot 5)^4} = \frac{5^4 \cdot 2^6}{2^4 \cdot 5^4} = 2^2 = 4$.

---

#### CÂU 12 (2,0 ĐIỂM): TÌM SỐ HỮU TỈ $x$, BIẾT:

* **Mã đề 101:**
  - a) (0,5 đ) $x + \frac{2}{5} = \frac{9}{10} \implies x = \frac{9}{10} - \frac{4}{10} = \frac{5}{10} = \frac{1}{2}$.
  - b) (0,5 đ) $\frac{2}{3}x - \frac{1}{2} = \frac{5}{6} \implies \frac{2}{3}x = \frac{5}{6} + \frac{3}{6} = \frac{8}{6} = \frac{4}{3} \implies x = \frac{4}{3} : \frac{2}{3} = 2$.
  - c) (0,5 đ) $\left(x - \frac{1}{2}\right)^2 = \frac{9}{16} \implies x - \frac{1}{2} = \pm\frac{3}{4} \implies x \in \left\{\frac{5}{4}; -\frac{1}{4}\right\}$.
  - d) (0,5 đ) $\left|2x - \frac{1}{3}\right| = \frac{5}{3} \implies 2x - \frac{1}{3} = \frac{5}{3}$ hoặc $2x - \frac{1}{3} = -\frac{5}{3} \implies x \in \left\{1; -\frac{2}{3}\right\}$.

* **Mã đề 102:**
  - a) (0,5 đ) $x + \frac{1}{3} = \frac{5}{6} \implies x = \frac{5}{6} - \frac{2}{6} = \frac{3}{6} = \frac{1}{2}$.
  - b) (0,5 đ) $\frac{3}{4}x - \frac{1}{3} = \frac{7}{6} \implies \frac{3}{4}x = \frac{7}{6} + \frac{2}{6} = \frac{9}{6} = \frac{3}{2} \implies x = \frac{3}{2} : \frac{3}{4} = 2$.
  - c) (0,5 đ) $\left(x - \frac{1}{3}\right)^2 = \frac{16}{25} \implies x - \frac{1}{3} = \pm\frac{4}{5} \implies x \in \left\{\frac{17}{15}; -\frac{7}{15}\right\}$.
  - d) (0,5 đ) $\left|2x - \frac{1}{2}\right| = \frac{7}{2} \implies 2x - \frac{1}{2} = \frac{7}{2}$ hoặc $2x - \frac{1}{2} = -\frac{7}{2} \implies x \in \left\{2; -\frac{3}{2}\right\}$.

* **Mã đề 103:**
  - a) (0,5 đ) $x + \frac{3}{4} = \frac{11}{12} \implies x = \frac{11}{12} - \frac{9}{12} = \frac{2}{12} = \frac{1}{6}$.
  - b) (0,5 đ) $\frac{4}{5}x - \frac{1}{2} = \frac{11}{10} \implies \frac{4}{5}x = \frac{11}{10} + \frac{5}{10} = \frac{16}{10} = \frac{8}{5} \implies x = \frac{8}{5} : \frac{4}{5} = 2$.
  - c) (0,5 đ) $\left(x - \frac{1}{4}\right)^2 = \frac{25}{36} \implies x - \frac{1}{4} = \pm\frac{5}{6} \implies x \in \left\{\frac{13}{12}; -\frac{7}{12}\right\}$.
  - d) (0,5 đ) $\left|3x - \frac{1}{4}\right| = \frac{11}{4} \implies 3x - \frac{1}{4} = \frac{11}{4}$ hoặc $3x - \frac{1}{4} = -\frac{11}{4} \implies x \in \left\{1; -\frac{5}{6}\right\}$.

* **Mã đề 104:**
  - a) (0,5 đ) $x + \frac{2}{7} = \frac{11}{14} \implies x = \frac{11}{14} - \frac{4}{14} = \frac{7}{14} = \frac{1}{2}$.
  - b) (0,5 đ) $\frac{5}{6}x - \frac{1}{4} = \frac{17}{12} \implies \frac{5}{6}x = \frac{17}{12} + \frac{3}{12} = \frac{20}{12} = \frac{5}{3} \implies x = \frac{5}{3} : \frac{5}{6} = 2$.
  - c) (0,5 đ) $\left(x - \frac{1}{5}\right)^2 = \frac{9}{25} \implies x - \frac{1}{5} = \pm\frac{3}{5} \implies x \in \left\{\frac{4}{5}; -\frac{2}{5}\right\}$.
  - d) (0,5 đ) $\left|2x - \frac{1}{5}\right| = \frac{9}{5} \implies 2x - \frac{1}{5} = \frac{9}{5}$ hoặc $2x - \frac{1}{5} = -\frac{9}{5} \implies x \in \left\{1; -\frac{4}{5}\right\}$.

---

#### CÂU 13 (2,0 ĐIỂM): HÌNH HỌC TỔNG HỢP (GÓC GÃY KHÚC & TIÊN ĐỀ EUCLID) - BÀI LÀM CHIA 2 CỘT

*(Khu vực làm bài: Chia 2 cột `\dongkeHaiCot{10}` có vách phân cách mờ ở giữa, học sinh vẽ hình hoặc làm ý a ở cột 1 và làm ý b ở cột 2)*

* **Mã đề 101:**
  Cho hai tia $Ax$ và $By$ song song với nhau ($Ax \parallel By$). Điểm $O$ nằm giữa hai đường thẳng chứa tia $Ax$ và $By$ sao cho tia $Ax$ và tia $By$ cùng nằm về một phía đối với đường thẳng $AB$. Biết $\widehat{xAO} = 40^\circ$ và $\widehat{yBO} = 50^\circ$.
  - a) (1,0 đ) Kẻ tia $Oz \parallel Ax$ (tia $Oz$ nằm trong góc $\widehat{AOB}$). Giải thích vì sao $Oz \parallel By$.
    - *Lời giải:*
      - Vì $Ax \parallel By$ (theo giả thiết) và $Oz \parallel Ax$ (theo cách vẽ). *(0,5đ)*
      - Theo tính chất ba đường thẳng song song (hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau), suy ra $Oz \parallel By$. *(0,5đ)*
  - b) (1,0 đ) Tính số đo góc $\widehat{AOB}$.
    - *Lời giải:*
      - Vì $Oz \parallel Ax$, nên $\widehat{AOz} = \widehat{xAO} = 40^\circ$ (hai góc so le trong). *(0,25đ)*
      - Vì $Oz \parallel By$, nên $\widehat{BOz} = \widehat{yBO} = 50^\circ$ (hai góc so le trong). *(0,25đ)*
      - Vì tia $Oz$ nằm trong góc $\widehat{AOB}$ nên:
        $$\widehat{AOB} = \widehat{AOz} + \widehat{BOz} = 40^\circ + 50^\circ = 90^\circ \quad (0{,}5\text{đ})$$

* **Mã đề 102:**
  Cho $Ax \parallel By$. Biết $\widehat{xAO} = 35^\circ$ và $\widehat{yBO} = 55^\circ$.
  - a) (1,0 đ) Kẻ $Oz \parallel Ax$. Vì $Ax \parallel By$ và $Oz \parallel Ax \implies Oz \parallel By$.
  - b) (1,0 đ) $\widehat{AOz} = \widehat{xAO} = 35^\circ$ (so le trong); $\widehat{BOz} = \widehat{yBO} = 55^\circ$ (so le trong). $\widehat{AOB} = 35^\circ + 55^\circ = 90^\circ$.

* **Mã đề 103:**
  Cho $Ax \parallel By$. Biết $\widehat{xAO} = 45^\circ$ và $\widehat{yBO} = 65^\circ$.
  - a) (1,0 đ) Kẻ $Oz \parallel Ax \implies Oz \parallel By$.
  - b) (1,0 đ) $\widehat{AOz} = 45^\circ$ (so le trong); $\widehat{BOz} = 65^\circ$ (so le trong). $\widehat{AOB} = 45^\circ + 65^\circ = 110^\circ$.

* **Mã đề 104:**
  Cho $Ax \parallel By$. Biết $\widehat{xAO} = 50^\circ$ và $\widehat{yBO} = 60^\circ$.
  - a) (1,0 đ) Kẻ $Oz \parallel Ax \implies Oz \parallel By$.
  - b) (1,0 đ) $\widehat{AOz} = 50^\circ$ (so le trong); $\widehat{BOz} = 60^\circ$ (so le trong). $\widehat{AOB} = 50^\circ + 60^\circ = 110^\circ$.

---

#### CÂU 14 (0,5 ĐIỂM): VẬN DỤNG CAO ĐIỂM 10 (BẤT ĐẲNG THỨC GIÁ TRỊ TUYỆT ĐỐI TÌM MIN) - BÀI LÀM CHIA 2 CỘT

*(Khu vực làm bài: Chia 2 cột `\dongkeHaiCot{6}` có vách phân cách mờ ở giữa)*

* **Mã đề 101:**
  Tìm giá trị nhỏ nhất của biểu thức: $A = \lvert x - 2026\rvert + \lvert x - 2\rvert$.
  - *Lời giải:*
    - Ta có: $A = \lvert 2026 - x\rvert + \lvert x - 2\rvert$.
    - Áp dụng bất đẳng thức $\lvert A\rvert + \lvert B\rvert \ge \lvert A + B\rvert$, ta có:
      $$A = \lvert 2026 - x\rvert + \lvert x - 2\rvert \ge \lvert (2026 - x) + (x - 2)\rvert = \lvert 2024\rvert = 2024 \quad (0{,}25\text{đ})$$
    - Dấu "$=$" xảy ra khi $(2026 - x)(x - 2) \ge 0 \iff 2 \le x \le 2026$.
    - Vậy giá trị nhỏ nhất của biểu thức $A$ là $2024$ khi $2 \le x \le 2026$. *(0,25đ)*

* **Mã đề 102:**
  Tìm giá trị nhỏ nhất của biểu thức: $A = \lvert x - 2025\rvert + \lvert x - 1\rvert$.
  - $A = \lvert 2025 - x\rvert + \lvert x - 1\rvert \ge \lvert 2025 - x + x - 1\rvert = 2024$.
  - Dấu "$=$" xảy ra khi $1 \le x \le 2025$. Vậy $\min A = 2024$ khi $1 \le x \le 2025$.

* **Mã đề 103:**
  Tìm giá trị nhỏ nhất của biểu thức: $A = \lvert x - 2026\rvert + \lvert x - 6\rvert$.
  - $A = \lvert 2026 - x\rvert + \lvert x - 6\rvert \ge \lvert 2026 - x + x - 6\rvert = 2020$.
  - Dấu "$=$" xảy ra khi $6 \le x \le 2026$. Vậy $\min A = 2020$ khi $6 \le x \le 2026$.

* **Mã đề 104:**
  Tìm giá trị nhỏ nhất của biểu thức: $A = \lvert x - 2024\rvert + \lvert x - 4\rvert$.
  - $A = \lvert 2024 - x\rvert + \lvert x - 4\rvert \ge \lvert 2024 - x + x - 4\rvert = 2020$.
  - Dấu "$=$" xảy ra khi $4 \le x \le 2024$. Vậy $\min A = 2020$ khi $4 \le x \le 2024$.
