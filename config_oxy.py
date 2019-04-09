# -*- coding: utf-8 -*-

def config_oxy(var1):
    
    u = bytes("Set_Protect(1)\n",'utf-8')
    var1.write(u)
    print("attente rep optode set_protect")
    a = var1.readline()
    print("rep optode set_protect :")
    try :
        print(a.decode())
    except UnicodeDecodeError :
        print("'utf-8' codec can't decode byte 0xe9 in position 1: invalid continuation byte")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Attention initialisation echouée : veillez redemarer le programme !!!!!!!!!!!!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    u = bytes("Set_Interval(5)\n",'utf-8')
    var1.write(u)
    print("attente rep optode set_Interval")
    a = var1.readline()
    print("rep optode Set_intalval :")
    try :
        print(a.decode())
    except UnicodeDecodeError :
        print("'utf-8' codec can't decode byte 0xe9 in position 1: invalid continuation byte")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Attention initialisation echouée : veillez redemarer le programme !!!!!!!!!!!!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    u = bytes("Save\n",'utf-8')
    var1.write(u)
    print("attente rep optode Save")
    a = var1.readline()
    print("rep optode Save :")
    try :
        print(a.decode())
    except UnicodeDecodeError :
        print("'utf-8' codec can't decode byte 0xe9 in position 1: invalid continuation byte")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Attention initialisation echouée : veillez redemarer le programme !!!!!!!!!!!!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    u = bytes("Load\n",'utf-8')
    var1.write(u)
    print("attente rep optode Load")
    a = var1.readline()
    print("rep optode Load") 
    try :
        print(a.decode())
    except UnicodeDecodeError :
        print("'utf-8' codec can't decode byte 0xe9 in position 1: invalid continuation byte")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Attention initialisation echouée : veillez redemarer le programme !!!!!!!!!!!!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    u = bytes("Get_All\n",'utf-8')
    var1.write(u)
    print("Parametres de l'optode :")
    
    for i in range(21):
        a = var1.readline()
        try :
            b = a.decode()
        except UnicodeDecodeError :
            print("'utf-8' codec can't decode byte 0xe9 in position 1: invalid continuation byte")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Attention : erreur dans l'affichage des paramêtres de l'optode, aucune idée des conséquences")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(b)