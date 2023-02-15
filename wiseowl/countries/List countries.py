import csv


def get_contents_of_file(continent_name):
    country_list = []
    try:
        with open(continent_name + '.csv', 'r') as file:
            print(continent_name)
            print('-' * len(continent_name))
            for line in csv.reader(file):
                country, capital = line[0], line[1]
                print(f'{country} ({capital})')

    except FileNotFoundError:
        print('No such continent!')


def get_country_dict(country_list):
    return country_list


def print_results(name, country_list):
    pass


# choose continent to show data for
continent_name = "Oceania"

get_contents_of_file(continent_name)
