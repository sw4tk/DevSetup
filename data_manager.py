import subprocess
from version_commands import VERSION_COMMANDS
import platform

def check_tool(tools):
    useros = platform.system().lower()
    data = {}
    for name in tools: 
        if name in VERSION_COMMANDS:
            if useros in VERSION_COMMANDS[name]:
                try:
                    command = VERSION_COMMANDS[name][useros]
                    result = subprocess.run(
                        command,
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                            data[name] = {
                               'installed' : True,
                                'version' : result.stdout.strip() or result.stderr.strip()
                        }
                    else:
                            data[name] = {
                                'installed' : False,
                                'version' : None
                           }
                except FileNotFoundError:
                    data[name] = {'installed' : False,'version' : None} 
            else:
                 print(f"{useros} is not supported for {name}")  
        else:
            print(f"{name} is not supported")
    return data
        


def categorizer(data):
    installed = []    
    missing = []
    for tool,item in data.items():
        if item['installed']:
            installed.append((tool,item['version']))
        else:
            missing.append(tool)
    return installed,missing

       
