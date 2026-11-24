# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 11 - BUỔI 02 (TOÁN 8)
## CHỦ ĐỀ TRỌNG TÂM: CỘNG TRỪ NHÂN CHIA ĐA THỨC - PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ - ĐỊNH LÝ THALES
### Bám sát chương trình: SGK Toán 8 - Kết nối tri thức với cuộc sống & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ ĐỊNH HƯỚNG NỘI DUNG (THEO YÊU CẦU ĐIỀU CHỈNH)

1. **Phạm vi kiến thức:**
   - **Đại số:**
     - Hoàn toàn loại bỏ phần Phân thức đại số.
     - Tập trung sâu vào 2 kỹ năng cốt lõi:
       + **Thực hiện phép tính (Câu 11):** Gồm đủ 4 phép toán cơ bản: **cộng, trừ, nhân, chia đa thức** (cộng đa thức nhiều biến, trừ đa thức, nhân đơn thức với đa thức, nhân đa thức với đa thức, chia đa thức cho đơn thức, chia đa thức một biến đã sắp xếp).
       + **Phân tích đa thức thành nhân tử (Câu 12):** Phương pháp đặt nhân tử chung, dùng hằng đẳng thức hiệu hai bình phương, nhóm hạng tử, phối hợp hằng đẳng thức.
   - **Hình học (Câu 13):**
     - Hoàn toàn loại bỏ tính chất đường phân giác.
     - Tập trung trọng tâm vào **Định lý Thales**:
       + **Ý a:** Chứng minh hai đường thẳng song song bằng **Định lý Thales đảo** (xét tỉ số các đoạn thẳng tương ứng trên hai cạnh).
       + **Ý b:** Tính độ dài đoạn thẳng chưa biết bằng **Hệ quả của định lý Thales** và tính toán đoạn thẳng trên cạnh.
     - **Quy chuẩn đồ họa & dàn trang:** Cột đề bên trái thu hẹp khoảng 2cm (`0.57\linewidth`), cột hình vẽ bên phải mở rộng (`0.41\linewidth`), hình vẽ TikZ chỉ vẽ sẵn tam giác ban đầu để học sinh tự dựng các điểm và đoạn thẳng khi làm bài.
   - **Vận dụng cao (Câu 14):**
     - Tìm giá trị nhỏ nhất (GTNN) của tam thức bậc hai đại số (không chứa phân thức).

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

| STT | Dạng bài | Số câu / Ý | Điểm số | Vị trí trên phiếu | Quy chuẩn định dạng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Trả lời ngắn (Short Answer) | 10 câu | 2,5 đ | Trang 1 (Đầu trang) | Lệnh `\shortans`, ô `KQ: [   ]` sát mép phải. |
| **2** | Thực hiện phép tính (Cộng, trừ, nhân, chia đa thức) | 6 ý ($a \to f$) | 3,0 đ | Trang 1 (Cuối trang) | Bảng $3 \times 2$, dùng `\oBaiTap[6]` lấp kín lề dưới Trang 1. |
| **3** | Phân tích đa thức thành nhân tử | 4 ý ($a \to d$) | 2,0 đ | Trang 2 (Đầu trang) | Bảng $2 \times 2$, dùng `\oBaiTap[5]`. |
| **4** | Hình học Định lý Thales | 2 ý ($a, b$) | 2,0 đ | Trang 2 (Giữa trang) | Cột đề `0.57\linewidth`, cột hình `0.41\linewidth`, bài giải `\dongkeHaiCot{11}`. |
| **5** | Vận dụng cao điểm 10 (GTNN) | 1 bài | 0,5 đ | Trang 2 (Cuối trang) | Ghép box `tabularx`, bài giải `\dongkeHaiCot{7}` sát lề dưới Trang 2. |
| **TỔNG** | | **23 mục** | **10,0 đ** | **2 mặt A4** | **Chính xác 8 trang PDF cho 4 mã đề (101-104)** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Tỉ số hai đoạn thẳng | $AB=6\text{ cm}, CD=8\text{ cm} \implies \dfrac{AB}{CD} =$ **$\dfrac{3}{4}$** | $MN=4\text{ cm}, PQ=10\text{ cm} \implies \dfrac{MN}{PQ} =$ **$\dfrac{2}{5}$** | $AB=9\text{ cm}, CD=12\text{ cm} \implies \dfrac{AB}{CD} =$ **$\dfrac{3}{4}$** | $EF=6\text{ cm}, GH=15\text{ cm} \implies \dfrac{EF}{GH} =$ **$\dfrac{2}{5}$** |
| **2** | Định lý Thales (tính đoạn trên cạnh) | $DE \parallel BC$, $AD=3\text{ cm}, DB=2\text{ cm}, AE=6\text{ cm} \implies EC =$ **$4\text{ cm}$** | $DE \parallel BC$, $AD=2\text{ cm}, DB=4\text{ cm}, AE=3\text{ cm} \implies EC =$ **$6\text{ cm}$** | $DE \parallel BC$, $AD=4\text{ cm}, DB=2\text{ cm}, AE=8\text{ cm} \implies EC =$ **$4\text{ cm}$** | $DE \parallel BC$, $AD=3\text{ cm}, DB=6\text{ cm}, AE=4\text{ cm} \implies EC =$ **$8\text{ cm}$** |
| **3** | Hệ quả Thales (tính đoạn song song) | $MN \parallel BC$, $\dfrac{AM}{AB}=\dfrac{2}{3}, BC=15 \implies MN =$ **$10\text{ cm}$** | $MN \parallel BC$, $\dfrac{AM}{AB}=\dfrac{3}{4}, BC=16 \implies MN =$ **$12\text{ cm}$** | $MN \parallel BC$, $\dfrac{AM}{AB}=\dfrac{2}{5}, BC=20 \implies MN =$ **$8\text{ cm}$** | $MN \parallel BC$, $\dfrac{AM}{AB}=\dfrac{3}{5}, BC=25 \implies MN =$ **$15\text{ cm}$** |
| **4** | Nhân đơn thức với đa thức | $2x(3x^2 - 4x + 1) =$ **$6x^3 - 8x^2 + 2x$** | $3x(2x^2 - 5x + 2) =$ **$6x^3 - 15x^2 + 6x$** | $2x(4x^2 - 3x + 2) =$ **$8x^3 - 6x^2 + 4x$** | $3x(3x^2 - 4x + 1) =$ **$9x^3 - 12x^2 + 3x$** |
| **5** | Khai triển bình phương hiệu | Khai triển $(2x - 3)^2 =$ **$4x^2 - 12x + 9$** | Khai triển $(3x - 2)^2 =$ **$9x^2 - 12x + 4$** | Khai triển $(2x - 5)^2 =$ **$4x^2 - 20x + 25$** | Khai triển $(3x - 1)^2 =$ **$9x^2 - 6x + 1$** |
| **6** | Phân tích thành nhân tử (đặt NTC) | Phân tích $5x^2 - 10xy =$ **$5x(x - 2y)$** | Phân tích $6x^2 - 12xy =$ **$6x(x - 2y)$** | Phân tích $4x^2 - 12xy =$ **$4x(x - 3y)$** | Phân tích $7x^2 - 14xy =$ **$7x(x - 2y)$** |
| **7** | Phân tích thành nhân tử (hiệu 2 bình phương) | Phân tích $9x^2 - 25 =$ **$(3x - 5)(3x + 5)$** | Phân tích $4x^2 - 49 =$ **$(2x - 7)(2x + 7)$** | Phân tích $16x^2 - 9 =$ **$(4x - 3)(4x + 3)$** | Phân tích $25x^2 - 36 =$ **$(5x - 6)(5x + 6)$** |
| **8** | Tính nhanh bằng HĐT bình phương một tổng | $73^2 + 27^2 + 54 \cdot 73 =$ **$10\,000$** | $84^2 + 16^2 + 32 \cdot 84 =$ **$10\,000$** | $68^2 + 32^2 + 64 \cdot 68 =$ **$10\,000$** | $77^2 + 23^2 + 46 \cdot 77 =$ **$10\,000$** |
| **9** | Thực tế đo chiều cao cây bằng Thales | Cọc cao $2\text{ m}$ bóng $1{,}5\text{ m}$; bóng cây $6\text{ m} \implies$ **$8\text{ m}$** | Cọc cao $2\text{ m}$ bóng $1{,}2\text{ m}$; bóng tháp $9\text{ m} \implies$ **$15\text{ m}$** | Cọc cao $1{,}8\text{ m}$ bóng $1{,}2\text{ m}$; bóng cây $8\text{ m} \implies$ **$12\text{ m}$** | Cọc cao $2\text{ m}$ bóng $1{,}5\text{ m}$; bóng cột $7{,}5\text{ m} \implies$ **$10\text{ m}$** |
| **10** | Định lý Thales đảo (điều kiện song song) | Điểm $M \in AB, N \in AC$. ĐK để $MN \parallel BC$ là **$\dfrac{AM}{MB} = \dfrac{AN}{NC}$** | Điểm $D \in AB, E \in AC$. ĐK để $DE \parallel BC$ là **$\dfrac{AD}{AB} = \dfrac{AE}{AC}$** | Điểm $M \in AB, N \in AC$. ĐK để $MN \parallel BC$ là **$\dfrac{AM}{AB} = \dfrac{AN}{AC}$** | Điểm $D \in AB, E \in AC$. ĐK để $DE \parallel BC$ là **$\dfrac{AD}{DB} = \dfrac{AE}{EC}$** |

---

### 2. CÂU 11 (3,0 ĐIỂM - THỰC HIỆN PHÉP TÍNH: CỘNG, TRỪ, NHÂN, CHIA ĐA THỨC - 6 Ý $A \to F$)

* **Mã đề 101:**
  - $a)$ $(3x^2y - 2xy^2 + 5xy) + (2x^2y + 4xy^2 - 5xy)$
  - $b)$ $(5x^3 - 4x^2 + 7x - 2) - (2x^3 - 4x^2 - 3x + 5)$
  - $c)$ $2x^2y(3x^2 - 4xy + y^2)$
  - $d)$ $(2x - 3)(x^2 - 4x + 1)$
  - $e)$ $(12x^4y^3 - 8x^3y^2 + 4x^2y) : 4x^2y$
  - $f)$ $(2x^3 - 5x^2 + 6x - 2) : (2x - 1)$

* **Mã đề 102:**
  - $a)$ $(4x^2y - 3xy^2 + 2xy) + (x^2y + 5xy^2 - 2xy)$
  - $b)$ $(6x^3 - 5x^2 + 8x - 3) - (2x^3 - 5x^2 - 2x + 4)$
  - $c)$ $3x^2y(2x^2 - 3xy + y^2)$
  - $d)$ $(2x - 1)(x^2 - 5x + 2)$
  - $e)$ $(15x^4y^3 - 9x^3y^2 + 3x^2y) : 3x^2y$
  - $f)$ $(2x^3 - 7x^2 + 7x - 2) : (2x - 1)$

* **Mã đề 103:**
  - $a)$ $(5x^2y - 4xy^2 + 3xy) + (2x^2y + 6xy^2 - 3xy)$
  - $b)$ $(7x^3 - 3x^2 + 6x - 4) - (3x^3 - 3x^2 - 4x + 5)$
  - $c)$ $2x^2y(4x^2 - 3xy + y^2)$
  - $d)$ $(3x - 2)(x^2 - 3x + 1)$
  - $e)$ $(16x^4y^3 - 12x^3y^2 + 4x^2y) : 4x^2y$
  - $f)$ $(3x^3 - 7x^2 + 5x - 1) : (3x - 1)$

* **Mã đề 104:**
  - $a)$ $(2x^2y - 5xy^2 + 4xy) + (3x^2y + 7xy^2 - 4xy)$
  - $b)$ $(5x^3 - 6x^2 + 9x - 1) - (x^3 - 6x^2 - x + 6)$
  - $c)$ $3x^2y(3x^2 - 4xy + y^2)$
  - $d)$ $(2x - 3)(x^2 - 3x + 2)$
  - $e)$ $(18x^4y^3 - 12x^3y^2 + 6x^2y) : 6x^2y$
  - $f)$ $(2x^3 - 9x^2 + 13x - 6) : (2x - 3)$

---

### 3. CÂU 12 (2,0 ĐIỂM - PHÂN TÍCH ĐA THỨC THÀNH NHÂN TỬ - 4 Ý $A \to D$)

* **Mã đề 101:**
  - $a)$ $4x^2 - 12x = 4x(x - 3)$
  - $b)$ $9x^2 - 16 = (3x - 4)(3x + 4)$
  - $c)$ $xy - 2y + 3x - 6 = (x - 2)(y + 3)$
  - $d)$ $x^2 - 2xy + y^2 - 25 = (x - y - 5)(x - y + 5)$

* **Mã đề 102:**
  - $a)$ $5x^2 - 15x = 5x(x - 3)$
  - $b)$ $16x^2 - 25 = (4x - 5)(4x + 5)$
  - $c)$ $xy - 3y + 4x - 12 = (x - 3)(y + 4)$
  - $d)$ $x^2 - 2xy + y^2 - 36 = (x - y - 6)(x - y + 6)$

* **Mã đề 103:**
  - $a)$ $6x^2 - 18x = 6x(x - 3)$
  - $b)$ $25x^2 - 4 = (5x - 2)(5x + 2)$
  - $c)$ $xy - 4y + 2x - 8 = (x - 4)(y + 2)$
  - $d)$ $x^2 - 2xy + y^2 - 49 = (x - y - 7)(x - y + 7)$

* **Mã đề 104:**
  - $a)$ $3x^2 - 12x = 3x(x - 4)$
  - $b)$ $4x^2 - 49 = (2x - 7)(2x + 7)$
  - $c)$ $xy - 5y + 3x - 15 = (x - 5)(y + 3)$
  - $d)$ $x^2 - 2xy + y^2 - 64 = (x - y - 8)(x - y + 8)$

---

### 4. CÂU 13 (2,0 ĐIỂM - HÌNH HỌC ĐỊNH LÝ THALES)

* **Mã đề 101:**
  Cho tam giác $ABC$ nhọn ($AB < AC$), có $AB = 12\text{ cm}, AC = 15\text{ cm}$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 4\text{ cm}$, trên cạnh $AC$ lấy điểm $E$ sao cho $AE = 5\text{ cm}$.
  - $a)$ (1,0 điểm): Chứng minh rằng $DE \parallel BC$ (sử dụng định lý Thales đảo).
  - $b)$ (1,0 điểm): Biết $BC = 18\text{ cm}$. Tính độ dài đoạn thẳng $DE$ và độ dài đoạn thẳng $DB$.
  *(Đáp số: $DE = 6\text{ cm}, DB = 8\text{ cm}$)*

* **Mã đề 102:**
  Cho tam giác $MNP$ nhọn ($MN < MP$), có $MN = 12\text{ cm}, MP = 16\text{ cm}$. Trên cạnh $MN$ lấy điểm $D$ sao cho $MD = 3\text{ cm}$, trên cạnh $MP$ lấy điểm $E$ sao cho $ME = 4\text{ cm}$.
  - $a)$ (1,0 điểm): Chứng minh rằng $DE \parallel NP$ (sử dụng định lý Thales đảo).
  - $b)$ (1,0 điểm): Biết $NP = 20\text{ cm}$. Tính độ dài đoạn thẳng $DE$ và độ dài đoạn thẳng $DN$.
  *(Đáp số: $DE = 5\text{ cm}, DN = 9\text{ cm}$)*

* **Mã đề 103:**
  Cho tam giác $ABC$ nhọn ($AB < AC$), có $AB = 10\text{ cm}, AC = 15\text{ cm}$. Trên cạnh $AB$ lấy điểm $M$ sao cho $AM = 4\text{ cm}$, trên cạnh $AC$ lấy điểm $N$ sao cho $AN = 6\text{ cm}$.
  - $a)$ (1,0 điểm): Chứng minh rằng $MN \parallel BC$ (sử dụng định lý Thales đảo).
  - $b)$ (1,0 điểm): Biết $BC = 25\text{ cm}$. Tính độ dài đoạn thẳng $MN$ và độ dài đoạn thẳng $MB$.
  *(Đáp số: $MN = 10\text{ cm}, MB = 6\text{ cm}$)*

* **Mã đề 104:**
  Cho tam giác $DEF$ nhọn ($DE < DF$), có $DE = 12\text{ cm}, DF = 18\text{ cm}$. Trên cạnh $DE$ lấy điểm $M$ sao cho $DM = 4\text{ cm}$, trên cạnh $DF$ lấy điểm $N$ sao cho $DN = 6\text{ cm}$.
  - $a)$ (1,0 điểm): Chứng minh rằng $MN \parallel EF$ (sử dụng định lý Thales đảo).
  - $b)$ (1,0 điểm): Biết $EF = 21\text{ cm}$. Tính độ dài đoạn thẳng $MN$ và độ dài đoạn thẳng $ME$.
  *(Đáp số: $MN = 7\text{ cm}, ME = 8\text{ cm}$)*

---

### 5. CÂU 14 (0,5 ĐIỂM - VẬN DỤNG CAO ĐIỂM 10)

* **Mã đề 101:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 6x + 13$.
  *(Lời giải: $A = (x - 3)^2 + 4 \ge 4$. Dấu "$=$" xảy ra khi $x = 3$. Vậy $\min A = 4$.)*
* **Mã đề 102:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 8x + 25$.
  *(Lời giải: $A = (x - 4)^2 + 9 \ge 9$. Dấu "$=$" xảy ra khi $x = 4$. Vậy $\min A = 9$.)*
* **Mã đề 103:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 10x + 31$.
  *(Lời giải: $A = (x - 5)^2 + 6 \ge 6$. Dấu "$=$" xảy ra khi $x = 5$. Vậy $\min A = 6$.)*
* **Mã đề 104:** Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 4x + 15$.
  *(Lời giải: $A = (x - 2)^2 + 11 \ge 11$. Dấu "$=$" xảy ra khi $x = 2$. Vậy $\min A = 11$.)*
