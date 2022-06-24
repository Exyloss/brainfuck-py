#!/usr/bin/env python3
import argparse

def file_to_str(file):
    f = open(file, 'r')
    temp = ""
    for i in f.readlines():
        temp += i
    return temp

parser = argparse.ArgumentParser(description='interprêteur brainfuck')
parser.add_argument('--file', nargs='?', metavar='FICHIER', type=str, help='renseigner un fichier contenant les instructions')
args = parser.parse_args()

if args.file != None:
    script = file_to_str(args.file)
else:
    script = input("Instructions : ")

def interpreter(script,ptr=0,vals=[0],chaine=""):
    for i in range(len(script)):
        if "]" in script[i:] and ("[" not in script[i:] or script[i:].index("]") < script[i:].index("]")):
                continue
        elif script[i] == ">":
            if ptr == len(vals)-1:
                vals.append(0)
            ptr += 1
        elif script[i] == "<":
            if ptr == 0:
                print("Erreur, valeur du pointeur inférieure à zéro caractère "+str(i+1)+".")
                quit()
            ptr -= 1
        elif script[i] == "+":
            vals[ptr] += 1
        elif script[i] == "-":
            if vals[ptr] == 0:
                print("Erreur, valeur inférieure à zéro caractère "+str(i+1)+".")
                quit()
            else:
                vals[ptr] -= 1
        elif script[i] == ".":
            chaine += chr(vals[ptr])
        elif script[i] == "[":
            w = script[i+1:]
            try:
                end_w = w.index("]")
            except:
                print("Erreur, boucle while non fermée.")
                quit()
            w = w[:end_w]
            while vals[ptr] != 0:
                (chaine, ptr, vals) = interpreter(w)
    return (chaine, ptr, vals)

print(interpreter(script)[0])
