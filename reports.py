# Report functions


def separate_data(file_name):
    '''
    In the data file every line contains properties of a game.
    Properties are separated by a tab character and
    lines are separated by line break characters.

    The order of properties:

    0 = Title (str)
    1 = Total copies sold (million) (float)
    2 = Release date (year) (int)
    3 = Genre (str)
    4 = Publisher (str)
    '''
    with open(file_name, "r") as f:
        read_game_list = f.readlines()
        game_list = [game.strip().split("\t") for game in read_game_list]
        for game in game_list:
            try:
                game[1] = float(game[1])
            except ValueError:
                raise ValueError("Total copies sold value: {}, is not a float.".format(game[1]))
            try:
                game[2] = int(game[2])
            except ValueError:
                raise ValueError("Release date value: {}, is not an intiger.".format(game[2]))
    return game_list


def count_games(file_name):
    with open(file_name, "r") as f:
        return len(f.readlines())


def decide(file_name, year):
    game_list = separate_data(file_name)
    return bool([game[2] for game in game_list if game[2] == year])


def get_latest(file_name):
    game_list = separate_data(file_name)
    return sorted(game_list, key=lambda x: x[2])[-1][0]


def count_by_genre(file_name, genre):
    game_list = separate_data(file_name)
    return sum([game.count(genre) for game in game_list])


def get_line_number_by_title(file_name, title):
    game_list = separate_data(file_name)
    line_number = [index for index in range(len(game_list)) if title in game_list[index]]
    if line_number:
        return line_number[0] + 1
    raise ValueError("Title not found.")


def alphabetical_order(list_of_strings):
    '''Bubble sorting with strings'''
    length = len(list_of_strings) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if list_of_strings[i].lower() > list_of_strings[i + 1].lower():
                sorted = False
                list_of_strings[i], list_of_strings[i + 1] = list_of_strings[i + 1], list_of_strings[i]
    return list_of_strings


def sort_abc(file_name):
    game_list = separate_data(file_name)
    return alphabetical_order([game[0] for game in game_list])


def get_genres(file_name):
    game_list = separate_data(file_name)
    return alphabetical_order(list(set([game[3] for game in game_list])))


def when_was_top_sold_fps(file_name):
    game_list = separate_data(file_name)
    data = {game[2]: game[1] for game in game_list if game[3] == "First-person shooter"}
    if data:
        return max(data.keys(), key=lambda x: data[x])
    raise ValueError("There's no FPS game.")
