from mpython import *       #导入mpython模块
import music
from siot import *
import time
import random

WIFI_SSID = 'Jeremy的iPhone'#替换成你的WIFI热点名称
WIFI_PASSWORD = '1234567890'#替换成你的WIFI热点密码

SERVER = "172.20.10.13"            # MQTT服务器IP
IOT_PORT = 1883
CLIENT_ID = "temperature_id"                  # 在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = 'farmer/tianqiSensors_temperature'  # “topic”为“项目名称/设备名称”
IOT_UserName ='siotcuijianwei'            # 用户名
IOT_PassWord ='siotcuijianwei'         # 密码

# wifi
def connectWIFI():
    mywifi = wifi()
    doing(0)
    mywifi.connectWiFi(WIFI_SSID,WIFI_PASSWORD)
    while mywifi.sta.isconnected() == False:
        pass
    ready(0)
    print('Connection successful')
    print(mywifi.sta.ifconfig())


def doing(led_num=0):
    rgb[led_num] = (50, 0, 0)  # 设置为红色，全亮度   
    rgb.write()
    # music.play(music.POWER_UP)


def ready(led_num=0):
    rgb[led_num] = (0, 50, 0)  # 设置为红色，全亮度   
    rgb.write()
    music.play(music.BA_DING)


def blink(led_num=0):
    rgb[led_num] = (0, 0, 50)
    rgb.write()
    time.sleep(0.2)
    rgb[led_num] = (0, 0, 0)
    rgb.write()
    time.sleep(0.1)


connectWIFI()  # 连接wifi热点
# MQTT服务器IP
doing(1)
client=iot(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
client.connect()
ready(1)

temperature = 15
scope = 1
time_interval = 1

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
        
    client.publish(IOT_pubTopic, str(temperature))
    blink(2)
    print(temperature)
    time.sleep(time_interval)  #隔1秒发送一次
