import csv
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


moves_df = pd.read_csv("C:/Users/12024/source/repos/cotainment folder - pkmn/moves.csv")

pound_move = pd.read_csv("C:/Users/12024/source/repos/cotainment folder - pkmn/move pound pokemon.csv")

print(moves_df.head(25))
print(moves_df.loc[2,'Clefairy'])

print(listpokemon, listpokemon.dtypes)
print(moves_dfcolumns, moves_df.dtypes)

listpokemon     = pound_move.loc[:,'Pokémon.1']
moves_dfcolumns =  moves_df.columns.to_list()
listpokemon = set(listpokemon).intersection(moves_dfcolumns)
moves_df.loc[2, listpokemon] = True

print(listpokemon)

#search both lists and return a list of matching values, then use
# # that list to update values for the moves_df dataframe

#
#
print(moves_df.loc[2,listpokemon])
print(moves_df.iloc[2,10:100])
#
# moves_df.to_csv("C:/Users/12024/source/repos/cotainment folder - pkmn/move check pound.csv")
fly
