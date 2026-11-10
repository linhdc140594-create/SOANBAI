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
    $$\begin{cases} 3x + y = 10 \\ 2x - 3y = 3 \end{cases} \iff \begin{cases} 9x + 3y = 30 \\ 2x - 3y = 3 \end{cases} \iff \begin{cases} 11x = 33 \\ y = 10 - 3x \end{cases} \iff \begin{cases} x = 3 \\ y = 1 \end{cases}$$
    Nghiệm $(x; y) = (3; 1)$.
  - $b)$ (1,25 điểm): Cho biểu thức $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} + 2} + \dfrac{4\sqrt{x}}{x - 4} \right) : \dfrac{\sqrt{x} + 2}{x - 4}$ với $x > 0, x \ne 4$. Rút gọn biểu thức $P$.
    * Quy đồng trong ngoặc: $\dfrac{x + 2\sqrt{x}}{x - 4} = \dfrac{\sqrt{x}(\sqrt{x} + 2)}{x - 4}$.
    * Rút gọn $P = \dfrac{\sqrt{x}(\sqrt{x} + 2)}{x - 4} \cdot \dfrac{x - 4}{\sqrt{x} + 2} = \sqrt{x}$.

* **Mã đề 102:**
  - $a)$ (1,25 điểm): Giải hệ $\begin{cases} 2x + 5y = 12 \\ 3x - y = 1 \end{cases} \iff \begin{cases} 17x = 17 \\ y = 3x - 1 \end{cases} \iff \begin{cases} x = 1 \\ y = 2 \end{cases}$. Nghiệm $(1; 2)$.
  - $b)$ (1,25 điểm): Cho $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} + 3} + \dfrac{6\sqrt{x}}{x - 9} \right) : \dfrac{\sqrt{x} + 3}{x - 9}$ ($x > 0, x \ne 9$). Rút gọn $P = \sqrt{x}$.

* **Mã đề 103:**
  - $a)$ (1,25 điểm): Giải hệ $\begin{cases} 3x - 2y = 7 \\ x + 3y = 6 \end{cases} \iff \begin{cases} 11y = 11 \\ x = 6 - 3y \end{cases} \iff \begin{cases} x = 3 \\ y = 1 \end{cases}$. Nghiệm $(3; 1)$.
  - $b)$ (1,25 điểm): Cho $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} + 1} + \dfrac{2\sqrt{x}}{x - 1} \right) : \dfrac{\sqrt{x} + 1}{x - 1}$ ($x > 0, x \ne 1$). Rút gọn $P = \sqrt{x}$.

* **Mã đề 104:**
  - $a)$ (1,25 điểm): Giải hệ $\begin{cases} 2x + 3y = 13 \\ 4x - y = 5 \end{cases} \iff \begin{cases} 14x = 28 \\ y = 4x - 5 \end{cases} \iff \begin{cases} x = 2 \\ y = 3 \end{cases}$. Nghiệm $(2; 3)$.
  - $b)$ (1,25 điểm): Cho $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} + 4} + \dfrac{8\sqrt{x}}{x - 16} \right) : \dfrac{\sqrt{x} + 4}{x - 16}$ ($x > 0, x \ne 16$). Rút gọn $P = \sqrt{x}$.

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
* **a) (1,25 điểm):** Chứng minh bốn điểm $M, A, O, B$ cùng thuộc một đường tròn.
  - Do $MA$ là tiếp tuyến tại $A \implies \widehat{MAO} = 90^\circ \implies M, A, O$ thuộc đường tròn đường kính $OM$ ($0{,}5$đ).
  - Do $MB$ là tiếp tuyến tại $B \implies \widehat{MBO} = 90^\circ \implies M, B, O$ thuộc đường tròn đường kính $OM$ ($0{,}5$đ).
  - Suy ra 4 điểm $M, A, O, B$ cùng thuộc đường tròn đường kính $OM$ ($0{,}25$đ).
* **b) (1,25 điểm):** Chứng minh $AC \parallel OM$ và $\Delta OHB \sim \Delta OBM$ (từ đó suy ra $OH \cdot OM = R^2$).
  - $MA = MB, OA = OB \implies OM$ là trung trực của $AB \implies OM \perp AB$ tại $H$ ($0{,}25$đ).
  - $\triangle ABC$ vuông tại $A$ (do $BC$ là đường kính) $\implies AC \perp AB$ ($0{,}25$đ).
  - Suy ra $AC \parallel OM$ (vì cùng $\perp AB$) ($0{,}25$đ).
  - Xét $\Delta OHB$ và $\Delta OBM$ có $\widehat{OHB} = \widehat{OBM} = 90^\circ$ và góc $\widehat{BOM}$ chung $\implies \Delta OHB \sim \Delta OBM$ (g-g) ($0{,}25$đ).
  - Tỉ số đồng dạng: $\dfrac{OH}{OB} = \dfrac{OB}{OM} \implies OH \cdot OM = OB^2 = R^2$ ($0{,}25$đ).

*(Áp dụng đồng bộ cho cả 4 mã đề 101, 102, 103, 104).*

