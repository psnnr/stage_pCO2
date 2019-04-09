# -*- coding: utf-8 -*-

def nouv_fichier(fichier_lecture,fichier_ecriture):
    
    mj = get_jour()
    mm = get_mois()
    name = "data/Data_Brut_" + str(mj) + "-" + str(mm) + ".txt"
    fichier_ecriture = open(name,"a")
    fichier_lecture = open(name,"r")
    fichier_ecriture.write("cycle     date       heure      longitude      latitude    route    vitesse  temp_sbe38       pression_eq         pression_atm           Licor_CO2 Licor_H20  Licor_p    Licor_t      optode_O2  optode_temp \n")
    
    return fichier_lecture,fichier_ecriture

