import random

dice_faces = [
    """
      _______
     |       |
     |   ●   |
     |       |
      ‾‾‾‾‾‾‾
    """,
    """
      _______
     | ●     |
     |       |
     |     ● |
      ‾‾‾‾‾‾‾
    """,
    """
      _______
     | ●     |
     |   ●   |
     |     ● |
      ‾‾‾‾‾‾‾
    """,
    """
      _______
     | ●   ● |
     |       |
     | ●   ● |
      ‾‾‾‾‾‾‾
    """,
    """
      _______
     | ●   ● |
     |   ●   |
     | ●   ● |
      ‾‾‾‾‾‾‾
    """,
    """
      _______
     | ●   ● |
     | ●   ● |
     | ●   ● |
      ‾‾‾‾‾‾‾
    """
]

print(dice_faces[random.randint(0, 5)])
