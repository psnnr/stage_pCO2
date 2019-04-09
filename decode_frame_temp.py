# -*- coding: utf-8 -*-

def decode_frame_temp(var1) :
    try:
        wr1 = str(var1)
    except ValueError:
        wr1 = "NaN  "
    return wr1[0:5]

#def decode_frame_temp(var1) :
#    wr1 = str(var1)
#    return wr1[0:5]