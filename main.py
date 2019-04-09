# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:12:40 2018

@author: Nathalie
"""

import serial
import time
import string
import matplotlib.pyplot as plt

#import pyqtgraph as pg
#import matplotlib.animation as animation

### execution des sous programmes ###

def main() :
    
    monjour = get_jour()
    monmois = get_mois()
    
    ### temps de rincages des cycles en secondes
    
    temps_rinc_etal_bas = 3*60
    temps_rinc_etal_haut = 3*60
    temps_rinc_etal_med = 3*60
    temps_rinc_azote = 3*60
    temps_rinc_air = 4*60
    temps_rinc_eau = 10*60
    
    ### temps de mesure des cycles en secondes
    
    temps_mesure_etal_bas = 3*60
    temps_mesure_etal_haut = 3*60
    temps_mesure_etal_med = 3*60
    temps_mesure_azote = 3*60
    temps_mesure_air = 3*60
    temps_mesure_eau = 300*60

    sortir = 0 # sortir de l'execution du programme
    fichier_lecture = fichier_ecriture = 0
    fichier_lecture,fichier_ecriture = nouv_fichier(fichier_lecture,fichier_ecriture)
    init_lecture_fichier_brut(fichier_lecture)
    fich = open("data/DataMoyenne.txt","a")
    fich.write("cycle       date       heure    longitude   latitude    route   vitesse    temp_sbe38                pression_equi           pression_atm       Licor_CO2          Licor_H2O           licor_P			Licor_temp         optode_O2             optode_T   \n")
    fich.close()

    ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor = initialisation_moxa() #initialisation des communications RS232 avec les capteurs et GPS
    
    while (sortir == 0) :
        
        print("choisir premier cycle :")
        print("0 - quitter le systeme")
        print("1 - azote")
        print("2 - etal bas")
        print("3 - etal haut")
        print("4 - etal moy")
        print("5 - air atmosphérique")
        print("6 - eau de mers")
        
        choix = input("entrer votre choix (0,1,2,3,4,5 ou 6)")
    
        if(choix == '0' or choix == '1' or choix == '2' or choix == '3' or choix == '4' or choix == '5' or choix == '6') :
            choix_int = int(choix)
            print("votre choix est :", choix_int)
            
            if choix_int == 0 :
                sortir = 1
                print("fin du programme")
                print("-----------------------------------------")
                print
                return 0
            else : 
                enchain_cycle(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor, fichier_lecture, fichier_ecriture,choix_int,temps_rinc_etal_bas,temps_rinc_etal_haut, temps_rinc_etal_med, temps_rinc_azote, temps_rinc_air, temps_rinc_eau, temps_mesure_etal_bas, temps_mesure_etal_haut, temps_mesure_etal_med, temps_mesure_azote, temps_mesure_air, temps_mesure_eau,monjour,monmois)

        else :
                print("entree incorrecte : veillez recommencer")
                print("------------------------------------")
                print
                

main()