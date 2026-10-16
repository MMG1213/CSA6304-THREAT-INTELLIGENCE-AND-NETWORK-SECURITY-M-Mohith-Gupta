"""Exercise 2: Basic TCP port scanner for authorized defensive testing only.
Use only on localhost or systems for which you have explicit permission.
"""
import socket

def scan_ports(host, ports, timeout=0.5):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                if sock.connect_ex((host, port)) == 0:
                    open_ports.append(port)
        except (socket.gaierror, OSError) as error:
            print(f"Could not test port {port}: {error}")
    return open_ports

if __name__ == "__main__":
    print("=== Simple TCP Port Scanner (authorized targets only) ===")
    host = input("Enter target host (for practice, use 127.0.0.1): ").strip()
    raw_ports = input("Enter ports separated by commas (example: 22,80,443): ").strip()
    try:
        ports = sorted({int(item.strip()) for item in raw_ports.split(",") if item.strip()})
        if not ports or any(port < 1 or port > 65535 for port in ports):
            raise ValueError("Ports must be between 1 and 65535.")
    except ValueError as error:
        print(f"Invalid port list: {error}")
    else:
        found = scan_ports(host, ports)
        print(f"\\nTarget: {host}")
        if found:
            print("Open TCP ports:", ", ".join(map(str, found)))
        else:
            print("No open TCP ports detected in the selected list.")
