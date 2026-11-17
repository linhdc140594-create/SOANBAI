# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 11 - BUỔI 02 (TOÁN 9)
## CHỦ ĐỀ: BÀI 15: DIỆN TÍCH HÌNH QUẠT TRÒN VÀ HÌNH VÀNH KHUYÊN - RÚT GỌN CĂN THỨC NÂNG CAO & TOÁN PHẦN TRĂM KINH TẾ
### Bám sát chương trình: SGK Toán 9 - Kết nối tri thức với cuộc sống (Chương V) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững công thức diện tích hình tròn $S = \pi R^2$.
   - Nắm vững công thức diện tích hình quạt tròn bán kính $R$, cung $n^\circ$: $S_q = \dfrac{\pi R^2 n}{360} = \dfrac{l R}{2}$.
   - Nắm vững công thức diện tích hình vành khuyên giới hạn bởi hai đường tròn đồng tâm $(O; R)$ và $(O; r)$ ($R > r$): $S_{vk} = \pi(R^2 - r^2)$.
   - Vận dụng phối hợp tính chất hai tiếp tuyến cắt nhau, nhận biết tam giác đều / hình vuông để tính góc ở tâm $\widehat{BOC}$, tính diện tích hình quạt tròn và hình vành khuyên.
   - Củng cố Đại số: Giải hệ phương trình chứa căn bậc hai dạng đặt ẩn phụ; Rút gọn biểu thức chứa căn bậc hai và tìm $x$ nguyên để biểu thức nhận giá trị nguyên ($P(x) \in \mathbb{Z}$).
   - Giải bài toán bằng cách lập hệ phương trình: Dạng toán kinh tế, thương mại, mua sắm giảm giá theo phần trăm theo giá niêm yết.

2. **Kỹ năng & Năng lực:**
   - Vẽ hình hai tiếp tuyến cắt nhau và hai đường tròn đồng tâm chính xác bằng TikZ.
   - Trình bày bài giải mạch lạc, khoa học, lập luận hình học chặt chẽ.
   - Kỹ năng biến đổi đại số tìm nghiệm nguyên chuẩn barem chấm thi tuyển sinh vào Lớp 10.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: đúng 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Vị trí trên đề | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | Trang 1 (Đầu) | Trả lời ngắn, lệnh `\shortans`, ô kết quả bo góc mép phải thẳng hàng, 1 dòng/câu. |
| **Câu 11** | 2 ý ($a, b$) | **2,5 đ** *(1,25 đ/ý)* | Trang 1 (Cuối) | Đại số tổng hợp (Hệ PT chứa căn & Rút gọn tìm $x \in \mathbb{Z}$). Bảng $1 \times 2$, dùng **`\oBaiTap[20]`** lấp kín đáy Trang 1. |
| **Câu 12** | 1 bài | **2,5 đ** | Trang 2 (Đầu) | Giải bài toán bằng cách lập hệ phương trình (Toán kinh tế phần trăm). Box `tabularx`, bài giải **`\dongke{16}`**. |
| **Câu 13** | 2 ý ($a, b$) | **2,5 đ** *(1,25 đ/ý)* | Trang 2 (Cuối) | Bài toán Hình học diện tích quạt tròn & vành khuyên (có hình TikZ). Box `tabularx`, bài giải **`\dongke{16}`** sát đáy Trang 2. |
| **Tổng cộng** | **15 câu/ý** | **10,0 đ** | **2 mặt A4** | **Chuẩn tuyệt đối 8 trang PDF cho 4 mã đề, lề dưới 10 - 14 mm.** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Tính diện tích quạt tròn | $(O; 6\text{ cm})$, quạt $60^\circ \implies S_q =$ **$6\pi\text{ cm}^2$** | $(O; 8\text{ cm})$, quạt $45^\circ \implies S_q =$ **$8\pi\text{ cm}^2$** | $(O; 6\text{ cm})$, quạt $90^\circ \implies S_q =$ **$9\pi\text{ cm}^2$** | $(O; 12\text{ cm})$, quạt $30^\circ \implies S_q =$ **$12\pi\text{ cm}^2$** |
| **2** | Bán kính từ diện tích hình tròn | Diện tích $S = 64\pi\text{ cm}^2 \implies R =$ **$8\text{ cm}$** | Diện tích $S = 81\pi\text{ cm}^2 \implies R =$ **$9\text{ cm}$** | Diện tích $S = 100\pi\text{ cm}^2 \implies R =$ **$10\text{ cm}$** | Diện tích $S = 49\pi\text{ cm}^2 \implies R =$ **$7\text{ cm}$** |
| **3** | Diện tích hình vành khuyên | Đồng tâm $R=5, r=3\text{ cm} \implies S =$ **$16\pi\text{ cm}^2$** | Đồng tâm $R=10, r=6\text{ cm} \implies S =$ **$64\pi\text{ cm}^2$** | Đồng tâm $R=13, r=5\text{ cm} \implies S =$ **$144\pi\text{ cm}^2$** | Đồng tâm $R=5, r=4\text{ cm} \implies S =$ **$9\pi\text{ cm}^2$** |
| **4** | Trục căn thức ở mẫu | $\dfrac{2}{\sqrt{3} - 1} =$ **$\sqrt{3} + 1$** | $\dfrac{2}{\sqrt{5} - 1} =$ **$\dfrac{\sqrt{5} + 1}{2}$** | $\dfrac{4}{\sqrt{5} - 1} =$ **$\sqrt{5} + 1$** | $\dfrac{3}{\sqrt{7} - 2} =$ **$\sqrt{7} + 2$** |
| **5** | So sánh căn thức bậc hai | So sánh $3\sqrt{2}$ và $\sqrt{19}$: **$<$** | So sánh $2\sqrt{5}$ và $\sqrt{21}$: **$<$** | So sánh $4\sqrt{2}$ và $\sqrt{31}$: **$>$** | So sánh $3\sqrt{3}$ và $\sqrt{26}$: **$>$** |
| **6** | Khai căn bậc ba số học | $\sqrt[3]{-64} =$ **$-4$** | $\sqrt[3]{-125} =$ **$-5$** | $\sqrt[3]{-27} =$ **$-3$** | $\sqrt[3]{-216} =$ **$-6$** |
| **7** | Điều kiện xác định căn thức | $\sqrt{\dfrac{1}{x - 2}}$ xác định khi: **$x > 2$** | $\sqrt{\dfrac{1}{x - 3}}$ xác định khi: **$x > 3$** | $\sqrt{\dfrac{1}{x - 5}}$ xác định khi: **$x > 5$** | $\sqrt{\dfrac{1}{x - 4}}$ xác định khi: **$x > 4$** |
| **8** | Góc chắn nửa đường tròn | Số đo góc nội tiếp chắn nửa đường tròn: **$90^\circ$** | $\Delta$ nội tiếp có 1 cạnh là đường kính là: **tam giác vuông** | Tâm đường tròn ngoại tiếp $\Delta$ vuông là: **trung điểm cạnh huyền** | Bán kính ngoại tiếp $\Delta$ vuông cạnh huyền $10$: **$5\text{ cm}$** |
| **9** | Tính chất hai tiếp tuyến | Tiếp tuyến tại $B, C$ cắt tại $A \implies AB =$ **$AC$** | Tiếp tuyến tại $B, C$ cắt tại $A \implies OA$ phân giác: **$\widehat{BOC}$** | Tiếp tuyến tại $B, C$ cắt tại $A \implies OA \perp$ **$BC$** | $OA$ cắt $BC$ tại $H \implies$ khoảng cách $d(O, BC) =$ **$OH$** |
| **10** | Toán thực tế mặt quạt xòe | Quạt $R = 24\text{ cm}$, góc $150^\circ \implies S =$ **$240\pi\text{ cm}^2$** | Quạt $R = 20\text{ cm}$, góc $144^\circ \implies S =$ **$160\pi\text{ cm}^2$** | Quạt $R = 18\text{ cm}$, góc $120^\circ \implies S =$ **$108\pi\text{ cm}^2$** | Quạt $R = 30\text{ cm}$, góc $108^\circ \implies S =$ **$270\pi\text{ cm}^2$** |

---

### 2. CÂU 11 (2,5 ĐIỂM - ĐẠI SỐ TỔNG HỢP - TRANG 1)

* **Mã đề 101:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 2\sqrt{x - 1} + \dfrac{1}{y + 2} = 5 \\ 3\sqrt{x - 1} - \dfrac{2}{y + 2} = 4 \end{cases}$. *(Đáp số: $(x; y) = (5; -1)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \dfrac{\sqrt{x} + 2}{\sqrt{x} - 1}$ với $x \ge 0, x \neq 1$. Tìm tất cả các giá trị nguyên của $x$ để $P$ nhận giá trị nguyên. *(Đáp số: $x \in \{0; 4; 16\}$)*

* **Mã đề 102:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} \sqrt{x + 2} + \dfrac{2}{y - 1} = 4 \\ 2\sqrt{x + 2} - \dfrac{3}{y - 1} = 1 \end{cases}$. *(Đáp số: $(x; y) = (2; 2)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \dfrac{\sqrt{x} + 3}{\sqrt{x} - 1}$ với $x \ge 0, x \neq 1$. Tìm tất cả các giá trị nguyên của $x$ để $P$ nhận giá trị nguyên. *(Đáp số: $x \in \{0; 4; 9; 25\}$)*

* **Mã đề 103:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 3\sqrt{x - 2} + \dfrac{1}{y + 1} = 7 \\ 2\sqrt{x - 2} - \dfrac{1}{y + 1} = 3 \end{cases}$. *(Đáp số: $(x; y) = (6; 0)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \dfrac{\sqrt{x} + 1}{\sqrt{x} - 2}$ với $x \ge 0, x \neq 4$. Tìm tất cả các giá trị nguyên của $x$ để $P$ nhận giá trị nguyên. *(Đáp số: $x \in \{1; 9; 25\}$)*

* **Mã đề 104:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 2\sqrt{x + 1} + \dfrac{3}{y - 2} = 7 \\ \sqrt{x + 1} - \dfrac{2}{y - 2} = 0 \end{cases}$. *(Đáp số: $(x; y) = (3; 3)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \dfrac{\sqrt{x} + 2}{\sqrt{x} - 2}$ với $x \ge 0, x \neq 4$. Tìm tất cả các giá trị nguyên của $x$ để $P$ nhận giá trị nguyên. *(Đáp số: $x \in \{1; 9; 16; 36\}$)*

---

### 3. CÂU 12 (2,5 ĐIỂM - TOÁN THỰC TẾ LẬP HỆ PHƯƠNG TRÌNH - TRANG 2)

* **Mã đề 101:** Bác An mua một chiếc áo và một đôi giày với tổng giá niêm yết là $800\,000$ đồng. Nhân dịp khuyến mãi, chiếc áo được giảm giá $15\%$, đôi giày được giảm giá $20\%$, do đó bác An chỉ phải trả tổng cộng $665\,000$ đồng. Hỏi giá niêm yết của mỗi món đồ là bao nhiêu?
  - *Đáp số:* Gọi giá niêm yết của áo và giày lần lượt là $x, y$ (đồng, $0 < x, y < 800\,000$).
    Hệ: $\begin{cases} x + y = 800\,000 \\ 0{,}85x + 0{,}80y = 665\,000 \end{cases} \implies \begin{cases} x = 500\,000 \\ y = 300\,000 \end{cases}$. Áo $500\,000$ đ, Giày $300\,000$ đ.

* **Mã đề 102:** Bạn Nam mua một chiếc cặp sách và một bộ dụng cụ học tập với tổng giá niêm yết là $500\,000$ đồng. Nhân dịp đầu năm học, chiếc cặp sách được giảm giá $20\%$, bộ dụng cụ được giảm giá $10\%$, do đó bạn Nam chỉ phải trả tổng cộng $420\,000$ đồng. Hỏi giá niêm yết của mỗi món đồ là bao nhiêu?
  - *Đáp số:* Hệ: $\begin{cases} x + y = 500\,000 \\ 0{,}80x + 0{,}90y = 420\,000 \end{cases} \implies \begin{cases} x = 300\,000 \\ y = 200\,000 \end{cases}$. Cặp $300\,000$ đ, Dụng cụ $200\,000$ đ.

* **Mã đề 103:** Mẹ mua một chiếc quạt điện và một chiếc ấm siêu tốc với tổng giá niêm yết là $900\,000$ đồng. Nhân dịp cuối tuần, quạt điện được giảm giá $10\%$, ấm siêu tốc được giảm giá $15\%$, do đó mẹ chỉ phải trả tổng cộng $790\,000$ đồng. Hỏi giá niêm yết của mỗi món đồ là bao nhiêu?
  - *Đáp số:* Hệ: $\begin{cases} x + y = 900\,000 \\ 0{,}90x + 0{,}85y = 790\,000 \end{cases} \implies \begin{cases} x = 500\,000 \\ y = 400\,000 \end{cases}$. Quạt $500\,000$ đ, Ấm $400\,000$ đ.

* **Mã đề 104:** Bác Bình mua một chiếc xe đạp và một chiếc mũ bảo hiểm với tổng giá niêm yết là $2\,400\,000$ đồng. Trong đợt tri ân khách hàng, xe đạp được giảm giá $10\%$, mũ bảo hiểm được giảm giá $25\%$, do đó bác Bình chỉ phải trả tổng cộng $2\,100\,000$ đồng. Hỏi giá niêm yết của mỗi món đồ là bao nhiêu?
  - *Đáp số:* Hệ: $\begin{cases} x + y = 2\,400\,000 \\ 0{,}90x + 0{,}75y = 2\,100\,000 \end{cases} \implies \begin{cases} x = 2\,000\,000 \\ y = 400\,000 \end{cases}$. Xe $2\,000\,000$ đ, Mũ $400\,000$ đ.

---

### 4. CÂU 13 (2,5 ĐIỂM - HÌNH HỌC DIỆN TÍCH QUẠT TRÒN & VÀNH KHUYÊN - TRANG 2)

* **Mã đề 101:** Cho đường tròn $(O; R)$ có bán kính $R = 6\text{ cm}$. Từ điểm $A$ nằm ngoài $(O)$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm) sao cho $\widehat{BAC} = 60^\circ$.
  - $a)$ (1,25 điểm): Chứng minh tam giác $ABC$ đều. Tính số đo góc ở tâm $\widehat{BOC}$ và tính diện tích hình quạt tròn $BOC$ ứng với cung nhỏ $\wideparen{BC}$. *(Đáp số: $\widehat{BOC} = 120^\circ; S_q = \dfrac{\pi \cdot 6^2 \cdot 120}{360} = 12\pi\text{ cm}^2$)*
  - $b)$ (1,25 điểm): Kẻ đường tròn $(O; r)$ đồng tâm với $(O)$ có bán kính $r = 3\text{ cm}$. Tính diện tích hình vành khuyên giới hạn bởi hai đường tròn $(O; R)$ và $(O; r)$. *(Đáp số: $S_{vk} = \pi(6^2 - 3^2) = 27\pi\text{ cm}^2$)*

* **Mã đề 102:** Cho đường tròn $(O; R)$ có bán kính $R = 9\text{ cm}$. Từ điểm $A$ nằm ngoài $(O)$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm) sao cho $\widehat{BAC} = 60^\circ$.
  - $a)$ (1,25 điểm): Chứng minh tam giác $ABC$ đều. Tính số đo góc ở tâm $\widehat{BOC}$ và tính diện tích hình quạt tròn $BOC$ ứng với cung nhỏ $\wideparen{BC}$. *(Đáp số: $\widehat{BOC} = 120^\circ; S_q = \dfrac{\pi \cdot 9^2 \cdot 120}{360} = 27\pi\text{ cm}^2$)*
  - $b)$ (1,25 điểm): Kẻ đường tròn $(O; r)$ đồng tâm với $(O)$ có bán kính $r = 6\text{ cm}$. Tính diện tích hình vành khuyên giới hạn bởi hai đường tròn $(O; R)$ và $(O; r)$. *(Đáp số: $S_{vk} = \pi(9^2 - 6^2) = 45\pi\text{ cm}^2$)*

* **Mã đề 103:** Cho đường tròn $(O; R)$ có bán kính $R = 8\text{ cm}$. Từ điểm $A$ nằm ngoài $(O)$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm) sao cho $AB \perp AC$ (hay $\widehat{BAC} = 90^\circ$).
  - $a)$ (1,25 điểm): Chứng minh tứ giác $ABOC$ là hình vuông. Tính diện tích hình quạt tròn $BOC$ ứng với cung nhỏ $\wideparen{BC}$. *(Đáp số: $\widehat{BOC} = 90^\circ; S_q = \dfrac{\pi \cdot 8^2 \cdot 90}{360} = 16\pi\text{ cm}^2$)*
  - $b)$ (1,25 điểm): Kẻ đường tròn $(O; r)$ đồng tâm với $(O)$ có bán kính $r = 4\text{ cm}$. Tính diện tích hình vành khuyên giới hạn bởi hai đường tròn $(O; R)$ và $(O; r)$. *(Đáp số: $S_{vk} = \pi(8^2 - 4^2) = 48\pi\text{ cm}^2$)*

* **Mã đề 104:** Cho đường tròn $(O; R)$ có bán kính $R = 10\text{ cm}$. Từ điểm $A$ nằm ngoài $(O)$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm) sao cho $AB \perp AC$ (hay $\widehat{BAC} = 90^\circ$).
  - $a)$ (1,25 điểm): Chứng minh tứ giác $ABOC$ là hình vuông. Tính diện tích hình quạt tròn $BOC$ ứng với cung nhỏ $\wideparen{BC}$. *(Đáp số: $\widehat{BOC} = 90^\circ; S_q = \dfrac{\pi \cdot 10^2 \cdot 90}{360} = 25\pi\text{ cm}^2$)*
  - $b)$ (1,25 điểm): Kẻ đường tròn $(O; r)$ đồng tâm với $(O)$ có bán kính $r = 6\text{ cm}$. Tính diện tích hình vành khuyên giới hạn bởi hai đường tròn $(O; R)$ và $(O; r)$. *(Đáp số: $S_{vk} = \pi(10^2 - 6^2) = 64\pi\text{ cm}^2$)*
