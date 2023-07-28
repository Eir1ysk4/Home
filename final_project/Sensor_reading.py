#done based on Mr.Nhan source code
import time
import serial.tools.list_ports
try:
    ser = serial.Serial(port="COM4",baudrate= 115200)
except:
    print("cant open port")

def sendCommand (cmd):
    ser.write(cmd.encode())

def requestData(cmd):
    sendCommand(cmd)
    time.sleep(1)
    readSerial()
    
mess = ""
tempData = 0 # to save sensor readings to a tempData

def processData(data):
    global tempData

    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    #save readings to tempData
    tempData = splitData
    
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def readTemperature():
# read temperature input via sensors
# print out temperature in C and alert when goes over certain value
    print("reading temp")
    global tempData
    #requesting reading of temp
    requestData("0")
     #if temp is higher than some num, turn on light 
    if float(tempData[2]) > 31:
        sendCommand("4")
    sendCommand("5")
    print ("end of reading")



