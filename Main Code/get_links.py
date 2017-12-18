
from bs4 import BeautifulSoup

import requests, json

link_list = []

total_pages = 0
while total_pages <= 8:
	total_pages = total_pages + 1
	url = "http://ensemble.nypl.org/programs?page=" + str(total_pages)

	print(url)

	playbill_page = requests.get(url)

	if playbill_page.status_code != 200:
		print ("There was an error with", url)

	html = playbill_page.text

	soup = BeautifulSoup(html, "html.parser")

	all_links = soup.find_all('a', string = 'View')

	for a_link in all_links:
		link = a_link.get('href')

		if link:
			link_text = a_link.text
			html = "http://ensemble.nypl.org/" + link
			link_list.append(html)

json.dump(link_list,open('playbill_links.json','w'), indent=4)
