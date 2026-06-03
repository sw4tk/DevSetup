import json
import os


def psaver(name,profile):
    localpath = os.path.join('profiles',f'{name}.json')
    with open(localpath, 'w', encoding='utf-8') as f:
        json.dump(profile,f, indent=4)
    
    
def ploader(name):
    localpath = os.path.join('profiles',f'{name}.json')
    with open(localpath , 'r' , encoding='utf-8') as f:
        data = json.load(f)
        return data

            
