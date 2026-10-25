import time

from scan_tcp import scan, scan_thread
from utils import ports_valides, resoudre_cible

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
            print("1 - Scan séquentiel")
            print("2 - Scan multithreadé")

            choix = input("Votre choix : ")

            debut = time.perf_counter()
            
            if choix == "1":
                ports_ouverts = scan(ip, ports)

            elif choix == "2":
                ports_ouverts = scan_thread(ip, ports)

            else:
                print("Choix invalide")

            if choix == "1" or choix == "2":
                fin = time.perf_counter()

                print(f"{ports_ouverts} port(s) ouvert(s)")
                print(f"Durée du scan : {fin - debut:.4f} secondes")
                print("Scan terminé")