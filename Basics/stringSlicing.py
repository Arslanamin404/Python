# Slicing creates a s substring by extracting characters from another string
# Two ways to perform slicing: indexing[] and slice()
# [start:stop:step]

print("\n-------------------------------------------------------")
username = "Future Gen"
firstName = username[0:6]
lastName = username[7:]
print(firstName)
print(lastName)
name = username[::2]  # this will skips every 2nd character
print(name)
reversedName = username[::-1]
print(reversedName)

print("-------------------------------------------------------")

# Slice()
website1 = "https://arsalanrather.org"
website2 = "https://google.com"
website3 = "https://yahoo.com"
website4 = "https://instagram.com"
website5 = "https://facebook.com"

# we have created it(slice) dynamically applicable for every website of .com domain
slice = slice(8, -4)

print(f"1. {website1[slice]}")
print(f"2. {website2[slice]}")
print(f"3. {website3[slice]}")
print(f"4. {website4[slice]}")
print(f"5. {website5[slice]}")
print("-------------------------------------------------------\n")
