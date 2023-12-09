import re
import sys

def find_sender(handle: str) -> None:
    """In this function, we find """
    with open(handle, "r") as f:
        for line in f:
            line = line.strip()
            if re.search("^From:", line):
                print(line)

if __name__ == "__main__":
    handle = "../texts/mbox-short.txt"
    find_sender(handle)
