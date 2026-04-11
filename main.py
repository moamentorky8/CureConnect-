from machine import Pin, I2C, SPI
import ssd1306
import time
import os

# 1. إعدادات الشاشة والساعة (I2C)
# SDA -> 21, SCL -> 22
try:
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
except:
    oled = None
    print("OLED/RTC not found, continuing...")

# 2. إعدادات الموتور (A4988)
# STEP -> 12, DIR -> 14
step_pin = Pin(12, Pin.OUT)
dir_pin = Pin(14, Pin.OUT)

# 3. إعدادات الحساس والبازر
# PIR -> 27, Buzzer -> 13
pir_sensor = Pin(27, Pin.IN)
buzzer = Pin(13, Pin.OUT)

# 4. إعدادات الـ SD Card (SPI) - اختياري
try:
    # CS=5, SCK=18, MOSI=23, MISO=19
    sd_spi = SPI(2, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
    # ملاحظة: في Wokwi الميموري كارد بتحتاج مكتبة sdcard.py لو حبيت تسجل داتا
except:
    print("SD Card initialization skipped")

def update_display(status):
    if oled:
        oled.fill(0)
        oled.text("CureConnect AI", 10, 5)
        oled.text("-" * 15, 10, 20)
        oled.text("Status:", 10, 35)
        oled.text(status, 65, 35)
        oled.show()

def run_dispenser():
    print("Motion Detected! Dispensing medicine...")
    update_display("Working")
    
    # تحريك الموتور لمدة ثانيتين
    dir_pin.value(1) # اتجاه اللف
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
    
    update_display("Ready")
    print("Dispensing finished.")

# البداية
update_display("Ready")
print("CureConnect System is Online...")

while True:
    # لو الحساس لقط حركة
    if pir_sensor.value() == 1:
        run_dispenser()
        # انتظار 5 ثواني عشان الموتور ميفضلش يلف لو أنت لسه قدام الجهاز
        time.sleep(5)
    
    time.sleep(0.1)