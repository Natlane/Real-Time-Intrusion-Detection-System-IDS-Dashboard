from scapy.all import *
import time

TARGET = "127.0.0.1"   # localhost untuk self-test
DELAY = 0.2

def icmp_flood():
    print("[TEST] Running ICMP Ping Flood...")
    for _ in range(60):
        send(IP(dst=TARGET)/ICMP(), verbose=0)
    print("[DONE] ICMP Flood sent.\n")

def syn_flood():
    print("[TEST] Running TCP SYN Flood...")
    for _ in range(60):
        send(IP(dst=TARGET)/TCP(dport=80, flags="S"), verbose=0)
    print("[DONE] SYN Flood sent.\n")

def port_scan():
    print("[TEST] Running Port Scan...")
    for port in range(20, 100):
        send(IP(dst=TARGET)/TCP(dport=port, flags="S"), verbose=0)
        time.sleep(0.01)
    print("[DONE] Port Scan sent.\n")

def high_connection():
    print("[TEST] Running High Connection Simulation...")
    for _ in range(80):
        send(IP(dst=TARGET)/TCP(dport=443, flags="A"), verbose=0)
    print("[DONE] High connection traffic sent.\n")

if __name__ == "__main__":
    print("🚀 SELF-TEST IDS STARTED")
    time.sleep(1)

    icmp_flood()
    time.sleep(DELAY)

    syn_flood()
    time.sleep(DELAY)

    port_scan()
    time.sleep(DELAY)

    high_connection()

    print("🎉 SELF-TEST COMPLETED — Check your IDS terminal now!")
