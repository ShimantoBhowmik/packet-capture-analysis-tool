#!/usr/bin/python3



def compute(ip,L,filename) :
    REPLY_SENT_COUNT=0
    REPLY_RECIEVED_COUNT=0
    REQ_SENT_COUNT=0
    REQ_RECIEVED_COUNT=0
    BYTES_SENT=0
    BYTES_RECIEVED=0
    DATA_SENT=0
    DATA_RECIEVED=0
    COUNT_1=0
    TOTAL_TIME_1=0
    COUNT_2=0
    TOTAL_TIME_2=0
    AVG_RTT=0
    AVG_REPLY_DELAY=0
    REQ_THROUGHPUT=0
    REQ_GOODPUT=0
    ORG_HOP=129
    HOP_COUNT=0
    for item in L :
        if item[8] == "reply":
            if item[2] == ip:
				#Echo Replies sent
                REPLY_SENT_COUNT += 1 
            elif item[3] == ip:
				#Echo Replies received
                REPLY_RECIEVED_COUNT += 1 

        if item[8] == "request":
            if item[2] == ip:
                REQ_SENT_COUNT += 1 
                BYTES_SENT += int(item[5]) 
                #42 -- the difference between ICMP packet size and ICMP payload size
                DATA_SENT += int(item[5]) - 42 
            elif item[3] == ip:
                REQ_RECIEVED_COUNT += 1 
                BYTES_RECIEVED += int(item[5]) 
                #42 -- the difference between ICMP packet size and ICMP payload size
                DATA_RECIEVED += int(item[5]) - 42 
                
                
    #Average round trip time Echo Request Throughput and Echo Request Goodput calc
    for i in range(0,len(L)):
        if L[i][8] == "request" :
            if L[i][2] == ip :
                COUNT_1 += 1
                TOTAL_TIME_1 += (float(L[i+1][1]))-(float(L[i][1]))

	# Average Reply Delay calculation
    for i in range(0,len(L)):
        if L[i][8] == "request" :
            if L[i][3] == ip :
                COUNT_2 += 1
                TOTAL_TIME_2 += (float(L[i+1][1]))-(float(L[i][1]))			
	
	#Hop Count calculation
    for i in range(0,len(L)):
        if L[i][8] == "reply" :
            if L[i][3] == ip :
                HOP_COUNT += (ORG_HOP - int(''.join(num for num in L[i][11] if num.isdigit())))
                
    AVG_RTT = (TOTAL_TIME_1 / COUNT_1)*1000 
    REQ_THROUGHPUT = (BYTES_SENT / TOTAL_TIME_1)/1000 #unit - seconds
    REQ_GOODPUT = (DATA_SENT / TOTAL_TIME_1)/1000 
    AVG_REPLY_DELAY = (TOTAL_TIME_2/COUNT_2) * 1000000 #unit - microseconds
    AVG_HOP = float(HOP_COUNT)/float(REQ_SENT_COUNT)
    
    return(REQ_SENT_COUNT,REQ_RECIEVED_COUNT,REPLY_SENT_COUNT,REPLY_RECIEVED_COUNT,round(BYTES_SENT,2),round(DATA_SENT,2),\
        round(BYTES_RECIEVED,2),round(DATA_RECIEVED,2),round(AVG_RTT,2),round(REQ_THROUGHPUT,1),round(REQ_GOODPUT,1),round(AVG_REPLY_DELAY,2,),round(AVG_HOP,2))



