import json

file_path = 'LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_02/so_do_tu_duy_nguoc.json'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

marker = '"tang": 5'
cut_idx = text.find(marker)
if cut_idx != -1:
    # find the opening brace before "tang": 5
    brace_idx = text.rfind('{', 0, cut_idx)
    base = text[:brace_idx]
    tail = '''{
      "tang": 5,
      "dich_den": "Kết luận cực trị",
      "suy_luan": "DH . DA = DB . DC <= ((DB+DC)/2)^2 = BC^2 / 4. Dấu bằng khi DB = DC <=> D trùng I <=> Tam giác ABC cân tại A <=> A là điểm chính giữa cung lớn BC."
    }
  ],
  "so_do_cong_thuc_hinh_thong": [
    "[ĐÍCH ĐẾN]: max(DH . DA) = BC^2 / 4 <=> A LÀ ĐIỂM CHÍNH GIỮA CUNG LỚN BC",
    "<= Dấu '=' BĐT Cauchy: DB = DC <=> D trùng I <=> Tam giác ABC cân tại A",
    "<= BĐT Cauchy: DB . DC <= ((DB+DC)/2)^2 = (BC/2)^2 = BC^2 / 4",
    "<= DH . DA = DB . DC",
    "<= { DH = DK ; DK . DA = DB . DC }",
    "<= { Tam giác HBK cân tại B <=> góc HBD = góc KBD ; Tam giác DBK ∼ Tam giác DAC (g-g) }",
    "<= góc HBD = góc KBD = góc KAC = 90° - góc C [GIẢ THIẾT KHỞI PHÁT TỰ NHIÊN]"
  ],
  "phan_tich_su_pham": {
    "ky_thuat_vang": "Kéo dài AD cắt (O) tại K để đưa điểm H thành điểm K trên đường tròn, kích hoạt định lý phương tích cát tuyến DK . DA = DB . DC và BĐT Cauchy.",
    "chuoi_cau_hoi": [
      "Câu 1: Đoạn DH nằm lơ lửng, làm sao đưa nó về đường tròn (O)?",
      "Câu 2: Nếu kéo dài AD cắt (O) tại K, điểm K có quan hệ đối xứng gì với trực tâm H qua BC?",
      "Câu 3: Tích DK . DA gợi nhớ đến định lý hình học nào trong đường tròn (O)?",
      "Câu 4: Tổng DB + DC có thay đổi không khi A di động trên cung lớn BC?"
    ]
  },
  "barem_diem": [
    {"muc": "Câu a", "diem": 0.75, "noi_dung": "Chứng minh tứ giác DHEC nội tiếp đường tròn đường kính HC"},
    {"muc": "Câu b", "diem": 0.75, "noi_dung": "Chứng minh BHCM là hình bình hành suy ra I là trung điểm HM"},
    {"muc": "Câu c - Ý 1", "diem": 0.25, "noi_dung": "Kéo dài AD cắt (O) tại K, chứng minh tam giác HBK cân suy ra DH = DK"},
    {"muc": "Câu c - Ý 2", "diem": 0.25, "noi_dung": "Chứng minh tam giác DBK đồng dạng DAC suy ra DK . DA = DB . DC"},
    {"muc": "Câu c - Ý 3", "diem": 0.25, "noi_dung": "Áp dụng BĐT Cauchy suy ra DH . DA <= BC^2 / 4"},
    {"muc": "Câu c - Ý 4", "diem": 0.25, "noi_dung": "Chỉ ra dấu bằng và kết luận A là điểm chính giữa cung lớn BC"}
  ]
}'''
    final_json = base + tail
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(final_json)

# Verify valid JSON
with open(file_path, 'r', encoding='utf-8') as f_in:
    d = json.load(f_in)

print("SUCCESS: JSON is 100% valid for BAI_HINH_02!")
print("Keys:", list(d.keys()))
print(f"Total mindmap levels: {len(d['so_do_tu_duy_nguoc'])}")

