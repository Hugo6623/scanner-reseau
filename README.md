# Scanner réseau TCP

Petit projet personnel de scanner de ports TCP en Python, pour mettre en pratique ce que j'apprends en réseau et en cybersécurité.

L'objectif est d'améliorer le scanner petit à petit en ajoutant de nouvelles fonctionnalités.

## Fonctionnalités actuelles

- Scanner une plage de ports TCP
- Détecter les ports ouverts
- Afficher le service associé à un port (HTTP, SSH...)
- Vérifier que la plage de ports est valide
- Afficher le nombre de ports ouverts et la durée du scan
- Accepter une adresse IP ou un nom de domaine
- Gérer les erreurs de saisie et de résolution d'adresse

## Utilisation

Lancer le programme avec :

```bash
python3 scanner.py
```

Puis entrer l'adresse IP à scanner et la plage de ports.

Exemple :

```text
Adresse IP cible : 127.0.0.1
Premier port : 1
Dernier port : 1000
```

## Améliorations prévues

- Améliorer la gestion des erreurs
- Accélérer le scan avec des threads
- Récupérer plus d'informations sur les services
- Sauvegarder les résultats dans un fichier
