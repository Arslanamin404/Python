"""use the replace() method to replace any word in a string with a different word.
Here’s a quick example showing how to replace
--> message.replace('dog', 'cat')

Read in each line from the file you just created and replace any word with the another word of your choice.
Print each modified line to the screen."""

with open("sample", "r") as file:
    content = file.read()
    content = content.replace("garden", "banana")
    print(content)
