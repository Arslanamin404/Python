from functools import reduce
word_list = ["The", "quick", "brown", "fox",
             "jumps", "over", "the", "lazy", "dog."]

concatenated_String = reduce(lambda x, y: f"{x} {y}", word_list)
print(concatenated_String)
