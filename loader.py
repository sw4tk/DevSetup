import json
import os

def loader():
    if not os.path.exists('data.json'):
        raise FileNotFoundError('data.json not found')
    with open('data.json') as f:
        data = json.load(f) 
    return data