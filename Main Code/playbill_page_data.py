
import requests, json, csv

from bs4 import BeautifulSoup

all_playbills = []
with open ('playbill_links_cleaned.json', 'r') as json_data:
	d = json.load(json_data)
	for line in d:

		playbill_data = {
			'show_title': [],
			'show_date': [],
			'theater_name': [],
			'location': [],
			'production_staff': [],
			'cast_member': [],
			'headliner': [],
			'advertisement': []
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

				if key == 'data':
					if 'title' in a_annotation[key] and 'type' in a_annotation[key]:
						if 'value' in a_annotation[key]['title'] and 'type' in a_annotation[key]:
							#print(a_annotation[key]['title']['value'])
							#print(a_annotation[key]['type']['value'])
							playbill_data['show_title'].append(a_annotation[key]['title']['value'])
							playbill_data['show_title'].append(a_annotation[key]['type']['value'])

					if 'date_opened' in a_annotation[key]:
						if 'value' in a_annotation[key]['date_opened']:
							#print(a_annotation[key]['date_opened']['value'])
							playbill_data['show_date'].append(a_annotation[key]['date_opened']['value'])

					if 'date_closed' in a_annotation[key]:
						if 'value' in a_annotation[key]['date_closed']:
							#print(a_annotation[key]['date_closed']['value'])
							playbill_data['show_date'].append(a_annotation[key]['date_closed']['value'])

					if 'theater' in a_annotation[key]:
						if 'value' in a_annotation[key]['theater']:
							#print(a_annotation[key]['theater']['value'])
							playbill_data['theater_name'].append(a_annotation[key]['theater']['value'])

					if 'location' in a_annotation[key]:
						if 'value' in a_annotation[key]['location']:
							#print(a_annotation[key]['location']['value'])
							playbill_data['location'].append(a_annotation[key]['location']['value'])

					if 'role' in a_annotation[key] and 'name' in a_annotation[key]:
						if 'value' in a_annotation[key]['role'] and 'name' in a_annotation[key]:
							# print(a_annotation[key]['role']['value'])
							# print(a_annotation[key]['name']['value'])
							playbill_data['production_staff'].append(a_annotation[key]['role']['value'])
							playbill_data['production_staff'].append(a_annotation[key]['name']['value'])

					if 'actor' in a_annotation[key] and 'character' in a_annotation[key] and 'description' in a_annotation[key]:
						if 'value' in a_annotation[key]['actor'] and 'character' in a_annotation[key] and 'description' in a_annotation[key]:
							# print(a_annotation[key]['actor']['value'])
							# print(a_annotation[key]['character']['value'])
							# print(a_annotation[key]['description']['value'])
							playbill_data['cast_member'].append(a_annotation[key]['actor']['value'])
							playbill_data['cast_member'].append(a_annotation[key]['character']['value'])
							playbill_data['cast_member'].append(a_annotation[key]['description']['value'])

					if 'actor' in a_annotation[key]:
						if 'value' in a_annotation[key]['actor']:
							#print(a_annotation[key]['actor']['value'])
							playbill_data['headliner'].append(a_annotation[key]['actor']['value'])

					if 'company' in a_annotation[key] and 'address' in a_annotation[key] and 'goods' in a_annotation[key]:
						if 'value' in a_annotation[key]['company'] and a_annotation[key]['address'] and a_annotation[key]['goods']:
							# print(a_annotation[key]['company']['value'])
							# print(a_annotation[key]['address']['value'])
							# print(a_annotation[key]['goods']['value'])
							playbill_data['advertisement'].append(a_annotation[key]['company']['value'])
							playbill_data['advertisement'].append(a_annotation[key]['address']['value'])
							playbill_data['advertisement'].append(a_annotation[key]['goods']['value'])
		# add it to the list
		all_playbills.append(playbill_data)
		json.dump(all_playbills,open('playbill_page_data.json','w'), indent=4)
