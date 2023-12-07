def convert(celsius):
    print(f"{celsius} C = {(celsius * 9/5)+32} F")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="USE : This Command Line Utility will be used to convert temperature from Celsius to Fahrenheit"
    )
    parser.add_argument(
        '-c', '--celsius', metavar="Celsius", required=True, type=float,
        help="Enter Temperature in Celsius"
    )

    args = parser.parse_args()
    convert(args.celsius)
