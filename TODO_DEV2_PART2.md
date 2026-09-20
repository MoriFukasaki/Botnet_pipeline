# TO-DO LIST GIAI ĐOẠN 2: DEV 2 (DATA & PCAP ENGINEER)
# HỖ TRỢ TÍCH HỢP & HOÀN THIỆN CHƯƠNG 2 BÁO CÁO KHOA HỌC

> **Thành viên**: Dev 2 (Kỹ sư Dữ liệu mạng & Bóc tách PCAP)  
> **Giai đoạn**: Sprint 2 - Chặng về đích (Ngày 9 đến Ngày 14)  
> **Trọng trách chính**: Hoàn thiện toàn bộ nội dung văn bản Chương 2 nộp cho Leader và hỗ trợ kiểm thử module bóc tách PCAP cho CLI/Web.  

---

## 📌 Trạng Thái Hiện Tại
- [x] Thu thập tập dữ liệu mẫu PCAP từ kịch bản CTU-13.
- [x] Lập trình module gom nhóm luồng truyền thông `src/data/flow_extractor.py`.
- [x] Lập trình module gán nhãn Ground-Truth `src/data/labeling.py`.
- [x] Xuất thành công tệp dữ liệu luồng hoàn chỉnh `data/processed/ctu13_labeled_flows.csv` (104.385 bản ghi).
- [ ] Soạn thảo và hoàn thiện bản thảo văn bản **Chương 2 Báo cáo**.
- [ ] Hỗ trợ Dev 1 và Dev 5 kiểm thử luồng trích xuất PCAP trực tiếp.
- [ ] Chuẩn bị bài thuyết trình 2 - 3 phút về tầng dữ liệu mạng.

---

## 🛠 Công Cụ & Tài Nguyên Cần Dùng
* **Văn bản**: Microsoft Word / Google Docs (soạn thảo báo cáo).
* **Công cụ bổ trợ**: Wireshark (chụp ảnh minh họa các gói tin PCAP để chèn vào báo cáo).
* **Mã nguồn liên quan**: `src/data/flow_extractor.py`, `src/data/labeling.py`.

---

## 💻 Nhiệm Vụ Chi Tiết Từng Ngày (To-do List)

### 1. Hỗ trợ Dev 1 và Dev 5 kiểm thử module PCAP (Hạn chót: Ngày 10)
- [ ] Phối hợp với Dev 1 để đảm bảo hàm `extract_flows(pcap_path)` trong `flow_extractor.py` có thể được gọi độc lập từ file khác mà không phát sinh lỗi đường dẫn.
- [ ] Chuẩn bị sẵn 2 file PCAP kiểm thử nhỏ (khoảng 5 - 10MB):
  * `test_clean.pcap`: Lưu lượng mạng thông thường (không nhiễm Botnet).
  * `test_botnet.pcap`: Lưu lượng mạng chứa máy tính bị nhiễm Botnet.
  *(2 file này sẽ dùng để nạp vào Web của Dev 5 và CLI của Dev 1 trong buổi bảo vệ)*.

### 2. Soạn thảo văn bản Chương 2 Báo cáo (Hạn chót: Ngày 11)
- [ ] Mở Word soạn thảo **Chương 2: TỔNG QUAN TẬP DỮ LIỆU CTU-13 VÀ PHƯƠNG PHÁP TRÍCH XUẤT ĐẶC TRƯNG TỪ PCAP** (khoảng 3 - 5 trang) theo dàn ý chuẩn mực sau:

#### Dàn ý chi tiết Chương 2:
1. **2.1 Giới thiệu tập dữ liệu chuẩn CTU-13**:
   * Xuất xứ: Do Đại học Kỹ thuật Séc (CTU) thu thập và công bố năm 2011.
   * Mô tả kịch bản được chọn trong đề tài: Tên mã độc Botnet (ví dụ Neris, Rbot...), cơ chế phát tán và hành vi độc hại.
   * Cấu trúc gói tin mạng thô: Định dạng `.pcap` chứa các frame Ethernet, header IP, TCP/UDP.
2. **2.2 Khái niệm Luồng mạng (Network Flow - 5-Tuple)**:
   * Giải thích tại sao phải gom gói tin thành luồng: Gói tin rời rạc không mang tính thống kê hành vi, luồng mạng thể hiện được bản chất của một phiên truyền thông hoàn chỉnh.
   * Định nghĩa bộ ngũ định danh luồng (5-Tuple): Địa chỉ IP nguồn, Địa chỉ IP đích, Cổng nguồn, Cổng đích, Giao thức truyền tải (TCP/UDP).
3. **2.3 Định nghĩa các đặc trưng luồng mạng được trích xuất**:
   * Lập bảng mô tả chi tiết các trường đặc trưng thống kê:
     * `flow_duration`: Thời gian tồn tại của phiên truyền thông.
     * `total_fwd_pkts`, `total_bwd_pkts`: Tổng số gói tin gửi đi và nhận về.
     * `total_fwd_bytes`, `total_bwd_bytes`: Tổng khối lượng dữ liệu trao đổi.
     * `bytes_per_sec`, `packets_per_sec`: Tốc độ truyền tải thông tin.
     * `packet_len_mean`, `packet_len_std`: Chiều dài gói tin trung bình và độ lệch chuẩn.
4. **2.4 Cơ chế gán nhãn Ground-Truth (Chân lý mặt đất)**:
   * Nêu rõ căn cứ khoa học: Dựa vào tài liệu công bố chính thức của CTU-13 (danh sách địa chỉ IP bị lây nhiễm trong phòng thí nghiệm).
   * Giải thích logic gán nhãn: Luồng có IP dính mã độc gán `label = 1` (Botnet), ngược lại gán `label = 0` (Normal).
   * Bảng thống kê sơ bộ số lượng luồng trích xuất được: Tổng số 104.385 luồng.

### 3. Nộp bản thảo và chuẩn bị thuyết trình (Hạn chót: Ngày 12 - 13)
- [ ] Gửi file Word `Chuong_2_Dev2.docx` cho Leader (Dev 1) để tổng hợp.
- [ ] Chuẩn bị nội dung nói 2 - 3 phút trong buổi bảo vệ: Tập trung giải thích cách bóc tách gói tin và cách gán nhãn chính xác.

---

## 🎯 Tiêu Chí Nghiệm Thu Sản Phẩm
- [ ] File bản thảo Chương 2 hoàn chỉnh, có bảng biểu giải thích rõ ràng, có hình ảnh minh họa gói tin từ Wireshark.
- [ ] Cung cấp đủ 2 file PCAP mẫu nhỏ để phục vụ trình diễn Live Demo.

