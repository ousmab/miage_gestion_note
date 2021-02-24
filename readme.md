# MIAGE APPLICATION DE GESTION DES NOTES DES ETUDIANTS
Projet réalisé en MIAGE dans le cadre d'environnement et dévéloppement intégré (EDI)

## Installation

### python sur windows
```
-installer python 3 sur votre machine si vous êtes sur windows 

```
lien de téléchargement de python https://www.python.org/downloads/

### installer le gestionnaire de dépendance PIP 

- Télécharger le fichier get-pip.py https://bootstrap.pypa.io/get-pip.py
- ouvrir le terminal cmd et executer le fichier en faisant > python get-pip.py

- plus d'informations sur l'installation de pip ici 

https://stackoverflow.com/questions/4750806/how-can-i-install-pip-on-windows

### installer un virtualenv 
```
- exécuter dans le terminal la commande > pip install virtualenv
```
### créer un environnement virtuel pour votre projet avec pip
```
- aller dans le dossier de votre projet avec cd /dossier/de/mon/projet
- exécuter la commande virtualenv venv 

NB (venv est le nom que vous donnez a votre environnement)

- et enfin activer votre environnement en faisant venv\Scripts\activate
```
### cloner le dépôt github du projet miage rss reader
```
git clone https://github.com/ousmab/miage_rss_reader.git

```
NB on suppose que vous avez git installer sur votre système sinon aller lire ceci 
https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement/6113016-installez-git-sur-votre-ordinateur

### installer les dépendances du projet avec pip
```
- exécuter pip install -r requirements.txt
```

### Lancer l'application
```
Placez vous au même niveau que le fichier main.py et éxécutez > python main.py

Plus d'informations sur flask voici le lien https://flask.palletsprojects.com/en/1.1.x/
```
