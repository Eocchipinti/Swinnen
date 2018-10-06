# -*- coding: utf-8 -*-


def maxnote(liste):
    m = liste[0]
    for i in range(1, len(liste)):
        if m < liste[i]:
            m = liste[i]
    return m


def minnote(liste):
    m = liste[0]
    for i in range(1, len(liste)):
        if m > liste[i]:
            m = liste[i]
    return m


def moyenne(liste):
    s = 0.
    for i in range(len(liste)):
        s += liste[i]
    return s / len(liste)


note = []
n = float(input("n = "))
while n >= 0:
    note.append(n)
    print("Note la plus basse: ", minnote(note))
    print("Note la plus haute: ", maxnote(note))
    print("La moyenne des notes: ", moyenne(note))
    n = float(input("n = "))
