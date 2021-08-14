# Web Server

## What is a web server?

It is a server running on the physical/vm server that receives the request from the client using the HTTP protocol and returns the HTTP response.

The client can be a website or any other program that is using HTTP to communicate over the network.

We make use of `sockets`. Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection.

Sockets basics: https://www.geeksforgeeks.org/socket-programming-python

Socket options: https://notes.shichao.io/unp/ch7/#getsockopt-and-setsockopt-functions

Before the client sends the `http` request, it needs to establish the `TCP` connection with the **web server**.
Once the connection is established, the client sends the HTTP request over the TCP connection and waits for the HTTP response from the webserver.

<p align="center">
  <img width="700" src="https://github.com/karankumarshreds/CustomWebserver/blob/master/img/img1.PNG"/>
</p>

The TCP connection is initiated from the client and to establish that, both client and server use `sockets`.

## Integrate any web framework with your web server

Before we move ahead, we need to understand what **WSGI** is.

### WSGI (Web Server Gateway Interface)

The Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. (coming straight at'ya via wiki)

All the Web Servers must implement the WSGI integration which allows us to use and integrate any python web framework onto the Web Server. Think of it as a protocol.

<p align="center">
  <img width="700" src="https://github.com/karankumarshreds/CustomWebserver/blob/master/img/img2.PNG"/>
</p>

**NOTE:** WSGI support needs to be handled from both the webserver and the weframework.

<p align="center">
  <img width="700" src="https://github.com/karankumarshreds/CustomWebserver/blob/master/img/img3.PNG"/>
</p>

Sources:

- https://docs.python.org/3/library/wsgiref.html
