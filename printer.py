def printer(data,installed,missing):
    print('='*35)
 
    print(f'\nTotal Scanned:{len(data)}')

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
        