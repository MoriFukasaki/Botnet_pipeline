# BOTNET DETECTION PIPELINE (BOTNET_PIPELINE)
# BẢNG PHÂN CÔNG NHIỆM VỤ & MA TRẬN TRÁCH NHIỆM (5 THÀNH VIÊN)

**Đề tài**: Xây dựng Pipeline trích xuất đặc trưng và phát hiện Botnet từ lưu lượng mạng PCAP  
**Môn học**: Ứng dụng Học máy trong An toàn thông tin (Machine Learning for Cybersecurity)  
**Thời gian thực hiện**: 5 tuần  

---

## 1. Định hướng Triển khai & Tối ưu Hóa Dự án
- **Lựa chọn mô hình dạng bảng (Tabular Features)**: Đối với bài toán dữ liệu luồng mạng có cấu trúc dạng bảng, các mô hình học máy dạng cây (Random Forest, Decision Tree) mang lại hiệu quả cao, tốc độ hội tụ nhanh và tối ưu tài nguyên tính toán hơn so với Deep Learning.
- **Trực quan hóa độ quan trọng của đặc trưng**: Khai thác trực tiếp thuộc tính `feature_importances_` của mô hình Random Forest để đánh giá các đặc trưng đóng góp lớn nhất vào việc phân loại hành vi Botnet.
- **Phân tách chuyên môn hóa giữa ML Core (Dev 4) và Ứng dụng Web (Dev 5)**:
  - *Dev 4*: Tập trung tối ưu và đánh giá các thuật toán học máy, xuất bảng so sánh số liệu thực nghiệm.
  - *Dev 5*: Xây dựng giao diện Web (Streamlit) phục vụ việc trực quan hóa kết quả và trình diễn kịch bản quét lưu lượng mạng thực tế.
- **Leader (Dev 1)**: Đảm nhận phát triển công cụ dòng lệnh suy diễn (`detect.py`), kết nối luồng xử lý tự động toàn hệ thống và chủ trì biên tập Báo cáo + Slide.

---

## 2. Bảng Phân Công Công Việc Chi Tiết (Dev 1 - Dev 5)

### Dev 1: Leader (System Architect & Integration)
- **Nhiệm vụ cụ thể**:
  1. Quản trị Git repository, quy chuẩn cấu trúc thư mục và định dạng trao đổi dữ liệu.
  2. Xây dựng script điều phối tự động `scripts/run_pipeline.py` kết nối toàn bộ hệ thống.
  3. Lập trình công cụ dòng lệnh suy diễn cảnh báo `src/inference/detect.py`.
  4. Chủ trì biên soạn khung Báo cáo tổng kết và Slide thuyết trình báo cáo.
- **Đánh giá tải việc**: Tập trung vào kiến trúc hệ thống, tích hợp và điều phối tiến độ.

### Dev 2: Data & PCAP Engineer (PCAP Processing & Labeling)
- **Nhiệm vụ cụ thể**:
  1. Thu thập dữ liệu PCAP chuẩn (CTU-13) và thiết lập môi trường xử lý lưu lượng mạng.
  2. Lập trình module gom luồng và trích xuất đặc trưng mạng `src/data/flow_extractor.py`.
  3. Lập trình gán nhãn dữ liệu chuẩn `src/data/labeling.py` (đối chiếu danh sách IP Botnet).
  4. Xuất tập dữ liệu luồng hoàn chỉnh `ctu13_labeled_flows.csv`.
- **Đánh giá tải việc**: Chuyên trách tầng thu thập và xử lý dữ liệu gói tin mạng thô.

### Dev 3: Data Scientist (EDA, Preprocessing & Anti-Leakage)
- **Nhiệm vụ cụ thể**:
  1. Khảo sát và phân tích khám phá dữ liệu (EDA) trong Jupyter Notebook.
  2. Lập trình module `src/features/preprocessor.py`: xử lý giá trị khuyết thiếu (NaN) và ngoại lai (Inf).
  3. **Loại bỏ triệt để các đặc trưng rò rỉ dữ liệu (IP, Port, Timestamp - Anti-Leakage)**.
  4. Chuẩn hóa dữ liệu với `RobustScaler` và phân chia tập dữ liệu Train/Test (70/30) có phân tầng.
- **Đánh giá tải việc**: Đảm bảo chất lượng dữ liệu sạch và tính khách quan của bài toán ML.

### Dev 4: Machine Learning Engineer (Core ML Models & Evaluation)
- **Nhiệm vụ cụ thể**:
  1. Lập trình script `src/models/train.py` huấn luyện các thuật toán học máy:
     - Logistic Regression (Mô hình cơ sở - Baseline)
     - Decision Tree (Cây quyết định)
     - Random Forest (Rừng ngẫu nhiên)
     - Multi-Layer Perceptron (MLP - Mạng nơ-ron đa tầng)
  2. Đo đạc các chỉ số đo lường: Accuracy, Precision, Recall, F1-Score và False Positive Rate (FPR).
  3. Xuất bảng tổng hợp so sánh vào `results/benchmark_results.csv` và lưu trữ `models/best_model.joblib`.
- **Đánh giá tải việc**: Chuyên trách thuật toán học máy và phân tích hiệu năng mô hình.

### Dev 5: Web Demo & Visualization Engineer (Visualization & Streamlit UI)
- **Nhiệm vụ cụ thể**:
  1. Thiết kế biểu đồ Ma trận nhầm lẫn (Confusion Matrix) và Biểu đồ mức độ quan trọng đặc trưng (Feature Importance).
  2. Lập trình giao diện Web Demo bằng **Streamlit (`app.py`)**:
     - Cho phép chọn file PCAP hoặc tải tệp mới lên hệ thống.
     - Phân tích và hiển thị tỷ lệ lây nhiễm kèm bảng danh sách các địa chỉ IP bị nghi vấn.
  3. Xây dựng kịch bản trình diễn tương tác trực tiếp trong buổi bảo vệ đề tài.
- **Đánh giá tải việc**: Chuyên trách trải nghiệm người dùng và trực quan hóa sản phẩm.

---

## 3. Ma Trận Trách Nhiệm RACI Chuẩn Hóa

| Hạng mục công việc | Dev 1 (Leader) | Dev 2 (PCAP) | Dev 3 (Data Clean) | Dev 4 (ML Core) | Dev 5 (Web Demo) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1. Khởi tạo Git & Quản lý tiến độ | **A / R** | I | I | I | I |
| 2. Trích xuất đặc trưng luồng từ PCAP | I | **A / R** | C | I | I |
| 3. Gán nhãn Botnet vs Normal | I | **A / R** | C | I | I |
| 4. Tiền xử lý dữ liệu & Chống Data Leakage | I | C | **A / R** | C | I |
| 5. Chuẩn hóa & Phân chia Train/Test | I | I | **A / R** | C | I |
| 6. Huấn luyện các mô hình ML | I | I | C | **A / R** | I |
| 7. Đo đạc F1, Precision, Recall, FPR | I | I | I | **A / R** | C |
| 8. Trực quan hóa Ma trận nhầm lẫn & Đặc trưng | I | I | I | C | **A / R** |
| 9. Lập trình Web Demo Streamlit (`app.py`) | C | I | I | I | **A / R** |
| 10. Xây dựng công cụ CLI suy diễn (`detect.py`) | **A / R** | C | C | C | C |
| 11. Tích hợp Pipeline tự động (`run_pipeline.py`) | **A / R** | C | C | C | C |
| 12. Soạn thảo Báo cáo tổng kết khoa học | **A / R** | R (Chương 2) | R (Chương 3) | R (Chương 4) | R (Chương 5) |
| 13. Thiết kế Slide & Kịch bản thuyết trình | **A / R** | C | C | C | C |

*(Quy ước RACI: **A** - Accountable (Chịu trách nhiệm chính), **R** - Responsible (Người thực hiện), **C** - Consulted (Tham vấn), **I** - Informed (Nhận thông tin))*.
