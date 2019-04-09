# -*- coding: utf-8 -*-

### selection les informations utiles de la tramme GPS recu en bytes ###
### renvoi date heure long lat route vitesse                         ###

def decode_frame_GPS(var1):
    h = var1.split(",")
    try :
        if h[3] == "" :
            h[3] = "NaN"
    except IndexError :
        print("Erreur trames GPS : longitude")
        
    try :
        if h[5] == "" :
            h[5] = "NaN"
    except IndexError :
        print("Erreur trames GPS : latitude")
        
    try :
        if h[8] == "" :
            h[8] = "NaN"
    except IndexError :
        print("Erreur trames GPS : cap")
        
    try :
        if h[7] == "" :
            h[7] = "NaN"
    except IndexError :
        print("Erreur trames GPS : date")
        
    u = h[9][0:2] + "/" + h[9][2:4] + "/" + h[9][4:6] + "    " + h[1][0:2] + ":" + h[1][2:4] + ":" + h[1][4:6] + "     " + h[3] + "      " + h[5] + "     " + h[8] + "     " + h[7] + "    "
    return u
