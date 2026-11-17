# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 11 - BUỔI 01 (TOÁN 9)
## CHỦ ĐỀ: BÀI 15: ĐỘ DÀI CUNG TRÒN & CHU VI ĐƯỜNG TRÒN - GIẢI HỆ PHƯƠNG TRÌNH ẨN PHỤ & TOÁN LÀM CHUNG LÀM RIÊNG
### Bám sát chương trình: SGK Toán 9 - Kết nối tri thức với cuộc sống (Chương V) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững công thức chu vi đường tròn $C = 2\pi R = \pi d$ và công thức tính độ dài cung tròn $n^\circ$ bán kính $R$: $l = \dfrac{\pi R n}{180}$.
   - Biết tính độ dài cung tròn khi biết góc ở tâm và bán kính; ngược lại tính bán kính hoặc số đo độ của cung tròn khi biết độ dài cung.
   - Vận dụng tính chất hai tiếp tuyến cắt nhau để chứng minh quan hệ vuông góc $OA \perp BC$, tính góc ở tâm $\widehat{BOC}$, tính độ dài cung nhỏ và cung lớn của đường tròn.
   - Vận dụng tính chất góc nội tiếp chắn nửa đường tròn để chứng minh đường thẳng vuông góc và quan hệ song song $CD \parallel OA$.
   - Củng cố Đại số: Giải hệ phương trình bậc nhất hai ẩn bằng phương pháp đặt ẩn phụ dạng phân thức; Rút gọn biểu thức phân thức chứa căn bậc hai $P(x)$ và tính giá trị tại điểm chính phương.
   - Giải bài toán bằng cách lập hệ phương trình: Dạng toán làm việc chung - làm việc riêng (khối lượng công việc).

2. **Kỹ năng & Năng lực:**
   - Dựng hình đường tròn, hai tiếp tuyến cắt nhau và đường kính bằng TikZ chính xác, trực quan.
   - Trình bày bài giải hình học lập luận chặt chẽ: "giả thiết $\to$ định lí $\to$ kết luận", không nhảy bước.
   - Trình bày bài toán tự luận chuẩn barem chấm thi tuyển sinh vào Lớp 10 của các Sở GD&ĐT.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: đúng 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Vị trí trên đề | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | Trang 1 (Đầu) | Trả lời ngắn, lệnh `\shortans`, ô kết quả bo góc mép phải thẳng hàng, 1 dòng/câu. |
| **Câu 11** | 2 ý ($a, b$) | **2,5 đ** *(1,25 đ/ý)* | Trang 1 (Cuối) | Đại số tổng hợp (Hệ PT ẩn phụ & Rút gọn căn). Bảng $1 \times 2$, dùng **`\oBaiTap[20]`** lấp kín đáy Trang 1. |
| **Câu 12** | 1 bài | **2,5 đ** | Trang 2 (Đầu) | Giải bài toán bằng cách lập hệ phương trình (Toán làm chung làm riêng). Box `tabularx`, bài giải **`\dongke{16}`**. |
| **Câu 13** | 2 ý ($a, b$) | **2,5 đ** *(1,25 đ/ý)* | Trang 2 (Cuối) | Bài toán Hình học tiếp tuyến + độ dài cung tròn (có hình TikZ). Box `tabularx`, bài giải **`\dongke{16}`** sát đáy Trang 2. |
| **Tổng cộng** | **15 câu/ý** | **10,0 đ** | **2 mặt A4** | **Chuẩn tuyệt đối 8 trang PDF cho 4 mã đề, lề dưới 10 - 14 mm.** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Tính độ dài cung tròn | $(O; 6\text{ cm})$, cung $60^\circ \implies l =$ **$2\pi\text{ cm}$** | $(O; 9\text{ cm})$, cung $40^\circ \implies l =$ **$2\pi\text{ cm}$** | $(O; 4\text{ cm})$, cung $90^\circ \implies l =$ **$2\pi\text{ cm}$** | $(O; 10\text{ cm})$, cung $36^\circ \implies l =$ **$2\pi\text{ cm}$** |
| **2** | Bán kính từ chu vi đường tròn | Chu vi $C = 16\pi\text{ cm} \implies R =$ **$8\text{ cm}$** | Chu vi $C = 18\pi\text{ cm} \implies R =$ **$9\text{ cm}$** | Chu vi $C = 20\pi\text{ cm} \implies R =$ **$10\text{ cm}$** | Chu vi $C = 12\pi\text{ cm} \implies R =$ **$6\text{ cm}$** |
| **3** | Số đo cung từ độ dài cung | $R=12\text{ cm}, l=3\pi\text{ cm} \implies n =$ **$45^\circ$** | $R=10\text{ cm}, l=5\pi\text{ cm} \implies n =$ **$90^\circ$** | $R=18\text{ cm}, l=6\pi\text{ cm} \implies n =$ **$60^\circ$** | $R=15\text{ cm}, l=2{,}5\pi\text{ cm} \implies n =$ **$30^\circ$** |
| **4** | Căn bậc hai số học | Căn bậc hai số học của $144$ là: **$12$** | Căn bậc hai số học của $169$ là: **$13$** | Căn bậc hai số học của $196$ là: **$14$** | Căn bậc hai số học của $225$ là: **$15$** |
| **5** | Điều kiện xác định căn thức | $\sqrt{2x - 8}$ xác định khi: **$x \ge 4$** | $\sqrt{3x - 12}$ xác định khi: **$x \ge 4$** | $\sqrt{5x - 15}$ xác định khi: **$x \ge 3$** | $\sqrt{4x - 20}$ xác định khi: **$x \ge 5$** |
| **6** | Rút gọn căn thức số học | $\sqrt{50} - \sqrt{18} + \sqrt{8} =$ **$4\sqrt{2}$** | $\sqrt{75} - \sqrt{27} + \sqrt{12} =$ **$4\sqrt{3}$** | $\sqrt{48} - \sqrt{12} + \sqrt{27} =$ **$5\sqrt{3}$** | $\sqrt{32} - \sqrt{8} + \sqrt{18} =$ **$5\sqrt{2}$** |
| **7** | Nghiệm hệ phương trình | $\begin{cases} 3x - y = 7 \\ x + y = 5 \end{cases} \implies (x; y) =$ **$(3; 2)$** | $\begin{cases} 2x - y = 5 \\ x + y = 4 \end{cases} \implies (x; y) =$ **$(3; 1)$** | $\begin{cases} 3x + y = 10 \\ x - y = 2 \end{cases} \implies (x; y) =$ **$(3; 1)$** | $\begin{cases} 2x + y = 8 \\ x - y = 1 \end{cases} \implies (x; y) =$ **$(3; 2)$** |
| **8** | Đường cao tam giác vuông | $\Delta$ vuông cạnh $6\text{ cm}, 8\text{ cm} \implies h =$ **$4{,}8\text{ cm}$** | $\Delta$ vuông cạnh $9\text{ cm}, 12\text{ cm} \implies h =$ **$7{,}2\text{ cm}$** | $\Delta$ vuông cạnh $3\text{ cm}, 4\text{ cm} \implies h =$ **$2{,}4\text{ cm}$** | $\Delta$ vuông cạnh $12\text{ cm}, 16\text{ cm} \implies h =$ **$9{,}6\text{ cm}$** |
| **9** | Tính chất tiếp tuyến | Tiếp tuyến $d$ tại $M$ của $(O)$ vuông góc với $OM$ tại: **tiếp điểm $M$** | Đường thẳng vuông góc bán kính tại điểm trên $(O)$ là: **tiếp tuyến** | Số tiếp tuyến kẻ từ điểm ngoài đường tròn tới $(O)$ là: **$2$** | Khoảng cách từ tâm tới tiếp tuyến của $(O; R)$ là: **$R$** |
| **10** | Toán thực tế bánh xe lăn | Bánh xe $d = 60\text{ cm}$, lăn $10$ vòng đi được: **$6\pi\text{ m}$** | Bánh xe $d = 70\text{ cm}$, lăn $10$ vòng đi được: **$7\pi\text{ m}$** | Bánh xe $d = 50\text{ cm}$, lăn $10$ vòng đi được: **$5\pi\text{ m}$** | Bánh xe $d = 80\text{ cm}$, lăn $10$ vòng đi được: **$8\pi\text{ m}$** |

---

### 2. CÂU 11 (2,5 ĐIỂM - ĐẠI SỐ TỔNG HỢP - TRANG 1)

* **Mã đề 101:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 2x - 3y = 1 \\ 3x + 2y = 8 \end{cases}$. *(Đáp số: $(x; y) = (2; 1)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} + 2} + \dfrac{4\sqrt{x}}{x - 4}\right) : \dfrac{\sqrt{x} + 2}{x - 4}$ với $x \ge 0, x \neq 4$. Rút gọn $P$ và tính giá trị của $P$ tại $x = 9$. *(Đáp số: $P = \sqrt{x}$; tại $x = 9 \implies P = 3$)*

* **Mã đề 102:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 3x + 2y = 7 \\ 2x - 3y = -4 \end{cases}$. *(Đáp số: $(x; y) = (1; 2)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} + 3} + \dfrac{6\sqrt{x}}{x - 9}\right) : \dfrac{\sqrt{x} + 3}{x - 9}$ với $x \ge 0, x \neq 9$. Rút gọn $P$ và tính giá trị của $P$ tại $x = 16$. *(Đáp số: $P = \sqrt{x}$; tại $x = 16 \implies P = 4$)*

* **Mã đề 103:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 3x - 2y = 4 \\ 2x + 3y = 7 \end{cases}$. *(Đáp số: $(x; y) = (2; 1)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} + 1} + \dfrac{2\sqrt{x}}{x - 1}\right) : \dfrac{\sqrt{x} + 1}{x - 1}$ với $x \ge 0, x \neq 1$. Rút gọn $P$ và tính giá trị của $P$ tại $x = 25$. *(Đáp số: $P = \sqrt{x}$; tại $x = 25 \implies P = 5$)*

* **Mã đề 104:**
  - $a)$ (1,25 điểm): Giải hệ phương trình: $\begin{cases} 2x + 3y = 8 \\ 3x - 2y = -1 \end{cases}$. *(Đáp số: $(x; y) = (1; 2)$)*
  - $b)$ (1,25 điểm): Cho biểu thức $P = \left(\dfrac{\sqrt{x}}{\sqrt{x} + 4} + \dfrac{8\sqrt{x}}{x - 16}\right) : \dfrac{\sqrt{x} + 4}{x - 16}$ với $x \ge 0, x \neq 16$. Rút gọn $P$ và tính giá trị của $P$ tại $x = 4$. *(Đáp số: $P = \sqrt{x}$; tại $x = 4 \implies P = 2$)*

---

### 3. CÂU 12 (2,5 ĐIỂM - TOÁN THỰC TẾ LẬP HỆ PHƯƠNG TRÌNH - TRANG 2)

* **Mã đề 101:** Hai tổ công nhân cùng làm chung một công việc thì hoàn thành trong $12$ giờ. Nếu tổ I làm trong $4$ giờ rồi nghỉ, tổ II làm tiếp trong $9$ giờ thì cả hai tổ hoàn thành được $\dfrac{7}{12}$ công việc. Hỏi nếu làm riêng thì mỗi tổ hoàn thành công việc đó trong bao lâu?
  - *Đáp số:* Gọi thời gian tổ I, tổ II làm riêng là $x, y$ (giờ, $x, y > 12$). Hệ: $\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{12} \\ \dfrac{4}{x} + \dfrac{9}{y} = \dfrac{7}{12} \end{cases} \implies \begin{cases} x = 30 \\ y = 20 \end{cases}$. Tổ I làm riêng trong $30$ giờ, Tổ II làm riêng trong $20$ giờ.

* **Mã đề 102:** Hai đội công nhân cùng sửa một đoạn đường thì hoàn thành trong $12$ ngày. Nếu đội I làm trong $3$ ngày rồi nghỉ, đội II làm tiếp trong $8$ ngày thì cả hai đội sửa được $\dfrac{1}{2}$ đoạn đường. Hỏi nếu làm riêng thì mỗi đội sửa xong đoạn đường trong bao lâu?
  - *Đáp số:* Hệ: $\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{12} \\ \dfrac{3}{x} + \dfrac{8}{y} = \dfrac{1}{2} \end{cases} \implies \begin{cases} x = 30 \\ y = 20 \end{cases}$. Đội I sửa trong $30$ ngày, Đội II sửa trong $20$ ngày.

* **Mã đề 103:** Hai vòi nước cùng chảy vào một bể cạn thì đầy bể sau $6$ giờ. Nếu mở vòi I chảy trong $2$ giờ rồi khóa lại và mở vòi II chảy tiếp trong $5$ giờ thì cả hai vòi chảy được $\dfrac{8}{15}$ bể nước. Hỏi nếu chảy riêng thì mỗi vòi chảy đầy bể trong bao lâu?
  - *Đáp số:* Hệ: $\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{6} \\ \dfrac{2}{x} + \dfrac{5}{y} = \dfrac{8}{15} \end{cases} \implies \begin{cases} x = 10 \\ y = 15 \end{cases}$. Vòi I chảy trong $10$ giờ, Vòi II chảy trong $15$ giờ.

* **Mã đề 104:** Hai vòi nước cùng chảy vào một bể cạn thì đầy bể sau $4$ giờ. Nếu mở vòi I chảy trong $3$ giờ rồi khóa lại và mở vòi II chảy tiếp trong $2$ giờ thì cả hai vòi chảy được $\dfrac{2}{3}$ bể nước. Hỏi nếu chảy riêng thì mỗi vòi chảy đầy bể trong bao lâu?
  - *Đáp số:* Hệ: $\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{4} \\ \dfrac{3}{x} + \dfrac{2}{y} = \dfrac{2}{3} \end{cases} \implies \begin{cases} x = 6 \\ y = 12 \end{cases}$. Vòi I chảy trong $6$ giờ, Vòi II chảy trong $12$ giờ.

---

### 4. CÂU 13 (2,5 ĐIỂM - HÌNH HỌC TIẾP TUYẾN & ĐỘ DÀI CUNG TRÒN - TRANG 2)

* **Mã đề 101:** Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
  - $a)$ (1,25 điểm): Chứng minh $OA \perp BC$ tại $H$. Cho $R = 6\text{ cm}$ và $\widehat{BOC} = 120^\circ$, hãy tính độ dài cung nhỏ $\wideparen{BC}$ của đường tròn $(O)$. *(Đáp số: $l = \dfrac{\pi \cdot 6 \cdot 120}{180} = 4\pi\text{ cm}$)*
  - $b)$ (1,25 điểm): Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \parallel OA$.

* **Mã đề 102:** Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
  - $a)$ (1,25 điểm): Chứng minh $OA \perp BC$ tại $H$. Cho $R = 9\text{ cm}$ và $\widehat{BOC} = 80^\circ$, hãy tính độ dài cung nhỏ $\wideparen{BC}$ của đường tròn $(O)$. *(Đáp số: $l = \dfrac{\pi \cdot 9 \cdot 80}{180} = 4\pi\text{ cm}$)*
  - $b)$ (1,25 điểm): Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \parallel OA$.

* **Mã đề 103:** Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
  - $a)$ (1,25 điểm): Chứng minh $OA \perp BC$ tại $H$. Cho $R = 8\text{ cm}$ và $\widehat{BOC} = 90^\circ$, hãy tính độ dài cung nhỏ $\wideparen{BC}$ của đường tròn $(O)$. *(Đáp số: $l = \dfrac{\pi \cdot 8 \cdot 90}{180} = 4\pi\text{ cm}$)*
  - $b)$ (1,25 điểm): Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \parallel OA$.

* **Mã đề 104:** Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
  - $a)$ (1,25 điểm): Chứng minh $OA \perp BC$ tại $H$. Cho $R = 12\text{ cm}$ và $\widehat{BOC} = 60^\circ$, hãy tính độ dài cung nhỏ $\wideparen{BC}$ của đường tròn $(O)$. *(Đáp số: $l = \dfrac{\pi \cdot 12 \cdot 60}{180} = 4\pi\text{ cm}$)*
  - $b)$ (1,25 điểm): Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \parallel OA$.
