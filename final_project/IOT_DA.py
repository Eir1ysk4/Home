
import random
import requests

# varible to receive equation from server
BMI_equation = ""

def init_BMI_equation():
    global BMI_equation
    headers = {}
    #feed's API
    url = "	https://io.adafruit.com/api/v2/Eir1ysk4/feeds/bmi-equation"
    x = requests.get(url=url, headers = headers, verify = False)
    data = x.json()
    BMI_equation = data["last_value"]

def calBMI(w, h):
    global BMI_equation
    res = round(eval(BMI_equation),2)
    return res

def getValue():
    BP = random.randint(90, 120) #blood pressure
    BC = random.randint(1300, 2000) # Burnt calories per day 
    HR = random.randint(60, 100) # Heart rate
    SD = random.randint(3, 12) # Sleep duration per day in hours
    Steps = random.randint(700, 1000) # Step taken per day
    Weight = random.randint(45, 75) # current weight
    Height = round(random.uniform(1, 2), 2) # current height
    BMI_status = calBMI(Weight,Height) # current BMI
    return [BMI_status, BP, BC, HR, SD, Steps, Weight]

