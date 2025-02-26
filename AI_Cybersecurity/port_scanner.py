import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.create_connection((target, port), timeout=1):
                open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            pass
    return open_ports

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Change this to your target IP
    ports_to_scan = [66, 80, 81, 443, 445, 457, 1080, 1100, 1241, 1352]
    
    open_ports = scan_ports(target_ip, ports_to_scan)
    
    print(f"Open Ports on {target_ip}: {open_ports}")
