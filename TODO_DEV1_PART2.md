# TO-DO LIST GIAI ĐOẠN 2: DEV 1 (LEADER & SYSTEM ARCHITECT)
# TÍCH HỢP HỆ THỐNG, CLI DETECT, RUN PIPELINE & BÁO CÁO TỔNG THỂ

> **Thành viên**: Dev 1 (Trưởng nhóm / Kiến trúc sư hệ thống)  
> **Giai đoạn**: Sprint 2 - Chặng về đích (Ngày 9 đến Ngày 14)  
> **Trọng trách chính**: Kết nối toàn bộ module thành sản phẩm hoàn chỉnh, viết CLI, tổng hợp Báo cáo Word và thiết kế Slide bảo vệ.  

---

## 📌 Trạng Thái Hiện Tại
- [x] Khởi tạo Git repository và cấu trúc thư mục quy chuẩn.
- [x] Quản trị tiến độ và hỗ trợ giải quyết xung đột mã nguồn.
- [ ] Lập trình công cụ CLI suy diễn `src/inference/detect.py`.
- [ ] Lập trình script điều phối tự động `scripts/run_pipeline.py`.
- [ ] Chủ trì biên tập cuốn Báo cáo khoa học hoàn chỉnh (`Bao_cao_Botnet.docx`).
- [ ] Thiết kế Slide thuyết trình bảo vệ đề tài (`Slide_Bao_ve.pptx`).

---

## 🛠 Công Cụ & Tài Nguyên Cần Dùng
* **Ngôn ngữ & Thư viện**: Python 3.10+, `argparse` hoặc `click`, `pickle` / `joblib`, `scikit-learn`, `pandas`.
* **Văn phòng**: Microsoft Word (định dạng chuẩn bìa, mục lục), PowerPoint / Canva (thiết kế Slide).
* **Đầu vào tiếp nhận**:
  * Nhận mô hình tối ưu `models/best_model.joblib` từ **Dev 4**.
  * Nhận hàm tiền xử lý `src/features/preprocessor.py` từ **Dev 3**.
  * Nhận hàm trích xuất `src/data/flow_extractor.py` từ **Dev 2**.
  * Nhận các chương báo cáo: Chương 2 (Dev 2), Chương 3 (Dev 3), Chương 4 (Dev 4), Chương 5 (Dev 5).

---

## 💻 Nhiệm Vụ Chi Tiết Từng Ngày (To-do List)

### 1. Đồng bộ mã nguồn từ Dev 4 (Hạn chót: Ngày 10)
- [ ] Chuyển sang nhánh `Dev1` và kéo model mới nhất từ `Dev4`:
  ```bash
  git checkout Dev1
  git merge Dev4 -m "Merge Dev4: Lay best_model va pipeline ML"
  ```

### 2. Phát triển công cụ CLI `src/inference/detect.py` (Hạn chót: Ngày 11)
- [ ] Lập trình file `src/inference/detect.py` có khả năng nhận tham số file PCAP từ dòng lệnh:
  ```bash
  python src/inference/detect.py --pcap path/to/capture.pcap
  ```
- [ ] **Quy trình hoạt động bên trong script**:
  1. Đọc file PCAP thông qua module `flow_extractor.py` của Dev 2 $\rightarrow$ Xuất ra bảng luồng.
  2. Lưu lại danh sách IP gốc (`src_ip`, `dst_ip`) để phục vụ cảnh báo.
  3. Đưa qua bộ lọc rò rỉ dữ liệu và chuẩn hóa của Dev 3.
  4. Nạp mô hình `models/best_model.joblib` để phân loại luồng mạng.
  5. Xuất cảnh báo ra màn hình Terminal:
     * Tổng số luồng quét được.
     * Số luồng bị phát hiện là Botnet.
     * **Danh sách các địa chỉ IP độc hại nghi vấn** cần chặn.

### 3. Phát triển script điều phối `scripts/run_pipeline.py` (Hạn chót: Ngày 12)
- [ ] Tạo file `scripts/run_pipeline.py` cho phép chạy 1 lệnh duy nhất tự động toàn bộ quy trình:
  ```bash
  python scripts/run_pipeline.py
  ```
  *(Tự động gọi: Tiền xử lý $\rightarrow$ Huấn luyện mô hình $\rightarrow$ Xuất báo cáo số liệu)*.

### 4. Tổng hợp Báo cáo nghiên cứu khoa học (Hạn chót: Ngày 13)
- [ ] Soạn thảo **Chương 1: Mở đầu & Mục tiêu đề tài** (Lý do chọn đề tài, tính cấp thiết của việc phát hiện Botnet từ lưu lượng mạng, mục tiêu và phạm vi nghiên cứu).
- [ ] Soạn thảo **Chương 6: Kết luận & Hướng phát triển** (Tổng kết những việc đã làm được, các hạn chế còn tồn đọng và hướng mở rộng như phát hiện theo thời gian thực).
- [ ] Ghép toàn bộ nội dung thành file `Bao_cao_Botnet.docx` hoàn chỉnh:
  * Trang bìa chuẩn trường/khoa, Lời cảm ơn, Mục lục tự động, Danh mục bảng biểu/hình vẽ.
  * Chương 1: Mở đầu (Dev 1).
  * Chương 2: Tổng quan tập dữ liệu CTU-13 & Bóc tách đặc trưng PCAP (Dev 2).
  * Chương 3: Khám phá dữ liệu (EDA), Tiền xử lý & Chống Data Leakage (Dev 3).
  * Chương 4: Huấn luyện & Đánh giá hiệu năng 4 mô hình Machine Learning (Dev 4).
  * Chương 5: Triển khai Ứng dụng Web Demo Streamlit & Trực quan hóa (Dev 5).
  * Chương 6: Kết luận & Hướng phát triển (Dev 1).
  * Tài liệu tham khảo.

### 5. Thiết kế Slide thuyết trình bảo vệ đề tài (Hạn chót: Ngày 14)
- [ ] Thiết kế file `Slide_Bao_ve.pptx` (khoảng 15 - 20 slide):
  * Bố cục chuẩn: Tổng quan đề tài $\rightarrow$ Dữ liệu $\rightarrow$ Tiền xử lý $\rightarrow$ Huấn luyện ML $\rightarrow$ Demo Web $\rightarrow$ Kết luận.
  * Chèn đầy đủ các biểu đồ của Dev 5 và bảng điểm của Dev 4.
  * Phân chia thời lượng nói: Mỗi thành viên thuyết trình 2 - 3 phút về phần việc của mình.

---

## 🎯 Tiêu Chí Nghiệm Thu Sản Phẩm
- [ ] Lệnh `python src/inference/detect.py --pcap test.pcap` chạy mượt mà, in ra kết quả cảnh báo chuẩn xác.
- [ ] Cuốn Báo cáo `.docx` đầy đủ 6 chương, định dạng chỉn chu, không lỗi chính tả.
- [ ] Slide thuyết trình `.pptx` đẹp mắt, phân công rõ ràng cho 5 thành viên.

