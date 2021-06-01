# WAP to open three files 1.txt,2.txt and 3.txt. if any of these files are not present,
# a message without exiting the program must be printed prompting the same.
import os


def checkFiles(filename):
    try:
        with open(filename) as fil:
            print(fil.read())

    except FileNotFoundError as e:
        print(f"The file {filename} You Searched Does not exist. Create one first.")


one="1.txt"
two="2.txt"
three="3.txt"

checkFiles(one)
checkFiles(two)
checkFiles(three)









