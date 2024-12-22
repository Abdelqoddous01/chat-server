# Multi-Client Chat Server ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Chat Icon](https://img.icons8.com/ios/50/chat.png)


A simple multi-client chat server built using Python's `socket` and `threading` modules. This server allows multiple clients to connect concurrently, communicate with each other, and share messages. Each client connects with a unique username, and the server manages clients and their interactions using threads.

## Features

- **Multi-client support**: Handles multiple clients concurrently using threading.
- **Username validation**: Ensures each client has a unique username.
- **Message broadcasting**: Sends messages from any client to all other connected clients.
- **Client disconnect notifications**: Notifies all clients when someone disconnects.
- **Clear screen**: Clears the client's terminal screen when they connect.

## Requirements

- Python 3.x
- Basic understanding of Python and networking concepts
- No external libraries required, just built-in Python modules.

## Installation

### 1. Clone the repository:

   ```bash
   git clone https://github.com/Abdelqoddous01/chat-server.git
   cd chat-server
   python server.py
   ```

## How to Connect

To connect to the chat server, you can use the `telnet` command. 

### 1. Using Telnet:

Open your terminal or command prompt and run the following command:

```bash
telnet <IP_ADDRESS> <PORT>

###Exemple:
telnet 127.0.0.1 12345
```

### 2. Using Client code:
You can generate a simple code for client and run it while the server is running.

```bash

import socket

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server
    message = input("Enter your message: ")

    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())
        message = input("Enter your message: ")

    client_socket.close()

if __name__ == '__main__':
    client_program()

```

## Thank You!

Thank you for checking out this project! 🙌 Your support means a lot. If you found this project useful or interesting, feel free to **star** it and share it with others. 💡

Don't forget to join the conversation, contribute, or stay updated by following this repository. If you have any questions or suggestions, **open an issue** or submit a **pull request**!

🌟 **[Join me on GitHub](https://github.com/Abdelqoddous01)** 🌟

Let's build something great together! 🚀
