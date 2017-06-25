# printing.py - print reports
import reports


def main():
    print(reports.count_games("game_stat.txt"))
    print(reports.decide("game_stat.txt", 2012))
    print(reports.get_latest("game_stat.txt"))
    print(reports.count_by_genre("game_stat.txt", "RPG"))
    print(reports.get_line_number_by_title("game_stat.txt", "Diablo III"))
    print(reports.sort_abc("game_stat.txt"))
    print(reports.get_genres("game_stat.txt"))
    print(reports.when_was_top_sold_fps("game_stat.txt"))

if __name__ == "__main__":
    main()
