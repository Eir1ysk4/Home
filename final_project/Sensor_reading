#done based on Mr.Nhan source code
import time
import serial.tools.list_ports
try:
    ser = serial.Serial(port="COM4",baudrate= 115200)
except:
    print("cant open port")

def sendCommand (cmd):
    ser.write(cmd.encode())
    
mess = ""
tempData = 0 # to save sensor readings to a tempData
def processData(data):
    global tempData

    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    #save readings to tempData
    tempData = splitData
    print(splitData)

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            print(mess)
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def readTemperature():
# read temperature input via sensors
# print out temperature in C and alert when goes over certain value
    print("reading temp")
    for _ in range (5):
        global tempData
        #requesting reading of temp
        requestData("0")
        print (float(tempData[2]))
        #if temp is higher than some num, turn on light 
        if float(tempData[2]) > 29:
            sendCommand("4")
    sendCommand("5")
    print ("end of reading")


def readHumidity():
# read humidity input via sensors
# print out humidity in percentage of water in surrounding environment
# and alert(via turning on LED light) when goes over certain value
    print("reading humidity")
    for _ in range (5):
        global tempData
        #requesting reading of humidity
        requestData("1")
        print (float(tempData[2]))
        #if humidity is higher than some num, turn on light 
        if float(tempData[2]) > 45:
            sendCommand("4")
    sendCommand("5")
    print ("end of reading")
    

def requestData(cmd):
    sendCommand(cmd)
    time.sleep(1)
    readSerial()

# sendCommand("2")
# time.sleep(2)
# sendCommand("3")
# time.sleep(2)
# sendCommand("4")
# time.sleep(2)
# sendCommand("5")
# readTemperature()

