import pandas as pd


pokebox = pd.read_csv('moves&pokemon.csv')

#replace, only on the pokemon rows
#0 with FALSE and True with TRUE
pokebox.where(pokebox == 0, "FALSE", inplace = True)
print(pokebox.head(20))