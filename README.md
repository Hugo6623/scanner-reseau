# Scanner réseau TCP

Petit projet personnel de scanner de ports TCP en Python, pour mettre en pratique mes connaissances en programmation et en réseaux.

L'objectif est de créer un scanner simple et de l'améliorer petit à petit en ajoutant de nouvelles fonctionnalités.

## Fonctionnalités actuelles

- Scanner une plage de ports TCP
- Détecter les ports ouverts
- Afficher le service associé à un port (HTTP, SSH...)
- Accepter une adresse IP ou un nom de domaine
- Vérifier que la plage de ports est valide
- Choisir entre un scan classique et un scan multithreadé
- Choisir le timeout des connexions
- Afficher le nombre de ports ouverts et la durée du scan
- Sauvegarder les résultats dans un fichier CSV

## Utilisation

Lancer le programme avec :

```bash
python3 scanner.py
```

Puis entrer l'adresse IP ou le nom de domaine, la plage de ports, le timeout et le mode de scan.

Exemple :

```text
Adresse IP ou nom de domaine : 127.0.0.1
Premier port : 7998
Dernier port : 8002
Timeout en secondes (ex : 0.5) : 0.5
1 - Scan séquentiel
2 - Scan multithreadé
Votre choix : 2

Port 8000 : ouvert (irdmi)
1 port(s) ouvert(s)
Durée du scan : 0.0225 secondes
Scan terminé
```

Les ports ouverts sont également enregistrés dans le fichier `resultats.csv`.

## Améliorations possibles

- Améliorer la gestion des erreurs
- Ajouter le support d'IPv6
- Récupérer plus d'informations sur les services

Pour l'instant, le scanner fonctionne avec TCP et IPv4. Il est destiné à des tests sur des machines personnelles ou avec autorisation.