# -*- coding: utf-8 -*-

def nouv_fichier_ecriture(fichier_ecriture):
    mj = get_jour()
    mm = get_mois()
    name = "data/Data_Brut_" + str(mj) + "-" + str(mm) + ".txt"
    fichier_ecriture = open(name,"a")
    
    return fichier_ecriture