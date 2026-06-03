from scan import check_tool
from tools import tools
from categorizer import categorizer
from printer import printer
from storage import loader,saver
from profile_storage import ploader,psaver
from profile_manager import create_profile, delete_profile, list_profiles, edit_profile,show_profile
import os
import argparse
import sys




if len(sys.argv) < 2:
    print('usage:\n    python main.py scan\n    python main.py report\n    python main.py version\n    python main.py doctor')
    sys.exit(1)
else:
    command = sys.argv[1]
    if command == 'scan':
        if len(sys.argv) > 2:
            profile = sys.argv[2]
            profile_data = ploader(profile)
            tools = profile_data['tools']
            data = check_tool(tools)
            installed,missing = categorizer(data)
            health = (len(installed) / len(tools)) * 100
            print('\nDevsetup v0.5.0 Profile Comparision')
            printer(data,installed,missing)
            print(f'\nEnvironment Health : {health:.2f}%')
            print(f'Installed : {len(installed)}/{len(tools)}\n')

        
        else:
            print('\nScanning...')
            data = check_tool(tools)
            installed,missing = categorizer(data)
            saver(data)
            print('\nDevsetup v0.5.0 Scan Report')
            printer(data,installed,missing)
            print('\n')
            

    elif command == 'report':
        data = loader()
        installed,missing = categorizer(data)
        print('\nDevsetup v0.5.0 Report')
        printer(data,installed,missing)
        print('\n')

    elif command == 'version':
       with open('VERSION','r') as f:
            print(f'Version : {f.read()}')

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













    