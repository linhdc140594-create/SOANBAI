# KẾ HOẠCH NỘI DUNG & THIẾT KẾ PHIẾU BÀI TẬP CHUYÊN ĐỀ (4 TRANG)
## CHUYÊN ĐỀ: GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH (TOÁN 9)
### ÔN THI ĐỊNH KỲ GIỮA HỌC KỲ 1 & TRỌNG TÂM LUYỆN THI VÀO LỚP 10
**Đơn vị biên soạn:** Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU & ĐỊNH HƯỚNG SƯ PHẠM
1. **Mục tiêu kiến thức:**
   - Học sinh nắm vững quy trình 3 bước giải bài toán bằng cách lập hệ phương trình bậc nhất hai ẩn theo chuẩn SGK mới (Kết nối tri thức / Cánh diều).
   - Nắm chắc phương pháp lập bảng phân tích dữ kiện 3 cột/3 dòng cho từng thể loại toán lời văn.
   - Tránh các bẫy phổ biến trong kỳ thi vào 10: Quên đặt điều kiện cho ẩn, quên đổi đơn vị đo (phút sang giờ), quên kiểm tra và đối chiếu điều kiện trước khi kết luận.
2. **Quy chuẩn định dạng:**
   - **Quy mô:** Đúng chuẩn **4 trang A4** (tương đương 2 tờ giấy in 2 mặt hoặc 1 tài liệu chuyên đề gập đôi).
   - **Trình bày:** Sử dụng font chữ sư phạm chuẩn, khung hộp lý thuyết trang trọng (`tcolorbox` / `tabularx`), bảng biểu kẻ viền rõ ràng, dòng kẻ chấm mờ viết tay chuẩn mực (`\dongke`).
   - **Số liệu toán học:** 100% số liệu thực tế, nghiệm nguyên đẹp, không lẻ, chuẩn tính toán.

---

## 📐 II. CẤU TRÚC CHI TIẾT BỐ CỤC 4 TRANG A4

```
┌───────────────────────────────────────────────┬───────────────────────────────────────────────┐
│ TRANG 1/4: TỔNG QUAN PHƯƠNG PHÁP &            │ TRANG 2/4: DẠNG 2: TOÁN NĂNG SUẤT &           │
│            DẠNG 1: TOÁN CHUYỂN ĐỘNG           │            CÔNG VIỆC CHUNG - RIÊNG, VÒI NƯỚC  │
│ 1. Khung 3 bước vàng giải toán lập hệ PT      │ 1. Phương pháp & Công thức then chốt (A=N*t)  │
│ 2. Dạng 1: Chuyển động (Đường bộ & Đường thủy)│ 2. Bảng phân tích mẫu công việc chung/riêng   │
│    - Bảng phân tích mẫu S = v * t             │ 3. Ví dụ mẫu có lời giải chi tiết             │
│    - Ví dụ mẫu có lời giải mẫu mực            │ 4. Hệ thống 3 bài tập tự luyện chọn lọc       │
│ 3. Hệ thống 3 bài tập tự luyện chọn lọc       │    (Kèm ô kẻ đáp số & dòng kẻ trình bày)      │
├───────────────────────────────────────────────┼───────────────────────────────────────────────┤
│ TRANG 3/4: DẠNG 3: TOÁN HÌNH HỌC THỰC TẾ &    │ TRANG 4/4: DẠNG 4: TOÁN PHẦN TRĂM, KINH TẾ &  │
│            QUAN HỆ SỐ, CẤU TẠO SỐ             │            BÀI TOÁN THỰC TẾ NÂNG CAO VÀO 10   │
│ 1. Phương pháp: Kích thước HCN & Cấu tạo số   │ 1. Phương pháp: Giá bán, chiết khấu, nồng độ  │
│ 2. Ví dụ mẫu hình học mảnh vườn thay đổi S    │ 2. Ví dụ mẫu kinh tế mua sắm / vượt mức       │
│ 3. Hệ thống 3 bài tập tự luyện chọn lọc       │ 3. Hệ thống 3 bài tập tự luyện chọn lọc       │
│    (Kèm ô kẻ đáp số & dòng kẻ trình bày)      │ 4. Bảng tổng kết thang điểm & lưu ý tránh bẫy │
└───────────────────────────────────────────────┴───────────────────────────────────────────────┘
```

---

## 📝 III. MA TRẬN BÀI TẬP & SỐ LIỆU TOÁN HỌC TỪNG TRANG

### 🔹 TRANG 1: TỔNG QUAN PHƯƠNG PHÁP & DẠNG 1: TOÁN CHUYỂN ĐỘNG
* **Lý thuyết:**
  - Quy trình 3 bước: Bước 1 (Lập hệ PT: Chọn 2 ẩn + đk + đơn vị $\to$ Lập bảng đại lượng $\to$ Thiết lập 2 phương trình); Bước 2 (Giải hệ PT); Bước 3 (Đối chiếu điều kiện $\to$ Kết luận).
  - Công thức: $S = v \cdot t \implies v = \dfrac{S}{t}, t = \dfrac{S}{v}$.
  - Chuyển động đường thủy: $v_{xuôi} = v_{thực} + v_{nước}$; $v_{ngược} = v_{thực} - v_{nước}$.
* **Ví dụ mẫu 1 (Chuyển động đường bộ - ngược chiều & cùng chiều):**
  - Hai địa điểm $A$ và $B$ cách nhau $120\text{ km}$. Hai xe khởi hành cùng lúc đi ngược chiều thì gặp nhau sau $1{,}5$ giờ ($1$ giờ $30$ phút). Nếu đi cùng chiều thì xe đi nhanh hơn đuổi kịp xe đi chậm hơn sau $6$ giờ.
  - Hệ PT: $\begin{cases} 1{,}5(x + y) = 120 \\ 6(x - y) = 120 \end{cases} \iff \begin{cases} x + y = 80 \\ x - y = 20 \end{cases} \implies x = 50\text{ km/h}, y = 30\text{ km/h}$.
* **Bài tập tự luyện 1 (Đường bộ - 2 ô tô khởi hành khác thời điểm):**
  - Quãng đường $AB = 180\text{ km}$. Xe thứ nhất khởi hành từ $A$. Sau $30$ phút ($0{,}5$ giờ), xe thứ hai khởi hành từ $B$ đi ngược chiều. Hai xe gặp nhau sau khi xe thứ hai đi được $1{,}5$ giờ. Biết mỗi giờ xe thứ hai đi nhanh hơn xe thứ nhất $10\text{ km}$.
  - Hệ PT: $\begin{cases} 2x + 1{,}5y = 180 \\ y - x = 10 \end{cases} \implies x = 45\text{ km/h}, y = 55\text{ km/h}$.
* **Bài tập tự luyện 2 (Đường thủy - Canô xuôi dòng và ngược dòng):**
  - Một canô chạy trên khúc sông dài $90\text{ km}$. Thời gian xuôi dòng hết $3$ giờ, thời gian ngược dòng hết $4{,}5$ giờ ($4$ giờ $30$ phút). Tính vận tốc riêng của canô và vận tốc dòng nước.
  - Hệ PT: $\begin{cases} 3(x + y) = 90 \\ 4{,}5(x - y) = 90 \end{cases} \iff \begin{cases} x + y = 30 \\ x - y = 20 \end{cases} \implies x = 25\text{ km/h}, y = 5\text{ km/h}$.
* **Bài tập tự luyện 3 (Xe máy và ô tô cùng xuất phát từ A đến B):**
  - Hai xe cùng khởi hành từ $A$ đến $B$ dài $120\text{ km}$. Ô tô đi nhanh hơn xe máy $20\text{ km/h}$ nên đến $B$ trước xe máy $1$ giờ. (Lập hệ PT theo thời gian hoặc vận tốc).

---

### 🔹 TRANG 2: DẠNG 2: TOÁN NĂNG SUẤT & CÔNG VIỆC CHUNG - RIÊNG, VÒI NƯỚC
* **Lý thuyết:**
  - Quy ước: Toàn bộ công việc hoàn thành là $1$ (đơn vị công việc).
  - Khối lượng công việc = Năng suất trong 1 đơn vị thời gian $\times$ Thời gian làm.
  - Hai đối tượng cùng làm trong 1 giờ: $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{T_{chung}}$.
* **Ví dụ mẫu 2 (Hai tổ công nhân cùng làm một công việc):**
  - Hai tổ công nhân cùng làm chung một công việc thì hoàn thành trong $12$ giờ. Nếu tổ I làm trong $4$ giờ rồi tổ II làm tiếp trong $6$ giờ thì cả hai tổ hoàn thành được $40\%$ ($\dfrac{2}{5}$) công việc. Hỏi mỗi tổ làm một mình thì sau bao lâu hoàn thành công việc?
  - Hệ PT: $\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{12} \\[6pt] \dfrac{4}{x} + \dfrac{6}{y} = \dfrac{2}{5} \end{cases} \implies x = 20\text{ giờ}, y = 30\text{ giờ}$.
* **Bài tập tự luyện 4 (Hai vòi nước cùng chảy vào bể rỗng):**
  - Hai vòi nước cùng chảy vào một bể không có nước thì sau $6$ giờ đầy bể. Nếu mở vòi I chảy trong $2$ giờ rồi mở vòi II chảy trong $3$ giờ thì cả hai vòi chảy được $\dfrac{2}{5}$ bể nước. Hỏi nếu chảy riêng thì mỗi vòi chảy trong bao lâu đầy bể?
  - Hệ PT: $\begin{cases} \dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{6} \\[6pt] \dfrac{2}{x} + \dfrac{3}{y} = \dfrac{2}{5} \end{cases} \implies x = 10\text{ giờ}, y = 15\text{ giờ}$.
* **Bài tập tự luyện 5 (Kế hoạch sản xuất chi tiết máy theo ngày):**
  - Hai tổ theo kế hoạch phải làm $720$ sản phẩm. Thực tế tổ I làm vượt mức $15\%$, tổ II làm vượt mức $12\%$ nên cả hai tổ đã làm được $819$ sản phẩm. Tính số sản phẩm mỗi tổ phải làm theo kế hoạch.
  - Hệ PT: $\begin{cases} x + y = 720 \\ 0{,}15x + 0{,}12y = 99 \end{cases} \implies x = 420\text{ sản phẩm}, y = 300\text{ sản phẩm}$.
* **Bài tập tự luyện 6 (Đội xe chở hàng hỗ trợ đồng bào):**
  - Hai đội xe được giao vận chuyển $140$ tấn hàng cứu trợ. Đội I vận chuyển trong $3$ ngày, đội II trong $4$ ngày thì hoàn thành. Biết mỗi ngày đội I vận chuyển nhiều hơn đội II $5$ tấn. Tính năng suất mỗi ngày của từng đội.
  - Hệ PT: $\begin{cases} 3x + 4y = 140 \\ x - y = 5 \end{cases} \implies x = 20\text{ tấn/ngày}, y = 15\text{ tấn/ngày}$.

---

### 🔹 TRANG 3: DẠNG 3: TOÁN HÌNH HỌC THỰC TẾ & QUAN HỆ SỐ
* **Lý thuyết:**
  - Hình chữ nhật: Nửa chu vi $p = x + y$, diện tích ban đầu $S = xy$.
  - Khi thay đổi kích thước: Chiều dài mới $x \pm a$, chiều rộng mới $y \pm b$, diện tích mới $(x \pm a)(y \pm b)$.
  - Cấu tạo số có hai chữ số: $\overline{ab} = 10a + b$ ($a \in \{1, \dots, 9\}; b \in \{0, \dots, 9\}$). Khi đổi chỗ: $\overline{ba} = 10b + a$.
* **Ví dụ mẫu 3 (Mảnh đất hình chữ nhật thay đổi kích thước):**
  - Một mảnh vườn hình chữ nhật có chu vi $80\text{ m}$. Nếu tăng chiều rộng thêm $3\text{ m}$ và giảm chiều dài đi $2\text{ m}$ thì diện tích mảnh vườn tăng thêm $24\text{ m}^2$. Tính diện tích mảnh vườn lúc ban đầu.
  - Hệ PT: $\begin{cases} x + y = 40 \\ (x - 2)(y + 3) = xy + 24 \end{cases} \iff \begin{cases} x + y = 40 \\ 3x - 2y = 30 \end{cases} \implies x = 22\text{ m}, y = 18\text{ m} \implies S = 396\text{ m}^2$.
* **Bài tập tự luyện 7 (Thửa ruộng hình chữ nhật):**
  - Một thửa ruộng hình chữ nhật có chiều dài hơn chiều rộng $15\text{ m}$. Nếu giảm chiều dài $2\text{ m}$ và tăng chiều rộng $3\text{ m}$ thì diện tích thửa ruộng tăng thêm $44\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu.
  - Hệ PT: $\begin{cases} x - y = 15 \\ (x - 2)(y + 3) = xy + 44 \end{cases} \iff \begin{cases} x - y = 15 \\ 3x - 2y = 50 \end{cases} \implies x = 35\text{ m}, y = 20\text{ m}$.
* **Bài tập tự luyện 8 (Tìm số tự nhiên có hai chữ số):**
  - Tìm một số tự nhiên có hai chữ số biết chữ số hàng chục lớn hơn chữ số hàng đơn vị là $2$. Nếu viết thêm chữ số $0$ vào giữa hai chữ số thì được số mới có ba chữ số lớn hơn số ban đầu $540$ đơn vị, đồng thời tổng hai chữ số bằng $10$.
  - Hệ PT: $\begin{cases} x - y = 2 \\ x + y = 10 \end{cases} \implies x = 6, y = 4 \implies$ Số cần tìm là $64$.
* **Bài tập tự luyện 9 (Sân trường hình chữ nhật mở rộng):**
  - Một sân trường hình chữ nhật có chu vi $120\text{ m}$. Để phục vụ hoạt động thể thao, nhà trường mở rộng chiều dài thêm $5\text{ m}$ và chiều rộng thêm $3\text{ m}$ thì diện tích tăng thêm $245\text{ m}^2$. Tính kích thước ban đầu của sân trường.
  - Hệ PT: $\begin{cases} x + y = 60 \\ (x + 5)(y + 3) = xy + 245 \end{cases} \iff \begin{cases} x + y = 60 \\ 3x + 5y = 230 \end{cases} \implies x = 35\text{ m}, y = 25\text{ m}$.

---

### 🔹 TRANG 4: DẠNG 4: TOÁN PHẦN TRĂM, KINH TẾ, MUA SẮM & NÂNG CAO VÀO 10
* **Lý thuyết:**
  - Giá bán sau giảm giá $k\%$: Giá mới $= (1 - k\%) \times$ Giá niêm yết.
  - Pha chế dung dịch: Khối lượng chất tan $= m_{dung dịch} \times C\%$.
* **Ví dụ mẫu 4 (Mua sắm thực tế có chiết khấu theo tỉ lệ phần trăm):**
  - Bác An mua hai món hàng A và B có tổng giá niêm yết là $600\,000$ đồng. Nhân dịp ngày hội mua sắm, cửa hàng giảm giá món hàng A là $10\%$ và món hàng B là $20\%$, do đó bác An chỉ phải thanh toán tổng cộng $500\,000$ đồng. Hỏi giá niêm yết của mỗi món hàng là bao nhiêu?
  - Hệ PT: $\begin{cases} x + y = 600\,000 \\ 0{,}90x + 0{,}80y = 500\,000 \end{cases} \implies x = 200\,000\text{ đ}, y = 400\,000\text{ đ}$.
* **Bài tập tự luyện 10 (Mua vé xem phim & combo bắp nước):**
  - Một nhóm bạn học sinh mua vé xem phim và combo bắp nước. Lần 1 mua $4$ vé xem phim và $3$ combo bắp nước hết $380\,000$ đồng. Lần 2 mua thêm $2$ vé xem phim và $4$ combo bắp nước cùng loại hết $340\,000$ đồng. Tính giá tiền của $1$ vé xem phim và $1$ combo bắp nước.
  - Hệ PT: $\begin{cases} 4x + 3y = 380\,000 \\ 2x + 4y = 340\,000 \end{cases} \implies x = 50\,000\text{ đ}, y = 60\,000\text{ đ}$.
* **Bài tập tự luyện 11 (Pha chế dung dịch muối theo nồng độ phần trăm):**
  - Có hai loại dung dịch muối nồng độ $10\%$ và $15\%$. Cần trộn bao nhiêu gam dung dịch mỗi loại để được $500\text{ gam}$ dung dịch muối có nồng độ $12\%$?
  - Hệ PT: $\begin{cases} x + y = 500 \\ 0{,}10x + 0{,}15y = 0{,}12 \times 500 = 60 \end{cases} \implies x = 300\text{ gam}, y = 200\text{ gam}$.
* **Bài tập tự luyện 12 (Bài toán nâng cao thi tuyển sinh vào 10):**
  - Trong tháng đầu, hai tổ sản xuất làm được $800$ sản phẩm. Sang tháng thứ hai, tổ I làm vượt mức $15\%$, nhưng tổ II do thiếu nguyên liệu nên giảm $10\%$ so với tháng đầu, do đó cả hai tổ làm được tổng cộng $845$ sản phẩm. Tính số sản phẩm mỗi tổ làm được trong tháng đầu.
  - Hệ PT: $\begin{cases} x + y = 800 \\ 1{,}15x + 0{,}90y = 845 \end{cases} \iff \begin{cases} x + y = 800 \\ 0{,}15x - 0{,}10y = 45 \end{cases} \implies x = 500\text{ sp}, y = 300\text{ sp}$.
* **Khung tổng kết:**
  - 4 tiêu chí chấm điểm tự luận bài toán thực tế chuẩn kỳ thi Tuyển sinh vào 10 (Điểm tối đa $2{,}0$ hoặc $2{,}5$ điểm):
    1. Đặt ẩn phụ, đơn vị, điều kiện chuẩn xác ($0{,}25$đ).
    2. Biểu diễn các đại lượng chưa biết qua ẩn ($0{,}75$đ - $1{,}0$đ).
    3. Lập hệ PT và giải hệ PT chính xác ($0{,}75$đ).
    4. Đối chiếu điều kiện và viết câu trả lời kết luận ($0{,}25$đ).

---

## 🚀 IV. BƯỚC TIẾP THEO (SAU KHI THẦY DUYỆT)
1. Viết script Python `generate_chuyen_de_4_trang.py` để sinh mã nguồn LaTeX chuẩn mực.
2. Biên dịch bằng `pdflatex` và kiểm tra chính xác **4 trang PDF** không thừa không thiếu.
3. Tạo file `DAP_AN_VA_LOI_GIAI_CHI_TIET.md` đầy đủ bảng tóm tắt đại lượng và lời giải chi tiết cho cả 12 bài tập rèn luyện.

