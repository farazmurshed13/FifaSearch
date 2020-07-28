import soFifaScraper as sFS
import pandas as pd

bank = sFS.get_player_data()

df = pd.read_json(open(bank, 'r'))
df.set_index('name', inplace=True)
print(df.head())
