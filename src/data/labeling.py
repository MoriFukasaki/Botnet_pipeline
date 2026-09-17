"""
src/data/labeling.py
---------------------------------------------------------
Gán nhãn Botnet (1) / Normal (0) cho từng flow đã trích xuất,
dựa trên danh sách IP đã bị nhiễm Botnet được công bố kèm theo
kịch bản CTU-13 đã chọn (đọc trong file README.* của scenario,
hoặc trang https://www.stratosphereips.org/datasets-ctu13).

Nhiệm vụ: Thành viên 2 - Kỹ sư Dữ liệu Mạng (Tuần 2)

Cách chạy:
    python src/data/labeling.py
---------------------------------------------------------
"""

import pandas as pd


BOTNET_IPS = {
    "147.32.84.165",
    
}


def label_flows(df: pd.DataFrame, botnet_ips: set) -> pd.DataFrame:
    """
    Quy tắc gán nhãn (đúng theo TODO_LIST.md):
        Nếu src_ip HOẶC dst_ip nằm trong danh sách Botnet IP
        -> label = 1 (Botnet)
        Ngược lại -> label = 0 (Normal)
    """
    if not botnet_ips:
        raise ValueError(
            "BOTNET_IPS đang rỗng! Hãy điền danh sách IP botnet "
            "thật của kịch bản CTU-13 đã chọn trước khi chạy."
        )

    df = df.copy()
    df["label"] = (
        df["src_ip"].isin(botnet_ips) | df["dst_ip"].isin(botnet_ips)
    ).astype(int)
    return df


def print_label_stats(df: pd.DataFrame) -> None:
    counts = df["label"].value_counts()
    total = len(df)
    n_normal = int(counts.get(0, 0))
    n_botnet = int(counts.get(1, 0))

    print("=== Thống kê nhãn sau khi gán ===")
    print(f"  Normal (0) : {n_normal:>8,} flow  ({n_normal / total * 100:5.1f}%)")
    print(f"  Botnet (1) : {n_botnet:>8,} flow  ({n_botnet / total * 100:5.1f}%)")
    print(f"  Tổng cộng  : {total:>8,} flow")

    if n_botnet == 0 or n_normal == 0:
        print("\n⚠️  CẢNH BÁO: Dữ liệu chỉ có 1 loại nhãn! "
              "Kiểm tra lại danh sách BOTNET_IPS hoặc file PCAP nguồn.")


def main():
    input_path = "data/processed/flows_unlabeled.csv"
    output_path = "data/processed/ctu13_labeled_flows.csv"

    df = pd.read_csv(input_path)
    print(f"Đã đọc {len(df):,} flow từ {input_path}")

    labeled_df = label_flows(df, BOTNET_IPS)
    print_label_stats(labeled_df)

    labeled_df.to_csv(output_path, index=False)
    print(f"\nĐã lưu file kết quả cuối cùng: {output_path}")
    print("File này sẽ được bàn giao cho Thành viên 3 (tiền xử lý & chống rò rỉ dữ liệu).")


if __name__ == "__main__":
    main()
