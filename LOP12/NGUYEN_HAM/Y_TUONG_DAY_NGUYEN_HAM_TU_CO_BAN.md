# KẾ HOẠCH & Ý TƯỞNG GIẢNG DẠY CHUYÊN ĐỀ: NGUYÊN HÀM (TOÁN 12)
## PHƯƠNG PHÁP TIẾP CẬN TỰ NHIÊN -- ĐI TỪ NHỮNG BÀI TOÁN DỄ NHẤT

---

## 🎯 I. TRIẾT LÝ SƯ PHẠM: TẠI SAO HỌC SINH THƯỜNG SỢ NGUYÊN HÀM?

### 1. Rào cản tâm lý của học sinh:
- **Bị ngộp công thức:** Giáo viên thường đưa ra ngay một bảng nguyên hàm gồm 12 -- 15 công thức trừu tượng ($\int x^\alpha dx, \int \frac{1}{x} dx, \int e^x dx, \int \sin x dx, \int \frac{1}{\cos^2 x} dx...$) khiến học sinh mất phương hướng.
- **Loạn dấu giữa Đạo hàm và Nguyên hàm:** Học sinh vừa học xong đạo hàm ở lớp 11 ($\sin' = \cos$, $\cos' = -\sin$) sang nguyên hàm lại bị ngược lại ($\int \sin = -\cos$, $\int \cos = \sin$).
- **Không hiểu bản chất của $+ C$:** Coi $+ C$ là một thủ tục hình thức mà không hiểu nguồn gốc toán học và ý nghĩa thực tế.
- **Thói quen áp dụng sai:** Tự ý áp dụng phép nhân/chia như đạo hàm: $\int [f(x) \cdot g(x)] dx = \int f(x) dx \cdot \int g(x) dx$ (Sai lầm phổ biến nhất!).

### 2. Giải pháp cốt lõi: "ĐẢO CHIỀU TƯ DUY -- LẤY ĐẠO HÀM LÀM BÀN ĐẠP"
* **Quy tắc 1:** Không giới thiệu ký hiệu $\int$ ngay trong 5 phút đầu tiên.
* **Quy tắc 2:** Bắt đầu bằng trò chơi đố vui "Tìm hàm gốc": Đạo hàm của hàm nào thì ra kết quả này?
* **Quy tắc 3:** Chỉ dạy duy nhất **MỘT công thức lũy thừa** trong nửa đầu tiết 1 cho đến khi học sinh thành thạo tuyệt đối.
* **Quy tắc 4:** Xây dựng phản xạ tự kiểm tra: *"Muốn biết mình làm đúng hay sai, chỉ cần lấy kết quả vừa tìm được đem đạo hàm lại!"*

---

## 🚀 II. LỘ TRÌNH 6 CHẶNG BẬC THANG (STEP-BY-STEP PROGRESSION)

```
[Chặng 0: Trò chơi Đảo ngược Đạo hàm & Bí mật của +C]
       │
       ▼
[Chặng 1: Công thức Lũy thừa $x^n$ -- Khẩu quyết: "Mũ cộng 1, chia mũ mới"]
       │
       ▼
[Chặng 2: Tiền xử lý -- Khai triển & Tách phân thức trước khi lấy Nguyên hàm]
       │
       ▼
[Chặng 3: Mở rộng Mũ âm $\frac{1}{x^k}$ & Căn thức $\sqrt[n]{x^m}$]
       │
       ▼
[Chặng 4: Mở rộng Bậc nhất $ax + b$ -- Khẩu quyết: "Nhớ chia cho a"]
       │
       ▼
[Chặng 5: Nguyên hàm Lượng giác & Mũ -- Tuyệt chiêu né bẫy đổi dấu]
       │
       ▼
[Chặng 6: Tìm hằng số $C$ qua điều kiện điểm $F(x_0) = y_0$ & Ứng dụng thực tế]
```

---

### 🟢 CHẶNG 0: TRÒ CHƠI "ĐẢO NGƯỢC ĐẠO HÀM" & BÍ MẬT CỦA HẰNG SỐ $C$

#### 1. Đặt vấn đề tự nhiên:
Thầy viết lên bảng một cột các hàm số đạo hàm quen thuộc lớp 11 và yêu cầu học sinh điền hàm số ban đầu $F(x)$ có đạo hàm bằng $f(x)$:

| Đạo hàm $f(x) = F'(x)$ | Học sinh suy đoán hàm gốc $F(x)$ | Kiểm tra lại bằng đạo hàm |
| :---: | :---: | :---: |
| $2x$ | $x^2$ | $(x^2)' = 2x$ |
| $3x^2$ | $x^3$ | $(x^3)' = 3x^2$ |
| $4x^3$ | $x^4$ | $(x^4)' = 4x^3$ |
| $1$ | $x$ | $(x)' = 1$ |
| $0$ | $5$ hoặc $-7$ hoặc $100$ | $(C)' = 0$ |
| $\cos x$ | $\sin x$ | $(\sin x)' = \cos x$ |

#### 2. Nút thắt sư phạm (Hỏi xoáy để tìm ra $+ C$):
* Thầy hỏi: *"Nếu bạn A trả lời hàm gốc của $2x$ là $x^2 + 5$ thì bạn A đúng hay sai?"*
* Cả lớp kiểm tra: $(x^2 + 5)' = 2x + 0 = 2x \implies$ **Bạn A đúng!**
* Bạn B nói: $x^2 - 100$ cũng có đạo hàm là $2x \implies$ **Bạn B cũng đúng!**
* **Kết luận của Thầy:** Không phải chỉ có 1 hàm, mà có **vô số hàm gốc** sai khác nhau một hằng số $C$.
  $$\text{Họ tất cả các hàm gốc của } 2x \text{ là } x^2 + C \quad (C \in \mathbb{R})$$

#### 3. Giới thiệu ký hiệu chính thức:
* Phép toán đi tìm hàm gốc gọi là phép tính **Nguyên hàm**.
* Ký hiệu chiếc "móc câu": $\int 2x \, dx = x^2 + C$.
  * $\int$: Dấu tích phân / nguyên hàm (chữ S kéo dài -- Sum).
  * $2x$: Biểu thức dưới dấu nguyên hàm ($f(x)$).
  * $dx$: Vi phân biến $x$ (nhắc nhở biến lấy nguyên hàm là biến $x$).
  * $x^2 + C$: Họ nguyên hàm.

---

### 🟢 CHẶNG 1: CÔNG THỨC LŨY THỪA $x^n$ -- KHẨU QUYẾT: "MŨ CỘNG 1, CHIA MŨ MỚI"

#### 1. Xây dựng công thức:
Quan sát quy luật:
* $\int x^1 dx = \dfrac{x^2}{2} + C$
* $\int x^2 dx = \dfrac{x^3}{3} + C$
* $\int x^3 dx = \dfrac{x^4}{4} + C$
* $\int x^4 dx = \dfrac{x^5}{5} + C$

$$\boxed{\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (n \ne -1)}$$

> [!TIP]
> **Khẩu quyết cho học sinh:** *"Lấy số mũ hiện tại cộng thêm 1, rồi đem toàn bộ chia cho chính cái số mũ mới đó!"*

#### 2. Hai tính chất tách rời (Tuyến tính):
* **Hằng số thì để nguyên:** $\int k \cdot f(x) dx = k \int f(x) dx$
* **Tổng, hiệu thì tách riêng làm từng đứa:** $\int [f(x) \pm g(x)] dx = \int f(x) dx \pm \int g(x) dx$

#### 3. Bộ bài tập ví dụ thực chiến (từ dễ đến vừa):
* **Ví dụ 1.1:** $\int 5x^4 dx = 5 \cdot \dfrac{x^5}{5} + C = x^5 + C$.
* **Ví dụ 1.2:** $\int (3x^2 - 4x + 5) dx$:
  * $3x^2 \longrightarrow 3 \cdot \dfrac{x^3}{3} = x^3$
  * $-4x \longrightarrow -4 \cdot \dfrac{x^2}{2} = -2x^2$
  * $5 \longrightarrow 5x$
  * Kết quả: $x^3 - 2x^2 + 5x + C$.
* **Ví dụ 1.3:** $\int (6x^5 - x^3 + 2x - 7) dx = x^6 - \dfrac{x^4}{4} + x^2 - 7x + C$.

---

### 🟢 CHẶNG 2: TIỀN XỬ LÝ -- KHAI TRIỂN & RÚT GỌN TRƯỚC KHI LẤY NGUYÊN HÀM

> [!WARNING]
> **CẢNH BÁO "BẪY TỬ THẦN":**
> Nguyên hàm **TUYỆT ĐỐI KHÔNG CÓ** công thức nhân đôi hay chia đôi trực tiếp:
> $$\int f(x) \cdot g(x) dx \ne \int f(x) dx \cdot \int g(x) dx$$
> $$\int \frac{f(x)}{g(x)} dx \ne \frac{\int f(x) dx}{\int g(x) dx}$$

#### Phương pháp: Gặp nhân, chia, bình phương $\rightarrow$ PHẢI NHÂN TUNG TÓE / CHIA ĐA THỨC về dạng đa thức rồi mới làm!

#### 1. Dạng nhân đa thức / hằng đẳng thức:
* **Ví dụ 2.1:** $\int (x - 2)(2x + 1) dx$
  * *Bước 1 (Nhân phá ngoặc):* $(x - 2)(2x + 1) = 2x^2 + x - 4x - 2 = 2x^2 - 3x - 2$.
  * *Bước 2 (Lấy nguyên hàm từng đơn thức):*
    $$\int (2x^2 - 3x - 2) dx = \frac{2x^3}{3} - \frac{3x^2}{2} - 2x + C.$$
* **Ví dụ 2.2:** $\int (2x - 3)^2 dx$
  * *Khai triển hằng đẳng thức:* $(2x - 3)^2 = 4x^2 - 12x + 9$.
  * *Nguyên hàm:* $\dfrac{4x^3}{3} - 6x^2 + 9x + C$.

#### 2. Dạng phân thức đa thức chia cho đơn thức:
* **Ví dụ 2.3:** $\int \dfrac{3x^4 - 5x^2 + 2x}{x} dx$
  * *Chia từng hạng tử cho $x$:* $\dfrac{3x^4}{x} - \dfrac{5x^2}{x} + \dfrac{2x}{x} = 3x^3 - 5x + 2$.
  * *Nguyên hàm:* $\dfrac{3x^4}{4} - \dfrac{5x^2}{2} + 2x + C$.

---

### 🟢 CHẶNG 3: MỞ RỘNG MŨ ÂM $\dfrac{1}{x^k}$ & CĂN THỨC $\sqrt[n]{x^m}$

Dạy học sinh quy tắc chuyển đổi lũy thừa lớp 11 trước khi áp dụng công thức "Mũ cộng 1, chia mũ mới":

$$\frac{1}{x^k} = x^{-k} \qquad \text{và} \qquad \sqrt[n]{x^m} = x^{\frac{m}{n}}$$

#### 1. Xử lý mẫu số lũy thừa:
* **Ví dụ 3.1:** Tính $\int \dfrac{1}{x^2} dx$:
  * Chuyển thành: $\int x^{-2} dx$.
  * Mũ cộng 1: $-2 + 1 = -1$.
  * Kết quả: $\dfrac{x^{-1}}{-1} + C = -\dfrac{1}{x} + C$.
  *(Đóng khung học thuộc luôn vì bài nào cũng gặp: $\int \frac{1}{x^2} dx = -\frac{1}{x} + C$)*
* **Ví dụ 3.2:** Tính $\int \dfrac{1}{x^3} dx = \int x^{-3} dx = \dfrac{x^{-2}}{-2} + C = -\dfrac{1}{2x^2} + C$.

#### 2. Xử lý căn thức:
* **Ví dụ 3.3:** Tính $\int \sqrt{x} \, dx$:
  * Đổi căn thành mũ: $\sqrt{x} = x^{1/2}$.
  * Mũ cộng 1: $\dfrac{1}{2} + 1 = \dfrac{3}{2}$.
  * Chia cho mũ mới: $\dfrac{x^{3/2}}{3/2} = \dfrac{2}{3} x^{3/2} = \dfrac{2}{3} x\sqrt{x} + C$.
* **Ví dụ 3.4:** Tính $\int \dfrac{1}{\sqrt{x}} dx = \int x^{-1/2} dx = \dfrac{x^{1/2}}{1/2} + C = 2\sqrt{x} + C$.

#### 3. Trường hợp ngoại lệ duy nhất $n = -1$:
Khi gặp $\int \dfrac{1}{x} dx = \int x^{-1} dx$, nếu cộng 1 sẽ ra $x^0 / 0$ (vô nghĩa!).
Do đó, đây là công thức riêng biệt:
$$\boxed{\int \frac{1}{x} dx = \ln|x| + C}$$
*(Nhắc học sinh: Bắt buộc phải có dấu giá trị tuyệt đối $|x|$ vì biểu thức dưới logarit phải dương).*

---

### 🟢 CHẶNG 4: MỞ RỘNG BẬC NHẤT $ax + b$ -- KHẨU QUYẾT: "NHỚ CHIA CHO $a$"

Khi biểu thức bên trong ngoặc là hàm bậc nhất $ax + b$, công thức giữ nguyên dạng nhưng **nhân thêm $\dfrac{1}{a}$**:

$$\boxed{\int f(ax + b) dx = \frac{1}{a} F(ax + b) + C}$$

#### So sánh trực quan để học sinh không bao giờ quên:

| Nguyên hàm cơ bản | Nguyên hàm mở rộng bậc nhất ($ax+b$) | Lưu ý then chốt |
| :--- | :--- | :--- |
| $\int x^4 dx = \dfrac{x^5}{5} + C$ | $\int (2x + 1)^4 dx = \mathbf{\dfrac{1}{2}} \cdot \dfrac{(2x+1)^5}{5} + C = \dfrac{(2x+1)^5}{10} + C$ | Chia cho $a = 2$ |
| $\int \dfrac{1}{x} dx = \ln\|x\| + C$ | $\int \dfrac{1}{3x - 2} dx = \mathbf{\dfrac{1}{3}} \ln\|3x - 2\| + C$ | Chia cho $a = 3$ |
| $\int \dfrac{1}{x^2} dx = -\dfrac{1}{x} + C$ | $\int \dfrac{1}{(4x - 1)^2} dx = \mathbf{\dfrac{1}{4}} \cdot \left(-\dfrac{1}{4x - 1}\right) + C$ | Chia cho $a = 4$ |

---

### 🟢 CHẶNG 5: NGUYÊN HÀM LƯỢNG GIÁC & HÀM MŨ

#### 1. Tuyệt chiêu nhớ dấu Lượng giác:
Vẽ trục tròn lượng giác hoặc dùng khẩu quyết:
* **Đạo hàm:** $\sin$ ra $+\cos$, $\cos$ ra $-\sin$.
* **Nguyên hàm:** ĐI NGƯỢC LẠI $\implies$ **$\sin$ ra $-\cos$, $\cos$ ra $+\sin$**.

$$\int \cos x \, dx = \sin x + C \qquad\qquad \int \sin x \, dx = -\cos x + C$$

* Mở rộng bậc nhất:
  * $\int \cos(3x) dx = \dfrac{1}{3} \sin(3x) + C$
  * $\int \sin(2x - \frac{\pi}{4}) dx = -\dfrac{1}{2} \cos(2x - \frac{\pi}{4}) + C$
* Công thức phân thức lượng giác:
  * $\int \dfrac{1}{\cos^2 x} dx = \tan x + C \implies \int \dfrac{1}{\cos^2(2x)} dx = \dfrac{1}{2}\tan(2x) + C$
  * $\int \dfrac{1}{\sin^2 x} dx = -\cot x + C$

#### 2. Hàm mũ (Dễ nhất trần đời):
* $\int e^x dx = e^x + C \implies \int e^{3x + 1} dx = \dfrac{1}{3} e^{3x+1} + C$.
* $\int a^x dx = \dfrac{a^x}{\ln a} + C \implies \int 2^x dx = \dfrac{2^x}{\ln 2} + C$.

---

### 🟢 CHẶNG 6: DẠNG TOÁN TÌM HẰNG SỐ $C$ & BÀI TOÁN THỰC TẾ

#### 1. Dạng toán tìm $F(x)$ thỏa mãn $F(x_0) = y_0$:
* **Phương pháp 2 bước:**
  * *Bước 1:* Tính nguyên hàm $F(x)$ chứa ẩn $+ C$.
  * *Bước 2:* Thay điểm $(x_0, y_0)$ vào để giải tìm hằng số $C$, sau đó kết luận hàm số $F(x)$ hoàn chỉnh.
* **Ví dụ 6.1:** Tìm nguyên hàm $F(x)$ của hàm số $f(x) = 3x^2 - 4x + 1$, biết $F(1) = 5$.
  * *Giải:*
    * $F(x) = \int (3x^2 - 4x + 1) dx = x^3 - 2x^2 + x + C$.
    * Vì $F(1) = 5 \implies (1)^3 - 2(1)^2 + 1 + C = 5 \iff 0 + C = 5 \implies C = 5$.
    * Vậy $F(x) = x^3 - 2x^2 + x + 5$.

#### 2. Ứng dụng thực tế: Bài toán chuyển động (Vật lý 12):
* Mối liên hệ: $s'(t) = v(t)$ và $v'(t) = a(t)$.
* Đi ngược lại bằng nguyên hàm:
  $$v(t) = \int a(t) dt \qquad \text{và} \qquad s(t) = \int v(t) dt$$
* **Ví dụ 6.2:** Một đoàn tàu đang chạy với vận tốc $v_0 = 20\text{ m/s}$ thì người lái tàu hãm phanh với gia tốc $a(t) = -2\text{ m/s}^2$.
  * Tìm phương trình vận tốc: $v(t) = \int (-2) dt = -2t + C$.
  * Tại thời điểm $t = 0$, $v(0) = 20 \implies C = 20 \implies v(t) = -2t + 20$.
  * Tàu dừng lại khi $v(t) = 0 \iff -2t + 20 = 0 \iff t = 10\text{ (giây)}$.
  * Quãng đường tàu đi được từ khi hãm phanh đến khi dừng hẳn:
    $s(t) = \int (-2t + 20) dt = -t^2 + 20t + C'$. (Với $s(0) = 0 \implies C' = 0$).
    $\implies s(10) = -(10)^2 + 20(10) = 100\text{ m}$.

---

## 📝 III. MA TRẬN PHIẾU BÀI TẬP BẬC THANG DÀNH CHO HỌC SINH MỚI BẮT ĐẦU

Thầy có thể chia đề thành 4 mức độ rõ ràng để học sinh làm bài không bị sốc:

### Mức độ 1: Nhận biết -- Áp dụng 1 bước công thức (10 câu ngắn)
1. $\int x^5 dx$
2. $\int 7x^6 dx$
3. $\int (4x^3 - 2x + 1) dx$
4. $\int \frac{1}{x^2} dx$
5. $\int \frac{1}{x} dx$
6. $\int \cos x dx$
7. $\int \sin x dx$
8. $\int e^x dx$
9. $\int 3^x dx$
10. $\int \frac{1}{\cos^2 x} dx$

### Mức độ 2: Thông hiểu -- Tiền xử lý biến đổi trước (Khai triển / Chia đa thức)
1. $\int (x + 1)(2x - 3) dx$
2. $\int (3x - 1)^2 dx$
3. $\int \dfrac{2x^3 - 4x^2 + 5}{x^2} dx$
4. $\int \left(\sqrt{x} + \dfrac{1}{\sqrt{x}}\right) dx$
5. $\int \tan^2 x \, dx$ *(Gợi ý: $\tan^2 x = \frac{1}{\cos^2 x} - 1$)*

### Mức độ 3: Mở rộng bậc nhất $ax + b$
1. $\int (3x - 2)^5 dx$
2. $\int \dfrac{1}{2x + 5} dx$
3. $\int \dfrac{1}{(3x - 1)^2} dx$
4. $\int \cos(4x + \frac{\pi}{3}) dx$
5. $\int e^{5x - 2} dx$

### Mức độ 4: Vận dụng -- Tìm nguyên hàm thỏa mãn điều kiện $F(x_0) = y_0$
1. Tìm $F(x)$ của $f(x) = 4x^3 - 6x$, biết $F(1) = 3$.
2. Tìm $F(x)$ của $f(x) = \cos x + 2$, biết $F(0) = 1$.
3. Tìm $F(x)$ của $f(x) = \dfrac{1}{2x - 1}$, biết $F(1) = 2$.
4. Một chất điểm chuyển động với vận tốc $v(t) = 3t^2 - 2t\text{ (m/s)}$. Biết tại thời điểm ban đầu $t=0$, chất điểm ở vị trí $s(0) = 5\text{ m}$. Tính quãng đường vật đi được sau $3$ giây.

---

## ⚠️ IV. SỔ TAY "CHỐNG BẪY VÀ SAI LẦM KINH ĐIỂN" (DÀNH CHO HỌC SINH)

| Sai lầm thường gặp | Bản chất sai | Sửa lại cho đúng |
| :--- | :--- | :--- |
| $\int x^4 dx = 4x^3 + C$ | Lẫn lộn với công thức **Đạo hàm** | Phải tăng số mũ: $\dfrac{x^5}{5} + C$ |
| $\int (x^2 + 1)(x - 3) dx = \left(\frac{x^3}{3} + x\right)\left(\frac{x^2}{2} - 3x\right)$ | Tự bịa ra nguyên hàm của tích bằng tích nguyên hàm | **Bắt buộc nhân phá ngoặc** thành $x^3 - 3x^2 + x - 3$ rồi mới lấy nguyên hàm |
| $\int \dfrac{1}{3x+1} dx = \ln\|3x+1\| + C$ | **Quên chia cho hệ số $a$** của $ax+b$ | Phải có $\dfrac{1}{a}$: $\mathbf{\dfrac{1}{3}} \ln\|3x+1\| + C$ |
| $\int \cos(2x) dx = -2\sin(2x) + C$ | Vừa nhầm dấu đạo hàm, vừa nhân $a$ thay vì chia $a$ | Nguyên hàm $\cos$ ra $+\sin$, chia cho 2: $\mathbf{\dfrac{1}{2}} \sin(2x) + C$ |
| $\int \dfrac{1}{x^3} dx = \ln\|x^3\| + C$ | Nghĩ mẫu số nào cũng ra $\ln$ | Chỉ có bậc 1 mới ra $\ln$. Mẫu mũ cao phải đổi sang $x^{-3} \implies \dfrac{x^{-2}}{-2} = -\dfrac{1}{2x^2} + C$ |
| Quên viết $+ C$ trong bài tự luận | Bị trừ $0{,}25$đ mỗi câu | Luôn kiểm tra đuôi $+ C$ trước khi nộp bài |

