def readFile(file_name):
    try:
        with open(file_name, 'r') as file:
            i = 1
            while True:
                line = file.readline()
                if not line:
                    print("\nEOF! Reached")
                    break
                name = line.split(',')[0]
                mat = line.split(',')[1]
                sst = line.split(',')[2]
                sci = line.split(',')[3]
                urd = line.split(',')[4]
                eng = line.split(',')[4]

                print(f"Marks of {name} in Math is {float(mat)}")
                print(f"Marks of {name} in SSt is {float(sst)}")
                print(f"Marks of {name} in Science is {float(sci)}")
                print(f"Marks of {name} in Urdu is {float(urd)}")
                print(f"Marks of {name} in English is {float(eng)}", end="")
                print("\n")
                i += 1
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    fileName = 'studentMarks'
    readFile(fileName)
