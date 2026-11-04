import json

file_path = 'LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_01/so_do_tu_duy_nguoc.json'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

marker = '"nghe_thuat_su_pham"'
cut_idx = text.find(marker)
if cut_idx != -1:
    base = text[:cut_idx]
    tail = '''"nghe_thuat_su_pham": {
    "tai_sao_nghi_ra_duong_phu": "Điểm E đã có góc AEC = 90 độ. Hạ EG vuông góc AC tạo ra tam giác vuông EGF nhận EF làm cạnh huyền, đồng thời cho ngay hệ thức lượng CE^2 = CG . CA. Hệ thức này ghép trực tiếp với kết quả CE^2 = CN . CI ở câu trước.",
    "chuoi_cau_hoi_dan_dat": [
      "Câu hỏi 1: Điểm M và điểm P có tính chất đối xứng gì đối với đoạn thẳng EF?",
      "Câu hỏi 2: Vậy muốn M, N, P thẳng hàng, điểm N bắt buộc phải có tính chất gì trên đoạn thẳng EF?",
      "Câu hỏi 3: Đoạn thẳng EF đang lơ lửng, muốn chứng minh trung điểm ta nên gắn nó vào loại hình học nào?",
      "Câu hỏi 4: Ta đã chứng minh CE^2 = CN . CI ở câu trước, làm sao tạo ra một tích đoạn thẳng mới bằng CE^2?"
    ]
  },
  "barem_diem": [
    {"muc": "Câu a", "diem": 0.75, "noi_dung": "Chứng minh tứ giác BEHD nội tiếp đường tròn đường kính BH"},
    {"muc": "Câu b1", "diem": 0.75, "noi_dung": "Chứng minh CE^2 = CN . CI qua hai tam giác đồng dạng CEN và CIE"},
    {"muc": "Câu b2 - Ý 1", "diem": 0.25, "noi_dung": "Chứng minh PM là đường trung trực của đoạn thẳng EF"},
    {"muc": "Câu b2 - Ý 2", "diem": 0.25, "noi_dung": "Kẻ đường phụ EG vuông góc AC, chứng minh tam giác CNG đồng dạng tam giác CAI"},
    {"muc": "Câu b2 - Ý 3", "diem": 0.25, "noi_dung": "Chứng minh tam giác NGF cân tại N, suy ra N là trung điểm của EF"},
    {"muc": "Câu b2 - Ý 4", "diem": 0.25, "noi_dung": "Từ PM là trung trực EF và N là trung điểm EF suy ra M, N, P thẳng hàng"}
  ]
}'''
    final_json = base + tail
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(final_json)

with open(file_path, 'r', encoding='utf-8') as f_in:
    d = json.load(f_in)

print("SUCCESS: JSON is 100% valid!")
print("Keys:", list(d.keys()))
print(f"Total mindmap levels: {len(d['so_do_tu_duy_nguoc'])}")
for lvl in d['so_do_tu_duy_nguoc']:
    print(f"  Tầng {lvl['tang']}: {lvl['dich_den']}")

