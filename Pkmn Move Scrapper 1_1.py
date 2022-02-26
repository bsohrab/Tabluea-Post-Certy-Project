import csv

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


def compatiblePokemon():
    moveset_url = 'https://bulbapedia.bulbagarden.net' + radiogogo
    moveset_page = requests.get(moveset_url)
    movesoup = BeautifulSoup(moveset_page.content, "html.parser")
    move_table = movesoup.find('table', {"class": "roundy"})
    print(move_table)
    for pkmn in move_table.findAll('a', {"title": re.compile('(Pokémon)')}):
        print(pkmn.string)
url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_moves'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

digest = soup.find('table')
for dbenter in digest.findAll('tr'):
    print(dbenter.text)
    radiogogo = dbenter.find('a')['href']


    # movable = move_table.findAll('a', title=re.compile('.* (Pokemon)'))
    # for movedbenter in move_table.findAll('a', title=True):
    #     print(movedbenter.string)
    #     # if "(Pokemon)" in movedbenter['title']:
    #     #     print(movedbenter['text'])



with open("movelist.csv",'w', newline='') as veri:
    writer = csv.DictWriter(veri, fieldnames)
    writer.writeheader()



# blackhole = soup.find('table').find('tr')
# print(blackhole)
# blackhole2 = blackhole.find('a')
# print(blackhole2)
# blacktroll = blackhole.findAll('a')
# print(blacktroll)
#
#
# for herfs in blackhole.findAll('a'):
#     print(herfs)
#     print(herfs['href'])
# # df_list = pd.read_html(page.text)
# df = df_list[0]
# print(df)
# df.to_csv("C:\\Users\\12024\\source\\repos\\cheep.csv")