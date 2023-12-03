# Given a text file count how many of each “category” of each image there are. This text file is actually a list of files
# corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for
# the images. Once you take a look at the first line or two of the file, it will be clear which part represents
# the scene category.

def count_image_categories(filename):
    # Initialize a dictionary to store category counts
    category_counts = {}
    with open(filename, "r") as file:
        # Iterate through each line in the file
        for line in file:
            category = line.strip().split("/")[2]
            # Check if the category is already in the dictionary
            if category in category_counts:
                # If it is, increment the count for that category
                category_counts[category] += 1
            else:
                # If it's not, add it to the dictionary with a count of 1
                category_counts[category] = 1
    return category_counts


f_name = "imageDB.txt"
category_count = count_image_categories(f_name)

with open("imageDataAnalysis.txt", "w") as file:
    for category, count in category_count.items():
        file.write(f"The image file has {count} pictures under {category}.\n")
