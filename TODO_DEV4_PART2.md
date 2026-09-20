# TO-DO LIST GIAI ĐOẠN 2: DEV 4 (MACHINE LEARNING ENGINEER)
# ĐỒNG BỘ MÔ HÌNH LÊN GIT & HOÀN THIỆN CHƯƠNG 4 BÁO CÁO KHOA HỌC

> **Thành viên**: Dev 4 (Kỹ sư Học máy & Đánh giá mô hình)  
> **Giai đoạn**: Sprint 2 - Chặng về đích (Ngày 9 đến Ngày 14)  
> **Trọng trách chính**: Đẩy kết quả mô hình đã huấn luyện lên Git, bàn giao sản phẩm cho Dev 1 & Dev 5, và soạn thảo toàn bộ Chương 4 Báo cáo.  

---

## 📌 Trạng Thái Hiện Tại
- [x] Lập trình script huấn luyện và đánh giá `src/models/train.py`.
- [x] Merge dữ liệu sạch từ nhánh `Dev3` sang nhánh `Dev4` thành công (commit `5fbcdd8`).
- [x] Huấn luyện hoàn tất 4 mô hình: Logistic Regression, Decision Tree, Random Forest, MLP trên 73.070 dòng dữ liệu thật.
- [x] Xuất bảng kết quả thực nghiệm `results/benchmark_results.csv` và mô hình tối ưu `models/best_model.joblib`.
- [ ] Push các tệp kết quả và mã nguồn cập nhật lên GitHub remote (`origin/Dev4`).
- [ ] Thông báo cho Dev 1 và Dev 5 kéo mã nguồn về tích hợp.
- [ ] Soạn thảo và hoàn thiện bản thảo văn bản **Chương 4 Báo cáo**.
- [ ] Chuẩn bị bài thuyết trình 2 - 3 phút về phần Machine Learning.

---

## 🛠 Công Cụ & Tài Nguyên Cần Dùng
* **Mã nguồn**: `src/models/train.py`, `models/best_model.joblib`, `results/benchmark_results.csv`.
* **Văn bản**: Microsoft Word / Google Docs (soạn thảo báo cáo).
* **Kiến thức trọng tâm**: 4 thuật toán ML, bài toán mất cân bằng dữ liệu cực đoan, chỉ số F1-Score & FPR.

---

## 💻 Nhiệm Vụ Chi Tiết Từng Ngày (To-do List)

### 1. Đẩy mã nguồn và kết quả lên GitHub (Hạn chót: Ngày 10 - Thực hiện ngay)
- [ ] Mở Terminal trên nhánh `Dev4` và gõ lệnh lưu trữ, đẩy kết quả lên remote:
  ```bash
  git add models/best_model.joblib results/benchmark_results.csv src/models/train.py
  git commit -m "Dev4: Hoan thanh huan luyen tren du lieu that va xuat best_model"
  git push origin Dev4
  ```
- [ ] Nhắn tin vào nhóm thông báo cho Dev 1 và Dev 5:
  > *"Dev 4 đã hoàn tất huấn luyện trên dữ liệu thật và đẩy lên nhánh `Dev4`. Dev 1 và Dev 5 kéo nhánh `Dev4` về để lấy `best_model.joblib` và `benchmark_results.csv` nhé!"*

### 2. Soạn thảo văn bản Chương 4 Báo cáo (Hạn chót: Ngày 12)
- [ ] Mở Word soạn thảo **Chương 4: HUẤN LUYỆN, ĐÁNH GIÁ VÀ LỰA CHỌN MÔ HÌNH HỌC MÁY TRONG PHÁT HIỆN BOTNET** (khoảng 4 - 6 trang) theo dàn ý chuẩn sau:

#### Dàn ý chi tiết Chương 4:
1. **4.1 Tổng quan lý thuyết 4 thuật toán Học máy**:
   * **Logistic Regression**: Mô hình tuyến tính cơ sở (Baseline), tính toán xác suất dựa trên hàm Sigmoid. Ưu điểm tốc độ cực nhanh, dễ giải thích.
   * **Decision Tree (Cây quyết định)**: Phân nhánh dựa trên chỉ số Gini Impurity hoặc Entropy. Trực quan hóa luật phân loại tốt nhưng dễ bị học vẹt (Overfitting).
   * **Random Forest (Rừng ngẫu nhiên)**: Thuật toán Ensemble học kết hợp (Bagging), tạo ra 100 cây quyết định độc lập và biểu quyết đa số. Khắc phục triệt để Overfitting, độ ổn định cao trên dữ liệu bảng.
   * **Multi-Layer Perceptron (MLP - Mạng nơ-ron đa tầng)**: Mạng nơ-ron truyền thẳng (Feedforward Neural Network) với các tầng ẩn (Hidden Layers), có khả năng mô hình hóa mối quan hệ phi tuyến phức tạp.
2. **4.2 Thách thức Mất cân bằng dữ liệu cực đoan (Severe Imbalanced Classification)**:
   * Thực trạng: Trong 73.070 luồng của tập Train chỉ có đúng 34 luồng Botnet (~0.05%).
   * "Cạm bẫy độ chính xác" (Accuracy Paradox): Nếu mô hình chỉ đoán bừa toàn bộ là sạch (Normal), độ chính xác vẫn đạt 99.95%, nhưng tỷ lệ phát hiện Botnet bằng 0%!
   * Giải pháp kỹ thuật: Áp dụng cơ chế phạt trọng số `class_weight='balanced'` để ép thuật toán chú trọng hơn vào các mẫu Botnet hiếm hoi.
3. **4.3 Các chỉ số đánh giá chuyên biệt trong An toàn thông tin**:
   * Giải thích tại sao không dùng Accuracy mà phải dùng:
     * **Recall (Độ nhạy)**: Đo lường tỷ lệ bắt trúng Botnet (bỏ sót 1 con Botnet có thể làm sập toàn bộ hệ thống).
     * **Precision (Độ chính xác)**: Đo lường mức độ tin cậy khi mô hình phát ra cảnh báo.
     * **F1-Score**: Trung bình điều hòa giữa Precision và Recall.
     * **False Positive Rate (FPR - Tỷ lệ báo động giả)**: $\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}$. Trong vận hành SOC, nếu FPR cao sẽ làm tràn ngập cảnh báo rác, gây kiệt sức cho kỹ sư an ninh.
4. **4.4 Phân tích kết quả thực nghiệm**:
   * Dán bảng số liệu từ file `results/benchmark_results.csv` vào báo cáo:
     ```text
                    Model  Accuracy  Precision  Recall  F1-Score      FPR
      Logistic Regression    0.7939     0.0019  0.8571    0.0037 0.206089
            Decision Tree    0.9862     0.0094  0.2857    0.0181 0.013514
            Random Forest    0.9961     0.0000  0.0000    0.0000 0.003482
     MLP (Neural Network)    0.9996     0.0000  0.0000    0.0000 0.000000
     ```
   * So sánh và nhận xét ưu nhược điểm thực tế của từng mô hình trên dữ liệu mạng thật.
5. **4.5 Biện luận lý do lựa chọn mô hình tối ưu để triển khai**:
   * Giải thích lý do lựa chọn mô hình để đóng gói vào `models/best_model.joblib`: Cân bằng giữa khả năng bắt trúng Botnet cao nhất (Recall) và việc kiểm soát báo động giả.

### 3. Nộp bản thảo và chuẩn bị thuyết trình (Hạn chót: Ngày 13)
- [ ] Gửi file Word `Chuong_4_Dev4.docx` cho Leader (Dev 1).
- [ ] Chuẩn bị bài thuyết trình 2 - 3 phút: Nêu bật được bài toán mất cân bằng lớp cực đoan và ý nghĩa thực tế của chỉ số FPR/Recall trong phòng thủ mạng.

---

## 🎯 Tiêu Chí Nghiệm Thu Sản Phẩm
- [ ] Nhánh `Dev4` trên GitHub có đầy đủ `models/best_model.joblib` và `benchmark_results.csv`.
- [ ] File bản thảo Chương 4 hoàn chỉnh, có bảng biểu so sánh và lập luận bảo mật thuyết phục.

