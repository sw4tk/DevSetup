import json
import os
from datetime import datetime

from storage import saver


def psaver(name,profile):
    localpath = os.path.join('profiles',f'{name}.json')
    with open(localpath, 'w', encoding='utf-8') as f:
        json.dump(profile,f, indent=4)
    
    
def ploader(name):
    localpath = os.path.join('profiles',f'{name}.json')
    with open(localpath , 'r' , encoding='utf-8') as f:
        data = json.load(f)
        return data
    
def pexport(name,current_version):
    profile = ploader(name)
    profile['devsetup_version'] = current_version
    profile['date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(profile)
    os.makedirs('exports', exist_ok=True)
    with open(f"{os.path.join('exports',f'{name}_export.json')}", 'w', encoding='utf-8') as f:
        json.dump(profile,f, indent=4)

            
