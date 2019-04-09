# -*- coding: utf-8 -*-

######################## AD0 : 425 , AD1 : 435 ###############################

#def conv_capt_pression(var1,var2,var3) :
#    i = int(var1,16)
#    n = ((i/1023) * var2) + var3
#    return n

def conv_capt_pression(var1,var2,var3) :
    try:
        i = int(var1,16)
        n = ((i/1023) * var2) + var3
    except ValueError :
        n = "NaN"
    return n

