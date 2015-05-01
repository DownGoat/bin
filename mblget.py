from lxml import html
import urllib.request
import sys

list_url = "http://www.malwareblacklist.com/showAllMalwareURL.php?userName=Guest&sessionID=&downloadOption=0&ID=sF7h850HJtu75sadlFH46LKnnbJGFH679gJC8"

url_data = None

a = open("/home/dwg/Downloads/html.html", "r")

url_data = a.read()
a.close()
url_data = url_data.replace("<wbr>", "")
xpath = "/html/body/table[2]/tbody/tr[59]/td[2]/span"

tree = html.fromstring(url_data)

links = tree.xpath("//td[@style='text-align:left; padding-left:5px; padding-right:5px;']/text()")
links2 = tree.xpath("//span[@style='font-size:10px']/text()")

filtered = []


for l in links:
    if len(l) != 1 and len(l) != 7:
        filtered.append(l.strip())

filtered += links2

a = open("list.txt", "w")
for x in filtered:
    a.write(x + "\n")

a.close()

