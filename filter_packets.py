#!/usr/bin/python3

def read_and_filter_packets(filename, node) :
    filter_file = "Node_" + str(node) + "_filtered.txt"
    with open(filename, 'r') as f, open(filter_file, 'w') as file:
        lines = f.readlines()
        for line in lines:
            if 'ping' in line:
                file.write(line)
def filter() :
	read_and_filter_packets("Node1.txt",1)
	read_and_filter_packets("Node2.txt",2)
	read_and_filter_packets("Node3.txt",3)
	read_and_filter_packets("Node4.txt",4)
  
def main():
	filter()
 
if __name__ == "__main__":
    main()