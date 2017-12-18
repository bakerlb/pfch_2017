import json, csv

data = json.load(open ('playbill_data_zipped.json'))

dir_counts = {}


for playbill in data:


  for staff in playbill['production_staff']:

    # is it the director?
    if 'Playwright' in staff:

      # is our director in our dir_counts yet?
      if staff['Playwright'] not in dir_counts:
        # no, so make a it an empty dict so we can add the actors names to it
        dir_counts[staff['Playwright']] = {}

      # now we know the director exists in the dir_counts
      for actor in playbill['headliner']:
          if actor not in dir_counts[staff['Playwright']]:
            dir_counts[staff['Playwright']][actor] = 0

          # increment it by one
          dir_counts[staff['Playwright']][actor] = dir_counts[staff['Playwright']][actor] + 1

print(json.dumps(dir_counts,indent=4))

json.dump(dir_counts,open('playwright_and_headliner.json','w'), indent=4)
