# Append a dictionary of student marks to above file
import pickle

with open("studentListBin", "rb") as f:
    data = pickle.load(f)

dict = {}
for name in data:
    dict[name] = float(input(f"Enter marks for {name}: "))


with open("studentListBin", "ab") as f:
    pickle.dump(dict, f)
