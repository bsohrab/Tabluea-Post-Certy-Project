from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_moves'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

digest = soup.find('table')
for dbenter in digest.findAll('tr'):
    print(dbenter.text)
    radiogogo = dbenter.find('a')['href']

    moveset_url  = 'https://bulbapedia.bulbagarden.net'+ radiogogo
    moveset_page = requests.get(moveset_url)
    movesoup     = BeautifulSoup(moveset_page.content, "html.parser")
    move_table = movesoup.find('table', {"class": "roundy"})
    # print(move_table)
    dates = soup.findAll("div", {"id": re.compile('date.*')})
    # movable = move_table.findAll('a', title=re.compile('.* (Pokemon)'))
    # for movedbenter in move_table.findAll('a', title=True):
    #     print(movedbenter.string)
    #     # if "(Pokemon)" in movedbenter['title']:
    #     #     print(movedbenter['text'])
    for link in move_table.findAll('a', title=True):
        if link.find(text=re.compile("(Pokemon)")):
            thelink = link
            break

    print(thelink)





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