 # To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
total_tag = list()

for tag in tags:
    total_tag.append(tag.get('href', None))

print(total_tag[17])

#http://py4e-data.dr-chuck.net/known_by_Nikiya.html
#http://py4e-data.dr-chuck.net/known_by_Allana.html
#http://py4e-data.dr-chuck.net/known_by_Primrose.html
#http://py4e-data.dr-chuck.net/known_by_Triniti.html
#http://py4e-data.dr-chuck.net/known_by_Frederick.html
#http://py4e-data.dr-chuck.net/known_by_Keilan.html
#http://py4e-data.dr-chuck.net/known_by_Damian.html
