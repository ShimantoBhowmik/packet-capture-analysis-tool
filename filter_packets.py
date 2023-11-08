#!/usr/bin/python3
    
# Define a function to read packets from a file and filter out lines containing 'ping'.
# The filtered lines are written to a new file based on the given node number.
def read_and_filter_packets(filename, node):
    # Construct the output file name based on the node number.
    filter_file = "Node_" + str(node) + "_filtered.txt"
    with open(filename, 'r') as f, open(filter_file, 'w') as file:
        lines = f.readlines()
        for line in lines:
            # Check if the line contains 'ping'.
            if 'ping' in line:
                # Write the line to the filtered file.
                file.write(line)

# Define a function to filter packets for multiple nodes.
def filter():
    # Call the read_and_filter_packets function for each node's input file.
    read_and_filter_packets("Node1.txt", 1)
    read_and_filter_packets("Node2.txt", 2)
    read_and_filter_packets("Node3.txt", 3)
    read_and_filter_packets("Node4.txt", 4)

# Define the main function that triggers the packet filtering process.
def main():
    filter()

if __name__ == "__main__":
    # Call the main function to start the packet filtering process.
    main()