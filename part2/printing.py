# Print function
import reports


def main():
    print(reports.get_most_played("game_stat.txt"),
          reports.sum_sold("game_stat.txt"),
          reports.get_selling_avg("game_stat.txt"),
          reports.count_longest_title("game_stat.txt"),
          reports.get_date_avg("game_stat.txt"),
          reports.get_game("game_stat.txt", "Doom 3"),
          reports.count_grouped_by_genre("game_stat.txt"),
          reports.get_date_ordered("game_stat.txt"), sep="\n")

if __name__ == "__main__":
    main()
