import json
import requests
import sys
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=10000&term=" +sys.argv[1] )   
print(json.dumps(response.json(),indent=3))
o= response.json()
i=0
for result in o["results"]:
    print(result["trackName"])
    i+=1
print(i)    