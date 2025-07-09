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
   git clone https://github.com/mustaqimdhada/WiFiScanner.git
   
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
python wifi.py
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
  <img src="https://github.com/user-attachments/assets/780c18d8-52ff-45b6-988d-f0e482008c8a" alt="Chat Interface" width="600"/>
  <img src="https://github.com/user-attachments/assets/14f714db-674e-4e94-8e5c-fcdcf7010345" alt="Emoji Picker" width="600"/>
  <img src="https://github.com/user-attachments/assets/f429cd7f-3336-4996-98f6-29b3364ddece" alt="Random Password Generation" width="600"/>

## 🎥 Demo Video

https://github.com/user-attachments/assets/f2d1fb19-3cb7-40ef-adf7-706a736ffd47
