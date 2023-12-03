def countWords(f_name):
    try:
        with open(f_name, 'r') as file:
            content = file.read()
            chars = len(content)
            # .split() without args it splits the string based on any whitespace chars(spaces,tabs,newline)
            words = len(content.split())
            newline = content.count("\n")
            print(f"Total number of characters in this file are {chars}")
            print(f"Total number of words in this file are {words}")
            print(f"Total number of lines in this file are {newline}")
    except FileNotFoundError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Something unexpected occurred: {err}")


if __name__ == "__main__":
    fileName = '../myFile.txt'
    countWords(fileName)
