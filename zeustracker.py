import urllib.request


rss_url = "https://zeustracker.abuse.ch/monitor.php?urlfeed=binaries"
f = urllib.request.urlopen(rss_url)

xml_data = f.read()
xml_data = xml_data.decode("utf-8").split("\n")

a = open("zeuslist.txt", "w")

for line in xml_data:
    if line.startswith("<description>URL:"):
        url = line.split(" ")[1][:-1]
        a.write(url + "\n")
a.close()
