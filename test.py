import base64
import requests

url = 'https://api.github.com/repos/akshaypradheep/apitxt3/contents/msg.txt'
req = requests.get(url)
req = req.json()  
content = base64.decodestring(req['content'])
print content