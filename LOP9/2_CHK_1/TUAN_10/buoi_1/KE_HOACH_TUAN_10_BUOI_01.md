# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 10 - BUỔI 01 (TOÁN 9)
## CHỦ ĐỀ: VỊ TRÍ TƯƠNG ĐỐI CỦA ĐƯỜNG THẲNG VÀ ĐƯỜNG TRÒN - TIẾP TUYẾN
### Bám sát chương trình: SGK Toán 9 - Kết nối tri thức với cuộc sống (Chương V) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững 3 vị trí tương đối của đường thẳng và đường tròn dựa trên hệ thức giữa khoảng cách $d$ từ tâm đến đường thẳng và bán kính $R$: không giao nhau ($d > R$), tiếp xúc ($d = R$), cắt nhau ($d < R$).
   - Nắm vững định nghĩa và tính chất của tiếp tuyến: tiếp tuyến vuông góc với bán kính tại tiếp điểm.
   - Nắm vững dấu hiệu nhận biết tiếp tuyến của đường tròn: nếu một đường thẳng đi qua một điểm của đường tròn và vuông góc với bán kính đi qua điểm đó thì đường thẳng đó là tiếp tuyến của đường tròn.
   - Vận dụng thành thạo tính chất đường trung trực, tam giác bằng nhau để chứng minh một đường thẳng là tiếp tuyến.
   - Củng cố Đại số: Giải hệ hai phương trình bậc nhất hai ẩn bằng phương pháp đặt ẩn phụ; Rút gọn biểu thức phân thức chứa căn bậc hai và tính giá trị tại điểm chính phương.
   - Giải bài toán bằng cách lập hệ phương trình (dạng toán chuyển động ca nô trên sông xuôi dòng và ngược dòng).

2. **Kỹ năng:**
   - Kỹ năng vẽ hình tiếp tuyến của đường tròn chuẩn xác bằng TikZ, ký hiệu bán kính vuông góc.
   - Trình bày lời giải hình học mạch lạc, lập luận chặt chẽ: "có căn cứ $\to$ suy ra $\to$ kết luận", không nhảy bước.
   - Trình bày bài toán tự luận chuẩn barem chấm thi tuyển sinh vào Lớp 10.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề hoán vị tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Thời gian (phút) | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | 10 | Trả lời ngắn, lệnh `\shortans`, ô kết quả bo góc mép phải, bố trí 2 cột Trang 1. |
| **Câu 11** | 2 ý | **2,5 đ** *(1,25 đ/ý)* | 15 | Đại số tổng hợp (Hệ PT ẩn phụ & Rút gọn căn thức). Bảng $1 \times 2$, dùng **`\oBaiTap[21]`** lấp kín đáy Trang 1. |
| **Câu 12** | 1 bài | **2,5 đ** | 10 | Giải bài toán bằng cách lập hệ phương trình (Toán ca nô xuôi ngược dòng). Box `tabularx`, bài giải **`\dongke{16}`** trên Trang 2. |
| **Câu 13** | 2 ý | **2,5 đ** *(1,25 đ/ý)* | 10 | Bài toán Hình học tiếp tuyến và đường kính (có hình TikZ). Box `tabularx`, bài giải **`\dongke{17}`** chạm sát đáy Trang 2. |
| **Tổng cộng** | **15 câu/ý** | **10,0 đ** | **45** | **Khít mép giấy cả 2 trang, chuẩn 100% cấu trúc thi vào Lớp 10.** |

---

## 🔢 III. BẢNG DỮ LIỆU SỐ HỌC 4 MÃ ĐỀ (HOÀN TOÀN TƯƠNG ĐƯƠNG)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - 2,5 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Vị trí tương đối đường thẳng và $(O)$ | Cho $(O; 4\text{ cm})$, khoảng cách $d = 4\text{ cm}$. Số điểm chung là: **$1$** | Cho $(O; 5\text{ cm})$, khoảng cách $d = 3\text{ cm}$. Số điểm chung là: **$2$** | Cho $(O; 6\text{ cm})$, khoảng cách $d = 7\text{ cm}$. Số điểm chung là: **$0$** | Cho $(O; 5\text{ cm})$, đường thẳng tiếp xúc $(O)$. Khoảng cách $d =$ **$5\text{ cm}$** |
| **2** | Tính chất góc tiếp tuyến | Tiếp tuyến $AB$ của $(O)$ tại tiếp điểm $B$. Số đo $\widehat{ABO} =$ **$90^\circ$** | Tiếp tuyến $Ax$ của $(O)$ tại $A$. Khẳng định đúng là $Ax \dots OA$: **$\perp$** | Tiếp tuyến của $(O)$ vuông góc với bán kính tại: **tiếp điểm** | Đường thẳng $d \perp OA$ tại $A \in (O)$ thì $d$ là: **tiếp tuyến** |
| **3** | Tính độ dài đoạn tiếp tuyến | $(O; 3\text{ cm}), OA = 5\text{ cm}$, tiếp tuyến $AB \implies AB =$ **$4\text{ cm}$** | $(O; 5\text{ cm}), OA = 13\text{ cm}$, tiếp tuyến $AB \implies AB =$ **$12\text{ cm}$** | $(O; 6\text{ cm}), OA = 10\text{ cm}$, tiếp tuyến $AB \implies AB =$ **$8\text{ cm}$** | $(O; 8\text{ cm}), OA = 17\text{ cm}$, tiếp tuyến $AB \implies AB =$ **$15\text{ cm}$** |
| **4** | Căn bậc hai số học | Căn bậc hai số học của $121$ là: **$11$** | Căn bậc hai số học của $144$ là: **$12$** | Căn bậc hai số học của $169$ là: **$13$** | Căn bậc hai số học của $196$ là: **$14$** |
| **5** | Điều kiện xác định căn thức | ĐKXĐ của $\sqrt{3x - 9}$ là: **$x \ge 3$** | ĐKXĐ của $\sqrt{4x - 16}$ là: **$x \ge 4$** | ĐKXĐ của $\sqrt{5x - 15}$ là: **$x \ge 3$** | ĐKXĐ của $\sqrt{2x - 10}$ là: **$x \ge 5$** |
| **6** | Rút gọn căn thức số | Tính: $\sqrt{32} - \sqrt{18} + \sqrt{8} =$ **$3\sqrt{2}$** | Tính: $\sqrt{48} - \sqrt{27} + \sqrt{12} =$ **$3\sqrt{3}$** | Tính: $\sqrt{50} - \sqrt{32} + \sqrt{18} =$ **$4\sqrt{2}$** | Tính: $\sqrt{75} - \sqrt{27} + \sqrt{12} =$ **$4\sqrt{3}$** |
| **7** | Nghiệm của hệ phương trình | Hệ $\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$ có $(x; y) =$ **$(3; 1)$** | Hệ $\begin{cases} 2x + y = 8 \\ x - y = 1 \end{cases}$ có $(x; y) =$ **$(3; 2)$** | Hệ $\begin{cases} 2x + y = 9 \\ x - y = 3 \end{cases}$ có $(x; y) =$ **$(4; 1)$** | Hệ $\begin{cases} 2x + y = 10 \\ x - y = 2 \end{cases}$ có $(x; y) =$ **$(4; 2)$** |
| **8** | Hệ thức lượng tam giác vuông | $\Delta$ vuông đường cao $AH$, hình chiếu $4\text{ cm}$ và $9\text{ cm} \implies AH =$ **$6\text{ cm}$** | $\Delta$ vuông đường cao $AH$, hình chiếu $2\text{ cm}$ và $8\text{ cm} \implies AH =$ **$4\text{ cm}$** | $\Delta$ vuông đường cao $AH$, hình chiếu $3\text{ cm}$ và $12\text{ cm} \implies AH =$ **$6\text{ cm}$** | $\Delta$ vuông đường cao $AH$, hình chiếu $1\text{ cm}$ và $9\text{ cm} \implies AH =$ **$3\text{ cm}$** |
| **9** | Khoảng cách từ tâm đến dây | $(O; 5\text{ cm})$, dây $CD = 8\text{ cm} \implies d(O, CD) =$ **$3\text{ cm}$** | $(O; 10\text{ cm})$, dây $CD = 16\text{ cm} \implies d(O, CD) =$ **$6\text{ cm}$** | $(O; 13\text{ cm})$, dây $CD = 24\text{ cm} \implies d(O, CD) =$ **$5\text{ cm}$** | $(O; 5\text{ cm})$, $d(O, CD) = 4\text{ cm} \implies CD =$ **$6\text{ cm}$** |
| **10** | Toán thực tế tỉ số lượng giác | Thang $4\text{ m}$, chân cách tường $2\text{ m}$. Góc thang tạo với đất: **$60^\circ$** | Thang $6\text{ m}$, chân cách tường $3\text{ m}$. Góc thang tạo với đất: **$60^\circ$** | Cột cờ cao $5\text{ m}$, bóng dài $5\text{ m}$. Góc tia nắng với đất: **$45^\circ$** | Cọc cao $3\text{ m}$, bóng dài $3\text{ m}$. Góc tia nắng với đất: **$45^\circ$** |

---

### 2. PHẦN TỰ LUẬN - TRANG 1 & TRANG 2

#### CÂU 11 (2,5 ĐIỂM): ĐẠI SỐ TỔNG HỢP

* **Mã đề 101:**
  - $a)$ (1,25 điểm): Giải hệ phương trình:
    $$\begin{cases} 2x + 3y = 7 \\ 3x - y = 5 \end{cases} \iff \begin{cases} 2x + 3y = 7 \\ 9x - 3y = 15 \end{cases} \iff \begin{cases} 11x = 22 \\ y = 3x - 5 \end{cases} \iff \begin{cases} x = 2 \\ y = 1 \end{cases}$$
    Nghiệm $(x; y) = (2; 1)$.
  - $b)$ (1,25 điểm): Cho biểu thức $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} - 1} - \dfrac{1}{x - \sqrt{x}} \right) : \dfrac{\sqrt{x} + 1}{x - 1}$ với $x > 0, x \ne 1$. Rút gọn biểu thức $P$.
    * Quy đồng trong ngoặc: $\dfrac{x - 1}{\sqrt{x}(\sqrt{x} - 1)} = \dfrac{\sqrt{x} + 1}{\sqrt{x}}$.
    * Rút gọn $P = \dfrac{\sqrt{x} + 1}{\sqrt{x}} : \dfrac{1}{\sqrt{x} - 1} = \dfrac{x - 1}{\sqrt{x}}$.

* **Mã đề 102:**
  - $a)$ (1,25 điểm): Giải hệ $\begin{cases} 3x - y = 7 \\ 2x + 3y = 12 \end{cases} \iff \begin{cases} 11x = 33 \\ y = 3x - 7 \end{cases} \iff \begin{cases} x = 3 \\ y = 2 \end{cases}$. Nghiệm $(3; 2)$.
  - $b)$ (1,25 điểm): Cho $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} - 2} - \dfrac{4}{x - 2\sqrt{x}} \right) : \dfrac{\sqrt{x} + 2}{x - 4}$ ($x > 0, x \ne 4$). Rút gọn $P = \dfrac{x - 4}{\sqrt{x}}$.

* **Mã đề 103:**
  - $a)$ (1,25 điểm): Giải hệ $\begin{cases} 2x + y = 8 \\ 3x - 2y = 5 \end{cases} \iff \begin{cases} 7x = 21 \\ y = 8 - 2x \end{cases} \iff \begin{cases} x = 3 \\ y = 2 \end{cases}$. Nghiệm $(3; 2)$.
  - $b)$ (1,25 điểm): Cho $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} - 3} - \dfrac{9}{x - 3\sqrt{x}} \right) : \dfrac{\sqrt{x} + 3}{x - 9}$ ($x > 0, x \ne 9$). Rút gọn $P = \dfrac{x - 9}{\sqrt{x}}$.

* **Mã đề 104:**
  - $a)$ (1,25 điểm): Giải hệ $\begin{cases} 2x + 3y = 8 \\ 3x - y = 1 \end{cases} \iff \begin{cases} 11x = 11 \\ y = 3x - 1 \end{cases} \iff \begin{cases} x = 1 \\ y = 2 \end{cases}$. Nghiệm $(1; 2)$.
  - $b)$ (1,25 điểm): Cho $P = \left( \dfrac{\sqrt{x}}{\sqrt{x} - 1} - \dfrac{1}{x - \sqrt{x}} \right) : \dfrac{\sqrt{x} + 1}{x - 1}$ ($x > 0, x \ne 1$). Rút gọn $P = \dfrac{x - 1}{\sqrt{x}}$.

---

#### CÂU 12 (2,5 ĐIỂM): TOÁN THỰC TẾ LẬP HỆ PHƯƠNG TRÌNH

* **Mã đề 101:** Một ca nô chạy trên khúc sông trong $7$ giờ, xuôi dòng $108\text{ km}$ và ngược dòng $63\text{ km}$. Một lần khác, ca nô đó cũng chạy trong $7$ giờ, xuôi dòng $81\text{ km}$ và ngược dòng $84\text{ km}$. Tính vận tốc của ca nô khi nước yên lặng và vận tốc của dòng nước (biết các vận tốc không đổi).
  - Gọi vận tốc xuôi dòng là $x$ (km/h) và ngược dòng là $y$ (km/h) ($x > y > 0$).
  - Thời gian lần thứ nhất: $\dfrac{108}{x} + \dfrac{63}{y} = 7$ ($0{,}5$đ).
  - Thời gian lần thứ hai: $\dfrac{81}{x} + \dfrac{84}{y} = 7$ ($0{,}5$đ).
  - Hệ phương trình: $\begin{cases} \dfrac{108}{x} + \dfrac{63}{y} = 7 \\ \dfrac{81}{x} + \dfrac{84}{y} = 7 \end{cases}$ ($0{,}25$đ).
  - Giải hệ bằng đặt ẩn phụ $u = \dfrac{1}{x}, v = \dfrac{1}{y} \implies \begin{cases} 108u + 63v = 7 \\ 81u + 84v = 7 \end{cases} \iff \begin{cases} u = \dfrac{1}{27} \\ v = \dfrac{1}{21} \end{cases} \iff \begin{cases} x = 27 \\ y = 21 \end{cases}$ (TMĐK) ($0{,}75$đ).
  - Vận tốc thực của ca nô: $v_{\text{thực}} = \dfrac{x + y}{2} = \dfrac{27 + 21}{2} = 24\text{ km/h}$.
  - Vận tốc dòng nước: $v_{\text{nước}} = \dfrac{x - y}{2} = \dfrac{27 - 21}{2} = 3\text{ km/h}$ ($0{,}5$đ).

* **Mã đề 102:** Một ca nô chạy trong $4$ giờ, xuôi dòng $90\text{ km}$ và ngược dòng $32\text{ km}$. Một lần khác ca nô cũng chạy trong $4$ giờ, xuôi dòng $60\text{ km}$ và ngược dòng $48\text{ km}$. Tính vận tốc thực của ca nô và vận tốc dòng nước.
  - $\begin{cases} \dfrac{90}{x} + \dfrac{32}{y} = 4 \\ \dfrac{60}{x} + \dfrac{48}{y} = 4 \end{cases} \iff \begin{cases} x = 30 \\ y = 16 \end{cases} \implies v_{\text{thực}} = 23\text{ km/h}, v_{\text{nước}} = 7\text{ km/h}$.

* **Mã đề 103:** Một ca nô chạy trong $5$ giờ, xuôi dòng $60\text{ km}$ và ngược dòng $48\text{ km}$. Một lần khác chạy trong $5$ giờ, xuôi dòng $40\text{ km}$ và ngược dòng $64\text{ km}$. Tính vận tốc thực của ca nô và vận tốc dòng nước.
  - $\begin{cases} \dfrac{60}{x} + \dfrac{48}{y} = 5 \\ \dfrac{40}{x} + \dfrac{64}{y} = 5 \end{cases} \iff \begin{cases} x = 20 \\ y = 16 \end{cases} \implies v_{\text{thực}} = 18\text{ km/h}, v_{\text{nước}} = 2\text{ km/h}$.

* **Mã đề 104:** Một ca nô chạy trong $6$ giờ, xuôi dòng $90\text{ km}$ và ngược dòng $60\text{ km}$. Một lần khác chạy trong $6$ giờ, xuôi dòng $120\text{ km}$ và ngược dòng $40\text{ km}$. Tính vận tốc thực của ca nô và vận tốc dòng nước.
  - $\begin{cases} \dfrac{90}{x} + \dfrac{60}{y} = 6 \\ \dfrac{120}{x} + \dfrac{40}{y} = 6 \end{cases} \iff \begin{cases} x = 30 \\ y = 20 \end{cases} \implies v_{\text{thực}} = 25\text{ km/h}, v_{\text{nước}} = 5\text{ km/h}$.

---

#### CÂU 13 (2,5 ĐIỂM): HÌNH HỌC TIẾP TUYẾN CỦA ĐƯỜNG TRÒN

Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Qua $A$ kẻ hai tiếp tuyến $AB, AC$ với đường tròn $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.
* **Mã đề 101:** Cho $R = 3\text{ cm}, OA = 5\text{ cm}$.
  - $a)$ (1,25 điểm): Chứng minh bốn điểm $A, B, O, C$ cùng thuộc một đường tròn.
    * Do $AB$ là tiếp tuyến tại $B \implies \widehat{ABO} = 90^\circ \implies A, B, O$ cùng thuộc đường tròn đường kính $OA$ ($0{,}5$đ).
    * Do $AC$ là tiếp tuyến tại $C \implies \widehat{ACO} = 90^\circ \implies A, C, O$ cùng thuộc đường tròn đường kính $OA$ ($0{,}5$đ).
    * Suy ra bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $OA$ ($0{,}25$đ).
  - $b)$ (1,25 điểm): Kẻ đường kính $CD$ của $(O)$. Chứng minh $BD \parallel OA$ và tính độ dài đoạn thẳng $BC$.
    * $AB = AC, OB = OC \implies OA$ là trung trực của $BC \implies OA \perp BC$ tại $H$ ($0{,}25$đ).
    * $B \in (O)$ đường kính $CD \implies \widehat{CBD} = 90^\circ \implies BD \perp BC$ ($0{,}25$đ).
    * Suy ra $BD \parallel OA$ (cùng $\perp BC$) ($0{,}25$đ).
    * Trong $\Delta OBA$ vuông tại $B$: $AB = \sqrt{OA^2 - OB^2} = \sqrt{5^2 - 3^2} = 4\text{ cm}$ ($0{,}25$đ).
    * Đường cao $BH$: $BH = \dfrac{OB \cdot AB}{OA} = \dfrac{3 \cdot 4}{5} = 2{,}4\text{ cm} \implies BC = 2BH = 4{,}8\text{ cm}$ ($0{,}25$đ).

* **Mã đề 102:** Cho $R = 6\text{ cm}, OA = 10\text{ cm}$.
  - $a)$ Chứng minh bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $OA$ ($1{,}25$đ).
  - $b)$ $BD \parallel OA$. $AB = 8\text{ cm}; BH = 4{,}8\text{ cm} \implies BC = 9{,}6\text{ cm}$ ($1{,}25$đ).

* **Mã đề 103:** Cho $R = 9\text{ cm}, OA = 15\text{ cm}$.
  - $a)$ Chứng minh bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $OA$ ($1{,}25$đ).
  - $b)$ $BD \parallel OA$. $AB = 12\text{ cm}; BH = 7{,}2\text{ cm} \implies BC = 14{,}4\text{ cm}$ ($1{,}25$đ).

* **Mã đề 104:** Cho $R = 12\text{ cm}, OA = 20\text{ cm}$.
  - $a)$ Chứng minh bốn điểm $A, B, O, C$ cùng thuộc đường tròn đường kính $OA$ ($1{,}25$đ).
  - $b)$ $BD \parallel OA$. $AB = 16\text{ cm}; BH = 9{,}6\text{ cm} \implies BC = 19{,}2\text{ cm}$ ($1{,}25$đ).

