from scanner import check_tool
from tools import tools
from saver import saver
from categorizer import categorizer

data = check_tool(tools)
installed,missing = categorizer(data)
saver(data)


print('DevSetup v0.2.0 Report')
print('='*20)
 
print(f'\nTotal Scanned:{len(tools)}\n')

print('\nInstalled:')
if not installed:
    print('None')
else:
    for item in installed:
       
        print(f"✔ {item[0]} : {item[1]}")

print('\nMissing:')
if not missing:
    print('None')
else:
    for item in missing:
        print(f"✘ {item}")




    