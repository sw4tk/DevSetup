import json

from profile_storage import ploader, psaver , pexport
from profile_manager import create_profile, delete_profile, list_profiles, edit_profile,show_profile
from data_manager import check_tool, categorizer
from printer import printer
from storage import loader, saver
from default_tools import default_tools
from validators import profile_validator
import os

current_version = "0.7.0"

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
    args.name = namehandler(args.name)
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
    elif args.action == 'import':
        if f"{args.name}.json" in os.listdir("profiles"):
            print(f"Profile {args.name} already exists. Please choose a different name or delete the existing profile.")
            return
        with open(f"{args.name}.json", 'r', encoding='utf-8') as f:
            try:
                profile = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Profile {args.name} is not a valid JSON file: {e}")
                return
            profile.remove['date']
            profile.removep['current_version']
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

    
