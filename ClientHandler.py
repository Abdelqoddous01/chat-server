import socket

class ClientHandler:
    # Class-level variables
    nb_client = 0  # Tracks the number of clients connected
    clients = []  # List of (socket, username) tuples to store connected clients

    def __init__(self, clientsocket, address):
        """Initializes the client handler with the client's socket and address."""
        self.client_socket = clientsocket  # The socket for communication with the client
        self.client_address = address  # The address of the client

    def get_message(self, message):
        """Sends a prompt message to the client and waits for a response."""
        self.client_socket.send(f"{message}".encode())  # Send the message to the client

        data = ""
        while True:
            # Receive data from the client (up to 1024 bytes at a time)
            message = self.client_socket.recv(1024).decode()
            if not message:  # If the message is empty, return None
                return None

            data += message  # Append the received message to the data buffer

            # If the message contains a newline, return the message after stripping it of extra spaces
            if '\n' in data:
                return data.strip()

    def send_message(self, message):
        """Sends a message to the client."""
        self.client_socket.send(f"{message}\r\n".encode())  # Send the message to the client with a newline

    def validate_user(self, username):
        """Checks if the username is unique by searching through the list of clients."""
        for _, user in ClientHandler.clients:  # Loop through the list of clients
            if user == username:  # If the username already exists, it's not valid
                return False
        return True  # Return True if the username is unique

    def clear_screen(self):
        """Clears the client's screen by sending escape sequences."""
        self.client_socket.send("\033[2J\033[H".encode())  # ANSI escape code to clear the screen and reset the cursor position

    def handle_client(self, Username):
        """Handles the client connection and manages the interaction."""
        # Keep asking for a unique username if the one provided is already taken
        while not self.validate_user(Username):
            self.send_message("Username already used!")
            Username = self.get_message("Username (unique): ")

        # Add the client to the list of clients (socket, username tuple)
        ClientHandler.clients.append((self.client_socket, Username))
        print(f"Client connected: {Username}")
        self.clear_screen()  # Clear the client's screen upon connection

        try:
            # Send a welcome message to the newly connected user
            self.client_socket.send(f"Welcome {Username} to the chat room!\r\n".encode())
            # Broadcast that the new user has joined the chat (excluding the user itself)
            self.broadcast(f"{Username} has joined the chat!", exclude=Username)

            while True:
                # Get a message from the client
                data = self.get_message("Message >> ")

                if data:
                    if data.lower() not in ['quit', 'exit']:  # If the client sends a message that is not 'quit' or 'exit'
                        # Broadcast the message to all clients (excluding the sender)
                        self.broadcast(f"\r{Username} : {data}", exclude=Username)
                    else:
                        # If the client wants to quit, inform them and notify others
                        self.client_socket.send("You are disconnected.\r\n".encode())
                        print(f"{Username} disconnected.")
                        self.broadcast(f"{Username} has left the chat.", exclude=Username)
                        break  # Break out of the loop and close the connection

        except Exception as e:
            print(f"Error with client {Username}: {e}")  # Log any exceptions during communication
        finally:
            # Clean up: Remove the client from the list and close the socket
            self.remove_client(Username)
            self.client_socket.close()
            print(f"Connection with {Username} closed.")

    def broadcast(self, message, exclude=None):
        """Broadcasts a message to all connected clients, excluding a specific user."""
        for client_socket, username in ClientHandler.clients:
            if username != exclude:  # Don't send the message to the sender (the one excluded)
                try:
                    # Send the message to the client
                    client_socket.send(f"{message}\r\n".encode())
                except Exception as e:
                    print(f"Error sending message to {username}: {e}")  # Log errors when sending a message to a client

    def remove_client(self, username):
        """Removes a client from the list of connected clients."""
        ClientHandler.clients = [
            (socket, user) for socket, user in ClientHandler.clients if user != username
        ]
        # Rebuild the clients list excluding the client with the specified username
