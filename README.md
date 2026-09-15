# Botnet_sexline
# BẢNG PHÂN CÔNG NHIỆM VỤ & MA TRẬN TRÁCH NHIỆM (5 THÀNH VIÊN)

**Đề tài**: Xây dựng Pipeline trích xuất đặc trưng và phát hiện Botnet từ lưu lượng mạng PCAP  
**Môn học**: Ứng dụng Học máy trong An toàn thông tin (Machine Learning for Cybersecurity)  
**Thời gian thực hiện**: 5 tuần  

---

## 1. Triết lý phân chia công việc tối ưu (Giảm tải & Cân bằng thực tế)
- **Cắt bỏ hoàn toàn Deep Learning (MLP/CNN)**: Với bài toán dữ liệu luồng mạng dạng bảng (Tabular Features), các mô hình cây như Random Forest, Gradient Boosting cho hiệu quả vượt trội hơn Deep Learning, huấn luyện cực nhanh và không lo lỗi cài đặt PyTorch/GPU.
- **Cắt bỏ SHAP phức tạp**: Chỉ sử dụng thuộc tính có sẵn `feature_importances_` của Random Forest (vừa trực quan, vừa nhẹ nhàng).
- **Tách bạch rõ ràng giữa Backend ML (Người 4) và Trình diễn Web Demo (Người 5)**:
  - *Thành viên 4*: Chỉ tập trung huấn luyện 3 thuật toán Scikit-Learn quen thuộc, xuất bảng điểm số.
  - *Thành viên 5*: Chỉ tập trung dựng giao diện Web Streamlit (viết nhanh, trực quan, không phải đụng tới toán học/thuật toán phức tạp).
- **Leader (Thành viên 1)**: Đỡ thêm phần viết script CLI suy diễn (`detect.py`), kết nối pipeline và làm Báo cáo + Slide.

---

## 2. Bảng Phân Công Công Việc Đã Tinh Gọn

### Thành viên 1: Leader (System Architect & Integration)
- **Nhiệm vụ cụ thể**:
  1. Quản lý Git repository, thống nhất định dạng file giữa các bạn.
  2. Viết script điều phối chính `scripts/run_pipeline.py` để kết nối toàn bộ hệ thống.
  3. Viết script CLI suy diễn cảnh báo `src/inference/detect.py` (đỡ việc cho TV4/TV5).
  4. Đảm nhận viết phần khung sườn Báo cáo tổng kết và Slide thuyết trình.
- **Đánh giá tải việc**: **Rất nhẹ về code**, tập trung quản lý và tổng hợp.

### Thành viên 2: Data & PCAP Engineer (PCAP Processing & Labeling)
- **Nhiệm vụ cụ thể**:
  1. Tải file PCAP mẫu (CTU-13) hoặc dùng bộ sinh PCAP giả lập.
  2. Lập trình module gom luồng và trích xuất đặc trưng `src/data/flow_extractor.py`.
  3. Lập trình gán nhãn ground-truth `src/data/labeling.py` (so khớp IP nhiễm Botnet).
  4. Xuất ra file dữ liệu `ctu13_labeled_flows.csv`.
- **Đánh giá tải việc**: **Vừa phải**, chỉ làm việc với file PCAP và Scapy.

### Thành viên 3: Data Scientist (EDA, Preprocessing & Anti-Leakage)
- **Nhiệm vụ cụ thể**:
  1. Thực hiện phân tích khám phá (EDA) trong Jupyter Notebook (vẽ phân bố nhãn, độ dài luồng).
  2. Lập trình `src/features/preprocessor.py`: điền giá trị thiếu (NaN), xử lý Inf.
  3. **Loại bỏ các cột gây rò rỉ dữ liệu (IP, Port, Timestamp)**.
  4. Chuẩn hóa dữ liệu bằng `RobustScaler` và phân chia tập Train/Test (70/30).
- **Đánh giá tải việc**: **Vừa phải**, chuyên tâm xử lý dữ liệu sạch.

### Thành viên 4: Machine Learning Engineer (Core ML Models) - *ĐÃ GIẢM TẢI*
- **Nhiệm vụ cụ thể**:
  1. Lập trình `src/models/train.py` huấn luyện 3 mô hình cơ bản của Scikit-Learn:
     - Logistic Regression (Mô hình cơ sở)
     - Decision Tree (Cây quyết định)
     - Random Forest (Rừng ngẫu nhiên)
  2. Đo đạc các chỉ số đánh giá: Accuracy, Precision, Recall, F1-Score, FPR.
  3. Xuất bảng điểm số so sánh ra file CSV và lưu file `best_model.joblib`.
  4. *(Đã bỏ: Deep Learning, Optuna tuning, SHAP values phức tạp)*.
- **Đánh giá tải việc**: **Nhẹ nhàng, vừa sức**, chỉ dùng API Scikit-Learn có sẵn.

### Thành viên 5: Web Demo & Visualization Engineer - *ĐÃ GIẢM TẢI*
- **Nhiệm vụ cụ thể**:
  1. Vẽ biểu đồ Ma trận nhầm lẫn (Confusion Matrix) và Feature Importance từ kết quả của TV4.
  2. Lập trình giao diện Web Demo bằng **Streamlit (`app.py`)**:
     - Cho phép chọn file PCAP hoặc upload file.
     - Bấm nút phân tích: hiển thị tỷ lệ Botnet và bảng danh sách IP nghi vấn.
  3. Chuẩn bị kịch bản bấm demo trực tiếp trước giảng viên trong buổi bảo vệ.
  4. *(Đã bỏ: Không phải code Deep Learning hay huấn luyện mạng nơ-ron)*.
- **Đánh giá tải việc**: **Nhẹ nhàng, thú vị**, Streamlit có sẵn component UI, không cần HTML/CSS.

---

## 3. Ma Trận Trách Nhiệm RACI (Đã Tinh Chỉnh Cân Bằng)

| Hạng mục công việc | TV1 (Leader) | TV2 (PCAP) | TV3 (Data Clean) | TV4 (ML Core) | TV5 (Web Demo) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1. Khởi tạo Git & Quản lý tiến độ | **A / R** | I | I | I | I |
| 2. Trích xuất đặc trưng luồng từ PCAP | I | **A / R** | C | I | I |
| 3. Gán nhãn Botnet vs Normal | I | **A / R** | C | I | I |
| 4. Tiền xử lý dữ liệu & Chống Leakage | I | C | **A / R** | C | I |
| 5. Chuẩn hóa & Train/Test Split | I | I | **A / R** | C | I |
| 6. Huấn luyện 3 mô hình ML (LR, DT, RF) | I | I | C | **A / R** | I |
| 7. Đo đạc F1, Precision, Recall, FPR | I | I | I | **A / R** | C |
| 8. Vẽ Confusion Matrix & Bar Charts | I | I | I | C | **A / R** |
| 9. Lập trình Web Demo Streamlit (`app.py`) | C | I | I | I | **A / R** |
| 10. Viết CLI suy diễn (`detect.py`) | **A / R** | C | C | C | C |
| 11. Tích hợp Pipeline (`run_pipeline.py`) | **A / R** | C | C | C | C |
| 12. Soạn thảo Báo cáo tổng kết (Word/LaTeX) | **A / R** | R (Chương 2) | R (Chương 3) | R (Chương 4) | R (Chương 5) |
| 13. Thiết kế Slide & Kịch bản thuyết trình | **A / R** | C | C | C | C |


