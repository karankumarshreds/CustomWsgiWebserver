import socket 

HOST, PORT = '', 8888

# AF_INET refers to the address-family ipv4
# SOCK_STREAM means connection-oriented TCP protocol
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print("Socket successfully created")
  # Setting the socket options 
  # SOL_SOCKET   === 	Permit sending of broadcast datagrams
  # SO_REUSEADDR === Allow local address reuse
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST, PORT))
  s.listen(1)
  print(f"Server HTTP on port {PORT}")
  print(s)
except socket.error as err:
  print("ERROR: Socket creation error %s" %(err))

while True: 
  client_socket, client_addr = s.accept()
  # Setting buffer size for incoming requests == 1024
  request_data = client_socket.recv(1024)
  # Print the requests as plain strings 
  print(request_data.decode("utf-8"))
  client_socket.sendall(b"""\
  HTTP/1.1 200 OK

  Hello, World!
  """)
  # close the client_connection after we are finished dealing with the client 
  client_socket.close() 

