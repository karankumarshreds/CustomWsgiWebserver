import io 
import socket 
import sys 

class WSGIServer():
  address_type        = socket.AF_INET
  socket_type         = socket.SOCK_STREAM
  request_queue_size  = 1

  s = None

  def __init__(self, server_address):
    # Create a socket instance 
    self.s = socket.socket(self.address_type, self.socket_type)
    print("Socket successfully created")
    # SOL_SOCKET   === 	Permit sending of broadcast datagrams
    # SO_REUSEADDR ===  Allow local address reuse
    self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.s.bind(server_address)
    self.s.listen(self.request_queue_size)
    # Get server host name and port
    host, port = self.s.getsockname()[:2]
    print("HOST: ", host)
    print("PORT: ", port)
    # returns the full domain name based on the host name 
    self.server_name = socket.getfqdn(host)
    self.server_port = port
    # Return headers set by Web framework/Web application
    self.headers_set = []

  # Sets the callable application as the WSGI application that will receive requests
  # Required method by the WSI docs 
  def set_app(self, application):
    self.application = application
  
  # Required method by the WSI docs 
  def serve_forever(self):
    while True:
      # New client connection
      self.client_connection, client_address = self.s.accept()
      self.request_data = self.client_connection.recv(1024)
      self.request_data = string_data = self.request_data.decode("utf-8")
      request_line = string_data.splitlines()[0]
      request_line = request_line.rstrip('\r\n')
      # Break down the request line into components
      (
        self.request_method,  
        self.path,            
        self.request_version  
      ) = request_line.split()
      # Construct environment dictionary using request data
      env = self.get_environ()
      result = self.application(env, self.start_response)
      self.finish_response(result)

  # Required method by the WSI docs 
  def get_environ(self):
    env = {}
    # Required WSGI variables
    env['wsgi.version']      = (1, 0)
    env['wsgi.url_scheme']   = 'http'
    env['wsgi.input']        = io.StringIO(self.request_data)
    env['wsgi.errors']       = sys.stderr
    env['wsgi.multithread']  = False
    env['wsgi.multiprocess'] = False
    env['wsgi.run_once']     = False
    # Required CGI variables
    env['REQUEST_METHOD']    = self.request_method    # GET
    env['PATH_INFO']         = self.path              # /hello
    env['SERVER_NAME']       = self.server_name       # localhost
    env['SERVER_PORT']       = str(self.server_port)  # 8888
    return env

  # Required method by the WSI docs 
  # The framework/application generates an HTTP status and HTTP response 
  # headers and passes them to the ‘start_response’ method for the server 
  # to store them.
  def start_response(self, status, response_headers, exc_info=None):
    # Add necessary server headers
    server_headers = [
        ('Date', 'Mon, 00 Jul 2021 5:54:48 GMT'),
        ('Server', 'WSGIServer 0.2'),
    ]
    self.headers_set = [status, response_headers + server_headers]

  # [result] is must contain headers and status returned from the 
  # start_response method
  def finish_response(self, result):
    try: 
        status, response_headers = self.headers_set
        response = f'HTTP/1.1 {status}\r\n'
        for header in response_headers:
          # adding first and second alphabet of each 
          # header in a new line 
          response += '{0}: {1}\r\n'.format(*header)
        response += '\r\n'
        for data in result:
          response += data.decode("utf-8") 
        # Print formatted response data 
        print(''.join(
            f'> {line}\n' for line in response.splitlines()
        )) 
        # Encoding the formatted response string to byte 
        # format to send back to the client 
        response_bytes = response.encode()
        self.client_connection.sendall(response_bytes)
    finally:
        self.client_connection.close()


SERVER_ADDRESS = (HOST, PORT) = '', 8888

def make_server(server_address, application):
    server = WSGIServer(server_address) # will be done while initializing 
    server.set_app(application)
    return server # returning the instance of the WSGI Server 
     

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as <your_module_name>:<wsgi_app_name>')
    # [0] would be the name of this current file 
    # [1] would be the name of the <your_module_name>:<wsgi_app_name>
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print(f'WSGIServer: Serving HTTP on port {PORT} ...\n')
    httpd.serve_forever()
