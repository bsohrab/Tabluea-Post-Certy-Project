import csv
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

import numpy as np
from IPython.display import display


def compatiblePokemon(movesetlink, moves_df, axis):

    #find the url link by move
    moveset_url = 'https://bulbapedia.bulbagarden.net' + movesetlink
    moveset_page = requests.get(moveset_url)
    moveset_soup = BeautifulSoup(moveset_page.content, "html.parser")

    try:
        moveset_table = moveset_soup.find('table', {'class':'roundy'})
        learnPokemon = pd.read_html(str(moveset_table))[0]
        listpokemon = learnPokemon.loc[:, ('Pokémon', 'Pokémon.1')]
        moves_dfcolumns = moves_df.columns.to_list()
        listpokemon = set(listpokemon).intersection(moves_dfcolumns)
        moves_df.loc[axis, listpokemon] = True
        return moves_df
    except:
        return moves_df






pokemonDataframe = pd.DataFrame()
#retrieve the URL site landing
url_moves = 'https://bulbapedia.bulbagarden.net/wiki/List_of_moves'
url_names = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
movespage = requests.get(url_moves)
namespage = requests.get(url_names)


moves_df = pd.read_html(movespage.text)[1] # or [1], [2]
#limit to generation 1 for now
#filter our the names that repeat twice indicating regional forms
names_df     = pd.read_html(namespage.text)[1]
names_series = names_df.dropna(subset =['Kdex']).loc[:,'Pokémon']
moves_df     = moves_df.assign(**dict.fromkeys(names_series.tolist(),0))
index = 0

#append a row of blanks to names_df after adding the contents for column 3 to the moves_df as headers
#then pass that later to the defined function to relay the searching for contested values
moves_df.to_csv("C:\\Users\\12024\\source\\repos\\cotainment folder - pkmn\\moves.csv")


#loop through each table entry for the moves in pokemon
soup = BeautifulSoup(movespage.content, "html.parser")
move_table = soup.find('table')
for currentMove in move_table.findAll('tr'):
    radiogaga = currentMove.find('a')['href']
    #use the hyperlink direction to enter the website for the pokemon move
    #and scrape all the pokemon names who can learn that move
    if "(move)" not in radiogaga:
        continue
    else:
        moves_df = compatiblePokemon(radiogaga, moves_df, index)
        index+=1
    #add the pokeon names to the current row, next columns



#Convert the dataframe to a csv
moves_df.to_csv("C:\\Users\\12024\\source\\repos\\cotainment folder - pkmn\\moves&pokemon.csv")

