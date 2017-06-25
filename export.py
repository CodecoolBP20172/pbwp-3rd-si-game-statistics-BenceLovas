# export.py - exports reports (to export.txt by default)
import printing
import sys


def main(file_name="export.txt"):
    with open(file_name, "w") as f:
        sys.stdout = f
        printing.main()

if __name__ == "__main__":
    main()
