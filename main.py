from machine import Pin, I2C, PWM
import ssd1306
import time

# 1. إعدادات الشاشة (OLED)
# المعيد طلب نستخدم oled = None كحالة افتراضية
oled = None 

try:
    # إعداد الـ I2C على pins 21 و 22
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    # محاولة تعريف الشاشة
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    print("OLED initialized.")
except:
    # لو الشاشة مش موجودة بنخليها None عشان الـ If Statement تعرف
    oled = None
    print("OLED not found, continuing in headless mode...")

# 2. إعدادات السيرفو (Pin 18)
servo = PWM(Pin(18), freq=50)

def set_angle(angle):
    # معادلة تحويل الزاوية لنبضة Duty يفهمها السيرفو في Wokwi
    duty = int(((angle / 180) * 102) + 26)
    servo.duty(duty)

# 3. الحساس والبازر (Pins 27 & 13)
pir_sensor = Pin(27, Pin.IN)
buzzer = Pin(13, Pin.OUT)

def update_display(msg):
    # تطبيق طلب المعيد: الـ If Statement للتأكد من وجود الشاشة
    if oled is not None:
        try:
            oled.fill(0)
            oled.text("CureConnect AI", 10, 5)
            oled.text("-" * 15, 10, 20)
            oled.text("Status:", 10, 40)
            oled.text(msg, 65, 40)
            oled.show()
        except:
            pass # لو حصل مشكلة أثناء الكتابة ميوقفش الكود

def dispense_medicine():
    print("Motion Detected! Dispensing...")
    update_display("Working")
    
    # تحريك السيرفو (فتح البوابة 90 درجة)
    set_angle(90)
    
    # التوقيت اللي طلبته (800 مللي ثانية)
    time.sleep_ms(800) 
    
    # إغلاق البوابة (العودة لزاوية 0)
    set_angle(0)
    
    # تنبيه صوتي
    buzzer.value(1)
    time.sleep_ms(300)
    buzzer.value(0)
    
    update_display("Ready")
    print("Dispensing finished.")

# بداية التشغيل (ضبط الوضع الأصلي)
set_angle(0)
update_display("Ready")
print("CureConnect System is Online...")

while True:
    # فحص الحساس (Input)
    if pir_sensor.value() == 1:
        dispense_medicine()
        # انتظار 5 ثواني لمنع التكرار المباشر
        time.sleep(5)
    
    time.sleep(0.1) # راحة للمعالج
