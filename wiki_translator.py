

import sys
import webbrowser

import pyperclip
import requests
import bs4

def format_searchterm(searchterm):
    formated_searchterm = searchterm.strip('.,;:-?!() ')
    return formated_searchterm.replace(' ', '_')

searchterm = str(pyperclip.paste())
formated_searchterm = format_searchterm(searchterm)

eng_url = 'https://en.wikipedia.org/wiki/' + formated_searchterm
response = requests.get(eng_url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print('Kein englischer Wikipedia-Eintrag vorhanden')
    print(eng_url)
    sys.exit()

eng_wikisoup = bs4.BeautifulSoup(response.text, "html5lib")
link_to_german = eng_wikisoup.select('.interwiki-de .interlanguage-link-target')

try:
    ger_url = link_to_german[0].get('href')
except IndexError:
    print('Kein deutscher Wikipedia-Eintrag vorhanden')
else:
    webbrowser.open_new_tab(ger_url)