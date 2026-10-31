# -*- coding: utf-8 -*-
"""
Script sinh Phiếu bài tập cuối tuần Toán 5 - TUAN_13 với 7 Mã đề (501 -> 507).
Chủ đề: Hình tam giác -- Diện tích hình tam giác -- Hình thang -- Diện tích hình thang
Bài 4 và Bài 5: Chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
"""

import os
import sys
import json
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = 13
WEEK_TITLE = 'Hình tam giác -- Diện tích hình tam giác -- Hình thang -- Diện tích hình thang'

TOPICS = [
    'Nhận biết các yếu tố và loại hình tam giác',
    'Xác định đáy và chiều cao tương ứng của tam giác',
    'Công thức tính diện tích hình tam giác',
    'Tính diện tích tam giác có đáy và chiều cao cho trước',
    'Tính diện tích tam giác vuông khi biết hai cạnh góc vuông',
    'Tính độ dài đáy hoặc chiều cao tam giác khi biết diện tích',
    'Đặc điểm hình thang và các yếu tố hình thang',
    'Công thức tính diện tích hình thang',
    'Tính diện tích hình thang khi biết hai đáy và chiều cao',
    'Tính chiều cao hình thang khi biết diện tích và tổng hai đáy',
    'Mối quan hệ diện tích tam giác khi thay đổi đáy',
    'Bài toán thực tế tính diện tích thửa ruộng hình thang'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Một hình tam giác có bao nhiêu đỉnh, bao nhiêu cạnh và bao nhiêu góc:', '$3$ đỉnh, $3$ cạnh, $3$ góc', '$4$ đỉnh, $4$ cạnh, $4$ góc', '$3$ đỉnh, $4$ cạnh, $3$ góc', '$3$ đỉnh, $3$ cạnh, $4$ góc', 'A'),
        'c2': ('Trong hình tam giác vuông, hai cạnh góc vuông chính là:', 'Hai đường chéo', 'Đáy và chiều cao tương ứng', 'Hai cạnh đáy', 'Hai cạnh huyền', 'B'),
        'c3': ('Công thức tính diện tích hình tam giác có độ dài đáy $a$ và chiều cao $h$ là:', '$S = (a \\times h) : 2$', '$S = a \\times h$', '$S = (a + h) : 2$', '$S = (a + h) \\times 2$', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $12\,\text{cm}$ và chiều cao $8\,\text{cm}$ là:', r'$96\,\text{cm}^2$', r'$48\,\text{cm}^2$', r'$24\,\text{cm}^2$', r'$40\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có độ dài hai cạnh góc vuông là $6\,\text{cm}$ và $8\,\text{cm}$ là:', r'$48\,\text{cm}^2$', r'$14\,\text{cm}^2$', r'$24\,\text{cm}^2$', r'$28\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $30\,\text{cm}^2$, chiều cao $6\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$10\,\text{cm}$', r'$5\,\text{cm}$', r'$15\,\text{cm}$', r'$8\,\text{cm}$', 'A'),
        'c7': ('Hình thang là hình tứ giác có:', 'Hai cặp cạnh đối diện song song', 'Một cặp cạnh đối diện song song', 'Bốn góc vuông', 'Bốn cạnh bằng nhau', 'B'),
        'c8': ('Công thức tính diện tích hình thang có hai đáy $a, b$ và chiều cao $h$ là:', '$S = (a + b) \\times h$', '$S = (a \\times b) \\times h : 2$', '$S = (a + b) \\times h : 2$', '$S = a \\times b : 2$', 'C'),
        'c9': (r'Một hình thang có đáy lớn $15\,\text{cm}$, đáy bé $9\,\text{cm}$, chiều cao $8\,\text{cm}$. Diện tích hình thang đó là:', r'$96\,\text{cm}^2$', r'$192\,\text{cm}^2$', r'$90\,\text{cm}^2$', r'$108\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $60\,\text{cm}^2$, tổng độ dài hai đáy là $20\,\text{cm}$. Chiều cao hình thang là:', r'$3\,\text{cm}$', r'$6\,\text{cm}$', r'$12\,\text{cm}$', r'$8\,\text{cm}$', 'B'),
        'c11': (r'Một thửa ruộng hình thang có đáy lớn $40\,\text{m}$, đáy bé $25\,\text{m}$, chiều cao $20\,\text{m}$. Diện tích thửa ruộng đó là:', r'$650\,\text{m}^2$', r'$1\\,300\,\text{m}^2$', r'$600\,\text{m}^2$', r'$700\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $15\,\text{cm}$. Kéo dài đáy thêm $4\,\text{cm}$ thì diện tích tăng thêm $18\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$60\,\text{cm}^2$', r'$67{,}5\,\text{cm}^2$', r'$72\,\text{cm}^2$', r'$54\,\text{cm}^2$', 'B'),
        'b1': ('$45{,}8 + 27{,}65$', '$84{,}3 - 39{,}48$', '$18{,}5 \\times 4{,}2$', '$91{,}8 : 5{,}4$'),
        'b1_ans': ('73{,}45', '44{,}82', '77{,}7', '17'),
        'b2': [('x + 18{,}5 = 45{,}2', 'x = 45{,}2 - 18{,}5', 'x = 26{,}7'),
               ('x - 24{,}6 = 38{,}8', 'x = 38{,}8 + 24{,}6', 'x = 63{,}4'),
               ('x \\times 4{,}5 = 38{,}25', 'x = 38{,}25 : 4{,}5', 'x = 8{,}5'),
               ('x : 3{,}6 = 12{,}5', 'x = 12{,}5 \\times 3{,}6', 'x = 45')],
        'b3': [(r'S_{\Delta} = (16 \times 10) : 2', r'\text{cm}^2', '80'),
               (r'S_{\Delta\text{ vuông}} = (12 \times 9) : 2', r'\text{cm}^2', '54'),
               (r'S_{\text{thang}} = (18 + 12) \times 8 : 2', r'\text{cm}^2', '120'),
               (r'S_{\text{thang}} = 25 \times 10 : 2', r'\text{m}^2', '125')]
    },
    {
        'code': '502',
        'c1': ('Tam giác có một góc vuông được gọi là:', 'Tam giác vuông', 'Tam giác nhọn', 'Tam giác tù', 'Tam giác đều', 'A'),
        'c2': ('Đoạn thẳng vuông góc kẻ từ đỉnh của tam giác xuống cạnh đáy đối diện gọi là:', 'Cạnh bên', 'Chiều cao', 'Đường chéo', 'Trung điểm', 'B'),
        'c3': ('Muốn tính diện tích hình tam giác, ta lấy độ dài đáy nhân với chiều cao (cùng đơn vị đo) rồi:', 'Chia cho 2', 'Nhân với 2', 'Chia cho 4', 'Giữ nguyên', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $14\,\text{cm}$ và chiều cao $9\,\text{cm}$ là:', r'$126\,\text{cm}^2$', r'$63\,\text{cm}^2$', r'$46\,\text{cm}^2$', r'$32\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có hai cạnh góc vuông là $8\,\text{cm}$ và $10\,\text{cm}$ là:', r'$80\,\text{cm}^2$', r'$18\,\text{cm}^2$', r'$40\,\text{cm}^2$', r'$45\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $45\,\text{cm}^2$, chiều cao $9\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$10\,\text{cm}$', r'$5\,\text{cm}$', r'$15\,\text{cm}$', r'$8\,\text{cm}$', 'A'),
        'c7': ('Hình thang có một cạnh bên vuông góc với hai đáy gọi là:', 'Hình thang cân', 'Hình thang vuông', 'Hình bình hành', 'Hình thoi', 'B'),
        'c8': ('Muốn tính diện tích hình thang ta lấy tổng độ dài hai đáy nhân với chiều cao (cùng đơn vị đo) rồi:', 'Nhân với 2', 'Chia cho 4', 'Chia cho 2', 'Giữ nguyên', 'C'),
        'c9': (r'Một hình thang có đáy lớn $18\,\text{cm}$, đáy bé $12\,\text{cm}$, chiều cao $10\,\text{cm}$. Diện tích hình thang đó là:', r'$150\,\text{cm}^2$', r'$300\,\text{cm}^2$', r'$140\,\text{cm}^2$', r'$160\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $84\,\text{cm}^2$, tổng độ dài hai đáy là $24\,\text{cm}$. Chiều cao hình thang là:', r'$3{,}5\,\text{cm}$', r'$7\,\text{cm}$', r'$14\,\text{cm}$', r'$8\,\text{cm}$', 'B'),
        'c11': (r'Một mảnh đất hình thang có đáy lớn $35\,\text{m}$, đáy bé $25\,\text{m}$, chiều cao $16\,\text{m}$. Diện tích mảnh đất đó là:', r'$480\,\text{m}^2$', r'$960\,\text{m}^2$', r'$450\,\text{m}^2$', r'$500\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $20\,\text{cm}$. Kéo dài đáy thêm $5\,\text{cm}$ thì diện tích tăng thêm $30\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$100\,\text{cm}^2$', r'$120\,\text{cm}^2$', r'$150\,\text{cm}^2$', r'$90\,\text{cm}^2$', 'B'),
        'b1': ('$54{,}6 + 32{,}75$', '$92{,}4 - 47{,}65$', '$24{,}5 \\times 3{,}6$', '$98{,}8 : 5{,}2$'),
        'b1_ans': ('87{,}35', '44{,}75', '88{,}2', '19'),
        'b2': [('x + 23{,}4 = 56{,}8', 'x = 56{,}8 - 23{,}4', 'x = 33{,}4'),
               ('x - 31{,}5 = 42{,}7', 'x = 42{,}7 + 31{,}5', 'x = 74{,}2'),
               ('x \\times 5{,}2 = 44{,}2', 'x = 44{,}2 : 5{,}2', 'x = 8{,}5'),
               ('x : 4{,}5 = 14', 'x = 14 \\times 4{,}5', 'x = 63')],
        'b3': [(r'S_{\Delta} = (18 \times 12) : 2', r'\text{cm}^2', '108'),
               (r'S_{\Delta\text{ vuông}} = (14 \times 8) : 2', r'\text{cm}^2', '56'),
               (r'S_{\text{thang}} = (22 + 14) \times 10 : 2', r'\text{cm}^2', '180'),
               (r'S_{\text{thang}} = 30 \times 12 : 2', r'\text{m}^2', '180')]
    },
    {
        'code': '503',
        'c1': ('Tam giác có ba góc đều nhọn gọi là:', 'Tam giác nhọn', 'Tam giác vuông', 'Tam giác tù', 'Tam giác cân', 'A'),
        'c2': ('Khoảng cách vuông góc giữa hai đáy của hình thang gọi là:', 'Cạnh đáy', 'Chiều cao', 'Đường chéo', 'Cạnh bên', 'B'),
        'c3': ('Muốn tính diện tích tam giác ta lấy đáy nhân với chiều cao rồi:', 'Chia cho 2', 'Nhân với 2', 'Cộng với 2', 'Trừ đi 2', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $16\,\text{cm}$ và chiều cao $7\,\text{cm}$ là:', r'$112\,\text{cm}^2$', r'$56\,\text{cm}^2$', r'$48\,\text{cm}^2$', r'$36\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có hai cạnh góc vuông là $12\,\text{cm}$ và $5\,\text{cm}$ là:', r'$60\,\text{cm}^2$', r'$17\,\text{cm}^2$', r'$30\,\text{cm}^2$', r'$35\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $48\,\text{cm}^2$, chiều cao $8\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$12\,\text{cm}$', r'$6\,\text{cm}$', r'$18\,\text{cm}$', r'$10\,\text{cm}$', 'A'),
        'c7': ('Hai cạnh song song của hình thang được gọi là:', 'Hai cạnh bên', 'Hai cạnh đáy', 'Hai đường cao', 'Hai đường chéo', 'B'),
        'c8': ('Diện tích hình thang có đáy lớn $a$, đáy bé $b$, chiều cao $h$ tính bởi:', '$S = (a + b) \\times h$', '$S = (a - b) \\times h : 2$', '$S = (a + b) \\times h : 2$', '$S = a \\times b : 2$', 'C'),
        'c9': (r'Một hình thang có đáy lớn $20\,\text{cm}$, đáy bé $14\,\text{cm}$, chiều cao $8\,\text{cm}$. Diện tích hình thang đó là:', r'$136\,\text{cm}^2$', r'$272\,\text{cm}^2$', r'$140\,\text{cm}^2$', r'$130\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $75\,\text{cm}^2$, tổng độ dài hai đáy là $25\,\text{cm}$. Chiều cao hình thang là:', r'$3\,\text{cm}$', r'$6\,\text{cm}$', r'$12\,\text{cm}$', r'$8\,\text{cm}$', 'B'),
        'c11': (r'Một thửa ruộng hình thang có đáy lớn $50\,\text{m}$, đáy bé $30\,\text{m}$, chiều cao $24\,\text{m}$. Diện tích thửa ruộng đó là:', r'$960\,\text{m}^2$', r'$1\\,920\,\text{m}^2$', r'$900\,\text{m}^2$', r'$1\\,000\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $18\,\text{cm}$. Kéo dài đáy thêm $6\,\text{cm}$ thì diện tích tăng thêm $27\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$75\,\text{cm}^2$', r'$81\,\text{cm}^2$', r'$90\,\text{cm}^2$', r'$72\,\text{cm}^2$', 'B'),
        'b1': ('$62{,}8 + 35{,}45$', '$85{,}6 - 48{,}35$', '$26{,}5 \\times 4{,}2$', '$85{,}8 : 3{,}9$'),
        'b1_ans': ('98{,}25', '37{,}25', '111{,}3', '22'),
        'b2': [('x + 27{,}5 = 64{,}2', 'x = 64{,}2 - 27{,}5', 'x = 36{,}7'),
               ('x - 36{,}8 = 45{,}4', 'x = 45{,}4 + 36{,}8', 'x = 82{,}2'),
               ('x \\times 6{,}5 = 55{,}25', 'x = 55{,}25 : 6{,}5', 'x = 8{,}5'),
               ('x : 5{,}2 = 15', 'x = 15 \\times 5{,}2', 'x = 78')],
        'b3': [(r'S_{\Delta} = (20 \times 14) : 2', r'\text{cm}^2', '140'),
               (r'S_{\Delta\text{ vuông}} = (16 \times 9) : 2', r'\text{cm}^2', '72'),
               (r'S_{\text{thang}} = (24 + 16) \times 12 : 2', r'\text{cm}^2', '240'),
               (r'S_{\text{thang}} = 35 \times 14 : 2', r'\text{m}^2', '245')]
    },
    {
        'code': '504',
        'c1': ('Tam giác có một góc tù gọi là:', 'Tam giác tù', 'Tam giác nhọn', 'Tam giác vuông', 'Tam giác đều', 'A'),
        'c2': ('Trong tam giác, mỗi đỉnh có tương ứng bao nhiêu đường cao:', '$2$ đường cao', '$1$ đường cao', '$3$ đường cao', '$4$ đường cao', 'B'),
        'c3': ('Nếu đáy của tam giác tăng lên gấp đôi, chiều cao giữ nguyên thì diện tích tam giác:', 'Tăng gấp đôi', 'Tăng gấp bốn', 'Không đổi', 'Giảm đi một nửa', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $18\,\text{cm}$ và chiều cao $11\,\text{cm}$ là:', r'$198\,\text{cm}^2$', r'$99\,\text{cm}^2$', r'$88\,\text{cm}^2$', r'$72\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có hai cạnh góc vuông là $14\,\text{cm}$ và $6\,\text{cm}$ là:', r'$84\,\text{cm}^2$', r'$20\,\text{cm}^2$', r'$42\,\text{cm}^2$', r'$48\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $63\,\text{cm}^2$, chiều cao $9\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$14\,\text{cm}$', r'$7\,\text{cm}$', r'$21\,\text{cm}$', r'$12\,\text{cm}$', 'A'),
        'c7': ('Đặc điểm nào đúng với hình thang vuông:', 'Có $4$ góc vuông', 'Có một góc vuông (cạnh bên vuông góc với 2 đáy)', 'Hai đáy không song song', 'Hai cạnh bên bằng nhau', 'B'),
        'c8': ('Muốn tính diện tích hình thang, ta lấy tổng hai đáy nhân với chiều cao rồi:', 'Nhân 2', 'Trừ 2', 'Chia cho 2', 'Giữ nguyên', 'C'),
        'c9': (r'Một hình thang có đáy lớn $22\,\text{cm}$, đáy bé $16\,\text{cm}$, chiều cao $12\,\text{cm}$. Diện tích hình thang đó là:', r'$228\,\text{cm}^2$', r'$456\,\text{cm}^2$', r'$220\,\text{cm}^2$', r'$235\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $96\,\text{cm}^2$, tổng độ dài hai đáy là $24\,\text{cm}$. Chiều cao hình thang là:', r'$4\,\text{cm}$', r'$8\,\text{cm}$', r'$16\,\text{cm}$', r'$12\,\text{cm}$', 'B'),
        'c11': (r'Một mảnh đất hình thang có đáy lớn $45\,\text{m}$, đáy bé $35\,\text{m}$, chiều cao $20\,\text{m}$. Diện tích mảnh đất đó là:', r'$800\,\text{m}^2$', r'$1\\,600\,\text{m}^2$', r'$750\,\text{m}^2$', r'$850\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $24\,\text{cm}$. Kéo dài đáy thêm $6\,\text{cm}$ thì diện tích tăng thêm $36\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$120\,\text{cm}^2$', r'$144\,\text{cm}^2$', r'$150\,\text{cm}^2$', r'$136\,\text{cm}^2$', 'B'),
        'b1': ('$58{,}6 + 43{,}75$', '$94{,}5 - 56{,}48$', '$32{,}5 \\times 3{,}4$', '$99{,}9 : 3{,}7$'),
        'b1_ans': ('102{,}35', '38{,}02', '110{,}5', '27'),
        'b2': [('x + 32{,}6 = 78{,}4', 'x = 78{,}4 - 32{,}6', 'x = 45{,}8'),
               ('x - 42{,}5 = 51{,}8', 'x = 51{,}8 + 42{,}5', 'x = 94{,}3'),
               ('x \\times 7{,}2 = 61{,}2', 'x = 61{,}2 : 7{,}2', 'x = 8{,}5'),
               ('x : 6{,}4 = 16', 'x = 16 \\times 6{,}4', 'x = 102{,}4')],
        'b3': [(r'S_{\Delta} = (22 \times 16) : 2', r'\text{cm}^2', '176'),
               (r'S_{\Delta\text{ vuông}} = (18 \times 10) : 2', r'\text{cm}^2', '90'),
               (r'S_{\text{thang}} = (26 + 18) \times 14 : 2', r'\text{cm}^2', '308'),
               (r'S_{\text{thang}} = 40 \times 15 : 2', r'\text{m}^2', '300')]
    },
    {
        'code': '505',
        'c1': ('Tổng ba góc trong một hình tam giác luôn bằng:', '$180^\\circ$', '$90^\\circ$', '$360^\\circ$', '$270^\\circ$', 'A'),
        'c2': ('Đường cao của tam giác tù xuất phát từ đỉnh góc nhọn nằm ở:', 'Bên trong tam giác', 'Bên ngoài tam giác', 'Trên cạnh huyền', 'Trùng với đỉnh', 'B'),
        'c3': ('Nếu chiều cao tam giác tăng gấp đôi, đáy giữ nguyên thì diện tích tam giác:', 'Tăng gấp đôi', 'Tăng gấp bốn', 'Không đổi', 'Giảm đi một nửa', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $20\,\text{cm}$ và chiều cao $13\,\text{cm}$ là:', r'$260\,\text{cm}^2$', r'$130\,\text{cm}^2$', r'$120\,\text{cm}^2$', r'$140\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có hai cạnh góc vuông là $15\,\text{cm}$ và $8\,\text{cm}$ là:', r'$120\,\text{cm}^2$', r'$23\,\text{cm}^2$', r'$60\,\text{cm}^2$', r'$65\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $72\,\text{cm}^2$, chiều cao $12\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$12\,\text{cm}$', r'$6\,\text{cm}$', r'$18\,\text{cm}$', r'$10\,\text{cm}$', 'A'),
        'c7': ('Trong hình thang vuông, đường cao chính là:', 'Đáy lớn', 'Cạnh bên vuông góc với hai đáy', 'Đáy bé', 'Cạnh bên xiên', 'B'),
        'c8': ('Muốn tính diện tích hình thang, ta lấy tổng hai đáy nhân với chiều cao rồi:', 'Nhân 2', 'Trừ 2', 'Chia cho 2', 'Giữ nguyên', 'C'),
        'c9': (r'Một hình thang có đáy lớn $25\,\text{cm}$, đáy bé $15\,\text{cm}$, chiều cao $14\,\text{cm}$. Diện tích hình thang đó là:', r'$280\,\text{cm}^2$', r'$560\,\text{cm}^2$', r'$270\,\text{cm}^2$', r'$290\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $120\,\text{cm}^2$, tổng độ dài hai đáy là $30\,\text{cm}$. Chiều cao hình thang là:', r'$4\,\text{cm}$', r'$8\,\text{cm}$', r'$16\,\text{cm}$', r'$12\,\text{cm}$', 'B'),
        'c11': (r'Một thửa ruộng hình thang có đáy lớn $55\,\text{m}$, đáy bé $35\,\text{m}$, chiều cao $25\,\text{m}$. Diện tích thửa ruộng đó là:', r'$1\\,125\,\text{m}^2$', r'$2\\,250\,\text{m}^2$', r'$1\\,100\,\text{m}^2$', r'$1\\,200\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $25\,\text{cm}$. Kéo dài đáy thêm $5\,\text{cm}$ thì diện tích tăng thêm $40\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$180\,\text{cm}^2$', r'$200\,\text{cm}^2$', r'$220\,\text{cm}^2$', r'$190\,\text{cm}^2$', 'B'),
        'b1': ('$67{,}5 + 38{,}65$', '$98{,}2 - 49{,}38$', '$35{,}4 \\times 3{,}5$', '$108 : 4{,}5$'),
        'b1_ans': ('106{,}15', '48{,}82', '123{,}9', '24'),
        'b2': [('x + 35{,}8 = 86{,}2', 'x = 86{,}2 - 35{,}8', 'x = 50{,}4'),
               ('x - 48{,}6 = 37{,}5', 'x = 37{,}5 + 48{,}6', 'x = 86{,}1'),
               ('x \\times 8{,}5 = 72{,}25', 'x = 72{,}25 : 8{,}5', 'x = 8{,}5'),
               ('x : 7{,}5 = 18', 'x = 18 \\times 7{,}5', 'x = 135')],
        'b3': [(r'S_{\Delta} = (24 \times 18) : 2', r'\text{cm}^2', '216'),
               (r'S_{\Delta\text{ vuông}} = (20 \times 12) : 2', r'\text{cm}^2', '120'),
               (r'S_{\text{thang}} = (28 + 20) \times 15 : 2', r'\text{cm}^2', '360'),
               (r'S_{\text{thang}} = 45 \times 16 : 2', r'\text{m}^2', '360')]
    },
    {
        'code': '506',
        'c1': ('Tam giác có hai cạnh bằng nhau được gọi là:', 'Tam giác cân', 'Tam giác đều', 'Tam giác vuông', 'Tam giác tù', 'A'),
        'c2': ('Trong tam giác, đường cao tương ứng với cạnh đáy là đoạn thẳng kẻ từ đỉnh đối diện và:', 'Song song với đáy', 'Vuông góc với đường thẳng chứa đáy', 'Đi qua trung điểm cạnh bên', 'Bằng cạnh đáy', 'B'),
        'c3': ('Nếu cả đáy và chiều cao của tam giác đều tăng lên gấp đôi thì diện tích tam giác:', 'Tăng gấp bốn', 'Tăng gấp đôi', 'Tăng gấp tám', 'Không đổi', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $22\,\text{cm}$ và chiều cao $15\,\text{cm}$ là:', r'$330\,\text{cm}^2$', r'$165\,\text{cm}^2$', r'$150\,\text{cm}^2$', r'$175\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có hai cạnh góc vuông là $16\,\text{cm}$ và $9\,\text{cm}$ là:', r'$144\,\text{cm}^2$', r'$25\,\text{cm}^2$', r'$72\,\text{cm}^2$', r'$75\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $80\,\text{cm}^2$, chiều cao $10\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$16\,\text{cm}$', r'$8\,\text{cm}$', r'$20\,\text{cm}$', r'$12\,\text{cm}$', 'A'),
        'c7': ('Một hình thang có đáy lớn gấp đôi đáy bé, biết đáy bé là $10\,\text{cm}$ thì đáy lớn là:', '$15\,\text{cm}$', '$20\,\text{cm}$', '$25\,\text{cm}$', '$30\,\text{cm}$', 'B'),
        'c8': ('Muốn tính diện tích hình thang, ta lấy tổng độ dài hai đáy nhân với chiều cao rồi chia cho:', '$3$', '$4$', '$2$', '$1$', 'C'),
        'c9': (r'Một hình thang có đáy lớn $28\,\text{cm}$, đáy bé $18\,\text{cm}$, chiều cao $15\,\text{cm}$. Diện tích hình thang đó là:', r'$345\,\text{cm}^2$', r'$690\,\text{cm}^2$', r'$340\,\text{cm}^2$', r'$350\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $144\,\text{cm}^2$, tổng độ dài hai đáy là $36\,\text{cm}$. Chiều cao hình thang là:', r'$4\,\text{cm}$', r'$8\,\text{cm}$', r'$16\,\text{cm}$', r'$12\,\text{cm}$', 'B'),
        'c11': (r'Một thửa ruộng hình thang có đáy lớn $60\,\text{m}$, đáy bé $40\,\text{m}$, chiều cao $30\,\text{m}$. Diện tích thửa ruộng đó là:', r'$1\\,500\,\text{m}^2$', r'$3\\,000\,\text{m}^2$', r'$1\\,450\,\text{m}^2$', r'$1\\,550\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $30\,\text{cm}$. Kéo dài đáy thêm $6\,\text{cm}$ thì diện tích tăng thêm $45\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$210\,\text{cm}^2$', r'$225\,\text{cm}^2$', r'$240\,\text{cm}^2$', r'$200\,\text{cm}^2$', 'B'),
        'b1': ('$74{,}5 + 42{,}85$', '$102{,}4 - 58{,}75$', '$38{,}5 \\times 3{,}6$', '$124{,}8 : 4{,}8$'),
        'b1_ans': ('117{,}35', '43{,}65', '138{,}6', '26'),
        'b2': [('x + 41{,}5 = 95{,}8', 'x = 95{,}8 - 41{,}5', 'x = 54{,}3'),
               ('x - 52{,}4 = 43{,}8', 'x = 43{,}8 + 52{,}4', 'x = 96{,}2'),
               ('x \\times 9{,}2 = 87{,}4', 'x = 87{,}4 : 9{,}2', 'x = 9{,}5'),
               ('x : 8{,}4 = 20', 'x = 20 \\times 8{,}4', 'x = 168')],
        'b3': [(r'S_{\Delta} = (26 \times 20) : 2', r'\text{cm}^2', '260'),
               (r'S_{\Delta\text{ vuông}} = (22 \times 14) : 2', r'\text{cm}^2', '154'),
               (r'S_{\text{thang}} = (32 + 22) \times 16 : 2', r'\text{cm}^2', '432'),
               (r'S_{\text{thang}} = 50 \times 18 : 2', r'\text{m}^2', '450')]
    },
    {
        'code': '507',
        'c1': ('Tam giác có ba cạnh bằng nhau được gọi là:', 'Tam giác đều', 'Tam giác cân', 'Tam giác vuông', 'Tam giác nhọn', 'A'),
        'c2': ('Đáy và chiều cao của tam giác dùng để tính diện tích phải:', 'Bằng nhau', 'Có cùng một đơn vị đo', 'Khác đơn vị đo', 'Tùy ý', 'B'),
        'c3': ('Nếu đáy của tam giác giảm đi một nửa, chiều cao giữ nguyên thì diện tích tam giác:', 'Giảm đi một nửa', 'Giảm đi 4 lần', 'Không đổi', 'Tăng gấp đôi', 'A'),
        'c4': (r'Diện tích hình tam giác có đáy $24\,\text{cm}$ và chiều cao $16\,\text{cm}$ là:', r'$384\,\text{cm}^2$', r'$192\,\text{cm}^2$', r'$180\,\text{cm}^2$', r'$200\,\text{cm}^2$', 'B'),
        'c5': (r'Diện tích tam giác vuông có hai cạnh góc vuông là $18\,\text{cm}$ và $10\,\text{cm}$ là:', r'$180\,\text{cm}^2$', r'$28\,\text{cm}^2$', r'$90\,\text{cm}^2$', r'$95\,\text{cm}^2$', 'C'),
        'c6': (r'Một tam giác có diện tích $90\,\text{cm}^2$, chiều cao $12\,\text{cm}$. Độ dài đáy của tam giác đó là:', r'$15\,\text{cm}$', r'$7{,}5\,\text{cm}$', r'$20\,\text{cm}$', r'$14\,\text{cm}$', 'A'),
        'c7': ('Một hình thang có đáy lớn $24\,\text{cm}$, đáy bé bằng $\\dfrac{2}{3}$ đáy lớn. Đáy bé là:', '$12\,\text{cm}$', '$16\,\text{cm}$', '$18\,\text{cm}$', '$20\,\text{cm}$', 'B'),
        'c8': ('Tổng độ dài hai đáy của hình thang tính bởi công thức:', '$a + b = 2 \\times S \\times h$', '$a + b = S \\times h : 2$', '$a + b = 2 \\times S : h$', '$a + b = S : h$', 'C'),
        'c9': (r'Một hình thang có đáy lớn $32\,\text{cm}$, đáy bé $20\,\text{cm}$, chiều cao $16\,\text{cm}$. Diện tích hình thang đó là:', r'$416\,\text{cm}^2$', r'$832\,\text{cm}^2$', r'$410\,\text{cm}^2$', r'$420\,\text{cm}^2$', 'A'),
        'c10': (r'Một hình thang có diện tích $168\,\text{cm}^2$, tổng độ dài hai đáy là $42\,\text{cm}$. Chiều cao hình thang là:', r'$4\,\text{cm}$', r'$8\,\text{cm}$', r'$16\,\text{cm}$', r'$12\,\text{cm}$', 'B'),
        'c11': (r'Một thửa ruộng hình thang có đáy lớn $70\,\text{m}$, đáy bé $50\,\text{m}$, chiều cao $35\,\text{m}$. Diện tích thửa ruộng đó là:', r'$2\\,100\,\text{m}^2$', r'$4\\,200\,\text{m}^2$', r'$2\\,000\,\text{m}^2$', r'$2\\,200\,\text{m}^2$', 'A'),
        'c12': (r'Một tam giác có đáy $32\,\text{cm}$. Kéo dài đáy thêm $8\,\text{cm}$ thì diện tích tăng thêm $60\,\text{cm}^2$. Diện tích tam giác ban đầu là:', r'$220\,\text{cm}^2$', r'$240\,\text{cm}^2$', r'$260\,\text{cm}^2$', r'$200\,\text{cm}^2$', 'B'),
        'b1': ('$81{,}6 + 49{,}75$', '$115{,}2 - 68{,}45$', '$42{,}5 \\times 4{,}2$', '$147 : 4{,}2$'),
        'b1_ans': ('131{,}35', '46{,}75', '178{,}5', '35'),
        'b2': [('x + 48{,}6 = 105{,}4', 'x = 105{,}4 - 48{,}6', 'x = 56{,}8'),
               ('x - 58{,}5 = 54{,}8', 'x = 54{,}8 + 58{,}5', 'x = 113{,}3'),
               ('x \\times 9{,}5 = 99{,}75', 'x = 99{,}75 : 9{,}5', 'x = 10{,}5'),
               ('x : 9{,}2 = 25', 'x = 25 \\times 9{,}2', 'x = 230')],
        'b3': [(r'S_{\Delta} = (28 \times 22) : 2', r'\text{cm}^2', '308'),
               (r'S_{\Delta\text{ vuông}} = (24 \times 16) : 2', r'\text{cm}^2', '192'),
               (r'S_{\text{thang}} = (36 + 24) \times 18 : 2', r'\text{cm}^2', '540'),
               (r'S_{\text{thang}} = 60 \times 20 : 2', r'\text{m}^2', '600')]
    }
]

MA_DE_LIST = []
for idx, cfg in enumerate(MA_DE_CONFIGS):
    item = {
        'ma_de': cfg['code'],
        'tn': [
            cfg['c1'], cfg['c2'], cfg['c3'], cfg['c4'],
            cfg['c5'], cfg['c6'], cfg['c7'], cfg['c8'],
            cfg['c9'], cfg['c10'], cfg['c11'], cfg['c12']
        ],
        'bai1': cfg['b1'],
        'bai1_ans': cfg['b1_ans'],
        'bai2': cfg['b2'],
        'bai3': cfg['b3'],
        'bai4': g5_bai4_bai5[idx]['bai4'],
        'bai5': g5_bai4_bai5[idx]['bai5']
    }
    MA_DE_LIST.append(item)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base_dir, f'TUAN_{WEEK_NUM:02d}')
    os.makedirs(out_dir, exist_ok=True)

    tex_content = render_tex(WEEK_NUM, WEEK_TITLE, MA_DE_LIST, grade=5)
    tex_path = os.path.join(out_dir, f'Phieu_Bai_Tap_Tuan_{WEEK_NUM:02d}_Toan5.tex')
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print('Wrote:', tex_path)

    md_content = render_markdown_answers(WEEK_NUM, WEEK_TITLE, TOPICS, MA_DE_LIST, grade=5)
    md_path = os.path.join(out_dir, 'DAP_AN_VA_THANG_DIEM.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print('Wrote:', md_path)

    compile_and_verify(WEEK_NUM, base_dir)

if __name__ == '__main__':
    main()

