from scanner import check_tool
from tools import tools
from categorizer import categorizer
from printer import printer
from doctor import doctor
from loader import loader
from saver import saver
from doctor_profiles import doctor_profiles as profiles
from profile_manager import create_profile, delete_profile, list_profiles, edit_profile,show_profile
import os
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
    elif command == 'profile':
        if len(sys.argv) < 3:
            print('usage:\n    python main.py profile create <name>\n    python main.py profile show <name>\n    python main.py profile delete <name>\n    python main.py profile edit <name>\n python main.py profile list')
        else:
            action = sys.argv[2]
            if action == 'list':
                
                list_profiles()
            elif len(sys.argv) < 4 :
                print('usage:\n    python main.py profile create <name>\n    python main.py profile show <name>\n    python main.py profile list\n    python main.py profile delete <name>')
            else:
                if action == 'create':
                    print('Creating profile\n')
                    create_profile(sys.argv[3])
                elif action == 'delete':
                    print('Deleting profile\n')
                    delete_profile(sys.argv[3])
                elif action == 'show':
                    print('Showing profile\n')
                    show_profile(sys.argv[3])
                elif action == 'edit':
                    edit_profile(sys.argv[3])
                else:
                    print('Invalid command')
               
    else:
        print('Invalid command')    













    