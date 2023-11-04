#!/usr/bin/python3

from filter_packets import *
from packet_parser import *
from compute_metrics import *


IP_FILE_1_FILTER = "192.168.100.1"
IP_FILE_2_FILTER = "192.168.100.2"
IP_FILE_3_FILTER = "192.168.200.1"
IP_FILE_4_FILTER = "192.168.200.2"

OUTPUT_FILE = "output.txt"

def main():
    L1,L2,L3,L4 = [],[],[],[]
    filter()
    for i in range(1,5):
        parse("Node_" + str(i) + "_filtered.txt", eval("L" + str(i)))

    nodes = [
        (IP_FILE_1_FILTER, L1, "Node_1_filtered.txt"),
        (IP_FILE_2_FILTER, L2, "Node_2_filtered.txt"),
        (IP_FILE_3_FILTER, L3, "Node_3_filtered.txt"),
        (IP_FILE_4_FILTER, L4, "Node_4_filtered.txt")
    ]

    with open(OUTPUT_FILE, "w") as file:
        for ip, list_obj, filtered_file in nodes:
            (
                request_sent, 
                request_recieved, 
                replies_sent, 
                replies_received, 
                request_bytes_sent, 
                request_data_sent, 
                request_bytes_receieved, 
                request_data_received, 
                average_rtt, 
                request_throughput, 
                request_goodput, 
                average_reply_delay, 
                echo_request_hop
            ) = compute(ip, list_obj, filtered_file)

            node_name = filtered_file.replace("_filtered.txt", "").replace("_"," ")

            file.write(f"{node_name}\n")
            file.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
            file.write(f"{request_sent},{request_recieved},{replies_sent},{replies_received}\n")
            file.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
            file.write(f"{request_bytes_sent},{request_data_sent}\n")
            file.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
            file.write(f"{request_bytes_receieved},{request_data_received}\n")
            file.write("\n")
            file.write(f"Average RTT (milliseconds),{average_rtt}\n")
            file.write(f"Echo Request Throughput (kB/sec),{request_throughput}\n")
            file.write(f"Echo Request Goodput (kB/sec),{request_goodput}\n")
            file.write(f"Average Reply Delay (microseconds),{average_reply_delay}\n")
            file.write(f"Average Echo Request Hop Count,{echo_request_hop}\n")
            file.write("\n")

if __name__ == "__main__":
    main()
