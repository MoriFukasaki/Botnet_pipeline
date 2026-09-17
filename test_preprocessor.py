import numpy as np
import pandas as pd
from src.features.preprocessor import NetworkPreprocessor

# Tạo dữ liệu giả lập mạng
data = {
    'src_ip': ['192.168.1.10', '10.0.0.5', '172.16.0.2', '192.168.1.15', '10.0.0.8'],
    'dst_ip': ['8.8.8.8', '1.1.1.1', '8.8.8.8', '192.168.1.1', '10.0.0.1'],
    'src_port': [1234, 5678, 8080, 443, 80],
    'dst_port': [80, 443, 53, 8080, 443],
    'timestamp': [1600000000, 1600000001, 1600000002, 1600000003, 1600000004],
    'packet_rate': [100.5, np.inf, np.nan, 250.0, 15.2],
    'flow_duration': [1.2, 3.4, 5.6, 0.5, 2.1],
    'label': [0, 1, 0, 1, 0]
}
df_mock = pd.DataFrame(data)

print("--- DỮ LIỆU GỐC ---")
print(df_mock.head())

preprocessor = NetworkPreprocessor()
X, y = preprocessor.preprocess_pipeline(df_mock, target_col='label')

print("\n--- SAU KHI XỬ LÝ (Đã lọc IP, Port, Timestamp, NaN, Inf) ---")
print(X.head())

X_train, X_test, y_train, y_test = preprocessor.split_and_scale(X, y, test_size=0.4)
print(f"\nKích thước X_train: {X_train.shape}")
print(f"Kích thước X_test: {X_test.shape}")
print("\n✅ Test module thành công xuất sắc!")