# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:11:15 2018

@author: Nathalie
"""

def etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor, fichier_lecture,fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li) :
    print("fonction etal moy")
    type_cycle = 4

    debut = time.time()
    actu = debut
    rin = debut + temps_rinc_etal_med # 3 min rincage
    fin = debut + temps_rinc_etal_med + temps_mesure_etal_med # 3 min mesure
    
    vanne = bytes("BD8600\n\r",'utf-8') #commande ouverture vanne 1,2 et 7
    ser_mio.write(vanne) #envoi commande
    print("début du rincage")
    while rin >= actu :
        actu = time.time()
        send_lecture_seule(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor)
    print("fin du rincage, début des mesures")
    while fin >= actu:
        actu = time.time()
        valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = send_rs232(type_cycle, ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor, fichier_ecriture,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li) #acauisition
    print("fin des mesures")
    vanne = bytes("BD0000\n\r",'utf-8') #commande fermeture vanne 1, 2 et 7
    ser_mio.write(vanne) #envoi commande
    
    fichier_ecriture.close()
    fichier_moyennage(fichier_lecture)
    fichier_lecture,fichier_ecriture,monjour,monmois = ouverture_nouv_fichier_brut(fichier_lecture,fichier_ecriture,monjour,monmois)
    
    return fichier_lecture, fichier_ecriture,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li