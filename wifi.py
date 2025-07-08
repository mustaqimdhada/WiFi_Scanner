import customtkinter as ctk
import pywifi
from pywifi import const
import time

# ------------------ Signal Strength Category ------------------ #
def categorize_signal(signal):
    if signal >= -50:
        return "Excellent", "green"
    elif signal >= -70:
        return "Moderate", "orange"
    else:
        return "Weak", "red"

# ------------------ Security Detection ------------------ #
def get_auth_type(network):
    if const.AKM_TYPE_WPA2PSK in network.akm:
        return "WPA2-PSK"
    elif const.AKM_TYPE_WPAPSK in network.akm:
        return "WPA-PSK"
    elif const.AKM_TYPE_NONE in network.akm:
        return "Open"
    else:
        return "Unknown"

# ------------------ Auto Scan Function ------------------ #
rescan_interval = 20000  # 20 seconds (in ms)

def scan_wifi():
    for widget in output_frame.winfo_children():
        widget.destroy()

    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(3)
        results = iface.scan_results()

        seen = set()
        for network in results:
            if network.ssid not in seen and network.ssid != "":
                seen.add(network.ssid)
                signal_text, signal_color = categorize_signal(network.signal)

                net_frame = ctk.CTkFrame(output_frame, corner_radius=10)
                net_frame.pack(pady=5, padx=10, fill="x")

                ssid_label = ctk.CTkLabel(net_frame, text=f"📶 SSID: {network.ssid}",
                                          font=("Arial", 14, "bold"))
                ssid_label.pack(anchor="w", padx=10, pady=2)

                security_label = ctk.CTkLabel(net_frame, text=f"🔒 Security: {get_auth_type(network)}",
                                              font=("Arial", 12))
                security_label.pack(anchor="w", padx=10, pady=2)

                signal_label = ctk.CTkLabel(net_frame,
                                            text=f"📡 Signal: {network.signal} dBm — {signal_text}",
                                            font=("Arial", 12),
                                            text_color=signal_color)
                signal_label.pack(anchor="w", padx=10, pady=2)

    except Exception as e:
        error_label = ctk.CTkLabel(output_frame, text=f"❌ Error: {e}",
                                   text_color="red", font=("Arial", 14))
        error_label.pack(pady=10)

    # Schedule next scan after 20 seconds
    app.after(rescan_interval, scan_wifi)

# ------------------ GUI Setup ------------------ #
ctk.set_appearance_mode("System")  # Dark/Light/System
ctk.set_default_color_theme("green")  # Or "green", "dark-blue"

app = ctk.CTk()
app.title("📡 Wi-Fi Network Scanner")
app.geometry("550x600")
app.resizable(False, False)

# Title
title_label = ctk.CTkLabel(app, text="📡 Wi-Fi Scanner", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Scan Button
def start_auto_scan():
    scan_button.configure(state="disabled")
    scan_wifi()

scan_button = ctk.CTkButton(app, text="🔍 Start Scanning",
                            font=("Arial", 16), command=start_auto_scan)
scan_button.pack(pady=10)

# Scrollable Frame for Output
scrollable = ctk.CTkScrollableFrame(app, width=500, height=450)
scrollable.pack(padx=10, pady=10, fill="both", expand=True)

output_frame = scrollable  # Use alias for inner widgets

# Run App
app.mainloop()
