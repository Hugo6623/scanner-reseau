import socket
import time

def ports_valides(debut, fin):
    return 1 <= debut <= fin <= 65535

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



#ports = [22, 80, 443, 8000]

target = input("Adresse IP cible : ")

debut_port = int(input("Premier port : "))
fin_port = int(input("Dernier port : "))

if not ports_valides(debut_port, fin_port):
    print("Erreur : plage de ports invalide")
else:
    ports = range(debut_port, fin_port + 1)

    debut = time.time()
    ports_ouverts = scan(target, ports)
    fin = time.time()

    print(f"{ports_ouverts} port(s) ouvert(s)")
    print(f"Durée du scan : {fin - debut:.2f} secondes")
    print("Scan terminé")

