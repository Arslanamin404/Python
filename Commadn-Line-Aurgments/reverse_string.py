def reverse(str):
    print(f"Reversed String: {str[::-1]}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="USE: This command line utility will be used to reverse a string!"
    )
    parser.add_argument(
        "-s", "--string", metavar="String",
        required=True, help="Please Enter a string"
    )

    args = parser.parse_args()
    reverse(args.string)
