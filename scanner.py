import socket
import time
from concurrent.futures import ThreadPoolExecutor


def ports_valides(debut, fin):
    return 1 <= debut <= fin <= 65535


def resoudre_cible(target):
    try:
        ip = socket.gethostbyname(target)
        return ip

    except socket.gaierror:
        return None


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

#ports = [22, 80, 443, 8000]
# Programme principal
""""
target = input("Adresse IP ou nom de domaine : ")

ip = resoudre_cible(target)

if ip is None:
    print("Erreur : impossible de résoudre l'adresse")

else:
    print(f"Adresse IP : {ip}")

    try:
        debut_port = int(input("Premier port : "))
        fin_port = int(input("Dernier port : "))

    except ValueError:
        print("Erreur : veuillez entrer des nombres entiers")

    else:
        if not ports_valides(debut_port, fin_port):
            print("Erreur : plage de ports invalide")
        else:
            ports = range(debut_port, fin_port + 1)

            debut = time.time()
            ports_ouverts = scan(ip, ports)
            fin = time.time()

            print(f"{ports_ouverts} port(s) ouvert(s)")
            print(f"Durée du scan : {fin - debut:.2f} secondes")
            print("Scan terminé")

"""
target = "127.0.0.1"
ports = range(7990, 8011)

# Scan séquentiel
print("=== Scan séquentiel ===")

debut = time.perf_counter()
scan(target, ports)
fin = time.perf_counter()

print(f"Durée : {fin - debut:.4f} secondes")


# Scan multithreadé
print("\n=== Scan multithreadé ===")

debut = time.perf_counter()
nb_ouverts = scan_thread(target, ports)
print(f"{nb_ouverts} port(s) ouvert(s)")
fin = time.perf_counter()

print(f"Durée : {fin - debut:.4f} secondes")