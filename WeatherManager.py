import requests
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("pic\MyriadPro.otf", size=50)

def get_weather():

    res = requests.get("http://api.openweathermap.org/data/2.5/weather", 
        params={'id': 524901, 'units': 'metric', 'lang': 'ru', 'APPID': '76536255a8b4db9dd5858ec08709a85e'})
    data = res.json()
    
    temp = int(data['main']['temp'])
    if temp > 0:
        temp = "+" + str(temp) + "°"
    elif temp == 0:
        temp = str(temp) + "°"
    else:
        temp = "-" + str(temp) + "°"
        
    feels = int(data['main']['feels_like'])
    if feels > 0:
        feels = "+" + str(feels) + "°"
    elif feels == 0: 
        feels = str(feels) + "°"
    else:
        feels = "-" + str(feels) + "°"
    
    status = str.capitalize((data['weather'][0]['description']))
    if status == "Небольшой дождь" or "Дождь": 
        forecast = Image.open("rain.png")
    elif status == "Пасмурно":
        forecast = Image.open("cloudy.png")
    else:
        forecast = Image.open("sample.png")
    
    temperature = ImageDraw.Draw(forecast)
        
    temperature.text((108,300), status, font=font)
    temperature.text((108,400), "Ощущается как", font=font)
    temperature.text((108,350), "Температура", font=font)
    temperature.text((460,350), temp, font=font)
    temperature.text((460,400), feels, font=font)
    
    return forecast





