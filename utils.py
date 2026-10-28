import socket

def ports_valides(debut, fin):
    return 1 <= debut <= fin <= 65535


def resoudre_cible(target):
    try:
        ip = socket.gethostbyname(target)
        return ip

    except socket.gaierror:
        return None
    
def export_csv(resultats_scan):
    with open("resultats.csv", "w") as fichier:
        fichier.write("port,service\n")

        for port, service in resultats_scan:
            fichier.write(f"{port},{service}\n")