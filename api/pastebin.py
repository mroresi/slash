import requests 
import json 
import time 

from core import (
    banner,
    color,
    symbol,
    clear,
    highlight,
    info_highlight,
    error_highlight,
    css
)

from api.extract import extract 
from api.timeline import get_timeline

class gathered:
    links = []
    includes = []
def search(value):
    print(f"{symbol.log} Searching {color.bold}{color.orange}{value}{color.reset} on {color.bold}Pastebin{color.reset}...")
        
    req = requests.get(f"https://psbdmp.cc/api/search/domain/{value}",timeout=25)

    db = json.loads(req.text)
    cnt = db["count"]
    data = db["data"]
    out = f"{symbol.paste_found}:\n"
    
    # Get timeline instance
    timeline = get_timeline(value)

    if(cnt!=0):
        for i in range(0,cnt):
            #print(f"{symbol.paste_found} {color.bold}Paste{color.reset} : [{color.red}{color.underline}https://pastebin.com/{data[i]['id']}{color.reset}] {color.bold}Include{color.reset} : {color.reset}[{color.orange}{data[i]['text']}{color.reset}]")
            #time.sleep(4)
            include = ''
            includes = data[i]['text'].split()
            for w in includes:
                include+=w
            
            extract.phone("pastebin",include)
            
            paste_url = "https://pastebin.com/"+data[i]['id']
            out+=f"     {color.reset}[{color.whitebg}{data[i]['id']}{color.reset}] {color.bold}Paste{color.reset} : [{color.red}{color.underline}{paste_url}{color.reset}] {color.bold}Include{color.reset} : {color.reset}[{color.include}{include}{color.reset}]\n"
            gathered.includes.append({data[i]['id']:data[i]['text']})
            gathered.links.append({data[i]['id']:paste_url})
            
            # Add to timeline
            timeline.add_paste_event(data[i]['id'], paste_url)

    if(len(gathered.links)!=0):
        print(out)
    print(f"{symbol.log} Pastebin search finished! {color.red}{len(gathered.links)}{color.reset} results found for {color.bold}{color.orange}{value}{color.reset}.")
    #print(gathered.includes)