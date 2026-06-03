import json
import os

def loader():
    if not os.path.exists('data.json'):
        raise FileNotFoundError('data.json not found')
    with open('data.json') as f:
        data = json.load(f) 
    return data

def saver(data):
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data,f, indent=4)
    