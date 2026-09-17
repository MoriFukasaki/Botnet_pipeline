import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler

class NetworkPreprocessor:
    def __init__(self):
        self.scaler = RobustScaler()
        # Danh sách các đặc trưng dễ gây rò rỉ dữ liệu (Anti-Leakage)
        self.leakage_columns = [
            'src_ip', 'dst_ip', 'source_ip', 'destination_ip',
            'src_port', 'dst_port', 'source_port', 'destination_port',
            'timestamp', 'time', 'flow_id', 'label_string'
        ]

    def remove_leakage(self, df: pd.DataFrame) -> pd.DataFrame:
        """Loại bỏ triệt để các đặc trưng rò rỉ dữ liệu."""
        cols_to_drop = [col for col in self.leakage_columns if col in df.columns]
        df_cleaned = df.drop(columns=cols_to_drop)
        return df_cleaned

    def handle_missing_and_inf(self, df: pd.DataFrame) -> pd.DataFrame:
        """Xử lý giá trị khuyết thiếu (NaN) và vô cùng (Inf)."""
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.fillna(0, inplace=True)
        return df

    def preprocess_pipeline(self, df: pd.DataFrame, target_col: str):
        """Pipeline thực hiện toàn bộ quy trình tiền xử lý."""
        df = self.handle_missing_and_inf(df)
        df = self.remove_leakage(df)
        
        if target_col in df.columns:
            X = df.drop(columns=[target_col])
            y = df[target_col]
        else:
            raise ValueError(f"Không tìm thấy cột nhãn '{target_col}' trong DataFrame.")
            
        return X, y

    def split_and_scale(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.3):
        """Phân chia tập dữ liệu Train/Test (70/30) có phân tầng và chuẩn hóa bằng RobustScaler."""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, stratify=y, random_state=42
        )
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled, y_train, y_test