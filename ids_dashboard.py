from flask import Flask, render_template_string
from flask_socketio import SocketIO
from scapy.all import *
from collections import defaultdict
import threading

# Flask setup
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# IDS counters
connection_count = defaultdict(int)
syn_count = defaultdict(int)
icmp_count = defaultdict(int)
scan_detected = set()

THRESHOLD_CONNECTION = 50
THRESHOLD_SYN = 40
THRESHOLD_ICMP = 50

LOG_ALERT = "alerts.log"
LOG_TRAFFIC = "traffic.log"

# HTML Dashboard (langsung embedded)
dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Realtime IDS Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.5.4/socket.io.min.js"></script>

    <style>
        body { background: #111; color: #eee; font-family: Arial; padding: 20px; }
        .alert-box { background:#222; padding:10px; border-radius:10px; margin-bottom:10px; }
        .red { color:#ff4444; font-weight:bold; }
    </style>
</head>
<body>
    <h1>🔥 Realtime IDS Dashboard</h1>

    <h3>📡 Live Alerts</h3>
    <div id="alerts"></div>

    <h3>📊 Traffic Chart (Packets per Protocol)</h3>
    <canvas id="trafficChart" width="400" height="180"></canvas>

    <script>
        const socket = io();

        // ====== ALERTS =======
        socket.on("alert", function(data){
            const alerts = document.getElementById("alerts");
            const div = document.createElement("div");
            div.className = "alert-box";
            div.innerHTML = "<span class='red'>[ALERT]</span> " + data;
            alerts.prepend(div);
        });

        // ====== CHART =======
        const ctx = document.getElementById("trafficChart").getContext("2d");
        const trafficChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["TCP", "UDP", "ICMP"],
                datasets: [{
                    label: "Packets",
                    data: [0, 0, 0],
                    borderWidth: 2
                }]
            },
            options: { scales: { y: { beginAtZero: true }}}
        });

        socket.on("traffic", function(data){
            trafficChart.data.datasets[0].data = [
                data.tcp,
                data.udp,
                data.icmp
            ];
            trafficChart.update();
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(dashboard_html)


# ====== IDS LOGIC =======
traffic_counter = {"tcp": 0, "udp": 0, "icmp": 0}

def log_alert(msg):
    with open(LOG_ALERT, "a") as f:
        f.write(msg + "\n")
    socketio.emit("alert", msg)
    print("[ALERT] " + msg)

def log_traffic(proto):
    with open(LOG_TRAFFIC, "a") as f:
        f.write(proto + "\n")

def detect_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src

        # ------------ TCP --------------
        if packet.haslayer(TCP):
            traffic_counter["tcp"] += 1
            log_traffic("TCP")

            flags = packet[TCP].flags
            connection_count[src] += 1

            # SYN packet
            if flags == "S":
                syn_count[src] += 1

                if syn_count[src] > 20 and src not in scan_detected:
                    scan_detected.add(src)
                    log_alert(f"Port scan detected from {src}")

                if syn_count[src] > THRESHOLD_SYN:
                    log_alert(f"Possible SYN flood attack from {src}")

            if connection_count[src] > THRESHOLD_CONNECTION:
                log_alert(f"Suspicious high traffic from {src}")

        # ------------ UDP --------------
        if packet.haslayer(UDP):
            traffic_counter["udp"] += 1
            log_traffic("UDP")

        # ------------ ICMP --------------
        if packet.haslayer(ICMP):
            traffic_counter["icmp"] += 1
            log_traffic("ICMP")

            icmp_count[src] += 1
            if icmp_count[src] > THRESHOLD_ICMP:
                log_alert(f"ICMP ping flood from {src}")

        # Update chart to client
        socketio.emit("traffic", traffic_counter)


def start_sniff():
    sniff(iface="eth0", prn=detect_packet, store=False)


# Run IDS in separate thread
threading.Thread(target=start_sniff, daemon=True).start()

if __name__ == "__main__":
    print("🔥 IDS + Web Dashboard running on http://127.0.0.1:5000")
    socketio.run(app, host="0.0.0.0", port=5000)
