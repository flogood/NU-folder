import socket
HOST = '127.0.0.1'
PORT = 8888

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[*] Connecting to server at {HOST}:{PORT}...")
    s.connect((HOST, PORT))
    print('[+] Connection successful!')

    # Prepare and send the message
    message = "Hello, I am the client."
    s.sendall(message.encode('utf-8'))

    # Recieve the server's reply
    data = s.recv(1024)
    response = data.decode('utf-8')
    print(f"[*] Server response: {response}")

except ConnectionRefusedError:
    print("[-] Connection refused. Is the server running?")
except socket.error as e:
    print(f"[-] CLIENT ERROR: An unexpected socket error occurred: {e}")
finally:
    if 's' in locals():
        s.close()
