import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_413818.json"
jsData = urllib.request.urlopen(url, context=ctx).read().decode()
js = json.loads(jsData)
#print(json.dumps(js, indent=4))
result = 0
for comment in js["comments"]:
    result += comment["count"]
print(result)