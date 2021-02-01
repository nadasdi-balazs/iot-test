''' numbers 0-9 without whitespaces:
  |  |  |  || ||  |  | || || |
|_|  ||_  _|  | _||_|  ||_| _|
'''


ENCODING = {
    "  ||_|": 0,
    "  |  |": 1,
    "  ||_ ": 2,
    "  | _|": 3,
    "| |  |": 4,
    "|   _|": 5,
    "|  |_|": 6,
    # "| |  |": 7,
    "| ||_|": 8,
    "| | _|": 9
}


def parse_entries(second_line, third_line):
    entry = []
    for index in range(len(second_line)):
        current_number = second_line[index] + third_line[index]
        if str(current_number).isspace():
            continue
        decoded = ENCODING[current_number]
        print("-- parse_entries, decoded: '" + str(decoded) + "'")
        entry.append(decoded)
    return entry


