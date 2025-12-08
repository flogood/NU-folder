"""
CYB333 Midterm - Part 1: TCP Server
Student: Crsyatl Edwards-Flores
Description: A simple TCP server that listens on localhost:8888,
             accepts one client connection, receives a message,
             and sends back an acknowledgment.
"""

import socket

# Configuration
HOST = '127.0.0.1'  # The server's IP address (localhost)
PORT = 8888         # The port number it will listen on

print("="*60)
print("CYB333 MIDTERM - TCP SERVER")
print("="*60)

# --- 1. Error Handling: Use a try/except block to catch binding issues ---
try:
    # 2. Create the Socket (TCP/IPv4)
    # AF_INET = IPv4, SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[✓] Socket created successfully")
    
    # 3. Bind the socket to the address and port
    # This reserves the port for our server
    s.bind((HOST, PORT))
    print(f"[✓] Socket bound to {HOST}:{PORT}")
    
    # 4. Listen for incoming connections
    # The server is now ready to accept connections
    s.listen()
    print(f"[*] Server listening on {HOST}:{PORT}")
    print("[*] Waiting for client connection...")
    
    # 5. Accept the connection when a client connects
    # This blocks (waits) until a client connects
    conn, addr = s.accept()
    print(f"[✓] Connection established with {addr}")

    # --- Communication with the client ---
    with conn:
        # 6. Receive data from the client
        # Buffer size is 1024 bytes
        data = conn.recv(1024) 
        
        if data:
            # Decode bytes to string
            message = data.decode('utf-8')
            print(f"[✓] Received from client: '{message}'")
            
            # 7. Send a response back to the client
            response = f"Server received your message: '{message}'"
            conn.sendall(response.encode('utf-8'))
            print(f"[✓] Sent acknowledgment to client")
            
        else:
            print("[-] No data received from client")
    
    print("[✓] Connection closed")
    print("="*60)
    print("SERVER EXECUTION COMPLETED SUCCESSFULLY")
    print("="*60)
            
except socket.error as e:
    # This catches errors like the port already being in use
    print(f"[✗] A socket error occurred: {e}")
    print("    Common causes:")
    print("    - Port already in use (try a different port)")
    print("    - Permission denied (try a higher port number)")

except Exception as e:
    # Catch any other unexpected errors
    print(f"[✗] An unexpected error occurred: {e}")

finally:
    # Ensure the socket closes cleanly
    if 's' in locals():
        s.close()
        print("[*] Socket closed")
