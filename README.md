# pfch_2017

This repository contains code used to explore the New York Public Library Ensemble website: http://ensemble.nypl.org/about.

The repository contains four folders. The Main Code folder contains the Python code files. The File Outputs folder contains the files output by the main Python code files. The Pairings folder contains the code and files output used to match directors with actors, directors with headliners, playwrights with actors, playwrights with headliners, and producers with headliners. The Visualizations folder contains all of the files used to create the visualizations for the project.

In order to run the main code, download the Python library Beautiful Soup.

Main Code
get_links.py – Gets links to individual playbill pages using Beautiful Soup and outputs playbill_links.json

playbill_page_data.py – Extracts data from individual playbill pages and outputs playbill_page_data.json

playbill_counts.py – Counts each metadata field and outputs counts.json. Also outputs each metadata fields to its own CSV file: headliners.csv, show_titles.csv, show_dates.csv, theater_names.csv, locations.csv, production_staff.csv, cast_members.csv, advertisements.csv.

playbill_data_zipped.py – Combs each playbill page and zips together the dictionaries for show title and type, production staff role and name, actor and character, advertisement company and address

ads.py – Extracts only the ad types from individual playbill pages and outputs ad_types.json

ad_types_counts.py – Counts types of ads and outputs ad_types_counts.csv and ads_dump.json

File Outputs
playbill_links_cleaned.json - playbill_links.json contains five links for which there was no corresponding JSON file. These five links have been removed in playbill_links_cleaned.json, because this project was a proof of concept exercise and did not require total comprehensiveness. The five links are: http://ensemble.nypl.org//transcriptions/514a37280f7ca62c33000091
http://ensemble.nypl.org//transcriptions/514a35cf0f7ca62c33000003
http://ensemble.nypl.org//transcriptions/514a30a75c5a8c2894000146
http://ensemble.nypl.org//transcriptions/514a22a00f7ca6251300027d
http://ensemble.nypl.org//transcriptions/514a21d60f7ca62513000101
