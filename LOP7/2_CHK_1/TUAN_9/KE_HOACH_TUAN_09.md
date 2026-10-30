# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 09 (TOÁN 7)
## CHIẾN DỊCH 2_CHK_1: BÀI 12 - TỔNG CÁC GÓC TRONG MỘT TAM GIÁC
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)
### Bám sát chương trình: Toán 7 - Kết nối tri thức với cuộc sống (Chương IV)

---

## 🎯 I. MỤC TIÊU HỌC TẬP & NGUYÊN TẮC TINH GIẢN (TUẦN 9)

Tuần 9 là tuần mở đầu giai đoạn **Cuối Học Kỳ 1 (`2_CHK_1`)**, học sinh chính thức bước vào **Hình học phẳng thực thụ (Chương IV: Tam giác bằng nhau)**. Trọng tâm tuần 9 là chiếm lĩnh trọn vẹn **Bài 12: Tổng các góc trong một tam giác**:

### 1. Mục tiêu trọng tâm:
* **Buổi 01 - Định lí Tổng ba góc của tam giác & Tính chất góc nhọn tam giác vuông:**
  - Nắm vững định lí: Tổng ba góc trong một tam giác bằng $180^\circ$.
  - Vận dụng vào tam giác vuông: Hai góc nhọn của tam giác vuông phụ nhau (tổng bằng $90^\circ$).
  - Nhận biết tam giác nhọn, tam giác vuông, tam giác tù dựa vào số đo các góc.
  - Tính góc trong tam giác có đường cao, phân giác tạo thành các tam giác con lồng ghép.
  - Củng cố Đại số: Phép tính số hữu tỉ, lũy thừa, căn bậc hai số học, quy tắc chuyển vế và giá trị tuyệt đối.

* **Buổi 02 - Góc ngoài của tam giác & Ứng dụng thực tế hình học:**
  - Nắm vững định nghĩa và tính chất: Góc ngoài của một tam giác bằng tổng hai góc trong không kề với nó.
  - Nhận xét: Mỗi góc ngoài luôn lớn hơn từng góc trong không kề với nó.
  - Định lí mở rộng: Tổng ba góc ngoài tại ba đỉnh của tam giác luôn bằng $360^\circ$.
  - Bài toán kinh điển về tia phân giác: Góc tạo bởi 2 tia phân giác trong $\widehat{BIC} = 90^\circ + \dfrac{\widehat{A}}{2}$ và góc tạo bởi 2 tia phân giác ngoài $\widehat{BKC} = 90^\circ - \dfrac{\widehat{A}}{2}$.
  - Bài toán thực tế liên môn: Độ nghiêng mái nhà chữ A, góc thang dựa tường, giàn giáo xây dựng.

---

## 📐 II. QUY CHUẨN MA TRẬN ĐỀ THI (10 ĐIỂM / 45 PHÚT / 1 TỜ A4 IN 2 MẶT)

* **Hình thức:** Phiếu kiểm tra in 2 mặt A4, gồm **4 mã đề hoán vị tương đương ($101, 102, 103, 104$)**, biên dịch chính xác **8 trang PDF** (mỗi mã đề 2 trang).
* **Thang điểm 10 điểm (Chuẩn tối ưu mới - Lớp 7):**
  * **Câu 1 đến Câu 10 (2,5 điểm - Trang 1):** 10 câu trả lời ngắn dùng lệnh `\shortans`, mỗi câu $0{,}25$ điểm. Thiết kế 2 cột gọn gàng, có ô vuông bo góc `KQ: [   ]` sát mép phải.
  * **Câu 11 (3,0 điểm - Trang 1):** Thực hiện phép tính gồm **6 ý ($a, b, c, d, e, f$)**, mỗi ý $0{,}5$ điểm (bố trí bảng $3 \times 2$, dùng `\oBaiTap[5]` lấp kín 100% sát đáy Trang 1).
  * **Câu 12 (2,0 điểm - Trang 2):** Tìm số hữu tỉ $x$ gồm **4 ý ($a, b, c, d$)**, mỗi ý $0{,}5$ điểm (bố trí bảng $2 \times 2$, dùng `\oBaiTap[5]`).
  * **Câu 13 (2,0 điểm - Trang 2):** Bài toán hình học phẳng (2 ý $a, b$, mỗi ý $1{,}0$ điểm). Ghép đề bài + hình vẽ TikZ trực tiếp vào khung box `tabularx`, khu vực bài giải chia 2 cột `\dongkeHaiCot{10}` có vách phân cách mờ ở giữa.
  * **Câu 14 (0,5 điểm - Trang 2):** Bài toán vận dụng cao phân loại điểm 10. Ghép đề bài vào khung box `tabularx`, bài giải `\dongkeHaiCot{6}` chạm sát đáy Trang 2.

---

## 🗺️ III. MA TRẬN CHI TIẾT TỪNG BUỔI HỌC

### 📌 BUỔI 01: ĐỊNH LÍ TỔNG CÁC GÓC TRONG TAM GIÁC & GÓC NHỌN TAM GIÁC VUÔNG
* **Chi tiết file kế hoạch:** [buoi_1/KE_HOACH_TUAN_09_BUOI_01.md](buoi_1/KE_HOACH_TUAN_09_BUOI_01.md)
* **Câu 1 $\to$ 10 (2,5 đ):** 10 câu trả lời ngắn: Số đối số hữu tỉ, căn bậc hai số học, giá trị tuyệt đối, làm tròn số, định lí tổng ba góc $180^\circ$, tính góc thứ 3 khi biết 2 góc, tính góc nhọn còn lại trong tam giác vuông, tam giác có các góc theo tỉ lệ, nhận biết tam giác tù, bài toán thực tế góc thang dựa tường.
* **Câu 11 (3,0 đ - Trang 1): Thực hiện phép tính (6 ý $a \to f$, mỗi ý $0{,}5$đ):**
  * $a)$ Cộng trừ phân số hữu tỉ nhóm mẫu.
  * $b)$ Tính nhanh bằng tính chất phân phối $A \cdot B + A \cdot C$.
  * $c)$ Lũy thừa số hữu tỉ phối hợp số nguyên.
  * $d)$ Căn bậc hai số học phối hợp giá trị tuyệt đối.
  * $e)$ Thứ tự thực hiện phép tính có ngoặc vuông $[ \dots ]$.
  * $f)$ Rút gọn biểu thức lũy thừa đưa về cùng cơ số nguyên tố.
* **Câu 12 (2,0 đ - Trang 2): Tìm số hữu tỉ $x$ (4 ý $a \to d$, mỗi ý $0{,}5$đ):**
  * $a)$ Chuyển vế đổi dấu cơ bản.
  * $b)$ Nhân chia hai bước có phân số.
  * $c)$ Phương trình lũy thừa $\left(x \pm \dfrac{a}{b}\right)^2 = \dfrac{c^2}{d^2}$ (2 trường hợp).
  * $d)$ Phương trình chứa giá trị tuyệt đối $|ax \pm b| = c$ (2 trường hợp).
* **Câu 13 (2,0 đ - Trang 2): Bài toán Hình học về tam giác vuông và đường cao (Chia 2 cột `\dongkeHaiCot{10}`):**
  * $a)$ (1,0 đ): Tính các góc trong tam giác vuông khi biết một góc nhọn và đường cao $AH$.
  * $b)$ (1,0 đ): Kẻ tia phân giác $AD$ của góc $\widehat{HAC}$, chứng minh tam giác $ABD$ có hai góc bằng nhau $\widehat{BAD} = \widehat{BDA}$.
* **Câu 14 (0,5 đ - Trang 2): Vận dụng cao điểm 10 (Chia 2 cột `\dongkeHaiCot{6}`):**
  * Tìm giá trị nhỏ nhất của biểu thức chứa giá trị tuyệt đối: $A = |x - a| + |x - b|$ ($a > b$) áp dụng BĐT $|A| + |B| \ge |A + B|$.

---

### 📌 BUỔI 02: GÓC NGOÀI CỦA TAM GIÁC & ỨNG DỤNG THỰC TẾ
* **Chi tiết file kế hoạch:** [buoi_2/KE_HOACH_TUAN_09_BUOI_02.md](buoi_2/KE_HOACH_TUAN_09_BUOI_02.md)
* **Câu 1 $\to$ 10 (2,5 đ):** 10 câu trả lời ngắn: Số đối, căn bậc hai số học, giá trị tuyệt đối, định nghĩa tính chất góc ngoài, tính số đo góc ngoài khi biết 2 góc trong không kề, tìm góc trong khi biết góc ngoài, tổng 3 góc ngoài bằng $360^\circ$, góc ngoài tam giác vuông, góc tạo bởi hai tia phân giác trong $\widehat{BIC} = 90^\circ + \dfrac{\widehat{A}}{2}$, bài toán thực tế góc mái nhà.
* **Câu 11 (3,0 đ - Trang 1): Thực hiện phép tính (6 ý $a \to f$, mỗi ý $0{,}5$đ):**
  * Phép tính số hữu tỉ kết hợp phân số, số thập phân, lũy thừa, căn bậc hai số học và thứ tự ngoặc lồng nhau.
* **Câu 12 (2,0 đ - Trang 2): Tìm số hữu tỉ $x$ (4 ý $a \to d$, mỗi ý $0{,}5$đ):**
  * 4 dạng toán tìm $x$ chuẩn mực: chuyển vế, nhân chia, lũy thừa bậc hai, giá trị tuyệt đối.
* **Câu 13 (2,0 đ - Trang 2): Bài toán Hình học về góc ngoài và tia phân giác (Chia 2 cột `\dongkeHaiCot{10}`):**
  * $a)$ (1,0 đ): Cho $\Delta ABC$ có $\widehat{A} = \alpha$. Tính góc tạo bởi hai tia phân giác trong $\widehat{BIC} = 90^\circ + \dfrac{\alpha}{2}$.
  * $b)$ (1,0 đ): Tính góc tạo bởi hai tia phân giác ngoài $\widehat{BKC} = 90^\circ - \dfrac{\alpha}{2}$.
* **Câu 14 (0,5 đ - Trang 2): Vận dụng cao điểm 10 (Chia 2 cột `\dongkeHaiCot{6}`):**
  * Tìm giá trị lớn nhất của phân thức có mẫu chứa giá trị tuyệt đối: $B = \dfrac{m}{|x - a| + n}$ ($m, n > 0$).

---

## 📐 IV. BẢNG THAM CHIẾU QUY CHUẨN KỸ THUẬT IN ẤN (LAYOUT GOLD STANDARD)

| Vị trí | Quy cách kỹ thuật tối ưu mới | Tác dụng thẩm mỹ & Sư phạm |
| :--- | :--- | :--- |
| **Header Trang 1** | Bảng 1 dòng duy nhất: `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 09 - BUỔI <Y>` \| `Mã đề: <MÃ> - Trang 1/2` | Tiết kiệm diện tích, bỏ hoàn toàn khung họ tên rườm rà. |
| **Khung Điểm số** | Bảng Điểm & Nhận xét cao cố định `\rule{0pt}{1.8cm}` | Rộng rãi, trang trọng, thuận tiện ghi lời phê. |
| **10 Câu ngắn** | Dùng lệnh `\shortans{...}` với cấu hình `\SAOPTN{widthSA=2.8,heightSA=0.62}` | Bỏ bảng trắc nghiệm A, B, C, D; sinh ô `KQ: [   ]` bo góc tinh tế mép phải. |
| **Câu 11 (Trang 1)** | Bảng $3 \times 2$ gồm **6 ý ($a \to f$)** với **`\oBaiTap[5]`** (5 dòng kẻ mờ/ô) | Auto-fill lấp kín 100% sát đáy Trang 1 (3,0 điểm). |
| **Header Trang 2** | Khung rút gọn: `TOÁN 7 - TUẦN 09 - BUỔI <Y> \| Mã đề: <MÃ> - Trang 2/2` | Đồng bộ nhận diện đề thi mặt sau. |
| **Câu 12 (Trang 2)** | Bảng $2 \times 2$ gồm **4 ý ($a \to d$)** với **`\oBaiTap[5]`** | Trình bày 4 phương trình tìm $x$ rõ ràng, mạch lạc (2,0 điểm). |
| **Câu 13 (Trang 2)** | Ghép đề bài + hình TikZ vào box `tabularx`, bài giải **`\dongkeHaiCot{10}`** | Chia đôi cột làm bài, nhân đôi không gian trình bày hình học (2,0 điểm). |
| **Câu 14 (Trang 2)** | Ghép đề bài vào box `tabularx`, bài giải **`\dongkeHaiCot{6}`** | Chạm sát mép lề dưới Trang 2, tuyệt đối không tràn (0,5 điểm). |

