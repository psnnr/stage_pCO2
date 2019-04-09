# -*- coding: utf-8 -*-

def fichier_moyennage(fichier_lecture):
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    m8 = 0
    m9 = 0
    
    cpt_m1 = 0
    cpt_m2 = 0
    cpt_m3 = 0
    cpt_m4 = 0
    cpt_m5 = 0
    cpt_m6 = 0
    cpt_m7 = 0
    cpt_m8 = 0
    cpt_m9 = 0
    
    cpt = 0
    read_data = fichier_lecture.readline()
    
    if read_data[0] == 'c' :
        read_data = fichier_lecture.readline()
    
    if read_data == '':
        print("Erreur : lecture du fichier brut impossible")
        
    if read_data[0] == 'c' :
        read_data = fichier_lecture.readline()

    while(read_data):
        V = read_data.split()
        if len(V) <= 15 :
            V[7] = V[8] = V[9] = V[10] = V[11] = V[12] = V[13] = V[14] = V[15] = "NaN"
            
        if ((V[7] == '') | (V[7] == "NaN")):
            V[7] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m1 = m1 + float(V[7])
        except ValueError:
            cpt_m1 = cpt_m1 + 1
       
        if ((V[8] == '') | (V[8] == "NaN")):
            V[8] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m2 = m2 + float(V[8])
        except ValueError :
            cpt_m2 = cpt_m2 + 1
        
        if ((V[9] == '') | (V[9] == "NaN")):
            V[9] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m3 = m3 + float(V[9])
        except ValueError :
            cpt_m3 = cpt_m3 + 1            
            
        if ((V[10] == '') | (V[10] == "NaN")):
            V[10] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m4 = m4 + float(V[10])
        except ValueError :
            cpt_m4 = cpt_m4 + 1
            
        if ((V[11] == '') | (V[11] == "NaN")):
            V[11] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m5 = m5 + float(V[11])
        except ValueError :
            cpt_m5 = cpt_m5 + 1
            
        if ((V[12] == '') | (V[12] == "NaN")):
            V[12] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m6 = m6 + float(V[12])
        except ValueError :
            cpt_m6 = cpt_m6 + 1
            
        if ((V[13] == '') | (V[13] == "NaN")):
            V[13] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m7 = m7 + float(V[13])
        except ValueError :
            cpt_m7 = cpt_m7 + 1
            
        if ((V[14] == '') | (V[14] == "NaN")):
            V[14] = 0
            cpt_m8 = cpt_m8 + 1
        try:
            m8 = m8 + float(V[14])
        except ValueError :
            cpt_m8 = cpt_m8 + 1
            
        if ((V[15] == '') | (V[15] == "NaN")):
            V[15] = 0
            cpt_m1 = cpt_m1 + 1
        try:
            m9 = m9 + float(V[7])
        except ValueError:
            cpt_m9 = cpt_m9 + 1
        
        cpt = cpt + 1
        read_data = fichier_lecture.readline()
    
    if cpt > cpt_m1 :
        m1 = m1/(cpt - cpt_m1)
    else:
        m1 = "NaN"
        
    if cpt > cpt_m2 :
        m2 = m2/(cpt - cpt_m2)
    else:
        m2 = "NaN"
    
    if cpt > cpt_m3 :
        m3 = m3/(cpt - cpt_m3)
    else:
        m3 = "NaN"
    
    if cpt > cpt_m4 :
        m4 = m4/(cpt - cpt_m4)
    else:
        m4 = "NaN"
    
    if cpt > cpt_m5 :
        m5 = m5/(cpt - cpt_m5)
    else:
        m5 = "NaN"
        
    if cpt > cpt_m6 :
        m6 = m6/(cpt - cpt_m6)
    else:
        m6 = "NaN"
        
    if cpt > cpt_m7 :
        m7 = m7/(cpt - cpt_m7)
    else:
        m7 = "NaN"
        
    if cpt > cpt_m8 :
        m8 = m8/(cpt - cpt_m8)
    else:
        m8 = "NaN"
        
    if cpt > cpt_m9 :
        m9 = m9/(cpt - cpt_m9)
    else:
        m9 = "NaN"
    
    fich = open("data/DataMoyenne.txt","a")
    fich.write(V[0])
    fich.write("        ")
    fich.write(V[1])
    fich.write("    ")
    fich.write(V[2])
    fich.write("    ")
    fich.write(V[3])
    fich.write("    ")
    fich.write(V[4])
    fich.write("    ")
    fich.write(V[5])
    fich.write("    ")
    fich.write(V[6])
    fich.write("    ")
    fich.write(str(m1))
    fich.write("    ")
    fich.write(str(m2))
    fich.write("    ")
    fich.write(str(m3))
    fich.write("    ")
    fich.write(str(m4))
    fich.write("    ")
    fich.write(str(m5))
    fich.write("    ")
    fich.write(str(m6))
    fich.write("    ")
    fich.write(str(m7))
    fich.write("    ")
    fich.write(str(m8))
    fich.write("    ")
    fich.write(str(m9))
    fich.write("\n")
    
    fich.close()
    
    return 0