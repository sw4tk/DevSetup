import platform
import subprocess
from tools_metadata import TOOL_METADATA,DEPENDENCY_TOOLS

ALREADY_INSTALLED = [
    'existing package already installed',
    'already installed',
    'already exists',
    'already in path',
    'no newer',
    'already up to date',
]

def install_tool(tool,installation_data):
    currentplatform = platform.system().lower()
    if currentplatform == "windows":
        if tool in DEPENDENCY_TOOLS:
            parent = DEPENDENCY_TOOLS[tool]
            print(f'Skipping {tool} (Installed with {parent} runtime)')
            installation_data['installed'].append(tool)
            return
        mainpackage = TOOL_METADATA[currentplatform][tool]
        print(f"Installing {mainpackage} on Windows")
        result = subprocess.run(
    [
        "winget",
        "install",
        "--id",
        mainpackage,
        "--exact",
        "--accept-package-agreements",
        "--accept-source-agreements"
    ],
    capture_output=True,
    text=True
)
        output = result.stdout + result.stderr
        if result.returncode == 0:
            print(f' [OK] Installed {mainpackage}')
            installation_data['installed'].append(tool)
            return

        for line in ALREADY_INSTALLED:
            if line in output:
                print("[OK] Already installed")
                installation_data['installed'].append(tool)
                return
      
        else:
            print(f'[ERROR] Failed to install {mainpackage}')
            installation_data['failed'].append(tool)
            return
        
        
        
