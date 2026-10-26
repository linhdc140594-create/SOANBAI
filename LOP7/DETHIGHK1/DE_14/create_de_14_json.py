import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_14'

tikz_cau4 = r'''\begin{tikzpicture}[scale=0.75, line cap=round, line join=round]
    \coordinate (O) at (0,0);
    \coordinate (C) at (2.2,0);
    \coordinate (B) at (32:2.2);
    \coordinate (A) at (64:2.2);
    \draw[thick] (O) -- (C) node[right] {$C$};
    \draw[thick] (O) -- (B) node[above right] {$B$};
    \draw[thick] (O) -- (A) node[above] {$A$};
    \node[below left] at (O) {$O$};
    \draw[thick] (O) ++(0:0.45) arc (0:32:0.45);
    \node[font=\footnotesize] at (16:0.75) {$32^\circ$};
    \draw[thick] (O) ++(32:0.45) arc (32:64:0.45);
\end{tikzpicture}'''

tikz_cau6 = r'''\begin{tikzpicture}[scale=1.3, line cap=round, line join=round]
    \draw[thick, ->] (-0.3,0) -- (2.0,0) node[below] {$x$};
    \draw[thick] (0, 0.08) -- (0, -0.08) node[below=2pt] {$0$};
    \draw[thick] (1.5, 0.08) -- (1.5, -0.08) node[below=2pt] {$1$};
    \draw (0.5, 0.05) -- (0.5, -0.05);
    \draw (1.0, 0.05) -- (1.0, -0.05);
    \filldraw[red] (1.0, 0) circle (1.5pt) node[above=3pt, black] {$a$};
\end{tikzpicture}'''

tikz_cau10 = r'''\begin{tikzpicture}[scale=0.72, line cap=round, line join=round]
    \draw[thick] (-2, 1.8) node[left] {$A$} -- (2.5, 1.8) node[right] {$B$};
    \draw[thick] (-2, 0) node[left] {$C$} -- (2.5, 0) node[right] {$D$};
    \coordinate (E) at (-0.5, 1.8);
    \coordinate (F) at (0.5, 0);
    \draw[thick] ($(E)!-0.3!(F)$) -- ($(F)!-0.3!(E)$);
    \filldraw[black] (E) circle (1.2pt) node[above left] {$E$};
    \filldraw[black] (F) circle (1.2pt) node[below right] {$F$};
    % E1 = 120 (angle AEF)
    \draw[thick] (E) ++(180:0.4) arc (180:299.1:0.4);
    \node[font=\footnotesize] at ($(E)+(-0.6,-0.2)$) {$120^\circ$};
    \node[font=\footnotesize] at ($(E)+(-0.35,0.3)$) {$1$};
    % CFE = 60
    \draw[thick] (F) ++(180:0.4) arc (180:119.1:0.4);
    \node[font=\footnotesize] at ($(F)+(-0.6,0.3)$) {$60^\circ$};
\end{tikzpicture}'''

tikz_cau2_p2 = r'''\begin{tikzpicture}[scale=0.7, line cap=round, line join=round]
    % Lines m and n
    \draw[thick] (-2.2, 2.0) -- (2.8, 2.0) node[right] {$m$};
    \draw[thick] (-2.2, 0) -- (2.8, 0) node[right] {$n$};
    % Line d perpendicular at H and I
    \draw[thick] (-1.6, 2.5) -- (-1.6, -0.5) node[below] {$d$};
    \filldraw[black] (-1.6, 2.0) circle (1.2pt) node[above left] {$H$};
    \filldraw[black] (-1.6, 0) circle (1.2pt) node[below left] {$I$};
    \draw[thick] (-1.6, 2.0) ++(0,-0.18) -- ++(0.18,0) -- ++(0,0.18);
    \draw[thick] (-1.6, 0) ++(0,0.18) -- ++(0.18,0) -- ++(0,-0.18);
    % Line c slanted cutting m at A, n at B
    \draw[thick] (2.0, 2.9) node[above right] {$c$} -- (-0.8, -0.7);
    \filldraw[black] (1.1, 2.0) circle (1.2pt) node[above left] {$A$};
    \filldraw[black] (0.1, 0) circle (1.2pt) node[above left] {$B$};
    % Angle ABI = 80
    \draw[thick] (0.1, 0) ++(180:0.4) arc (180:63.4:0.4);
    \node[font=\footnotesize] at (-0.35, 0.45) {$80^\circ$};
\end{tikzpicture}'''

tikz_hop_cn = r'''\begin{tikzpicture}[scale=0.72, line cap=round, line join=round]
    \coordinate (A) at (0, 1.8);
    \coordinate (B) at (3.0, 1.8);
    \coordinate (C) at (4.0, 2.6);
    \coordinate (D) at (1.0, 2.6);
    \coordinate (A_prime) at (0, 0);
    \coordinate (B_prime) at (3.0, 0);
    \coordinate (C_prime) at (4.0, 0.8);
    \coordinate (D_prime) at (1.0, 0.8);

    \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
    \draw[thick] (A) -- (A_prime) -- (B_prime) -- (B);
    \draw[thick] (B_prime) -- (C_prime) -- (C);
    \draw[thick, dashed] (D) -- (D_prime) -- (A_prime);
    \draw[thick, dashed] (D_prime) -- (C_prime);

    \node[above left] at (A) {$A$};
    \node[above] at (B) {$B$};
    \node[above right] at (C) {$C$};
    \node[above] at (D) {$D$};
    \node[below left] at (A_prime) {$A'$};
    \node[below] at (B_prime) {$B'$};
    \node[right] at (C_prime) {$C'$};
    \node[left] at (D_prime) {$D'$};

    \node[below] at ($(A_prime)!0.5!(B_prime)$) {$4\text{ cm}$};
    \node[right] at ($(B_prime)!0.5!(C_prime)+(0.1,-0.1)$) {$2\text{ cm}$};
    \node[right] at ($(B)!0.5!(B_prime)$) {$3\text{ cm}$};
\end{tikzpicture}'''

de_data = {
    "de_so": 14,
    "tieu_de": "ĐỀ SỐ 14",
    "phan_I_trac_nghiem": [
        {
            "cau": 1,
            "noi_dung": r"Phát biểu nào sau đây là đúng?",
            "lua_chon": {
                "A": r"$\sqrt{2} \in \mathbb{Q}$",
                "B": r"$-5 \notin \mathbb{Q}$",
                "C": r"$-\dfrac{5}{4} \notin \mathbb{Q}$",
                "D": r"$\dfrac{3}{2} \in \mathbb{Q}$"
            },
            "dap_an": "D",
            "loi_giai": r"Ta có $\dfrac{3}{2}$ là phân số có tử và mẫu là các số nguyên ($2 \neq 0$) nên $\dfrac{3}{2} \in \mathbb{Q}$."
        },
        {
            "cau": 2,
            "noi_dung": r"Số giá trị nguyên của $x$ thỏa mãn $-\dfrac{2}{3} < \dfrac{x}{12} < -\dfrac{1}{4}$ là:",
            "lua_chon": {
                "A": r"$3$",
                "B": r"$2$",
                "C": r"$5$",
                "D": r"$4$"
            },
            "dap_an": "D",
            "loi_giai": r"Quy đồng mẫu số chung 12: $-\dfrac{8}{12} < \dfrac{x}{12} < -\dfrac{3}{12} \iff -8 < x < -3$. Do $x \in \mathbb{Z}$ nên $x \in \{-7; -6; -5; -4\}$. Có 4 giá trị thỏa mãn."
        },
        {
            "cau": 3,
            "noi_dung": r"Số $9$ có căn bậc hai số học là:",
            "lua_chon": {
                "A": r"$3$ và $-3$",
                "B": r"$3$",
                "C": r"$-3$",
                "D": r"$18$"
            },
            "dap_an": "B",
            "loi_giai": r"Căn bậc hai số học của một số không âm $a$ là $\sqrt{a} \ge 0$. Do đó căn bậc hai số học của $9$ là $\sqrt{9} = 3$."
        },
        {
            "cau": 4,
            "noi_dung": r"Cho hình vẽ bên, biết $OB$ là tia phân giác của $\widehat{AOC}$. Khi đó số đo của $\widehat{AOB}$ là:",
            "hinh_tikz": tikz_cau4,
            "lua_chon": {
                "A": r"$65^\circ$",
                "B": r"$32^\circ$",
                "C": r"$130^\circ$",
                "D": r"$18^\circ$"
            },
            "dap_an": "B",
            "loi_giai": r"Do $OB$ là tia phân giác của $\widehat{AOC}$ nên $\widehat{AOB} = \widehat{BOC} = 32^\circ$."
        },
        {
            "cau": 5,
            "noi_dung": r"Kết quả của phép tính $\left(-\dfrac{1}{3}\right)^{2024} : \left(-\dfrac{1}{3}\right)^{2022}$ là:",
            "lua_chon": {
                "A": r"$\dfrac{1}{3}$",
                "B": r"$-\dfrac{1}{9}$",
                "C": r"$\dfrac{1}{9}$",
                "D": r"$-\dfrac{2}{3}$"
            },
            "dap_an": "C",
            "loi_giai": r"Áp dụng quy tắc chia hai lũy thừa cùng cơ số: $\left(-\dfrac{1}{3}\right)^{2024 - 2022} = \left(-\dfrac{1}{3}\right)^2 = \dfrac{1}{9}$."
        },
        {
            "cau": 6,
            "noi_dung": r"Quan sát trục số bên dưới và chọn đáp án đúng về giá trị của điểm $a$:",
            "hinh_tikz": tikz_cau6,
            "lua_chon": {
                "A": r"$a = \dfrac{1}{3}$",
                "B": r"$a = \dfrac{1}{2}$",
                "C": r"$a = \dfrac{2}{5}$",
                "D": r"$a = \dfrac{2}{3}$"
            },
            "dap_an": "D",
            "loi_giai": r"Đoạn đơn vị từ $0$ đến $1$ được chia thành 3 phần bằng nhau. Điểm $a$ ở vạch chia thứ 2 theo chiều dương tính từ $0$, do đó $a = \dfrac{2}{3}$."
        },
        {
            "cau": 7,
            "noi_dung": r"Trong các số $\dfrac{9}{7}; 0{,}2; 0; -\dfrac{13}{5}; \dfrac{3}{15}; -\dfrac{2}{5}; -\dfrac{8}{5}$, có bao nhiêu số hữu tỉ dương?",
            "lua_chon": {
                "A": r"$1$",
                "B": r"$3$",
                "C": r"$2$",
                "D": r"$4$"
            },
            "dap_an": "B",
            "loi_giai": r"Các số hữu tỉ dương gồm có: $\dfrac{9}{7}; 0{,}2; \dfrac{3}{15}$ (tổng cộng 3 số)."
        },
        {
            "cau": 8,
            "noi_dung": r"Cho $\widehat{xOy} = 80^\circ$. Góc đối đỉnh với $\widehat{xOy}$ có số đo độ là:",
            "lua_chon": {
                "A": r"$50^\circ$",
                "B": r"$80^\circ$",
                "C": r"$100^\circ$",
                "D": r"$120^\circ$"
            },
            "dap_an": "B",
            "loi_giai": r"Hai góc đối đỉnh thì bằng nhau nên góc đối đỉnh với $\widehat{xOy}$ cũng có số đo bằng $80^\circ$."
        },
        {
            "cau": 9,
            "noi_dung": r"Các mặt của hình lập phương đều là:",
            "lua_chon": {
                "A": "Hình vuông.",
                "B": "Tam giác đều.",
                "C": "Hình chữ nhật.",
                "D": "Hình thoi."
            },
            "dap_an": "A",
            "loi_giai": r"Hình lập phương có 6 mặt đều là các hình vuông bằng nhau."
        },
        {
            "cau": 10,
            "noi_dung": r"Cho hình vẽ bên, biết $\widehat{CFE} = 60^\circ, \widehat{E}_1 = 120^\circ$. Xét hai khẳng định: (I) $\widehat{BEF} = 60^\circ$; (II) $AB \parallel CD$. Khẳng định nào sau đây là đúng?",
            "hinh_tikz": tikz_cau10,
            "lua_chon": {
                "A": "Chỉ (I) đúng.",
                "B": "Chỉ (II) đúng.",
                "C": "Cả (I) và (II) đều đúng.",
                "D": "Cả (I) và (II) đều sai."
            },
            "dap_an": "C",
            "loi_giai": r"Vì $\widehat{BEF}$ và $\widehat{E}_1$ là hai góc kề bù nên $\widehat{BEF} = 180^\circ - 120^\circ = 60^\circ$ (khẳng định I đúng). Mặt khác, $\widehat{CFE} = \widehat{BEF} = 60^\circ$ là hai góc so le trong bằng nhau nên $AB \parallel CD$ (khẳng định II đúng)."
        },
        {
            "cau": 11,
            "noi_dung": r"Hai đường thẳng $xx'$ và $yy'$ cắt nhau tại $O$. Góc đối đỉnh với $\widehat{x'Oy}$ là:",
            "lua_chon": {
                "A": r"$\widehat{xOy'}$",
                "B": r"$\widehat{x'Oy}$",
                "C": r"$\widehat{x'Oy'}$",
                "D": r"$\widehat{xOy}$"
            },
            "dap_an": "A",
            "loi_giai": r"Tia đối của $Ox'$ là $Ox$, của $Oy$ là $Oy'$. Vậy góc đối đỉnh với $\widehat{x'Oy}$ là $\widehat{xOy'}$."
        },
        {
            "cau": 12,
            "noi_dung": r"Cho ba đường thẳng phân biệt $a, b, c$ biết $a \parallel c$ và $b \parallel c$. Kết luận nào sau đây là đúng?",
            "lua_chon": {
                "A": r"$a$ cắt $b$",
                "B": r"$a \parallel b$",
                "C": r"$a \perp b$",
                "D": r"$a$ trùng $b$"
            },
            "dap_an": "B",
            "loi_giai": r"Hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì chúng song song với nhau ($a \parallel b$)."
        }
    ],
    "phan_II_dung_sai": [
        {
            "cau": 1,
            "noi_dung": r"Cho biểu thức $P = \dfrac{3}{5} \cdot \left(-\dfrac{5}{6}\right) + \left(-\dfrac{1}{2}\right)^2 - \left|-\dfrac{3}{4}\right|$. Xét tính đúng sai của các mệnh đề sau:",
            "menh_de": [
                {
                    "y": "a",
                    "noi_dung": r"Giá trị của phép nhân $\dfrac{3}{5} \cdot \left(-\dfrac{5}{6}\right)$ bằng $-\dfrac{1}{2}$.",
                    "dap_an": "Đúng",
                    "loi_giai": r"Ta có $\dfrac{3}{5} \cdot \left(-\dfrac{5}{6}\right) = -\dfrac{3 \cdot 5}{5 \cdot 6} = -\dfrac{3}{6} = -\dfrac{1}{2}$."
                },
                {
                    "y": "b",
                    "noi_dung": r"Giá trị của lũy thừa $\left(-\dfrac{1}{2}\right)^2$ bằng $-\dfrac{1}{4}$.",
                    "dap_an": "Sai",
                    "loi_giai": r"Ta có $\left(-\dfrac{1}{2}\right)^2 = \dfrac{(-1)^2}{2^2} = \dfrac{1}{4} \neq -\dfrac{1}{4}$."
                },
                {
                    "y": "c",
                    "noi_dung": r"Giá trị tuyệt đối $\left|-\dfrac{3}{4}\right|$ bằng $\dfrac{3}{4}$.",
                    "dap_an": "Đúng",
                    "loi_giai": r"Giá trị tuyệt đối của một số luôn không âm nên $\left|-\dfrac{3}{4}\right| = \dfrac{3}{4}$."
                },
                {
                    "y": "d",
                    "noi_dung": r"Giá trị của biểu thức $P$ bằng $-1$.",
                    "dap_an": "Đúng",
                    "loi_giai": r"Thay các giá trị vào biểu thức: $P = -\dfrac{1}{2} + \dfrac{1}{4} - \dfrac{3}{4} = -\dfrac{2}{4} + \dfrac{1}{4} - \dfrac{3}{4} = -\dfrac{4}{4} = -1$."
                }
            ]
        },
        {
            "cau": 2,
            "noi_dung": r"Quan sát hình vẽ bên, biết đường thẳng $d \perp m$ tại $H$, $d \perp n$ tại $I$; đường thẳng $c$ cắt $m$ tại $A$ và cắt $n$ tại $B$ sao cho $\widehat{ABI} = 80^\circ$. Xét tính đúng sai của các mệnh đề sau:",
            "hinh_tikz": tikz_cau2_p2,
            "menh_de": [
                {
                    "y": "a",
                    "noi_dung": r"Hai đường thẳng $m$ và $n$ song song với nhau ($m \parallel n$).",
                    "dap_an": "Đúng",
                    "loi_giai": r"Vì $m \perp d$ và $n \perp d$ nên $m \parallel n$."
                },
                {
                    "y": "b",
                    "noi_dung": r"Góc so le trong với góc $\widehat{ABI}$ tại đỉnh $A$ có số đo bằng $80^\circ$.",
                    "dap_an": "Đúng",
                    "loi_giai": r"Vì $m \parallel n$ nên góc so le trong với $\widehat{ABI}$ tại đỉnh $A$ bằng $\widehat{ABI} = 80^\circ$."
                },
                {
                    "y": "c",
                    "noi_dung": r"Góc trong cùng phía với góc $\widehat{ABI}$ tại đỉnh $A$ có số đo bằng $80^\circ$.",
                    "dap_an": "Sai",
                    "loi_giai": r"Hai góc trong cùng phía bù nhau, do đó góc trong cùng phía với $\widehat{ABI}$ có số đo bằng $180^\circ - 80^\circ = 100^\circ$ chứ không phải $80^\circ$."
                },
                {
                    "y": "d",
                    "noi_dung": r"Số đo góc $\widehat{AHI}$ bằng $90^\circ$.",
                    "dap_an": "Đúng",
                    "loi_giai": r"Vì $d \perp m$ tại $H$ nên $\widehat{AHI} = 90^\circ$."
                }
            ]
        }
    ],
    "phan_III_tra_loi_ngan": [
        {
            "cau": 1,
            "noi_dung": r"Tìm số hữu tỉ $x$, biết: $3 \cdot \left(x - \dfrac{1}{4}\right) + \dfrac{1}{2} = \dfrac{1}{3}$.",
            "dap_an": "\\dfrac{7}{36}",
            "loi_giai": r"Ta có: $3 \cdot \left(x - \dfrac{1}{4}\right) = \dfrac{1}{3} - \dfrac{1}{2} = -\dfrac{1}{6} \iff x - \dfrac{1}{4} = -\dfrac{1}{6} : 3 = -\dfrac{1}{18} \iff x = -\dfrac{1}{18} + \dfrac{1}{4} = \dfrac{-2 + 9}{36} = \dfrac{7}{36}$."
        },
        {
            "cau": 2,
            "noi_dung": r"Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ như hình vẽ có chiều dài $D'C' = 4\text{ cm}$, chiều rộng $B'C' = 2\text{ cm}$ và chiều cao $BB' = 3\text{ cm}$. Tính thể tích của hình hộp chữ nhật này.",
            "hinh_tikz": tikz_hop_cn,
            "dap_an": "24\\text{ cm}^3",
            "loi_giai": r"Thể tích của hình hộp chữ nhật là: $V = a \cdot b \cdot c = 4 \cdot 2 \cdot 3 = 24\text{ cm}^3$."
        }
    ],
    "phan_IV_tu_luan": [
        {
            "cau": 1,
            "noi_dung": r"Tính giá trị các biểu thức sau (tính bằng cách hợp lý nếu có thể):",
            "cac_y": [
                {
                    "y": "a",
                    "cau_hoi": r"$A = \dfrac{2}{7} + \left(-\dfrac{3}{7}\right) : \dfrac{3}{2}$",
                    "loi_giai": r"$A = \dfrac{2}{7} + \left(-\dfrac{3}{7}\right) \cdot \dfrac{2}{3} = \dfrac{2}{7} + \left(-\dfrac{2}{7}\right) = 0$."
                },
                {
                    "y": "b",
                    "cau_hoi": r"$B = \dfrac{5}{17} \cdot \left(-\dfrac{31}{33}\right) + \dfrac{5}{17} \cdot \left(-\dfrac{2}{33}\right) + 2\dfrac{5}{17}$",
                    "loi_giai": r"$B = \dfrac{5}{17} \cdot \left(-\dfrac{31}{33} - \dfrac{2}{33}\right) + 2 + \dfrac{5}{17} = \dfrac{5}{17} \cdot (-1) + \dfrac{5}{17} + 2 = -\dfrac{5}{17} + \dfrac{5}{17} + 2 = 2$."
                },
                {
                    "y": "c",
                    "cau_hoi": r"$C = \sqrt{4} + \sqrt{9} + \sqrt{16} + \sqrt{25}$",
                    "loi_giai": r"$C = 2 + 3 + 4 + 5 = 14$."
                },
                {
                    "y": "d",
                    "cau_hoi": r"$D = 0{,}(5) - 1\dfrac{1}{3} - 0{,}(7)$",
                    "loi_giai": r"Đổi sang phân số: $0{,}(5) = \dfrac{5}{9}; 0{,}(7) = \dfrac{7}{9}; 1\dfrac{1}{3} = \dfrac{4}{3} = \dfrac{12}{9}$. Khi đó: $D = \dfrac{5}{9} - \dfrac{12}{9} - \dfrac{7}{9} = \dfrac{5 - 12 - 7}{9} = -\dfrac{14}{9}$."
                }
            ]
        },
        {
            "cau": 2,
            "noi_dung": r"Tìm $x$, biết:",
            "cac_y": [
                {
                    "y": "a",
                    "cau_hoi": r"$2x - \dfrac{1}{3} = \dfrac{5}{6}$",
                    "loi_giai": r"$2x = \dfrac{5}{6} + \dfrac{1}{3} = \dfrac{5}{6} + \dfrac{2}{6} = \dfrac{7}{6} \iff x = \dfrac{7}{6} : 2 = \dfrac{7}{12}$. Vậy $x = \dfrac{7}{12}$."
                },
                {
                    "y": "b",
                    "cau_hoi": r"$\left(x - \dfrac{1}{2}\right)^2 = \dfrac{9}{25}$",
                    "loi_giai": (
                        r"Vì $\left(\dfrac{3}{5}\right)^2 = \dfrac{9}{25}$ và $\left(-\dfrac{3}{5}\right)^2 = \dfrac{9}{25}$, ta xét hai trường hợp:\par "
                        r"$\bullet$ TH1: $x - \dfrac{1}{2} = \dfrac{3}{5} \iff x = \dfrac{3}{5} + \dfrac{1}{2} = \dfrac{6 + 5}{10} = \dfrac{11}{10}$.\par "
                        r"$\bullet$ TH2: $x - \dfrac{1}{2} = -\dfrac{3}{5} \iff x = -\dfrac{3}{5} + \dfrac{1}{2} = \dfrac{-6 + 5}{10} = -\dfrac{1}{10}$.\par "
                        r"Vậy $x = \dfrac{11}{10}$ hoặc $x = -\dfrac{1}{10}$."
                    )
                }
            ]
        },
        {
            "cau": 3,
            "noi_dung": r"Bể cá của quán cà phê Koi có dạng hình hộp chữ nhật có chiều dài $1{,}8\text{ m}$, chiều rộng $1{,}2\text{ m}$ và chiều cao $1{,}5\text{ m}$.",
            "cac_y": [
                {
                    "y": "a",
                    "cau_hoi": r"Tính diện tích xung quanh của bể cá.",
                    "loi_giai": r"Diện tích xung quanh của bể cá là: $S_{xq} = 2 \cdot (1{,}8 + 1{,}2) \cdot 1{,}5 = 2 \cdot 3 \cdot 1{,}5 = 9\text{ m}^2$."
                },
                {
                    "y": "b",
                    "cau_hoi": r"Chủ quán đã đổ nước vào bể sao cho mực nước cách miệng bể $20\text{ cm}$. Hỏi chủ quán đã đổ vào bể bao nhiêu lít nước? (biết rằng ban đầu bể không có nước).",
                    "loi_giai": (
                        r"Đổi $20\text{ cm} = 0{,}2\text{ m}$.\par "
                        r"Chiều cao mực nước trong bể là: $h = 1{,}5 - 0{,}2 = 1{,}3\text{ m}$.\par "
                        r"Thể tích nước đã đổ vào bể là: $V = 1{,}8 \cdot 1{,}2 \cdot 1{,}3 = 2{,}808\text{ m}^3$.\par "
                        r"Đổi $2{,}808\text{ m}^3 = 2808\text{ dm}^3 = 2808\text{ lít}$.\par "
                        r"Vậy chủ quán đã đổ vào bể $2808$ lít nước."
                    )
                }
            ]
        },
        {
            "cau": 4,
            "noi_dung": r"Cho hai biểu thức sau: $A = \dfrac{25^{800} \cdot 16^{60} \cdot 3^{2500}}{8^{80} \cdot 27^{60} \cdot 5^{1600}}$ và $B = 3^{2025}$. Hãy so sánh $A$ và $B$.",
            "loi_giai": (
                r"Ta có: $A = \dfrac{(5^2)^{800} \cdot (2^4)^{60} \cdot 3^{2500}}{(2^3)^{80} \cdot (3^3)^{60} \cdot 5^{1600}} = \dfrac{5^{1600} \cdot 2^{240} \cdot 3^{2500}}{2^{240} \cdot 3^{180} \cdot 5^{1600}}$.\par "
                r"Rút gọn cả tử và mẫu cho $5^{1600}$ và $2^{240}$:\par "
                r"\centerline{$A = \dfrac{3^{2500}}{3^{180}} = 3^{2500 - 180} = 3^{2320}$.}\par "
                r"Vì $2320 > 2025$ nên $3^{2320} > 3^{2025} \implies A > B$."
            )
        }
    ]
}

with open(os.path.join(work_dir, 'de_14.json'), 'w', encoding='utf-8') as f:
    json.dump(de_data, f, ensure_ascii=False, indent=2)

print("Created de_14.json successfully!")
