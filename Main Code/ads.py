#json load (not loads - look it up) to open file, store into a variable, list of urls, write for loop to go through each url

import requests, json, csv

#this is where the for loop starts, indent everything after it
from bs4 import BeautifulSoup

# matt: make a list that will hold them all
all_playbills = []
with open ('playbill_links_cleaned.json', 'r') as json_data:
	d = json.load(json_data)
	for line in d:

		playbill_data = {
			'advertisement': [],
		}

		# replace "http....." with variable - that's what will change each time
		url = str(line) + '.json'
		print(url)
		playbill_page = requests.get(url)

		if playbill_page.status_code != 200:
			print ("There was an error with", url)

		page_json = playbill_page.text

		data = json.loads(page_json)
		#print(data['transcription'])
		for a_annotation in data['transcription']['annotations']:
			for key in a_annotation:
				# if key == 'name':
				# 	print(a_annotation[key])

				if key == 'data':

					if 'company' in a_annotation[key] and 'address' in a_annotation[key] and 'goods' in a_annotation[key]:
						if 'value' in a_annotation[key]['company'] and a_annotation[key]['address'] and a_annotation[key]['goods']:

							playbill_data['advertisement'].append(a_annotation[key]['goods']['value'])
		# add it to the list
		all_playbills.append(playbill_data)
		json.dump(all_playbills,open('ad_types.json','w'), indent=4)
