# reports.py - only functions


def separate_data(file_name):
    with open(file_name, "r") as f:
        read_game_list = f.readlines()
        game_list = [game.replace("\n", "").split("\t") for game in read_game_list]
    return game_list


def count_games(file_name):
    with open(file_name, "r") as f:
        return len(f.readlines())


def decide(file_name, year):
    game_list = separate_data(file_name)
    return bool([game[2] for game in game_list if game[2] == str(year)])


def get_latest(file_name):
    game_list = separate_data(file_name)
    return sorted(game_list, key=lambda x: int(x[2]))[-1][0]


def count_by_genre(file_name, genre):
    game_list = separate_data(file_name)
    return sum([game.count(genre) for game in game_list])


def get_line_number_by_title(file_name, title):
    game_list = separate_data(file_name)
    line_number = [index for index in range(len(game_list)) if title in game_list[index]]
    if line_number:
        return int(line_number[0]) + 1
    raise ValueError("Title not found.")


def alphabetical_order(list_of_strings):
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
    data = {int(game[2]): float(game[1]) for game in game_list if game[3] == "First-person shooter"}
    if data:
        return max(data.keys(), key=lambda x: data[x])
    raise ValueError("There's no FPS games.")
