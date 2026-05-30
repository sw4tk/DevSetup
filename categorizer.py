

def categorizer(data):
    installed = []    
    missing = []
    for tool,item in data.items():
        if item['installed']:
            installed.append((tool,item['version']))
        else:
            missing.append(tool)
    return installed,missing
