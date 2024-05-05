from bs4 import BeautifulSoup
import json

file = open("all_frogs.html.txt", "r", encoding="utf-8")
html = file.read().replace("\n","")
file.close()

soup = BeautifulSoup(html, "lxml")
tableRows = soup.find_all("tr")
print("ok go")

#0 is species name
#1 is photos/no photos
#2 is  sounds/blank
#3 is red list status (endangered?)
#4 is vernacular/common name or blank
#5 is family
#6 is order (anura because they are all frogs)

out = open("out.txt","w", encoding="utf-8")

data = []

for tr in tableRows:
    tds = tr.find_all("td")
    if len(tds) != 0:
        obj = {}
        obj["name"] = tds[0].a.string
        obj["has_photos"] = len(tds[1].find_all("a"))
        if obj["has_photos"]: 
            obj["photos"] = tds[1].find_all("a")[0]["href"]
        obj["redlist_status"] = "NE" if tds[3].small.string == None else tds[3].small.string.split("(")[1][0:2]
        obj["vernacular_name"] = []
        vnstr = list(tds[4].small.stripped_strings)
        if len(vnstr):
            vnlist = vnstr[0].split("; ")
            for vn in vnlist:
                obj["vernacular_name"].append(vn)
        obj["family"] = list(tds[5].small.stripped_strings)[0]

        data.append(obj)

out.write(json.dumps(data))
out.close()