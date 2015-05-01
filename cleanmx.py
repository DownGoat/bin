import urllib.request
import sys

list_url = "http://support.clean-mx.de/clean-mx/xmlviruses.php?"


url_data = urllib.request.urlopen(list_url).read().decode("ISO-8859-1")

links = []
lines = url_data.split("\n")
a = open("cleanmx.txt", "w")
for line in lines:
    line = line.strip()
    if line.startswith("<url>"):
        url = line[14:-9]
        a.write(url + "\n")

a.close()



