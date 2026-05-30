from scanner import check_tool
from tools import tools


for tool in tools:
    print(f'{tool} : {check_tool(tool)}')