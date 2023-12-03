# use list datatype to store the questions and their correl answers
# display the final amount the person is taking home
def startQuiz(questions, options, correctAnswer, userName):
    money = 0
    for i in range(len(questions)):
        current_question = questions[i]
        print("----------------------------------------------")
        print(current_question)
        print("----------------------------------------------")
        #
        # # print 2d list of options
        # for j in range(len(options[i])):
        #     current_options = options[i][j]
        #     print(" - " + current_options)
        print(f"\t- {options[i][0]}\t\t\t- {options[i][1]}")
        print(f"\t- {options[i][2]}\t\t\t- {options[i][3]}")
        print("----------------------------------------------")

        current_answer = correctAnswer[i].lower()
        user_input = input("Your Answer: ").lower().strip()

        # check for correct answer
        if user_input == current_answer:
            money += 1500
            print("\nCorrect! You earned", money, "Rupees")
        else:
            print("\nWrong!")
            money = 0
            break
        print("----------------------------------------------\n")

    print(
        f"\n{userName} Thanks for playing! You earned a total of", money, "Rupees"
    )
    print("\n-----------------------------------------------------------------\n")


questions = [
    "What is the capital of Japan?",
    "How many continents are there on Earth?",
    "Who wrote the play 'Romeo and Juliet?'",
    "What is the chemical symbol for gold?",
    "Which planet is known as 'Red Planet'?",
    "What is largest mammal on earth?",
    "Which gas do plants absorb from the atmosphere?",
    "What is the tallest mountain in the world?",
    "Who painted the Mona Lisa?",
    "Who is the author of the Harry Potter book series?",
]
options = [
    ["Tokyo", "Beijing", "Korea", "Seoul"],
    ["5", "12", "7", "9"],
    ["Ruskin Bond", "Charles Dickens", "Jane Austin", "William Shakespeare"],
    ["Au", "Ag", "Fe", "Gu"],
    ["Venus", "Jupiter", "Mars", "Pluto"],
    ["African Elephant", "Blue Whale", "Giraffe", "Hippo"],
    ["Oxygen", "Florine", "Nitrogen", "Carbon Dioxide"],
    ["Mount Everest", "Mount Fuji", "Mount Kilimanjaro", "Mount Lidwas"],
    ["Pablo Picasso", "Vincent Van Gogh", "Leonardo da Vinci", "John Michel"],
    ["JRR Tolkien", "JK Rowling", "George Orwell", "Stephen King"],
]
correctAnswer = [
    "Tokyo",
    "7",
    "William Shakespeare",
    "Au",
    "Mars",
    "Blue Whale",
    "Carbon Dioxide",
    "Mount Everest",
    "Leonardo da Vinci",
    "JK Rowling",
]

print(
    "Welcome to this Demo KCB Game. In this game you will be asked some questions and you have to input the correct answer.\n")
userName = input("Please enter your name: ")
print("\n**Rules and Regulations:**")
print("1. Entry FREE")
print("2. Correct answers earn you money, but a wrong answer means you lose everything earned")
print("3. Input your answer with correct spellings so that your answer gets counted as correct")
print("\n\tExperience the Thrill - Win Big or Go Home!\n")
print("Lets begin! " + userName + "\n")

startQuiz(questions, options, correctAnswer, userName)
