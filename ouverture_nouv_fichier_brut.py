# -*- coding: utf-8 -*-

def ouverture_nouv_fichier_brut(fichier_lecture,fichier_ecriture,monjour,monmois):
    mj = get_jour()
    mm = get_mois()
        
    if(monjour == mj):
        fichier_ecriture = nouv_fichier_ecriture(fichier_ecriture)
    else:
        fichier_lecture.close()
        fichier_ecriture.close()
        monjour = mj
        monmois = mm
        name = "data/Data_Brut_" + str(mj) + "-" + str(mm) + ".txt"
        fichier_ecriture = open(name,"a")
        fichier_lecture = open(name,"r")
        fichier_ecriture.write("cycle     date       heure      longitude      latitude    route    vitesse  temp_sbe38       pression_eq         pression_atm           Licor_CO2 Licor_H20  Licor_p    Licor_t      optode_O2  optode_temp \n")
        fichier_lecture.readline()
        
    return fichier_lecture,fichier_ecriture,monjour,monmois