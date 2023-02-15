colours = ['Purple', 'Green', 'Yellow']
film = 'Sillicone Valley'
number = 42

my_stats = (colours, film, number)

for i, stats in enumerate(my_stats):
    print(f'Item {i+1} has type {type(stats)}: {stats}')