#!/usr/bin/env python3
import argparse
import sys

def file_to_str(file):
    f = open(file, 'r')
    temp = ""
    for i in f.readlines():
        for j in i:
            if j in "[]<>+-.,":
                temp += j
            elif j == "\t" or j == " ":
                continue
            else:
                break
    return temp

def interpreter(script,ptr=0,vals=[0]):
    """
    Fonction prennant en paramètre un script brainfuck
    et renvoyant un tuple contenant le tableau des valeurs
    modifiées et la dernière position du pointeur.
    """
    for i in range(len(script)):
        if "]" in script[i:] and ("[" not in script[i:] or script[i:].index("]") < script[i:].index("]")):
                continue
        elif script[i] == ">":
            if ptr == len(vals)-1: # Si le pointeur est à la fin du tableau
                vals.append(0)
            ptr += 1 # Déplacer le pointeur vers la droite
        elif script[i] == "<":
            if ptr == 0: # Si le pointeur est au début du tableau
                print("Erreur, inférieur à zéro caractère "+str(i+1)+".")
                quit()
            ptr -= 1 # Déplacer le pointeur vers la gauche
        elif script[i] == "+":
            vals[ptr] += 1 # On incrémente la valeur située à l'adresse du pointeur
        elif script[i] == "-":
            if vals[ptr] == 0: # Si la valeur à l'adresse du pointeur est à zéro
                print("Erreur, valeur inférieure à zéro caractère "+str(i+1)+".")
                quit()
            else:
                vals[ptr] -= 1 # On incrémente la valeur située à l'adresse du pointeur
        elif script[i] == ".":
            sys.stdout.write(chr(vals[ptr]))
        elif script[i] == ",":
            while True:
                try:
                    r = int(input("Valeur à ajouter : "))
                    vals[ptr] = r
                    break
                except:
                    print("Erreur, vous n'avez pas renseigné de nombre.")
        elif script[i] == "[":
            w = script[i+1:] # Tableau débutant après [
            try:
                end_w = w.index("]")
            except:
                print("Erreur, boucle while non fermée.")
                quit()
            w = w[:end_w] # Tableau contenant les valeurs à l'interieur de la boucle
            while vals[ptr] != 0:
                (ptr, vals) = interpreter(w) # Utilisation récursive de la fonction afin de faire fonctionner la boucle
    return (ptr, vals)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='interprêteur brainfuck')
    parser.add_argument('--file', nargs='?', metavar='FICHIER', type=str, help='renseigner un fichier contenant les instructions')
    args = parser.parse_args()

    if args.file != None:
        script = file_to_str(args.file)
    else:
        script = input("Instructions : ")

    interpreter(script)
