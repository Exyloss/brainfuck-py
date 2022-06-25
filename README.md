# brainfuck-py
Interpréteur du langage brainfuck écrit en python
# Fonctionnalités
## Mise en page
Support des commentaires et des sauts de lignes,
les commentaires sont à utiliser en fin de ligne
après un espace, comme ceci :
```
++++++++++ Ceci est un commentaire
[>+++++++>++++++++++>+++>+<<<<-] Fin de la boucle
>++.>+.+++++++..+++.>++.<<++++++++
+++++++.>.+++.------.--------.>+.>.
```
## Caractères supportés
Support des caractères suivants :
 - \+
 - \-
 - <
 - \>
 - [
 - ]
 - .
 - ,
# Utilisation
## Lire l'expression depuis un fichier
python brainfuck.py --file [nom_du_fichier]
## Écrire et lire l'expression dans l'interpréteur
python brainfuck.py
