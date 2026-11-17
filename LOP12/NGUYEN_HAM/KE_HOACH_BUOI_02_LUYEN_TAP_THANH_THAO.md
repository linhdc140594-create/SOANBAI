# KẾ HOẠCH BÀI DẠY: NGUYÊN HÀM (BUỔI 2)
## CHUYÊN ĐỀ: RÈN PHẢN XẠ & THÀNH THẠO KỸ NĂNG BIẾN ĐỔI TIỀN XỬ LÝ
*(Chương trình Toán 12 -- GDPT 2018 | Lớp Toán Thầy Lĩnh | Bộ 8 Trang A4 Có Dòng Kẻ)*

---

## 🎯 I. MỤC TIÊU SƯ PHẠM BUỔI 2

1. **Khắc sâu và tạo phản xạ vô điều kiện:**
   - Chưa vội sang phương pháp Đổi biến số hay Từng phần. Học sinh cần thành thạo toàn diện các kỹ năng đại số, phân thức, lượng giác và mũ.
   - Trị dứt điểm lỗi kinh điển: quên hệ số $\dfrac{1}{a}$ khi gặp biểu thức bậc nhất $ax + b$.
   - Tránh nhầm dấu đạo hàm và nguyên hàm ($\int \sin = -\cos$, $\int \cos = \sin$).

2. **Làm chủ 4 kỹ thuật biến đổi tiền xử lý (Pre-processing):**
   - **Kỹ thuật 1:** Đưa căn thức và nghịch đảo về số mũ phân số/mũ âm: $\sqrt[n]{x^m} = x^{\frac{m}{n}}, \frac{1}{x^k} = x^{-k}$.
   - **Kỹ thuật 2:** Chia đa thức khi bậc tử $\ge$ bậc mẫu: $\frac{P(x)}{ax+b} = Q(x) + \frac{r}{ax+b}$.
   - **Kỹ thuật 3:** Tách phân thức mẫu có 2 nghiệm bậc nhất: $\frac{1}{(x-a)(x-b)} = \frac{1}{b-a}\left(\frac{1}{x-b} - \frac{1}{x-a}\right)$.
   - **Kỹ thuật 4:** Biến đổi lượng giác không cần đổi biến (Hạ bậc $\sin^2, \cos^2$; Tích thành tổng; $\tan^2 x = \frac{1}{\cos^2 x} - 1$).

3. **Hình thức tài liệu:**
   - Tập phiếu gồm **chính xác 8 trang A4** (4 tờ in 2 mặt).
   - Mỗi đầu trang có khung **"CẢNH BÁO LỖI SAI & PHƯƠNG PHÁP VÀNG"**.
   - Bài tập được phân bố đều vào các ô `\oBaiTap` với dòng kẻ chấm mờ cự ly 18.5pt chuẩn viết tay học sinh THPT.

---

## 📑 II. MA TRẬN 8 TRANG A4 CHI TIẾT

```
[Trang 1: Phản xạ Bậc nhất ax + b] ─────────► [Trang 2: Căn thức & Lũy thừa âm]
                 │                                            │
[Trang 3: Phân thức: Chia đa thức] ─────────► [Trang 4: Phân thức: Tách mẫu số]
                 │                                            │
[Trang 5: Lượng giác: Hạ bậc & ĐHT] ────────► [Trang 6: Lượng giác Tích thành Tổng & Mũ]
                 │                                            │
[Trang 7: Tìm hằng số C & Điểm thuộc] ──────► [Trang 8: Toán thực tế liên môn Vật lý - Sinh - KT]
```

---

### 📄 TRANG 1: RÈN PHẢN XẠ CÔNG THỨC MỞ RỘNG BẬC NHẤT $ax + b$
* **Khung ghi nhớ:** 
  $$\int f(ax+b)\,dx = \frac{1}{a}F(ax+b) + C \quad (a \ne 0)$$
  *Khẩu quyết: "Ruột là bậc nhất $ax+b \implies$ BẮT BUỘC nhân thêm $\dfrac{1}{a}$ ở phía trước!"*
* **Bài 1 (3,0 điểm) -- Đa thức và lũy thừa bậc nhất (6 câu, mỗi câu 3 dòng kẻ):**
  a) $\int (2x - 5)^4 \, dx$
  b) $\int (3 - 4x)^5 \, dx$
  c) $\int (5x + 2)^3 \, dx$
  d) $\int (1 - 2x)^6 \, dx$
  e) $\int 3(2x + 1)^4 \, dx$
  f) $\int (4 - x)^7 \, dx$
* **Bài 2 (4,0 điểm) -- Phân thức mẫu bậc nhất $\dfrac{1}{ax+b}$ và $\dfrac{1}{(ax+b)^2}$ (6 câu, mỗi câu 4 dòng kẻ):**
  a) $\int \frac{1}{2x + 3} \, dx$
  b) $\int \frac{1}{3x - 5} \, dx$
  c) $\int \frac{1}{4 - 5x} \, dx$
  d) $\int \frac{6}{2x - 1} \, dx$
  e) $\int \frac{1}{(2x + 1)^2} \, dx$
  f) $\int \frac{1}{(3x - 2)^2} \, dx$

---

### 📄 TRANG 2: KỸ THUẬT XỬ LÝ CĂN THỨC VÀ SỐ MŨ PHÂN SỐ / MŨ ÂM
* **Khung ghi nhớ:**
  - Chuyển căn về lũy thừa: $\sqrt[n]{(ax+b)^m} = (ax+b)^{\frac{m}{n}}$.
  - Hai công thức quen thuộc:
    $$\int \sqrt{ax+b} \, dx = \frac{1}{a} \cdot \frac{2}{3}(ax+b)\sqrt{ax+b} + C$$
    $$\int \frac{1}{\sqrt{ax+b}} \, dx = \frac{1}{a} \cdot 2\sqrt{ax+b} + C$$
* **Bài 3 (4,0 điểm) -- Căn bậc hai và căn bậc ba bậc nhất (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \sqrt{2x + 1} \, dx$
  b) $\int \sqrt{3x - 2} \, dx$
  c) $\int \frac{4}{\sqrt{2x + 5}} \, dx$
  d) $\int \sqrt[3]{3x + 1} \, dx$
* **Bài 4 (4,0 điểm) -- Biến đổi rút gọn căn thức và đa thức (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{x^2 - 3x\sqrt{x} + 2}{\sqrt{x}} \, dx$
  b) $\int \sqrt{x}(2x^2 - 4x + 3) \, dx$
  c) $\int \left(\frac{2}{x^3} - \frac{3}{x^2} + \sqrt{x}\right) dx$
  d) $\int \frac{(x + \sqrt{x})^2}{x} \, dx$

---

### 📄 TRANG 3: KỸ NĂNG BIẾN ĐỔI PHÂN THỨC HỮU TỈ (DẠNG 1: CHIA ĐA THỨC)
* **Khung phương pháp:**
  - Bậc của tử $\ge$ bậc của mẫu $\implies$ **Bắt buộc chia đa thức**:
    $$\frac{P(x)}{ax+b} = Q(x) + \frac{r}{ax+b}$$
* **Bài 5 (4,0 điểm) -- Tử bậc 1, mẫu bậc 1 (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{2x + 5}{x + 1} \, dx = \int \left(2 + \frac{3}{x+1}\right) dx$
  b) $\int \frac{3x - 2}{x - 2} \, dx = \int \left(3 + \frac{4}{x-2}\right) dx$
  c) $\int \frac{4x + 1}{2x - 1} \, dx = \int \left(2 + \frac{3}{2x-1}\right) dx$
  d) $\int \frac{6x - 5}{3x + 2} \, dx = \int \left(2 - \frac{9}{3x+2}\right) dx$
* **Bài 6 (4,0 điểm) -- Tử bậc 2, mẫu bậc 1 (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{x^2 + 3x - 2}{x + 1} \, dx = \int \left(x + 2 - \frac{4}{x+1}\right) dx$
  b) $\int \frac{x^2 - 4x + 5}{x - 2} \, dx = \int \left(x - 2 + \frac{1}{x-2}\right) dx$
  c) $\int \frac{2x^2 + 3x - 1}{2x + 1} \, dx = \int \left(x + 1 - \frac{2}{2x+1}\right) dx$
  d) $\int \frac{x^2 + 1}{x - 1} \, dx = \int \left(x + 1 + \frac{2}{x-1}\right) dx$

---

### 📄 TRANG 4: KỸ NĂNG BIẾN ĐỔI PHÂN THỨC HỮU TỈ (DẠNG 2: TÁCH MẪU SỐ NHÂN TỬ)
* **Khung phương pháp:**
  - Mẫu phân tích thành tích $(x-a)(x-b)$ với $a \ne b$:
    $$\frac{1}{(x-a)(x-b)} = \frac{1}{b-a}\left(\frac{1}{x-b} - \frac{1}{x-a}\right)$$
  - Tử có chứa $x$: Dùng kỹ thuật tách theo đạo hàm mẫu hoặc đồng nhất hệ số $\frac{mx+n}{(x-a)(x-b)} = \frac{A}{x-a} + \frac{B}{x-b}$.
* **Bài 7 (4,0 điểm) -- Mẫu số có dạng $x^2 - a^2$ hoặc $(x+a)(x+b)$ với tử là hằng số (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{1}{(x+1)(x+2)} \, dx$
  b) $\int \frac{1}{x^2 - 1} \, dx = \int \frac{1}{(x-1)(x+1)} \, dx$
  c) $\int \frac{1}{x^2 - 4} \, dx = \int \frac{1}{(x-2)(x+2)} \, dx$
  d) $\int \frac{1}{x^2 - 5x + 6} \, dx = \int \frac{1}{(x-2)(x-3)} \, dx$
* **Bài 8 (4,0 điểm) -- Tử bậc 1, mẫu phân tích thành nhân tử (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{2x + 3}{(x+1)(x+2)} \, dx = \int \left(\frac{1}{x+1} + \frac{1}{x+2}\right) dx$
  b) $\int \frac{3x - 1}{x^2 - 1} \, dx = \int \left(\frac{1}{x-1} + \frac{2}{x+1}\right) dx$
  c) $\int \frac{5x - 7}{x^2 - 3x + 2} \, dx = \int \left(\frac{2}{x-1} + \frac{3}{x-2}\right) dx$
  d) $\int \frac{x}{x^2 - 4} \, dx = \int \left(\frac{1/2}{x-2} + \frac{1/2}{x+2}\right) dx$

---

### 📄 TRANG 5: KỸ NĂNG BIẾN ĐỔI LƯỢNG GIÁC (DẠNG 1: HẠ BẬC & ĐỒNG NHẤT THỨC)
* **Khung phương pháp:**
  - Công thức hạ bậc:
    $$\sin^2(ax) = \frac{1 - \cos(2ax)}{2}, \qquad \cos^2(ax) = \frac{1 + \cos(2ax)}{2}$$
  - Công thức đồng nhất thức:
    $$\tan^2 x = \frac{1}{\cos^2 x} - 1 \implies \int \tan^2 x \, dx = \tan x - x + C$$
    $$\cot^2 x = \frac{1}{\sin^2 x} - 1 \implies \int \cot^2 x \, dx = -\cot x - x + C$$
* **Bài 9 (4,0 điểm) -- Lượng giác dùng công thức hạ bậc (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int 4\sin^2 x \, dx$
  b) $\int 6\cos^2(2x) \, dx$
  c) $\int (2\sin^2 x + 4\cos^2 x) \, dx$
  d) $\int \left(\sin^4 x - \cos^4 x\right) dx = \int (-\cos 2x) \, dx$
* **Bài 10 (4,0 điểm) -- Lượng giác chứa $\tan^2, \cot^2$ và bậc nhất (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int (1 + \tan^2 x + 3\cos x) \, dx$
  b) $\int \tan^2(2x) \, dx$
  c) $\int \cot^2(3x) \, dx$
  d) $\int \left(\frac{1}{\sin^2(2x)} + \frac{1}{\cos^2(3x)}\right) dx$

---

### 📄 TRANG 6: LƯỢNG GIÁC TÍCH THÀNH TỔNG & HÀM SỐ MŨ BIẾN ĐỔI LŨY THỪA
* **Khung phương pháp:**
  - Tích thành tổng:
    $$\cos a \cos b = \frac{1}{2}[\cos(a-b) + \cos(a+b)]$$
    $$\sin a \sin b = \frac{1}{2}[\cos(a-b) - \cos(a+b)]$$
    $$\sin a \cos b = \frac{1}{2}[\sin(a+b) + \sin(a-b)]$$
  - Biến đổi hàm số mũ:
    $$a^x \cdot b^x = (ab)^x, \qquad \frac{a^x}{b^x} = \left(\frac{a}{b}\right)^x, \qquad \int a^{kx+b} dx = \frac{1}{k}\frac{a^{kx+b}}{\ln a} + C$$
* **Bài 11 (4,0 điểm) -- Tích thành tổng lượng giác (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int 2\sin(3x)\cos(x) \, dx$
  b) $\int 2\cos(4x)\cos(2x) \, dx$
  c) $\int 2\sin(5x)\sin(x) \, dx$
  d) $\int \cos(3x)\sin(2x) \, dx$
* **Bài 12 (4,0 điểm) -- Hàm số mũ biến đổi lũy thừa (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int (2^x \cdot 3^x) \, dx = \int 6^x \, dx$
  b) $\int \frac{8^x - 4^x}{2^x} \, dx$
  c) $\int (e^{3x-1} + 3 \cdot 2^{2x+1}) \, dx$
  d) $\int (e^x + 1)^2 \, dx = \int (e^{2x} + 2e^x + 1) \, dx$

---

### 📄 TRANG 7: TÌM NGUYÊN HÀM $F(x)$ VỚI ĐIỀU KIỆN $F(x_0) = y_0$ (LUYỆN TẬP CHUYÊN SÂU)
* **Khung phương pháp:**
  - Tính họ nguyên hàm $F(x) = \int f(x) \, dx + C$.
  - Thay $x = x_0$ vào hệ thức $F(x_0) = y_0 \implies$ giải phương trình tìm hằng số $C$.
  - Khi biểu thức chứa $\ln|u(x)|$, xét dấu $u(x_0)$ trên khoảng đã cho để phá dấu trị tuyệt đối.
* **Bài 13 (4,0 điểm) -- Tìm $F(x)$ của hàm đa thức và phân thức hữu tỉ (4 câu, mỗi câu 7 dòng kẻ):**
  a) Tìm $F(x)$ của $f(x) = 3x^2 - 4x + 5$, biết $F(1) = 6$.
  b) Tìm $F(x)$ của $f(x) = \frac{1}{2x - 3}$ trên $(\frac{3}{2}; +\infty)$, biết $F(2) = 3$.
  c) Tìm $F(x)$ của $f(x) = \frac{2x + 1}{x + 1}$ trên $(-1; +\infty)$, biết $F(0) = 4$.
  d) Tìm $F(x)$ của $f(x) = \frac{1}{x^2 - 1}$ trên $(1; +\infty)$, biết $F(2) = \ln 3$.
* **Bài 14 (4,0 điểm) -- Tìm $F(x)$ của hàm lượng giác và hàm số mũ (4 câu, mỗi câu 7 dòng kẻ):**
  a) Tìm $F(x)$ của $f(x) = 2\sin(2x) + 3\cos x$, biết $F(0) = 2$.
  b) Tìm $F(x)$ của $f(x) = 4\cos^2 x$, biết $F(\frac{\pi}{4}) = \frac{\pi}{2}$.
  c) Tìm $F(x)$ của $f(x) = 3e^{3x} - 2x$, biết $F(0) = 5$.
  d) Tìm $F(x)$ của $f(x) = 2^x \ln 2 + e^{2x}$, biết $F(0) = \frac{5}{2}$.

---

### 📄 TRANG 8: BÀI TOÁN THỰC TẾ LIÊN MÔN (VẬT LÝ -- KINH TẾ -- SINH HỌC)
* **Khung phương pháp:**
  - **Vật lý:** Vận tốc $v(t) = \int a(t) \, dt + C_1$; Quãng đường $s(t) = \int v(t) \, dt + C_2$.
  - **Sinh học:** Số lượng cá thể $N(t) = \int N'(t) \, dt + C$.
  - **Kinh tế:** Tổng chi phí $C(x) = \int C'(x) \, dx + C_0$ ($C_0$ là chi phí cố định).
* **Bài 15 (4,0 điểm) -- Hai bài toán chuyển động học (Vật lý 12, mỗi bài 6 dòng kẻ):**
  a) **(Ô tô hãm phanh):** Một ô tô đang chuyển động với vận tốc đều $v_0 = 20\text{ m/s}$ (khoảng $72\text{ km/h}$) thì người lái phát hiện chướng ngại vật và hãm phanh khẩn cấp với gia tốc $a(t) = -4\text{ m/s}^2$.
     - Thiết lập phương trình vận tốc $v(t)$ và tính thời gian từ khi phanh đến khi xe dừng hẳn.
     - Tính quãng đường ô tô trượt được từ lúc đạp phanh đến khi dừng hẳn.
  b) **(Tàu hỏa tăng tốc):** Một đoàn tàu bắt đầu rời ga chuyển động thẳng nhanh dần với gia tốc $a(t) = 0{,}6t\text{ (m/s}^2\text{)}$.
     - Tìm phương trình vận tốc $v(t)$ biết tại $t = 0$, $v(0) = 0$.
     - Tính quãng đường đoàn tàu đi được trong 10 giây đầu tiên.
* **Bài 16 (4,0 điểm) -- Hai bài toán Sinh học & Kinh tế (Mỗi bài 6 dòng kẻ):**
  a) **(Tăng trưởng vi khuẩn):** Số lượng vi khuẩn trong một mẻ cấy thí nghiệm tăng với tốc độ $N'(t) = 150 e^{0{,}3t}$ (con/giờ). Biết ban đầu thí nghiệm ($t = 0$) có $500$ con vi khuẩn.
     - Tìm hàm số $N(t)$ biểu thị số lượng vi khuẩn tại thời điểm $t$.
     - Ước tính số lượng vi khuẩn sau 4 giờ (làm tròn đến hàng đơn vị).
  b) **(Chi phí sản xuất):** Một công ty sản xuất thiết bị điện tử có chi phí cận biên để sản xuất $x$ sản phẩm mỗi ngày là $C'(x) = 3x^2 - 12x + 40$ (nghìn đồng/sản phẩm). Biết chi phí cố định ban đầu của công ty là $500$ nghìn đồng ($C(0) = 500$).
     - Tìm hàm tổng chi phí $C(x)$.
     - Tính tổng chi phí khi sản xuất 10 sản phẩm trong ngày.
