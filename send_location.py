import requests
import os
TOKEN = os.environ['TOKEN']

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
    button1 = {'text':'Contact','request_contact':True}
    button2 = {'text':'Location','request_location':True}
    keyboard = [[button1],[button2]]

    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    data = {
            'chat_id':chat_id,
            'text':text,
            'parse_mode':'HTML',
            'reply_markup': reply_markup
        }
    
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',json=data)

updates = get_updates(TOKEN)
last_update = get_last_update(updates)
chat_id, text, last_message_id = last_update

send_message(TOKEN,chat_id,text)