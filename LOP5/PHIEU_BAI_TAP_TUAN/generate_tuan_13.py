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
    'Bài toán thực tế tính diện tích thửa ruộng hình thang',
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Một hình tam giác có bao nhiêu đỉnh, bao nhiêu cạnh và bao nhiêu góc:', '$4$ đỉnh, $4$ cạnh, $4$ góc', '$3$ đỉnh, $4$ cạnh, $3$ góc', '$3$ đỉnh, $3$ cạnh, $3$ góc', '$3$ đỉnh, $3$ cạnh, $4$ góc', 'C'),
        'c2': ('Trong hình tam giác vuông, hai cạnh góc vuông chính là:', 'Đáy và chiều cao tương ứng', 'Hai đường chéo', 'Hai cạnh đáy', 'Hai cạnh huyền', 'A'),
        'c3': ('Công thức tính diện tích hình tam giác có độ dài đáy $a$ và chiều cao $h$ là:', '$S = a \\times h$', '$S = (a + h) : 2$', '$S = (a + h) \\times 2$', '$S = (a \\times h) : 2$', 'D'),
        'c4': ('Diện tích hình tam giác có đáy $12\\,\\text{cm}$ và chiều cao $8\\,\\text{cm}$ là:', '$96\\,\\text{cm}^2$', '$48\\,\\text{cm}^2$', '$24\\,\\text{cm}^2$', '$40\\,\\text{cm}^2$', 'B'),
        'c5': ('Diện tích tam giác vuông có độ dài hai cạnh góc vuông là $6\\,\\text{cm}$ và $8\\,\\text{cm}$ là:', '$24\\,\\text{cm}^2$', '$48\\,\\text{cm}^2$', '$14\\,\\text{cm}^2$', '$28\\,\\text{cm}^2$', 'A'),
        'c6': ('Một tam giác có diện tích $30\\,\\text{cm}^2$, chiều cao $6\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$5\\,\\text{cm}$', '$15\\,\\text{cm}$', '$10\\,\\text{cm}$', '$8\\,\\text{cm}$', 'C'),
        'c7': ('Hình thang là hình tứ giác có:', 'Hai cặp cạnh đối diện song song', 'Một cặp cạnh đối diện song song', 'Bốn góc vuông', 'Bốn cạnh bằng nhau', 'B'),
        'c8': ('Công thức tính diện tích hình thang có hai đáy $a, b$ và chiều cao $h$ là:', '$S = (a + b) \\times h$', '$S = (a \\times b) \\times h : 2$', '$S = a \\times b : 2$', '$S = (a + b) \\times h : 2$', 'D'),
        'c9': ('Một hình thang có đáy lớn $15\\,\\text{cm}$, đáy bé $9\\,\\text{cm}$, chiều cao $8\\,\\text{cm}$. Diện tích hình thang đó là:', '$192\\,\\text{cm}^2$', '$96\\,\\text{cm}^2$', '$90\\,\\text{cm}^2$', '$108\\,\\text{cm}^2$', 'B'),
        'c10': ('Một hình thang có diện tích $60\\,\\text{cm}^2$, tổng độ dài hai đáy là $20\\,\\text{cm}$. Chiều cao hình thang là:', '$3\\,\\text{cm}$', '$12\\,\\text{cm}$', '$8\\,\\text{cm}$', '$6\\,\\text{cm}$', 'D'),
        'c11': ('Một thửa ruộng hình thang có đáy lớn $40\\,\\text{m}$, đáy bé $25\\,\\text{m}$, chiều cao $20\\,\\text{m}$. Diện tích thửa ruộng đó là:', '$650\\,\\text{m}^2$', '$1\\\\,300\\,\\text{m}^2$', '$600\\,\\text{m}^2$', '$700\\,\\text{m}^2$', 'A'),
        'c12': ('Một tam giác có đáy $15\\,\\text{cm}$. Kéo dài đáy thêm $4\\,\\text{cm}$ thì diện tích tăng thêm $18\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$60\\,\\text{cm}^2$', '$72\\,\\text{cm}^2$', '$67{,}5\\,\\text{cm}^2$', '$54\\,\\text{cm}^2$', 'C'),
        'b1': ('$45{,}8 + 27{,}65$', '$84{,}3 - 39{,}48$', '$18{,}5 \\times 4{,}2$', '$91{,}8 : 5{,}4$', '$36{,}75 + 48{,}9$', '$100 - 45{,}76$', '$24{,}6 \\times 3{,}5$', '$75{,}6 : 4{,}2$'),
        'b1_ans': ('73{,}45', '44{,}82', '77{,}7', '17', '85{,}65', '54{,}24', '86{,}1', '18'),
        'b2': [
            ('x + 18{,}5 = 45{,}2', 'x = 45{,}2 - 18{,}5', 'x = 26{,}7'),
            ('x - 24{,}6 = 38{,}8', 'x = 38{,}8 + 24{,}6', 'x = 63{,}4'),
            ('x : 3{,}6 = 12{,}5', 'x = 12{,}5 \\times 3{,}6', 'x = 45'),
            ('x \\times 4{,}5 = 38{,}25', 'x = 38{,}25 : 4{,}5', 'x = 8{,}5'),
            ('72{,}5 - x = 28{,}7', 'x = 72{,}5 - 28{,}7', 'x = 43{,}8'),
            ('48 : x = 6{,}4', 'x = 48 : 6{,}4', 'x = 7{,}5'),
        ],
        'b3': [
            ('8\\,\\text{m}^2', '\\text{dm}^2', '800'),
            ('15\\,\\text{dm}^2', '\\text{cm}^2', '1\\,500'),
            ('4\\,\\text{m}^2', '\\text{cm}^2', '40\\,000'),
            ('5\\,\\text{ha}', '\\text{m}^2', '50\\,000'),
            ('2\\,\\text{km}^2', '\\text{ha}', '200'),
            ('600\\,\\text{cm}^2', '\\text{dm}^2', '6'),
            ('40\\,000\\,\\text{m}^2', '\\text{ha}', '4'),
            ('7\\,\\text{m}^2\\,25\\,\\text{dm}^2', '\\text{dm}^2', '725'),
            ('9\\,\\text{dm}^2\\,6\\,\\text{cm}^2', '\\text{cm}^2', '906'),
            ('3{,}5\\,\\text{m}^2', '\\text{dm}^2', '350'),
            ('0{,}45\\,\\text{ha}', '\\text{m}^2', '4\\,500'),
            ('6\\,\\text{m}^2\\,8\\,\\text{dm}^2', '\\text{m}^2', '6{,}08'),
        ]
    },
    {
        'code': '502',
        'c1': ('Tam giác có một góc vuông được gọi là:', 'Tam giác nhọn', 'Tam giác vuông', 'Tam giác tù', 'Tam giác đều', 'B'),
        'c2': ('Đoạn thẳng vuông góc kẻ từ đỉnh của tam giác xuống cạnh đáy đối diện gọi là:', 'Cạnh bên', 'Đường chéo', 'Trung điểm', 'Chiều cao', 'D'),
        'c3': ('Muốn tính diện tích hình tam giác, ta lấy độ dài đáy nhân với chiều cao (cùng đơn vị đo) rồi:', 'Chia cho 2', 'Nhân với 2', 'Chia cho 4', 'Giữ nguyên', 'A'),
        'c4': ('Diện tích hình tam giác có đáy $14\\,\\text{cm}$ và chiều cao $9\\,\\text{cm}$ là:', '$126\\,\\text{cm}^2$', '$46\\,\\text{cm}^2$', '$63\\,\\text{cm}^2$', '$32\\,\\text{cm}^2$', 'C'),
        'c5': ('Diện tích tam giác vuông có hai cạnh góc vuông là $8\\,\\text{cm}$ và $10\\,\\text{cm}$ là:', '$80\\,\\text{cm}^2$', '$18\\,\\text{cm}^2$', '$45\\,\\text{cm}^2$', '$40\\,\\text{cm}^2$', 'D'),
        'c6': ('Một tam giác có diện tích $45\\,\\text{cm}^2$, chiều cao $9\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$10\\,\\text{cm}$', '$5\\,\\text{cm}$', '$15\\,\\text{cm}$', '$8\\,\\text{cm}$', 'A'),
        'c7': ('Hình thang có một cạnh bên vuông góc với hai đáy gọi là:', 'Hình thang cân', 'Hình bình hành', 'Hình thang vuông', 'Hình thoi', 'C'),
        'c8': ('Muốn tính diện tích hình thang ta lấy tổng độ dài hai đáy nhân với chiều cao (cùng đơn vị đo) rồi:', 'Nhân với 2', 'Chia cho 2', 'Chia cho 4', 'Giữ nguyên', 'B'),
        'c9': ('Một hình thang có đáy lớn $18\\,\\text{cm}$, đáy bé $12\\,\\text{cm}$, chiều cao $10\\,\\text{cm}$. Diện tích hình thang đó là:', '$150\\,\\text{cm}^2$', '$300\\,\\text{cm}^2$', '$140\\,\\text{cm}^2$', '$160\\,\\text{cm}^2$', 'A'),
        'c10': ('Một hình thang có diện tích $84\\,\\text{cm}^2$, tổng độ dài hai đáy là $24\\,\\text{cm}$. Chiều cao hình thang là:', '$3{,}5\\,\\text{cm}$', '$14\\,\\text{cm}$', '$7\\,\\text{cm}$', '$8\\,\\text{cm}$', 'C'),
        'c11': ('Một mảnh đất hình thang có đáy lớn $35\\,\\text{m}$, đáy bé $25\\,\\text{m}$, chiều cao $16\\,\\text{m}$. Diện tích mảnh đất đó là:', '$960\\,\\text{m}^2$', '$450\\,\\text{m}^2$', '$500\\,\\text{m}^2$', '$480\\,\\text{m}^2$', 'D'),
        'c12': ('Một tam giác có đáy $20\\,\\text{cm}$. Kéo dài đáy thêm $5\\,\\text{cm}$ thì diện tích tăng thêm $30\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$100\\,\\text{cm}^2$', '$120\\,\\text{cm}^2$', '$150\\,\\text{cm}^2$', '$90\\,\\text{cm}^2$', 'B'),
        'b1': ('$54{,}6 + 32{,}75$', '$92{,}4 - 47{,}65$', '$24{,}5 \\times 3{,}6$', '$98{,}8 : 5{,}2$', '$42{,}86 + 39{,}5$', '$90 - 36{,}48$', '$18{,}4 \\times 4{,}5$', '$83{,}2 : 3{,}2$'),
        'b1_ans': ('87{,}35', '44{,}75', '88{,}2', '19', '82{,}36', '53{,}52', '82{,}8', '26'),
        'b2': [
            ('x + 23{,}4 = 56{,}8', 'x = 56{,}8 - 23{,}4', 'x = 33{,}4'),
            ('x - 31{,}5 = 42{,}7', 'x = 42{,}7 + 31{,}5', 'x = 74{,}2'),
            ('x : 4{,}5 = 14', 'x = 14 \\times 4{,}5', 'x = 63'),
            ('x \\times 5{,}2 = 44{,}2', 'x = 44{,}2 : 5{,}2', 'x = 8{,}5'),
            ('85{,}4 - x = 36{,}8', 'x = 85{,}4 - 36{,}8', 'x = 48{,}6'),
            ('54 : x = 7{,}2', 'x = 54 : 7{,}2', 'x = 7{,}5'),
        ],
        'b3': [
            ('6\\,\\text{m}^2', '\\text{dm}^2', '600'),
            ('18\\,\\text{dm}^2', '\\text{cm}^2', '1\\,800'),
            ('3\\,\\text{m}^2', '\\text{cm}^2', '30\\,000'),
            ('7\\,\\text{ha}', '\\text{m}^2', '70\\,000'),
            ('3\\,\\text{km}^2', '\\text{ha}', '300'),
            ('800\\,\\text{cm}^2', '\\text{dm}^2', '8'),
            ('60\\,000\\,\\text{m}^2', '\\text{ha}', '6'),
            ('5\\,\\text{m}^2\\,34\\,\\text{dm}^2', '\\text{dm}^2', '534'),
            ('8\\,\\text{dm}^2\\,5\\,\\text{cm}^2', '\\text{cm}^2', '805'),
            ('4{,}2\\,\\text{m}^2', '\\text{dm}^2', '420'),
            ('0{,}65\\,\\text{ha}', '\\text{m}^2', '6\\,500'),
            ('4\\,\\text{m}^2\\,15\\,\\text{dm}^2', '\\text{m}^2', '4{,}15'),
        ]
    },
    {
        'code': '503',
        'c1': ('Tam giác có ba góc đều nhọn gọi là:', 'Tam giác vuông', 'Tam giác tù', 'Tam giác cân', 'Tam giác nhọn', 'D'),
        'c2': ('Khoảng cách vuông góc giữa hai đáy của hình thang gọi là:', 'Chiều cao', 'Cạnh đáy', 'Đường chéo', 'Cạnh bên', 'A'),
        'c3': ('Muốn tính diện tích tam giác ta lấy đáy nhân với chiều cao rồi:', 'Nhân với 2', 'Cộng với 2', 'Chia cho 2', 'Trừ đi 2', 'C'),
        'c4': ('Diện tích hình tam giác có đáy $16\\,\\text{cm}$ và chiều cao $7\\,\\text{cm}$ là:', '$112\\,\\text{cm}^2$', '$56\\,\\text{cm}^2$', '$48\\,\\text{cm}^2$', '$36\\,\\text{cm}^2$', 'B'),
        'c5': ('Diện tích tam giác vuông có hai cạnh góc vuông là $12\\,\\text{cm}$ và $5\\,\\text{cm}$ là:', '$60\\,\\text{cm}^2$', '$30\\,\\text{cm}^2$', '$17\\,\\text{cm}^2$', '$35\\,\\text{cm}^2$', 'B'),
        'c6': ('Một tam giác có diện tích $48\\,\\text{cm}^2$, chiều cao $8\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$6\\,\\text{cm}$', '$18\\,\\text{cm}$', '$10\\,\\text{cm}$', '$12\\,\\text{cm}$', 'D'),
        'c7': ('Hai cạnh song song của hình thang được gọi là:', 'Hai cạnh đáy', 'Hai cạnh bên', 'Hai đường cao', 'Hai đường chéo', 'A'),
        'c8': ('Diện tích hình thang có đáy lớn $a$, đáy bé $b$, chiều cao $h$ tính bởi:', '$S = (a + b) \\times h$', '$S = (a - b) \\times h : 2$', '$S = (a + b) \\times h : 2$', '$S = a \\times b : 2$', 'C'),
        'c9': ('Một hình thang có đáy lớn $20\\,\\text{cm}$, đáy bé $14\\,\\text{cm}$, chiều cao $8\\,\\text{cm}$. Diện tích hình thang đó là:', '$272\\,\\text{cm}^2$', '$140\\,\\text{cm}^2$', '$130\\,\\text{cm}^2$', '$136\\,\\text{cm}^2$', 'D'),
        'c10': ('Một hình thang có diện tích $75\\,\\text{cm}^2$, tổng độ dài hai đáy là $25\\,\\text{cm}$. Chiều cao hình thang là:', '$3\\,\\text{cm}$', '$6\\,\\text{cm}$', '$12\\,\\text{cm}$', '$8\\,\\text{cm}$', 'B'),
        'c11': ('Một thửa ruộng hình thang có đáy lớn $50\\,\\text{m}$, đáy bé $30\\,\\text{m}$, chiều cao $24\\,\\text{m}$. Diện tích thửa ruộng đó là:', '$1\\\\,920\\,\\text{m}^2$', '$900\\,\\text{m}^2$', '$960\\,\\text{m}^2$', '$1\\\\,000\\,\\text{m}^2$', 'C'),
        'c12': ('Một tam giác có đáy $18\\,\\text{cm}$. Kéo dài đáy thêm $6\\,\\text{cm}$ thì diện tích tăng thêm $27\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$81\\,\\text{cm}^2$', '$75\\,\\text{cm}^2$', '$90\\,\\text{cm}^2$', '$72\\,\\text{cm}^2$', 'A'),
        'b1': ('$38{,}7 + 45{,}65$', '$81{,}5 - 36{,}78$', '$16{,}5 \\times 4{,}8$', '$86{,}4 : 3{,}6$', '$53{,}48 + 28{,}7$', '$100 - 54{,}35$', '$25{,}6 \\times 3{,}4$', '$78{,}4 : 2{,}8$'),
        'b1_ans': ('84{,}35', '44{,}72', '79{,}2', '24', '82{,}18', '45{,}65', '87{,}04', '28'),
        'b2': [
            ('x + 27{,}5 = 64{,}2', 'x = 64{,}2 - 27{,}5', 'x = 36{,}7'),
            ('x - 36{,}8 = 45{,}4', 'x = 45{,}4 + 36{,}8', 'x = 82{,}2'),
            ('x : 5{,}2 = 15', 'x = 15 \\times 5{,}2', 'x = 78'),
            ('x \\times 6{,}5 = 55{,}25', 'x = 55{,}25 : 6{,}5', 'x = 8{,}5'),
            ('91{,}2 - x = 43{,}6', 'x = 91{,}2 - 43{,}6', 'x = 47{,}6'),
            ('63 : x = 8{,}4', 'x = 63 : 8{,}4', 'x = 7{,}5'),
        ],
        'b3': [
            ('9\\,\\text{m}^2', '\\text{dm}^2', '900'),
            ('24\\,\\text{dm}^2', '\\text{cm}^2', '2\\,400'),
            ('5\\,\\text{m}^2', '\\text{cm}^2', '50\\,000'),
            ('4\\,\\text{ha}', '\\text{m}^2', '40\\,000'),
            ('4\\,\\text{km}^2', '\\text{ha}', '400'),
            ('900\\,\\text{cm}^2', '\\text{dm}^2', '9'),
            ('80\\,000\\,\\text{m}^2', '\\text{ha}', '8'),
            ('8\\,\\text{m}^2\\,45\\,\\text{dm}^2', '\\text{dm}^2', '845'),
            ('6\\,\\text{dm}^2\\,8\\,\\text{cm}^2', '\\text{cm}^2', '608'),
            ('5{,}8\\,\\text{m}^2', '\\text{dm}^2', '580'),
            ('0{,}32\\,\\text{ha}', '\\text{m}^2', '3\\,200'),
            ('7\\,\\text{m}^2\\,24\\,\\text{dm}^2', '\\text{m}^2', '7{,}24'),
        ]
    },
    {
        'code': '504',
        'c1': ('Tam giác có một góc tù gọi là:', 'Tam giác tù', 'Tam giác nhọn', 'Tam giác vuông', 'Tam giác đều', 'A'),
        'c2': ('Trong tam giác, mỗi đỉnh có tương ứng bao nhiêu đường cao:', '$2$ đường cao', '$3$ đường cao', '$1$ đường cao', '$4$ đường cao', 'C'),
        'c3': ('Nếu đáy của tam giác tăng lên gấp đôi, chiều cao giữ nguyên thì diện tích tam giác:', 'Tăng gấp bốn', 'Không đổi', 'Giảm đi một nửa', 'Tăng gấp đôi', 'D'),
        'c4': ('Diện tích hình tam giác có đáy $18\\,\\text{cm}$ và chiều cao $11\\,\\text{cm}$ là:', '$198\\,\\text{cm}^2$', '$99\\,\\text{cm}^2$', '$88\\,\\text{cm}^2$', '$72\\,\\text{cm}^2$', 'B'),
        'c5': ('Diện tích tam giác vuông có hai cạnh góc vuông là $14\\,\\text{cm}$ và $6\\,\\text{cm}$ là:', '$84\\,\\text{cm}^2$', '$20\\,\\text{cm}^2$', '$42\\,\\text{cm}^2$', '$48\\,\\text{cm}^2$', 'C'),
        'c6': ('Một tam giác có diện tích $63\\,\\text{cm}^2$, chiều cao $9\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$7\\,\\text{cm}$', '$14\\,\\text{cm}$', '$21\\,\\text{cm}$', '$12\\,\\text{cm}$', 'B'),
        'c7': ('Đặc điểm nào đúng với hình thang vuông:', 'Có $4$ góc vuông', 'Hai đáy không song song', 'Hai cạnh bên bằng nhau', 'Có một góc vuông (cạnh bên vuông góc với 2 đáy)', 'D'),
        'c8': ('Muốn tính diện tích hình thang, ta lấy tổng hai đáy nhân với chiều cao rồi:', 'Chia cho 2', 'Nhân 2', 'Trừ 2', 'Giữ nguyên', 'A'),
        'c9': ('Một hình thang có đáy lớn $22\\,\\text{cm}$, đáy bé $16\\,\\text{cm}$, chiều cao $12\\,\\text{cm}$. Diện tích hình thang đó là:', '$456\\,\\text{cm}^2$', '$228\\,\\text{cm}^2$', '$220\\,\\text{cm}^2$', '$235\\,\\text{cm}^2$', 'B'),
        'c10': ('Một hình thang có diện tích $96\\,\\text{cm}^2$, tổng độ dài hai đáy là $24\\,\\text{cm}$. Chiều cao hình thang là:', '$8\\,\\text{cm}$', '$4\\,\\text{cm}$', '$16\\,\\text{cm}$', '$12\\,\\text{cm}$', 'A'),
        'c11': ('Một mảnh đất hình thang có đáy lớn $45\\,\\text{m}$, đáy bé $35\\,\\text{m}$, chiều cao $20\\,\\text{m}$. Diện tích mảnh đất đó là:', '$1\\\\,600\\,\\text{m}^2$', '$750\\,\\text{m}^2$', '$800\\,\\text{m}^2$', '$850\\,\\text{m}^2$', 'C'),
        'c12': ('Một tam giác có đáy $24\\,\\text{cm}$. Kéo dài đáy thêm $6\\,\\text{cm}$ thì diện tích tăng thêm $36\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$120\\,\\text{cm}^2$', '$150\\,\\text{cm}^2$', '$136\\,\\text{cm}^2$', '$144\\,\\text{cm}^2$', 'D'),
        'b1': ('$58{,}6 + 43{,}75$', '$94{,}5 - 56{,}48$', '$32{,}5 \\times 3{,}4$', '$99{,}9 : 3{,}7$', '$46{,}58 + 37{,}6$', '$90 - 43{,}65$', '$19{,}5 \\times 4{,}4$', '$91{,}2 : 3{,}8$'),
        'b1_ans': ('102{,}35', '38{,}02', '110{,}5', '27', '84{,}18', '46{,}35', '85{,}8', '24'),
        'b2': [
            ('x + 32{,}6 = 78{,}4', 'x = 78{,}4 - 32{,}6', 'x = 45{,}8'),
            ('x - 42{,}5 = 51{,}8', 'x = 51{,}8 + 42{,}5', 'x = 94{,}3'),
            ('x : 6{,}4 = 16', 'x = 16 \\times 6{,}4', 'x = 102{,}4'),
            ('x \\times 7{,}2 = 61{,}2', 'x = 61{,}2 : 7{,}2', 'x = 8{,}5'),
            ('76{,}8 - x = 29{,}5', 'x = 76{,}8 - 29{,}5', 'x = 47{,}3'),
            ('72 : x = 9{,}6', 'x = 72 : 9{,}6', 'x = 7{,}5'),
        ],
        'b3': [
            ('12\\,\\text{m}^2', '\\text{dm}^2', '1\\,200'),
            ('25\\,\\text{dm}^2', '\\text{cm}^2', '2\\,500'),
            ('6\\,\\text{m}^2', '\\text{cm}^2', '60\\,000'),
            ('8\\,\\text{ha}', '\\text{m}^2', '80\\,000'),
            ('5\\,\\text{km}^2', '\\text{ha}', '500'),
            ('500\\,\\text{cm}^2', '\\text{dm}^2', '5'),
            ('50\\,000\\,\\text{m}^2', '\\text{ha}', '5'),
            ('6\\,\\text{m}^2\\,18\\,\\text{dm}^2', '\\text{dm}^2', '618'),
            ('7\\,\\text{dm}^2\\,4\\,\\text{cm}^2', '\\text{cm}^2', '704'),
            ('2{,}8\\,\\text{m}^2', '\\text{dm}^2', '280'),
            ('0{,}75\\,\\text{ha}', '\\text{m}^2', '7\\,500'),
            ('5\\,\\text{m}^2\\,9\\,\\text{dm}^2', '\\text{m}^2', '5{,}09'),
        ]
    },
    {
        'code': '505',
        'c1': ('Tổng ba góc trong một hình tam giác luôn bằng:', '$90^\\circ$', '$180^\\circ$', '$360^\\circ$', '$270^\\circ$', 'B'),
        'c2': ('Đường cao của tam giác tù xuất phát từ đỉnh góc nhọn nằm ở:', 'Bên trong tam giác', 'Trên cạnh huyền', 'Trùng với đỉnh', 'Bên ngoài tam giác', 'D'),
        'c3': ('Nếu chiều cao tam giác tăng gấp đôi, đáy giữ nguyên thì diện tích tam giác:', 'Tăng gấp bốn', 'Tăng gấp đôi', 'Không đổi', 'Giảm đi một nửa', 'B'),
        'c4': ('Diện tích hình tam giác có đáy $20\\,\\text{cm}$ và chiều cao $13\\,\\text{cm}$ là:', '$130\\,\\text{cm}^2$', '$260\\,\\text{cm}^2$', '$120\\,\\text{cm}^2$', '$140\\,\\text{cm}^2$', 'A'),
        'c5': ('Diện tích tam giác vuông có hai cạnh góc vuông là $15\\,\\text{cm}$ và $8\\,\\text{cm}$ là:', '$60\\,\\text{cm}^2$', '$120\\,\\text{cm}^2$', '$23\\,\\text{cm}^2$', '$65\\,\\text{cm}^2$', 'A'),
        'c6': ('Một tam giác có diện tích $72\\,\\text{cm}^2$, chiều cao $12\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$6\\,\\text{cm}$', '$18\\,\\text{cm}$', '$12\\,\\text{cm}$', '$10\\,\\text{cm}$', 'C'),
        'c7': ('Trong hình thang vuông, đường cao chính là:', 'Đáy lớn', 'Đáy bé', 'Cạnh bên xiên', 'Cạnh bên vuông góc với hai đáy', 'D'),
        'c8': ('Muốn tính diện tích hình thang, ta lấy tổng hai đáy nhân với chiều cao rồi:', 'Nhân 2', 'Chia cho 2', 'Trừ 2', 'Giữ nguyên', 'B'),
        'c9': ('Một hình thang có đáy lớn $25\\,\\text{cm}$, đáy bé $15\\,\\text{cm}$, chiều cao $14\\,\\text{cm}$. Diện tích hình thang đó là:', '$560\\,\\text{cm}^2$', '$270\\,\\text{cm}^2$', '$280\\,\\text{cm}^2$', '$290\\,\\text{cm}^2$', 'C'),
        'c10': ('Một hình thang có diện tích $120\\,\\text{cm}^2$, tổng độ dài hai đáy là $30\\,\\text{cm}$. Chiều cao hình thang là:', '$4\\,\\text{cm}$', '$16\\,\\text{cm}$', '$12\\,\\text{cm}$', '$8\\,\\text{cm}$', 'D'),
        'c11': ('Một thửa ruộng hình thang có đáy lớn $55\\,\\text{m}$, đáy bé $35\\,\\text{m}$, chiều cao $25\\,\\text{m}$. Diện tích thửa ruộng đó là:', '$1\\\\,125\\,\\text{m}^2$', '$2\\\\,250\\,\\text{m}^2$', '$1\\\\,100\\,\\text{m}^2$', '$1\\\\,200\\,\\text{m}^2$', 'A'),
        'c12': ('Một tam giác có đáy $25\\,\\text{cm}$. Kéo dài đáy thêm $5\\,\\text{cm}$ thì diện tích tăng thêm $40\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$180\\,\\text{cm}^2$', '$220\\,\\text{cm}^2$', '$200\\,\\text{cm}^2$', '$190\\,\\text{cm}^2$', 'C'),
        'b1': ('$67{,}5 + 38{,}65$', '$98{,}2 - 49{,}38$', '$35{,}4 \\times 3{,}5$', '$108 : 4{,}5$', '$38{,}76 + 45{,}8$', '$100 - 38{,}72$', '$28{,}4 \\times 3{,}5$', '$85{,}5 : 4{,}5$'),
        'b1_ans': ('106{,}15', '48{,}82', '123{,}9', '24', '84{,}56', '61{,}28', '99{,}4', '19'),
        'b2': [
            ('x + 35{,}8 = 86{,}2', 'x = 86{,}2 - 35{,}8', 'x = 50{,}4'),
            ('x - 48{,}6 = 37{,}5', 'x = 37{,}5 + 48{,}6', 'x = 86{,}1'),
            ('x : 7{,}5 = 18', 'x = 18 \\times 7{,}5', 'x = 135'),
            ('x \\times 8{,}5 = 72{,}25', 'x = 72{,}25 : 8{,}5', 'x = 8{,}5'),
            ('84{,}6 - x = 35{,}9', 'x = 84{,}6 - 35{,}9', 'x = 48{,}7'),
            ('96 : x = 12{,}8', 'x = 96 : 12{,}8', 'x = 7{,}5'),
        ],
        'b3': [
            ('14\\,\\text{m}^2', '\\text{dm}^2', '1\\,400'),
            ('32\\,\\text{dm}^2', '\\text{cm}^2', '3\\,200'),
            ('7\\,\\text{m}^2', '\\text{cm}^2', '70\\,000'),
            ('6\\,\\text{ha}', '\\text{m}^2', '60\\,000'),
            ('6\\,\\text{km}^2', '\\text{ha}', '600'),
            ('700\\,\\text{cm}^2', '\\text{dm}^2', '7'),
            ('70\\,000\\,\\text{m}^2', '\\text{ha}', '7'),
            ('9\\,\\text{m}^2\\,52\\,\\text{dm}^2', '\\text{dm}^2', '952'),
            ('5\\,\\text{dm}^2\\,9\\,\\text{cm}^2', '\\text{cm}^2', '509'),
            ('6{,}4\\,\\text{m}^2', '\\text{dm}^2', '640'),
            ('0{,}85\\,\\text{ha}', '\\text{m}^2', '8\\,500'),
            ('8\\,\\text{m}^2\\,35\\,\\text{dm}^2', '\\text{m}^2', '8{,}35'),
        ]
    },
    {
        'code': '506',
        'c1': ('Tam giác có hai cạnh bằng nhau được gọi là:', 'Tam giác đều', 'Tam giác vuông', 'Tam giác cân', 'Tam giác tù', 'C'),
        'c2': ('Trong tam giác, đường cao tương ứng với cạnh đáy là đoạn thẳng kẻ từ đỉnh đối diện và:', 'Song song với đáy', 'Vuông góc với đường thẳng chứa đáy', 'Đi qua trung điểm cạnh bên', 'Bằng cạnh đáy', 'B'),
        'c3': ('Nếu cả đáy và chiều cao của tam giác đều tăng lên gấp đôi thì diện tích tam giác:', 'Tăng gấp đôi', 'Tăng gấp tám', 'Không đổi', 'Tăng gấp bốn', 'D'),
        'c4': ('Diện tích hình tam giác có đáy $22\\,\\text{cm}$ và chiều cao $15\\,\\text{cm}$ là:', '$165\\,\\text{cm}^2$', '$330\\,\\text{cm}^2$', '$150\\,\\text{cm}^2$', '$175\\,\\text{cm}^2$', 'A'),
        'c5': ('Diện tích tam giác vuông có hai cạnh góc vuông là $16\\,\\text{cm}$ và $9\\,\\text{cm}$ là:', '$144\\,\\text{cm}^2$', '$25\\,\\text{cm}^2$', '$75\\,\\text{cm}^2$', '$72\\,\\text{cm}^2$', 'D'),
        'c6': ('Một tam giác có diện tích $80\\,\\text{cm}^2$, chiều cao $10\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$16\\,\\text{cm}$', '$8\\,\\text{cm}$', '$20\\,\\text{cm}$', '$12\\,\\text{cm}$', 'A'),
        'c7': ('Một hình thang có đáy lớn gấp đôi đáy bé, biết đáy bé là $10\\,\text{cm}$ thì đáy lớn là:', '$15\\,\text{cm}$', '$20\\,\text{cm}$', '$25\\,\text{cm}$', '$30\\,\text{cm}$', 'B'),
        'c8': ('Muốn tính diện tích hình thang, ta lấy tổng độ dài hai đáy nhân với chiều cao rồi chia cho:', '$3$', '$4$', '$2$', '$1$', 'C'),
        'c9': ('Một hình thang có đáy lớn $28\\,\\text{cm}$, đáy bé $18\\,\\text{cm}$, chiều cao $15\\,\\text{cm}$. Diện tích hình thang đó là:', '$690\\,\\text{cm}^2$', '$340\\,\\text{cm}^2$', '$350\\,\\text{cm}^2$', '$345\\,\\text{cm}^2$', 'D'),
        'c10': ('Một hình thang có diện tích $144\\,\\text{cm}^2$, tổng độ dài hai đáy là $36\\,\\text{cm}$. Chiều cao hình thang là:', '$4\\,\\text{cm}$', '$16\\,\\text{cm}$', '$8\\,\\text{cm}$', '$12\\,\\text{cm}$', 'C'),
        'c11': ('Một thửa ruộng hình thang có đáy lớn $60\\,\\text{m}$, đáy bé $40\\,\\text{m}$, chiều cao $30\\,\\text{m}$. Diện tích thửa ruộng đó là:', '$3\\\\,000\\,\\text{m}^2$', '$1\\\\,500\\,\\text{m}^2$', '$1\\\\,450\\,\\text{m}^2$', '$1\\\\,550\\,\\text{m}^2$', 'B'),
        'c12': ('Một tam giác có đáy $30\\,\\text{cm}$. Kéo dài đáy thêm $6\\,\\text{cm}$ thì diện tích tăng thêm $45\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$225\\,\\text{cm}^2$', '$210\\,\\text{cm}^2$', '$240\\,\\text{cm}^2$', '$200\\,\\text{cm}^2$', 'A'),
        'b1': ('$74{,}5 + 42{,}85$', '$102{,}4 - 58{,}75$', '$38{,}5 \\times 3{,}6$', '$124{,}8 : 4{,}8$', '$49{,}68 + 34{,}5$', '$90 - 27{,}85$', '$31{,}5 \\times 2{,}6$', '$94{,}6 : 4{,}3$'),
        'b1_ans': ('117{,}35', '43{,}65', '138{,}6', '26', '84{,}18', '62{,}15', '81{,}9', '22'),
        'b2': [
            ('x + 41{,}5 = 95{,}8', 'x = 95{,}8 - 41{,}5', 'x = 54{,}3'),
            ('x - 52{,}4 = 43{,}8', 'x = 43{,}8 + 52{,}4', 'x = 96{,}2'),
            ('x : 8{,}4 = 20', 'x = 20 \\times 8{,}4', 'x = 168'),
            ('x \\times 9{,}2 = 87{,}4', 'x = 87{,}4 : 9{,}2', 'x = 9{,}5'),
            ('95{,}3 - x = 47{,}8', 'x = 95{,}3 - 47{,}8', 'x = 47{,}5'),
            ('84 : x = 11{,}2', 'x = 84 : 11{,}2', 'x = 7{,}5'),
        ],
        'b3': [
            ('16\\,\\text{m}^2', '\\text{dm}^2', '1\\,600'),
            ('28\\,\\text{dm}^2', '\\text{cm}^2', '2\\,800'),
            ('8\\,\\text{m}^2', '\\text{cm}^2', '80\\,000'),
            ('9\\,\\text{ha}', '\\text{m}^2', '90\\,000'),
            ('7\\,\\text{km}^2', '\\text{ha}', '700'),
            ('400\\,\\text{cm}^2', '\\text{dm}^2', '4'),
            ('90\\,000\\,\\text{m}^2', '\\text{ha}', '9'),
            ('4\\,\\text{m}^2\\,65\\,\\text{dm}^2', '\\text{dm}^2', '465'),
            ('4\\,\\text{dm}^2\\,7\\,\\text{cm}^2', '\\text{cm}^2', '407'),
            ('7{,}5\\,\\text{m}^2', '\\text{dm}^2', '750'),
            ('0{,}55\\,\\text{ha}', '\\text{m}^2', '5\\,500'),
            ('9\\,\\text{m}^2\\,42\\,\\text{dm}^2', '\\text{m}^2', '9{,}42'),
        ]
    },
    {
        'code': '507',
        'c1': ('Tam giác có ba cạnh bằng nhau được gọi là:', 'Tam giác cân', 'Tam giác vuông', 'Tam giác nhọn', 'Tam giác đều', 'D'),
        'c2': ('Đáy và chiều cao của tam giác dùng để tính diện tích phải:', 'Bằng nhau', 'Khác đơn vị đo', 'Có cùng một đơn vị đo', 'Tùy ý', 'C'),
        'c3': ('Nếu đáy của tam giác giảm đi một nửa, chiều cao giữ nguyên thì diện tích tam giác:', 'Giảm đi một nửa', 'Giảm đi 4 lần', 'Không đổi', 'Tăng gấp đôi', 'A'),
        'c4': ('Diện tích hình tam giác có đáy $24\\,\\text{cm}$ và chiều cao $16\\,\\text{cm}$ là:', '$384\\,\\text{cm}^2$', '$192\\,\\text{cm}^2$', '$180\\,\\text{cm}^2$', '$200\\,\\text{cm}^2$', 'B'),
        'c5': ('Diện tích tam giác vuông có hai cạnh góc vuông là $18\\,\\text{cm}$ và $10\\,\\text{cm}$ là:', '$180\\,\\text{cm}^2$', '$28\\,\\text{cm}^2$', '$90\\,\\text{cm}^2$', '$95\\,\\text{cm}^2$', 'C'),
        'c6': ('Một tam giác có diện tích $90\\,\\text{cm}^2$, chiều cao $12\\,\\text{cm}$. Độ dài đáy của tam giác đó là:', '$7{,}5\\,\\text{cm}$', '$15\\,\\text{cm}$', '$20\\,\\text{cm}$', '$14\\,\\text{cm}$', 'B'),
        'c7': ('Một hình thang có đáy lớn $24\\,\text{cm}$, đáy bé bằng $\\dfrac{2}{3}$ đáy lớn. Đáy bé là:', '$12\\,\text{cm}$', '$18\\,\text{cm}$', '$20\\,\text{cm}$', '$16\\,\text{cm}$', 'D'),
        'c8': ('Tổng độ dài hai đáy của hình thang tính bởi công thức:', '$a + b = 2 \\times S : h$', '$a + b = 2 \\times S \\times h$', '$a + b = S \\times h : 2$', '$a + b = S : h$', 'A'),
        'c9': ('Một hình thang có đáy lớn $32\\,\\text{cm}$, đáy bé $20\\,\\text{cm}$, chiều cao $16\\,\\text{cm}$. Diện tích hình thang đó là:', '$416\\,\\text{cm}^2$', '$832\\,\\text{cm}^2$', '$410\\,\\text{cm}^2$', '$420\\,\\text{cm}^2$', 'A'),
        'c10': ('Một hình thang có diện tích $168\\,\\text{cm}^2$, tổng độ dài hai đáy là $42\\,\\text{cm}$. Chiều cao hình thang là:', '$4\\,\\text{cm}$', '$16\\,\\text{cm}$', '$12\\,\\text{cm}$', '$8\\,\\text{cm}$', 'D'),
        'c11': ('Một thửa ruộng hình thang có đáy lớn $70\\,\\text{m}$, đáy bé $50\\,\\text{m}$, chiều cao $35\\,\\text{m}$. Diện tích thửa ruộng đó là:', '$4\\\\,200\\,\\text{m}^2$', '$2\\\\,000\\,\\text{m}^2$', '$2\\\\,100\\,\\text{m}^2$', '$2\\\\,200\\,\\text{m}^2$', 'C'),
        'c12': ('Một tam giác có đáy $32\\,\\text{cm}$. Kéo dài đáy thêm $8\\,\\text{cm}$ thì diện tích tăng thêm $60\\,\\text{cm}^2$. Diện tích tam giác ban đầu là:', '$220\\,\\text{cm}^2$', '$240\\,\\text{cm}^2$', '$260\\,\\text{cm}^2$', '$200\\,\\text{cm}^2$', 'B'),
        'b1': ('$81{,}6 + 49{,}75$', '$115{,}2 - 68{,}45$', '$42{,}5 \\times 4{,}2$', '$147 : 4{,}2$', '$56{,}48 + 48{,}7$', '$100 - 42{,}58$', '$23{,}5 \\times 4{,}6$', '$112 : 3{,}5$'),
        'b1_ans': ('131{,}35', '46{,}75', '178{,}5', '35', '105{,}18', '57{,}42', '108{,}1', '32'),
        'b2': [
            ('x + 48{,}6 = 105{,}4', 'x = 105{,}4 - 48{,}6', 'x = 56{,}8'),
            ('x - 58{,}5 = 54{,}8', 'x = 54{,}8 + 58{,}5', 'x = 113{,}3'),
            ('x : 9{,}2 = 25', 'x = 25 \\times 9{,}2', 'x = 230'),
            ('x \\times 9{,}5 = 99{,}75', 'x = 99{,}75 : 9{,}5', 'x = 10{,}5'),
            ('102{,}4 - x = 54{,}6', 'x = 102{,}4 - 54{,}6', 'x = 47{,}8'),
            ('90 : x = 12', 'x = 90 : 12', 'x = 7{,}5'),
        ],
        'b3': [
            ('18\\,\\text{m}^2', '\\text{dm}^2', '1\\,800'),
            ('35\\,\\text{dm}^2', '\\text{cm}^2', '3\\,500'),
            ('9\\,\\text{m}^2', '\\text{cm}^2', '90\\,000'),
            ('10\\,\\text{ha}', '\\text{m}^2', '100\\,000'),
            ('8\\,\\text{km}^2', '\\text{ha}', '800'),
            ('300\\,\\text{cm}^2', '\\text{dm}^2', '3'),
            ('30\\,000\\,\\text{m}^2', '\\text{ha}', '3'),
            ('8\\,\\text{m}^2\\,76\\,\\text{dm}^2', '\\text{dm}^2', '876'),
            ('3\\,\\text{dm}^2\\,8\\,\\text{cm}^2', '\\text{cm}^2', '308'),
            ('8{,}2\\,\\text{m}^2', '\\text{dm}^2', '820'),
            ('0{,}95\\,\\text{ha}', '\\text{m}^2', '9\\,500'),
            ('3\\,\\text{m}^2\\,65\\,\\text{dm}^2', '\\text{m}^2', '3{,}65'),
        ]
    },
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
