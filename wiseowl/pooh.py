import pandas as pd

path = 'Pooh.xlsx'

tournament_data = pd.read_excel(path)
#print(tournament_data.info())
winners_table = tournament_data.sort_values('Poohsticks score', ascending=False)
#print(winners_table)
winners_table = winners_table.rename(columns={'Name': 'Character', 'Poohsticks score': 'Score', 'Matches Played': 'Played'})
#print(winners_table.head(n=3))

print(winners_table.agg({'Score': ['min', 'max', 'median', 'mean'], 'Played': ['min', 'max', 'median', 'mean']}))

#df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})