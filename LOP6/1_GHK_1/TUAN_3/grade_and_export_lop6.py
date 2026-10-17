import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRATCH_PAGES = r'C:\Users\Admin\.gemini\antigravity-ide\brain\0a9f024e-c55e-4f4d-a770-56f664ce8f68\scratch\pages'
OUT_FOLDER_INDIVIDUAL = os.path.join(BASE_DIR, 'BAI_CHAM_TUNG_HOC_SINH')
FINAL_COMBINED_PDF = os.path.join(BASE_DIR, 'TAYSON_0001_DA_CHAM.pdf')
REPORT_MD = os.path.join(BASE_DIR, 'BANG_DIEM_CHI_TIET_LOP6_TUAN3.md')

os.makedirs(OUT_FOLDER_INDIVIDUAL, exist_ok=True)

# Fonts
font_score = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 56)
font_text_bold = ImageFont.truetype(r'C:\Windows\Fonts\timesbd.ttf', 27)
font_text_reg = ImageFont.truetype(r'C:\Windows\Fonts\times.ttf', 25)
font_tag = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 24)
font_mc = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 22)

red_ink = (215, 20, 20)
red_bg = (255, 240, 240)

def draw_tag_box(draw, x, y, text):
    draw.rectangle([x, y, x + 230, y + 38], fill=red_bg, outline=red_ink, width=2)
    draw.text((x + 10, y + 5), text, fill=red_ink, font=font_tag)

def draw_mc_mark(draw, cx, correct):
    y = 525
    if correct:
        draw.line([(cx+25, y+14), (cx+32, y+22), (cx+45, y+2)], fill=red_ink, width=4)
        draw.text((cx + 52, y), '+0.5', fill=red_ink, font=font_mc)
    else:
        draw.line([(cx+28, y+2), (cx+44, y+20)], fill=red_ink, width=4)
        draw.line([(cx+44, y+2), (cx+28, y+20)], fill=red_ink, width=4)
        draw.text((cx + 52, y), '0.0', fill=red_ink, font=font_mc)

students = [
    {
        'stt': '01', 'id': 'DUCKIEN1405', 'name': 'Nguyễn Đức Kiên',
        'filename': 'NGUYEN_DUC_KIEN_8.75.pdf', 'de': '104',
        'p_front': 2, 'p_back': 1, 'score': '8.75',
        'c1': '3b: D1 | Cần xem lại cách đổi đơn vị diện tích (1m² = 10000cm²).',
        'c2': 'Điểm TN: 2.5 / 2.5   |   Điểm TL: 6.25 / 7.5',
        'mc': [True, True, True, True, True],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D1 | 0.00 đ ]'}
    },
    {
        'stt': '02', 'id': '0967395567', 'name': 'Nguyễn Ngọc Hân',
        'filename': 'NGUYEN_NGOC_HAN_9.5.pdf', 'de': '102',
        'p_front': 4, 'p_back': 3, 'score': '9.50',
        'c1': 'TN: C5 | Bài làm rất tốt, lập luận và tính toán chính xác.',
        'c2': 'Điểm TN: 2.0 / 2.5   |   Điểm TL: 7.50 / 7.5',
        'mc': [True, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '03', 'id': 'THANHTRUC0405', 'name': 'Bùi Lê Thanh Trúc',
        'filename': 'BUI_LE_THANH_TRUC_4.75.pdf', 'de': '103',
        'p_front': 6, 'p_back': 5, 'score': '4.75',
        'c1': '1a: H1 | 2a: T1 | 2b: B0 | 3b: D1 | Cần ôn lại trắc nghiệm và các bước giải.',
        'c2': 'Điểm TN: 0.5 / 2.5   |   Điểm TL: 4.25 / 7.5',
        'mc': [False, False, False, False, True],
        'tags': {'1a': '[ H1 | 0.375 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ T1 | 0.75 đ ]', '2b': '[ B0 | 0.00 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D1 | 0.00 đ ]'}
    },
    {
        'stt': '04', 'id': 'TRONGKIEN0107', 'name': 'Nguyễn Trọng Kiên',
        'filename': 'NGUYEN_TRONG_KIEN_8.75.pdf', 'de': '104',
        'p_front': 8, 'p_back': 7, 'score': '8.75',
        'c1': '3b: D1 | Bài làm tốt, chú ý đổi đơn vị diện tích (1m² = 10000cm²).',
        'c2': 'Điểm TN: 2.5 / 2.5   |   Điểm TL: 6.25 / 7.5',
        'mc': [True, True, True, True, True],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D1 | 0.00 đ ]'}
    },
    {
        'stt': '05', 'id': 'MINHKHOI2510', 'name': 'Lê Thái Minh Khôi',
        'filename': 'LE_THAI_MINH_KHOI_8.75.pdf', 'de': '104',
        'p_front': 10, 'p_back': 9, 'score': '8.75',
        'c1': '3b: D1 | Bài làm tốt, chú ý đổi đơn vị diện tích xăng-ti-mét vuông.',
        'c2': 'Điểm TN: 2.5 / 2.5   |   Điểm TL: 6.25 / 7.5',
        'mc': [True, True, True, True, True],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D1 | 0.00 đ ]'}
    },
    {
        'stt': '06', 'id': 'TUNGLAM2108', 'name': 'Phan Tùng Lâm',
        'filename': 'PHAN_TUNG_LAM_8.25.pdf', 'de': '101',
        'p_front': 12, 'p_back': 11, 'score': '8.25',
        'c1': 'TN: C2, C5 | 3b: D2 | Chú ý công thức diện tích hình vuông cạnh x cạnh.',
        'c2': 'Điểm TN: 1.5 / 2.5   |   Điểm TL: 6.75 / 7.5',
        'mc': [True, False, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D2 | 0.50 đ ]'}
    },
    {
        'stt': '07', 'id': 'QUANGHAI3005', 'name': 'Vũ Quang Hải',
        'filename': 'VU_QUANG_HAI_7.75.pdf', 'de': '101',
        'p_front': 14, 'p_back': 13, 'score': '7.75',
        'c1': 'TN: C1, C2, C5 | 3b: D2 | Cần ôn lại trắc nghiệm và diện tích hình vuông.',
        'c2': 'Điểm TN: 1.0 / 2.5   |   Điểm TL: 6.75 / 7.5',
        'mc': [False, False, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D2 | 0.50 đ ]'}
    },
    {
        'stt': '08', 'id': 'TRILAM1605', 'name': 'Trương Trí Lâm',
        'filename': 'TRUONG_TRI_LAM_8.25.pdf', 'de': '102',
        'p_front': 16, 'p_back': 15, 'score': '8.25',
        'c1': 'TN: C2, C5 | 1d: H1 | Chú ý số hạng tự do khi đặt thừa số chung.',
        'c2': 'Điểm TN: 1.5 / 2.5   |   Điểm TL: 6.75 / 7.5',
        'mc': [True, False, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ H1 | 0.00 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '09', 'id': 'QUOCHAI1801', 'name': 'Trần Quốc Hải',
        'filename': 'TRAN_QUOC_HAI_8.0.pdf', 'de': '103',
        'p_front': 18, 'p_back': 17, 'score': '8.00',
        'c1': 'TN: C1, C2, C5 | 3b: T1 | Cẩn thận số 0 khi nhân 60 x 60.',
        'c2': 'Điểm TN: 1.0 / 2.5   |   Điểm TL: 7.00 / 7.5',
        'mc': [False, False, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ T1 | 0.75 đ ]'}
    },
    {
        'stt': '10', 'id': 'CAOTAI1405', 'name': 'Lê Cao Tài',
        'filename': 'LE_CAO_TAI_9.5.pdf', 'de': '102',
        'p_front': 20, 'p_back': 19, 'score': '9.50',
        'c1': 'TN: C5 | Bài làm xuất sắc, chữ viết rõ ràng, tính toán chuẩn xác.',
        'c2': 'Điểm TN: 2.0 / 2.5   |   Điểm TL: 7.50 / 7.5',
        'mc': [True, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '11', 'id': 'NHATMINH2203', 'name': 'Trần Nhật Minh',
        'filename': 'TRAN_NHAT_MINH_9.25.pdf', 'de': '104',
        'p_front': 22, 'p_back': 21, 'score': '9.25',
        'c1': 'TN: C5 | 3b: T1 | Bài làm rất tốt, chú ý ghi đúng 50x50 = 2500cm².',
        'c2': 'Điểm TN: 2.0 / 2.5   |   Điểm TL: 7.25 / 7.5',
        'mc': [True, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ T1 | 1.00 đ ]'}
    },
    {
        'stt': '12', 'id': 'KHANHTHI1004', 'name': 'Nguyễn Khánh Thi',
        'filename': 'NGUYEN_KHANH_THI_7.25.pdf', 'de': '102',
        'p_front': 24, 'p_back': 23, 'score': '7.25',
        'c1': 'TN: C1, C2, C4, C5 | 1b: C1 | 1d: H1 | Cần xem kỹ đề và rèn trắc nghiệm.',
        'c2': 'Điểm TN: 0.5 / 2.5   |   Điểm TL: 6.75 / 7.5',
        'mc': [False, False, True, False, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ C1 | 0.375 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ H1 | 0.25 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '13', 'id': 'BAOAN0601', 'name': 'Lê Trần Bảo An',
        'filename': 'LE_TRAN_BAO_AN_9.0.pdf', 'de': '101',
        'p_front': 26, 'p_back': 25, 'score': '9.00',
        'c1': 'TN: C1, C5 | Tự luận xuất sắc, trình bày bài sạch đẹp tuyệt đối.',
        'c2': 'Điểm TN: 1.5 / 2.5   |   Điểm TL: 7.50 / 7.5',
        'mc': [False, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '14', 'id': 'LEKHANHTHI', 'name': 'Nguyễn Lê Khánh Thi',
        'filename': 'NGUYEN_LE_KHANH_THI_10.0.pdf', 'de': '103',
        'p_front': 28, 'p_back': 27, 'score': '10.0',
        'c1': 'Bài làm xuất sắc đạt điểm tuyệt đối 10/10. Rất khen ngợi em!',
        'c2': 'Điểm TN: 2.5 / 2.5   |   Điểm TL: 7.50 / 7.5',
        'mc': [True, True, True, True, True],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '15', 'id': 'LAMPHONG', 'name': 'Nguyễn Lâm Phong',
        'filename': 'NGUYEN_LAM_PHONG_9.5.pdf', 'de': '102',
        'p_front': 30, 'p_back': 29, 'score': '9.50',
        'c1': 'TN: C5 | Bài làm rất tốt, trình bày cẩn thận, tính toán chính xác.',
        'c2': 'Điểm TN: 2.0 / 2.5   |   Điểm TL: 7.50 / 7.5',
        'mc': [True, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '16', 'id': '097514456', 'name': 'Võ Yến Ngọc',
        'filename': 'VO_YEN_NGOC_7.5.pdf', 'de': '103',
        'p_front': 32, 'p_back': 31, 'score': '7.50',
        'c1': 'TN: C1, C2, C5 | 1b: C1 | 1d: H1 | Cần làm hết trắc nghiệm và chép đúng đề.',
        'c2': 'Điểm TN: 1.0 / 2.5   |   Điểm TL: 6.50 / 7.5',
        'mc': [False, False, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ C1 | 0.25 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ H1 | 0.00 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '17', 'id': '0917193898', 'name': 'Nguyễn Yến Nhi',
        'filename': 'NGUYEN_YEN_NHI_9.0.pdf', 'de': '101',
        'p_front': 34, 'p_back': 33, 'score': '9.00',
        'c1': 'TN: C1, C5 | Tự luận xuất sắc, lập luận chặt chẽ, trình bày sạch sẽ.',
        'c2': 'Điểm TN: 1.5 / 2.5   |   Điểm TL: 7.50 / 7.5',
        'mc': [False, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ Đ | 1.25 đ ]'}
    },
    {
        'stt': '18', 'id': 'THAONHI3108', 'name': 'Bùi Thảo Nhi',
        'filename': 'BUI_THAO_NHI_8.25.pdf', 'de': '101',
        'p_front': 36, 'p_back': 35, 'score': '8.25',
        'c1': 'TN: C5 | 3b: D1 | Chú ý công thức diện tích gạch và đổi đơn vị.',
        'c2': 'Điểm TN: 2.0 / 2.5   |   Điểm TL: 6.25 / 7.5',
        'mc': [True, True, True, True, False],
        'tags': {'1a': '[ Đ | 0.625 đ ]', '1b': '[ Đ | 0.625 đ ]', '1c': '[ Đ | 0.625 đ ]', '1d': '[ Đ | 0.625 đ ]',
                 '2a': '[ Đ | 1.25 đ ]', '2b': '[ Đ | 1.25 đ ]', '3a': '[ Đ | 1.25 đ ]', '3b': '[ D1 | 0.00 đ ]'}
    }
]

mc_cols = [240, 510, 780, 1050, 1320]
all_combined_pages = []

print("Bắt đầu xử lý chấm điểm và tạo file cho 18 học sinh...")

for s in students:
    # 1. Mặt trước (Trang 1)
    p_front_file = os.path.join(SCRATCH_PAGES, f"page_{s['p_front']:02d}.jpg")
    img_f = Image.open(p_front_file).convert('RGB')
    draw_f = ImageDraw.Draw(img_f)

    # Điểm số
    draw_f.text((150, 325), s['score'], fill=red_ink, font=font_score)
    # Lời nhận xét
    draw_f.text((490, 315), s['c1'], fill=red_ink, font=font_text_bold)
    draw_f.text((490, 365), s['c2'], fill=red_ink, font=font_text_reg)

    # Đánh dấu trắc nghiệm
    for i, cor in enumerate(s['mc']):
        draw_mc_mark(draw_f, mc_cols[i], cor)

    # Tag điểm Câu 1
    draw_tag_box(draw_f, 100, 1580, s['tags']['1a'])
    draw_tag_box(draw_f, 850, 1580, s['tags']['1b'])
    draw_tag_box(draw_f, 100, 2220, s['tags']['1c'])
    draw_tag_box(draw_f, 850, 2220, s['tags']['1d'])

    # 2. Mặt sau (Trang 2)
    p_back_file = os.path.join(SCRATCH_PAGES, f"page_{s['p_back']:02d}.jpg")
    img_b = Image.open(p_back_file).convert('RGB')
    draw_b = ImageDraw.Draw(img_b)

    # Tag điểm Câu 2 & Câu 3
    draw_tag_box(draw_b, 100, 1070, s['tags']['2a'])
    draw_tag_box(draw_b, 850, 1070, s['tags']['2b'])
    draw_tag_box(draw_b, 100, 1680, s['tags']['3a'])
    draw_tag_box(draw_b, 100, 2210, s['tags']['3b'])

    # Lưu file PDF riêng từng học sinh
    single_pdf_path = os.path.join(OUT_FOLDER_INDIVIDUAL, s['filename'])
    img_f.save(
        single_pdf_path,
        save_all=True,
        append_images=[img_b],
        resolution=200.0,
        quality=85
    )
    print(f"Đã xuất: {s['filename']} (Điểm: {s['score']})")

    # Thêm vào danh sách file gộp
    all_combined_pages.append(img_f)
    all_combined_pages.append(img_b)

# Xuất file gộp toàn bộ lớp
print(f"\nĐang tạo file PDF tổng hợp cả lớp ({len(all_combined_pages)} trang)...")
all_combined_pages[0].save(
    FINAL_COMBINED_PDF,
    save_all=True,
    append_images=all_combined_pages[1:],
    resolution=200.0,
    quality=85
)
print(f"Đã lưu Master PDF: {FINAL_COMBINED_PDF}")

# Xuất báo cáo bảng điểm chi tiết markdown
report_content = f"""# BẢNG TỔNG HỢP ĐIỂM KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 03 BUỔI 01
**Lớp:** TOÁN 6 - TÂY SƠN | **Sĩ số làm bài:** 18 học sinh | **Ngày chấm:** 24/09/2026
**File PDF tổng hợp:** `TAYSON_0001_DA_CHAM.pdf` (36 trang, đã sắp đúng Mặt trước $\to$ Mặt sau)
**Thư mục bài riêng:** `BAI_CHAM_TUNG_HOC_SINH/`

---

## 📊 BẢNG ĐIỂM CHI TIẾT TỪNG HỌC SINH

| STT | Họ và tên học sinh | Mã đề | Điểm TN (2.5) | Điểm TL (7.5) | Tổng Điểm (10) | Xếp Loại | Tên file PDF bài chấm |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
"""

for s in students:
    sc = float(s['score'])
    if sc >= 9.0:
        xl = "Xuất sắc"
    elif sc >= 8.0:
        xl = "Giỏi"
    elif sc >= 6.5:
        xl = "Khá"
    elif sc >= 5.0:
        xl = "Trung bình"
    else:
        xl = "Yếu"
    
    tn_sc = sum(0.5 for m in s['mc'] if m)
    tl_sc = sc - tn_sc
    report_content += f"| {s['stt']} | **{s['name']}** | {s['de']} | {tn_sc:.1f} | {tl_sc:.2f} | **{sc:.2f}** | {xl} | `{s['filename']}` |\n"

# Thống kê
scores = [float(s['score']) for s in students]
avg_score = sum(scores) / len(scores)
max_score = max(scores)
min_score = min(scores)

report_content += f"""
---

## 📈 THỐNG KÊ PHỔ ĐIỂM
- **Điểm trung bình lớp:** **{avg_score:.2f} / 10**
- **Điểm cao nhất (Thủ khoa):** **{max_score:.2f}** (*Nguyễn Lê Khánh Thi - 10.0 điểm*)
- **Điểm thấp nhất:** **{min_score:.2f}** (*Bùi Lê Thanh Trúc - 4.75 điểm*)
- **Tỉ lệ Giỏi & Xuất sắc ($\ge 8.0$):** {sum(1 for sc in scores if sc >= 8.0)} / 18 ({sum(1 for sc in scores if sc >= 8.0)/18*100:.1f}%)
- **Tỉ lệ Khá (6.5 - 7.9):** {sum(1 for sc in scores if 6.5 <= sc < 8.0)} / 18 ({sum(1 for sc in scores if 6.5 <= sc < 8.0)/18*100:.1f}%)
- **Tỉ lệ Trung bình & Dưới TB ($< 6.5$):** {sum(1 for sc in scores if sc < 6.5)} / 18 ({sum(1 for sc in scores if sc < 6.5)/18*100:.1f}%)

---

## 🔍 NHẬN XÉT CHUNG VỀ CHUYÊN MÔN
1. **Phần Trắc nghiệm:**
   - Đa số học sinh nắm vững tính chất phân phối và phép chia có dư.
   - Câu 5 (khẳng định đúng về số 0 / số 1) có nhiều bạn nhầm lẫn chọn phương án sai.
2. **Phần Tự luận:**
   - **Câu 1 (Tính hợp lý):** Rất tốt! Đa số các em đều phát hiện ra các cặp nhân nhẩm tròn chục/tròn trăm ($25 \\times 4$, $125 \\times 8$, $250 \\times 4$, $50 \\times 2$) và đặt thừa số chung rất nhanh.
   - **Câu 2 (Tìm $x$):** Làm rất tốt, 17/18 học sinh đạt điểm tuyệt đối 2.5/2.5.
   - **Câu 3 (Bài toán thực tế):**
     - Đa số làm đúng ý a tính diện tích sân.
      - Ở ý b, nhiều học sinh bị lỗi đổi đơn vị diện tích: nhầm 2500 cm² = 25 m² thay vì 0.25 m², hoặc nhầm 40 x 4 thay vì 40 x 40. Thầy cô cần nhấn mạnh lại quy tắc 1 m² = 10.000 cm² cho cả lớp ở buổi chữa bài.
"""

with open(REPORT_MD, 'w', encoding='utf-8') as f:
    f.write(report_content)

print(f"\nĐã xuất báo cáo điểm số: {REPORT_MD}")
print("HOÀN THÀNH TOÀN BỘ QUY TRÌNH CHẤM BÀI!")