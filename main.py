import argparse
from functions import scan, report, profile, version ,install ,install_specifictool,scan_tool

parser = argparse.ArgumentParser(description='Devsetup - A Developer Environment Setup and Management Tool')
subparsers = parser.add_subparsers(dest='command', help='Available commands')

install_parser = subparsers.add_parser('install', help='Install tools from a profile')
install_parser.add_argument('profile', help='Profile to install')
install_parser.set_defaults(func=install)

tool_parser = subparsers.add_parser('install-tool', help='Install a specific tool')
tool_parser.add_argument('tool', help='Tool to install')
tool_parser.set_defaults(func=install_specifictool)

scan_parser = subparsers.add_parser('scan', help='Scan the system for installed tools')
scan_parser.add_argument('profile', nargs='?', help='Profile to compare against')
scan_parser.set_defaults(func=scan)

toolscan_parser = subparsers.add_parser('scan-tool', help='Scan the system for a specific tool')
toolscan_parser.add_argument('tool', help='Tool to scan for')
toolscan_parser.set_defaults(func=scan_tool)

reports_parser = subparsers.add_parser('report', help='Show reports')
reports_parser.set_defaults(func=report)

profile_parser = subparsers.add_parser('profile', help='Manage profiles')

profile_subparsers = profile_parser.add_subparsers(dest='action', help='Profile actions')
profile_subparsers.add_parser('list', help='List all profiles')
profile_subparsers.add_parser('create', help='Create a new profile').add_argument('name', help='Name of the profile to create')
profile_subparsers.add_parser('delete', help='Delete a profile').add_argument('name', help='Name of the profile to delete')
profile_subparsers.add_parser('show', help='Show a profile').add_argument('name', help='Name of the profile to show')
profile_subparsers.add_parser('edit', help='Edit a profile').add_argument('name', help='Name of the profile to edit')
profile_subparsers.add_parser('import', help='Import a profile from a JSON file').add_argument('name', help='Name of the profile to import (without .json extension)')
profile_subparsers.add_parser('export', help='Export a profile to a JSON file').add_argument('name', help='Name of the profile to export (without .json extension)')

profile_parser.set_defaults(func=profile)

version_parser = subparsers.add_parser('version', help='Show the current version of Devsetup')
version_parser.set_defaults(func=version)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()


  













    