# KẾ HOẠCH BÀI DẠY: NGUYÊN HÀM (BUỔI 3)
## CHUYÊN ĐỀ: PHƯƠNG PHÁP ĐỔI BIẾN SỐ & KỸ THUẬT VI PHÂN
*(Chương trình Toán 12 -- GDPT 2018 | Lớp Toán Thầy Lĩnh | Bộ 8 Trang A4 Có Dòng Kẻ)*

---

## 🎯 I. MỤC TIÊU SƯ PHẠM BUỔI 3

1. **Chuyển dịch tư duy: Từ nguyên hàm trực tiếp sang nguyên hàm gián tiếp:**
   - Ở Buổi 1 & 2, học sinh đã thành thạo việc khai triển đại số, chia đa thức, hạ bậc lượng giác để đưa về bảng nguyên hàm cơ bản và mở rộng $ax+b$.
   - Buổi 3 đưa học sinh bước vào phương pháp giải tích quan trọng nhất: **Phương pháp Đổi biến số loại 1** (Đặt $t = u(x)$).
   - Xây dựng **"Con mắt nhìn vi phân" (Pattern Recognition)**: Học sinh nhìn vào một biểu thức phức hợp là phát hiện ngay mối liên hệ giữa hàm số $u(x)$ và đạo hàm $u'(x)dx$ của nó.

2. **Làm chủ 6 họ bài toán đổi biến số cốt lõi:**
   - **Họ 1 (Đại số & Lũy thừa):** Đặt $t = ax^2 + b$, $t = ax^3 + b$, vi phân bậc giảm 1.
   - **Họ 2 (Căn thức):** Đặt $t = \sqrt{u(x)} \implies t^2 = u(x) \implies 2t\,dt = u'(x)dx$.
   - **Họ 3 (Hàm số Mũ):** Nhận diện $(e^x)' = e^x$, đặt $t = e^x$ hoặc $t = \text{mẫu}$.
   - **Họ 4 (Hàm số Logarit):** Nhận diện $(\ln x)' = \frac{1}{x}$, đặt $t = \ln x$ khi có cụm $\frac{dx}{x}$.
   - **Họ 5 (Lượng giác bậc lẻ & $\tan/\cot$):** Tách vi phân lượng giác $(-d(\cos x), d(\sin x), \frac{dx}{\cos^2 x})$.
   - **Họ 6 (Kỹ thuật vi phân nhẩm & Hàm ẩn $f(x)$):** Rèn phản xạ trắc nghiệm $10$ giây và bài toán hàm ẩn mức 8+.

3. **Quy chuẩn tài liệu:**
   - Phiếu gồm **chính xác 8 trang A4** (4 tờ in 2 mặt).
   - Dòng kẻ chấm mờ cự ly $18.5\text{pt}$ chuẩn viết tay học sinh THPT.
   - Đầu mỗi trang có khung **"CẢNH BÁO LỖI SAI & PHƯƠNG PHÁP VÀNG"**.
   - Bố trí lề đáy đạt chuẩn **10 -- 15 mm**.

---

## 📑 II. MA TRẬN 8 TRANG A4 CHI TIẾT

```
[Trang 1: Đổi biến Đa thức & Phân thức] ───► [Trang 2: Đổi biến Căn thức & Rút lũy thừa]
                 │                                            │
[Trang 3: Đổi biến Hàm số Mũ e^x] ────────► [Trang 4: Đổi biến Logarit ln x & dx/x]
                 │                                            │
[Trang 5: Đổi biến Lượng giác sin, cos] ──► [Trang 6: Đổi biến tan, cot & Lượng giác phụ]
                 │                                            │
[Trang 7: Kỹ thuật Vi phân du & Hàm ẩn] ──► [Trang 8: Tìm hằng số C & Ứng dụng Thực tế]
```

---

### 📄 TRANG 1: PHƯƠNG PHÁP ĐỔI BIẾN SỐ -- ĐA THỨC VÀ PHÂN THỨC HỮU TỈ
* **Khung ghi nhớ:** 
  $$\int f(u(x)) \cdot u'(x) \, dx = \int f(u) \, du = F(u) + C = F(u(x)) + C$$
  *Quy trình 4 bước: 1) Đặt $t = u(x) \implies$ 2) Lấy vi phân $dt = u'(x)dx \implies$ 3) Biểu diễn nguyên hàm theo $t \implies$ 4) Lấy nguyên hàm và trả về biến $x$.*
* **Bài 1 (4,0 điểm) -- Đổi biến đa thức lũy thừa bậc cao (4 câu, mỗi câu 5 dòng kẻ):**
  a) $\int 2x(x^2 + 1)^4 \, dx$
  b) $\int 3x^2(x^3 - 2)^5 \, dx$
  c) $\int x(2x^2 + 3)^6 \, dx$
  d) $\int x^2(1 - 2x^3)^4 \, dx$
* **Bài 2 (4,0 điểm) -- Đổi biến phân thức hữu tỉ mẫu lũy thừa (4 câu, mỗi câu 5 dòng kẻ):**
  a) $\int \frac{2x}{(x^2 + 1)^2} \, dx$
  b) $\int \frac{x}{(2x^2 + 3)^3} \, dx$
  c) $\int \frac{3x^2}{(x^3 - 1)^4} \, dx$
  d) $\int \frac{x - 1}{(x^2 - 2x + 5)^3} \, dx$

---

### 📄 TRANG 2: KỸ THUẬT ĐỔI BIẾN CĂN THỨC & RÚT THỪA SỐ LŨY THỪA
* **Khung phương pháp:**
  - *Khẩu quyết: "Gặp căn thức $\sqrt{u(x)}$, thường đặt $t = \text{căn}$. Sau đó BÌNH PHƯƠNG 2 vế rồi mới lấy vi phân để triệt tiêu căn, tránh phát sinh phân số!"*
  - $t = \sqrt{u(x)} \implies t^2 = u(x) \implies 2t\,dt = u'(x)\,dx \implies t\,dt = \frac{1}{2}u'(x)\,dx$.
* **Bài 3 (4,0 điểm) -- Căn thức bậc hai cơ bản (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int 2x\sqrt{x^2 + 1} \, dx$
  b) $\int x\sqrt{3 - x^2} \, dx$
  c) $\int \frac{x}{\sqrt{x^2 + 4}} \, dx$
  d) $\int \frac{x}{\sqrt{1 - 2x^2}} \, dx$
* **Bài 4 (4,0 điểm) -- Kỹ thuật rút thừa số $x^3, x^5$ & Căn bậc ba (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int x^3\sqrt{x^2 + 1} \, dx$ *(Gợi ý: $x^3 = x^2 \cdot x$, đặt $t = \sqrt{x^2+1} \implies x^2 = t^2 - 1$)*
  b) $\int x^3(x^2 - 2)^5 \, dx$
  c) $\int x^2\sqrt[3]{x^3 + 1} \, dx$ *(Đặt $t = \sqrt[3]{x^3+1} \implies t^3 = x^3 + 1 \implies 3t^2 dt = 3x^2 dx$)*
  d) $\int \frac{x^3}{\sqrt{x^2 + 2}} \, dx$

---

### 📄 TRANG 3: ĐỔI BIẾN HÀM SỐ MŨ ($e^x$ VÀ $a^x$)
* **Khung phương pháp:**
  - Đạo hàm hàm mũ: $(e^x)' = e^x$. Do đó, khi thấy biểu thức chứa $e^x$ đi kèm với cụm $e^x dx \implies$ Đặt $t = e^x$ hoặc $t$ là căn thức chứa $e^x$.
  - Mũ phức tạp: $\int x e^{x^2} dx \implies t = x^2 \implies dt = 2x\,dx$.
* **Bài 5 (4,0 điểm) -- Hàm mũ nguyên hàm trực diện & phân thức (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int e^x (e^x + 2)^3 \, dx$
  b) $\int \frac{e^x}{e^x + 3} \, dx$
  c) $\int \frac{e^x}{(e^x + 1)^2} \, dx$
  d) $\int \frac{e^x}{2e^x - 1} \, dx$
* **Bài 6 (4,0 điểm) -- Hàm mũ chứa căn thức và mũ biến đổi (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int e^x \sqrt{e^x + 1} \, dx$
  b) $\int \frac{e^x}{\sqrt{2e^x + 3}} \, dx$
  c) $\int x e^{x^2 + 1} \, dx$
  d) $\int \frac{e^{2x}}{e^x + 1} \, dx$ *(Gợi ý: $e^{2x} = e^x \cdot e^x$, đặt $t = e^x + 1$)*

---

### 📄 TRANG 4: ĐỔI BIẾN HÀM SỐ LOGARIT ($\ln x$)
* **Khung phương pháp:**
  - Nhận diện cốt lõi: $(\ln x)' = \frac{1}{x}$.
  - Cứ thấy $\ln x$ xuất hiện đồng thời với mẫu số có $x$ (tức có cụm $\frac{dx}{x}$) $\implies$ Đặt $t = \ln x$ (hoặc $t = a\ln x + b$, $t = \sqrt{\dots}$).
* **Bài 7 (4,0 điểm) -- Biểu thức chứa $\ln x$ và $\frac{1}{x}$ cơ bản (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{\ln x}{x} \, dx$
  b) $\int \frac{(\ln x)^3 + 1}{x} \, dx$
  c) $\int \frac{1}{x \ln x} \, dx$
  d) $\int \frac{2\ln x + 3}{x} \, dx$
* **Bài 8 (4,0 điểm) -- Logarit chứa mẫu lũy thừa và căn thức (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{1}{x(\ln x + 1)^2} \, dx$
  b) $\int \frac{\sqrt{\ln x + 2}}{x} \, dx$
  c) $\int \frac{1}{x\sqrt{2\ln x + 1}} \, dx$
  d) $\int \frac{\ln x}{x(\ln^2 x + 1)} \, dx$

---

### 📄 TRANG 5: ĐỔI BIẾN HÀM LƯỢNG GIÁC ($\sin x$ VÀ $\cos x$ BẬC LẺ)
* **Khung phương pháp:**
  - Biểu thức chứa $\sin x$ bậc lẻ $\longrightarrow$ tách $1$ lượng $\sin x\,dx = -d(\cos x)$, đưa phần còn lại về $\cos x$ bằng $\sin^2 x = 1 - \cos^2 x$, đặt $t = \cos x$.
  - Biểu thức chứa $\cos x$ bậc lẻ $\longrightarrow$ tách $1$ lượng $\cos x\,dx = d(\sin x)$, đưa phần còn lại về $\sin x$ bằng $\cos^2 x = 1 - \sin^2 x$, đặt $t = \sin x$.
* **Bài 9 (4,0 điểm) -- Lượng giác tích lũy thừa bậc lẻ (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \sin x \cos^4 x \, dx$
  b) $\int \cos x \sin^5 x \, dx$
  c) $\int \sin^3 x \cos^2 x \, dx$
  d) $\int \cos^3 x \, dx = \int (1 - \sin^2 x)\cos x \, dx$
* **Bài 10 (4,0 điểm) -- Phân thức lượng giác và căn thức (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{\cos x}{\sin x + 2} \, dx$
  b) $\int \frac{\sin x}{(2\cos x + 1)^2} \, dx$
  c) $\int \sin x \sqrt{\cos x + 1} \, dx$
  d) $\int \frac{\cos x}{\sqrt{3\sin x + 1}} \, dx$

---

### 📄 TRANG 6: ĐỔI BIẾN LƯỢNG GIÁC CHỨA $\tan x, \cot x$ & KỸ THUẬT PHỤ
* **Khung phương pháp:**
  - Nhận diện $\tan$: $(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x \implies$ Thấy $\frac{dx}{\cos^2 x}$ đặt $t = \tan x$.
  - Nhận diện $\cot$: $(\cot x)' = -\frac{1}{\sin^2 x} = -(1 + \cot^2 x) \implies$ Thấy $\frac{dx}{\sin^2 x}$ đặt $t = \cot x$.
* **Bài 11 (4,0 điểm) -- Nguyên hàm chứa $\tan x, \cot x$ (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx$
  b) $\int \cot x \, dx = \int \frac{\cos x}{\sin x} \, dx$
  c) $\int \frac{\tan x + 1}{\cos^2 x} \, dx$
  d) $\int \frac{\sqrt{\tan x}}{\cos^2 x} \, dx$
* **Bài 12 (4,0 điểm) -- Đổi biến nâng cao & lượng giác nhân tử (4 câu, mỗi câu 7 dòng kẻ):**
  a) $\int \frac{e^{\tan x}}{\cos^2 x} \, dx$
  b) $\int \frac{\sin 2x}{1 + \cos^2 x} \, dx$ *(Gợi ý: $(\cos^2 x)' = -\sin 2x$)*
  c) $\int \frac{\sin 2x}{(2 + \sin^2 x)^2} \, dx$
  d) $\int \frac{1}{\sin x} \, dx = \int \frac{\sin x}{\sin^2 x} \, dx = \int \frac{\sin x}{1 - \cos^2 x} \, dx$

---

### 📄 TRANG 7: KỸ THUẬT VI PHÂN SIÊU TỐC ($du$) & BÀI TOÁN HÀM ẨN
* **Khung phương pháp:**
  - Bộ 4 công thức vi phân nhẩm nhanh trắc nghiệm:
    1) $\int [u(x)]^n \cdot u'(x) \, dx = \frac{[u(x)]^{n+1}}{n+1} + C$
    2) $\int \frac{u'(x)}{u(x)} \, dx = \ln|u(x)| + C$
    3) $\int \frac{u'(x)}{\sqrt{u(x)}} \, dx = 2\sqrt{u(x)} + C$
    4) $\int e^{u(x)} \cdot u'(x) \, dx = e^{u(x)} + C$
* **Bài 13 (4,0 điểm) -- Điền kết quả nhanh bằng kỹ thuật vi phân nhẩm (6 câu, mỗi câu 4 dòng kẻ):**
  a) $\int 4x(2x^2 + 1)^5 \, dx$
  b) $\int \frac{2x + 1}{x^2 + x + 1} \, dx$
  c) $\int \frac{2x}{\sqrt{x^2 + 5}} \, dx$
  d) $\int 3x^2 e^{x^3} \, dx$
  e) $\int \frac{\cos x}{\sin x + 3} \, dx$
  f) $\int \frac{1}{x(\ln^2 x + 4)} \cdot 2\ln x \, dx$
* **Bài 14 (4,0 điểm) -- Bài toán Hàm ẩn $f(x)$ và đạo hàm $f'(x)$ (2 câu, mỗi câu 11 dòng kẻ):**
  a) Cho hàm số $f(x)$ liên tục và không âm trên $\mathbb{R}$ thỏa mãn $f'(x) \cdot \sqrt{f(x)} = 3x^2$ với mọi $x \in \mathbb{R}$ và $f(0) = 4$. Hãy xác định công thức hàm số $f(x)$.
  b) Cho hàm số $f(x) > 0$ thỏa mãn hệ thức $\frac{f'(x)}{f(x)} = 2x - 3$ với mọi $x \in \mathbb{R}$ và $f(1) = 1$. Hãy tìm giá trị nhỏ nhất của hàm số $f(x)$ trên $\mathbb{R}$.

---

### 📄 TRANG 8: TÌM HẰNG SỐ $C$ & BÀI TOÁN THỰC TẾ NÂNG CAO (PHI TUYẾN)
* **Khung phương pháp:**
  - Kết hợp đổi biến số tìm họ nguyên hàm $F(x) + C$, thay điểm $(x_0, y_0)$ để tìm $C$.
  - Vật lý: Vận tốc $v(t) = \int a(t)dt$, Quãng đường $s(t) = \int v(t)dt$ khi hàm phi tuyến chứa căn/mẫu.
  - Y học: Nồng độ thuốc $C(t) = \int C'(t)dt$.
* **Bài 15 (4,0 điểm) -- Tìm nguyên hàm $F(x)$ thỏa mãn $F(x_0) = y_0$ bằng đổi biến (2 câu, mỗi câu 7 dòng kẻ):**
  a) Tìm nguyên hàm $F(x)$ của hàm số $f(x) = \frac{2x + 1}{\sqrt{x^2 + x + 2}}$ biết rằng $F(1) = 6$.
  b) Tìm nguyên hàm $F(x)$ của hàm số $f(x) = \frac{e^x}{e^x + 1}$ biết rằng đồ thị hàm số $F(x)$ đi qua điểm $M(0; \ln 2 + 3)$.
* **Bài 16 (4,0 điểm) -- Bài toán thực tế liên môn Vật lý & Y học (2 câu, mỗi bài 6 dòng kẻ):**
  a) **[Vật lý -- Chuyển động biến đổi phi tuyến]** Một vật chuyển động thẳng có vận tốc tức thời phụ thuộc thời gian $t$ (giây) theo công thức $v(t) = t\sqrt{t^2 + 9}\text{ (m/s)}$. Biết tại thời điểm ban đầu $t = 0$, vật ở gốc tọa độ $s(0) = 0\text{ m}$.
     - Thiết lập phương trình quãng đường $s(t)$ của vật theo thời gian $t$.
     - Tính quãng đường vật di chuyển được sau $4$ giây đầu tiên.
  b) **[Y học -- Nồng độ thuốc trong huyết tương]** Sau khi tiêm một liều kháng sinh vào cơ thể bệnh nhân, tốc độ thay đổi nồng độ thuốc trong máu sau $t$ giờ được mô tả bởi hàm số $C'(t) = \frac{20t}{(t^2 + 1)^2}\text{ (mg/L/giờ)}$. Biết rằng tại thời điểm bắt đầu tiêm ($t = 0$), nồng độ thuốc trong máu bằng $0$ ($C(0) = 0$).
     - Xác định hàm số nồng độ thuốc $C(t)$ theo thời gian $t$.
     - Tính nồng độ thuốc trong máu sau $3$ giờ tiêm (làm tròn kết quả đến $2$ chữ số thập phân).
