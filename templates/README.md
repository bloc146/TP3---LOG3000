Raison d’être:
Ce dossier contient le fichier HTML. Ce fichier sert à afficher l’interface du site. 
Cela permet de séparer ce qui est affiché à l’écran de la logique du programme en Python.

Contenu:
Le fichier principal est index.html. Il correspond à la page principale de la calculatrice. Il contient la structure
de la page, les boutons de la calculatrice et la zone où le résultat est affiché. Il inclut aussi un peu de
JavaScript simple pour gérer les clics et utilise une feuille de style pour l’apparence.

Dépendances et hypothèses:
Ces fichiers sont utilisés par Flask grâce à la fonction render_template. Le fichier index.html peut recevoir des
données envoyées par le backend, par exemple une valeur de résultat à afficher. Le bon fonctionnement
dépend aussi de la présence du dossier static, qui contient le fichier style.css utilisé pour le style de la page.