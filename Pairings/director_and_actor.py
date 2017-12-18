import json, csv

data = json.load(open ('playbill_data_zipped.json'))

dir_counts = {}


for playbill in data:


  for staff in playbill['production_staff']:

    # is it the director?
    if 'Director' in staff:

      # is our director in our dir_counts yet?
      if staff['Director'] not in dir_counts:
        # no, so make a it an empty dict so we can add the actors names to it
        dir_counts[staff['Director']] = {}

      # now we know the director exists in the dir_counts
      for actor in playbill['cast_member']:

        # actor looks like this {'John Rogers': 'Lieut. Johann'} but we don't know the key (here 'John Rogers') so loop through the keys (even though there is only one)
        for actor_name in actor:

          #is this actor in the director count yet?
          if actor_name not in dir_counts[staff['Director']]:
            dir_counts[staff['Director']][actor_name] = 0

          # increment it by one
          dir_counts[staff['Director']][actor_name] = dir_counts[staff['Director']][actor_name] + 1

print(json.dumps(dir_counts,indent=4))

json.dump(dir_counts,open('director_and_actor.json','w'), indent=4)
