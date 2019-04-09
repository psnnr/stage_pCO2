# -*- coding: utf-8 -*-

def get_mois():
    
    now = time.localtime(time.time()) #retourne lheure avec date et annee
    return now[1]