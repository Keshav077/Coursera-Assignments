import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.py4e.com/code3/mbox.txt"
xmlData = urllib.request.urlopen(url,context=ctx).read()
