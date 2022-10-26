import os
import requests
import os
key = os.environ['KEY']
def get_data_city(key:str, city:str)->dict:
    url = f'https://api.openweathermap.org/data/2.5/weather'

    payload = {
        'q':city,
        'appid':key
    }
    
    r = requests.get(url,params=payload)
    if r.status_code == 200:
        data = r.json()
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = round(float(data['main']['temp']) - 273)
        wind = data['wind']['speed']
        
        text = f'Weather: {weather}\nTemprature: {temp}\nWind Speed: {wind}\nDescription: {description}'
        return text
    else:
        return 'Quyidagi shaharlardan birini tanlang!👇'