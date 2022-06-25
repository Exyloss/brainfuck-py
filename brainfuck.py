#!/usr/bin/env python3
import argparse
import sys
import os

def end_loop(w):
    """
    Fonction permettant de trouver
    la fin d'une boucle while en
    brainfuck.
    """
    tab = [1]
    for i in range(len(w)):
        if w[i] == "[":
            tab.append(1)
        elif w[i] == "]":
            tab.pop()
            if len(tab) == 0:
                return i

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

def interpreter(script,ptr=0,vals=[0], debug=True):
    """
    Fonction prennant en paramètre un script brainfuck
    et renvoyant un tuple contenant le tableau des valeurs
    modifiées et la dernière position du pointeur.
    """
    for i in range(len(script)):
        if "]" in script[i:] and ("[" not in script[i:] or script[i:].index("]") < script[i:].index("[")):
                continue
        elif script[i] == ">":
            if ptr == len(vals)-1: # Si le pointeur est à la fin du tableau
                vals.append(0)
            ptr += 1 # Déplacer le pointeur vers la droite
        elif script[i] == "<":
            if ptr == 0: # Si le pointeur est au début du tableau
                print("Erreur, pointeur inférieur à zéro caractère "+str(i+1)+".")
                quit()
            ptr -= 1 # Déplacer le pointeur vers la gauche
        elif script[i] == "+":
            vals[ptr] += 1 # On incrémente la valeur située à l'adresse du pointeur
        elif script[i] == "-":
            vals[ptr] -= 1 # On décrémente la valeur située à l'adresse du pointeur
        elif script[i] == ".":
            sys.stdout.write(chr(vals[ptr]))
        elif script[i] == ",":
            vals[ptr] = int(input(""))
        elif script[i] == "[":
            w = script[i+1:] # Tableau débutant après [
            try:
                end_w = end_loop(w)
            except:
                print("Erreur, boucle while non fermée.")
                quit()
            w = w[:end_w] # Tableau contenant les valeurs à l'interieur de la boucle
            while vals[ptr]:
                (ptr, vals) = interpreter(w, ptr, vals) # Utilisation récursive de la fonction afin de faire fonctionner la boucle
    return (ptr, vals)

def bf2c(script, name):
    f = open(name, "w")
    f.write("#include <stdio.h>\n")
    f.write("int main() {\n")
    f.write("unsigned char* ptr;\n")
    for i in script:
        if i == "+":
            f.write("++(*ptr);\n")
        elif i == "-":
            f.write("--(*ptr);\n")
        elif i == ">":
            f.write("ptr++;\n")
        elif i == "<":
            f.write("ptr--;\n")
        elif i == ".":
            f.write("putchar(*ptr);\n")
        elif i == ",":
            f.write("(*ptr) = getchar();\n")
        elif i == "[":
            f.write("while (*ptr) {\n")
        elif i == "]":
            f.write("}\n")
    f.write("}\n")
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='interpréteur brainfuck')
    parser.add_argument('file', nargs='?', metavar='FICHIER', type=str, help='renseigner un fichier contenant les instructions')
    parser.add_argument('--translate', nargs='?', metavar='FICHIER', type=str, help='renseigner un fichier de sortie')
    args = parser.parse_args()

    if args.file != None:
        script = file_to_str(args.file)
    else:
        script = input("Instructions : ")

    if args.compile != None:
        bf2c(script, args.compile)
        r = input("Compiler le fichier C ? (o/n) ")
        if r == "o":
            os.system("gcc "+args.compile)
            print("Fichier compilé avec comme nom «a.out».")
        quit()

    interpreter(script)
