from profile_storage import ploader
from profile_manager import create_profile, delete_profile, list_profiles, edit_profile,show_profile
from data_manager import check_tool, categorizer
from printer import printer
from storage import loader, saver
from default_tools import default_tools

version = "0.6.0"

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
        print(f'\nDevsetup v{version} Profile Comparison')
        printer(data,installed,missing)
        print(f'\nEnvironment Health : {health:.2f}%')
        print(f'Installed : {len(installed)}/{len(tools)}\n')
    else:
        print('\nScanning...')
        data = check_tool(tools)
        installed,missing = categorizer(data)
        saver(data)
        print(f'\nDevsetup v{version} Scan Report')
        printer(data,installed,missing)
        print('\n')


def version(args):
    with open('VERSION','r') as f:
        print(f'Version : {f.read()}')

def report(args):
    data = loader()
    installed,missing = categorizer(data)
    print(f'\nDevsetup v{version} Report')
    printer(data,installed,missing)
    print('\n')

def profile(args):
    if not args.action:
            print("Please specify an action: list, create, delete, show, edit")
            return
    if args.action == 'list':
        list_profiles()
    elif args.action == 'create':
        create_profile(args.name)
    elif args.action == 'delete':
        delete_profile(args.name)
    elif args.action == 'show':
        show_profile(args.name)
    elif args.action == 'edit':
        edit_profile(args.name)