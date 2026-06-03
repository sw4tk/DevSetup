import argparse
from functions import scan, report, profile, version

parser = argparse.ArgumentParser(description='Devsetup - A Developer Environment Setup and Management Tool')
subparsers = parser.add_subparsers(dest='command', help='Available commands')

scan_parser = subparsers.add_parser('scan', help='Scan the system for installed tools')
scan_parser.add_argument('profile', nargs='?', help='Profile to compare against')
scan_parser.set_defaults(func=scan)

reports_parser = subparsers.add_parser('report', help='Show reports')
reports_parser.set_defaults(func=report)

profile_parser = subparsers.add_parser('profile', help='Manage profiles')

profile_subparsers = profile_parser.add_subparsers(dest='action', help='Profile actions')
profile_subparsers.add_parser('list', help='List all profiles')
profile_subparsers.add_parser('create', help='Create a new profile').add_argument('name', help='Name of the profile to create')
profile_subparsers.add_parser('delete', help='Delete a profile').add_argument('name', help='Name of the profile to delete')
profile_subparsers.add_parser('show', help='Show a profile').add_argument('name', help='Name of the profile to show')
profile_subparsers.add_parser('edit', help='Edit a profile').add_argument('name', help='Name of the profile to edit')
profile_parser.set_defaults(func=profile)

version_parser = subparsers.add_parser('version', help='Show the current version of Devsetup')
version_parser.set_defaults(func=version)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()


  













    