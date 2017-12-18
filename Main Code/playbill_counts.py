import json, csv

data = json.load(open ('playbill_page_data.json'))

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

json.dump(counts,open('counts.json','w'), indent=4)

#Headliners
headliners = counts["headliner"]
headliners = sorted(headliners.items(), key=lambda x:x[1], reverse=True)

# for headliner in headliners:
#     if headliner[1]>=6:
#         print(headliner)

with open('headliners.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(headliners)

#Show Titles
show_titles = counts["show_title"]
show_titles = sorted(show_titles.items(), key=lambda x:x[1], reverse=True)

with open('show_titles.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(show_titles)

#Show Dates
show_dates = counts["show_date"]
show_dates = sorted(show_dates.items(), key=lambda x:x[1], reverse=True)

with open('show_dates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(show_dates)

#Theater Names
theater_names = counts["theater_name"]
theater_names = sorted(theater_names.items(), key=lambda x:x[1], reverse=True)

with open('theater_names.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(theater_names)

#Theater Locations
locations = counts["location"]
locations = sorted(locations.items(), key=lambda x:x[1], reverse=True)

with open('locations.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(locations)

#Production Staff
production_staff = counts["production_staff"]
production_staff = sorted(production_staff.items(), key=lambda x:x[1], reverse=True)

with open('production_staff.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(production_staff)

#Cast Members
cast_members = counts["cast_member"]
cast_members = sorted(cast_members.items(), key=lambda x:x[1], reverse=True)

with open('cast_members.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(cast_members)

#Advertisements
advertisements = counts["advertisement"]
advertisements = sorted(advertisements.items(), key=lambda x:x[1], reverse=True)

with open('advertisements.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(advertisements)
