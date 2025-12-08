"""
CYB333 Midterm - Part 2: Port Scanner
Student: Crystal Edwards-Flores
Description: A TCP port scanner that scans localhost (127.0.0.1) and 
             scanme.nmap.org for open ports. Includes error handling
             and clear output for documentation.
             
ETHICAL NOTICE: Only scan systems you have permission to scan.
scanme.nmap.org is provided by Nmap for testing purposes.
"""

import socket
from datetime import datetime

# Port scanner function
def scan_port(target, port, timeout=1):
    """
    Scan a single port on the target host.
    
    Args:
        target (str): IP address or hostname to scan
        port (int): Port number to check
        timeout (float): Connection timeout in seconds
        
    Returns:
        bool: True if port is open, False if closed
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Attempt to connect to the port
        result = sock.connect_ex((target, port))
        sock.close()
        
        # Return True if connection successful (port open)
        return result == 0
        
    except socket.gaierror:
        # Hostname could not be resolved
        return False
    except socket.error:
        # Could not connect
        return False

def scan_target(target, ports, description):
    """
    Scan multiple ports on a target host and display results.
    
    Args:
        target (str): IP address or hostname to scan
        ports (list): List of port numbers to scan
        description (str): Description of the target for display
    """
    print("="*70)
    print(f"SCANNING: {description}")
    print(f"Target: {target}")
    print(f"Ports to scan: {len(ports)} ports")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    open_ports = []
    closed_count = 0
    
    # Scan each port
    for port in ports:
        # Show progress every 100 ports
        if port % 100 == 0:
            print(f"[*] Progress: Scanning port {port}...")
        
        if scan_port(target, port):
            # Port is open
            try:
                # Try to get service name
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            
            print(f"[✓] Port {port:5d} - OPEN    (Service: {service})")
            open_ports.append(port)
        else:
            closed_count += 1
    
    # Summary
    print("="*70)
    print(f"SCAN COMPLETE: {description}")
    print(f"Total ports scanned: {len(ports)}")
    print(f"Open ports found: {len(open_ports)}")
    print(f"Closed ports: {closed_count}")
    
    if open_ports:
        print(f"Open port list: {open_ports}")
    else:
        print("No open ports found.")
    
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print()

# Main execution
if __name__ == "__main__":
    print("\n" + "="*70)
    print("CYB333 MIDTERM - PORT SCANNER")
    print("="*70)
    print("ETHICAL NOTICE:")
    print("This tool is for educational purposes only.")
    print("Only scan systems you have explicit permission to test.")
    print("scanme.nmap.org is provided by Nmap for testing purposes.")
    print("="*70)
    print()
    
    # Task 1: Scan localhost (127.0.0.1) - Ports 1-1024
    localhost_target = "127.0.0.1"
    localhost_ports = range(1, 1025)  # Ports 1 to 1024
    
    scan_target(
        target=localhost_target,
        ports=localhost_ports,
        description="LOCALHOST (127.0.0.1) - Well-known ports (1-1024)"
    )
    
    # Task 2: Scan scanme.nmap.org - Common ports only
    # Using common ports to be respectful and keep scan time reasonable
    remote_target = "scanme.nmap.org"
    common_ports = [
        20,    # FTP Data
        21,    # FTP Control
        22,    # SSH
        23,    # Telnet
        25,    # SMTP
        53,    # DNS
        80,    # HTTP
        110,   # POP3
        143,   # IMAP
        443,   # HTTPS
        445,   # SMB
        3306,  # MySQL
        3389,  # RDP
        5432,  # PostgreSQL
        8080,  # HTTP Alternate
        8443,  # HTTPS Alternate
    ]
    
    scan_target(
        target=remote_target,
        ports=common_ports,
        description="REMOTE HOST (scanme.nmap.org) - Common ports"
    )
    
    print("="*70)
    print("ALL SCANS COMPLETED")
    print("="*70)
    print("\nREMINDER: Document these results with screenshots for your submission.")
    print()
