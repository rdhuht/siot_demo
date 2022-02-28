import siot
import time
import random

SERVER = input("server:")           # MQTT服务器IP
CLIENT_ID = "humidity_id"                  # 在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = 'farmer/tianqiSensors_humidity'  # “topic”为“项目名称/设备名称”
IOT_UserName ='siot'            # 用户名
IOT_PassWord ='siot'         # 密码

siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()

humidity = int(input("模拟湿度初始值："))
scope = int(input("模拟湿度变化幅度设定："))
time_interval = int(input("发送信息的频率是（秒）:"))

while True:
    upDown = random.randint(0, 2)
    if upDown == 1:
        up = random.randint(1, scope)
        humidity += up
    elif upDown == 2:
        down = random.randint(1, scope)
        humidity -= down
    else:
        pass
        
    siot.publish(IOT_pubTopic, humidity)
    print(f"湿度：{humidity}%")
    time.sleep(time_interval)  #隔1秒发送一次

