
# coding: utf-8

# In[ ]:


import time
import socket

pings = 1

#Send ping 10 times 
while pings < 11:  

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server
    message = 'test'

    addr = ("127.0.0.1", 12000)

    #Send ping
    start = time.time()
    clientSocket.sendto(message, addr)

    #If data is received back from server, print 
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print data + " " + pings + " "+ elapsed        

    #If data is not received back from server, print it has timed out  
    except timeout:
        print 'REQUEST TIMED OUT'

    pings = pings - 1


# In[ ]:


# We will need the following module to generate randomized lost packets
    import random
    from socket import *

    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    # Assign IP address and port number to socket
    serverSocket.bind(('', 12000))

    while True:
        # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)

        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)

        # Capitalize the message from the client
        message = message.upper()

        # If rand is less is than 4, we consider the packet lost and do notrespond
        if rand < 4:
            continue

        # Otherwise, the server responds
        serverSocket.sendto(message, address) 

