tall_buildings = {
    'Burj Khalifa': (1, 'Dubai', 'UAE', 828),
    'Shanghai Tower': (2, 'Shanghai', 'China', 632),
    'Abraj Al-Bait Clock Tower': (3, 'Mecca', 'Saudi Arabia', 601),
    'Ping An Finance Center': (4, 'Shenzhen', 'China', 599),
    'Lotte World Tower': (5, 'Seoul', 'South Korea', 554),
    'One World Trade Center': (6, 'New York City', 'United States', 541)
}

for name, info in tall_buildings.items():
    print(f'{name} in {info[1]} is {info[3]} meters high')