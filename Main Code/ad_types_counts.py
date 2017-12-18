import json, csv

data = json.load(open ('ads.json'))

counts = {}

for playbill in data:
    for key in playbill:
        if key not in counts:
            counts[key] = {}
        for values in playbill[key]:
            if values not in counts[key]:
                counts[key][values] = 0
            counts[key][values] = counts[key][values] + 1
# print(counts)

json.dump(counts,open('ads_dump.json','w'), indent=4)

#Advertisements
advertisements = counts["advertisement"]
advertisements = sorted(advertisements.items(), key=lambda x:x[1], reverse=True)

with open('ad_types_counts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(advertisements)
