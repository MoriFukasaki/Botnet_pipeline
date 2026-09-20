import os
import pickle
import warnings
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings("ignore")

def calculate_fpr(y_true, y_pred):
    """
    Tính False Positive Rate (FPR - Tỷ lệ báo động giả):
    FPR = FP / (FP + TN)
    """
    cm = metrics.confusion_matrix(y_true, y_pred)
    if cm.size == 4:
        tn, fp, fn, tp = cm.ravel()
        return float(fp / (fp + tn)) if (fp + tn) > 0 else 0.0
    return 0.0

def load_or_create_data(train_path: str, test_path: str):
    """
    Load dữ liệu từ dev 3.
    Nếu Dev 3 chưa làm xong, tự động sinh dữ liệu giả lập (Dummy) để Dev 4 test code trước.
    """
    if not os.path.exists(train_path) or not os.path.exists(test_path):
        print(f"[!] Chua tim thay du lieu tu Dev 3 ({train_path}).")
        print("[*] Dang tu dong tao 200 dong du lieu gia lap de test...")
        
        os.makedirs(os.path.dirname(train_path), exist_ok=True)
        feature_cols = [f"feature_{i}" for i in range(10)]
        
        # Tạo dữ liệu train giả lập
        dummy_train = pd.DataFrame(np.random.randn(200, 10), columns=feature_cols)
        dummy_train["label"] = np.random.choice([0, 1], size=200, p=[0.7, 0.3])
        dummy_train.to_csv(train_path, index=False)
        
        # Tạo dữ liệu test giả lập
        dummy_test = pd.DataFrame(np.random.randn(80, 10), columns=feature_cols)
        dummy_test["label"] = np.random.choice([0, 1], size=80, p=[0.7, 0.3])
        dummy_test.to_csv(test_path, index=False)
        print("[+] Da tao du lieu gia lap thanh cong. San sang chay!")

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    X_train = train_df.drop(columns=["label"])
    y_train = train_df["label"]
    X_test = test_df.drop(columns=["label"])
    y_test = test_df["label"]
    
    return X_train, y_train, X_test, y_test

def train_and_evaluate():
    print("==========================================================")
    print("BAT DAU HUAN LUYEN VA DANH GIA MO HINH")
    print("==========================================================\n")

    train_path = "data/train_processed.csv"
    test_path = "data/test_processed.csv"

    X_train, y_train, X_test, y_test = load_or_create_data(train_path, test_path)
    print(f"[*] Kich thuoc tap Train: {X_train.shape}, Tap Test: {X_test.shape}")

    # Danh sách các mô hình huấn luyện
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=10, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1),
        "MLP (Neural Network)": MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42)
    }

    results = []
    best_f1 = -1.0
    best_model = None
    best_model_name = ""

    print("\n--- BAT DAU TRAINING & CHAM DIEM ---")
    for name, model in models.items():
        print(f"[*] Dang huan luyen: {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = metrics.accuracy_score(y_test, y_pred)
        prec = metrics.precision_score(y_test, y_pred, zero_division=0)
        rec = metrics.recall_score(y_test, y_pred, zero_division=0)
        f1 = metrics.f1_score(y_test, y_pred, zero_division=0)
        fpr = calculate_fpr(y_test, y_pred)

        results.append({
            "Model": name,
            "Accuracy": round(acc, 4),
            "Precision": round(prec, 4),
            "Recall": round(rec, 4),
            "F1-Score": round(f1, 4),
            "FPR": round(fpr, 4)
        })

        print(f"    -> Acc: {acc:.4f} | Prec: {prec:.4f} | Rec: {rec:.4f} | F1: {f1:.4f} | FPR: {fpr:.4f}")

        if f1 > best_f1:
            best_f1 = f1
            best_model = model
            best_model_name = name

    # Xuất kết quả ra file CSV cho Dev 5 dùng làm Dashboard
    os.makedirs("results", exist_ok=True)
    results_df = pd.DataFrame(results)
    results_csv_path = "results/benchmark_results.csv"
    results_df.to_csv(results_csv_path, index=False)
    print(f"\n[+] Da luu bang so sanh hieu nang vao: {results_csv_path}")
    print("\n" + results_df.to_string(index=False))

    # Lưu model tốt nhất cho Dev 1 (CLI) và Dev 5 (Web)
    if best_model is not None:
        os.makedirs("models", exist_ok=True)
        model_save_path = "models/best_model.joblib"
        with open(model_save_path, "wb") as f:
            pickle.dump(best_model, f)
        print(f"\n[+] Mo hinh xuat sac nhat: [{best_model_name}] voi F1 = {best_f1:.4f}")
        print(f"[+] Da luu model vao: {model_save_path}")

    print("\n==========================================================")
    print("[+] HOAN THANH TAC VU HUAN LUYEN VA DANH GIA MO HINH")
    print("==========================================================")

if __name__ == "__main__":
    train_and_evaluate()
