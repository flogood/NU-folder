# CYB333 Midterm Project - Python Network Programming

**Student:** [Your Name]  
**Course:** CYB333 - Network Security  
**Date:** December 7, 2025  
**Repository:** https://github.com/flogood/NU-folder

---

## Project Overview

This project demonstrates fundamental Python network programming concepts including TCP socket communication and port scanning. It consists of three main components developed as part of the CYB333 midterm examination.

### Components

1. **TCP Server** (`server.py`) - A simple TCP server that listens for client connections
2. **TCP Client** (`client.py`) - A TCP client that connects to the server and exchanges messages
3. **Port Scanner** (`port_scanner.py`) - A network reconnaissance tool for identifying open ports

---

## Part 1: Socket Connection (TCP Client/Server)

### Description

The TCP client and server programs demonstrate basic socket programming concepts:

- **Server**: Binds to localhost (127.0.0.1) on port 8888, listens for incoming connections, receives messages, and sends acknowledgments
- **Client**: Connects to the server, sends a message, and receives the server's response

### Features

- ✅ Error handling for connection issues
- ✅ Clear output messages for debugging and verification
- ✅ Proper socket cleanup using context managers
- ✅ Detailed code comments for educational purposes

### How to Run

**Step 1: Start the Server**
```bash
py CYB333_Midterm/server.py
```

Wait for the message: `[*] Waiting for client connection...`

**Step 2: Start the Client (in a separate terminal)**
```bash
py CYB333_Midterm/client.py
```

**Expected Output:**
- Server displays connection established, message received, and acknowledgment sent
- Client displays successful connection, message sent, and server response received

---

## Part 2: Port Scanner

### Description

A TCP port scanner that identifies open ports on specified targets:
- **Target 1**: localhost (127.0.0.1) - scans ports 1-1024
- **Target 2**: scanme.nmap.org - scans common ports (16 ports)

### Features

- ✅ Scans multiple targets automatically
- ✅ Service identification for open ports
- ✅ Progress indicators for long scans
- ✅ Comprehensive error handling
- ✅ Ethical notice and responsible scanning practices
- ✅ Clear summary reports

### How to Run

```bash
py CYB333_Midterm/port_scanner.py
```

**Expected Behavior:**
1. Displays ethical notice
2. Scans localhost (1-2 minutes)
3. Scans scanme.nmap.org (10-30 seconds)
4. Displays summary of findings

**Typical Results:**
- **Localhost**: Usually shows ports 135 (epmap) and 445 (microsoft-ds) on Windows
- **scanme.nmap.org**: Typically shows ports 22 (SSH) and 80 (HTTP)

---

## Development Approach

### Planning Phase
1. Reviewed socket programming concepts from course materials
2. Researched Python's `socket` module documentation
3. Planned code structure with error handling in mind
4. Designed output format for clear demonstration

### Implementation Phase
1. **Server Development**: Started with basic socket creation, binding, and listening
2. **Client Development**: Implemented connection logic and message exchange
3. **Port Scanner**: Built scanning function, then added multi-target capability
4. **Testing**: Iteratively tested each component and refined error handling

### Challenges Encountered
- **Port Already in Use**: Resolved by implementing proper socket cleanup and error messages
- **Scan Performance**: Balanced thoroughness with reasonable execution time
- **Output Clarity**: Designed output to be both informative and screenshot-friendly

---

## GitHub Copilot Usage and Reflection

### How GitHub Copilot Assisted

**1. Code Generation**
- Provided socket creation boilerplate code
- Suggested error handling patterns
- Generated comprehensive comments and docstrings

**2. Problem Solving**
- Helped troubleshoot WinError 10048 (port in use)
- Suggested timeout values for port scanning
- Recommended best practices for socket cleanup

**3. Documentation**
- Assisted in writing clear code comments
- Helped structure README.md
- Provided suggestions for professional output formatting

### Example Prompts Used
- "Create a TCP server that listens on localhost port 8888"
- "Add error handling for socket connection failures"
- "Write a port scanner function with timeout handling"
- "How to properly close sockets in Python"

### Learning Outcomes
- Gained deeper understanding of socket programming fundamentals
- Learned importance of proper error handling in network applications
- Developed skills in ethical network reconnaissance
- Improved ability to write clear, documented code
- Enhanced troubleshooting skills for network-related issues

### Copilot's Impact on Learning
GitHub Copilot accelerated development while maintaining learning objectives. Rather than replacing understanding, it served as an intelligent assistant that:
- Provided syntax help without obscuring concepts
- Offered best practices that improved code quality
- Enabled focus on understanding network concepts rather than syntax details
- Demonstrated professional coding standards

---

## Security and Ethical Considerations

### Ethical Scanning Practices

**Permission is Essential**
- ⚠️ **Never scan networks or systems without explicit authorization**
- This project only scans authorized targets:
  - **127.0.0.1 (localhost)**: Your own computer
  - **scanme.nmap.org**: Explicitly provided by Nmap for testing purposes

### Legal and Ethical Framework

**Computer Fraud and Abuse Act (CFAA)**
- Unauthorized port scanning can be illegal under federal law
- Always obtain written permission before scanning networks
- Understand that "just testing" is not a legal defense

**Responsible Disclosure**
- If vulnerabilities are discovered, report them responsibly
- Follow established disclosure timelines
- Protect sensitive information

**Professional Ethics**
- Use security tools only for authorized testing or educational purposes
- Respect privacy and data protection laws
- Maintain confidentiality of discovered vulnerabilities

### Security Best Practices Demonstrated

1. **Error Handling**: Prevents information leakage through error messages
2. **Timeout Implementation**: Prevents resource exhaustion
3. **Clear Logging**: Enables audit trails and troubleshooting
4. **Ethical Notices**: Reminds users of legal obligations

### Educational Context

This project was developed in a controlled educational environment for learning purposes. The techniques demonstrated should only be applied:
- On systems you own
- With explicit written authorization
- In authorized testing environments
- For legitimate security research with proper protocols

---

## Technical Requirements

### Prerequisites
- Python 3.x (tested with Python 3.13.7)
- Windows 10/11 (code is cross-platform compatible)
- VS Code with Python extension (recommended)
- Network connectivity for remote scanning

### Dependencies
- No external packages required (uses Python standard library only)
- `socket` module (built-in)
- `datetime` module (built-in)

---

## Project Structure

```
NU-folder/
└── CYB333_Midterm/
    ├── server.py          # TCP server implementation
    ├── client.py          # TCP client implementation
    ├── port_scanner.py    # Port scanning tool
    └── README.md          # This file
```

---

## Testing and Verification

### Part 1: TCP Communication
- ✅ Server successfully binds to port 8888
- ✅ Client successfully connects to server
- ✅ Message transmission works bidirectionally
- ✅ Error handling tested (port in use, connection refused)
- ✅ Clean socket shutdown verified

### Part 2: Port Scanner
- ✅ Successfully scans localhost ports 1-1024
- ✅ Successfully scans scanme.nmap.org
- ✅ Correctly identifies open ports
- ✅ Service identification works
- ✅ Error handling tested (unreachable hosts, timeouts)

---

## Screenshots

Screenshots demonstrating successful execution are included in the project submission:

1. **TCP Server Output**: Shows listening, connection, message receipt, and acknowledgment
2. **TCP Client Output**: Shows connection, message sent, and response received
3. **Port Scanner - Localhost**: Shows scan results for 127.0.0.1
4. **Port Scanner - Remote**: Shows scan results for scanme.nmap.org

---

## References

See `CITATIONS.md` for complete APA-formatted citations.

---

## Acknowledgments

- Course materials and lectures from CYB333
- GitHub Copilot for development assistance
- Nmap project for providing scanme.nmap.org as a testing resource
- Python Software Foundation for excellent documentation

---

## License and Academic Integrity

This project was completed as part of academic coursework. The code may be used for educational reference with proper attribution. All work is original except where explicitly cited.

**Academic Integrity Statement**: This project represents my own work. GitHub Copilot was used as an assistive tool, but all code was reviewed, understood, and verified by me before submission.

---

**End of README**
