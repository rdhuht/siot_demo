import siot
from time import sleep

SERVER = input("server:")          # MQTT服务器IP
CLIENT_ID = "phone_id"              #在SIoT上，CLIENT_ID可以留空
IOT_pubTopics  = ['farmer/tianqiSensors_temperature', 'farmer/tianqiSensors_humidity']   #“topic”为“项目名称/设备名称”
IOT_UserName ='siot'        #用户名
IOT_PassWord ='siot'     #密码


def sub_cb(client, userdata, msg):#定义收到消息时的提示信息
    message = msg.payload
#     print("\nTopic:" + str(msg.topic) + " Message:" + str(message))
    t = int(message)
#     temperature_judge(t)
    humidity_judge(t)
    

def temperature_judge(t):
    if t >= 20:
        print(f"当前温度{t}, 启动降温执行器(风扇)")
        print("风扇降温中……")
        sleep(5)
    elif t < 15:
        print(f"当前温度{t}, 启动升温执行器(光照RGB灯)")
        print("光照加热中……")
        sleep(5)
    else:
        print(f"当前温度{t}")

def humidity_judge(t):
    if t >= 40:
        print(f"当前湿度{t}, 启动降低湿度执行器(降湿度设备)")
        print("干燥中……")
        sleep(5)
    elif t < 15:
        print(f"当前湿度{t}, 启动升高湿度执行器(洒水)")
        print("加湿度中……")
        sleep(5)
    else:
        print(f"当前湿度{t}")
        
        
siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()
siot.subscribe(IOT_pubTopics[1], sub_cb)
siot.loop()