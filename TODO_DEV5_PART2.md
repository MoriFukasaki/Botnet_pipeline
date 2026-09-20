# TO-DO LIST GIAI ĐOẠN 2: DEV 5 (WEB DEMO & VISUALIZATION ENGINEER)
# XÂY DỰNG WEB STREAMLIT, TRỰC QUAN HÓA SỐ LIỆU & HOÀN THIỆN CHƯƠNG 5

> **Thành viên**: Dev 5 (Kỹ sư Trực quan hóa & Giao diện ứng dụng)  
> **Giai đoạn**: Sprint 2 - Chặng về đích (Ngày 9 đến Ngày 14)  
> **Trọng trách chính**: Bước vào giai đoạn then chốt nhất - Vẽ biểu đồ đánh giá, lập trình giao diện Web Streamlit phục vụ buổi bảo vệ, và soạn thảo Chương 5 Báo cáo.  

---

## 📌 Trạng Thái Hiện Tại
- [ ] Kéo mô hình `models/best_model.joblib` và bảng điểm `benchmark_results.csv` từ nhánh `Dev4`.
- [ ] Viết script sinh 2 biểu đồ trực quan: `confusion_matrix.png` và `feature_importance.png`.
- [ ] Lập trình hoàn thiện ứng dụng Web `app.py` bằng thư viện **Streamlit**.
- [ ] Chuẩn bị kịch bản bấm Live Demo trong 3 phút trước hội đồng chấm điểm.
- [ ] Soạn thảo và hoàn thiện bản thảo văn bản **Chương 5 Báo cáo**.
- [ ] Chuẩn bị bài thuyết trình 2 - 3 phút trình diễn sản phẩm thực tế.

---

## 🛠 Công Cụ & Tài Nguyên Cần Dùng
* **Ngôn ngữ & Thư viện**: Python 3.10+, `streamlit`, `matplotlib`, `seaborn`, `pandas`, `pickle` / `joblib`.
* **Đầu vào tiếp nhận**:
  * Mô hình tối ưu `models/best_model.joblib` từ **Dev 4**.
  * Bảng số liệu `results/benchmark_results.csv` từ **Dev 4**.
  * Bộ chuẩn hóa `models/scaler.joblib` từ **Dev 3**.
  * Module trích xuất luồng `src/data/flow_extractor.py` từ **Dev 2**.
  * 2 file PCAP thử nghiệm nhỏ (`test_clean.pcap` và `test_botnet.pcap`) từ **Dev 2**.

---

## 💻 Nhiệm Vụ Chi Tiết Từng Ngày (To-do List)

### 1. Đồng bộ mã nguồn từ Dev 4 (Hạn chót: Ngày 10)
- [ ] Chuyển sang nhánh `Dev5` và kéo toàn bộ kết quả của Dev 4 về:
  ```bash
  git checkout Dev5
  git merge Dev4 -m "Merge Dev4: Lay best_model va benchmark results"
  ```

### 2. Trực quan hóa biểu đồ đánh giá (Hạn chót: Ngày 11)
- [ ] Viết script ngắn (hoặc tích hợp trong notebook) sinh 2 ảnh biểu đồ chất lượng cao lưu vào thư mục `results/`:
  1. `results/confusion_matrix.png`:
     * Vẽ Ma trận nhầm lẫn (Confusion Matrix) dạng biểu đồ nhiệt (Heatmap) bằng `seaborn.heatmap`.
     * Thể hiện rõ 4 chỉ số: True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN).
  2. `results/feature_importance.png`:
     * Đọc thuộc tính `feature_importances_` từ mô hình Random Forest.
     * Vẽ biểu đồ thanh ngang (Horizontal Bar Chart) Top 10 đặc trưng luồng mạng có trọng số ảnh hưởng lớn nhất đến quyết định phát hiện Botnet.
- [ ] Gửi ngay 2 ảnh này cho Dev 1 để chèn vào Slide và Báo cáo.

### 3. Lập trình ứng dụng Web `app.py` bằng Streamlit (Hạn chót: Ngày 12)
- [ ] Cài đặt Streamlit nếu chưa có: `pip install streamlit`.
- [ ] Xây dựng giao diện web trong file `app.py` với cấu trúc 2 Tab trực quan:
  * **Thanh Sidebar bên trái**:
    * Tiêu đề: *Hệ thống Phát hiện Botnet từ Lưu lượng mạng PCAP*.
    * Thông tin nhóm nghiên cứu, mô hình AI đang kích hoạt (`best_model.joblib`).
  * **Tab 1 - Dashboard Đánh Giá Hiệu Năng**:
    * Hiển thị bảng so sánh 4 mô hình học máy từ file `results/benchmark_results.csv`.
    * Hiển thị 2 biểu đồ: Ma trận nhầm lẫn (`confusion_matrix.png`) và Tầm quan trọng của đặc trưng (`feature_importance.png`).
  * **Tab 2 - Trình Quét Trực Tiếp (Live PCAP Scanner)**:
    * Khung tải tệp (File Uploader) cho phép người dùng chọn file `.pcap` hoặc chọn nhanh file mẫu có sẵn.
    * Nút điều khiển: `[🚀 Phân tích lưu lượng]`.
    * Khi bấm nút:
      * Gọi module của Dev 2 để trích xuất các luồng mạng.
      * Gọi scaler của Dev 3 để chuẩn hóa thang đo.
      * Nạp `best_model.joblib` để phân loại từng luồng mạng (0: Normal, 1: Botnet).
    * Hiển thị kết quả trực quan (Metric Cards):
      * Tổng số luồng mạng đã phân tích.
      * Số luồng bị phát hiện là Botnet.
      * Tỷ lệ lây nhiễm (%).
    * **Bảng cảnh báo chi tiết**: Liệt kê danh sách các địa chỉ IP nguồn (`src_ip`) và IP đích (`dst_ip`) của các luồng độc hại để chuyên viên SOC tiến hành cách ly.

### 4. Chuẩn bị kịch bản bấm Live Demo (Hạn chót: Ngày 13)
- [ ] Kiểm tra chạy thử web: `streamlit run app.py`.
- [ ] Chuẩn bị sẵn kịch bản 3 phút thao tác mẫu để trình diễn trước giảng viên:
  * *Phút 1*: Mở Tab Dashboard, giới thiệu tổng quan hiệu năng các mô hình.
  * *Phút 2*: Sang Tab Live Scanner, tải file `test_clean.pcap` lên $\rightarrow$ Hệ thống báo 0% Botnet (Hệ thống an toàn).
  * *Phút 3*: Tải tiếp file `test_botnet.pcap` lên $\rightarrow$ Hệ thống phát hiện ngay lập tức các luồng Botnet và bôi đỏ danh sách IP độc hại $\rightarrow$ Thuyết phục giảng viên tuyệt đối!

### 5. Soạn thảo văn bản Chương 5 Báo cáo (Hạn chót: Ngày 13)
- [ ] Mở Word soạn thảo **Chương 5: TRIỂN KHAI ỨNG DỤNG WEB DEMO VÀ THỰC NGHIỆM TRỰC QUAN HÓA** (khoảng 3 - 5 trang):
  * Giới thiệu kiến trúc ứng dụng Web Streamlit.
  * Chụp ảnh màn hình giao diện Dashboard và giao diện Live Scanner.
  * Hướng dẫn chi tiết quy trình vận hành hệ thống phát hiện Botnet.
  * Phân tích ý nghĩa của biểu đồ Ma trận nhầm lẫn và biểu đồ Mức độ quan trọng của đặc trưng.
- [ ] Gửi file Word `Chuong_5_Dev5.docx` cho Leader (Dev 1).

---

## 🎯 Tiêu Chí Nghiệm Thu Sản Phẩm
- [ ] Ứng dụng Web `app.py` khởi động mượt mà bằng lệnh `streamlit run app.py`, không phát sinh lỗi khi upload file PCAP.
- [ ] Đầy đủ 2 ảnh biểu đồ chất lượng cao trong thư mục `results/`.
- [ ] Kịch bản Live Demo chuẩn bị kỹ lưỡng, sẵn sàng trình diễn trước hội đồng.
- [ ] Bản thảo Chương 5 hoàn chỉnh, chụp ảnh minh họa giao diện rõ nét.

