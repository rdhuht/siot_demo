from mpython import *       #导入mpython模块
import music
import time
from machine import Timer
# from umqtt.simple import MQTTClient
from siot import iot
import random
import network

WIFI_SSID = 'Jeremy的iPhone'#替换成你的WIFI热点名称
WIFI_PASSWORD = '1234567890'#替换成你的WIFI热点密码


def doing(led_num=0):
    rgb[led_num] = (50, 0, 0)  # 设置为红色，全亮度   
    rgb.write()
    # music.play(music.POWER_UP)


def ready(led_num=0):
    rgb[led_num] = (0, 50, 0)  # 设置为绿色，全亮度   
    rgb.write()
    music.play(music.BA_DING)
    

# wifi连接
def connectWIFI():
    mywifi = wifi()
    doing(0)
    mywifi.connectWiFi(WIFI_SSID,WIFI_PASSWORD)
    ready(0)
    print('WiFi Connection successful')


connectWIFI()  # 连接wifi热点

# MQTT连接
SERVER = "172.20.10.13"            # MQTT服务器IP
CLIENT_ID = ""                  # 在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = 'farmer/t'  # “topic”为“项目名称/设备名称”
username = "siot"
password = "siot"

client = iot(CLIENT_ID, SERVER, port=1883,user=username, password=password)
client.connect()

try:
    doing(1)
    client.connect()
    client.loop()
    ready(1)
    print("mqttconnected!")
except:
    print("mqttdisconnected!")

temperature = 10
scope = 1
while True:
    upDown = random.randint(0, 2)
    if upDown == 1:
        up = random.randint(1, scope)
        temperature += up
    elif upDown == 2:
        down = random.randint(1, scope)
        temperature -= down
    client.publish(IOT_pubTopic, str(temperature))
    time.sleep(1)

