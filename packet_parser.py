#!/usr/bin/python3

def parse(filename, L):
    # Open the specified file for reading.
    with open(filename, 'r') as f:
        # Read all lines from the file.
        lines = f.readlines()
        for line in lines:
            # Split each line into a list of values, stripping any leading/trailing whitespace.
            parsed_data = line.strip().split()
            # Append the parsed data list to the provided list 'L'.
            L.append(parsed_data)
