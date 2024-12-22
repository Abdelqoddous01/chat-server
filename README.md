# Multi-Client Chat Server

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
