# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ
## TOÁN 9 - TUẦN 08 - BUỔI 01
### CHỦ ĐỀ: MỘT SỐ HỆ THỨC GIỮA CẠNH VÀ GÓC TRONG TAM GIÁC VUÔNG
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. QUY CHUẨN ĐẶC BIỆT & BỐ CỤC TỐI ƯU MỚI (CHUẨN LỚP 9)

Theo yêu cầu chuẩn hóa cấu trúc đề kiểm tra:
1. **Header đỉnh trang siêu tối giản:**
   - Trang 1: `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 08 - BUỔI 01` và `Mã đề: <MÃ> - Trang 1/2`.
   - Trang 2: `TOÁN 9 - TUẦN 08 - BUỔI 01 | Mã đề: <MÃ> - Trang 2/2`.
   - Bỏ hoàn toàn dòng ghi chủ đề, thời gian; bỏ khung riêng họ tên (học sinh tự ghi tên lên lề trên cùng của giấy).
2. **Bảng Điểm số & Lời nhận xét:** Bắt buộc chiều cao `\rule{0pt}{1.8cm}`.
3. **Phần Trả lời ngắn (Câu 1 đến Câu 10 - 2,5 điểm):**
   - Cấu hình preamble: `\SAOPTN{widthSA=3.2,heightSA=0.62}`.
   - Mỗi câu có ô `\shortans{...}` bo góc mép phải câu hỏi.
   - Trọng tâm: Hệ thức cạnh góc vuông theo góc và cạnh huyền ($b = a \cdot \sin B$), cạnh góc vuông theo cos góc kề ($c = a \cdot \cos B$), cạnh góc vuông theo tan ($b = c \cdot \tan B$), giá trị lượng giác góc đặc biệt ($30^\circ, 45^\circ, 60^\circ$), tỉ số hai góc phụ nhau, góc nâng Mặt Trời, bài toán chiếc thang dựa tường, nghiệm hệ phương trình và nghiệm dương phương trình tích.
4. **Câu 11 (Trang 1 - 2,5 điểm):** Chia thành 2 ý:
   - **Ý a) (1,25 điểm):** Giải hệ phương trình bậc nhất hai ẩn (cộng đại số / thế).
   - **Ý b) (1,25 điểm):** Rút gọn biểu thức phân thức chứa căn bậc hai.
   - Trình bày dạng bảng $1 \times 2$ (chia 2 cột), mỗi cột `\oBaiTap[22]` $\to$ vừa vặn chạm sát đáy Trang 1.
5. **Câu 12 (Trang 2 - 2,5 điểm):** Giải bài toán bằng cách lập hệ phương trình (Toán thực tế năng suất / thi đua vượt mức kế hoạch chuẩn form đề tuyển sinh 10).
   - Đóng khung box liền mạch `tabularx`, bài giải `\dongke{16}` (hoặc chia 2 cột `\dongkeHaiCot{16}`) $\to$ đủ không gian trình bày đầy đủ các bước.
6. **Câu 13 (Trang 2 - 2,5 điểm):** Hệ thức giữa cạnh và góc trong tam giác vuông:
   - **Ý a) (1,5 điểm):** Giải tam giác vuông (biết 1 cạnh huyền và 1 góc nhọn đặc biệt $30^\circ$ hoặc $60^\circ$, tính cạnh góc vuông, góc còn lại và đường cao $AH$).
   - **Ý b) (1,0 điểm):** Kẻ đường cao, đường vuông góc và chứng minh hình chữ nhật / đẳng thức hình học lượng giác ($AD \cdot AB = AE \cdot AC$ hoặc $DE = AH$).
   - Đóng khung box liền mạch `tabularx`, bài giải `\dongke{17}` (hoặc chia 2 cột `\dongkeHaiCot{16}`) $\to$ vừa vặn chạm sát đáy Trang 2.
7. **Kiểm soát số trang:** Trọn vẹn 4 mã đề hoán vị ($101, 102, 103, 104$) trong file `.tex` $\rightarrow$ Biên dịch chính xác **8 trang PDF** (mỗi mã đề đúng 2 mặt A4).

---

## 📐 II. MA TRẬN THANG ĐIỂM (TỔNG 10,0 ĐIỂM)

| Câu | Thể loại | Nội dung kiến thức kiểm tra | Điểm | Định dạng LaTeX |
| :---: | :---: | :--- | :---: | :--- |
| **Câu 1 $\to$ 10** | **Trả lời ngắn** | 1. Cạnh góc vuông theo cạnh huyền và góc đối: $b = a \cdot \sin B$<br>2. Cạnh góc vuông theo cạnh huyền và góc kề: $c = a \cdot \cos B$<br>3. Cạnh góc vuông theo cạnh góc vuông kia và $\tan 45^\circ$: $b = c \cdot \tan 45^\circ$<br>4. Cạnh góc vuông theo cạnh góc vuông kia và $\tan 30^\circ$: $b = c \cdot \tan 30^\circ$<br>5. Mối quan hệ lượng giác hai góc phụ nhau: $\sin(90^\circ - \alpha) = \cos \alpha$<br>6. Tính giá trị biểu thức lượng giác góc đặc biệt ($30^\circ, 60^\circ$)<br>7. Bài toán thực tế góc nâng Mặt Trời qua bóng cột cờ/tòa nhà<br>8. Bài toán thực tế khoảng cách chân thang dựa tường nghiêng $60^\circ$<br>9. Tìm nghiệm của hệ hai phương trình bậc nhất hai ẩn<br>10. Nghiệm dương của phương trình tích $(x - a)(x + b) = 0$ | **2,5 đ**<br>*(0,25 đ/câu)* | Dùng `\shortans{...}`, ô kết quả bo góc mép phải |
| **Câu 11** | **Tự luận (Trang 1)** | **Đại số tổng hợp (2 ý):**<br>- a) (1,25 đ) Giải hệ hai phương trình bậc nhất hai ẩn<br>- b) (1,25 đ) Rút gọn biểu thức phân thức chứa căn bậc hai | **2,5 đ** | Bảng $1 \times 2$ (chia 2 cột), mỗi cột `\oBaiTap[22]` $\to$ kín mép đáy Trang 1 |
| **Câu 12** | **Tự luận (Trang 2)** | **Toán thực tế giải bằng cách lập hệ phương trình:**<br>Bài toán năng suất công việc / vượt mức kế hoạch theo phần trăm. Đặt 2 ẩn, lập hệ 2 phương trình bậc nhất hai ẩn, giải và kết luận. | **2,5 đ** | Khung bảng đóng hộp `tabularx`, bài giải `\dongke{16}` |
| **Câu 13** | **Tự luận (Trang 2)** | **Hình học: Hệ thức giữa cạnh và góc trong tam giác vuông:**<br>- a) (1,5 đ) Giải tam giác vuông khi biết cạnh huyền và góc nhọn ($30^\circ$ hoặc $60^\circ$), tính cạnh, góc và đường cao $AH$<br>- b) (1,0 đ) Chứng minh tứ giác hình chữ nhật và suy ra hai đoạn thẳng bằng nhau ($DE = AH$) hoặc chứng minh hệ thức lượng $AD \cdot AB = AE \cdot AC$ | **2,5 đ** | Khung bảng đóng hộp `tabularx`, bài giải `\dongke{17}` $\to$ kín mép đáy Trang 2 |

---

## 🔢 III. BẢNG DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ TƯƠNG ĐƯƠNG (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiểm tra | Mã 101 | Mã 102 | Mã 103 | Mã 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Cạnh theo $\sin B$ | $\Delta ABC$ vuông tại $A$ ($BC = 10\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{5\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($BC = 12\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{6\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($BC = 16\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{8\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($BC = 14\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{7\text{ cm}}$ |
| **2** | Cạnh theo $\cos B$ | $\Delta ABC$ vuông tại $A$ ($BC = 8\text{ cm}, \widehat{B} = 60^\circ$). $AB = \mathbf{4\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($BC = 10\text{ cm}, \widehat{B} = 60^\circ$). $AB = \mathbf{5\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($BC = 6\text{ cm}, \widehat{B} = 60^\circ$). $AB = \mathbf{3\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($BC = 14\text{ cm}, \widehat{B} = 60^\circ$). $AB = \mathbf{7\text{ cm}}$ |
| **3** | Cạnh theo $\tan 45^\circ$ | $\Delta ABC$ vuông tại $A$ ($AB = 6\text{ cm}, \widehat{B} = 45^\circ$). $AC = \mathbf{6\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($AB = 8\text{ cm}, \widehat{B} = 45^\circ$). $AC = \mathbf{8\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($AB = 5\text{ cm}, \widehat{B} = 45^\circ$). $AC = \mathbf{5\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($AB = 9\text{ cm}, \widehat{B} = 45^\circ$). $AC = \mathbf{9\text{ cm}}$ |
| **4** | Cạnh theo $\tan 30^\circ$ | $\Delta ABC$ vuông tại $A$ ($AB = 3\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{3\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($AB = 4\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{4\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($AB = 5\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{5\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($AB = 2\sqrt{3}\text{ cm}, \widehat{B} = 30^\circ$). $AC = \mathbf{2\text{ cm}}$ |
| **5** | Góc phụ nhau | Cho góc nhọn $\alpha$ có $\cos \alpha = 0{,}8$. Khi đó $\sin(90^\circ - \alpha) = \mathbf{0{,}8}$ | Cho góc nhọn $\alpha$ có $\sin \alpha = 0{,}6$. Khi đó $\cos(90^\circ - \alpha) = \mathbf{0{,}6}$ | Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{5}{13}$. Khi đó $\sin(90^\circ - \alpha) = \mathbf{\dfrac{5}{13}}$ | Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{12}{13}$. Khi đó $\cos(90^\circ - \alpha) = \mathbf{\dfrac{12}{13}}$ |
| **6** | Góc đặc biệt | Giá trị của $P = 2\sin 30^\circ + \sqrt{3}\tan 60^\circ$ bằng: $\mathbf{4}$ | Giá trị của $P = 2\cos 60^\circ + \sqrt{3}\cot 30^\circ$ bằng: $\mathbf{4}$ | Giá trị của $P = 4\sin 30^\circ - \tan 45^\circ$ bằng: $\mathbf{1}$ | Giá trị của $P = 2\cos 60^\circ + \tan 45^\circ$ bằng: $\mathbf{2}$ |
| **7** | Góc nâng Mặt Trời | Tòa nhà cao $20\text{ m}$, bóng dài $20\text{ m}$. Góc nâng của Mặt Trời là: $\mathbf{45^\circ}$ | Cột cờ cao $15\text{ m}$, bóng dài $15\text{ m}$. Góc nâng của Mặt Trời là: $\mathbf{45^\circ}$ | Ngọn hải đăng cao $30\text{ m}$, bóng dài $30\text{ m}$. Góc nâng là: $\mathbf{45^\circ}$ | Cây cau cao $12\text{ m}$, bóng dài $12\text{ m}$. Góc của tia nắng là: $\mathbf{45^\circ}$ |
| **8** | Chiếc thang dựa tường | Thang dài $4\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{2\text{ m}}$ | Thang dài $6\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{3\text{ m}}$ | Thang dài $5\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{2{,}5\text{ m}}$ | Thang dài $8\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{4\text{ m}}$ |
| **9** | Nghiệm hệ phương trình | Nghiệm của $\begin{cases} x + y = 7 \\ x - y = 3 \end{cases}$ là $(x; y) = \mathbf{(5; 2)}$ | Nghiệm của $\begin{cases} x + y = 8 \\ x - y = 2 \end{cases}$ là $(x; y) = \mathbf{(5; 3)}$ | Nghiệm của $\begin{cases} x + y = 9 \\ x - y = 1 \end{cases}$ là $(x; y) = \mathbf{(5; 4)}$ | Nghiệm của $\begin{cases} x + y = 6 \\ x - y = 4 \end{cases}$ là $(x; y) = \mathbf{(5; 1)}$ |
| **10** | Phương trình tích | Nghiệm dương của $(x - 6)(x + 2) = 0$ là: $\mathbf{6}$ | Nghiệm dương của $(x - 7)(x + 3) = 0$ là: $\mathbf{7}$ | Nghiệm dương của $(x - 8)(x + 1) = 0$ là: $\mathbf{8}$ | Nghiệm dương của $(x - 9)(x + 4) = 0$ là: $\mathbf{9}$ |

---

### 2. PHẦN TỰ LUẬN (CÂU 11 ĐẾN CÂU 13 - TỔNG CỘNG 7,5 ĐIỂM)

#### CÂU 11 (2,5 ĐIỂM): ĐẠI SỐ TỔNG HỢP (HỆ PHƯƠNG TRÌNH & RÚT GỌN CĂN THỨC)

* **Mã đề 101:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 2x + y = 7 \\ 3x - y = 8 \end{cases}$.
    - *Lời giải:* Cộng từng vế của hai phương trình ta được: $5x = 15 \Leftrightarrow x = 3$. *(0,5đ)*
    - Thay $x = 3$ vào phương trình $2x + y = 7$ ta được: $2 \cdot 3 + y = 7 \Leftrightarrow y = 1$. *(0,5đ)*
    - Vậy nghiệm của hệ phương trình là $(x; y) = (3; 1)$. *(0,25đ)*
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 4$:
    $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+2} + \dfrac{4\sqrt{x}}{x-4}\right) : \dfrac{\sqrt{x}+2}{x-4}$.
    - *Lời giải:* Với $x > 0, x \ne 4$:
      $P = \left(\dfrac{\sqrt{x}(\sqrt{x}-2) + 4\sqrt{x}}{(\sqrt{x}-2)(\sqrt{x}+2)}\right) \cdot \dfrac{x-4}{\sqrt{x}+2}$ *(0,5đ)*
      $= \dfrac{x - 2\sqrt{x} + 4\sqrt{x}}{x-4} \cdot \dfrac{x-4}{\sqrt{x}+2} = \dfrac{x + 2\sqrt{x}}{\sqrt{x}+2}$ *(0,5đ)*
      $= \dfrac{\sqrt{x}(\sqrt{x}+2)}{\sqrt{x}+2} = \sqrt{x}$. *(0,25đ)*

* **Mã đề 102:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 3x + y = 10 \\ 2x - y = 5 \end{cases} \Leftrightarrow \begin{cases} 5x = 15 \\ y = 10 - 3x \end{cases} \Leftrightarrow \begin{cases} x = 3 \\ y = 1 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 9$:
    $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+3} + \dfrac{6\sqrt{x}}{x-9}\right) : \dfrac{\sqrt{x}+3}{x-9} = \dfrac{x + 3\sqrt{x}}{\sqrt{x}+3} = \sqrt{x}$.

* **Mã đề 103:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 2x - y = 5 \\ x + y = 4 \end{cases} \Leftrightarrow \begin{cases} 3x = 9 \\ y = 4 - x \end{cases} \Leftrightarrow \begin{cases} x = 3 \\ y = 1 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 1$:
    $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+1} + \dfrac{2\sqrt{x}}{x-1}\right) : \dfrac{\sqrt{x}+1}{x-1} = \dfrac{x + \sqrt{x}}{\sqrt{x}+1} = \sqrt{x}$.

* **Mã đề 104:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} x + 2y = 8 \\ 3x - 2y = 4 \end{cases} \Leftrightarrow \begin{cases} 4x = 12 \\ 2y = 8 - x \end{cases} \Leftrightarrow \begin{cases} x = 3 \\ y = 2 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 16$:
    $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}+4} + \dfrac{8\sqrt{x}}{x-16}\right) : \dfrac{\sqrt{x}+4}{x-16} = \dfrac{x + 4\sqrt{x}}{\sqrt{x}+4} = \sqrt{x}$.

---

#### CÂU 12 (2,5 ĐIỂM): TOÁN NĂNG SUẤT THI ĐUA VƯỢT MỨC (HỆ PHƯƠNG TRÌNH)

* **Mã đề 101:**
  Theo kế hoạch, hai tổ sản xuất phải làm được tổng cộng $700$ sản phẩm. Nhờ cải tiến kỹ thuật, tổ I đã làm vượt mức kế hoạch $15\%$, tổ II đã làm vượt mức kế hoạch $20\%$, do đó cả hai tổ đã làm được $820$ sản phẩm. Hỏi theo kế hoạch, mỗi tổ phải sản xuất bao nhiêu sản phẩm?
  - *Lời giải:*
    - Gọi số sản phẩm tổ I phải làm theo kế hoạch là $x$ (sản phẩm), tổ II là $y$ (sản phẩm) ($x, y \in \mathbb{N}^*, x, y < 700$). *(0,5đ)*
    - Hai tổ theo kế hoạch phải làm $700$ sản phẩm nên ta có phương trình: $x + y = 700$. *(0,5đ)*
    - Thực tế, tổ I làm được $115\%x = 1{,}15x$ sản phẩm; tổ II làm được $120\%y = 1{,}20y$ sản phẩm. Cả hai tổ làm được $820$ sản phẩm nên ta có phương trình: $1{,}15x + 1{,}20y = 820$. *(0,5đ)*
    - Ta có hệ phương trình: $\begin{cases} x + y = 700 \\ 1{,}15x + 1{,}20y = 820 \end{cases} \Leftrightarrow \begin{cases} 1{,}15x + 1{,}15y = 805 \\ 1{,}15x + 1{,}20y = 820 \end{cases} \Leftrightarrow \begin{cases} 0{,}05y = 15 \\ x = 700 - y \end{cases} \Leftrightarrow \begin{cases} y = 300 \\ x = 400 \end{cases}$ (thỏa mãn ĐK). *(0,75đ)*
    - Kết luận: Theo kế hoạch, tổ I phải làm $400$ sản phẩm; tổ II phải làm $300$ sản phẩm. *(0,25đ)*

* **Mã đề 102:**
  Theo kế hoạch, hai tổ công nhân dự định dệt tổng cộng $800$ chiếc áo len. Do thi đua, tổ I dệt vượt mức $20\%$, tổ II dệt vượt mức $15\%$, nên cả hai tổ đã dệt được $945$ chiếc áo len. Hỏi theo kế hoạch, mỗi tổ dự định dệt bao nhiêu chiếc áo len?
  - *Hệ phương trình:* $\begin{cases} x + y = 800 \\ 1{,}20x + 1{,}15y = 945 \end{cases} \Leftrightarrow \begin{cases} 0{,}05x = 25 \\ y = 800 - x \end{cases} \Leftrightarrow \begin{cases} x = 500 \\ y = 300 \end{cases}$ (chiếc áo).

* **Mã đề 103:**
  Theo kế hoạch, hai xưởng cơ khí phải đúc tổng cộng $600$ chi tiết máy. Khi thực hiện, xưởng I vượt mức $10\%$, xưởng II vượt mức $15\%$, vì thế cả hai xưởng đúc được $675$ chi tiết máy. Hỏi theo kế hoạch, mỗi xưởng phải đúc bao nhiêu chi tiết máy?
  - *Hệ phương trình:* $\begin{cases} x + y = 600 \\ 1{,}10x + 1{,}15y = 675 \end{cases} \Leftrightarrow \begin{cases} 0{,}05y = 15 \\ x = 600 - y \end{cases} \Leftrightarrow \begin{cases} x = 300 \\ y = 300 \end{cases}$ (chi tiết máy).

* **Mã đề 104:**
  Theo kế hoạch, hai lớp $9A$ và $9B$ dự định thu gom tổng cộng $500\text{ kg}$ giấy vụn. Thực tế, lớp $9A$ vượt mức $15\%$, lớp $9B$ vượt mức $10\%$, nên cả hai lớp thu gom được $560\text{ kg}$ giấy vụn. Hỏi theo kế hoạch, mỗi lớp dự định thu gom bao nhiêu ki-lô-gam giấy vụn?
  - *Hệ phương trình:* $\begin{cases} x + y = 500 \\ 1{,}15x + 1{,}10y = 560 \end{cases} \Leftrightarrow \begin{cases} 0{,}05x = 10 \\ y = 500 - x \end{cases} \Leftrightarrow \begin{cases} x = 200 \\ y = 300 \end{cases}$ (kg giấy).

---

#### CÂU 13 (2,5 ĐIỂM): HỆ THỨC GIỮA CẠNH VÀ GÓC TRONG TAM GIÁC VUÔNG

* **Mã đề 101:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 8\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).
  - a) (1,5 điểm) Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.
    - *Lời giải:*
      - Số đo góc $C$: $\widehat{C} = 90^\circ - \widehat{B} = 90^\circ - 60^\circ = 30^\circ$. *(0,25đ)*
      - Trong tam giác $ABC$ vuông tại $A$:
        $AB = BC \cdot \cos B = 8 \cdot \cos 60^\circ = 8 \cdot \dfrac{1}{2} = 4\text{ cm}$. *(0,5đ)*
        $AC = BC \cdot \sin B = 8 \cdot \sin 60^\circ = 8 \cdot \dfrac{\sqrt{3}}{2} = 4\sqrt{3}\text{ cm}$. *(0,5đ)*
      - Đường cao $AH$:
        $AH = \dfrac{AB \cdot AC}{BC} = \dfrac{4 \cdot 4\sqrt{3}}{8} = 2\sqrt{3}\text{ cm}$. *(0,25đ)*
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$.
    - *Lời giải:*
      - Tứ giác $ADHE$ có: $\widehat{DAE} = 90^\circ$ (do $\Delta ABC$ vuông tại $A$), $\widehat{ADH} = 90^\circ$ ($HD \perp AB$), $\widehat{AEH} = 90^\circ$ ($HE \perp AC$). *(0,5đ)*
      - Do đó $ADHE$ là hình chữ nhật (tứ giác có 3 góc vuông). *(0,25đ)*
      - Suy ra hai đường chéo bằng nhau: $DE = AH$ (đpcm). *(0,25đ)*

* **Mã đề 102:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 10\text{ cm}$. Kẻ đường cao $AH$.
  - a) (1,5 điểm) Tính $\widehat{C} = 60^\circ$; $AC = 10 \cdot \sin 30^\circ = 5\text{ cm}$; $AB = 10 \cdot \cos 30^\circ = 5\sqrt{3}\text{ cm}$; $AH = \dfrac{5 \cdot 5\sqrt{3}}{10} = \dfrac{5\sqrt{3}}{2}\text{ cm}$.
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh $AD \cdot AB = AE \cdot AC$.
    - *Lời giải:* Trong $\Delta ABH$ vuông tại $H$: $AD \cdot AB = AH^2$. Trong $\Delta ACH$ vuông tại $H$: $AE \cdot AC = AH^2$. Suy ra $AD \cdot AB = AE \cdot AC = AH^2$.

* **Mã đề 103:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 12\text{ cm}$. Kẻ đường cao $AH$.
  - a) (1,5 điểm) Tính $\widehat{C} = 30^\circ$; $AB = 12 \cdot \cos 60^\circ = 6\text{ cm}$; $AC = 12 \cdot \sin 60^\circ = 6\sqrt{3}\text{ cm}$; $AH = \dfrac{6 \cdot 6\sqrt{3}}{12} = 3\sqrt{3}\text{ cm}$.
  - b) (1,0 điểm) Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$.

* **Mã đề 104:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 14\text{ cm}$. Kẻ đường cao $AH$.
  - a) (1,5 điểm) Tính $\widehat{C} = 60^\circ$; $AC = 14 \cdot \sin 30^\circ = 7\text{ cm}$; $AB = 14 \cdot \cos 30^\circ = 7\sqrt{3}\text{ cm}$; $AH = \dfrac{7 \cdot 7\sqrt{3}}{14} = \dfrac{7\sqrt{3}}{2}\text{ cm}$.
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh $AD \cdot AB = AE \cdot AC = AH^2$.
