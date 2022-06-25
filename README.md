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
## Traduction des instructions
Ce programme peut aussi traduire vos instructions en C,
cependant le traducteur n'indente pas le texte et ne le
compile pas. Le code peut être compilé à par à l'aide de
gcc avec la commande suivante :
```bash
$ gcc [fichier_c] -o [fichier_compilé]
```
# Utilisation
## Lire l'expression depuis un fichier
python brainfuck.py --file [nom_du_fichier]
## Écrire et lire l'expression dans l'interpréteur
python brainfuck.py
## Traduire les instructions en C
python brainfuck.py --file [nom_du_fichier] --compile [fichier_sortie]
# À faire
 - [ ] Support des boucles imbriquées
 - [X] Traduction brainfuck en C pour compiler
