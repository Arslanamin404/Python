import os


def get_file_info(file_path):
    if os.path.exists(file_path):
        # Get file details using os.path functions
        name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        creation_time = os.path.getctime(file_path)
        modification_time = os.path.getmtime(file_path)
        
        print(f"File Name: {name}")
        print(f"File Size: {file_size} kbs")
        print(f"File Creation Time: {str(creation_time)}")
        print(f"File Modification Time: {str(modification_time)}")

    else:
        print(f"The file '{file_path}' does not exist.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="This Command Line Utility will show the details of file!"
    )
    parser.add_argument(
        '-f', "--fname", required=True,
        help="Enter the file path", metavar="File Name"
    )

    args = parser.parse_args()
    get_file_info(args.fname)
