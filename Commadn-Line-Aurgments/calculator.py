def calculate(num1, num2, operator):
    if operator == "+":
        print(f"{num1}+{num2} = {num1 + num2}")
    elif operator == "-":
        print(f"{num1}-{num2} = {num1 - num2}")
    elif operator == "*":
        print(f"{num1}*{num2} = {num1 * num2}")
    elif operator == "/":
        print(f"{num1}/{num2} = {num1 / num2}")
    else:
        print(f"Invalid Operator!")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="use: This is a command line calculator. User needs to input 2 numbers and a operator."
    )

    parser.add_argument(
        '-o', '--operator', metavar="operator",
        required=True, help="Enter operator (+,-,*,/)",
        choices=["+", "-", "*", "/"]
    )

    parser.add_argument(
        '-n1', '--num1', metavar="number 1",
        required=True, type=int, help="Enter Number 1"
    )
    parser.add_argument(
        '-n2', '--num2', metavar="number 2",
        required=True, type=int, help="Enter Number 2"
    )

    args = parser.parse_args()
    calculate(args.num1, args.num2, args.operator)
