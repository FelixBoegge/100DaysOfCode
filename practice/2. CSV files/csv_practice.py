import csv


def show(x):
    line_count = 0
    with open('Pokemonlist.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for line in csv_reader:
            if x == 1:
                print(line)
            line_count += 1
    return line_count


def load(search_name, att):
    with open('Pokemonlist.csv', mode='r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for line in reader:
            if line['name'] == search_name:
                return line[att]


def add(temp):
    with open('Pokemonlist.csv', mode='a', newline='') as file:
        csv_writer = csv.writer(file, delimiter='\t')
        csv_writer.writerow(temp)


action = 1
while action in [1, 2, 3, 4, 5, 6]:
    action = int(input("Menu: what do you want to do:"
                       "\n1  read content of file"
                       "\n2  add a Pokemon to the file"
                       "\n3  read specific data"
                       "\n4  show all Pokemon with specific data"
                       "\n5  change specific data"
                       "\n6  Quit\n"))

    if action == 1:
        show(1)

    if action == 2:
        print("Now you can add a new Pokemon to the file:")
        pokenum = show(0)
        pokename = input("Name of Pokemon: ")
        poketype = input("Type of Pokemon: ")
        pokemaxHP = int(input("Maximum HP of Pokemon: "))
        pokedam = int(input("Damage the Pokemon will deal: "))
        temp_inp = [pokenum, pokename, poketype, pokemaxHP, pokedam, 'active']
        add(temp_inp)

    if action == 3:
        name = input("Which Pokemon are you looking for?: ")
        att = input("Which attribute do you want to see? (num, type, max_HP, dam, status): ")
        print(load(name, att))

    if action == 4:
        pass

    if action == 5:
        pass

    if action == 6:
        break
