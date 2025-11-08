import argparse
import requests
import sys
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument("url", nargs=1, help="metallum release page")

args = parser.parse_args()

if __name__ == '__main__':
	with open(args.url[0]) as r:
		out = ""
		soup = BeautifulSoup(r, 'html.parser')
		for each in soup.find(class_="table_lyrics").tbody.find_all(class_=['even', 'odd']):
			out += each.findChild().contents[1][:1] + "|" + each.find(class_='wrapWords').contents[0].strip() + "|" + out + each.find(attrs={'align': 'right'}).contents[0] + '\n'
		title = soup.title.contents[0].rsplit('-',1)[0]
		with open(f'out/{title}.txt', "w", encoding="utf-8") as f:
			f.write(out)
	sys.exit(0)
