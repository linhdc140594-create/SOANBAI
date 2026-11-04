# TỔNG HỢP CÁC CÁCH GIẢI CHI TIẾT VÀ PHÂN TÍCH SƯ PHẠM
## CHUYÊN ĐỀ: TAM GIÁC BẰNG NHAU & TOÁN ĐỐ PHÂN SỐ (TOÁN 7)
*(Tài liệu biên soạn dựa trên tham vấn API chuyên sâu từ ảnh bài tập học sinh)*

---

## 📌 ĐỀ BÀI TỔNG HỢP (TỪ ẢNH CHỤP VỞ HỌC SINH)

* **Bài 1:** Cho $\Delta ABC = \Delta MNP$ có $AB = 5\text{ cm}$, $AC = 7\text{ cm}$, $NP = (2x + 1)\text{ cm}$ và chu vi tam giác $ABC$ bằng $21\text{ cm}$. Tìm $x$.
* **Bài 2:** Một thùng chứa $120$ lít nước, lần thứ nhất người ta dùng $\dfrac{1}{4}$ lượng nước trong thùng; lần thứ hai dùng $\dfrac{2}{5}$ lượng nước còn lại sau lần thứ nhất. Hỏi sau hai lần dùng, trong thùng còn bao nhiêu lít nước?
* **Bài 3:** Cho tam giác $ABC$. Trên nửa mặt phẳng bờ $AC$ không chứa điểm $B$, lấy điểm $D$ sao cho $AD = BC$ và $CD = AB$.
  Vẽ hình và ghi giả thiết, kết luận của bài toán; sau đó:
  a) Chứng minh $\Delta ABC = \Delta CDA$.
  b) Chứng minh $AB \parallel CD$.
  c) Cho $\widehat{BAC} = 50^\circ$ và $\widehat{ABC} = 60^\circ$. Tính số đo $\widehat{ACB}$.

---

## 💡 BÀI 1: TÌM ẨN SỐ TRONG TAM GIÁC BẰNG NHAU

### 🎯 Phân tích cốt lõi
Ký hiệu hai tam giác bằng nhau $\Delta ABC = \Delta MNP$ quy định thứ tự các đỉnh tương ứng:
$$A \longleftrightarrow M, \quad B \longleftrightarrow N, \quad C \longleftrightarrow P$$
Do đó các cạnh tương ứng bằng nhau:
$$AB = MN = 5\text{ cm}, \quad AC = MP = 7\text{ cm}, \quad BC = NP = (2x + 1)\text{ cm}$$

---

### Các cách giải

#### 🔹 Cách 1: Tìm cạnh tương ứng trước rồi lập phương trình (Chuẩn mực THCS)
* Bước 1: Tính độ dài cạnh $BC$ của $\Delta ABC$:
  Chu vi tam giác $ABC$ là $C_{\Delta ABC} = AB + AC + BC = 21\text{ cm}$.
  Suy ra:
  $$BC = 21 - AB - AC = 21 - 5 - 7 = 9\text{ (cm)}$$
* Bước 2: Vì $\Delta ABC = \Delta MNP$ nên hai cạnh tương ứng bằng nhau:
  $$NP = BC \implies 2x + 1 = 9$$
* Bước 3: Giải phương trình tìm $x$:
  $$2x = 9 - 1 \iff 2x = 8 \iff x = 4$$
* Kết luận: Vậy $x = 4$.

#### 🔹 Cách 2: Sử dụng tính chất "Hai tam giác bằng nhau có cùng chu vi"
* Vì $\Delta ABC = \Delta MNP$ nên chu vi của $\Delta MNP$ bằng chu vi của $\Delta ABC$:
  $$C_{\Delta MNP} = C_{\Delta ABC} = 21\text{ cm}$$
* Các cạnh tương ứng: $MN = AB = 5\text{ cm}$, $MP = AC = 7\text{ cm}$, $NP = 2x + 1\text{ cm}$.
* Chu vi $\Delta MNP$ là tổng độ dài 3 cạnh:
  $$MN + MP + NP = 21 \iff 5 + 7 + (2x + 1) = 21$$
  $$\iff 2x + 13 = 21 \iff 2x = 8 \iff x = 4$$
* Kết luận: Vậy $x = 4$.

#### 🔹 Cách 3: Phương pháp số học và sơ đồ đoạn thẳng trực quan
* Coi chu vi tam giác $21\text{ cm}$ gồm 3 đoạn thẳng nối tiếp:
  - Đoạn 1: $AB = 5\text{ cm}$.
  - Đoạn 2: $AC = 7\text{ cm}$.
  - Đoạn 3: Cạnh còn lại $BC = NP = 2x + 1$.
* Tổng hai cạnh đã biết: $5 + 7 = 12\text{ cm}$.
* Cạnh còn lại $NP$ là: $21 - 12 = 9\text{ cm}$.
* Bài toán trở về tìm $x$ trong số học tiểu học:
  $2 \times x + 1 = 9 \implies 2 \times x = 8 \implies x = 4$.

#### 🔹 Cách 4: Phương pháp kiểm tra điều kiện hình học (Bất đẳng thức tam giác)
* Với $x = 4$, độ dài ba cạnh của tam giác là: $5\text{ cm}, 7\text{ cm}, 9\text{ cm}$.
* Kiểm tra bất đẳng thức tam giác:
  $$5 + 7 = 12 > 9 \quad (\text{đúng})$$
  $$5 + 9 = 14 > 7 \quad (\text{đúng})$$
  $$7 + 9 = 16 > 5 \quad (\text{đúng})$$
  Tam giác hoàn toàn tồn tại thực tế và nghiệm $x = 4$ hoàn toàn chính xác.

---

### ⚠️ Sai lầm học sinh thường gặp ở Bài 1
1. **Xác định sai cạnh tương ứng:** Học sinh không chú ý thứ tự đỉnh, gán nhầm $NP = AB = 5$ hoặc $NP = AC = 7$, dẫn tới giải sai $2x + 1 = 5 \implies x = 2$.
2. **Nhầm cạnh với chu vi:** Lập phương trình $2x + 1 = 21 \implies x = 10$.
3. **Quên kiểm tra điều kiện độ dài hình học:** Độ dài cạnh phải dương $2x + 1 > 0 \implies x > -0{,}5$ và thỏa mãn bất đẳng thức tam giác.

---

## 💡 BÀI 2: TOÁN THỰC TẾ VỀ PHÂN SỐ CỦA MỘT SỐ

### 🎯 Phân tích cốt lõi
* Tổng lượng nước ban đầu: $120$ lít.
* Lần 1: Dùng $\dfrac{1}{4}$ của **lượng nước trong thùng ban đầu**.
* Lần 2: Dùng $\dfrac{2}{5}$ của **lượng nước CÒN LẠI sau lần thứ nhất** (từ khóa mấu chốt).

---

### Các cách giải

#### 🔹 Cách 1: Giải từng bước cụ thể theo số học (Dễ hiểu nhất, chuẩn SGK)
1. Lượng nước người ta dùng trong lần thứ nhất là:
   $$120 \times \frac{1}{4} = 30\text{ (lít)}$$
2. Lượng nước còn lại trong thùng sau lần dùng thứ nhất là:
   $$120 - 30 = 90\text{ (lít)}$$
3. Lượng nước người ta dùng trong lần thứ hai là:
   $$90 \times \frac{2}{5} = 36\text{ (lít)}$$
4. Sau hai lần dùng, lượng nước còn lại trong thùng là:
   $$90 - 36 = 54\text{ (lít)}$$
   *(hoặc $120 - 30 - 36 = 54$ lít)*
* Đáp số: $54$ lít.

#### 🔹 Cách 2: Tìm phân số chỉ lượng nước còn lại (Nhân phân số liên tiếp - Tinh gọn nhất)
1. Sau lần thứ nhất, phân số chỉ lượng nước còn lại so với lượng nước ban đầu là:
   $$1 - \frac{1}{4} = \frac{3}{4}\text{ (lượng nước ban đầu)}$$
2. Vì lần thứ hai dùng $\dfrac{2}{5}$ lượng nước còn lại sau lần một, nên phân số chỉ lượng nước còn lại sau lần hai so với lượng nước còn lại sau lần một là:
   $$1 - \frac{2}{5} = \frac{3}{5}\text{ (lượng nước còn lại sau lần 1)}$$
3. Phân số chỉ lượng nước còn lại sau cả hai lần so với lượng nước ban đầu là:
   $$\frac{3}{4} \times \frac{3}{5} = \frac{9}{20}\text{ (lượng nước ban đầu)}$$
4. Lượng nước còn lại sau hai lần dùng là:
   $$120 \times \frac{9}{20} = 54\text{ (lít)}$$

#### 🔹 Cách 3: Quy về phân số so với tổng ban đầu rồi tính tổng lượng đã dùng
1. Phân số chỉ lượng nước dùng lần thứ hai so với ban đầu là:
   $$\frac{2}{5} \times \left(1 - \frac{1}{4}\right) = \frac{2}{5} \times \frac{3}{4} = \frac{3}{10}\text{ (lượng nước ban đầu)}$$
2. Phân số chỉ tổng lượng nước đã dùng sau cả hai lần là:
   $$\frac{1}{4} + \frac{3}{10} = \frac{5}{20} + \frac{6}{20} = \frac{11}{20}\text{ (lượng nước ban đầu)}$$
3. Tổng lượng nước đã dùng sau cả hai lần là:
   $$120 \times \frac{11}{20} = 66\text{ (lít)}$$
4. Lượng nước còn lại trong thùng là:
   $$120 - 66 = 54\text{ (lít)}$$

#### 🔹 Cách 4: Phương pháp sơ đồ đoạn thẳng (Quy về đơn vị)
* Mẫu số chung của $\dfrac{1}{4}$ và $\dfrac{2}{5}$ thông qua lượng còn lại là $20$.
* Ta coi $120$ lít nước ban đầu được chia đều thành $20$ phần bằng nhau:
  Giá trị một phần là: $120 : 20 = 6\text{ (lít)}$.
* Lần 1 dùng $\dfrac{1}{4}$ tức dùng: $20 \times \dfrac{1}{4} = 5\text{ phần}$.
  Còn lại sau lần 1: $20 - 5 = 15\text{ phần}$.
* Lần 2 dùng $\dfrac{2}{5}$ của số phần còn lại: $15 \times \dfrac{2}{5} = 6\text{ phần}$.
* Số phần còn lại sau cả hai lần là:
  $$15 - 6 = 9\text{ (phần)}$$
* Lượng nước còn lại là:
  $$9 \times 6 = 54\text{ (lít)}$$

#### 🔹 Cách 5: Tính theo tỉ số phần trăm
* Lượng nước ban đầu là $100\% = 120$ lít.
* Lần 1 dùng $\dfrac{1}{4} = 25\%$, còn lại: $100\% - 25\% = 75\%$.
* Lần 2 dùng $\dfrac{2}{5} = 40\%$ của $75\%$, tức chiếm: $40\% \times 75\% = 30\%$ lượng ban đầu.
* Sau 2 lần, lượng nước còn lại chiếm:
  $$75\% - 30\% = 45\%\text{ (lượng ban đầu)}$$
* Lượng nước còn lại là:
  $$120 \times 45\% = 120 \times 0{,}45 = 54\text{ (lít)}$$

---

### ⚠️ Bẫy sai lầm kinh điển ở Bài 2
* **Sai lầm phổ biến nhất:** Học sinh lấy $\dfrac{2}{5}$ nhân với $120$ thay vì nhân với lượng còn lại ($90$ lít):
  $120 \times \dfrac{2}{5} = 48\text{ lít} \implies 120 - 30 - 48 = 42\text{ lít}$ (**SAI**).
* **Cộng hai phân số trực tiếp:** $\dfrac{1}{4} + \dfrac{2}{5} = \dfrac{13}{20}$ rồi lấy $120 \times \left(1 - \dfrac{13}{20}\right) = 42\text{ lít}$ (**SAI** vì hai phân số không cùng quy chiếu về lượng nước ban đầu).

---

## 💡 BÀI 3: HÌNH HỌC TAM GIÁC BẰNG NHAU VÀ HAI ĐƯỜNG THẲNG SONG SONG

### 📐 Hình vẽ và Giả thiết - Kết luận

```
                D ------------------ C
               /                    /
              /                    /
             /                    /
            A ------------------ B
```

$$\begin{array}{|l|l|}
\hline
\textbf{Giả thiết (GT)} & \Delta ABC; \ D \text{ thuộc nửa mặt phẳng bờ } AC \text{ không chứa } B; \\
& AD = BC; \ CD = AB; \\
& \widehat{BAC} = 50^\circ; \ \widehat{ABC} = 60^\circ \text{ (áp dụng cho câu c)}. \\
\hline
\textbf{Kết luận (KL)} & \text{a) } \Delta ABC = \Delta CDA. \\
& \text{b) } AB \parallel CD. \\
& \text{c) Tính } \widehat{ACB}. \\
\hline
\end{array}$$

---

### 🔹 Câu a: Chứng minh $\Delta ABC = \Delta CDA$

* **Lời giải chuẩn (Trường hợp cạnh - cạnh - cạnh):**
  Xét $\Delta ABC$ và $\Delta CDA$, ta có:
  - $AB = CD$ (theo giả thiết).
  - $BC = DA$ (theo giả thiết vì $AD = BC$).
  - $AC$ là cạnh chung.
  
  Do đó:
  $$\Delta ABC = \Delta CDA \text{ (c.c.c)}$$

* **Lưu ý đặc biệt quan trọng về thứ tự đỉnh:**
  - Cạnh $AB$ đối diện đỉnh $C$, bằng cạnh $CD$ đối diện đỉnh $A \implies C \longleftrightarrow A$.
  - Cạnh $BC$ đối diện đỉnh $A$, bằng cạnh $DA$ đối diện đỉnh $C \implies A \longleftrightarrow C$.
  - Cạnh chung $AC$ đối diện đỉnh $B$, bằng cạnh chung $CA$ đối diện đỉnh $D \implies B \longleftrightarrow D$.
  - Bắt buộc phải viết đúng: $\Delta ABC = \Delta CDA$ (viết $\Delta ABC = \Delta CAD$ hoặc $\Delta ADC$ là **sai hoàn toàn**).

---

### 🔹 Câu b: Chứng minh $AB \parallel CD$

#### Cách 1: Dùng cặp góc so le trong bằng nhau (Cách tối ưu nhất)
* Từ kết quả câu a: $\Delta ABC = \Delta CDA$, suy ra:
  $$\widehat{BAC} = \widehat{DCA} \text{ (hai góc tương ứng)}$$
* Vì điểm $B$ và $D$ nằm trên hai nửa mặt phẳng đối nhau bờ $AC$, nên hai góc $\widehat{BAC}$ và $\widehat{DCA}$ ở vị trí **so le trong** đối với cát tuyến $AC$.
* Theo dấu hiệu nhận biết hai đường thẳng song song, suy ra:
  $$AB \parallel CD \quad (\text{đpcm})$$

#### Cách 2: Kẻ thêm đường chéo phụ $BD$
* Nối đoạn thẳng $BD$.
* Xét $\Delta ABD$ và $\Delta CDB$, ta có:
  - $AB = CD$ (giả thiết).
  - $AD = CB$ (giả thiết).
  - $BD$ là cạnh chung.
  $\implies \Delta ABD = \Delta CDB \text{ (c.c.c)}$.
* Suy ra: $\widehat{ABD} = \widehat{CDB}$ (hai góc tương ứng).
* Hai góc này ở vị trí so le trong đối với cát tuyến $BD$, do đó $AB \parallel CD$.

#### Cách 3: Dùng phương pháp phản chứng (Rèn luyện tư duy logic cao)
* Giả sử $AB$ không song song với $CD$, khi đó đường thẳng $AB$ và $CD$ cắt nhau tại điểm $O$.
* Tam giác $OAC$ có cát tuyến $AC$, với góc $\widehat{BAC}$ và $\widehat{DCA}$ bằng nhau nhưng ở vị trí so le trong $\implies$ dẫn tới một góc trong bằng một góc ngoài không kề, vô lý với định lí góc ngoài tam giác.
* Vậy điều giả sử là sai $\implies AB \parallel CD$.

---

### 🔹 Câu c: Tính số đo $\widehat{ACB}$ khi $\widehat{BAC} = 50^\circ$ và $\widehat{ABC} = 60^\circ$

#### Cách 1: Áp dụng định lí tổng ba góc trong $\Delta ABC$ (Nhanh và trực tiếp nhất)
* Xét tam giác $ABC$, áp dụng định lí tổng ba góc trong một tam giác:
  $$\widehat{BAC} + \widehat{ABC} + \widehat{ACB} = 180^\circ$$
* Thay số:
  $$50^\circ + 60^\circ + \widehat{ACB} = 180^\circ$$
  $$\implies 110^\circ + \widehat{ACB} = 180^\circ \implies \widehat{ACB} = 180^\circ - 110^\circ = 70^\circ$$
* Kết luận: Vậy $\widehat{ACB} = 70^\circ$.

#### Cách 2: Sử dụng góc ngoài của tam giác
* Vẽ tia đối $Cx$ của tia $CB$.
* Góc $\widehat{ACx}$ là góc ngoài tại đỉnh $C$ của $\Delta ABC$, theo tính chất góc ngoài:
  $$\widehat{ACx} = \widehat{BAC} + \widehat{ABC} = 50^\circ + 60^\circ = 110^\circ$$
* Vì $\widehat{ACB}$ và $\widehat{ACx}$ là hai góc kề bù:
  $$\widehat{ACB} = 180^\circ - \widehat{ACx} = 180^\circ - 110^\circ = 70^\circ$$

#### Cách 3: Tính gián tiếp thông qua tam giác bằng nhau $\Delta CDA$
* Do $\Delta ABC = \Delta CDA$ (chứng minh ở câu a), nên:
  $$\widehat{CDA} = \widehat{ABC} = 60^\circ \quad \text{và} \quad \widehat{DCA} = \widehat{BAC} = 50^\circ$$
* Xét $\Delta CDA$, tổng ba góc trong tam giác bằng $180^\circ$:
  $$\widehat{CAD} = 180^\circ - (\widehat{CDA} + \widehat{DCA}) = 180^\circ - (60^\circ + 50^\circ) = 70^\circ$$
* Mặt khác, vì $\Delta ABC = \Delta CDA$ nên hai góc tương ứng $\widehat{ACB} = \widehat{CAD}$.
* Suy ra $\widehat{ACB} = 70^\circ$.

#### Cách 4: Dùng tính chất hai đường thẳng song song và hai góc trong cùng phía
* Tương tự câu b, ta cũng có $\widehat{BCA} = \widehat{DAC}$ (so le trong) $\implies AD \parallel BC$.
* Khi $AD \parallel BC$, hai góc trong cùng phía đối với cát tuyến $AB$ bù nhau:
  $$\widehat{DAB} + \widehat{ABC} = 180^\circ \implies \widehat{DAB} = 180^\circ - 60^\circ = 120^\circ$$
* Mà tia $AC$ nằm giữa hai tia $AB, AD$ nên:
  $$\widehat{DAB} = \widehat{BAC} + \widehat{CAD} \implies \widehat{CAD} = 120^\circ - 50^\circ = 70^\circ$$
* Do $\widehat{ACB} = \widehat{CAD}$ (hai góc tương ứng của hai tam giác bằng nhau) $\implies \widehat{ACB} = 70^\circ$.

---

## 🚀 BÀI TOÁN PHÁT TRIỂN & MỞ RỘNG TƯ DUY
1. **Mở rộng 1:** Chứng minh thêm $AD \parallel BC$. Từ đó kết luận tứ giác $ABCD$ là hình bình hành (kiến thức chuẩn bị cho lớp 8).
2. **Mở rộng 2:** Gọi $O$ là giao điểm của $AC$ và $BD$. Chứng minh $\Delta AOB = \Delta COD$, từ đó suy ra $O$ là trung điểm của cả $AC$ và $BD$ (hai đường chéo cắt nhau tại trung điểm của mỗi đường).
3. **Mở rộng 3:** Tính toàn bộ số đo các góc của tứ giác $ABCD$:
   - $\widehat{B} = \widehat{D} = 60^\circ$.
   - $\widehat{A} = \widehat{C} = 50^\circ + 70^\circ = 120^\circ$.
   Tổng bốn góc của tứ giác: $60^\circ + 60^\circ + 120^\circ + 120^\circ = 360^\circ$ (khớp hoàn hảo với định lí tổng các góc của tứ giác).

