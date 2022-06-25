# brainfuck-py
Interpréteur du langage brainfuck écrit en python
# Fonctionnalités
## Mise en page
Support des commentaires, des sauts de lignes
et des indentations,
les commentaires peuvent être placés à la fin
d'une ligne, comme ici :
```brainfuck
++++++++++ Ceci est un commentaire
[
    >+++++++>++++++++++>+++>+<<<<-
] Fin de la boucle
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
# À faire
 - [ ] Support des boucles imbriquées
 - [ ] Traduction brainfuck en C pour compiler
