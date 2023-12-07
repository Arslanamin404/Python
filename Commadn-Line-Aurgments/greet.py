def hello(name, lang):
    greeting = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hollo",
    }
    msg = f"{greeting[lang]}, {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="This command line utility will be used to greet people"
    )
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help="Name of the Person is required in order to greet him!"
    )

    parser.add_argument(
        '-l', '--lang', metavar='language',
        required=True, choices=["English", "Spanish", "German"],
        help="Language is required!"
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
