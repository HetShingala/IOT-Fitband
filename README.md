# IoT FitBand: Smart Health Monitoring System using Raspberry Pi

## Overview

The **IoT FitBand** is a smart, real-time health monitoring system that measures a user’s **heart rate**, **temperature**, and **humidity**, displays the readings on an **OLED display**, and uploads the data to the **ThingSpeak cloud** for remote visualization.
It is built using a **Raspberry Pi 4 Model B** and various sensors interfaced via I2C and GPIO, demonstrating how IoT can be applied in healthcare for remote and continuous health tracking.

---

## Features

* Real-time monitoring of heart rate, temperature, and humidity
* Local OLED display for live data visualization
* Automatic data upload to **ThingSpeak IoT Cloud**
* Buzzer alerts on abnormal readings
* Compact, low-cost, and portable system
* Suitable for healthcare, fitness, and IoT applications

---

## Hardware Components

| Component                     | Description                        | Function                                     |
| ----------------------------- | ---------------------------------- | -------------------------------------------- |
| **Raspberry Pi 4 Model B**    | Main processing unit with Wi-Fi    | Controls all sensors and uploads data        |
| **DHT11 Sensor**              | Temperature & humidity sensor      | Measures environmental parameters            |
| **Pulse Sensor**              | Analog heart rate sensor           | Detects heartbeat and produces analog signal |
| **ADS1115 ADC**               | 16-bit Analog-to-Digital Converter | Converts pulse sensor signal for the Pi      |
| **SSD1306 OLED Display**      | 0.96" I2C display                  | Displays real-time readings                  |
| **Buzzer**                    | Active buzzer                      | Alerts user on abnormal readings             |
| **Jumper Wires & Breadboard** | —                                  | Circuit connections                          |

---

## Software Requirements

| Software                             | Purpose                        |
| ------------------------------------ | ------------------------------ |
| **Raspberry Pi OS (Debian/Linux)**   | Operating system               |
| **Python 3**                         | Programming language           |
| **Adafruit CircuitPython Libraries** | Sensor & display interfacing   |
| **ThingSpeak Cloud**                 | IoT data visualization         |
| **VNC / SSH / Thonny IDE**           | Remote development & debugging |

---

## Circuit Connections

| Module                          | Raspberry Pi Pin         | Description       |
| ------------------------------- | ------------------------ | ----------------- |
| **DHT11**                       | GPIO4 (Pin 7)            | Sensor data       |
| **Pulse Sensor → ADS1115 (A0)** | A0 Input                 | Analog signal     |
| **ADS1115 (I2C)**               | SDA → GPIO2, SCL → GPIO3 | I2C communication |
| **OLED (SSD1306)**              | SDA → GPIO2, SCL → GPIO3 | I2C communication |
| **Buzzer**                      | GPIO17 (Pin 11)          | Digital output    |

---

## Working Principle

1. The **Pulse Sensor** detects heartbeat signals and sends analog voltage to the **ADS1115 ADC**.
2. The **ADS1115** converts the analog signal into a digital value readable by the **Raspberry Pi**.
3. The **DHT11 Sensor** measures temperature and humidity.
4. The **Raspberry Pi** processes all sensor data and displays it on the **OLED display**.
5. Data is uploaded to **ThingSpeak** every 20 seconds for remote monitoring and visualization.
6. If the temperature or heart rate exceeds a preset threshold, a **buzzer alert** is triggered.

---

## ThingSpeak Setup

1. Create an account on [ThingSpeak](https://thingspeak.com/).
2. Create a new channel named **IoT FitBand Monitoring System**.
3. Add 3 fields:

   * **Field 1** – Temperature (°C)
   * **Field 2** – Humidity (%)
   * **Field 3** – Heart Rate (BPM)
4. Copy the **Write API Key** and paste it into your Python code as:

   ```python
   THINGSPEAK_API_KEY = "YOUR_API_KEY_HERE"
   ```
5. Run your code and view live graphs on your ThingSpeak dashboard.

---

## Installation

### 1. Update System and Enable I2C

```bash
sudo apt update
sudo raspi-config
# Enable I2C under Interface Options → I2C → Enable
sudo reboot
```

### 2. Create a Virtual Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
sudo apt install libgpiod2 i2c-tools -y
pip install adafruit-circuitpython-dht
pip install adafruit-circuitpython-ads1x15
pip install adafruit-circuitpython-ssd1306
pip install Adafruit-Blinka
pip install requests
pip install pillow
pip install RPI.GPIO
```

---

## ▶️ Running the Project

```bash
source venv/bin/activate
python3 fitband.py
```

You will see:

* Sensor readings on the OLED screen
* Live data graphs on your ThingSpeak channel

---

## Output

### OLED Display Output

```
IoT FitBand
Temp: 28.5°C
Hum: 52%
Pulse: 78 BPM
```

### ThingSpeak Dashboard

* Field 1: Temperature vs Time
* Field 2: Humidity vs Time
* Field 3: Heart Rate vs Time

---

## Applications

* Real-time health and fitness monitoring
* Remote patient care and elderly tracking
* IoT-based wearable health systems
* Research in biomedical signal processing

---

## Future Enhancements

* Integration with **SpO₂ (Oxygen) and ECG sensors**
* Mobile app for live health tracking
* Cloud-based anomaly detection using AI
* Addition of GPS for location-based emergency alerts

---

## Conclusion

The **IoT FitBand** successfully implements a smart health monitoring system using Raspberry Pi and IoT technology.
By combining multiple sensors, real-time display, and cloud connectivity, it provides an affordable and scalable solution for continuous health tracking.
This project bridges the gap between wearable technology and IoT, paving the way for smarter healthcare innovations.

---
