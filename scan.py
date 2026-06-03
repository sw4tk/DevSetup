import subprocess

def check_tool(tools):
    data = {}
    for name in tools: 
        try:
            result = subprocess.run(
                [name,'--version'],
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
    return data
        
       
