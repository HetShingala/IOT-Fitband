# -*- coding: utf-8 -*-
import time
import board
import busio
import Adafruit_DHT
from gpiozero import Buzzer
import adafruit_ssd1306
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ----------------------------
# Setup
# ----------------------------
# I2C bus (shared by OLED + ADS1115)
i2c = busio.I2C(board.SCL, board.SDA)

# OLED Display
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

# ADS1115 (for KY-039)
ads = ADS.ADS1115(i2c)
ads.gain = 1
pulse = AnalogIn(ads, ADS.P0)

# DHT11 Sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# Buzzer
buzzer = Buzzer(17)

# Thresholds
TEMP_THRESHOLD = 37.5
HEART_THRESHOLD = 90  # BPM

# ----------------------------
# Functions
# ----------------------------
def get_heart_rate(samples=150, delay=0.01):
    readings = []
    for _ in range(samples):
        readings.append(pulse.value)
        time.sleep(delay)

    avg = sum(readings) / len(readings)
    beats = 0
    above = False

    for val in readings:
        if val > avg * 1.02 and not above:
            beats += 1
            above = True
        elif val < avg:
            above = False

    bpm = (beats / (samples * delay)) * 60
    return int(bpm)

# ----------------------------
# Main Loop
# ----------------------------
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is None or temperature is None:
        continue

    heart_rate = get_heart_rate()

    # Display on OLED
    oled.fill(0)
    oled.text(f"Temp: {temperature:.1f}C", 0, 0)
    oled.text(f"Hum:  {humidity:.1f}%", 0, 10)
    oled.text(f"Heart: {heart_rate} BPM", 0, 20)

    if temperature > TEMP_THRESHOLD and heart_rate > HEART_THRESHOLD:
        oled.text("⚠ ALERT ⚠", 0, 40)
        buzzer.on()
    else:
        buzzer.off()

    oled.show()
    time.sleep(2)

