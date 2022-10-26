from ctypes import resize
import requests
import os
import weather_api
TOKEN = os.environ['TOKEN']
key = os.environ['KEY']
def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def get_last_update(updates):
    last_updates = updates['result'][-1]
    chat_id = last_updates['message']['chat']['id']
    text = last_updates['message']['text']
    message_id = last_updates['message']['message_id']
    return chat_id, text, message_id

def send_message(TOKEN,chat_id, text):
    button1 = {'text':'Samarkand'}
    button2 = {'text':'Tashkent'}
    button3 = {'text':'Bukhara'}
    button4 = {'text':'Andijan'}
    
    keyboard = [[button1, button2],[button3,button4]]
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}

    data = {
            'chat_id':chat_id,
            'text':text,
            'parse_mode':'HTML',
            'reply_markup':reply_markup
        }

    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data)
new_message = -1
while True:
    updates = get_updates(TOKEN)
    last_update = get_last_update(updates)
    chat_id, text, last_message_id = last_update

    
    weather_data = weather_api.get_data_city(key,text)
    send_message(TOKEN,chat_id,weather_data)