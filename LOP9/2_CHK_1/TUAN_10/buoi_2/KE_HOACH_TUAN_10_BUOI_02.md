# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 10 - BUỔI 02 (TOÁN 9)
## CHỦ ĐỀ: TÍNH CHẤT HAI TIẾP TUYẾN CẮT NHAU & ĐƯỜNG TRÒN NỘI TIẾP
### Bám sát chương trình: SGK Toán 9 - Kết nối tri thức với cuộc sống (Chương V) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững định lí về tính chất của hai tiếp tuyến cắt nhau: Nếu hai tiếp tuyến của một đường tròn cắt nhau tại một điểm thì điểm đó cách đều hai tiếp điểm ($MA = MB$); tia kẻ từ điểm đó đi qua tâm là tia phân giác của góc tạo bởi hai tiếp tuyến ($MO$ là phân giác $\widehat{AMB}$); tia kẻ từ tâm đi qua điểm đó là tia phân giác của góc tạo bởi hai bán kính đi qua các tiếp điểm ($OM$ là phân giác $\widehat{AOB}$).
   - Nắm vững tính chất: Đường nối từ tâm đến giao điểm hai tiếp tuyến là đường trung trực của đoạn thẳng nối hai tiếp điểm ($OM \perp AB$ tại trung điểm $H$).
   - Nắm vững khái niệm đường tròn nội tiếp tam giác: Tâm đường tròn nội tiếp tam giác là giao điểm của ba đường phân giác trong.
   - Củng cố Đại số: Giải hệ hai phương trình quy về bậc nhất hai ẩn; Rút gọn biểu thức chứa căn và tìm số nguyên $x$ để biểu thức nhận giá trị nguyên.
   - Giải bài toán bằng cách lập hệ phương trình (dạng toán kinh tế, thương mại, mua sắm giảm giá phần trăm theo giá niêm yết).

2. **Kỹ năng:**
   - Kỹ năng vẽ hình hai tiếp tuyến cắt nhau bằng TikZ, xác định góc vuông, đường trung trực, đường kính.
   - Trình bày lời giải hình học 2 ý chuẩn xác, tính toán độ dài và diện tích tam giác tạo bởi hai tiếp tuyến.
   - Kỹ năng trình bày bài giải tự luận chuẩn barem chấm thi tuyển sinh vào Lớp 10.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề hoán vị tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Thời gian (phút) | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | 10 | Trả lời ngắn, lệnh `\shortans`, ô kết quả bo góc mép phải, bố trí 2 cột Trang 1. |
| **Câu 11** | 2 ý | **2,5 đ** *(1,25 đ/ý)* | 15 | Đại số tổng hợp (Hệ PT & Tìm $x$ nguyên để $Q$ nguyên). Bảng $1 \times 2$, dùng **`\oBaiTap[21]`** lấp kín đáy Trang 1. |
| **Câu 12** | 1 bài | **2,5 đ** | 10 | Giải bài toán bằng cách lập hệ phương trình (Toán mua sắm giảm giá). Box `tabularx`, bài giải **`\dongke{16}`** trên Trang 2. |
| **Câu 13** | 2 ý | **2,5 đ** *(1,25 đ/ý)* | 10 | Bài toán Hình học hai tiếp tuyến cắt nhau (có hình TikZ). Box `tabularx`, bài giải **`\dongke{17}`** chạm sát đáy Trang 2. |
| **Tổng cộng** | **15 câu/ý** | **10,0 đ** | **45** | **Khít mép giấy cả 2 trang, chuẩn 100% cấu trúc thi vào Lớp 10.** |

---

## 🔢 III. BẢNG DỮ LIỆU SỐ HỌC 4 MÃ ĐỀ (HOÀN TOÀN TƯƠNG ĐƯƠNG)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - 2,5 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Tính chất 2 tiếp tuyến cắt nhau | $MA, MB$ tiếp tuyến cắt nhau tại $M \implies$ Khẳng định đúng là: **$MA = MB$** | $MA, MB$ tiếp tuyến của $(O) \implies MO$ là phân giác góc: **$\widehat{AMB}$** | $MA, MB$ tiếp tuyến của $(O) \implies OM$ là phân giác góc: **$\widehat{AOB}$** | Tiếp tuyến tại $A, B$ cắt nhau ở $M \implies OM$ là trung trực của: **$AB$** |
| **2** | Góc giữa 2 tiếp tuyến cắt nhau | $MA, MB$ tiếp tuyến $(O)$, $\widehat{AMB} = 60^\circ \implies \widehat{AOB} =$ **$120^\circ$** | $MA, MB$ tiếp tuyến $(O)$, $\widehat{AOB} = 110^\circ \implies \widehat{AMB} =$ **$70^\circ$** | $MA, MB$ tiếp tuyến $(O)$, $\widehat{AMB} = 80^\circ \implies \widehat{AOB} =$ **$100^\circ$** | $MA, MB$ tiếp tuyến $(O)$, $\widehat{AOB} = 130^\circ \implies \widehat{AMB} =$ **$50^\circ$** |
| **3** | Đường tròn nội tiếp tam giác | Tâm đường tròn nội tiếp tam giác là giao điểm ba đường: **phân giác trong** | Tâm đường tròn ngoại tiếp tam giác là giao điểm ba đường: **trung trực** | $\Delta$ vuông cạnh $6, 8, 10\text{ cm}$. Bán kính nội tiếp $r =$ **$2\text{ cm}$** | $\Delta$ vuông cạnh $5, 12, 13\text{ cm}$. Bán kính nội tiếp $r =$ **$2\text{ cm}$** |
| **4** | Khai căn hằng đẳng thức | Tính: $\sqrt{(3 - \sqrt{10})^2} =$ **$\sqrt{10} - 3$** | Tính: $\sqrt{(2 - \sqrt{5})^2} =$ **$\sqrt{5} - 2$** | Tính: $\sqrt{(\sqrt{7} - 3)^2} =$ **$3 - \sqrt{7}$** | Tính: $\sqrt{(\sqrt{11} - 4)^2} =$ **$4 - \sqrt{11}$** |
| **5** | Điều kiện xác định căn thức | ĐKXĐ của $\dfrac{1}{\sqrt{x - 3}}$ là: **$x > 3$** | ĐKXĐ của $\dfrac{1}{\sqrt{x - 4}}$ là: **$x > 4$** | ĐKXĐ của $\dfrac{1}{\sqrt{x - 5}}$ là: **$x > 5$** | ĐKXĐ của $\dfrac{1}{\sqrt{x - 2}}$ là: **$x > 2$** |
| **6** | Phương trình chứa căn đơn giản | Nghiệm của $\sqrt{x} = 5$ là: **$x = 25$** | Nghiệm của $\sqrt{x} = 6$ là: **$x = 36$** | Nghiệm của $\sqrt{x} = 7$ là: **$x = 49$** | Nghiệm của $\sqrt{x} = 8$ là: **$x = 64$** |
| **7** | Nghiệm của hệ phương trình | Hệ $\begin{cases} 3x - y = 5 \\ x + 2y = 4 \end{cases} \implies (x; y) =$ **$(2; 1)$** | Hệ $\begin{cases} 3x - y = 7 \\ x + 2y = 7 \end{cases} \implies (x; y) =$ **$(3; 2)$** | Hệ $\begin{cases} 3x - y = 8 \\ x + 2y = 5 \end{cases} \implies (x; y) =$ **$(3; 1)$** | Hệ $\begin{cases} 3x - y = 4 \\ x + 2y = 6 \end{cases} \implies (x; y) =$ **$(2; 2)$** |
| **8** | Chu vi đường tròn | Chu vi đường tròn $(O; R = 5\text{ cm})$ là: **$10\pi\text{ cm}$** | Chu vi đường tròn $(O; R = 6\text{ cm})$ là: **$12\pi\text{ cm}$** | Chu vi đường tròn $(O; R = 7\text{ cm})$ là: **$14\pi\text{ cm}$** | Chu vi đường tròn $(O; R = 8\text{ cm})$ là: **$16\pi\text{ cm}$** |
| **9** | Diện tích hình tròn | Bán kính $R = 4\text{ cm}$. Diện tích hình tròn là: **$16\pi\text{ cm}^2$** | Bán kính $R = 5\text{ cm}$. Diện tích hình tròn là: **$25\pi\text{ cm}^2$** | Bán kính $R = 3\text{ cm}$. Diện tích hình tròn là: **$9\pi\text{ cm}^2$** | Bán kính $R = 6\text{ cm}$. Diện tích hình tròn là: **$36\pi\text{ cm}^2$** |
| **10** | Toán thực tế số vòng quay | Bánh xe đường kính $60\text{ cm}$, đi $180\pi\text{ cm}$ thì quay: **$3\text{ vòng}$** | Bánh xe đường kính $50\text{ cm}$, đi $200\pi\text{ cm}$ thì quay: **$4\text{ vòng}$** | Bánh xe đường kính $70\text{ cm}$, đi $350\pi\text{ cm}$ thì quay: **$5\text{ vòng}$** | Bánh xe đường kính $40\text{ cm}$, đi $240\pi\text{ cm}$ thì quay: **$6\text{ vòng}$** |

---

### 2. PHẦN TỰ LUẬN - TRANG 1 & TRANG 2

#### CÂU 11 (2,5 ĐIỂM): ĐẠI SỐ TỔNG HỢP

* **Mã đề 101:**
  - $a)$ (1,25 điểm): Giải hệ phương trình:
    $$\begin{cases} 2(x + y) + 3(x - y) = 4 \\ (x + y) - 2(x - y) = 9 \end{cases}$$
    * Đặt $u = x + y, v = x - y$. Hệ trở thành: $\begin{cases} 2u + 3v = 4 \\ u - 2v = 9 \end{cases} \iff \begin{cases} u = 5 \\ v = -2 \end{cases}$.
    * Suy ra: $\begin{cases} x + y = 5 \\ x - y = -2 \end{cases} \iff \begin{cases} 2x = 3 \\ 2y = 7 \end{cases} \iff \begin{cases} x = \dfrac{3}{2} \\ y = \dfrac{7}{2} \end{cases}$. Nghiệm $(x; y) = \left(\dfrac{3}{2}; \dfrac{7}{2}\right)$.
  - $b)$ (1,25 điểm): Cho biểu thức $Q = \dfrac{\sqrt{x} + 3}{\sqrt{x} + 1}$ với $x \ge 0$. Tìm các giá trị nguyên của $x$ để biểu thức $Q$ nhận giá trị nguyên.
    * Ta có: $Q = \dfrac{\sqrt{x} + 1 + 2}{\sqrt{x} + 1} = 1 + \dfrac{2}{\sqrt{x} + 1}$.
    * Để $Q$ nhận giá trị nguyên thì $\dfrac{2}{\sqrt{x} + 1}$ phải là số nguyên $\implies \sqrt{x} + 1 \in \text{Ư}(2) = \{1; 2\}$.
    * Do $\sqrt{x} \ge 0 \implies \sqrt{x} + 1 \ge 1$:
      - Trường hợp 1: $\sqrt{x} + 1 = 1 \iff \sqrt{x} = 0 \iff x = 0$ (thỏa mãn).
      - Trường hợp 2: $\sqrt{x} + 1 = 2 \iff \sqrt{x} = 1 \iff x = 1$ (thỏa mãn).
    * Kết luận: $x \in \{0; 1\}$.

* **Mã đề 102:**
  - $a)$ (1,25 điểm): Giải hệ phương trình:
    $$\begin{cases} 3(x + y) + 2(x - y) = 13 \\ 2(x + y) - (x - y) = 4 \end{cases}$$
    * Đặt $u = x + y, v = x - y \implies \begin{cases} 3u + 2v = 13 \\ 2u - v = 4 \end{cases} \iff \begin{cases} u = 3 \\ v = 2 \end{cases}$.
    * Suy ra $\begin{cases} x + y = 3 \\ x - y = 2 \end{cases} \iff x = \dfrac{5}{2}, y = \dfrac{1}{2}$.
  - $b)$ (1,25 điểm): Cho $Q = \dfrac{\sqrt{x} + 4}{\sqrt{x} + 1}$ ($x \ge 0$). Tìm các giá trị nguyên của $x$ để $Q$ nhận giá trị nguyên.
    * $Q = 1 + \dfrac{3}{\sqrt{x} + 1} \implies \sqrt{x} + 1 \in \text{Ư}(3) = \{1; 3\}$.
    * $\sqrt{x} + 1 = 1 \iff x = 0$; $\sqrt{x} + 1 = 3 \iff \sqrt{x} = 2 \iff x = 4$. Kết luận: $x \in \{0; 4\}$.

* **Mã đề 103:**
  - $a)$ (1,25 điểm): Giải hệ phương trình:
    $$\begin{cases} 4(x + y) + (x - y) = 11 \\ (x + y) - 3(x - y) = -7 \end{cases}$$
    * Đặt $u = x + y, v = x - y \implies \begin{cases} 4u + v = 11 \\ u - 3v = -7 \end{cases} \iff \begin{cases} u = 2 \\ v = 3 \end{cases}$.
    * Suy ra $\begin{cases} x + y = 2 \\ x - y = 3 \end{cases} \iff x = \dfrac{5}{2}, y = -\dfrac{1}{2}$.
  - $b)$ (1,25 điểm): Cho $Q = \dfrac{\sqrt{x} + 5}{\sqrt{x} + 2}$ ($x \ge 0$). Tìm các giá trị nguyên của $x$ để $Q$ nhận giá trị nguyên.
    * $Q = 1 + \dfrac{3}{\sqrt{x} + 2}$. Vì $\sqrt{x} + 2 \ge 2$ nên $\sqrt{x} + 2 = 3 \iff \sqrt{x} = 1 \iff x = 1$. Kết luận: $x = 1$.

* **Mã đề 104:**
  - $a)$ (1,25 điểm): Giải hệ phương trình:
    $$\begin{cases} 2(x + y) + (x - y) = 7 \\ 3(x + y) - 2(x - y) = 7 \end{cases}$$
    * Đặt $u = x + y, v = x - y \implies \begin{cases} 2u + v = 7 \\ 3u - 2v = 7 \end{cases} \iff \begin{cases} u = 3 \\ v = 1 \end{cases}$.
    * Suy ra $\begin{cases} x + y = 3 \\ x - y = 1 \end{cases} \iff x = 2, y = 1$.
  - $b)$ (1,25 điểm): Cho $Q = \dfrac{\sqrt{x} + 7}{\sqrt{x} + 3}$ ($x \ge 0$). Tìm các giá trị nguyên của $x$ để $Q$ nhận giá trị nguyên.
    * $Q = 1 + \dfrac{4}{\sqrt{x} + 3}$. Vì $\sqrt{x} + 3 \ge 3$ nên $\sqrt{x} + 3 = 4 \iff \sqrt{x} = 1 \iff x = 1$. Kết luận: $x = 1$.

---

#### CÂU 12 (2,5 ĐIỂM): TOÁN THỰC TẾ LẬP HỆ PHƯƠNG TRÌNH

* **Mã đề 101:** Nhân dịp khai trương, một siêu thị điện máy giảm giá $10\%$ cho mặt hàng tivi và $15\%$ cho mặt hàng máy giặt theo giá niêm yết. Bác Nam mua một chiếc tivi và một chiếc máy giặt với tổng giá niêm yết là $20\text{ triệu đồng}$, nhưng nhờ chương trình giảm giá nên bác chỉ phải thanh toán số tiền là $17{,}4\text{ triệu đồng}$. Tính giá niêm yết của mỗi mặt hàng nêu trên.
  - Gọi giá niêm yết của chiếc tivi là $x$ (triệu đồng), máy giặt là $y$ (triệu đồng) ($0 < x, y < 20$) ($0{,}25$đ).
  - Tổng giá niêm yết: $x + y = 20$ ($0{,}5$đ).
  - Số tiền thanh toán thực tế: $(1 - 10\%)x + (1 - 15\%)y = 17{,}4 \iff 0{,}9x + 0{,}85y = 17{,}4$ ($0{,}5$đ).
  - Hệ phương trình: $\begin{cases} x + y = 20 \\ 0{,}9x + 0{,}85y = 17{,}4 \end{cases}$ ($0{,}25$đ).
  - Giải hệ phương trình:
    $$\begin{cases} 0{,}9x + 0{,}9y = 18 \\ 0{,}9x + 0{,}85y = 17{,}4 \end{cases} \iff \begin{cases} 0{,}05y = 0{,}6 \\ x = 20 - y \end{cases} \iff \begin{cases} y = 12 \\ x = 8 \end{cases} \quad \text{(thỏa mãn điều kiện)} \quad \text{($0{,}75$đ).}$$
  - Kết luận: Giá niêm yết của chiếc tivi là $8\text{ triệu đồng}$, chiếc máy giặt là $12\text{ triệu đồng}$ ($0{,}25$đ).

* **Mã đề 102:** Hai mặt hàng có tổng giá niêm yết là $25\text{ triệu đồng}$. Nhân dịp lễ, mặt hàng thứ nhất giảm $10\%$, mặt hàng thứ hai giảm $20\%$, người mua phải thanh toán tổng số tiền là $21{,}5\text{ triệu đồng}$. Tính giá niêm yết của mỗi mặt hàng.
  - $\begin{cases} x + y = 25 \\ 0{,}9x + 0{,}8y = 21{,}5 \end{cases} \iff \begin{cases} x = 15 \\ y = 10 \end{cases}$ (triệu đồng).

* **Mã đề 103:** Hai mặt hàng có tổng giá niêm yết là $30\text{ triệu đồng}$. Mặt hàng thứ nhất giảm $20\%$, mặt hàng thứ hai giảm $15\%$, người mua thanh toán tổng cộng $24{,}6\text{ triệu đồng}$. Tính giá niêm yết của mỗi mặt hàng.
  - $\begin{cases} x + y = 30 \\ 0{,}8x + 0{,}85y = 24{,}6 \end{cases} \iff \begin{cases} x = 18 \\ y = 12 \end{cases}$ (triệu đồng).

* **Mã đề 104:** Hai mặt hàng có tổng giá niêm yết là $18\text{ triệu đồng}$. Mặt hàng thứ nhất giảm $15\%$, mặt hàng thứ hai giảm $10\%$, người mua thanh toán tổng cộng $15{,}7\text{ triệu đồng}$. Tính giá niêm yết của mỗi mặt hàng.
  - $\begin{cases} x + y = 18 \\ 0{,}85x + 0{,}9y = 15{,}7 \end{cases} \iff \begin{cases} x = 10 \\ y = 8 \end{cases}$ (triệu đồng).

---

#### CÂU 13 (2,5 ĐIỂM): HÌNH HỌC TÍNH CHẤT HAI TIẾP TUYẾN CẮT NHAU

Cho đường tròn $(O; R)$ và điểm $M$ nằm bên ngoài đường tròn. Qua $M$ kẻ hai tiếp tuyến $MA, MB$ với đường tròn $(O)$ ($A, B$ là các tiếp điểm). Kẻ đường kính $BC$ của đường tròn $(O)$. Đoạn thẳng $OM$ cắt $AB$ tại $H$.
* **Mã đề 101:** Cho $R = 15\text{ cm}, OM = 25\text{ cm}$.
  - $a)$ (1,25 điểm): Chứng minh $OM \perp AB$ tại $H$ và tính độ dài đoạn thẳng $AB$.
    * Theo tính chất hai tiếp tuyến cắt nhau ta có: $MA = MB$ ($0{,}25$đ).
    * Lại có $OA = OB = R$. Suy ra $OM$ là đường trung trực của đoạn thẳng $AB$ ($0{,}25$đ).
    * Do đó $OM \perp AB$ tại trung điểm $H$ của $AB$ ($0{,}25$đ).
    * Áp dụng định lí Pythagore trong $\Delta OAM$ vuông tại $A$:
      $$MA = \sqrt{OM^2 - OA^2} = \sqrt{25^2 - 15^2} = \sqrt{625 - 225} = 20\text{ cm} \quad \text{($0{,}25$đ).}$$
    * Áp dụng hệ thức lượng trong $\Delta OAM$ vuông tại $A$, đường cao $AH$:
      $$AH \cdot OM = OA \cdot MA \implies AH = \dfrac{15 \cdot 20}{25} = 12\text{ cm} \implies AB = 2 \cdot AH = 24\text{ cm} \quad \text{($0{,}25$đ).}$$
  - $b)$ (1,25 điểm): Chứng minh $AC \parallel OM$ và tính diện tích tam giác $MAB$.
    * Điểm $A$ thuộc đường tròn đường kính $BC$ nên $\widehat{BAC} = 90^\circ \implies AC \perp AB$ ($0{,}25$đ).
    * Lại có $OM \perp AB$ (theo ý a). Suy ra $AC \parallel OM$ (cùng vuông góc với $AB$) ($0{,}25$đ).
    * Áp dụng hệ thức lượng trong $\Delta OAM$ vuông tại $A$:
      $$OH = \dfrac{OA^2}{OM} = \dfrac{15^2}{25} = 9\text{ cm} \implies MH = OM - OH = 25 - 9 = 16\text{ cm} \quad \text{($0{,}25$đ).}$$
    * Diện tích tam giác $MAB$ là:
      $$S_{MAB} = \dfrac{1}{2} AB \cdot MH = \dfrac{1}{2} \cdot 24 \cdot 16 = 192\text{ cm}^2 \quad \text{($0{,}5$đ).}$$

* **Mã đề 102:** Cho $R = 6\text{ cm}, OM = 10\text{ cm}$.
  - $a)$ Chứng minh $OM \perp AB$ tại $H$. $MA = \sqrt{10^2 - 6^2} = 8\text{ cm}$; $AH = \dfrac{6 \cdot 8}{10} = 4{,}8\text{ cm} \implies AB = 9{,}6\text{ cm}$ ($1{,}25$đ).
  - $b)$ Chứng minh $AC \parallel OM$. $OH = \dfrac{6^2}{10} = 3{,}6\text{ cm} \implies MH = 10 - 3{,}6 = 6{,}4\text{ cm}$.
    $S_{MAB} = \dfrac{1}{2} \cdot 9{,}6 \cdot 6{,}4 = 30{,}72\text{ cm}^2$ ($1{,}25$đ).

* **Mã đề 103:** Cho $R = 9\text{ cm}, OM = 15\text{ cm}$.
  - $a)$ $MA = 12\text{ cm}$; $AH = \dfrac{9 \cdot 12}{15} = 7{,}2\text{ cm} \implies AB = 14{,}4\text{ cm}$ ($1{,}25$đ).
  - $b)$ $AC \parallel OM$. $OH = \dfrac{9^2}{15} = 5{,}4\text{ cm} \implies MH = 15 - 5{,}4 = 9{,}6\text{ cm}$.
    $S_{MAB} = \dfrac{1}{2} \cdot 14{,}4 \cdot 9{,}6 = 69{,}12\text{ cm}^2$ ($1{,}25$đ).

* **Mã đề 104:** Cho $R = 12\text{ cm}, OM = 20\text{ cm}$.
  - $a)$ $MA = 16\text{ cm}$; $AH = \dfrac{12 \cdot 16}{20} = 9{,}6\text{ cm} \implies AB = 19{,}2\text{ cm}$ ($1{,}25$đ).
  - $b)$ $AC \parallel OM$. $OH = \dfrac{12^2}{20} = 7{,}2\text{ cm} \implies MH = 20 - 7{,}2 = 12{,}8\text{ cm}$.
    $S_{MAB} = \dfrac{1}{2} \cdot 19{,}2 \cdot 12{,}8 = 122{,}88\text{ cm}^2$ ($1{,}25$đ).

