from machine import Pin, I2C, PWM, SPI
import ssd1306
import time
import os

# =========================
# 1. إعداد الـ SD Card (SPI)
# =========================
print("--- CureConnect System Booting ---")
sd_mounted = False

try:
    # إعداد الـ SPI: SCK=18, MOSI=23, MISO=19
    sd_spi = SPI(1, baudrate=40000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
    import sdcard
    # CS واصل على Pin 5
    sd = sdcard.SDCard(sd_spi, Pin(5))
    os.mount(sd, "/sd")
    sd_mounted = True
    print("✅ SD Card: Mounted Successfully")
except Exception as e:
    print("⚠️ SD Card: Failed to Mount ->", e)

# =========================
# 2. إعداد الشاشة والـ RTC (I2C)
# =========================
try:
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    print("✅ OLED Connection: Established")
except Exception as e:
    print("❌ OLED Connection: Failed ->", e)

# =========================
# 3. إعداد السيرفو والحساسات
# =========================
servo = PWM(Pin(14), freq=50) # السيرفو على بن 14
pir = Pin(27, Pin.IN)
buzzer = Pin(13, Pin.OUT)

def set_angle(angle):
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

def get_time_str():
    """دالة لجلب الوقت وتنسيقه"""
    t = time.localtime()
    # تنسيق الوقت HH:MM:SS
    return "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])

def update_display(status):
    if oled:
        oled.fill(0)
        oled.text("CureConnect AI", 10, 5)
        oled.text("-" * 16, 0, 15)
        
        # رجعنا إظهار الوقت هنا
        oled.text("Time: " + get_time_str(), 0, 30)
        
        oled.text("Status: " + status, 0, 50)
        oled.show()

def log_to_sd(event_msg):
    if sd_mounted:
        try:
            with open("/sd/medical_log.txt", "a") as f:
                f.write(get_time_str() + " - " + event_msg + "\n")
            print("💾 SD Log: Recorded")
        except:
            print("❌ SD Log Error")

# --- البداية الفعلية ---
set_angle(0)
update_display("Ready")
print("🚀 System is Ready...")

while True:
    # تحديث الشاشة كل ثانية لإظهار الوقت وهو بيعد
    update_display("Ready")
    
    if pir.value() == 1:
        print("🚨 ALERT: Motion Detected!")
        update_display("Dispensing")
        
        # تسجيل العملية على الـ SD مع الوقت
        log_to_sd("Medicine Dispensed")
        
        print("🔧 Action: Rotating Servo")
        set_angle(90)
        time.sleep(1)
        set_angle(0)
        
        buzzer.value(1)
        time.sleep(0.2)
        buzzer.value(0)
        
        print("✅ Task Finished.")
        update_display("Ready")
        
        # انتظار توقف الحركة لمنع التكرار
        while pir.value() == 1:
            time.sleep(0.1)
            update_display("Ready")
            
    time.sleep(1) # تحديث كل ثانية
