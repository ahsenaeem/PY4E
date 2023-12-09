# Search for lines that contain 'From'
import re
import sys

# Opening the file we wish to search through:

def find_sender(hand: str) -> None:
# hand = "../texts/mbox-short.txt"
    with open(hand, "r") as f:
        for line in f:
            # Removing extra spacing:
            line = line.strip()
            if re.search("From:", line):
                print(line)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        hand = sys.argv[1]
        try:
            find_sender(hand)
        except:
            print("The file path is invalid.")
    else:
        print("Please provide a file path as an argument.")
