
import sys
from Adafruit_IO import MQTTClient
import time
import urllib3


#import already existed file
import Sensor_reading as sr
import IOT_DA as Da

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AIO_FEED_ID = ["bmi","blood-pressure","	burned-calories"
               ,"heart-rates", "sleep-duration","steps", "weight"]
AIO_USERNAME = "Eir1ysk4"
AIO_KEY = "aio_wjot67ee6SikXLGPmBbInILhPS9C"

# connect to server and subscribe to feeds
def connected(client):
    print("Connected to server!!!")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)
    client.subscribe("body-temperature")

# relay successful subscription
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed successfully...")

# disconnect client from server
def disconnected(client):
    print("Disconnected from server!")
    sys.exit (1)

# handle communicating actions sent 
# and check for specific feed to show special message
def message(client , feed_id , payload):
    print(f"{feed_id} received data: {payload}")

    if (feed_id == "bmi-equation"):
        BMI_equation = payload
        print (BMI_equation)

# initiating connection process and requirements
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
Da.init_BMI_equation()

connected(client)

while (True):
    time.sleep(10)
    valueList = Da.getValue()
    print(valueList)
    for j in range(len(valueList)):
        client.publish(AIO_FEED_ID[j], valueList[j])
    sr.readTemperature()
    client.publish("body-temperature",float(sr.tempData))
disconnected(client)
