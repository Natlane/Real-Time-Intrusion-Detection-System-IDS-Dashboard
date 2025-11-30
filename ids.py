from scapy.all import *
from collections import defaultdict, Counter
import os
import time

# -----------------------
# Setup folder & logs
# -----------------------
if not os.path.exists("logs"):
    os.makedirs("logs")

ALERT_LOG = "logs/alerts.log"
TRAFFIC_LOG = "logs/traffic.log"

# -----------------------
# Thresholds & counters
# -----------------------
connection_count = defaultdict(int)
syn_count = defaultdict(int)
icmp_count = defaultdict(int)
scan_detected = set()

THRESHOLD_CONNECTION = 50
THRESHOLD_SYN = 40
THRESHOLD_ICMP = 50

# -----------------------
# Logging functions
# -----------------------
def log_alert(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    with open(ALERT_LOG, "a") as f:
        f.write(entry + "\n")
    print("[ALERT] " + message)

def log_traffic(packet):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    proto = "OTHER"
    src = dst = ""
    flags = ""

    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        if packet.haslayer(TCP):
            proto = "TCP"
            flags = str(packet[TCP].flags)
        elif packet.haslayer(UDP):
            proto = "UDP"
        elif packet.haslayer(ICMP):
            proto = "ICMP"

    entry = f"[{timestamp}] {proto} {src} -> {dst} {flags}"
    with open(TRAFFIC_LOG, "a") as f:
        f.write(entry + "\n")

# -----------------------
# Packet detection
# -----------------------
def detect_packet(packet):
    # log all traffic
    log_traffic(packet)

    if packet.haslayer(IP):
        src = packet[IP].src

        # TCP connections
        if packet.haslayer(TCP):
            flags = packet[TCP].flags
            connection_count[src] += 1

            # SYN flood & port scan
            if flags == "S":
                syn_count[src] += 1

                if syn_count[src] > 20 and src not in scan_detected:
                    scan_detected.add(src)
                    log_alert(f"Port scan detected from {src}")

                if syn_count[src] > THRESHOLD_SYN:
                    log_alert(f"Possible SYN flood attack from {src}")

            # Too many connections
            if connection_count[src] > THRESHOLD_CONNECTION:
                log_alert(f"Suspicious high traffic from {src}")

        # ICMP flood
        if packet.haslayer(ICMP):
            icmp_count[src] += 1
            if icmp_count[src] > THRESHOLD_ICMP:
                log_alert(f"Ping flood detected from {src}")

# -----------------------
# IDS start function
# -----------------------
def start_ids():
    print("🚀 IDS is running... listening for network traffic.")
    # Ganti iface sesuai interface aktif: 'eth0', 'lo', dsb.
    sniff(iface="eth0", prn=detect_packet, store=False)

# -----------------------
# Main
# -----------------------
if __name__ == "__main__":
    start_ids()
