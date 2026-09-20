# TO-DO LIST GIAI ĐOẠN 2: DEV 3 (DATA SCIENTIST & PREPROCESSING)
# HỖ TRỢ CHUẨN HÓA SUY DIỄN & HOÀN THIỆN CHƯƠNG 3 BÁO CÁO KHOA HỌC

> **Thành viên**: Dev 3 (Chuyên viên Khám phá dữ liệu & Tiền xử lý chống rò rỉ)  
> **Giai đoạn**: Sprint 2 - Chặng về đích (Ngày 9 đến Ngày 14)  
> **Trọng trách chính**: Hoàn thiện toàn bộ nội dung văn bản Chương 3 nộp cho Leader và hỗ trợ bộ chuẩn hóa RobustScaler phục vụ suy diễn.  

---

## 📌 Trạng Thái Hiện Tại
- [x] Thực hiện phân tích khám phá dữ liệu (EDA) hoàn chỉnh trong `notebooks/eda.ipynb`.
- [x] Lập trình module `src/features/preprocessor.py` loại bỏ các trường rò rỉ thông tin (IP, Port, Timestamp).
- [x] Xử lý thành công các giá trị bất thường (`Inf`, `NaN`).
- [x] Chuẩn hóa thang đo với `RobustScaler` và phân chia tập Train/Test theo tỷ lệ 70/30 có phân tầng.
- [x] Xuất thành công `data/train_processed.csv` (73.070 dòng) và `data/test_processed.csv` (31.317 dòng).
- [ ] Soạn thảo và hoàn thiện bản thảo văn bản **Chương 3 Báo cáo**.
- [ ] Lưu trữ và đóng gói `models/scaler.joblib` phục vụ Dev 1 (CLI) và Dev 5 (Web).
- [ ] Chuẩn bị bài thuyết trình 2 - 3 phút về kỹ thuật tiền xử lý và chống Data Leakage.

---

## 🛠 Công Cụ & Tài Nguyên Cần Dùng
* **Văn bản**: Microsoft Word / Google Docs.
* **Hình ảnh số liệu**: Trích xuất các biểu đồ trực quan từ notebook `notebooks/eda.ipynb`.
* **Mã nguồn liên quan**: `src/features/preprocessor.py`, `notebooks/eda.ipynb`.

---

## 💻 Nhiệm Vụ Chi Tiết Từng Ngày (To-do List)

### 1. Đóng gói bộ chuẩn hóa `scaler.joblib` (Hạn chót: Ngày 10)
- [ ] Đảm bảo bộ chuẩn hóa `RobustScaler` đã được fit trên tập Train và lưu trữ thành file:
  📁 `models/scaler.joblib`
  *(File này là bắt buộc để Dev 1 và Dev 5 dùng chuẩn hóa dữ liệu PCAP mới khi người dùng bấm quét)*.

### 2. Soạn thảo văn bản Chương 3 Báo cáo (Hạn chót: Ngày 11)
- [ ] Mở Word soạn thảo **Chương 3: KHÁM PHÁ DỮ LIỆU (EDA), TIỀN XỬ LÝ VÀ CƠ CHẾ PHÒNG CHỐNG RÒ RỈ DỮ LIỆU (ANTI-LEAKAGE)** (khoảng 4 - 6 trang) theo dàn ý chi tiết sau:

#### Dàn ý chi tiết Chương 3:
1. **3.1 Phân tích khám phá dữ liệu (Exploratory Data Analysis - EDA)**:
   * Chèn các biểu đồ từ file `notebooks/eda.ipynb` vào báo cáo:
     * Biểu đồ tròn/cột phân bố nhãn: Nêu rõ hiện tượng **mất cân bằng lớp cực đoan (Severe Class Imbalance)**: Lớp Normal chiếm 99.95%, lớp Botnet chỉ chiếm 0.05% (34 luồng trong Train, 14 luồng trong Test).
     * Biểu đồ phân bố độ dài luồng mạng và phân bố kích thước gói tin.
   * Nhận xét về độ lệch và sự phân tán mạnh của dữ liệu mạng thực tế.
2. **3.2 Xử lý giá trị bất thường (Missing Values & Infinite Numbers)**:
   * Hiện tượng chia cho 0: Các luồng có `flow_duration = 0` dẫn đến tốc độ `bytes_per_sec` đạt giá trị vô cực (`Inf`).
   * Phương pháp xử lý: Chuyển đổi `Inf` và `-Inf` thành `NaN`, sau đó điền khuyết thiếu bằng giá trị trung vị (Median) hoặc số 0 để tránh làm sai lệch mô hình.
3. **3.3 Cơ chế phòng chống rò rỉ dữ liệu (Anti-Leakage) - Trọng tâm lý thuyết**:
   * **Vấn đề rò rỉ dữ liệu (Data Leakage) trong An toàn thông tin**: Nếu giữ lại địa chỉ IP (`src_ip`, `dst_ip`), số hiệu cổng (`port`), hoặc mốc thời gian (`timestamp`), mô hình sẽ học vẹt định danh cụ thể của máy thí nghiệm thay vì học bản chất hành vi tấn công.
   * Hậu quả nếu không loại bỏ: Độ chính xác ảo đạt 100% trong phòng thí nghiệm nhưng thất bại hoàn toàn khi triển khai trên mạng thực tế.
   * Giải pháp: Xóa bỏ triệt để toàn bộ 6 trường định danh, chỉ giữ lại các trường đặc trưng thống kê hành vi thuần túy.
4. **3.4 Chuẩn hóa dữ liệu bằng RobustScaler**:
   * Tại sao không dùng `StandardScaler` hay `MinMaxScaler`? Vì dữ liệu lưu lượng mạng chứa rất nhiều điểm ngoại lai (Outliers - các đợt bùng nổ lưu lượng, gói tin khổng lồ).
   * Cơ chế của `RobustScaler`: Chuẩn hóa dựa trên trung vị (Median) và khoảng tứ phân vị (IQR = Q3 - Q1), giúp loại bỏ ảnh hưởng tiêu cực của các giá trị ngoại lai.
5. **3.5 Chiến lược phân chia tập dữ liệu huấn luyện và kiểm thử (Train/Test Split)**:
   * Tỷ lệ phân chia: 70% Huấn luyện (73.070 dòng) - 30% Kiểm thử (31.317 dòng).
   * Kỹ thuật phân tầng (`stratify=y`): Đảm bảo tỷ lệ mẫu hiếm Botnet ở cả tập Train và tập Test đều được giữ nguyên vẹn.

### 3. Nộp bản thảo và chuẩn bị thuyết trình (Hạn chót: Ngày 12 - 13)
- [ ] Xuất file Word `Chuong_3_Dev3.docx` nộp cho Leader (Dev 1).
- [ ] Chuẩn bị bài thuyết trình 2 - 3 phút: Tập trung làm rõ lý do tại sao phải loại bỏ IP/Port và ưu điểm của RobustScaler (đây là câu hỏi giảng viên rất hay hỏi để kiểm tra hiểu biết).

---

## 🎯 Tiêu Chí Nghiệm Thu Sản Phẩm
- [ ] Bản thảo Chương 3 chi tiết, lập luận chặt chẽ, đầy đủ hình ảnh đồ thị phân tích từ notebook EDA.
- [ ] File `models/scaler.joblib` được bàn giao cho Dev 1 và Dev 5.

