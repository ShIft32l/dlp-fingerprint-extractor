# Phase 05: Output Generator & CLI
Status: ⬜ Pending

## Objective
Nguyên bản hóa hệ thống thành một luồng chạy liên tục từ đầu đến cuối thông qua một file `main.py` có giao diện dòng lệnh (CLI). Định dạng output phải là file dễ dàng copy/paste vào hệ thống DLP.

## Requirements
### Functional
- [ ] Giao diện CLI nhận đối số (Arguments): thư mục chứa file mẫu, loại tài liệu cần focus. (VD: `python main.py --input ./samples --type "board_papers"`).
- [ ] Hàm `generate_output(phrases_list, output_format="txt")`.
- [ ] Ghi danh sách ra file (TXT mỗi dòng 1 câu HOẶC CSV có hai cột String/Type).

## Implementation Steps
1. [ ] Sử dụng thư viện `argparse` hoặc `click` trong `main.py`.
2. [ ] Ghép toàn bộ Pipeline: 
    * Quét file trong Folder -> Parser -> Text Processing -> AI Evaluator -> Generator.
3. [ ] Viết hàm `export_to_txt` và `export_to_csv` vào `src/generator.py`.
4. [ ] Thêm Progress Bar (ví dụ dùng thư viện `tqdm`) để User không bị "mù thông tin" khi script đang chạy lâu do gọi API.

## Files to Create/Modify
- `main.py` - File thực thi chính.
- `src/generator.py` - Module xuất kết quả.

## Test Criteria
- [ ] Chạy lệnh `python main.py --help` hiển thị đúng các tham số hướng dẫn.
- [ ] Chạy lệnh sinh thành công 1 thư mục mẫu nhỏ và tạo ra thư mục `output/` chứa file `sit_dictionary.txt`.

---
Next Phase: phase-06-testing.md
