import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    resultat = sock.connect_ex((target, port))
    sock.close()
    if resultat == 0:
        return True
    else:
        return False

def scan(target, ports):
    ports_ouverts = 0

    for port in ports:
        if scan_port(target, port):
            ports_ouverts += 1
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "inconnu"

            print(f"Port {port} : ouvert ({service})")

    return ports_ouverts


def scan_thread(target, ports):
    ports_ouverts = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        resultats = executor.map(lambda port: scan_port(target, port),ports)

        for port, ouvert in zip(ports, resultats):
            if ouvert:
                ports_ouverts += 1

                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "inconnu"

                print(f"Port {port} : ouvert ({service})")

    return ports_ouverts