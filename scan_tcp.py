import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port,timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    resultat = sock.connect_ex((target, port))
    sock.close()
    if resultat == 0:
        return True
    else:
        return False

def scan(target, ports,timeout):
    ports_ouverts = 0
    resultats_scan = []
    for port in ports:
        if scan_port(target, port,timeout):
            ports_ouverts += 1
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "inconnu"

            print(f"Port {port} : ouvert ({service})")
            resultats_scan.append([port, service])

    return ports_ouverts, resultats_scan


def scan_thread(target, ports,timeout):
    ports_ouverts = 0
    resultats_scan = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        resultats = executor.map(lambda port: scan_port(target, port,timeout),ports)

        for port, ouvert in zip(ports, resultats):
            if ouvert:
                ports_ouverts += 1

                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "inconnu"

                print(f"Port {port} : ouvert ({service})")
                resultats_scan.append([port, service])

    return ports_ouverts, resultats_scan