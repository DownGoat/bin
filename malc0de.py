import urllib.request
import sys

list_url = "http://malc0de.com/rss/"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"


u = urllib.request.Request(list_url, headers={"User-Agent": user_agent})

url_data = urllib.request.urlopen(u).read().decode("ISO-8859-1")

links = []
lines = url_data.split("\n")
a = open("malc0de.txt", "w")
for line in lines:
    line = line.strip()
    if line.startswith("<description>URL:"):
        url = line.split(" ")[1][:-1]
        a.write(url + "\n")

a.close()



