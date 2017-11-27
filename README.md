## Présentation du projet

Ce projet contient de quoi vous permettre de démarrer la mise en place du site web pour votre projet.

Il permet de visualiser la base de données d'un magasin de disque.
La base de données a été récupéré sur ce site, avant d'etre simplifiée : 
[Chinook Record Store](https://chinookdatabase.codeplex.com/)

## Roles des fichiers

 - example.sqlite : la base de données `sqlite` (que vous pouvez visualiser avec PyCharm).
Si vous préférez utiliser un autre outil que PyCharm pour gérer votre BDD SQLite, vous pouvez utiliser 
[http://sqlitebrowser.org/](DB Browser).

 - model.py : le script Python avec toutes les requêtes `SQL` vers la base de données

 - webserver.py : un script Python permettant de lancer un serveur web local sur votre machine, 
 c'est ce fichier qu'il faut exécuter pour lancer votre projet. Une fois lancé, vous pouvez voir votre projet 
 en accédant à l'URL suivante : [http://localhost:5000](http://localhost:5000).

 - templates/ : les fichiers template `HTML` pour générer les pages de votre site.

 - static/ : l'ensemble des ressources statiques (feuilles de style, fichiers javascript) 
 => vous n'avez pas à y toucher, sauf si vous etes vraiment en avance.

## Installation de Flask pour Python

 - Dans PyCharm, ouvrez le préférences (Settings) et rechercher "inter", vous devez voir votre interpréteur Python
 - Cliquer sur le "+" pour installer un nouveau module, et rechercher le module "flask"
 - Installer le module, et vous pouvez maintenant lancer le fichier "webserver.py"
 
Vous pouvez aussi utiliser `Alt-Entrée` sur l'import de flask (en rouge si pas installé), 
PyCharm vous proposera d'installer le module manquant.

## liens utiles

 * [Templates Jinja officiel](http://jinja.pocoo.org/)
 * [Templates Jinja tuto](https://realpython.com/blog/python/primer-on-jinja-templating/)
 * [Flask](http://flask.pocoo.org/)
 * [SQLite](https://www.sqlite.org/)
 * [SQL](http://sql.sh/)
 * [Bootstrap](http://getbootstrap.com/)
 * [Manager pour BD SQLite](http://sqlitebrowser.org/)
