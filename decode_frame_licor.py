# -*- coding: utf-8 -*-

### 

#def decode_frame_licor(var1):
#    w = var1.split("\t")
#    if len(w) >= 5:
#        u = w[1] + "    " + w[2] + "    " + w[3] + "    " + w[4][0:6] + "    "
#    else:
#        u = "NaN" + "    " + "NaN" + "    " + "NaN" + "    " + "NaN" + "    "
#    return u

def decode_frame_licor(var1):
    w = var1.split("\t")
    if len(w) >= 5:
        w[4]=w[4][0:6]
        try:
            tanpon = float(w[1])
        except ValueError :
            w[1] = "NaN"
        try:
            tanpon = float(w[2])
        except ValueError :
            w[2] = "NaN"
        try:
            tanpon = float(w[3])
        except ValueError :
            w[3] = "NaN"
        try:
            tanpon = float(w[4])
        except ValueError :
            w[4] = "NaN"
            
        u = w[1] + "    " + w[2] + "    " + w[3] + "    " + w[4][0:6] + "    "
    else:
        u = "NaN" + "    " + "NaN" + "    " + "NaN" + "    " + "NaN" + "    "
    return u

