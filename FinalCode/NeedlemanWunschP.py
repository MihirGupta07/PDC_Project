import numpy
from joblib import Parallel, delayed
import multiprocessing as mp
from string import *

al_mat = ""
p_mat = ""
# s1 = input('Enter a file name: ')
list1 = "ATGTAGTGTATAAAGTACATGCA"
# s2 = input('Enter a file name: ')
list2 = "ATGTAGTACATGCA"
match = 1
mismatch = -1
gap = -2


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
    global al_mat
    global p_mat
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
    Parallel(n_jobs=2)(delayed(calc1)(i, penalty) for i in range(m))
    Parallel(n_jobs=2)(delayed(calc2)(i, penalty) for i in range(n))
    p_mat[0][0] = 0
    for i in range(1, m):
        Parallel(n_jobs=2)((delayed(calc3)(penalty, i, j, s1, s2) for j in range(1, n)))
    print(numpy.matrix(al_mat))
    print(numpy.matrix(p_mat))
    score = 0
    i = m - 1
    j = n - 1
    while i > 0 and j > 0:
        # Parallel(n_jobs=2)(delayed(calc4)(al_mat, i, j) for i in range(1, m))
        # calc4(al_mat, i, j)
        if (
            al_mat[i - 1][j] > al_mat[i - 1][j - 1]
            and al_mat[i - 1][j] > al_mat[i][j - 1]
        ):
            print("1st If")
            i = i - 1
            s2 = s2[: i + j] + "-" + s2[i + j :]

        elif (
            al_mat[i][j - 1] > al_mat[i - 1][j - 1]
            and al_mat[i][j - 1] > al_mat[i - 1][j]
        ):
            print("2nd If")
            j = j - 1
            s2 = s2[: i + j] + "-" + s2[i + j :]

        elif (
            al_mat[i - 1][j - 1] > al_mat[i][j - 1]
            and al_mat[i - 1][j - 1] > al_mat[i - 1][j]
        ):
            print("3rd If")

            i = i - 1
            j = j - 1

    print("check")
    print(s1)
    print(s2)
    score = al_mat[m - 1][n - 1]
    print(score)

    return (s1, score)


def calc1(i, penalty):
    print("done")
    global p_mat
    global al_mat
    al_mat[i][0] = penalty["GAP"] * i
    p_mat[i][0] = "V"
    # return (al_mat, p_mat)


def calc2(j, penalty):
    global p_mat
    global al_mat
    al_mat[0][j] = penalty["GAP"] * j
    p_mat[0][j] = "H"
    # return (al_mat, p_mat)


def calc3(penalty, i, j, s1, s2):
    global p_mat
    global al_mat

    di = al_mat[i - 1][j - 1] + Diagonal(s1[j - 1], s2[i - 1], penalty)
    ho = al_mat[i][j - 1] + penalty["GAP"]
    ve = al_mat[i - 1][j] + penalty["GAP"]
    al_mat[i][j] = max(di, ho, ve)
    p_mat[i][j] = Pointers(di, ho, ve)


def calc4(al_mat, i, j):
    if al_mat[i - 1][j] > al_mat[i - 1][j - 1] and al_mat[i - 1][j] > al_mat[i][j - 1]:
        print("1st If")
        i = i - 1
        s2 = s2[: i + j] + "-" + s2[i + j :]

    elif (
        al_mat[i][j - 1] > al_mat[i - 1][j - 1] and al_mat[i][j - 1] > al_mat[i - 1][j]
    ):
        print("2nd If")
        j = j - 1
        s2 = s2[: i + j] + "-" + s2[i + j :]

    elif (
        al_mat[i - 1][j - 1] > al_mat[i][j - 1]
        and al_mat[i - 1][j - 1] > al_mat[i - 1][j]
    ):
        print("3rd If")

        i = i - 1
        j = j - 1


NeedlemanWunch(list1, list2, match, mismatch, gap)
