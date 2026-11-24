# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ
## TOÁN 9 - TUẦN 12 - BUỔI 01
### CHỦ ĐỀ: BÀI 16: TÍNH CHẤT HAI TIẾP TUYẾN CẮT NHAU & CHỨNG MINH 4 ĐIỂM THUỘC ĐƯỜNG TRÒN, TAM GIÁC ĐỒNG DẠNG
### Bám sát chương trình: SGK Toán 9 - Kết nối tri thức với cuộc sống (Chương V: Đường tròn) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững tính chất tiếp tuyến của đường tròn: tiếp tuyến vuông góc với bán kính đi qua tiếp điểm ($AB \perp OB, AC \perp OC$).
   - **Kỹ năng chứng minh 4 điểm cùng thuộc một đường tròn:**
     * Nhận biết tam giác vuông có các đỉnh cùng thuộc đường tròn đường kính là cạnh huyền.
     * $\triangle ABO$ vuông tại $B \implies A, B, O$ thuộc đường tròn đường kính $AO$.
     * $\triangle ACO$ vuông tại $C \implies A, C, O$ thuộc đường tròn đường kính $AO$.
     * Kết luận bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $AO$.
   - **Kỹ năng chứng minh vuông góc & tam giác đồng dạng:**
     * Nắm vững tính chất của hai tiếp tuyến cắt nhau: $AB = AC, OB = OC = R \implies OA$ là đường trung trực của $BC \implies OA \perp BC$ tại $H$.
     * Chứng minh $\triangle OHB \backsim \triangle OBA$ (trường hợp góc - góc: có $\widehat{O}$ chung và $\widehat{OHB} = \widehat{OBA} = 90^\circ$).
     * Từ tỉ số đồng dạng $\dfrac{OH}{OB} = \dfrac{OB}{OA}$, suy ra hệ thức $OH \cdot OA = OB^2 = R^2$.
   - Củng cố Đại số chuẩn hóa:
     * Giải hệ hai phương trình bậc nhất hai ẩn cơ bản bằng phương pháp cộng đại số hoặc phương pháp thế.
     * Rút gọn biểu thức phân thức chứa căn bậc hai $P(x)$ và tính giá trị tại điểm $x = x_0$ chính phương (không lồng ghép câu hỏi tìm $x$ để biểu thức đạt giá trị).
   - Giải bài toán bằng cách lập hệ phương trình: Dạng **Toán chuyển động** (hai xe ô tô và xe máy đi ngược chiều gặp nhau).

2. **Kỹ năng & Năng lực:**
   - Học sinh tiếp tục hoàn thiện hình vẽ trên đường tròn $(O)$ đã vẽ sẵn trong đề bài.
   - Trình bày bài giải hình học lập luận chuẩn mực 2 ý: ý a chứng minh 4 điểm thuộc đường tròn, ý b chứng minh vuông góc và tam giác đồng dạng suy ra hệ thức.
   - Giải bài toán thực tế lập hệ phương trình đầy đủ các bước.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: đúng 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Vị trí trên đề | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | Trang 1 (Đầu) | Trả lời ngắn, lệnh `\shortans`, ô kết quả bo góc mép phải thẳng hàng, 1 dòng/câu. |
| **Câu 11** | 2 ý ($a, b$) | **2,5 đ** *(1,25 đ/ý)* | Trang 1 (Cuối) | Đại số (Hệ PT cơ bản & Rút gọn tính giá trị tại $x_0$). Bảng $1 \times 2$, dùng **`\oBaiTap[20]`** lấp kín đáy Trang 1. |
| **Câu 12** | 1 bài | **2,5 đ** | Trang 2 (Đầu) | Giải bài toán bằng cách lập hệ phương trình (Toán chuyển động). Box `tabularx`, bài giải **`\dongke{16}`**. |
| **Câu 13** | 2 ý ($a, b$) | **2,5 đ** *(1,25 đ/ý)* | Trang 2 (Cuối) | Bài toán Hình học (ý a: 4 điểm thuộc đường tròn; ý b: vuông góc & đồng dạng; vẽ sẵn đường tròn $(O)$). Box `tabularx`, bài giải **`\dongke{16}`** sát đáy Trang 2. |
| **Tổng cộng** | **15 câu/ý** | **10,0 đ** | **2 mặt A4** | **Chuẩn tuyệt đối 8 trang PDF cho 4 mã đề, lề dưới 10 - 15 mm.** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Độ dài tiếp tuyến | $A$ ngoài $(O; 5), AB$ tiếp tuyến, $OA = 13\text{ cm}$. $AB =$<br>$\to$ **$12\text{ cm}$** | $A$ ngoài $(O; 6), AB$ tiếp tuyến, $OA = 10\text{ cm}$. $AB =$<br>$\to$ **$8\text{ cm}$** | $A$ ngoài $(O; 8), AB$ tiếp tuyến, $OA = 17\text{ cm}$. $AB =$<br>$\to$ **$15\text{ cm}$** | $A$ ngoài $(O; 9), AB$ tiếp tuyến, $OA = 15\text{ cm}$. $AB =$<br>$\to$ **$12\text{ cm}$** |
| **2** | Góc giữa hai tiếp tuyến | $AB, AC$ là tiếp tuyến của $(O), \widehat{BOC} = 120^\circ \implies \widehat{BAC} =$<br>$\to$ **$60^\circ$** | $AB, AC$ là tiếp tuyến của $(O), \widehat{BOC} = 110^\circ \implies \widehat{BAC} =$<br>$\to$ **$70^\circ$** | $AB, AC$ là tiếp tuyến của $(O), \widehat{BAC} = 50^\circ \implies \widehat{BOC} =$<br>$\to$ **$130^\circ$** | $AB, AC$ là tiếp tuyến của $(O), \widehat{BAC} = 70^\circ \implies \widehat{BOC} =$<br>$\to$ **$110^\circ$** |
| **3** | Khoảng cách từ tâm đến tiếp tuyến | Khoảng cách từ tâm $O$ đến tiếp tuyến của $(O; R)$ bằng:<br>$\to$ **$R$** | Đường thẳng vuông góc bán kính tại tiếp điểm là:<br>$\to$ **Tiếp tuyến** | Số tiếp tuyến kẻ từ một điểm ngoài đường tròn tới $(O)$ là:<br>$\to$ **$2$** | Cho $(O; 5\text{ cm})$. Khoảng cách từ $O$ đến tiếp tuyến là:<br>$\to$ **$5\text{ cm}$** |
| **4** | Khai căn hằng đẳng thức | Giá trị biểu thức $\sqrt{(4 - \sqrt{17})^2} =$<br>$\to$ **$\sqrt{17} - 4$** | Giá trị biểu thức $\sqrt{(3 - \sqrt{11})^2} =$<br>$\to$ **$\sqrt{11} - 3$** | Giá trị biểu thức $\sqrt{(5 - \sqrt{26})^2} =$<br>$\to$ **$\sqrt{26} - 5$** | Giá trị biểu thức $\sqrt{(2 - \sqrt{7})^2} =$<br>$\to$ **$\sqrt{7} - 2$** |
| **5** | Điều kiện xác định căn thức | Điều kiện xác định của $\dfrac{1}{\sqrt{x - 3}}$ là:<br>$\to$ **$x > 3$** | Điều kiện xác định của $\dfrac{1}{\sqrt{x - 5}}$ là:<br>$\to$ **$x > 5$** | Điều kiện xác định của $\dfrac{1}{\sqrt{x - 4}}$ là:<br>$\to$ **$x > 4$** | Điều kiện xác định của $\dfrac{1}{\sqrt{x - 6}}$ là:<br>$\to$ **$x > 6$** |
| **6** | Rút gọn căn thức số học | Tính: $\sqrt{45} - \sqrt{20} + \sqrt{5} =$<br>$\to$ **$2\sqrt{5}$** | Tính: $\sqrt{48} - \sqrt{27} + \sqrt{3} =$<br>$\to$ **$2\sqrt{3}$** | Tính: $\sqrt{32} - \sqrt{18} + \sqrt{2} =$<br>$\to$ **$2\sqrt{2}$** | Tính: $\sqrt{75} - \sqrt{12} + \sqrt{27} =$<br>$\to$ **$6\sqrt{3}$** |
| **7** | Nghiệm hệ phương trình | Nghiệm của hệ $\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$ là $(x; y) =$<br>$\to$ **$(3; 1)$** | Nghiệm của hệ $\begin{cases} x + 2y = 7 \\ x - y = 1 \end{cases}$ là $(x; y) =$<br>$\to$ **$(3; 2)$** | Nghiệm của hệ $\begin{cases} 3x - y = 8 \\ x + y = 4 \end{cases}$ là $(x; y) =$<br>$\to$ **$(3; 1)$** | Nghiệm của hệ $\begin{cases} 2x - y = 5 \\ x + y = 4 \end{cases}$ là $(x; y) =$<br>$\to$ **$(3; 1)$** |
| **8** | Hệ thức lượng tam giác vuông | $\triangle$ vuông cạnh $6\text{ cm}, 8\text{ cm}$ có đường cao là:<br>$\to$ **$4{,}8\text{ cm}$** | $\triangle$ vuông cạnh $9\text{ cm}, 12\text{ cm}$ có đường cao là:<br>$\to$ **$7{,}2\text{ cm}$** | $\triangle$ vuông cạnh $5\text{ cm}, 12\text{ cm}$ có cạnh huyền là:<br>$\to$ **$13\text{ cm}$** | $\triangle$ vuông cạnh $3\text{ cm}, 4\text{ cm}$ có đường cao là:<br>$\to$ **$2{,}4\text{ cm}$** |
| **9** | Tính chất hai tiếp tuyến cắt nhau | Tiếp tuyến tại $B, C$ của $(O)$ cắt nhau tại $A \implies OA \perp$<br>$\to$ **$BC$** | Tiếp tuyến tại $B, C$ của $(O)$ cắt nhau tại $A \implies AB =$<br>$\to$ **$AC$** | Tiếp tuyến tại $B, C$ của $(O)$ cắt ở $A \implies$ phân giác $\widehat{BAC}$ là:<br>$\to$ **$AO$** | Tiếp tuyến tại $B, C$ của $(O)$ cắt ở $A \implies$ phân giác $\widehat{BOC}$ là:<br>$\to$ **$OA$** |
| **10** | Toán thực tế bánh xe lăn | Bánh xe $d = 50\text{ cm}$, lăn $10$ vòng đi được:<br>$\to$ **$5\pi\text{ m}$** | Bánh xe $d = 60\text{ cm}$, lăn $10$ vòng đi được:<br>$\to$ **$6\pi\text{ m}$** | Bánh xe $d = 70\text{ cm}$, lăn $10$ vòng đi được:<br>$\to$ **$7\pi\text{ m}$** | Bánh xe $d = 80\text{ cm}$, lăn $10$ vòng đi được:<br>$\to$ **$8\pi\text{ m}$** |

---

### 2. CÂU 11 (2,5 ĐIỂM - ĐẠI SỐ TỔNG HỢP - TRANG 1)

* **Mã đề 101:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 2x + y = 5 \\ 3x - 2y = 4 \end{cases} \implies \begin{cases} x = 2 \\ y = 1 \end{cases}$.
  - $b)$ (1,25 điểm): Cho $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} + 2} + \dfrac{4\sqrt{x}}{x - 4}\right) : \dfrac{\sqrt{x} + 2}{x - 4}$ với $x \ge 0, x \neq 4$. Rút gọn $P = \sqrt{x}$; tại $x = 9 \implies P = 3$.

* **Mã đề 102:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 3x + y = 7 \\ 2x - 3y = 1 \end{cases} \implies \begin{cases} x = 2 \\ y = 1 \end{cases}$.
  - $b)$ (1,25 điểm): Cho $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} + 3} + \dfrac{6\sqrt{x}}{x - 9}\right) : \dfrac{\sqrt{x} + 3}{x - 9}$ với $x \ge 0, x \neq 9$. Rút gọn $P = \sqrt{x}$; tại $x = 16 \implies P = 4$.

* **Mã đề 103:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 2x - y = 3 \\ x + 2y = 4 \end{cases} \implies \begin{cases} x = 2 \\ y = 1 \end{cases}$.
  - $b)$ (1,25 điểm): Cho $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 1} - \dfrac{2\sqrt{x}}{x - 1}\right) : \dfrac{\sqrt{x} - 1}{x - 1}$ với $x \ge 0, x \neq 1$. Rút gọn $P = \sqrt{x}$; tại $x = 25 \implies P = 5$.

* **Mã đề 104:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} x + 2y = 5 \\ 3x - y = 1 \end{cases} \implies \begin{cases} x = 1 \\ y = 2 \end{cases}$.
  - $b)$ (1,25 điểm): Cho $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} - 2} - \dfrac{4\sqrt{x}}{x - 4}\right) : \dfrac{\sqrt{x} - 2}{x - 4}$ với $x \ge 0, x \neq 4$. Rút gọn $P = \sqrt{x}$; tại $x = 9 \implies P = 3$.

---

### 3. CÂU 12 (2,5 ĐIỂM - TOÁN THỰC TẾ LẬP HỆ PHƯƠNG TRÌNH - TRANG 2)

* **Mã đề 101:** $S = 180\text{ km}, t = 2\text{ h}, v_1 - v_2 = 10\text{ km/h} \implies v_1 = 50, v_2 = 40\text{ km/h}$.
* **Mã đề 102:** $S = 150\text{ km}, t = 1{,}5\text{ h}, v_1 - v_2 = 20\text{ km/h} \implies v_1 = 60, v_2 = 40\text{ km/h}$.
* **Mã đề 103:** $S = 210\text{ km}, t = 2\text{ h}, v_1 - v_2 = 15\text{ km/h} \implies v_1 = 60, v_2 = 45\text{ km/h}$.
* **Mã đề 104:** $S = 160\text{ km}, t = 2\text{ h}, v_1 - v_2 = 20\text{ km/h} \implies v_1 = 50, v_2 = 30\text{ km/h}$.

---

### 4. CÂU 13 (2,5 ĐIỂM - HÌNH HỌC TIẾP TUYẾN & CHỨNG MINH ĐỒNG DẠNG - TRANG 2)

* **Đề bài chung:** Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với đường tròn $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
  - $a)$ (1,25 điểm): Chứng minh bốn điểm $A, B, O, C$ cùng thuộc một đường tròn.
    * $\triangle ABO$ vuông tại $B \implies A, B, O$ cùng thuộc đường tròn đường kính $AO$.
    * $\triangle ACO$ vuông tại $C \implies A, C, O$ cùng thuộc đường tròn đường kính $AO$.
    * Kết luận bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $AO$.
  - $b)$ (1,25 điểm): Chứng minh $OA \perp BC$ tại $H$ và $\triangle OHB \backsim \triangle OBA$, từ đó suy ra $OH \cdot OA = R^2$.
    * $AB = AC, OB = OC = R \implies OA$ là đường trung trực của $BC \implies OA \perp BC$ tại $H$.
    * $\triangle OHB$ và $\triangle OBA$ có $\widehat{OHB} = \widehat{OBA} = 90^\circ$ và góc $\widehat{O}$ chung $\implies \triangle OHB \backsim \triangle OBA$ (g-g).
    * Suy ra $\dfrac{OH}{OB} = \dfrac{OB}{OA} \implies OH \cdot OA = OB^2 = R^2$.
* **Hình vẽ TikZ:** Vẽ sẵn 1 đường tròn $(O)$ cùng tâm $O$ trong khung đề bài.
