import requests
import json

def retrive_messages(channel_id):
    headers = {
        'Authorization': ''
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=100', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value['content'], '\n')

retrive_messages('')
