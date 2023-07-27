print("MQTT with Adafruit IO")
import sys
from Adafruit_IO import MQTTClient
import random
import time


AIO_USERNAME = "Eir1ysk4"
AIO_KEY = ""

BMI = 'Weight/((Height)**2)'

def modify_value(Weight, Height):
    global BMI
    res = round(eval(BMI),2)
    print("BMI status: ",res)
    return res

def connected(client):
    print("Server connected ...")
    client.subscribe("Blood Pressure")
    client.subscribe("Body Temperature")
    client.subscribe("Burned Calories")
    client.subscribe("Heart Rates")
    client.subscribe("Sleep Duration")
    client.subscribe("Steps")
    client.subscribe("Weight")
    client.subscribe("BMI")
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed!!!")

def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected  #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    time.sleep(10)
    BP = random.randint(90, 120)
    BT = round(random.uniform(36.5, 37.5),2)
    BC = random.randint(1300, 2000)
    HR = random.randint(60, 100)
    SD = random.randint(3, 12)
    Steps = random.randint(700, 1000)
    Weight = random.randint(45, 75)
    client.publish("Blood Pressure", BP)
    client.publish("Body Temperature", BT)
    client.publish("Burned Calories", BC)
    client.publish("Heart Rates", HR)
    client.publish("Sleep Duration", SD)
    client.publish("Steps", Steps)
    client.publish("Weight", Weight)
    Height = round(random.uniform(1, 2), 2)
    BMI_status = round(modify_value(Weight, Height), 2)
    client.publish("BMI", BMI_status)
    pass
