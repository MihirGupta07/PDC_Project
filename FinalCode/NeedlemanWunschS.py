import re
import collections
import csv
import sys
import numpy
from string import *

# s1 = input('Enter a file name: ')
list1 = "ATGTAGTGTATAAAGTACATGCA"
# s2 = input('Enter a file name: ')
list2 = "ATGTAGTACATGCA"
# match = 1
# mismatch = -1
# gap = -2


def Diagonal(n1, n2, pt):
    if n1 == n2:
        return pt["MATCH"]
    else:
        return pt["MISMATCH"]


def Pointers(di, ho, ve):

    pointer = max(di, ho, ve)

    if di == pointer:
        return "D"
    elif ho == pointer:
        return "H"
    else:
        return "V"


def NeedlemanWunch(s1, s2, match, mismatch, gap):
    print("here")
    penalty = {
        "MATCH": match,
        "MISMATCH": mismatch,
        "GAP": gap,
    }
    n = len(s1) + 1
    m = len(s2) + 1
    al_mat = numpy.zeros((m, n), dtype=int)
    p_mat = numpy.zeros((m, n), dtype=str)
    for i in range(m):
        al_mat[i][0] = penalty["GAP"] * i
        p_mat[i][0] = "V"

    for j in range(n):
        al_mat[0][j] = penalty["GAP"] * j
        p_mat[0][j] = "H"

    p_mat[0][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            di = al_mat[i - 1][j - 1] + Diagonal(s1[j - 1], s2[i - 1], penalty)
            ho = al_mat[i][j - 1] + penalty["GAP"]
            ve = al_mat[i - 1][j] + penalty["GAP"]
            al_mat[i][j] = max(di, ho, ve)
            p_mat[i][j] = Pointers(di, ho, ve)
    print(numpy.matrix(al_mat))
    print(numpy.matrix(p_mat))

    path = ""
    score = 0
    i = m - 1
    j = n - 1
    while i > 0 and j > 0:
        if (
            al_mat[i - 1][j] > al_mat[i - 1][j - 1]
            and al_mat[i - 1][j] > al_mat[i][j - 1]
        ):
            i = i - 1
            s2 = s2[: i + j] + "-" + s2[i + j :]

        elif (
            al_mat[i][j - 1] > al_mat[i - 1][j - 1]
            and al_mat[i][j - 1] > al_mat[i - 1][j]
        ):
            j = j - 1
            s2 = s2[: i + j] + "-" + s2[i + j :]

        elif (
            al_mat[i - 1][j - 1] > al_mat[i][j - 1]
            and al_mat[i - 1][j - 1] > al_mat[i - 1][j]
        ):
            i = i - 1
            j = j - 1

    print("check")
    print(s1)
    print(s2)
    score = al_mat[m - 1][n - 1]
    print(score)
    return (s1, score)


# NeedlemanWunch(list1, list2, match, mismatch, gap)
