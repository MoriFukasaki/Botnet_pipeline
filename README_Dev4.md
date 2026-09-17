# Botnet_sexline

## Mô hình hiện tại trên branch `Dev4`

Đây là pipeline machine learning thử nghiệm để phân loại dữ liệu luồng mạng thành hai nhãn:

- `0`: Normal
- `1`: Botnet

Pipeline nhận hai file CSV đã được tiền xử lý, trong đó cột `label` là nhãn mục tiêu và các cột còn lại là đặc trưng số. Mã hiện tại nằm tại [`src/models/train.py`](src/models/train.py).

## Những gì mô hình có thể làm

- Đọc dữ liệu train/test từ `data/processed/train_data.csv` và `data/processed/test_data.csv`.
- Tự động tạo dữ liệu giả lập nếu hai file đầu vào chưa tồn tại, giúp kiểm tra pipeline trước khi có dữ liệu thật.
- Huấn luyện và so sánh 4 mô hình:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - MLP Neural Network
- Dự đoán nhãn Botnet/Normal trên tập test.
- Tính các chỉ số `Accuracy`, `Precision`, `Recall`, `F1-Score` và `FPR`.
- Chọn mô hình có `F1-Score` cao nhất và lưu lại để dùng cho bước suy luận sau.
- Xuất bảng kết quả so sánh ra CSV.

## Cách chạy

Từ thư mục gốc của repository:

```bash
python src/models/train.py
```

Sau khi chạy xong, pipeline tạo hoặc cập nhật:

```text
models/best_model.joblib
results/benchmark_results.csv
```

File `best_model.joblib` chứa mô hình có F1-Score cao nhất. File benchmark có các cột:
`Model`, `Accuracy`, `Precision`, `Recall`, `F1-Score`, `FPR`.

## Kết quả benchmark hiện tại

Kết quả đang lưu trong `results/benchmark_results.csv`:

| Model | Accuracy | Precision | Recall | F1-Score | FPR |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Logistic Regression | 0.7125 | 0.3333 | 0.0455 | 0.0800 | 0.0345 |
| Decision Tree | 0.6000 | 0.2917 | 0.3182 | 0.3043 | 0.2931 |
| Random Forest | 0.6250 | 0.0000 | 0.0000 | 0.0000 | 0.1379 |
| MLP (Neural Network) | 0.6625 | 0.3810 | 0.3636 | 0.3721 | 0.2241 |

Theo tiêu chí chọn F1-Score, kết quả hiện tại chọn **MLP (Neural Network)** làm `best_model`.

## Giới hạn hiện tại

- Mô hình chỉ nhận các vector đặc trưng số trong CSV; chưa đọc trực tiếp file PCAP.
- Chưa có script CLI để dự đoán trên dữ liệu mới và chưa có giao diện Streamlit trong branch này.
- Các đặc trưng đầu vào khi suy luận phải có cùng số lượng và thứ tự như lúc huấn luyện.
- Nếu thiếu dữ liệu đầu vào, dữ liệu giả lập được tạo ngẫu nhiên. Kết quả từ dữ liệu giả lập chỉ dùng để kiểm tra code, không đại diện cho hiệu năng phát hiện Botnet thực tế.
- `best_model.joblib` hiện được ghi bằng cơ chế pickle của Python; chỉ nên tải các file model đáng tin cậy.

## Cấu trúc liên quan

```text
data/processed/train_data.csv  # Dữ liệu huấn luyện
data/processed/test_data.csv   # Dữ liệu đánh giá
models/best_model.joblib        # Mô hình tốt nhất
results/benchmark_results.csv   # Kết quả so sánh các mô hình
src/models/train.py             # Script huấn luyện và đánh giá
```


