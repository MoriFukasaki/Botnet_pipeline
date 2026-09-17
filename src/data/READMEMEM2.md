BÁO CÁO TIẾN ĐỘ THỰC HIỆN - THÀNH VIÊN 2
Vai trò: Kỹ sư Dữ liệu Mạng (PCAP Processing & Labeling)  
Nhiệm vụ: Trích xuất đặc trưng luồng mạng (Flow Features) từ file PCAP thô và thực hiện gán nhãn dữ liệu Botnet/Normal cho bài tập lớn.


 1. Công cụ & Môi trường làm việc
- Ngôn ngữ & Môi trường: Python 3.14 (Virtual Environment `.venv`)
- Các thư viện chính: `scapy`, `pandas`, `numpy`
- Công cụ phân tích: Wireshark
- Tập dữ liệu sử dụng: CTU-13 Dataset - Scenario 7 (Sogou Botnet)
  - File PCAP nguồn: `capture20110816-2.truncated.pcap`
  - Dung lượng file PCAP thô: ~5.8 GB (Đã cắt/rút gọn dạng truncated để đọc nhanh)
  - Máy nhiễm Botnet (`Infected host`): IP `147.32.84.165` (Windows XP SARUMAN)

---

2. Tổng hợp công việc đã hoàn thành (To-do List)
 Chuẩn bị dữ liệu & Cấu trúc dự án
-  Khởi tạo và thiết lập môi trường ảo Python (`.venv`).
-  Tạo cấu trúc thư mục chuẩn cho dự án: `data/raw/`, `data/processed/`, `src/data/`.
-  Tải file PCAP mẫu của kịch bản CTU-13 Scenario 7 và đặt vào thư mục `data/raw/capture20110816-2.truncated.pcap`.

 Phát triển Module Trích xuất Đặc trưng Luồng (`flow_extractor.py`)
- Viết module `src/data/flow_extractor.py` thực hiện đọc gói tin 
- Gom nhóm các gói tin thành các Flow (Luồng 2 chiều - Bidirectional Flow) chuẩn dựa trên bộ 5-tuple: `(src_ip, dst_ip, src_port, dst_port, protocol)`.
- Tính toán 9 đặc trưng thống kê hình thái luồng mạng:
  - `flow_duration`: Thời gian tồn tại luồng (giây).
  - `total_fwd_pkts`, `total_bwd_pkts`: Tổng số gói tin đi (Forward) và về (Backward).
  - `total_fwd_bytes`, `total_bwd_bytes`: Tổng số bytes gửi đi và nhận về.
  - `bytes_per_sec`, `packets_per_sec`: Tốc độ truyền tải Bytes và Packets trên giây.
  - `packet_len_mean`, `packet_len_std`: Trung bình và độ lệch chuẩn kích thước gói tin.
  - Lưu kết quả trích xuất chưa gán nhãn vào file `data/processed/flows_unlabeled.csv`.

 Phát triển Module Gán nhãn Dữ liệu (`labeling.py`)
- [x] Đọc thông tin kịch bản từ tài liệu `README.md` của Scenario 7, xác định chính xác địa chỉ IP máy nhiễm Botnet: `147.32.84.165`.
-  Viết module `src/data/labeling.py` áp dụng quy tắc gán nhãn nhị phân:
- Nếu `src_ip` hoặc `dst_ip` là `147.32.84.165` => `label = 1` (Botnet).
 - Ngược lại => `label = 0` (Normal).
- Xuất tập dữ liệu hoàn chỉnh ra file `data/processed/ctu13_labeled_flows.csv`.

3. Kết quả nghiệm thu thực tế

3.1. Thống kê trích xuất PCAP (`flow_extractor.py`)
- Tổng số gói tin đã đọc:** `7,466,160` gói tin.
- Số gói tin bỏ qua (không phải TCP/UDP-IP):** `8,507` gói tin.
- Tổng số Flow gom được:** `104,385` luồng mạng.
- Thời gian xử lý:** `1812.5` giây (~30 phút).

 3.2. Thống kê kết quả gán nhãn (`labeling.py`)
| Loại nhãn (Label) | Ý nghĩa                         | Số lượng Flow | Tỷ lệ (%) |
| 0                 | Luồng mạng bình thường (Normal) | 104,337       | `~99.96%` |
| 1                 | Luồng mạng độc hại (Botnet)     | 48            | `~0.04%`  |
| Tổng cộng         | Tất cả luồng dữ liệu            | 104,385       | `100.0%`  |

File đầu ra: `data/processed/ctu13_labeled_flows.csv` 

4. Công việc tiếp theo (Kế hoạch Tuần 4)
- Bàn giao file dữ liệu `data/processed/ctu13_labeled_flows.csv` cho Thành viên 3 
- Soạn thảo nội dung Chương 2 Báo cáo:
  - Mô tả tổng quan về tập dữ liệu CTU-13 (Scenario 7 - Sogou Botnet).
  - Bảng định nghĩa và ý nghĩa kỹ thuật của 9 đặc trưng luồng mạng đã trích xuất.
  - Gửi bản nháp Chương 2 cho Leader (Thành viên 1) tổng hợp báo cáo.