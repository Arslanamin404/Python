import pytube
import os

def main():
    # Print a banner for the YouTube Video Downloader
    print("##############################################################################################")
    print("\t\t\t\t\tYouTube Video Downloader")
    print("##############################################################################################")


    try:
        # Get user input for the YouTube video URL
        link = input("Enter YouTube Video URL: ")
        # Create a YouTube object using the provided video URL
        yt = pytube.YouTube(link)

        # Get the best available video stream
        video_stream = yt.streams.first()

        if video_stream:
            # Create a directory for downloads if it doesn't exist
            if not os.path.exists("downloads"):
                os.makedirs("downloads")

            # Download the video to the 'downloads' folder
            video_stream.download(output_path="downloads")

            # Print a message after successful download
            print('\n------------------------------------------------------------------------------')
            print(f"Downloaded {yt.title} to the 'downloads' folder.")
            print('------------------------------------------------------------------------------\n')
        else:
            # Inform the user if no suitable video stream was found
            print("No suitable video stream found.")

    except pytube.exceptions.VideoUnavailable:
        # Handle the case where the video is not available or restricted
        print("The video is not available or restricted.")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {str(e)}")
    
    # Provide a clear exit message and wait for user input before exiting
    print("###################################################################################")
    input("\t\t\tPress Enter Key to exit.")
    print("###################################################################################")

if __name__ == "__main__":
    main()
