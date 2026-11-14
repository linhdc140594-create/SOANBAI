# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 11 - BUỔI 02 (TOÁN 8)
## CHỦ ĐỀ: BÀI 17: TÍNH CHẤT ĐƯỜNG PHÂN GIÁC CỦA TAM GIÁC & MỞ ĐẦU PHÂN THỨC ĐẠI SỐ
### Bám sát chương trình: SGK Toán 8 - Kết nối tri thức với cuộc sống (Chương IV) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững định lí tính chất đường phân giác của tam giác: Đường phân giác của một góc chia cạnh đối diện thành hai đoạn thẳng tỉ lệ với hai cạnh kề hai đoạn thẳng đó ($\dfrac{DB}{DC} = \dfrac{AB}{AC}$).
   - Vận dụng tính độ dài đoạn thẳng, chứng minh tỉ lệ thức, phối hợp định lí Pythagore trong tam giác vuông.
   - Nắm vững khái niệm phân thức đại số $\dfrac{A}{B}$ ($B \neq 0$), tìm điều kiện xác định.
   - Nắm vững tính chất cơ bản của phân thức đại số, quy tắc đổi dấu.
   - Thành thạo kỹ năng rút gọn phân thức đại số bằng cách phân tích tử và mẫu thành nhân tử.
   - Kỹ năng tìm $x$: Giải phương trình tích, phương trình đưa về dạng nhân tử.
   - Vận dụng cao: Tìm giá trị lớn nhất (GTLN) của phân thức có mẫu là tam thức bậc hai dương: $B = \dfrac{k}{x^2 - 2ax + b}$ ($k > 0$).

2. **Kỹ năng & Năng lực:**
   - Vẽ hình tam giác vuông và đường phân giác chính xác bằng TikZ.
   - Trình bày bài giải hình học 2 cột khoa học (`\dongkeHaiCot{10}` hoặc `\dongkeHaiCot{11}`).
   - Kỹ năng rút gọn phân thức cẩn thận, không làm tắt bước.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

| STT | Dạng bài | Số câu / Ý | Điểm số | Vị trí trên phiếu | Quy chuẩn định dạng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Trả lời ngắn (Short Answer) | 10 câu | 2,5 đ | Trang 1 (Đầu trang) | Lệnh `\shortans`, ô bo góc `KQ: [   ]` sát mép phải. |
| **2** | Rút gọn phân thức đại số | 6 ý ($a \to f$) | 3,0 đ | Trang 1 (Cuối trang) | Bảng $3 \times 2$, dùng `\oBaiTap[5]` lấp kín 100% lề dưới. |
| **3** | Tìm $x$ | 4 ý ($a \to d$) | 2,0 đ | Trang 2 (Đầu trang) | Bảng $2 \times 2$, dùng `\oBaiTap[5]`. |
| **4** | Hình học Đường phân giác | 2 ý ($a, b$) | 2,0 đ | Trang 2 (Giữa trang) | Ghép box `tabularx` có hình TikZ, bài giải `\dongkeHaiCot{10}`. |
| **5** | Vận dụng cao điểm 10 | 1 bài | 0,5 đ | Trang 2 (Cuối trang) | Ghép box `tabularx`, bài giải `\dongkeHaiCot{6}` sát lề dưới. |
| **TỔNG** | | **23 mục** | **10,0 đ** | **2 mặt A4** | **Chính xác 8 trang PDF cho 4 mã đề (101-104)** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Tỉ số đường phân giác | $\Delta ABC$, $AD$ là phân giác $\implies \dfrac{DB}{DC} =$ **$\dfrac{AB}{AC}$** | $\Delta MNP$, $MK$ là phân giác $\implies \dfrac{KN}{KP} =$ **$\dfrac{MN}{MP}$** | $\Delta DEF$, $DH$ là phân giác $\implies \dfrac{HE}{HF} =$ **$\dfrac{DE}{DF}$** | $\Delta ABC$, $BE$ là phân giác $\implies \dfrac{EA}{EC} =$ **$\dfrac{BA}{BC}$** |
| **2** | Tính đoạn thẳng từ phân giác | $AB=4, AC=6, DB=2 \implies DC =$ **$3\text{ cm}$** | $AB=6, AC=9, DB=4 \implies DC =$ **$6\text{ cm}$** | $MN=5, MP=10, KN=3 \implies KP =$ **$6\text{ cm}$** | $DE=4, DF=8, HE=3 \implies HF =$ **$6\text{ cm}$** |
| **3** | Tính cạnh từ tỉ số phân giác | $\dfrac{DB}{DC} = \dfrac{2}{3}, AB=6 \implies AC =$ **$9\text{ cm}$** | $\dfrac{DB}{DC} = \dfrac{3}{4}, AB=9 \implies AC =$ **$12\text{ cm}$** | $\dfrac{KN}{KP} = \dfrac{2}{5}, MN=4 \implies MP =$ **$10\text{ cm}$** | $\dfrac{HE}{HF} = \dfrac{3}{5}, DE=6 \implies DF =$ **$10\text{ cm}$** |
| **4** | Điều kiện xác định phân thức | $\dfrac{2x+1}{x-3}$ xác định khi **$x \neq 3$** | $\dfrac{3x-2}{x-4}$ xác định khi **$x \neq 4$** | $\dfrac{x+5}{x+2}$ xác định khi **$x \neq -2$** | $\dfrac{4x-1}{x+5}$ xác định khi **$x \neq -5$** |
| **5** | Phân thức bằng 0 | $\dfrac{x-5}{x+2} = 0 \implies x =$ **$5$** | $\dfrac{x-7}{x+3} = 0 \implies x =$ **$7$** | $\dfrac{x+4}{x-1} = 0 \implies x =$ **$-4$** | $\dfrac{x-6}{x+1} = 0 \implies x =$ **$6$** |
| **6** | Rút gọn phân thức đơn giản | $\dfrac{x^2-9}{x-3} =$ **$x + 3$** | $\dfrac{x^2-16}{x-4} =$ **$x + 4$** | $\dfrac{x^2-25}{x-5} =$ **$x + 5$** | $\dfrac{x^2-36}{x-6} =$ **$x + 6$** |
| **7** | Phân thức đối | Phân thức đối của $\dfrac{x-1}{x+2}$ là **$\dfrac{1-x}{x+2}$** | Phân thức đối của $\dfrac{x-3}{x+1}$ là **$\dfrac{3-x}{x+1}$** | Phân thức đối của $\dfrac{x-2}{x+5}$ là **$\dfrac{2-x}{x+5}$** | Phân thức đối của $\dfrac{x-4}{x+3}$ là **$\dfrac{4-x}{x+3}$** |
| **8** | Giá trị phân thức tại điểm | $\dfrac{x^2-1}{x-1}$ tại $x=9$ bằng **$10$** | $\dfrac{x^2-4}{x-2}$ tại $x=8$ bằng **$10$** | $\dfrac{x^2-9}{x-3}$ tại $x=7$ bằng **$10$** | $\dfrac{x^2-16}{x-4}$ tại $x=6$ bằng **$10$** |
| **9** | Thực tế chia đất phân giác | $AB=30, AC=45, BC=50 \implies DB =$ **$20\text{ m}$** | $AB=20, AC=30, BC=40 \implies DB =$ **$16\text{ m}$** | $AB=25, AC=50, BC=60 \implies DB =$ **$20\text{ m}$** | $AB=35, AC=70, BC=90 \implies DB =$ **$30\text{ m}$** |
| **10** | Tam giác vuông: góc phụ nhau | Góc nhọn $38^\circ \implies$ góc kia bằng **$52^\circ$** | Góc nhọn $42^\circ \implies$ góc kia bằng **$48^\circ$** | Góc nhọn $28^\circ \implies$ góc kia bằng **$62^\circ$** | Góc nhọn $34^\circ \implies$ góc kia bằng **$56^\circ$** |

---

### 2. CÂU 11 (3,0 ĐIỂM - RÚT GỌN PHÂN THỨC ĐẠI SỐ - 6 Ý $A \to F$)

* **Mã đề 101:**
  - $a)$ $\dfrac{6x^3 y^2}{9x^2 y^3} = \dfrac{2x}{3y}$
  - $b)$ $\dfrac{3x - 6}{x^2 - 4} = \dfrac{3}{x + 2}$
  - $c)$ $\dfrac{x^2 - 6x + 9}{x^2 - 9} = \dfrac{x - 3}{x + 3}$
  - $d)$ $\dfrac{3 - x}{x^2 - 9} = -\dfrac{1}{x + 3}$
  - $e)$ $\dfrac{x^2 - 5x + 6}{x^2 - 4} = \dfrac{x - 3}{x + 2}$
  - $f)$ Cho $P = \dfrac{x^2 + 2x}{x^2 - 4}$. Rút gọn $P$ và tính giá trị tại $x = 3$. ($P = \dfrac{x}{x - 2} = 3$)

* **Mã đề 102:**
  - $a)$ $\dfrac{8x^4 y^2}{12x^3 y^3} = \dfrac{2x}{3y}$
  - $b)$ $\dfrac{4x - 12}{x^2 - 9} = \dfrac{4}{x + 3}$
  - $c)$ $\dfrac{x^2 + 8x + 16}{x^2 - 16} = \dfrac{x + 4}{x - 4}$
  - $d)$ $\dfrac{4 - x}{x^2 - 16} = -\dfrac{1}{x + 4}$
  - $e)$ $\dfrac{x^2 - 7x + 12}{x^2 - 9} = \dfrac{x - 4}{x + 3}$
  - $f)$ Cho $P = \dfrac{x^2 + 3x}{x^2 - 9}$. Rút gọn $P$ và tính giá trị tại $x = 4$. ($P = \dfrac{x}{x - 3} = 4$)

* **Mã đề 103:**
  - $a)$ $\dfrac{10x^3 y^3}{15x^2 y^4} = \dfrac{2x}{3y}$
  - $b)$ $\dfrac{5x - 20}{x^2 - 16} = \dfrac{5}{x + 4}$
  - $c)$ $\dfrac{x^2 - 10x + 25}{x^2 - 25} = \dfrac{x - 5}{x + 5}$
  - $d)$ $\dfrac{5 - x}{x^2 - 25} = -\dfrac{1}{x + 5}$
  - $e)$ $\dfrac{x^2 - 6x + 8}{x^2 - 4} = \dfrac{x - 4}{x + 2}$
  - $f)$ Cho $P = \dfrac{x^2 + 4x}{x^2 - 16}$. Rút gọn $P$ và tính giá trị tại $x = 5$. ($P = \dfrac{x}{x - 4} = 5$)

* **Mã đề 104:**
  - $a)$ $\dfrac{14x^4 y^3}{21x^3 y^4} = \dfrac{2x}{3y}$
  - $b)$ $\dfrac{2x - 10}{x^2 - 25} = \dfrac{2}{x + 5}$
  - $c)$ $\dfrac{x^2 + 4x + 4}{x^2 - 4} = \dfrac{x + 2}{x - 2}$
  - $d)$ $\dfrac{2 - x}{x^2 - 4} = -\dfrac{1}{x + 2}$
  - $e)$ $\dfrac{x^2 - 8x + 15}{x^2 - 9} = \dfrac{x - 5}{x + 3}$
  - $f)$ Cho $P = \dfrac{x^2 + 2x}{x^2 - 4}$. Rút gọn $P$ và tính giá trị tại $x = 4$. ($P = \dfrac{x}{x - 2} = 2$)

---

### 3. CÂU 12 (2,0 ĐIỂM - TÌM $x$ - 4 Ý $A \to D$)

| Ý | Dạng phương trình | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **a** | Phương trình tích $(ax+b)(cx+d)=0$ | $(x-3)(2x+1)=0 \to x \in \{3; -1/2\}$ | $(x-4)(2x+1)=0 \to x \in \{4; -1/2\}$ | $(x-2)(3x+1)=0 \to x \in \{2; -1/3\}$ | $(x-5)(2x+1)=0 \to x \in \{5; -1/2\}$ |
| **b** | $(ax+b)^2 - c^2 = 0$ | $(2x-1)^2 - 9 = 0 \to x \in \{2; -1\}$ | $(2x-1)^2 - 25 = 0 \to x \in \{3; -2\}$ | $(3x-1)^2 - 16 = 0 \to x \in \{5/3; -1\}$ | $(2x+1)^2 - 9 = 0 \to x \in \{1; -2\}$ |
| **c** | Tách hạng tử tam thức bậc hai | $x^2 - 7x + 12 = 0 \to x \in \{3; 4\}$ | $x^2 - 5x + 6 = 0 \to x \in \{2; 3\}$ | $x^2 - 6x + 8 = 0 \to x \in \{2; 4\}$ | $x^2 - 8x + 15 = 0 \to x \in \{3; 5\}$ |
| **d** | Nhóm nhân tử chung | $x(x-2)+3(x-2)=0 \to x \in \{2; -3\}$ | $x(x-3)+4(x-3)=0 \to x \in \{3; -4\}$ | $x(x-4)+2(x-4)=0 \to x \in \{4; -2\}$ | $x(x-5)+3(x-5)=0 \to x \in \{5; -3\}$ |

---

### 4. CÂU 13 (2,0 ĐIỂM - HÌNH HỌC TÍNH CHẤT ĐƯỜNG PHÂN GIÁC & TAM GIÁC VUÔNG)

* **Mã đề 101:** Cho tam giác $ABC$ vuông tại $A$, có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Kẻ tia phân giác $AD$ của góc $\widehat{A}$ ($D \in BC$).
  - $a)$ (1,0 điểm): Tính độ dài cạnh huyền $BC$. Tính tỉ số $\dfrac{DB}{DC}$ và tính độ dài các đoạn thẳng $DB, DC$.
  - $b)$ (1,0 điểm): Từ $D$ kẻ $DH \perp AB$ tại $H$. Chứng minh tam giác $AHD$ vuông cân tại $H$ và tính độ dài đoạn thẳng $DH$.
* **Mã đề 102:** Cho tam giác $MNP$ vuông tại $M$, có $MN = 6\text{ cm}, MP = 8\text{ cm}$. Kẻ tia phân giác $MK$ của góc $\widehat{M}$ ($K \in NP$).
  - $a)$ (1,0 điểm): Tính độ dài cạnh huyền $NP$. Tính tỉ số $\dfrac{KN}{KP}$ và tính độ dài các đoạn thẳng $KN, KP$.
  - $b)$ (1,0 điểm): Từ $K$ kẻ $KH \perp MN$ tại $H$. Chứng minh tam giác $MHK$ vuông cân tại $H$ và tính độ dài đoạn thẳng $KH$.
* **Mã đề 103:** Cho tam giác $ABC$ vuông tại $A$, có $AB = 9\text{ cm}, AC = 12\text{ cm}$. Kẻ tia phân giác $AD$ của góc $\widehat{A}$ ($D \in BC$).
  - $a)$ (1,0 điểm): Tính độ dài cạnh huyền $BC$. Tính tỉ số $\dfrac{DB}{DC}$ và tính độ dài các đoạn thẳng $DB, DC$.
  - $b)$ (1,0 điểm): Từ $D$ kẻ $DH \perp AB$ tại $H$. Chứng minh tam giác $AHD$ vuông cân tại $H$ và tính độ dài đoạn thẳng $DH$.
* **Mã đề 104:** Cho tam giác $DEF$ vuông tại $D$, có $DE = 6\text{ cm}, DF = 8\text{ cm}$. Kẻ tia phân giác $DI$ của góc $\widehat{D}$ ($I \in EF$).
  - $a)$ (1,0 điểm): Tính độ dài cạnh huyền $EF$. Tính tỉ số $\dfrac{IE}{IF}$ và tính độ dài các đoạn thẳng $IE, IF$.
  - $b)$ (1,0 điểm): Từ $I$ kẻ $IK \perp DE$ tại $K$. Chứng minh tam giác $DKI$ vuông cân tại $K$ và tính độ dài đoạn thẳng $IK$.

---

### 5. CÂU 14 (0,5 ĐIỂM - VẬN DỤNG CAO ĐIỂM 10)

* **Mã đề 101:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{6}{x^2 - 4x + 7}$.
  - *Lời giải:* $B = \dfrac{6}{(x - 2)^2 + 3}$. Vì $(x - 2)^2 \ge 0 \implies (x - 2)^2 + 3 \ge 3 \implies B \le \dfrac{6}{3} = 2$. Dấu "$=$" xảy ra khi $x = 2$. Vậy $\max B = 2$ khi $x = 2$.
* **Mã đề 102:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{8}{x^2 - 6x + 13}$.
  - *Lời giải:* $B = \dfrac{8}{(x - 3)^2 + 4} \le \dfrac{8}{4} = 2$. Dấu "$=$" khi $x = 3$. Vậy $\max B = 2$ khi $x = 3$.
* **Mã đề 103:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{10}{x^2 - 2x + 6}$.
  - *Lời giải:* $B = \dfrac{10}{(x - 1)^2 + 5} \le \dfrac{10}{5} = 2$. Dấu "$=$" khi $x = 1$. Vậy $\max B = 2$ khi $x = 1$.
* **Mã đề 104:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{12}{x^2 - 8x + 20}$.
  - *Lời giải:* $B = \dfrac{12}{(x - 4)^2 + 4} \le \dfrac{12}{4} = 3$. Dấu "$=$" khi $x = 4$. Vậy $\max B = 3$ khi $x = 4$.

