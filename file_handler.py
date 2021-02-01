from seven_segment_parser import parse_entries
import os


class FileHandler:
    route = ""

    def __init__(self, given_route):
        root = os.path.dirname(os.path.realpath(__file__))
        self.route = root + given_route

    def extract_from_file(self):
        with open(self.route, "r") as handler:
            entries = self.handle_entry(handler)
            print("-- entries: '" + str(entries) + "'")
            return entries

    def handle_entry(self, handler):
        second_line = []
        third_line = []
        entries = []
        line_count = 0
        line = handler.readline()

        while line:
            print("-- line " + str(line_count) + ": '" + line + "'")
            line_state = line_count % 4
            print("-- line_state: " + str(line_state))
            if line_state == 0:
                line, line_count = self.end_of_iteration(handler, line, line_count)
                continue

            group_three = [line[i:i + 3] for i in range(0, len(line), 3)]
            print("---- group three:", group_three)
            if line_state == 1:
                second_line = group_three
            if line_state == 2:
                third_line = group_three
                entry = parse_entries(second_line, third_line)
                print("-- parsed entry: '" + str(entry) + "'")
                entries.append(entry)
            if line_state == 3:
                line, line_count = self.end_of_iteration(handler, line, line_count)
                continue

            line, line_count = self.end_of_iteration(handler, line, line_count)

        return entries

    def end_of_iteration(self, handler, line, line_count):
        line = handler.readline()
        line_count += 1
        return line, line_count
