import csv
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

import numpy as np
from IPython.display import display


def compatiblePokemon(movesetlink, moves_df):

    #find the url link by move
    moveset_url = 'https://bulbapedia.bulbagarden.net' + movesetlink
    moveset_page = requests.get(moveset_url)

    learnPokemon = pd.read_html(moveset_page.text)
    print(learnPokemon)


    #df[''] = df.replace(AXIS=1,INDEX=2)
    #approach 2
    filt = moves_df.isin(learnPokemon[3])
    moves_df.loc[filt] = True
    #approach 3
    for pokemon in learnPokemon[3]:
        #i think this below is a look up and now a value changer
        moves_df[pokemon] = True
    #check columns ## for matches in the moves df, and if there are any matches, make the
    #use all results to find, match, and indicate true value if a pokemon learns a move, false if not
    #update the column by the pokemon name found. maybe a loop through the learn pokemon column 3
    # series or maybe another way exists...

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



moves_df = names_df.assign(**dict.fromkeys(names_series.tolist(),0))

index = 1

#append a row of blanks to names_df after adding the contents for column 3 to the moves_df as headers
#then pass that later to the defined function to relay the searching for contested values
moves_df.to_csv("C:\\Users\\12024\\source\\repos\\cotainment folder - pkmn\\moves.csv")
names_df.to_csv("C:\\Users\\12024\\source\\repos\\cotainment folder - pkmn\\pokemon names.csv")
quit()

#loop through each table entry for the moves in pokemon
soup = BeautifulSoup(movespage.content, "html.parser")
move_table = soup.find('table')
for currentMove in move_table.findAll('tr'):
    radiogogo = currentMove.find('a')['href']
    #use the hyperlink direction to enter the website for the pokemon move
    #and scrape all the pokemon names who can learn that move
    pkmn_names = compatiblePokemon(radiogogo, names_df)
    #add the pokeon names to the current row, next columns
    moves_df.append(pkmn_names)

#Convert the dataframe to a csv
pokemonDataframe.to_csv("pokemon_moves_spreadsheet")

