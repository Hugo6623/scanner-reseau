import socket

def ports_valides(debut, fin):
    return 1 <= debut <= fin <= 65535


def resoudre_cible(target):
    try:
        ip = socket.gethostbyname(target)
        return ip

    except socket.gaierror:
        return None