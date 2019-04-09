# -*- coding: utf-8 -*-

def eau_mers(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor, fichier_lecture,fichier_ecriture, temps_rinc_eau,temps_mesure_eau,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li) :
    print("Eau de mers")
    type_cycle = 6
    
    debut = time.time()
    actu = debut
    rin = debut +  temps_rinc_eau #10 min rincage
    fin = debut +  temps_rinc_eau + temps_mesure_eau  #300 min mesure
    tevac = actu + (30*60)
    tmoy = actu + temps_rinc_eau + 5*60
    
    vanne = bytes("BD0100\n\r",'utf-8') #commande ouverture de la pompe
    ser_mio.write(vanne) #envoi commande
    print("début du rincage")
    while rin >= actu :
        actu = time.time()
        send_lecture_seule(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor)
    print("fin du rincage, début des mesures")
    while fin >= actu:
        actu = time.time()
        if actu >= tevac :
            evac_piege_froid(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor)
            actu = time.time()
            tevac = actu + 30*60
        valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li = send_rs232(type_cycle, ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor, fichier_ecriture,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li) #acauisition
        if(actu >= tmoy):
            fichier_ecriture.close()
            fichier_moyennage(fichier_lecture)
            fichier_lecture,fichier_ecriture,monjour,monmois = ouverture_nouv_fichier_brut(fichier_lecture,fichier_ecriture,monjour,monmois)
            actu = time.time()
            tmoy = actu + 5*60
        
    print("fin des mesures")
    vanne = bytes("BD0000\n\r",'utf-8') #commandnde fermeture pompe
    ser_mio.write(vanne) #envoi commande
    
    return fichier_lecture, fichier_ecriture,monjour,monmois,valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li