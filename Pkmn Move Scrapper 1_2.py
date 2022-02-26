import csv
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


def compatiblePokemon(movesetlink):
    pd_pokemon = pd.DataFrame()
    moveset_url = 'https://bulbapedia.bulbagarden.net' + movesetlink
    moveset_page = requests.get(moveset_url)
    movesoup = BeautifulSoup(moveset_page.content, "html.parser")
    move_table = movesoup.find('table', {"class": "roundy"})
    print(move_table)
    for pkmn in move_table.findAll('a', {"title": re.compile('(Pokémon)')}):
        print(pkmn.string)
        pd_pokemon.append(pkmn.string)

    return pd_pokemon



pokemonDataframe = pd.DataFrame()
#retrieve the URL site landing
url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_moves'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
move_table = soup.find('table')
index = 1
#loop through each table entry for the moves in pokemon
for currentMove in move_table.findAll('tr'):
    print(currentMove.text)
    #append to the current number row the basic information on the pokemon move
    #headers: Attack Name[1] | Attack Type[2] | Move Type[3] | Base Power[5] | Accuracy[6] | Generation [7]
    pokemonDataframe.append(currentMove[1])
    print(pokemonDataframe)
    radiogogo = currentMove.find('a')['href']
    #use the hyperlink direction to enter the website for the pokemon move
    #and scrape all the pokemon names who can learn that move
    pkmn_names = compatiblePokemon(radiogogo)
    #add the pokeon names to the current row, next columns
    pokemonDataframe.append(pkmn_names)

#Convert the dataframe to a csv
pokemonDataframe.to_csv("pokemon_moves_spreadsheet")

