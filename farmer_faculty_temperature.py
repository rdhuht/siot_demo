import siot
import time
import random


SERVER = input("server:")            # MQTT服务器IP
CLIENT_ID = "temperature_id"                  # 在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = 'farmer/tianqiSensors_temperature'  # “topic”为“项目名称/设备名称”
IOT_UserName ='siot'            # 用户名
IOT_PassWord ='siot'         # 密码

siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()

temperature = int(input("模拟温度初始值："))
scope = int(input("模拟温度变化幅度设定："))
time_interval = int(input("发送信息的频率是（秒）:"))

while True:
    upDown = random.randint(0, 2)
    if upDown == 1:
        up = random.randint(1, scope)
        temperature += up
    elif upDown == 2:
        down = random.randint(1, scope)
        temperature -= down
    else:
        pass
        
    siot.publish(IOT_pubTopic, temperature)
    print(f"温度：{temperature}℃")
    time.sleep(time_interval)  #隔1秒发送一次
