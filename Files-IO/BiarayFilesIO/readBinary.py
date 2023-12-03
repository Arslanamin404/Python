import pickle


with open("studentListBin", "rb") as f:
    # pickle.load(source) method is used to read  data from binary file
    data = pickle.load(f)
    
print(data)
