## introduction

This Python script creates a simple web shell using the http.server module. It sets up an HTTP server that listens on port 8000 by default.
When a client sends a GET request to the server, it responds with an HTML page containing a form where users can enter a shell command.
When a client sends a POST request with a command, the server executes the command using the subprocess module and returns the output to the client.

# Credit
Thanks to chatGPT for coming clutch in my darkest hour of embedded linux backdooring.

# Disclaimer
Please don't use this in a live production enviornment this was used in a controlled practice enviornment against blue team.
