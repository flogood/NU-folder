import socket

HOST = '127.0.0.1' # The server's IP address (localhost)
PORT = 8888        # The port number it will listen on

# --- 1. Error Handling: Use a try/except block to catch binding issues ---
try:
    # 2. Create the Socket (TCP/IPv4)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 3. Bind the socket to the address and port
    s.bind((HOST, PORT))
    
    # 4. Listen for incoming connections
    s.listen()
    print(f"[*] Server listening on {HOST}:{PORT}")
    
    # 5. Accept the connection when a client connects
    conn, addr = s.accept()
    print(f"[*] Connection established with {addr}")

    # --- Communication loop ---
    with conn:
        # 6. Receive data from the client
        data = conn.recv(1024) 
        if data:
            message = data.decode('utf-8')
            print(f"[*] Received: {message}")
            
            # 7. Send a response back to the client
            response = "Server received your message: " + message
            conn.sendall(response.encode('utf-8'))
            
except socket.error as e:
    # This catches errors like the port already being in use
    print(f"[-] A socket error occurred: {e}")

finally:
    # Ensure the socket closes cleanly
    if 's' in locals():
        s.close()