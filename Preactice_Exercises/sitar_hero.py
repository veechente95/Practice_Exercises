# https://web.archive.org/web/20220429062001/http://web.cs.ucla.edu/classes/spring22/cs31/
import random

normal_note = "g", "r", "y", "b", "o"
sustained_note = "G", "R", "Y", "B", "O"
no_note = "x"
colors = "G", "g", "R", "r", "Y", "y", "B", "b", "O", "o"
digit = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
end_beat = "/", ""


# color and digit
color_dict = {
    "G": 0,
    "g": 2,
    "R": 3,
    "r": 4,
    "Y": 5,
    "y": 6,
    "B": 7,
    "b": 8,
    "O": 9,
    "o": 1,
}

note_progression = random.choice(colors) + str(random.choice(digit)) + random.choice(end_beat)
print(note_progression)


# def syntactically_correct():
for beat in note_progression:
    if beat[-1] == "/":
        if len("/" > 0):
            return True
