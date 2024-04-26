# Qui est-ce

Projet de S3 en L2 informatique. Jeu de plateau "Qui-est-ce ?".

# Membres

Laurent Antoinette - Romain Campillo - Tony Nguyen - Frederic Sar (Groupe B)

Chargé de TD : 
- Vincent Boudet
- Philippe Janssen
- Sylvain Daudé
- Anne-Elisabeth Baert
- Clémentine Nebut
- Nicolas Pompidor
- Julien Destombes


# Commandes Git

Pour upload des changements :

```
git add .
git commit -m "message"
git push origin branch
```

Pour download des changements : 
```
git pull origin main --no-rebase
```

Pour télécharger projet :
```
git clone https://gitlab.etu.umontpellier.fr/e20180001091/qui-est-ce.git
```

Pour changer de branche :
```
git checkout branch
```
Si changement vers une branch qui n'existe pas localement
```
git checkout -b branch
```


# IDE

[Lien pour télécharger pydev (Eclipse)](https://devstory.net/11379/installer-pydev-pour-eclipse)

# Fonctionnalités de base (Partie local seul, 1 personnage mystère)

- [x] Poser des question imbriqués avec des connecteurs logiques
- [x] Mode facile : cochage automatique des portraits, indice nombre de personnes qui répondent non à une question


# Extension à implémenter

- Jouer contre l'ordinateur (Algorithme de décision) (Local 1vsOrdi, 2 personnage mystère)
- Jouer à deux (Réseaux)

# Rendus
- [x] 6 Mars 2022 Rendu du jeu de base
- [x] 27 Mars 2022 Rendu du générateur 
- [x] 16 Avril 2022 Rendu rapport
- [ ] 25 Avril 2022 Soutenance et démo **(SOON)**

# Evaluation
- Rendu logiciel : 10 points
- Rapport : 5 points
- Soutenance : 5 points

# Requirements
- [Python3.10.2](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)
- [tkinter](https://askubuntu.com/questions/1224230/how-to-install-tkinter-for-python-3-8)
- [pillow](https://pillow.readthedocs.io/en/stable/installation.html)

# Convention de nommage Python
- nom_fonction() snake_case()
- NomClasse CamelCase

[Source](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)

# Test unitaires
-pytest

# UML

## Diagramme de classe
![Diagramme de classe du jeu "Qui-est-ce?"](/docs/uml/JeuClassDiagram.jpg)

![Diagramme de classe du générateur](/docs/uml/ClassDiagramGenerateur.jpg)

# Installation

Vérifier que vous avez une version de python récente et que avez le module Pillow de la façon suivante :
![Instructions pour vérifier la version de python et pillow](/docs/images/terminalVerif.png)

```
#installer tkinter
sudo apt install python3-tk

#installer pillow
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

Paramétrez correctement votre PYTHONPATH pour qu'il inclus notre projet.

![Terminale PYTHONPATH](/docs/images/terminalPythonpath.png)

Pour modifier le $PYTHONPATH, il faut modifier le ~/.bashrc

Ouvrez le fichier comme-ceci :
```
sudo gedit ~/.bashrc
```

Ajouter à la fin du fichier le chemin vers le dossier

![.bashrc](/docs/images/bashrc.png)

```
export PYTHONPATH=$PYTHONPATH:<path>/qui-est-ce
```

Ou alors, si vous n'avez pas sudo, tapez la commande ci-dessus directement dans le terminale. Noubliez pas de vérifier avec echo $PYTHONPATH

# Exécution
Manuel d'utilisation dans /docs/manuel/

## Le jeu

<!-- ![Image d'un terminale bash](/docs/images/terminalExec.png) -->

![Fenetre Qui-est-ce?](/docs/images/fenetreExample.png)

```
python3 ./project/src/jeu
```

## Le générateur


![Fenetre Qui-est-ce?](/docs/images/fenetreExampleGen.png)

```
python3 ./project/src/generateur/ ./ressources/img/<directory_name_here>/ #n'oublier pas le dernier slash à la fin
```
directory_name

├── ClashRoyale

└── Madagascar

└── PlateauOriginal


```
python3 ./project/src/generateur/ -save #pour récupérer la dernière sauvegarde
```


![Fenetre générateur regarde les attributs](/docs/images/fenetreExampleGenAttribut.png)
![Fenetre générateur l'utilisateur choisit des valeurs](/docs/images/fenetreExampleGenSelectionValeurs.png)
![Fenetre générateur en cours de remplissage](/docs/images/fenetreExampleGenSemiRempli.png)
![Fenetre générateur a généré](/docs/images/fenetreExampleGenJSON.png)


# Rapport

Le rapport "rapport.pdf" est dans /rapport/rapport.pdf

