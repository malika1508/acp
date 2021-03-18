import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib.patches import Circle

# ======== pretraitement des donnees =========
def clean(data):
    qualitative_data = [
        "contact",
        "marital",
        "education",
        "day_of_week",
        "job",
        "default",
        "loan",
        "housing",
        "poutcome",
        "month",
        "y",
    ]
    data.drop(qualitative_data, 1, inplace=True)

    return data


# ========= centre reduite=============


def centre(data, n):  # retourner une matrice centre
    mean = data.describe().loc["mean"]  # recuperer la moyenne de chaque variable
    means = {}
    for col in data.columns:
        means[col] = [mean[col]] * n
    means = pd.DataFrame(means)  # cree un autre data frame qui contient les moyennes
    return data - means  # pour chaque colonne we substruct la moyenne


def centre_reduite(data, n_rows):  # return une matrice centrer et reduite
    std = data.describe().loc["std"]
    stds = {}
    for col in data.columns:
        stds[col] = [std[col]] * n_rows
    stds = pd.DataFrame(stds)
    return data / stds


# ============ car_covar/ corr =============


def var_covar(y, n_rows):  # return matrice de variance_covariance
    y_prime = np.transpose(y)
    matrice = np.dot(y_prime, y) / n_rows
    return matrice  # V = Y' Dp Y = (1/ nbr d individu) * Y' * Y


def corr(z, n_rows):  # return matrice de correlation
    z_prime = np.transpose(z)
    matrice = np.dot(z_prime, z)
    return matrice / n_rows  # R = Z' Dp Z = (1/ nbr d individu) Z' Z


# =========diago ==============


def diago(x):  # on calcules les valeurs et les vecteurs propres
    return np.linalg.eig(x)


def interpretation(vals, vects):
    inertie_totale = sum(vals)
    iner_expl = []  # inertie explique par l axe i
    for val in vals:
        iner_expl.append(val / inertie_totale)

    plt.scatter(range(10), vals)
    plt.show()


# ======= ACP ==============


def compo_prin(
    y, vals, vects
):  # retourn la projection des individus/ variables sur les axes

    c1 = np.dot(y, vects[0])  # projection des donnee sur axe 1
    c2 = np.dot(y, vects[1])  # projection des donnee sur axe 2
    c3 = np.dot(y, vects[2])  # projection des donnee sur axe 3
    w1 = sqrt(vals[0]) * vects[0]  # projection des variables sur axe 1
    w2 = sqrt(vals[1]) * vects[1]  # # projection des variables sur axe 2
    w3 = sqrt(vals[2]) * vects[2]  # # projection des variables sur axe 3
    return (c1, c2, w1, w2)


def corr_compo(y, vals, vects):
    cols = y.columns
    corre = []
    for j in range(2):
        corre.append([0] * len(cols))
        b = sqrt(vals[j])  # racine lamnda
        i = 0
        for col in cols:
            a = sqrt(var(y[col]))  # l'ecart type de la variable
            c = vects[j][i]  # u[i][j]
            val = b * c / a
            corre[j][i] = val
            i += 1
    return corre


# ========== affichage ===========
def afficher(c1, c2, w1, w2, mat, title):  # l affichage
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    circle = Circle((0, 0), 1, facecolor="none", edgecolor="blue", linewidth=3)
    # affichage du cercle de correlation
    ax[0].spines["top"].set_color("none")
    ax[0].spines["left"].set_position("zero")
    ax[0].spines["right"].set_color("none")
    ax[0].spines["bottom"].set_position("zero")
    ax[0].set_xlabel("c1")
    ax[0].set_ylabel("c2")
    ax[0].add_patch(circle)

    ax[0].scatter(mat[0], mat[1], color="blue")
    ax[0].set(xlim=(-1, 1), ylim=(-1, 1))
    ax[0].set_title(
        "cercle de correlation entre\n les anciennes et nouvelles variables"
    )

    # affichage de compo principales
    ax[1].scatter(c1, c2, color="blue", label="projection des individus")
    ax[1].scatter(w1, w2, color="red", label="projection des variables")
    ax[1].set_title(
        "la projection des individus sur les composantes \n principlae(C1, C2)"
    )
    ax[1].set_xlabel("c1")
    ax[1].set_ylabel("c2")
    plt.show()


def var(x):  # return la variance d un vecteur
    x_bar = np.mean(x)
    n = len(x)
    s = 0
    for i in range(n):
        s += x[i] ** 2
    s -= x_bar ** 2
    return s / n


# def affichage(c1, c2, w1, w2):
# fig, ax = plt.subplots(nrows=1, ncols=2)
# ax[0].scatter(c1, c2, marker='o', color='blue', )
# ax[0].scatter(w1, w2, marker='o', color='red', )

# plt.show()

# def corre_compo(vals, vects):
#     cor = []
#     for i in range(2):
#         cor.append([0]* len(vals))
#         b = sqrt(vals[i])
#         for j in range(len(vals)):
#             c = vects[i][j] # u[i][j]
#             val = b * c
#             cor[i][j] = val
#     return cor

# def coef_corr(x,y):
#     a = cov(x,y)
#     b = sqrt(cov(x,x))
#     c = sqrt(cov(y,y))
#     return (a / (b*c))
