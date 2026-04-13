# CureConnect: Smart IoT Medicine Dispenser 💊

**CureConnect** is an advanced, automated medicine dispensing system developed as part of my engineering coursework at **Borg El Arab Technological University**. This project integrates embedded systems, MicroPython, and 3D Mechanical Design (Fusion 360) to provide a reliable healthcare solution.

---

## 🚀 Project Overview
The system is designed for high reliability and smart monitoring. It remains in standby mode until the **PIR Motion Sensor** detects a patient's presence, ensuring that medication is dispensed only when needed.

### **Execution Flow:**
1.  **Detection:** The PIR sensor triggers the system upon sensing motion.
2.  **Dispensing:** The **SG90 Servo Motor** rapidly rotates to 90° and returns to 0° to release a single dose.
3.  **Real-time Logging:** Every dispensing event is timestamped via the **DS1307 RTC** and saved to a **MicroSD Card** for tracking.
4.  **Feedback:** Immediate acoustic notification via an **Active Buzzer** and visual status updates on the **OLED Display**.

---

## 🏗️ Mechanical Design (Autodesk Fusion 360)
* **Servo-Driven Mechanism:** Optimized gate design for precise pill release.
* **Integrated Shell:** A custom-designed 3D housing that fits the ESP32 and the full sensor suite in a compact, ergonomic form.

---

## 🛠️ Hardware Architecture & Updated Pinout
To ensure maximum torque for the Servo (solving the 3.3V voltage drop issue reported in earlier versions), the system now utilizes the **VIN (5V)** rail for actuators.



| Component | ESP32 Pin | Function | Power Rail |
| :--- | :--- | :--- | :--- |
| **SG90 Servo** | **GPIO 14** | PWM Angle Control | **VIN (5V)** |
| **PIR Sensor** | **GPIO 27** | Motion Detection | 3.3V |
| **Buzzer** | **GPIO 13** | Audio Notification | 3.3V |
| **OLED (SDA)** | **GPIO 21** | I2C Data Line | 3.3V |
| **OLED (SCL)** | **GPIO 22** | I2C Clock Line | 3.3V |
| **RTC (SDA/SCL)** | **21 / 22** | Shared I2C Bus | **VIN (5V)** |
| **SD Card (SPI)** | **5, 18, 19, 23**| Data Logging (CS, SCK, DO, DI) | 3.3V |

> **Engineering Note:** The Servo was moved from GPIO 18 to **GPIO 14** to prevent signal interference with the SD Card's SPI clock (SCK), ensuring stable storage operations.

---

## 💻 Software Stack
The project is programmed in **MicroPython**, featuring a robust and modular architecture:
* **`main.py`**: Core logic handling the dispensing sequence and error-safe OLED/SD initialization.
* **`sdcard.py`**: Driver for SPI-based data storage.
* **`ssd1306.py`**: Driver for the I2C OLED display.
* **Smart Logging:** Uses `os.mount` to create a local file system on the SD card for saving `medical_log.txt`.

---

## 🕹️ Live Simulation
The circuit has been fully tested and simulated on Wokwi with the updated power and signal routing.
🔗 [Run CureConnect (Pro) Simulation](https://wokwi.com/projects/your-link-here)

---

## 👨‍💻 Developed By
**Moamen Abdelfattah** *First Year Student - Borg El Arab Technological University*
