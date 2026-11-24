# ĐÁP ÁN & LỜI GIẢI CHI TIẾT
## PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ
*(Chuyên đề: Phương pháp đổi biến số loại 1 & Kỹ thuật vi phân nhẩm nhanh)*

---

## 📄 TRANG 1: PHƯƠNG PHÁP ĐỔI BIẾN SỐ -- ĐA THỨC VÀ PHÂN THỨC HỮU TỈ

### Bài 1 (4,0 điểm). Đa thức lũy thừa bậc cao
* **a)** $\displaystyle\int 2x(x^2 + 1)^4 \, dx$:
  - Đặt $t = x^2 + 1 \implies dt = 2x\,dx$.
  - Nguyên hàm theo $t$: $\displaystyle\int t^4 \, dt = \frac{t^5}{5} + C$.
  - Trả về biến $x$: $\mathbf{\dfrac{(x^2 + 1)^5}{5} + C}$.
* **b)** $\displaystyle\int 3x^2(x^3 - 2)^5 \, dx$:
  - Đặt $t = x^3 - 2 \implies dt = 3x^2 \, dx$.
  - Nguyên hàm: $\displaystyle\int t^5 \, dt = \frac{t^6}{6} + C = \mathbf{\dfrac{(x^3 - 2)^6}{6} + C}$.
* **c)** $\displaystyle\int x(2x^2 + 3)^6 \, dx$:
  - Đặt $t = 2x^2 + 3 \implies dt = 4x\,dx \implies x\,dx = \dfrac{1}{4}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{4}\int t^6 \, dt = \frac{1}{4} \cdot \frac{t^7}{7} + C = \mathbf{\dfrac{(2x^2 + 3)^7}{28} + C}$.
* **d)** $\displaystyle\int x^2(1 - 2x^3)^4 \, dx$:
  - Đặt $t = 1 - 2x^3 \implies dt = -6x^2 \, dx \implies x^2 \, dx = -\dfrac{1}{6}dt$.
  - Nguyên hàm: $\displaystyle-\frac{1}{6}\int t^4 \, dt = -\frac{1}{6} \cdot \frac{t^5}{5} + C = \mathbf{-\dfrac{(1 - 2x^3)^5}{30} + C}$.

---

### Bài 2 (4,0 điểm). Phân thức hữu tỉ mẫu lũy thừa
* **a)** $\displaystyle\int \frac{2x}{(x^2 + 1)^2} \, dx$:
  - Đặt $t = x^2 + 1 \implies dt = 2x\,dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t^2} \, dt = -\frac{1}{t} + C = \mathbf{-\dfrac{1}{x^2 + 1} + C}$.
* **b)** $\displaystyle\int \frac{x}{(2x^2 + 3)^3} \, dx$:
  - Đặt $t = 2x^2 + 3 \implies dt = 4x\,dx \implies x\,dx = \dfrac{1}{4}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{4}\int t^{-3} \, dt = \frac{1}{4} \cdot \frac{t^{-2}}{-2} + C = \mathbf{-\dfrac{1}{8(2x^2 + 3)^2} + C}$.
* **c)** $\displaystyle\int \frac{3x^2}{(x^3 - 1)^4} \, dx$:
  - Đặt $t = x^3 - 1 \implies dt = 3x^2 \, dx$.
  - Nguyên hàm: $\displaystyle\int t^{-4} \, dt = \frac{t^{-3}}{-3} + C = \mathbf{-\dfrac{1}{3(x^3 - 1)^3} + C}$.
* **d)** $\displaystyle\int \frac{x - 1}{(x^2 - 2x + 5)^3} \, dx$:
  - Đặt $t = x^2 - 2x + 5 \implies dt = (2x - 2)dx = 2(x - 1)dx \implies (x - 1)dx = \dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{2}\int t^{-3} \, dt = \frac{1}{2} \cdot \frac{t^{-2}}{-2} + C = \mathbf{-\dfrac{1}{4(x^2 - 2x + 5)^2} + C}$.

---

## 📄 TRANG 2: ĐỔI BIẾN CĂN THỨC & RÚT THỪA SỐ LŨY THỪA

### Bài 3 (4,0 điểm). Căn thức bậc hai cơ bản
* **a)** $\displaystyle\int 2x\sqrt{x^2 + 1} \, dx$:
  - Đặt $t = \sqrt{x^2 + 1} \implies t^2 = x^2 + 1 \implies 2t\,dt = 2x\,dx$.
  - Nguyên hàm: $\displaystyle\int t \cdot 2t\,dt = 2\int t^2 \, dt = \frac{2}{3}t^3 + C = \mathbf{\dfrac{2}{3}(x^2 + 1)\sqrt{x^2 + 1} + C}$.
* **b)** $\displaystyle\int x\sqrt{3 - x^2} \, dx$:
  - Đặt $t = \sqrt{3 - x^2} \implies t^2 = 3 - x^2 \implies 2t\,dt = -2x\,dx \implies x\,dx = -t\,dt$.
  - Nguyên hàm: $\displaystyle\int t(-t\,dt) = -\int t^2 \, dt = -\frac{t^3}{3} + C = \mathbf{-\dfrac{1}{3}(3 - x^2)\sqrt{3 - x^2} + C}$.
* **c)** $\displaystyle\int \frac{x}{\sqrt{x^2 + 4}} \, dx$:
  - Đặt $t = \sqrt{x^2 + 4} \implies t^2 = x^2 + 4 \implies t\,dt = x\,dx$.
  - Nguyên hàm: $\displaystyle\int \frac{t\,dt}{t} = \int 1\,dt = t + C = \mathbf{\sqrt{x^2 + 4} + C}$.
* **d)** $\displaystyle\int \frac{x}{\sqrt{1 - 2x^2}} \, dx$:
  - Đặt $t = \sqrt{1 - 2x^2} \implies t^2 = 1 - 2x^2 \implies 2t\,dt = -4x\,dx \implies x\,dx = -\dfrac{1}{2}t\,dt$.
  - Nguyên hàm: $\displaystyle\int \frac{-\frac{1}{2}t\,dt}{t} = -\frac{1}{2}t + C = \mathbf{-\dfrac{1}{2}\sqrt{1 - 2x^2} + C}$.

---

### Bài 4 (4,0 điểm). Căn thức bậc cao & rút thừa số
* **a)** $\displaystyle\int x^3\sqrt{x^2 + 1} \, dx = \int x^2\sqrt{x^2 + 1} \cdot x\,dx$:
  - Đặt $t = \sqrt{x^2 + 1} \implies t^2 = x^2 + 1 \implies x^2 = t^2 - 1$ và $t\,dt = x\,dx$.
  - Nguyên hàm: $\displaystyle\int (t^2 - 1)t \cdot t\,dt = \int (t^4 - t^2)dt = \frac{t^5}{5} - \frac{t^3}{3} + C = \mathbf{\dfrac{1}{15}(3x^2 - 2)(x^2 + 1)\sqrt{x^2 + 1} + C}$.
* **b)** $\displaystyle\int x^3(x^2 - 2)^5 \, dx = \int x^2(x^2 - 2)^5 x\,dx$:
  - Đặt $t = x^2 - 2 \implies x^2 = t + 2$ và $x\,dx = \dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{2}\int (t + 2)t^5 dt = \frac{1}{2}\int (t^6 + 2t^5)dt = \mathbf{\dfrac{(x^2 - 2)^7}{14} + \dfrac{(x^2 - 2)^6}{6} + C}$.
* **c)** $\displaystyle\int x^2\sqrt[3]{x^3 + 1} \, dx$:
  - Đặt $t = \sqrt[3]{x^3 + 1} \implies t^3 = x^3 + 1 \implies 3t^2 dt = 3x^2 dx \implies x^2 dx = t^2 dt$.
  - Nguyên hàm: $\displaystyle\int t \cdot t^2 dt = \int t^3 dt = \frac{t^4}{4} + C = \mathbf{\dfrac{1}{4}(x^3 + 1)\sqrt[3]{x^3 + 1} + C}$.
* **d)** $\displaystyle\int \frac{x^3}{\sqrt{x^2 + 2}} \, dx = \int \frac{x^2 \cdot x\,dx}{\sqrt{x^2 + 2}}$:
  - Đặt $t = \sqrt{x^2 + 2} \implies t^2 = x^2 + 2 \implies x^2 = t^2 - 2$ và $t\,dt = x\,dx$.
  - Nguyên hàm: $\displaystyle\int \frac{(t^2 - 2)t\,dt}{t} = \int (t^2 - 2)dt = \frac{t^3}{3} - 2t + C = \mathbf{\dfrac{1}{3}(x^2 - 4)\sqrt{x^2 + 2} + C}$.

---

## 📄 TRANG 3: ĐỔI BIẾN HÀM SỐ MŨ ($e^x$ VÀ $a^x$)

### Bài 5 (4,0 điểm). Hàm mũ trực diện & phân thức
* **a)** $\displaystyle\int e^x (e^x + 2)^3 \, dx$:
  - Đặt $t = e^x + 2 \implies dt = e^x dx$.
  - Nguyên hàm: $\displaystyle\int t^3 dt = \frac{t^4}{4} + C = \mathbf{\dfrac{(e^x + 2)^4}{4} + C}$.
* **b)** $\displaystyle\int \frac{e^x}{e^x + 3} \, dx$:
  - Đặt $t = e^x + 3 \implies dt = e^x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t}dt = \ln|t| + C = \mathbf{\ln(e^x + 3) + C}$ *(do $e^x + 3 > 0$)*.
* **c)** $\displaystyle\int \frac{e^x}{(e^x + 1)^2} \, dx$:
  - Đặt $t = e^x + 1 \implies dt = e^x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t^2}dt = -\frac{1}{t} + C = \mathbf{-\dfrac{1}{e^x + 1} + C}$.
* **d)** $\displaystyle\int \frac{e^x}{2e^x - 1} \, dx$:
  - Đặt $t = 2e^x - 1 \implies dt = 2e^x dx \implies e^x dx = \dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{2}\int \frac{1}{t}dt = \mathbf{\dfrac{1}{2}\ln|2e^x - 1| + C}$.

---

### Bài 6 (4,0 điểm). Hàm mũ chứa căn thức & mũ nâng cao
* **a)** $\displaystyle\int e^x \sqrt{e^x + 1} \, dx$:
  - Đặt $t = \sqrt{e^x + 1} \implies t^2 = e^x + 1 \implies 2t\,dt = e^x dx$.
  - Nguyên hàm: $\displaystyle\int t \cdot 2t\,dt = \frac{2}{3}t^3 + C = \mathbf{\dfrac{2}{3}(e^x + 1)\sqrt{e^x + 1} + C}$.
* **b)** $\displaystyle\int \frac{e^x}{\sqrt{2e^x + 3}} \, dx$:
  - Đặt $t = \sqrt{2e^x + 3} \implies t^2 = 2e^x + 3 \implies 2t\,dt = 2e^x dx \implies e^x dx = t\,dt$.
  - Nguyên hàm: $\displaystyle\int \frac{t\,dt}{t} = t + C = \mathbf{\sqrt{2e^x + 3} + C}$.
* **c)** $\displaystyle\int x e^{x^2 + 1} \, dx$:
  - Đặt $t = x^2 + 1 \implies dt = 2x\,dx \implies x\,dx = \dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{2}\int e^t dt = \mathbf{\dfrac{1}{2}e^{x^2 + 1} + C}$.
* **d)** $\displaystyle\int \frac{e^{2x}}{e^x + 1} \, dx = \int \frac{e^x \cdot e^x dx}{e^x + 1}$:
  - Đặt $t = e^x + 1 \implies e^x = t - 1$ và $dt = e^x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{t - 1}{t}dt = \int \left(1 - \frac{1}{t}\right)dt = t - \ln|t| + C = (e^x + 1) - \ln(e^x + 1) + C = \mathbf{e^x - \ln(e^x + 1) + C}$.

---

## 📄 TRANG 4: ĐỔI BIẾN HÀM SỐ LOGARIT ($\ln x$)

### Bài 7 (4,0 điểm). Biểu thức chứa $\ln x$ và $\dfrac{1}{x}$ cơ bản
* **a)** $\displaystyle\int \frac{\ln x}{x} \, dx$:
  - Đặt $t = \ln x \implies dt = \dfrac{1}{x}dx$.
  - Nguyên hàm: $\displaystyle\int t\,dt = \frac{t^2}{2} + C = \mathbf{\dfrac{\ln^2 x}{2} + C}$.
* **b)** $\displaystyle\int \frac{(\ln x)^3 + 1}{x} \, dx$:
  - Đặt $t = \ln x \implies dt = \dfrac{1}{x}dx$.
  - Nguyên hàm: $\displaystyle\int (t^3 + 1)dt = \mathbf{\dfrac{\ln^4 x}{4} + \ln x + C}$.
* **c)** $\displaystyle\int \frac{1}{x \ln x} \, dx$:
  - Đặt $t = \ln x \implies dt = \dfrac{1}{x}dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t}dt = \ln|t| + C = \mathbf{\ln|\ln x| + C}$.
* **d)** $\displaystyle\int \frac{2\ln x + 3}{x} \, dx$:
  - Đặt $t = 2\ln x + 3 \implies dt = \dfrac{2}{x}dx \implies \dfrac{1}{x}dx = \dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{2}\int t\,dt = \frac{t^2}{4} + C = \mathbf{\ln^2 x + 3\ln x + C}$.

---

### Bài 8 (4,0 điểm). Logarit chứa mẫu lũy thừa và căn thức
* **a)** $\displaystyle\int \frac{1}{x(\ln x + 1)^2} \, dx$:
  - Đặt $t = \ln x + 1 \implies dt = \dfrac{1}{x}dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t^2}dt = -\frac{1}{t} + C = \mathbf{-\dfrac{1}{\ln x + 1} + C}$.
* **b)** $\displaystyle\int \frac{\sqrt{\ln x + 2}}{x} \, dx$:
  - Đặt $t = \sqrt{\ln x + 2} \implies t^2 = \ln x + 2 \implies 2t\,dt = \dfrac{1}{x}dx$.
  - Nguyên hàm: $\displaystyle\int t \cdot 2t\,dt = \frac{2}{3}t^3 + C = \mathbf{\dfrac{2}{3}(\ln x + 2)\sqrt{\ln x + 2} + C}$.
* **c)** $\displaystyle\int \frac{1}{x\sqrt{2\ln x + 1}} \, dx$:
  - Đặt $t = \sqrt{2\ln x + 1} \implies t^2 = 2\ln x + 1 \implies 2t\,dt = \dfrac{2}{x}dx \implies \dfrac{1}{x}dx = t\,dt$.
  - Nguyên hàm: $\displaystyle\int \frac{t\,dt}{t} = t + C = \mathbf{\sqrt{2\ln x + 1} + C}$.
* **d)** $\displaystyle\int \frac{\ln x}{x(\ln^2 x + 1)} \, dx$:
  - Đặt $t = \ln^2 x + 1 \implies dt = 2\ln x \cdot \dfrac{1}{x}dx \implies \dfrac{\ln x}{x}dx = \dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle\frac{1}{2}\int \frac{1}{t}dt = \mathbf{\dfrac{1}{2}\ln(\ln^2 x + 1) + C}$.

---

## 📄 TRANG 5: ĐỔI BIẾN HÀM LƯỢNG GIÁC ($\sin x$ VÀ $\cos x$ BẬC LẺ)

### Bài 9 (4,0 điểm). Lượng giác tích lũy thừa bậc lẻ
* **a)** $\displaystyle\int \sin x \cos^4 x \, dx$:
  - Đặt $t = \cos x \implies dt = -\sin x dx \implies \sin x dx = -dt$.
  - Nguyên hàm: $\displaystyle\int t^4(-dt) = -\frac{t^5}{5} + C = \mathbf{-\dfrac{\cos^5 x}{5} + C}$.
* **b)** $\displaystyle\int \cos x \sin^5 x \, dx$:
  - Đặt $t = \sin x \implies dt = \cos x dx$.
  - Nguyên hàm: $\displaystyle\int t^5 dt = \mathbf{\dfrac{\sin^6 x}{6} + C}$.
* **c)** $\displaystyle\int \sin^3 x \cos^2 x \, dx = \int (1 - \cos^2 x)\cos^2 x \sin x \, dx$:
  - Đặt $t = \cos x \implies \sin x dx = -dt$.
  - Nguyên hàm: $\displaystyle\int (1 - t^2)t^2(-dt) = \int (t^4 - t^2)dt = \mathbf{\dfrac{\cos^5 x}{5} - \dfrac{\cos^3 x}{3} + C}$.
* **d)** $\displaystyle\int \cos^3 x \, dx = \int (1 - \sin^2 x)\cos x \, dx$:
  - Đặt $t = \sin x \implies dt = \cos x dx$.
  - Nguyên hàm: $\displaystyle\int (1 - t^2)dt = \mathbf{\sin x - \dfrac{\sin^3 x}{3} + C}$.

---

### Bài 10 (4,0 điểm). Phân thức lượng giác và căn thức
* **a)** $\displaystyle\int \frac{\cos x}{\sin x + 2} \, dx$:
  - Đặt $t = \sin x + 2 \implies dt = \cos x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t}dt = \mathbf{\ln(\sin x + 2) + C}$.
* **b)** $\displaystyle\int \frac{\sin x}{(2\cos x + 1)^2} \, dx$:
  - Đặt $t = 2\cos x + 1 \implies dt = -2\sin x dx \implies \sin x dx = -\dfrac{1}{2}dt$.
  - Nguyên hàm: $\displaystyle-\frac{1}{2}\int \frac{1}{t^2}dt = \frac{1}{2t} + C = \mathbf{\dfrac{1}{2(2\cos x + 1)} + C}$.
* **c)** $\displaystyle\int \sin x \sqrt{\cos x + 1} \, dx$:
  - Đặt $t = \sqrt{\cos x + 1} \implies t^2 = \cos x + 1 \implies 2t\,dt = -\sin x dx \implies \sin x dx = -2t\,dt$.
  - Nguyên hàm: $\displaystyle\int t(-2t\,dt) = -\frac{2}{3}t^3 + C = \mathbf{-\dfrac{2}{3}(\cos x + 1)\sqrt{\cos x + 1} + C}$.
* **d)** $\displaystyle\int \frac{\cos x}{\sqrt{3\sin x + 1}} \, dx$:
  - Đặt $t = \sqrt{3\sin x + 1} \implies t^2 = 3\sin x + 1 \implies 2t\,dt = 3\cos x dx \implies \cos x dx = \dfrac{2}{3}t\,dt$.
  - Nguyên hàm: $\displaystyle\int \frac{\frac{2}{3}t\,dt}{t} = \frac{2}{3}t + C = \mathbf{\dfrac{2}{3}\sqrt{3\sin x + 1} + C}$.

---

## 📄 TRANG 6: ĐỔI BIẾN LƯỢNG GIÁC $\tan x, \cot x$ & KỸ THUẬT PHỤ

### Bài 11 (4,0 điểm). Nguyên hàm chứa $\tan x, \cot x$
* **a)** $\displaystyle\int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx$:
  - Đặt $t = \cos x \implies dt = -\sin x dx$.
  - Nguyên hàm: $\displaystyle\int -\frac{dt}{t} = -\ln|\cos x| + C = \mathbf{\ln\left|\dfrac{1}{\cos x}\right| + C}$.
* **b)** $\displaystyle\int \cot x \, dx = \int \frac{\cos x}{\sin x} \, dx$:
  - Đặt $t = \sin x \implies dt = \cos x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{dt}{t} = \mathbf{\ln|\sin x| + C}$.
* **c)** $\displaystyle\int \frac{\tan x + 1}{\cos^2 x} \, dx$:
  - Đặt $t = \tan x \implies dt = \dfrac{1}{\cos^2 x}dx$.
  - Nguyên hàm: $\displaystyle\int (t + 1)dt = \mathbf{\dfrac{\tan^2 x}{2} + \tan x + C}$.
* **d)** $\displaystyle\int \frac{\sqrt{\tan x}}{\cos^2 x} \, dx$:
  - Đặt $t = \sqrt{\tan x} \implies t^2 = \tan x \implies 2t\,dt = \dfrac{1}{\cos^2 x}dx$.
  - Nguyên hàm: $\displaystyle\int t \cdot 2t\,dt = \frac{2}{3}t^3 + C = \mathbf{\dfrac{2}{3}\tan x\sqrt{\tan x} + C}$.

---

### Bài 12 (4,0 điểm). Lượng giác nhân tử & nâng cao
* **a)** $\displaystyle\int \frac{e^{\tan x}}{\cos^2 x} \, dx$:
  - Đặt $t = \tan x \implies dt = \dfrac{1}{\cos^2 x}dx$.
  - Nguyên hàm: $\displaystyle\int e^t dt = \mathbf{e^{\tan x} + C}$.
* **b)** $\displaystyle\int \frac{\sin 2x}{1 + \cos^2 x} \, dx$:
  - Nhận xét: $(1 + \cos^2 x)' = -2\cos x \sin x = -\sin 2x$.
  - Đặt $t = 1 + \cos^2 x \implies dt = -\sin 2x dx$.
  - Nguyên hàm: $\displaystyle\int -\frac{dt}{t} = -\ln|t| + C = \mathbf{-\ln(1 + \cos^2 x) + C}$.
* **c)** $\displaystyle\int \frac{\sin 2x}{(2 + \sin^2 x)^2} \, dx$:
  - Đặt $t = 2 + \sin^2 x \implies dt = 2\sin x \cos x dx = \sin 2x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{1}{t^2}dt = -\frac{1}{t} + C = \mathbf{-\dfrac{1}{2 + \sin^2 x} + C}$.
* **d)** $\displaystyle\int \frac{1}{\sin x} \, dx = \int \frac{\sin x \, dx}{\sin^2 x} = \int \frac{\sin x \, dx}{1 - \cos^2 x}$:
  - Đặt $t = \cos x \implies dt = -\sin x dx$.
  - Nguyên hàm: $\displaystyle\int \frac{-dt}{1 - t^2} = \int \frac{dt}{t^2 - 1} = \frac{1}{2}\ln\left|\frac{t - 1}{t + 1}\right| + C = \mathbf{\frac{1}{2}\ln\left|\dfrac{\cos x - 1}{\cos x + 1}\right| + C = \ln\left|\tan\frac{x}{2}\right| + C}$.

---

## 📄 TRANG 7: KỸ THUẬT VI PHÂN SIÊU TỐC ($du$) & BÀI TOÁN HÀM ẨN

### Bài 13 (4,0 điểm). Điền kết quả trực tiếp bằng vi phân nhẩm
* **a)** $\displaystyle\int 4x(2x^2 + 1)^5 \, dx = \int (2x^2 + 1)^5 d(2x^2 + 1) = \mathbf{\dfrac{(2x^2 + 1)^6}{6} + C}$.
* **b)** $\displaystyle\int \frac{2x + 1}{x^2 + x + 1} \, dx = \int \frac{d(x^2 + x + 1)}{x^2 + x + 1} = \mathbf{\ln(x^2 + x + 1) + C}$.
* **c)** $\displaystyle\int \frac{2x}{\sqrt{x^2 + 5}} \, dx = \int \frac{d(x^2 + 5)}{\sqrt{x^2 + 5}} = \mathbf{2\sqrt{x^2 + 5} + C}$.
* **d)** $\displaystyle\int 3x^2 e^{x^3} \, dx = \int e^{x^3} d(x^3) = \mathbf{e^{x^3} + C}$.

---

### Bài 14 (4,0 điểm). Bài toán hàm ẩn mức vận dụng (8+)
* **a) (2,0 điểm)** Xác định $f(x)$ biết $f'(x) \cdot \sqrt{f(x)} = 3x^2$ và $f(0) = 4$:
  - Ta có: $[f(x)]^{1/2} \cdot f'(x) = 3x^2$.
  - Lấy nguyên hàm hai vế theo $x$:
    $$\int [f(x)]^{1/2} f'(x) \, dx = \int 3x^2 \, dx \iff \int [f(x)]^{1/2} d(f(x)) = x^3 + C$$
    $$\iff \frac{[f(x)]^{3/2}}{3/2} = x^3 + C \iff \frac{2}{3}[f(x)]^{3/2} = x^3 + C.$$
  - Thay điều kiện $x = 0, f(0) = 4$:
    $$\frac{2}{3} \cdot 4^{3/2} = 0^3 + C \iff \frac{2}{3} \cdot 8 = C \implies C = \frac{16}{3}.$$
  - Do đó: $\dfrac{2}{3}[f(x)]^{3/2} = x^3 + \dfrac{16}{3} \iff [f(x)]^{3/2} = \dfrac{3}{2}x^3 + 8$.
  - Kết luận: $\mathbf{f(x) = \sqrt[3]{\left(\dfrac{3}{2}x^3 + 8\right)^2}}$.

* **b) (2,0 điểm)** Tìm GTNN của $f(x)$ biết $\dfrac{f'(x)}{f(x)} = 2x - 4$ và $f(1) = e^{-3}$:
  - Lấy nguyên hàm hai vế:
    $$\int \frac{f'(x)}{f(x)} \, dx = \int (2x - 4) \, dx \iff \ln|f(x)| = x^2 - 4x + C.$$
  - Vì $f(x) > 0$ nên $\ln(f(x)) = x^2 - 4x + C \iff f(x) = e^{x^2 - 4x + C}$.
  - Thay $x = 1, f(1) = e^{-3}$:
    $$e^{1^2 - 4(1) + C} = e^{-3} \iff -3 + C = -3 \implies C = 0.$$
  - Do đó: $f(x) = e^{x^2 - 4x}$.
  - Xét số mũ: $g(x) = x^2 - 4x = (x - 2)^2 - 4 \ge -4$ với mọi $x \in \mathbb{R}$.
  - Vì hàm số mũ $y = e^u$ đồng biến trên $\mathbb{R}$ nên:
    $$\min_{\mathbb{R}} f(x) = e^{\min g(x)} = e^{-4} = \frac{1}{e^4}, \quad \text{đạt được khi } x = 2.$$
  - Kết luận: $\mathbf{\min_{\mathbb{R}} f(x) = \dfrac{1}{e^4}}$ tại $x = 2$.

---

## 📄 TRANG 8: TÌM HẰNG SỐ $C$ & TOÁN THỰC TẾ LIÊN MÔN

### Bài 15 (4,0 điểm). Tìm nguyên hàm thỏa mãn điều kiện điểm thuộc
* **a)** Tìm $F(x)$ của $f(x) = \dfrac{2x + 1}{\sqrt{x^2 + x + 2}}$ biết $F(1) = 6$:
  - $F(x) = \displaystyle\int \frac{2x + 1}{\sqrt{x^2 + x + 2}} \, dx = \int \frac{d(x^2 + x + 2)}{\sqrt{x^2 + x + 2}} = 2\sqrt{x^2 + x + 2} + C$.
  - Thay $x = 1$: $F(1) = 2\sqrt{1^2 + 1 + 2} + C = 2\sqrt{4} + C = 4 + C = 6 \implies C = 2$.
  - Kết luận: $\mathbf{F(x) = 2\sqrt{x^2 + x + 2} + 2}$.
* **b)** Tìm $F(x)$ của $f(x) = \dfrac{e^x}{e^x + 1}$ biết đồ thị đi qua $M(0; \ln 2 + 3)$:
  - $F(x) = \displaystyle\int \frac{e^x}{e^x + 1} \, dx = \int \frac{d(e^x + 1)}{e^x + 1} = \ln(e^x + 1) + C$.
  - Đồ thị đi qua $M(0; \ln 2 + 3) \implies F(0) = \ln(e^0 + 1) + C = \ln 2 + C = \ln 2 + 3 \implies C = 3$.
  - Kết luận: $\mathbf{F(x) = \ln(e^x + 1) + 3}$.

---

### Bài 16 (4,0 điểm). Bài toán thực tế liên môn Vật lý & Y học
* **a) (2,0 điểm) [Vật lý -- Chuyển động biến đổi phi tuyến]**
  - **1)** Phương trình quãng đường:
    $$s(t) = \int v(t) \, dt = \int t\sqrt{t^2 + 9} \, dt.$$
    Đặt $u = \sqrt{t^2 + 9} \implies u^2 = t^2 + 9 \implies u\,du = t\,dt$.
    $$s(t) = \int u^2 \, du = \frac{u^3}{3} + C = \frac{1}{3}(t^2 + 9)\sqrt{t^2 + 9} + C.$$
    Tại $t = 0$, $s(0) = 0 \implies \dfrac{1}{3}(9)\sqrt{9} + C = 0 \iff 9 + C = 0 \implies C = -9$.
    $$\mathbf{s(t) = \frac{1}{3}(t^2 + 9)\sqrt{t^2 + 9} - 9\text{ (m)}}.$$
  - **2)** Quãng đường vật đi được sau 4 giây đầu:
    $$s(4) = \frac{1}{3}(4^2 + 9)\sqrt{4^2 + 9} - 9 = \frac{1}{3}(25)(5) - 9 = \frac{125}{3} - 9 = \mathbf{\frac{98}{3} \approx 32{,}67\text{ m}}.$$

* **b) (2,0 điểm) [Y học -- Dược động học nồng độ kháng sinh]**
  - **1)** Xác định hàm số nồng độ $C(t)$:
    $$C(t) = \int C'(t) \, dt = \int \frac{20t}{(t^2 + 1)^2} \, dt.$$
    Đặt $u = t^2 + 1 \implies du = 2t\,dt \implies 20t\,dt = 10\,du$.
    $$C(t) = \int \frac{10}{u^2} \, du = -\frac{10}{u} + C_0 = -\frac{10}{t^2 + 1} + C_0.$$
    Ban đầu $t = 0$, $C(0) = 0 \implies -\dfrac{10}{0 + 1} + C_0 = 0 \implies C_0 = 10$.
    $$\mathbf{C(t) = 10 - \frac{10}{t^2 + 1} = \frac{10t^2}{t^2 + 1}\text{ (mg/L)}}.$$
  - **2)** Nồng độ thuốc trong máu sau 3 giờ tiêm:
    $$C(3) = \frac{10 \cdot 3^2}{3^2 + 1} = \frac{90}{10} = \mathbf{9\text{ mg/L}} \quad \text{(đúng } 9{,}00\text{ mg/L)}.$$
