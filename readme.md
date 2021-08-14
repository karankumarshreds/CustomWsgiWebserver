# Web Server

## What is a web server?

It is a server running on the physical/vm server that receives the request from the client using the HTTP protocol and returns the HTTP response.

The client can be a website or any other program that is using HTTP to communicate over the network.

We make use of `sockets`. Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection.

Sockets basics: https://www.geeksforgeeks.org/socket-programming-python

Socket options: https://notes.shichao.io/unp/ch7/#getsockopt-and-setsockopt-functions

Before the client sends the `http` request, it needs to establish the `TCP` connection with the **web server**.
Once the connection is established, the client sends the HTTP request over the TCP connection and waits for the HTTP response from the webserver.

SOCKETS FROM THE CLIENT SIDE??????
