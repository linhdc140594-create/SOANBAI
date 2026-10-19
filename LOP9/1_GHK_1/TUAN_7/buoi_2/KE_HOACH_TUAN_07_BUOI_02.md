# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ
## TOÁN 9 - TUẦN 07 - BUỔI 02
### CHỦ ĐỀ: TỔNG HỢP ÔN TẬP GHK1 - ĐẠI SỐ & HÌNH HỌC LƯỢNG GIÁC (BUỔI 2)
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. QUY CHUẨN ĐẶC BIỆT & BỐ CỤC TỐI ƯU MỚI (CHUẨN LỚP 9)

Theo yêu cầu chuẩn hóa cấu trúc đề kiểm tra:
1. **Header đỉnh trang siêu tối giản:**
   - Trang 1: `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 7 - BUỔI 2` và `Mã đề: <MÃ> - Trang 1/2`.
   - Trang 2: `TOÁN 9 - TUẦN 7 - BUỔI 2 | Mã đề: <MÃ> - Trang 2/2`.
   - Bỏ hoàn toàn dòng ghi chủ đề, thời gian; bỏ khung riêng họ tên (học sinh tự ghi tên lên lề trên cùng của giấy).
2. **Bảng Điểm số & Lời nhận xét:** Bắt buộc chiều cao `\rule{0pt}{1.8cm}`.
3. **Phần Trả lời ngắn (Câu 1 đến Câu 10 - 2,5 điểm):**
   - Cấu hình preamble: `\SAOPTN{widthSA=3.2,heightSA=0.62}`.
   - Mỗi câu có ô `\shortans{...}` bo góc mép phải câu hỏi.
   - Trọng tâm: Cạnh và góc tam giác vuông, hệ thức lượng đường cao, hằng đẳng thức căn bậc hai, ĐKXĐ căn thức, khai phương thương, phương trình căn thức, thực tế lượng giác thang dựa tường, nghiệm hệ PT và tổng lượng giác phụ nhau.
4. **Câu 11 (Trang 1 - 2,5 điểm):** Chia thành 2 ý:
   - **Ý a) (1,25 điểm):** Giải hệ phương trình bậc nhất hai ẩn.
   - **Ý b) (1,25 điểm):** Rút gọn biểu thức chứa căn bậc hai.
   - Trình bày dạng bảng $1 \times 2$ (chia 2 cột), mỗi cột `\oBaiTap[8]` $\to$ vừa vặn chạm sát đáy Trang 1.
5. **Câu 12 (Trang 2 - 2,5 điểm):** Giải bài toán bằng cách lập hệ phương trình (Toán thực tế chuyển động hai xe đi ngược chiều gặp nhau).
   - Đóng khung box liền mạch kèm `\dongke{12}` $\to$ đủ không gian trình bày 4 bước chuẩn mực.
6. **Câu 13 (Trang 2 - 2,5 điểm):** Giải tam giác vuông và chứng minh đẳng thức:
   - **Ý a) (1,5 điểm):** Giải tam giác vuông (biết 1 cạnh huyền và góc nhọn $30^\circ$ hoặc $60^\circ$, tính các cạnh, góc còn lại và đường cao $AH$).
   - **Ý b) (1,0 điểm):** Chứng minh đẳng thức hình học lượng giác ($AD \cdot AB = AE \cdot AC$ hoặc $DE = AH$).
   - Đóng khung box liền mạch kèm `\dongke{12}` $\to$ vừa vặn chạm sát đáy Trang 2.
7. **Kiểm soát số trang:** Trọn vẹn 4 mã đề hoán vị ($101, 102, 103, 104$) trong file `.tex` $\rightarrow$ Biên dịch chính xác **8 trang PDF** (mỗi mã đề đúng 2 mặt A4).

---

## 📐 II. MA TRẬN THANG ĐIỂM (TỔNG 10,0 ĐIỂM)

| Câu | Thể loại | Nội dung kiến thức kiểm tra | Điểm | Định dạng LaTeX |
| :---: | :---: | :--- | :---: | :--- |
| **Câu 1 $\to$ 10** | **Trả lời ngắn** | 1. Tam giác vuông có góc $30^\circ$, tính cạnh đối diện góc $30^\circ$<br>2. Cho $\sin\alpha$, tính $\cos\alpha$ qua $\sin^2\alpha + \cos^2\alpha = 1$<br>3. Hệ thức lượng tam giác vuông: $AH = \sqrt{BH \cdot CH}$<br>4. Rút gọn hằng đẳng thức $\sqrt{(a - \sqrt{b})^2}$ với $a < \sqrt{b}$<br>5. Tìm ĐKXĐ của biểu thức chứa căn thức $\sqrt{ax - b}$<br>6. Khai phương một thương $\sqrt{A} : \sqrt{B}$ và căn số học<br>7. Giải phương trình chứa căn cơ bản $\sqrt{ax + b} = c$<br>8. Thực tế góc nghiêng chiếc thang dựa tường<br>9. Tìm nghiệm của hệ phương trình bậc nhất hai ẩn<br>10. Tính tổng các tỉ số lượng giác phụ nhau: $\sin^2 10^\circ + \dots + \sin^2 80^\circ$ | **2,5 đ**<br>*(0,25 đ/câu)* | Dùng `\shortans{...}`, ô kết quả bo góc mép phải |
| **Câu 11** | **Tự luận (Trang 1)** | **Đại số tổng hợp (2 ý):**<br>- a) (1,25 đ) Giải hệ hai phương trình bậc nhất hai ẩn<br>- b) (1,25 đ) Rút gọn biểu thức phân thức chứa căn bậc hai | **2,5 đ** | Bảng $1 \times 2$ (chia 2 cột), mỗi cột `\oBaiTap[8]` $\to$ kín mép đáy Trang 1 |
| **Câu 12** | **Tự luận (Trang 2)** | **Toán thực tế giải bằng cách lập hệ phương trình:**<br>Bài toán chuyển động ngược chiều của 2 xe khởi hành từ 2 địa điểm $A$ và $B$. Học sinh đặt ẩn, lập hệ 2 phương trình, giải hệ và kết luận. | **2,5 đ** | Khung bảng đóng hộp `tabularx`, bài giải `\dongke{12}` |
| **Câu 13** | **Tự luận (Trang 2)** | **Hình học: Giải tam giác vuông & Chứng minh đẳng thức:**<br>- a) (1,5 đ) Giải tam giác vuông: Tính cạnh, góc và đường cao $AH$<br>- b) (1,0 đ) Chứng minh đẳng thức hình học lượng giác ($AD \cdot AB = AE \cdot AC$ hoặc $DE = AH$) | **2,5 đ** | Khung bảng đóng hộp `tabularx`, bài giải `\dongke{12}` $\to$ kín mép đáy Trang 2 |

---

## 🔢 III. BẢNG DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ TƯƠNG ĐƯƠNG (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiểm tra | Mã 101 | Mã 102 | Mã 103 | Mã 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Cạnh trong tam giác vuông | $\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=12$). Cạnh $AC = \mathbf{6\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=16$). Cạnh $AC = \mathbf{8\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=14$). Cạnh $AC = \mathbf{7\text{ cm}}$ | $\Delta ABC$ vuông tại $A$ ($\widehat{B}=30^\circ, BC=18$). Cạnh $AC = \mathbf{9\text{ cm}}$ |
| **2** | $\sin^2\alpha + \cos^2\alpha = 1$ | Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{3}{5}$. Khi đó $\cos \alpha = \mathbf{\dfrac{4}{5}}$ | Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{3}{5}$. Khi đó $\sin \alpha = \mathbf{\dfrac{4}{5}}$ | Cho góc nhọn $\alpha$ có $\sin \alpha = \dfrac{5}{13}$. Khi đó $\cos \alpha = \mathbf{\dfrac{12}{13}}$ | Cho góc nhọn $\alpha$ có $\cos \alpha = \dfrac{5}{13}$. Khi đó $\sin \alpha = \mathbf{\dfrac{12}{13}}$ |
| **3** | Hệ thức lượng đường cao | Vuông tại $A$, $BH = 4, CH = 9$. Đường cao $AH = \mathbf{6}$ | Vuông tại $A$, $BH = 2, CH = 8$. Đường cao $AH = \mathbf{4}$ | Vuông tại $A$, $BH = 1, CH = 9$. Đường cao $AH = \mathbf{3}$ | Vuông tại $A$, $BH = 3, CH = 12$. Đường cao $AH = \mathbf{6}$ |
| **4** | Hằng đẳng thức căn bậc hai | Rút gọn $\sqrt{(2 - \sqrt{5})^2}$ được kết quả: $\mathbf{\sqrt{5} - 2}$ | Rút gọn $\sqrt{(3 - \sqrt{10})^2}$ được kết quả: $\mathbf{\sqrt{10} - 3}$ | Rút gọn $\sqrt{(1 - \sqrt{3})^2}$ được kết quả: $\mathbf{\sqrt{3} - 1}$ | Rút gọn $\sqrt{(2 - \sqrt{7})^2}$ được kết quả: $\mathbf{\sqrt{7} - 2}$ |
| **5** | ĐKXĐ của căn thức | Biểu thức $\sqrt{3x - 6}$ xác định khi: $\mathbf{x \ge 2}$ | Biểu thức $\sqrt{2x - 8}$ xác định khi: $\mathbf{x \ge 4}$ | Biểu thức $\sqrt{4x - 12}$ xác định khi: $\mathbf{x \ge 3}$ | Biểu thức $\sqrt{5x - 15}$ xác định khi: $\mathbf{x \ge 3}$ |
| **6** | Khai phương số học | Giá trị của $\sqrt{18} : \sqrt{2} + \sqrt{16}$ là: $\mathbf{7}$ | Giá trị của $\sqrt{50} : \sqrt{2} - \sqrt{9}$ là: $\mathbf{2}$ | Giá trị của $\sqrt{75} : \sqrt{3} + \sqrt{25}$ là: $\mathbf{10}$ | Giá trị của $\sqrt{48} : \sqrt{3} - \sqrt{4}$ là: $\mathbf{2}$ |
| **7** | Phương trình căn thức | Nghiệm của $\sqrt{2x - 1} = 3$ là $x = \mathbf{5}$ | Nghiệm của $\sqrt{3x + 1} = 4$ là $x = \mathbf{5}$ | Nghiệm của $\sqrt{4x + 1} = 5$ là $x = \mathbf{6}$ | Nghiệm của $\sqrt{2x + 5} = 5$ là $x = \mathbf{10}$ |
| **8** | Thực tế thang dựa tường | Thang dài $5\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{2{,}5\text{ m}}$ | Thang dài $6\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{3\text{ m}}$ | Thang dài $4\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{2\text{ m}}$ | Thang dài $8\text{ m}$ nghiêng $60^\circ$. Chân thang cách tường: $\mathbf{4\text{ m}}$ |
| **9** | Nghiệm hệ phương trình | Nghiệm của $\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$ là $(x; y) = \mathbf{(3; 2)}$ | Nghiệm của $\begin{cases} x + y = 6 \\ x - y = 2 \end{cases}$ là $(x; y) = \mathbf{(4; 2)}$ | Nghiệm của $\begin{cases} x + y = 7 \\ x - y = 1 \end{cases}$ là $(x; y) = \mathbf{(4; 3)}$ | Nghiệm của $\begin{cases} x + y = 8 \\ x - y = 2 \end{cases}$ là $(x; y) = \mathbf{(5; 3)}$ |
| **10** | Tổng lượng giác phụ nhau | Giá trị $\sin^2 10^\circ + \dots + \sin^2 80^\circ$ (8 số hạng) là: $\mathbf{4}$ | Giá trị $\cos^2 10^\circ + \dots + \cos^2 80^\circ$ (8 số hạng) là: $\mathbf{4}$ | Giá trị $\sin^2 15^\circ + \sin^2 35^\circ + \sin^2 55^\circ + \sin^2 75^\circ$ là: $\mathbf{2}$ | Giá trị $\cos^2 15^\circ + \cos^2 35^\circ + \cos^2 55^\circ + \cos^2 75^\circ$ là: $\mathbf{2}$ |

---

### 2. PHẦN TỰ LUẬN (CÂU 11 ĐẾN CÂU 13 - TỔNG CỘNG 7,5 ĐIỂM)

#### CÂU 11 (2,5 ĐIỂM): ĐẠI SỐ TỔNG HỢP (HỆ PHƯƠNG TRÌNH & RÚT GỌN CĂN THỨC)

* **Mã đề 101:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 2x + 3y = 12 \\ 3x - y = 7 \end{cases} \Leftrightarrow \begin{cases} 2x + 3y = 12 \\ 9x - 3y = 21 \end{cases} \Leftrightarrow \begin{cases} 11x = 33 \\ y = 3x - 7 \end{cases} \Leftrightarrow \begin{cases} x = 3 \\ y = 2 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 4$:
    $P = \left(\dfrac{1}{\sqrt{x}-2} + \dfrac{1}{\sqrt{x}+2}\right) \cdot \dfrac{x-4}{\sqrt{x}}$.
    - *Lời giải:* $P = \dfrac{\sqrt{x}+2+\sqrt{x}-2}{(\sqrt{x}-2)(\sqrt{x}+2)} \cdot \dfrac{x-4}{\sqrt{x}} = \dfrac{2\sqrt{x}}{x-4} \cdot \dfrac{x-4}{\sqrt{x}} = 2$.

* **Mã đề 102:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 3x + 2y = 13 \\ 2x - y = 4 \end{cases} \Leftrightarrow \begin{cases} 3x + 2y = 13 \\ 4x - 2y = 8 \end{cases} \Leftrightarrow \begin{cases} 7x = 21 \\ y = 2x - 4 \end{cases} \Leftrightarrow \begin{cases} x = 3 \\ y = 2 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 9$:
    $P = \left(\dfrac{1}{\sqrt{x}-3} + \dfrac{1}{\sqrt{x}+3}\right) \cdot \dfrac{x-9}{\sqrt{x}}$.
    - *Lời giải:* $P = \dfrac{2\sqrt{x}}{x-9} \cdot \dfrac{x-9}{\sqrt{x}} = 2$.

* **Mã đề 103:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 2x + y = 7 \\ 3x + 2y = 12 \end{cases} \Leftrightarrow \begin{cases} 4x + 2y = 14 \\ 3x + 2y = 12 \end{cases} \Leftrightarrow \begin{cases} x = 2 \\ y = 7 - 2x \end{cases} \Leftrightarrow \begin{cases} x = 2 \\ y = 3 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 1$:
    $P = \left(\dfrac{1}{\sqrt{x}-1} + \dfrac{1}{\sqrt{x}+1}\right) \cdot \dfrac{x-1}{\sqrt{x}}$.
    - *Lời giải:* $P = \dfrac{2\sqrt{x}}{x-1} \cdot \dfrac{x-1}{\sqrt{x}} = 2$.

* **Mã đề 104:**
  - a) (1,25 đ) Giải hệ phương trình: $\begin{cases} 3x - 2y = 5 \\ x + 2y = 7 \end{cases} \Leftrightarrow \begin{cases} 4x = 12 \\ 2y = 7 - x \end{cases} \Leftrightarrow \begin{cases} x = 3 \\ y = 2 \end{cases}$.
  - b) (1,25 đ) Rút gọn biểu thức với $x > 0, x \ne 16$:
    $P = \left(\dfrac{1}{\sqrt{x}-4} + \dfrac{1}{\sqrt{x}+4}\right) \cdot \dfrac{x-16}{\sqrt{x}}$.
    - *Lời giải:* $P = \dfrac{2\sqrt{x}}{x-16} \cdot \dfrac{x-16}{\sqrt{x}} = 2$.

---

#### CÂU 12 (2,5 ĐIỂM): GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH

* **Mã đề 101:**
  Hai xe máy cùng khởi hành một lúc từ hai địa điểm $A$ và $B$ cách nhau $90\text{ km}$, đi ngược chiều nhau và gặp nhau sau $1{,}5$ giờ. Biết rằng vận tốc của xe đi từ $A$ lớn hơn vận tốc của xe đi từ $B$ là $10\text{ km/h}$. Tính vận tốc của mỗi xe máy.
  - *Lời giải:*
    - Gọi vận tốc của xe đi từ $A$ là $x\text{ (km/h)}$, vận tốc của xe đi từ $B$ là $y\text{ (km/h)}$ ($x > y > 0$). *(0,5đ)*
    - Vì vận tốc xe đi từ $A$ lớn hơn vận tốc xe đi từ $B$ là $10\text{ km/h}$ nên: $x - y = 10$. *(0,5đ)*
    - Sau $1{,}5$ giờ, xe đi từ $A$ đi được $1{,}5x\text{ (km)}$, xe đi từ $B$ đi được $1{,}5y\text{ (km)}$. Tổng quãng đường là $90\text{ km}$ nên: $1{,}5x + 1{,}5y = 90 \Leftrightarrow x + y = 60$. *(0,5đ)*
    - Ta có hệ phương trình: $\begin{cases} x + y = 60 \\ x - y = 10 \end{cases} \Leftrightarrow \begin{cases} 2x = 70 \\ y = x - 10 \end{cases} \Leftrightarrow \begin{cases} x = 35 \\ y = 25 \end{cases}$ (thỏa mãn ĐK). *(0,75đ)*
    - Kết luận: Vận tốc xe đi từ $A$ là $35\text{ km/h}$; vận tốc xe đi từ $B$ là $25\text{ km/h}$. *(0,25đ)*

* **Mã đề 102:**
  Hai ô tô khởi hành cùng một lúc từ hai địa điểm $A$ và $B$ cách nhau $120\text{ km}$, đi ngược chiều nhau và gặp nhau sau $1{,}5$ giờ. Biết vận tốc ô tô đi từ $A$ lớn hơn vận tốc ô tô đi từ $B$ là $20\text{ km/h}$. Tính vận tốc của mỗi ô tô.
  - *Hệ phương trình:* $\begin{cases} 1{,}5x + 1{,}5y = 120 \\ x - y = 20 \end{cases} \Leftrightarrow \begin{cases} x + y = 80 \\ x - y = 20 \end{cases} \Leftrightarrow \begin{cases} x = 50 \\ y = 30 \end{cases}$ (km/h).

* **Mã đề 103:**
  Hai người đi xe đạp cùng khởi hành một lúc từ hai địa điểm $A$ và $B$ cách nhau $48\text{ km}$, đi ngược chiều nhau và gặp nhau sau $2$ giờ. Biết vận tốc người đi từ $A$ lớn hơn vận tốc người đi từ $B$ là $4\text{ km/h}$. Tính vận tốc của mỗi người.
  - *Hệ phương trình:* $\begin{cases} 2x + 2y = 48 \\ x - y = 4 \end{cases} \Leftrightarrow \begin{cases} x + y = 24 \\ x - y = 4 \end{cases} \Leftrightarrow \begin{cases} x = 14 \\ y = 10 \end{cases}$ (km/h).

* **Mã đề 104:**
  Hai xe máy khởi hành cùng một lúc từ hai địa điểm $A$ và $B$ cách nhau $100\text{ km}$, đi ngược chiều nhau và gặp nhau sau $1{,}25$ giờ (tức $1$ giờ $15$ phút). Biết vận tốc xe đi từ $A$ lớn hơn vận tốc xe đi từ $B$ là $16\text{ km/h}$. Tính vận tốc của mỗi xe.
  - *Hệ phương trình:* $\begin{cases} 1{,}25x + 1{,}25y = 100 \\ x - y = 16 \end{cases} \Leftrightarrow \begin{cases} x + y = 80 \\ x - y = 16 \end{cases} \Leftrightarrow \begin{cases} x = 48 \\ y = 32 \end{cases}$ (km/h).

---

#### CÂU 13 (2,5 ĐIỂM): GIẢI TAM GIÁC VUÔNG & CHỨNG MINH ĐẲNG THỨC

* **Mã đề 101:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 12\text{ cm}$. Kẻ đường cao $AH$ ($H \in BC$).
  - a) (1,5 điểm) Tính số đo góc $C$, độ dài các cạnh $AC, AB$ và độ dài đường cao $AH$.
    - *Lời giải:*
      - Số đo góc $C$: $\widehat{C} = 90^\circ - \widehat{B} = 90^\circ - 30^\circ = 60^\circ$. *(0,25đ)*
      - Trong tam giác $ABC$ vuông tại $A$:
        $AC = BC \cdot \sin B = 12 \cdot \sin 30^\circ = 12 \cdot \dfrac{1}{2} = 6\text{ cm}$. *(0,5đ)*
        $AB = BC \cdot \cos B = 12 \cdot \cos 30^\circ = 12 \cdot \dfrac{\sqrt{3}}{2} = 6\sqrt{3}\text{ cm}$. *(0,5đ)*
      - Độ dài đường cao $AH$:
        $AH = \dfrac{AB \cdot AC}{BC} = \dfrac{6\sqrt{3} \cdot 6}{12} = 3\sqrt{3}\text{ cm}$. *(0,25đ)*
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh rằng: $AD \cdot AB = AE \cdot AC$.
    - *Lời giải:*
      - Trong tam giác $ABH$ vuông tại $H$, đường cao $HD$: $AD \cdot AB = AH^2$ (hệ thức lượng). *(0,5đ)*
      - Trong tam giác $ACH$ vuông tại $H$, đường cao $HE$: $AE \cdot AC = AH^2$ (hệ thức lượng). *(0,25đ)*
      - Từ đó suy ra: $AD \cdot AB = AE \cdot AC = AH^2$ (đpcm). *(0,25đ)*

* **Mã đề 102:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 10\text{ cm}$. Kẻ đường cao $AH$.
  - a) (1,5 điểm) Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.
    - *Lời giải:* $\widehat{C} = 30^\circ$; $AB = 10 \cdot \cos 60^\circ = 5\text{ cm}$; $AC = 10 \cdot \sin 60^\circ = 5\sqrt{3}\text{ cm}$; $AH = \dfrac{5 \cdot 5\sqrt{3}}{10} = \dfrac{5\sqrt{3}}{2}\text{ cm}$.
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$.
    - *Lời giải:* Tứ giác $ADHE$ có $\widehat{DAE} = \widehat{ADH} = \widehat{AEH} = 90^\circ$ nên là hình chữ nhật, suy ra 2 đường chéo bằng nhau: $DE = AH$.

* **Mã đề 103:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 30^\circ$ và cạnh huyền $BC = 8\text{ cm}$. Kẻ đường cao $AH$.
  - a) (1,5 điểm) Tính số đo góc $C$, độ dài các cạnh $AC, AB$ và độ dài đường cao $AH$.
    - *Lời giải:* $\widehat{C} = 60^\circ$; $AC = 8 \cdot \sin 30^\circ = 4\text{ cm}$; $AB = 8 \cdot \cos 30^\circ = 4\sqrt{3}\text{ cm}$; $AH = 2\sqrt{3}\text{ cm}$.
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh rằng: $AD \cdot AB = AE \cdot AC$.

* **Mã đề 104:**
  Cho tam giác $ABC$ vuông tại $A$ có $\widehat{B} = 60^\circ$ và cạnh huyền $BC = 12\text{ cm}$. Kẻ đường cao $AH$.
  - a) (1,5 điểm) Tính số đo góc $C$, độ dài các cạnh $AB, AC$ và độ dài đường cao $AH$.
    - *Lời giải:* $\widehat{C} = 30^\circ$; $AB = 12 \cdot \cos 60^\circ = 6\text{ cm}$; $AC = 12 \cdot \sin 60^\circ = 6\sqrt{3}\text{ cm}$; $AH = 3\sqrt{3}\text{ cm}$.
  - b) (1,0 điểm) Kẻ $HD \perp AB$ tại $D$ và $HE \perp AC$ tại $E$. Chứng minh tứ giác $ADHE$ là hình chữ nhật và suy ra $DE = AH$.
