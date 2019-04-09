# -*- coding: utf-8 -*-

def evac_piege_froid(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor):
    ac = time.time()
    f = ac + 6
    print("evacuation du piege a froid")
    vanne = bytes("BD0402\n\r",'utf-8') #commande ouverture vanne 1,2 et 7
    #ser_mio.write(vanne) #envoi commande
    while ac <= f :
        ac = time.time()
        send_lecture_seule(ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor)
    print("evacuation terminé")
    vanne = bytes("BD0100\n\r",'utf-8') #commande ouverture vanne 1,2 et 7
    #ser_mio.write(vanne)
    return 0
    