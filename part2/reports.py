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


def get_most_played(file_name):
    game_list = separate_data(file_name)
    data = [[game[0], game[1]] for game in game_list]
    return sorted(data, key=lambda x: x[1], reverse=True)[0][0]


def sum_sold(file_name):
    game_list = separate_data(file_name)
    return sum([game[1] for game in game_list])


def get_selling_avg(file_name):
    game_list = separate_data(file_name)
    return sum([game[1] for game in game_list]) / len(game_list)


def count_longest_title(file_name):
    game_list = separate_data(file_name)
    return max([len(game[0]) for game in game_list])


def get_date_avg(file_name):
    game_list = separate_data(file_name)
    return -(-sum([game[2] for game in game_list]) // len(game_list))


def get_game(file_name, title):
    game_list = separate_data(file_name)
    return [game for game in game_list if game[0] == title][0]


def count_grouped_by_genre(file_name):
    game_list = separate_data(file_name)
    genres = set([game[3] for game in game_list])
    return {genre: sum([game.count(genre) for game in game_list]) for genre in genres}


def get_date_ordered(file_name):
    game_list = separate_data(file_name)
    return [game[0] for game in sorted(game_list, key=lambda x: (-x[2], x[0].lower()))]
