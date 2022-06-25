# brainfuck-py
Interpréteur du langage brainfuck écrit en python
# Fonctionnalités
## Possibilité d'ajouter des commentaires en fin de ligne
```
++++++++++ Ceci est un commentaire
[>+++++++>++++++++++>+++>+<<<<-] Fin de la boucle
>++.>+.+++++++..+++.>++.<<++++++++
+++++++.>.+++.------.--------.>+.>.
```
## Support des caractères suivants
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
