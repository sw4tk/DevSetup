import os
from profile_storage import saver
from profile_storage import loader
 
def ensure_profiles_folder():
    if os.path.exists("profiles") and os.path.isdir("profiles"):
        return
        
    
    os.mkdir("profiles")
        

def create_profile(name):
    ensure_profiles_folder()
    localpath = os.path.join("profiles",f"{name}.json")
    if os.path.exists(localpath):
        print("Profile already exists")
        return
    
    profile = {}
    profile["name"] = name
    profile["description"] = input("Enter a description for this profile: ").strip()
    tools = []
   
    while True:
        tool = input("Enter a tool to add to this profile(type 'done' when finished): ").lower().strip()
        if tool == "done":
            if not tools:
                print("Profile must have at least one tool")
                continue
            break
        elif not tool:
            continue
        else:
            tools.append(tool)

    profile["tools"] = tools
   
    saver(name,profile)
    print(f"Profile {name} created successfully")

def list_profiles():
    if not os.path.exists("profiles") or not os.path.isdir("profiles"):
        print("No profiles found")
        return
    
    if not os.listdir("profiles"):
        print("No profiles found")
        return

    print(f'\nProfiles({len(os.listdir("profiles"))}) :')
    for profile in sorted(os.listdir("profiles")):
        name,_ = os.path.splitext(profile)
        print(f'  • {name}')

    

def show_profile(name):
    localpath = os.path.join("profiles", f"{name}.json")
    if not os.path.exists(localpath):
        print(f"Profile {name} does not exist")
        return

    profile = loader(name)
    
    print(f"Name: {profile['name']}")
    print(f"Description: {profile['description']}")
    print("Tools :")
    for tool in profile["tools"]:
        print(f" - {tool}")


def delete_profile(name):
    localpath = os.path.join("profiles", name + ".json")
    if not os.path.exists(localpath):
        print(f"Profile {name} does not exist")
        return

    os.remove(localpath)
    print(f"Profile {name} deleted successfully")

def edit_profile(name):
    show_profile(name)
    profile = loader(name)
    description = input("Enter new description (leave blank to keep current): ")
    if description:
        profile["description"] = description

    tools = input("Enter new tools (comma separated, leave blank to keep current): ")
    if tools:
        profile["tools"] = tools.split(",")
    
    saver(name,profile)
    print(f"Profile {name} updated successfully")





        