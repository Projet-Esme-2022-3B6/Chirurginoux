import socket

class serveurUDP:
    def __init__(self):
        localIP     = "192.168.45.146"
        localPort   = 12345
        self.bufferSize  = 1024

        msgFromServer       = "Hello UDP Client"
        bytesToSend         = str.encode(msgFromServer)
        
        # Create a datagram socket
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind to address and ip
        self.UDPServerSocket.bind((localIP, localPort))
        
        print("UDP server up and listening")

     

    # Listen for incoming datagrams
    def transf_data(self):
        bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientIP)
        print(clientMsg)
        
        message=str(message)
        
        text=message.split("'")
        
        pos=text[1].split("/")
        
        posx=pos[0].split(",")
        posx=posx[0]+"."+posx[1]
        posx=float(posx)
        posx=posx/100
        
        posy=pos[1].split(",")
        posy=posy[0]+"."+posy[1]
        posy=float(posy)
        posy=posy/100
        
        posz=pos[2].split(",")
        posz=posz[0]+"."+posz[1]
        posz=float(posz)
        posz=posz/100
        return posx,posy,posz
        
        # Sending a reply to client
        #UDPServerSocket.sendto(bytesToSend, address)
