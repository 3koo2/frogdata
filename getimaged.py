import json

f = open("frogs.json", "r")
arr = json.loads(f.read())
f.close()

ic = 0
f = open("imaged.lines", "w")
for i in arr:
    if i['has_photos']:
        f.write(str(ic)+"\n")
    ic+=1
f.close()
