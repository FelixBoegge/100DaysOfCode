import csv


def show(x):
    poke_count = 0
    poke_dict = {}
    attributes = ['Number', 'Name', 'Type', 'HP', 'Damage', 'Status']
    with open('Pokemonlist.csv', mode='r') as file:
        pokemons = csv.DictReader(file, delimiter='\t', fieldnames=attributes)
        next(pokemons)
        for pokemon in pokemons:
            if x == 'all':
                print(pokemon)
            poke_count += 1
        print(poke_count)
        return poke_count


def add(temp):
    with open('Pokemonlist.csv', mode='a', newline='') as file:
        csv_writer = csv.writer(file, delimiter='\t')
        csv_writer.writerow(temp)


def show_spec(search, att, mode):
    with open('Pokemonlist.csv', mode='r') as file:
        temp = []
        pokemons = csv.DictReader(file, delimiter='\t')
        for pokemon in pokemons:
            if mode == 'att':
                if pokemon['Name'] == search:
                    print(f"{att}: {pokemon[att]}")
            elif mode == 'att_all':
                if pokemon[search] == att:
                    print(pokemon)


def change(name, att, att_new):
    with open('Pokemonlist.csv', mode='r') as file:
        pokelist = []
        attributes = ['Number', 'Name', 'Type', 'HP', 'Damage', 'Status']
        pokemons = csv.DictReader(file, delimiter='\t', fieldnames=attributes)
        next(pokemons)
        for pokemon in pokemons:
            pokelist.append(pokemon)
        for pokemon in pokelist:
            if pokemon['Name'] == name:
                pokemon[att] = att_new
        keys = pokelist[0].keys()
        with open('Pokemonlist.csv', mode='w', newline='') as cfile:
            writer = csv.DictWriter(cfile, keys, delimiter='\t')
            writer.writeheader()
            writer.writerows(pokelist)


action = 1
while action in [1, 2, 3, 4, 5]:
    action = int(input("Menu: what do you want to do:"
                       "\n1         read content of file"
                       "\n2         add a Pokemon to the file"
                       "\n3         read specific data"
                       "\n4         show all Pokemon with specific data"
                       "\n5         change specific data"
                       "\nany key   Quit\n"))

    if action == 1:
        show('all')
    elif action == 2:
        print("Now you can add a new Pokemon to the file:")
        poke_count = show('count')
        pokename = input("Name of Pokemon: ")
        poketype = input("Type of Pokemon: ")
        pokemaxHP = int(input("Maximum HP of Pokemon: "))
        pokedam = int(input("Damage the Pokemon will deal: "))
        temp_inp = [poke_count+1, pokename, poketype, pokemaxHP, pokedam, 'active']
        add(temp_inp)
    elif action == 3:
        name = input("Which Pokemon are you looking for?: ")
        att = input("Which attribute do you want to see? (Number, Type, HP, Damage, Status): ")
        show_spec(name, att, 'att')
    elif action == 4:
        att = input("Which attribute do you want to examine? (Number, Type, HP, Damage, Status): ")
        att_val = input("Which attribute-value are you looking for?: ")
        show_spec(att, att_val, 'att_all')

    elif action == 5:
        name = input("Which Pokemon do you want to change?: ")
        att = input("Which attribute do you want to change? (Number, Name, Type, HP, Damage, Status): ")
        att_new = input("New value for attribute: ")
        change(name, att, att_new)
