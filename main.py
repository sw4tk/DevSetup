from scanner import check_tool
from tools import tools
from saver import saver
from categorizer import categorizer
from loader import loader
from printer import printer
from profiles import profiles
from doctor import doctor
import sys



if len(sys.argv) < 2:
    print('usage:\n    python main.py scan\n    python main.py report\n    python main.py version\n    python main.py doctor')
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

    elif command == 'doctor':
        try:
            if len(sys.argv) < 3:
                print('usage:\n    python main.py doctor <profile>')
                print('\nProfiles :\n\n    webdev\n    python\n    ai')
            else:
                docdata = doctor(profiles,sys.argv[2])
                print('\nDevSetup v0.4 Doctor')
                print('='*20)
                print(f'\nProfile : {docdata["profile"]}')
                print(f'Description : {docdata["description"]}')
                print(f'Environment Health : {docdata["health"]:.0f}%')
                print(f'Installed : {docdata["installed_count"]}/{docdata["total_count"]}\n')
                print('Issues : ')
                if not docdata['issues']:
                    print('    None')
                else:
                    for name in docdata['issues']:
                        print(f'    {name} missing.')
                print('\n')

        except ValueError:
            print('Invalid profile')
            
    else:
        print('Invalid command')    













    