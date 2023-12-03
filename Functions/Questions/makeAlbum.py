"""Album: Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name , an album title,and  an optional parameter to make_album()
that allows you to store the number of tracks on an album. If the calling line includes a value for the
number of tracks, add that value to the album’s dictionary. Make at least one new function call that
includes the number of tracks on an album."""


def make_album(name, album_title, num_of_tracks=None):
    music_album = {
        "Name": name,
        "Album Name": album_title
    }
    if num_of_tracks is not None:
        music_album["Tracks"] = num_of_tracks
    return music_album


if __name__ == '__main__':
    while True:
        print("\nEnter the album information: ")
        artist = input("Artist [or q to quit]: ").title()
        if artist.lower() == 'q':
            print("Exiting. . .")
            break
        title = input("Album Title: ").title()
        tracks = input("Number of Tracks (optional): ")

        if tracks.isdigit():
            album = make_album(artist, title, int(tracks))
        else:
            album = make_album(artist, title)

        print("\nAlbum created successfully!")
        print("-----------------------------")
        for key, val in album.items():
            print(f"{key}:{val}")
        print("-----------------------------")
