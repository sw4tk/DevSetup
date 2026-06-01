def printer(data,installed,missing):
    print('DevSetup v0.4.0 Report')
    print('='*20)
 
    print(f'\nTotal Scanned:{len(data)}\n')

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
            print(f"✘ {item}\n")