"""
src/data/flow_extractor.py
---------------------------------------------------------
Trích xuất các luồng mạng (Network Flows) từ file PCAP và
tính toán các đặc trưng thống kê cho mỗi luồng.

Nhiệm vụ: Thành viên 2 - Kỹ sư Dữ liệu Mạng (Tuần 2)

Cách chạy:
    python src/data/flow_extractor.py data/raw/ten_file.pcap
---------------------------------------------------------
"""

import sys
import time
from collections import defaultdict

import numpy as np
import pandas as pd
from scapy.all import PcapReader, IP, TCP, UDP


def get_5_tuple(pkt):
    """
    Trích xuất 5-tuple định danh một luồng từ MỘT gói tin.
    5-tuple = (src_ip, dst_ip, src_port, dst_port, protocol)
    Trả về None nếu gói tin không phải IP hoặc không phải TCP/UDP
    (ví dụ ARP, ICMP) - tuỳ yêu cầu đề tài có thể mở rộng thêm.
    """
    if IP not in pkt:
        return None

    ip_layer = pkt[IP]
    src_ip, dst_ip = ip_layer.src, ip_layer.dst
    proto = ip_layer.proto  # 6 = TCP, 17 = UDP

    if TCP in pkt:
        src_port, dst_port = pkt[TCP].sport, pkt[TCP].dport
    elif UDP in pkt:
        src_port, dst_port = pkt[UDP].sport, pkt[UDP].dport
    else:
        return None

    return (src_ip, dst_ip, src_port, dst_port, proto)


def normalize_flow_key(five_tuple):
    """
    Một luồng TCP/UDP luôn có 2 chiều: gói đi (forward) và gói về
    (backward). Nếu không chuẩn hoá, ta sẽ tạo ra 2 flow riêng biệt
    cho cùng 1 kết nối thực tế.

    Quy ước: chiều nào có (ip, port) "nhỏ hơn" theo thứ tự từ điển
    thì được coi là chiều "chuẩn" (canonical) của flow.
    Trả về (khoá_flow_đã_chuẩn_hoá, "fwd" | "bwd").
    """
    src_ip, dst_ip, src_port, dst_port, proto = five_tuple
    if (src_ip, src_port) <= (dst_ip, dst_port):
        return (src_ip, dst_ip, src_port, dst_port, proto), "fwd"
    return (dst_ip, src_ip, dst_port, src_port, proto), "bwd"


def extract_flows(pcap_path, log_every=100_000):
    """
    Đọc PCAP theo kiểu streaming bằng PcapReader (KHÔNG dùng rdpcap,
    vì rdpcap nạp toàn bộ file vào RAM -> dễ tràn RAM với file lớn).
    Gom gói tin thành flow theo 5-tuple đã chuẩn hoá.
    """
    flows = defaultdict(lambda: {
        "src_ip": None, "dst_ip": None,
        "src_port": None, "dst_port": None, "protocol": None,
        "ts_start": None, "ts_end": None,
        "fwd_pkt_lens": [], "bwd_pkt_lens": [],
        "fwd_bytes": 0, "bwd_bytes": 0,
    })

    n_pkts = 0
    n_skipped = 0
    with PcapReader(pcap_path) as reader:
        for pkt in reader:
            n_pkts += 1
            if n_pkts % log_every == 0:
                print(f"  ... đã đọc {n_pkts:,} gói tin, "
                      f"{len(flows):,} flow tạm thời")

            five_tuple = get_5_tuple(pkt)
            if five_tuple is None:
                n_skipped += 1
                continue

            flow_key, direction = normalize_flow_key(five_tuple)
            f = flows[flow_key]

            if f["src_ip"] is None:
                (f["src_ip"], f["dst_ip"],
                 f["src_port"], f["dst_port"], f["protocol"]) = flow_key

            ts = float(pkt.time)
            pkt_len = len(pkt)
            f["ts_start"] = ts if f["ts_start"] is None else min(f["ts_start"], ts)
            f["ts_end"] = ts if f["ts_end"] is None else max(f["ts_end"], ts)

            if direction == "fwd":
                f["fwd_pkt_lens"].append(pkt_len)
                f["fwd_bytes"] += pkt_len
            else:
                f["bwd_pkt_lens"].append(pkt_len)
                f["bwd_bytes"] += pkt_len

    print(f"\nTổng số gói tin đọc được : {n_pkts:,}")
    print(f"Số gói tin bỏ qua (không phải TCP/UDP-IP): {n_skipped:,}")
    print(f"Tổng số flow gom được    : {len(flows):,}")
    return flows


def compute_features(flows):
    """
    Với mỗi flow, tính các đặc trưng thống kê theo đúng danh sách
    được yêu cầu trong TODO_LIST.md:
        flow_duration, total_fwd_pkts, total_bwd_pkts,
        total_fwd_bytes, total_bwd_bytes, bytes_per_sec,
        packets_per_sec, packet_len_mean, packet_len_std
    """
    rows = []
    MIN_DURATION = 1e-6  # tránh chia cho 0 với flow chỉ có 1 gói tin

    for f in flows.values():
        duration = max(f["ts_end"] - f["ts_start"], MIN_DURATION)
        all_lens = f["fwd_pkt_lens"] + f["bwd_pkt_lens"]
        total_pkts = len(all_lens)
        total_bytes = f["fwd_bytes"] + f["bwd_bytes"]

        rows.append({
            "src_ip": f["src_ip"],
            "dst_ip": f["dst_ip"],
            "src_port": f["src_port"],
            "dst_port": f["dst_port"],
            "protocol": f["protocol"],
            "timestamp": f["ts_start"],
            "flow_duration": duration,
            "total_fwd_pkts": len(f["fwd_pkt_lens"]),
            "total_bwd_pkts": len(f["bwd_pkt_lens"]),
            "total_fwd_bytes": f["fwd_bytes"],
            "total_bwd_bytes": f["bwd_bytes"],
            "bytes_per_sec": total_bytes / duration,
            "packets_per_sec": total_pkts / duration,
            "packet_len_mean": float(np.mean(all_lens)) if all_lens else 0.0,
            "packet_len_std": float(np.std(all_lens)) if len(all_lens) > 1 else 0.0,
        })

    return pd.DataFrame(rows)


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python flow_extractor.py <đường_dẫn_file.pcap>")
        sys.exit(1)

    pcap_path = sys.argv[1]
    print(f"Đang xử lý file: {pcap_path}")

    t0 = time.time()
    flows = extract_flows(pcap_path)
    df = compute_features(flows)
    print(f"Hoàn tất trích xuất đặc trưng trong {time.time() - t0:.1f} giây")

    print("\n5 dòng đầu tiên:")
    print(df.head())

    out_path = "data/processed/flows_unlabeled.csv"
    df.to_csv(out_path, index=False)
    print(f"\nĐã lưu kết quả (chưa gán nhãn) vào: {out_path}")
    print("Bước tiếp theo: chạy labeling.py để gán nhãn Botnet/Normal.")


if __name__ == "__main__":
    main()
