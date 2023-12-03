class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, other_vector):
        return Vector(self.i + other_vector.i, self.j + other_vector.j, self.k + other_vector.k)

    def __sub__(self, other_vector):
        return Vector(self.i - other_vector.i, self.j - other_vector.j, self.k - other_vector.k)

    def dot_product(self, other_vector):
        return (self.i * other_vector.i) + (self.j * other_vector.j) + (self.k * other_vector.k)


def perform_vector_operation(vector_A, vector_B, operation):
    if operation == "add":
        result = vector_A + vector_B
        opp = "(U+V)"
    elif operation == "sub":
        result = vector_A - vector_B
        opp = "(U-V)"
    elif operation == "dot":
        result = vector_A.dot_product(vector_B)
        opp = "(U.V)"

    print("\n-----------------------------------------------")
    print(f"Vector A = {vector_A}")
    print(f"Vector B = {vector_B}")
    print("-----------------------------------------------")
    print(f"Resultant{opp} = {result}")
    print("-----------------------------------------------")


def main():
    try:
        print("Please Enter Components of Vector A ")
        vector_A_i = int(input("Enter i component: "))
        vector_A_j = int(input("Enter j component: "))
        vector_A_k = int(input("Enter k component: "))

        print("\nPlease Enter Components of Vector B ")
        vector_B_i = int(input("Enter i component: "))
        vector_B_j = int(input("Enter j component: "))
        vector_B_k = int(input("Enter k component: "))

        vector_A = Vector(vector_A_i, vector_A_j, vector_A_k)
        vector_B = Vector(vector_B_i, vector_B_j, vector_B_k)

        print("\nPlease Enter Select an Action --->\n1. Vector Addition\n2. Vector Subtraction\n3. Dot Product\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            perform_vector_operation(vector_A, vector_B, "add")
        elif choice == 2:
            perform_vector_operation(vector_A, vector_B, "sub")
        elif choice == 3:
            perform_vector_operation(vector_A, vector_B, "dot")
        else:
            print("Invalid choice. Please choose 1 for addition or 2 for subtraction.")
    except ValueError:
        print("Error! Please enter a valid integer.")
    except Exception as err:
        print(f"Error! Something unexpected occurred: {err}")


if __name__ == "__main__":
    main()