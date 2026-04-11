from machine import Pin, I2C, PWM
import ssd1306
import time

# 1. إعدادات الشاشة (OLED) مع حماية if statement
oled = None
try:
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    print("OLED: Connected")
except:
    print("OLED: Not found, system will run anyway")

# 2. إعدادات السيرفو (Pin 18)
servo = PWM(Pin(18), freq=50)

def set_angle(angle):
    duty = int(((angle / 180) * 102) + 26)
    servo.duty(duty)

# 3. الحساس والبازر (Pins 27 & 13)
pir_sensor = Pin(27, Pin.IN)
buzzer = Pin(13, Pin.OUT)

def update_display(msg):
    # الـ if statement عشان الكود ميفصلش لو الشاشة مش واصلة
    if oled is not None:
        try:
            oled.fill(0)
            oled.text("CureConnect AI", 10, 5)
            oled.text("-" * 15, 10, 20)
            oled.text(msg, 10, 40)
            oled.show()
        except:
            pass

def dispense_medicine():
    print("Dispensing...")
    update_display("Dispensing...")
    
    # تحريك السيرفو لفتح البوابة
    set_angle(90)
    
    # التوقيت اللي طلبته (800 مللي ثانية)
    time.sleep_ms(800) 
    
    # إغلاق البوابة
    set_angle(0)
    
    # تنبيه صوتي
    buzzer.value(1)
    time.sleep_ms(300)
    buzzer.value(0)
    
    update_display("Ready")
    print("Done.")

# التشغيل المبدئي
set_angle(0)
update_display("System Ready")

while True:
    if pir_sensor.value() == 1:
        dispense_medicine()
        time.sleep(5) # انتظار لمنع التكرار المباشر
    time.sleep(0.1)