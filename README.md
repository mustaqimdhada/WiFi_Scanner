# 📡 Wi-Fi Network Scanner

## 📌 Overview

This project implements a real-time Wi-Fi network scanner using Python, customtkinter, and pywifi. It displays nearby Wi-Fi networks along with SSID, signal strength, and security type, auto-refreshing every 20 seconds.

## ✨ Features

- 🔍 Scan for available Wi-Fi networks in real-time
- 📶 Categorizes signal strength (Excellent, Moderate, Weak)
- 🔒 Displays network security type (WPA2-PSK, WPA-PSK, Open)
- 🖥️ GUI built with customtkinter for a modern appearance
- 🔄 Auto-refresh scan every 20 seconds

## ⚙️ Installation

### 📋 Prerequisites

- 🐍 Python 3.x
- 💻 Supported OS: Windows, Linux (requires pywifi support)

### 📦 Required Python Libraries:

- customtkinter
- pywifi

## 🚀 Installation Steps

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/WiFiScanner.git
   
   ```
2. Navigate to the project folder:

   ```
   cd WiFiScanner
   
   ```
3. Install the dependencies:

   ```
   pip install customtkinter pywifi
   
   ```

## 🛠️ Usage

### 🖥️ Launch the Scanner

```
python wifi_scanner.py
```

### 🧭 Inside the GUI:

- Click 🔍 Start Scanning to begin listing nearby networks
- The app will:- Show SSID
  - Indicate Security level
  - Display Signal Strength (colored based on strength)
  - Auto-scans every 20 seconds
  - 
## 🎨 Signal Strength Categories

- **Excellent**: Signal ≥ -50 dBm (Color: Green)
- **Moderate**: Signal ≥ -70 dBm (Color: Orange)
- **Weak**: Signal &lt; -70 dBm (Color: Red)

## 🔒 Security Detection

Identifies the following security types:

- WPA2-PSK
- WPA-PSK
- Open
- Unknown

## 🧪 Example Output

```
📶 SSID: MyHomeWiFi
🔒 Security: WPA2-PSK
📡 Signal: -42 dBm — Excellent
```
## 📸 Screenshots

## 🎥 Demo Video
