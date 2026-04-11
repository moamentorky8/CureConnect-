# CureConnect: Smart IoT Medicine Dispenser 💊

**CureConnect** is an automated medicine dispensing system developed as part of my engineering coursework at **Borg El Arab Technological University**. The project aims to help patients take their medications on time using IoT and motion-sensing technology.

---

## 🚀 Project Overview
The system is designed to be efficient and user-friendly. It remains in standby mode until the **PIR Motion Sensor** detects the patient's presence. 

**Execution Flow:**
1. **Detection:** The PIR sensor triggers the system.
2. **Dispensing:** The **NEMA 17 Stepper Motor** rotates for exactly 2 seconds to release the medication dose.
3. **Alert:** An **Active Buzzer** sounds to notify the patient.
4. **Monitoring:** The **OLED Display** provides real-time status updates (System Ready / Dispensing).

---

## 🛠️ Hardware Architecture
The circuit is built using the following components:
- **Microcontroller:** ESP32 (Wroom Module)
- **Actuator:** NEMA 17 Stepper Motor
- **Driver:** A4988 Stepper Driver
- **Sensor:** PIR Motion Sensor (HC-SR501)
- **Display:** 0.96" OLED SSD1306 (I2C interface)
- **Feedback:** Active Buzzer
- **Storage:** SD Card Module (SPI interface)
- **Timekeeping:** DS1307 RTC Module

---

## 📉 Circuit Pinout (Wiring)
| Component | ESP32 Pin | Function |
| :--- | :--- | :--- |
| **A4988 STEP** | GPIO 12 | Step Signal |
| **A4988 DIR** | GPIO 14 | Direction Control |
| **PIR Sensor** | GPIO 27 | Input Signal |
| **Buzzer** | GPIO 13 | Output Alert |
| **OLED SDA** | GPIO 21 | I2C Data |
| **OLED SCL** | GPIO 22 | I2C Clock |

---

## 💻 Software
The logic is implemented in **MicroPython**. The repository contains:
- `main.py`: Core system logic and state management.
- `ssd1306.py`: I2C driver for the OLED display.

---

## 🕹️ Live Simulation
You can run and test the full project (circuit and code) via the Wokwi simulation link below:

🔗 **[Run CureConnect Simulation on Wokwi](https://wokwi.com/projects/460992929619127297)**

---

## 👨‍💻 Developed By
**Moamen Abdelfattah ** *First Year Student - Borg El Arab Technological University*
