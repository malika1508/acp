#from cleaning import *
from functions import *

def main(path, norme):
    data = pd.read_csv(path)# inputs
    #data = pd.read_csv(url, sep = ";") 
    #data = clean(data) # pretraitemnt des donnees

    n = data.shape[0]

    Y = centre(data,n) # centrer la matrice

    Z = centre_reduite(Y, n) # centrer et reduire la matrice

    V = var_covar(Y, n) # matrice de variance /covariance

    R = corr(Z, n) # matrice de correlation
#====================ACP NORME =======================
    if norme:
        vals, vects = diago(R) # diagonalisation
        #interpretation(vals, vects)
        c1, c2,  w1, w2 = compo_prin(Z, vals.round(3), vects) # les projections individus et des variables sur les axes factoriels 
        cor = corr_compo(Z, vals, vects)# la correlation entre les anciennes et nouvelle variables
        afficher(c1, c2, w1, w2, cor, "ACP NORMÉE") # affichage du graphe
#====================ACP NON NORME =======================
    else:
        vals, vects = diago(V) # diagonalisation
        interpretation(vals, vects)

        c1, c2,  w1, w2 = compo_prin(Y, vals.round(3), vects) # les projections individus et des variables sur les axes factoriels 
        
        cor= corr_compo(Y, vals, vects)# la correlation entre les anciennes et nouvelle variables

        #afficher(c1, c2, w1, w2, cor, "ACP NON NORMÉE") # affichage du graphe
