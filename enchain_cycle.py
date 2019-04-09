# -*- coding: utf-8 -*-

def enchain_cycle(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor, fichier_lecture, fichier_ecriture,var,temps_rinc_etal_bas,temps_rinc_etal_haut, temps_rinc_etal_med, temps_rinc_azote, temps_rinc_air, temps_rinc_eau, temps_mesure_etal_bas, temps_mesure_etal_haut, temps_mesure_etal_med, temps_mesure_azote, temps_mesure_air, temps_mesure_eau,monjour,monmois):
    
    valeur_graph_pression_1 = []
    valeur_graph_pression_2 = []
    valeur_graph_pco2 = []
    valeur_graph_o2 = []
    valeur_graph_temp_sbe38 = []
    valeur_graph_temp_opt = []
    valeur_graph_temp_li = []
    
    
    if var == 1:
        while 1 :
            fichier_lecture, fichier_ecriture,monjour,monmois, valeur_graph_pression_1, valeur_graph_pression_2, valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = azote(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_azote,temps_mesure_azote, monjour, monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li)
            fichier_lecture, fichier_ecriture,monjour,monmois, valeur_graph_pression_1, valeur_graph_pression_2, valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = etal_bas(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_bas,temps_mesure_etal_bas,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li)
            fichier_lecture, fichier_ecriture,monjour,monmois, valeur_graph_pression_1, valeur_graph_pression_2, valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = etal_haut(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_haut,temps_mesure_etal_haut,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li)
            fichier_lecture, fichier_ecriture,monjour,monmois, valeur_graph_pression_1, valeur_graph_pression_2, valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li)
            fichier_lecture, fichier_ecriture,monjour,monmois, valeur_graph_pression_1, valeur_graph_pression_2, valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = air_atm(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_air,temps_mesure_air,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li)
            fichier_lecture, fichier_ecriture,monjour,monmois, valeur_graph_pression_1, valeur_graph_pression_2, valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture,fichier_ecriture,temps_rinc_eau,temps_mesure_eau,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li)  
            
    elif var == 2:
        while 1 :
            
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_bas(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_bas,temps_mesure_etal_bas,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_haut(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_haut,temps_mesure_etal_haut,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = air_atm(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_air,temps_mesure_air,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture,fichier_ecriture,temps_rinc_eau,temps_mesure_eau,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = azote(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_azote,temps_mesure_azote, monjour, monmois)
    
    elif var == 3:
        while 1 :
            
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_haut(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_haut,temps_mesure_etal_haut,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = air_atm(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_air,temps_mesure_air,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture,fichier_ecriture,temps_rinc_eau,temps_mesure_eau,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = azote(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_azote,temps_mesure_azote, monjour, monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_bas(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_bas,temps_mesure_etal_bas,monjour,monmois)
            
    elif var == 4:
        while 1 :        
            
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = air_atm(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_air,temps_mesure_air,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture,fichier_ecriture,temps_rinc_eau,temps_mesure_eau,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = azote(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_azote,temps_mesure_azote, monjour, monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_bas(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_bas,temps_mesure_etal_bas,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_haut(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_haut,temps_mesure_etal_haut,monjour,monmois)
            
            
    elif var == 5:
        while 1 :        
            
            fichier_lecture, fichier_ecriture,monjour,monmois = air_atm(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_air,temps_mesure_air,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture,fichier_ecriture,temps_rinc_eau,temps_mesure_eau,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = azote(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_azote,temps_mesure_azote, monjour, monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_bas(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_bas,temps_mesure_etal_bas,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_haut(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_haut,temps_mesure_etal_haut,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois)
    elif var == 6:
        while 1 :        
            
            fichier_lecture, fichier_ecriture,monjour,monmois = eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture,fichier_ecriture,temps_rinc_eau,temps_mesure_eau,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = azote(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_azote,temps_mesure_azote, monjour, monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_bas(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_bas,temps_mesure_etal_bas,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_haut(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_haut,temps_mesure_etal_haut,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = etal_moy(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_etal_med,temps_mesure_etal_med,monjour,monmois)
            fichier_lecture, fichier_ecriture,monjour,monmois = air_atm(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor,fichier_lecture, fichier_ecriture,temps_rinc_air,temps_mesure_air,monjour,monmois)
            