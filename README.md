Ce projet contient de quoi vous permettre de démarrer la mise en place du site web pour votre projet.

Le projet permet de visualiser la base de données d'un magasin de disque.
La base de données a été récupéré sur ce site :
https://chinookdatabase.codeplex.com/

Voici le role de chacun des fichiers :

 - example.sqlite : la base de données sqlite (que vous pouvez visualiser avec PyCharm)
 - model.py : un script Python qui contient les requêtes SQL vers la base de données
 - webserver.py : un script Python permettant de lancer un serveur web local sur votre machine
 - templates/ : les fichiers template HTML pour générer les pages
 - static/ : l'ensemble des ressources statiques (feuilles de style, fichier javascript)

Infos et liens utiles :

Installation de Flask pour Python
 - Ouvrez un terminal windows (Menu Démarrer, Exécuter, "cmd")
 - Naviguez dans c:\Python34\Scripts (ou vers le dossier ou vous avez installé Python)
 - Taper "pip.exe --proxy=http://10.100.100.242:80 install flask"

Utiliser PyCharm pour écrire le code et lancer le serveur web

Templates Jinja
https://realpython.com/blog/python/primer-on-jinja-templating/
http://jinja.pocoo.org/

Serveur web Flask
http://flask.pocoo.org/

SQLite et SQL
https://www.sqlite.org/
http://sql.sh/

Bootstrap
http://getbootstrap.com/examples/dashboard/
http://getbootstrap.com/

Manager pour BD SQLite
http://sqlitebrowser.org/
https://www.mysql.fr/products/workbench/
