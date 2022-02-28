# http://iot.dfrobot.com.cn/ 注册使用，主题没法自己定义，需要手机号，不适合实际教学环境。
from mpython import *       #导入mpython模块
import music
import time
from machine import Timer
from umqtt.simple import MQTTClient
import random
import time

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
SERVER = "182.254.130.180"            # MQTT服务器IP
CLIENT_ID = ""                  # 在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = b'mOrogiLng'  # “topic”为“项目名称/设备名称”
username = "wzt_imY7g"
password = "wktlimY7Rz"

client = MQTTClient(CLIENT_ID, SERVER, port=1883,user=username, password=password)
try:
    doing(1)
    client.connect()
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

