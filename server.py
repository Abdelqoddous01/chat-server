import socket
import ClientHandler
import threading

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the localhost on port 12345
server_socket.bind(('localhost', 12345))

# Start listening for incoming client connections with a backlog of 5 connections
server_socket.listen(5)

# Print a message indicating the server is ready to accept connections
print("Server is waiting for connections...")

def accept_connections():
    # Loop continuously to accept new client connections
    while True:
        # Accept an incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Create a ClientHandler object to manage this client's communication
        handle = ClientHandler.ClientHandler(client_socket, client_address)
        
        # Get the username from the client (unique username required)
        username = handle.get_message("Username (unique): ")

        # Start a new thread to handle the client using the 'handle_client' method from the ClientHandler class
        threading.Thread(target=handle.handle_client, args=(f"{username}",)).start()

# Main function to start accepting connections
if __name__ == "__main__":
    accept_connections()
