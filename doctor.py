from categorizer import categorizer
from scanner import check_tool
import json
import os

def doctor(profiles,mode):
    docdata = {}
    if not mode in profiles:
        raise ValueError('Invalid mode')
    else:
        tools = profiles[mode]["tools"]
        data = check_tool(tools)
        installed,missing = categorizer(data)
        docdata['profile'] = profiles[mode]["profile"] 
        docdata['description'] = profiles[mode]["description"]
        docdata['health'] = len(installed) / len(tools)*100
        docdata['installed'] = installed
        docdata['installed_count'] = len(installed)
        docdata['total_count'] = len(tools)
        docdata['issues'] = missing
    return docdata