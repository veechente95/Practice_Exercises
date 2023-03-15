# https://web.archive.org/web/20220429062001/http://web.cs.ucla.edu/classes/spring22/cs31/
import random

# normal_note = "g", "r", "y", "b", "o"
# sustained_note = "G", "R", "Y", "B", "O"
# no_note = "x"
colors = "G", "g", "R", "r", "Y", "y", "B", "b", "O", "o"
digit = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
beat = {
    "slash": "/",
    "color_slash": random.choice(colors) + "/",
    "color_digit_slash": random.choice(colors) + random.choice(digit) + "/",
    "color_2digits_slash": random.choice(colors) + random.choice(digit) + random.choice(digit) + "/",
}

print(list(beat.values()))


def has_proper_syntax(tune):   # Checks if syntactically correct.
    # Ends with "/"
    if tune[-1] == "/":
        return True
    else:
        return False




# color and digit
color_dict = {
    "G": "00",
    "g": "01",
    "R": "02",
    "r": "03",
    "Y": "04",
    "y": "05",
    "B": "06",
    "b": "07",
    "O": "08",
    "o": "09",
}

# def convert_tune(tune, instructions, bad_beat):
