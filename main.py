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

