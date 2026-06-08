import json
import time
import os
import platform
from tools_metadata import TOOL_METADATA
from profile_storage import ploader, psaver , pexport
from profile_manager import create_profile, delete_profile, list_profiles, edit_profile,show_profile
from data_manager import check_tool, categorizer
from printer import printer
from storage import loader, saver
from default_tools import default_tools
from validators import profile_validator
from installer import install_tool

current_version = "0.8.0"
userOS = platform.system().lower()

def namehandler(name):
    if name.endswith('.json'):
        return name.removesuffix('.json')
    return name

def calculate_health(installed, total):
    if total == 0:
        return 100.0
    return (len(installed) / total) * 100

def scan(args):
    tools = default_tools
    if args.profile:
        profile = args.profile
        try:
            profile_data = ploader(profile)
        except FileNotFoundError:
            print(f"Profile {profile} not found.")
            return

        tools = profile_data.get('tools', [])
        data = check_tool(tools)
        installed,missing = categorizer(data)
        health = calculate_health(installed, len(tools))
        print(f'\nDevsetup v{current_version} Profile Comparison')
        printer(data,installed,missing)
        print(f'\nEnvironment Health : {health:.2f}%')
        print(f'Installed : {len(installed)}/{len(tools)}\n')
    else:
        print('\nScanning...')
        data = check_tool(tools)
        installed,missing = categorizer(data)
        saver(data)
        print(f'\nDevsetup v{current_version} Scan Report')
        printer(data,installed,missing)
        print('\n')


def version(args):
    with open('VERSION','r') as f:
        print(f'Version : {f.read()}')

def report(args):
    data = loader()
    installed,missing = categorizer(data)
    print(f'\nDevsetup v{current_version} Report')
    printer(data,installed,missing)
    print('\n')

def profile(args):
    if not args.action:
            print("Please specify an action: list, create, delete, show, edit")
            return
    if args.action == 'list':
        list_profiles()
        return
    args.name = namehandler(args.name)

    if args.action == 'create':
        create_profile(args.name)
    elif args.action == 'delete':
        delete_profile(args.name)
    elif args.action == 'show':
        show_profile(args.name)
    elif args.action == 'edit':
        edit_profile(args.name)
    elif args.action == 'import':
        if f"{args.name}.json" in os.listdir("profiles"):
            print(f"Profile {args.name} already exists. Please choose a different name or delete the existing profile.")
            return
        try:
            with open(f"{args.name}.json", 'r', encoding='utf-8') as f:
                profile = json.load(f)
        except FileNotFoundError:
            print(f"Profile {args.name} not found.")
        except json.JSONDecodeError as e:
            print(f"Profile {args.name} is not a valid JSON file: {e}")
            return
        profile.pop('date',None)
        profile.pop('devsetup_version',None)
        try:
            profile_validator(profile)
        except ValueError as e:
            print(f"Profile {args.name} is invalid: {e}")
            return
        psaver(args.name, profile)
        print(f"Profile {args.name} imported successfully")
    elif args.action == 'export':
        pexport(args.name , current_version)
        print(f"Profile {args.name} exported successfully")
    else:
        print("Unknown action. Please specify one of: list, create, delete, show, edit, import, export")

def install(args):
    if not args.profile:
        print("Please specify a profile to install")
        return
    try:
        profile = ploader(args.profile)
    except FileNotFoundError:
        print(f"Profile {args.profile} does not exist")
        return

    if not profile:
        print(f"Profile {args.profile} does not exist")
        return
        
    data = check_tool(profile['tools'])
    if data:
        installed,missing = categorizer(data)
    else:
        print(f"No tools found in profile {args.profile}")
        return
    print(f'\nDevsetup {current_version} Installer :==>')

    printer(data,installed,missing)
    print('\n')

    if not missing:
        print('All tools are already installed')
        return
    
    choice = input('Do you want to install missing tools? (y/n): ').lower().strip()
    if choice != 'y':
        print('\nInstallation cancelled\n')
        return
    installation_data = {
        'installed' : [],
        'failed': []
    }
    for tool in missing:
        install_tool(tool,installation_data)
    print(f'\nDevSetup {current_version} Installation Summary :')
    print('='*30)
    print('Installed:')
    if len(installation_data['installed']) == 0:
        print('    - None')
    else:
        for tool in installation_data['installed']:
            print(f'    - {tool}')
    print('\n')
    print('Failed:')
    if len(installation_data['failed']) == 0:
        print('    - None')
    else:
        for tool in installation_data['failed']:
            print(f'    - {tool}')
    print('\n')
    print("[INFO]\nSome installed tools require a terminal restart.\nPlease restart your terminal and rerun the scan.")
    print('\nInstallation complete\n')
    choice = input('Do you want to verify installation? (y/n): ').lower().strip()

    if choice != 'y':
        print('\nVerification cancelled\n')
        return
    
    verify_installation(installation_data['installed'])




def install_specifictool(args):
    if not args.tool:
        print('No tool specified')
        return
    if args.tool not in TOOL_METADATA[userOS]:
        print('Tool not found')
        return
    scanstatus = scan_tool(args)
    if scanstatus:
        return
    print(f'Installing {args.tool}...')
    time.sleep(1)
    tool = args.tool
    installation_data = {
        'installed' : [],
        'failed': []
    }
    install_tool(tool,installation_data)
    print(f'\nDevSetup {current_version} Installation Summary :')
    print('='*30)
    print('\nInstalled:')
    if len(installation_data['installed']) == 0:
        print('    - None')
    else:
        for tool in installation_data['installed']:
            print(f'    - {tool}')
    print('\n')
    print('Failed:')
    if len(installation_data['failed']) == 0:
        print('    - None')
    else:
        for tool in installation_data['failed']:
            print(f'    - {tool}')
    print('\n')
    print("[INFO]\nSome installed tools require a terminal restart.\nPlease restart your terminal and rerun the scan.")

def scan_tool(args):
    if not args.tool:
        print('No tool specified')
        return
    if args.tool not in TOOL_METADATA[userOS]:
        print('Tool not found')
        return
    print(f'Scanning for {args.tool}...')
    data = check_tool([args.tool])
    installed,_ = categorizer(data)
    for name in installed:
        if name[0] == args.tool:
            print(f'{args.tool} is already installed')
            return True
    print(f'{args.tool} is not installed')
    return False


def verify_installation(installed):
    data = check_tool(installed)
    installed,failed = categorizer(data)
    print('\n')
    for name in installed:
        print(f'[OK] Verified  - {name[0]}')
    print('\n')
    for name in failed:
        print(f'[WARN] Installed but not detected in PATH yet - {name}')

