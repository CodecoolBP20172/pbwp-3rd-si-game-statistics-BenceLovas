# Export function

import printing
import sys


def main(file_name="export.txt"):
    '''Uses printing.py's main function to write into a file'''
    with open(file_name, "w") as f:
        sys.stdout = f
        printing.main()

if __name__ == "__main__":
    main()
