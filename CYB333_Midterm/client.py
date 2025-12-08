"""
CYB333 Midterm - Part 1: TCP Client
Student: Crystal Edwards-Flores
Description: A simple TCP client that connects to localhost:8888,
             sends a message to the server, and receives an acknowledgment.
"""

import socket

# Configuration - Must match the server's settings
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888         # The port used by the server

# The message to send
MESSAGE_TO_SEND = "Hello from CYB333 TCP Client! This is my midterm project."

print("="*60)
print("CYB333 MIDTERM - TCP CLIENT")
print("="*60)

# --- Error Handling: Use try/except to catch connection issues ---
try:
    # 1. Create a socket object
    # AF_INET = IPv4, SOCK_STREAM = TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[✓] Socket created successfully")
    
    # 2. Connect to the server
    print(f"[*] Attempting to connect to {HOST}:{PORT}...")
    client_socket.connect((HOST, PORT))
    print(f"[✓] Successfully connected to server at {HOST}:{PORT}")
    
    # 3. Send the message to the server
    print(f"[*] Sending message to server...")
    print(f"    Message: '{MESSAGE_TO_SEND}'")
    
    # Encode the string into bytes before sending
    client_socket.sendall(MESSAGE_TO_SEND.encode('utf-8'))
    print("[✓] Message sent successfully")
    
    # 4. Receive the server's response
    print("[*] Waiting for server response...")
    data = client_socket.recv(1024)
    
    if data:
        # Decode the received bytes into a readable string
        response = data.decode('utf-8')
        print(f"[✓] Received server response:")
        print(f"    '{response}'")
    else:
        print("[-] Received no response from server")
    
    # 5. Close the connection
    client_socket.close()
    print("[✓] Connection closed")
    
    print("="*60)
    print("CLIENT EXECUTION COMPLETED SUCCESSFULLY")
    print("="*60)

except ConnectionRefusedError:
    # Server is not running or not listening on the specified port
    print(f"[✗] Connection refused!")
    print(f"    Ensure the server is running on {HOST}:{PORT}")
    print("    Start the server first, then run this client.")
    
except socket.timeout:
    # Connection timed out
    print("[✗] Connection timed out!")
    print("    The server took too long to respond.")
    
except socket.error as e:
    # Other socket-related errors
    print(f"[✗] A socket error occurred: {e}")
    
except Exception as e:
    # Catch any other unexpected errors
    print(f"[✗] An unexpected error occurred: {e}")
