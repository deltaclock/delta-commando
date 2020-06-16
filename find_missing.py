import csv
import json
from pprint import pprint

with open("delta-profile.json") as f:
    delta_json = json.load(f)

delta_pkgs = set()
for pkg in delta_json.get("packages"):
    delta_pkgs.add(pkg["name"].lower())

#print(delta_pkgs)

with open('packages.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        name = ".".join(row[0].split(".")[:-1]).lower()
        name_flare = f"{name}.flare"
        name_fire = f"{name}.fireeye"
        #print({name, name_fire, name_flare})
        if delta_pkgs.isdisjoint({name, name_fire, name_flare}):
            pprint(row)