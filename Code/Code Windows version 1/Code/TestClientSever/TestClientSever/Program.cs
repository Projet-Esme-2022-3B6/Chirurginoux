using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

var client = new UdpClient();
IPEndPoint ep = new IPEndPoint(IPAddress.Parse("192.168.23.146"), 12345); // endpoint where server is listening
client.Connect(ep);
string line;
// send data

while (true)
{
    Console.Write("type what you want to send : \n");
    if ((line = Console.ReadLine()) != null)
    {
        Byte[] sendBytes = Encoding.ASCII.GetBytes(line);

        client.Send(sendBytes, sendBytes.Length);

        // then receive data
        var receivedData = client.Receive(ref ep);

        Console.Write("receive data from " + ep.ToString()+"\n");
    }
    
}