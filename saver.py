import json

def saver(data):
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data,f, indent=4)
    
    


            
