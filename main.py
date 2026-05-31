from scanner import check_tool
from tools import tools
from saver import saver
from categorizer import categorizer
from loader import loader
from printer import printer
import sys



if len(sys.argv) < 2:
    print('usage:\n    python main.py scan\n    python main.py report\n    python main.py version')
    sys.exit(1)
else:
    command = sys.argv[1]
    if command == 'scan':
        print('Scanning...')
        data = check_tool(tools)
        installed,missing = categorizer(data)
        saver(data)
        printer(data,installed,missing)

    elif command == 'report':
        data = loader()
        installed,missing = categorizer(data)
        printer(data,installed,missing)

    elif command == 'version':
       with open('VERSION','r') as f:
            print(f'Version : {f.read()}')

    else:
        print('Invalid command')    













    