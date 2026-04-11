from machine import Pin, I2C
import ssd1306
import time

# 1. إعداد الشاشة (SCL=22, SDA=21)
try:
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
except:
    print("OLED NOT FOUND")

# 2. إعداد الموتور (STEP=12, DIR=14)
step_pin = Pin(12, Pin.OUT)
dir_pin = Pin(14, Pin.OUT)

# 3. إعداد البازر والحساس (Buzzer=13, PIR=27)
buzzer = Pin(13, Pin.OUT)
sensor = Pin(27, Pin.IN)

def run_motor_2_sec():
    # تحديث الشاشة
    oled.fill(0)
    oled.text("CureConnect AI", 10, 10)
    oled.text("Dispensing...", 10, 30)
    oled.show()
    
    # تشغيل الموتور لمدة 2 ثانية
    dir_pin.value(1) 
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < 2000:
        step_pin.value(1)
        time.sleep_us(800)
        step_pin.value(0)
        time.sleep_us(800)
    
    # تنبيه صوتي
    buzzer.value(1)
    time.sleep(0.5)
    buzzer.value(0)
    
    # إعادة الشاشة للوضع العادي
    oled.fill(0)
    oled.text("System Ready", 20, 25)
    oled.show()

# البداية
oled.fill(0)
oled.text("CureConnect", 25, 25)
oled.show()

print("System Started...")

while True:
    # لو الحساس لقط حركة (PIR Sensor)
    if sensor.value() == 1:
        run_motor_2_sec()
        time.sleep(2) # انتظار بسيط عشان ميكررش الحركة بسرعة
    time.sleep(0.1)