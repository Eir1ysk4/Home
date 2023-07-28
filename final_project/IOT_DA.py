
import random
import requests

BMI_equation = ""

def init_BMI_equation():
    global BMI_equation
    headers = {}
    url = "	https://io.adafruit.com/api/v2/Eir1ysk4/feeds/bmi-equation"
    x = requests.get(url=url, headers = headers, verify = False)
    data = x.json()
    BMI_equation = data["last_value"]

def calBMI(w, h):
    global BMI_equation
    res = round(eval(BMI_equation),2)
    return res

def getValue():
    BP = random.randint(90, 120)
    BC = random.randint(1300, 2000)
    HR = random.randint(60, 100)
    SD = random.randint(3, 12)
    Steps = random.randint(700, 1000)
    Weight = random.randint(45, 75)
    Height = round(random.uniform(1, 2), 2)
    BMI_status = calBMI(Weight,Height)
    return [BMI_status, BP, BC, HR, SD, Steps, Weight]

