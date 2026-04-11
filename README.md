# CureConnect: Smart IoT Medicine Dispenser (Servo Edition) 💊

**CureConnect** is an automated medicine dispensing system developed as part of my engineering coursework at **Borg El Arab Technological University**. This project integrates embedded systems, MicroPython, and 3D Mechanical Design (Fusion 360) to help patients take their medications on time.

---

## 🚀 Project Overview
The system is optimized for speed and reliability. It remains in standby mode until the **PIR Motion Sensor** detects a patient's presence.

**Execution Flow:**
1. **Detection:** The PIR sensor triggers the system upon sensing motion.
2. **Dispensing:** The **SG90 Servo Motor** rapidly rotates to 90° to dispense the pill and returns to 0° within **800ms**.
3. **Alert:** An **Active Buzzer** provides an immediate acoustic notification.
4. **Monitoring:** The **OLED Display** provides real-time status updates (Ready / Working).

---

## 🏗️ Mechanical Design (Autodesk Fusion 360)
The project includes a custom mechanical structure designed in **Fusion 360**:
- **Servo-Driven Mechanism:** A precise dispensing gate or carousel designed for the SG90 Servo.
- **Compact Housing:** Engineered to fit the ESP32 and all sensors in a sleek, ergonomic shell.

---

## 🛠️ Hardware Architecture
- **Microcontroller:** ESP32 (Wroom Module)
- **Actuator:** SG90 Micro Servo (PWM Controlled)
- **Sensor:** PIR Motion Sensor (HC-SR501)
- **Display:** 0.96" OLED SSD1306 (I2C interface)
- **Feedback:** Active Buzzer
- **Timekeeping:** DS1307 RTC Module
- **Storage:** SD Card Module (SPI interface)

---

## 📉 Updated Circuit Pinout (Wiring)
| Component | ESP32 Pin | Function |
| :--- | :--- | :--- |
| **Servo PWM** | GPIO 18 | Angle Control |
| **PIR Sensor** | GPIO 27 | Motion Detection |
| **Buzzer** | GPIO 13 | Audio Alert |
| **OLED SDA** | GPIO 21 | I2C Data |
| **OLED SCL** | GPIO 22 | I2C Clock |

---

## 💻 Software Stack
The project is programmed in **MicroPython**. The code includes smart error handling for the display:
- `main.py`: Core logic with `if statements` to ensure the system runs even if the OLED is disconnected.
- `ssd1306.py`: MicroPython driver for the display.

---

## 🕹️ Live Simulation
Test the updated Servo-based circuit on Wokwi:

🔗 **[Run CureConnect (Servo) Simulation](https://wokwi.com/projects/460992929619127297)**

---

## 👨‍💻 Developed By
**Moamen Abdelfattah** *First Year Student - Borg El Arab Technological University*
