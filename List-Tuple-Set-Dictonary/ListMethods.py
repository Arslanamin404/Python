list = [12, 54, 43, 66, 43, 67, 43]
list.append(2023)
del list[1] #deletes element at index 1
# list.sort() #Ascending order
# list.sort(reverse=True)  # Descending order
# list.reverse()
print("Index of 43 is:", list.index(43))
print("Count of 43 is:", list.count(43))
newList = list.copy()
list.insert(2, 69)  # (index,value)
m = [2021, 2022, 2023]
list.extend(m)  #m list will be appended to 'list'
list.pop(0) #removes an element at (index)  
print(list)
