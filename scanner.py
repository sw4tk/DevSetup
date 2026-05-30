import subprocess

def check_tool(name):
    try:
        result = subprocess.run(
            [ name,'--banana'],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() or result.stderr.strip()
    except FileNotFoundError:
        return 'Not found'
       
