#!/usr/bin/python3

from filter_packets import *
from packet_parser import *
from compute_metrics import *

def main():
    L1,L2,L3,L4 = [],[],[],[]
    filter()
    for i in range(1,5):
        parse("Node_" + str(i) + "_filtered.txt", eval("L" + str(i)))
    compute()
    
if __name__ == "__main__":
    main()
