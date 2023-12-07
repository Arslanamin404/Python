import argparse


def sum(num1, num2):
    print(f"Sum of {num1} and {num2} is {num1+num2}!")


parser = argparse.ArgumentParser(
    description="use: To Calculate sum of two numbers."
)
parser.add_argument(
    "-n1", "--num1", metavar="Number 1", type=int,
    help="Enter Num 1", required=True
)
parser.add_argument(
    "-n2", "--num2", metavar="Number 2", type=int,
    help="Enter Num 2", required=True
)
args = parser.parse_args()
sum(args.num1, args.num2)
