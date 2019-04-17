# -*- coding: utf-8 -*-

def close():

    ### ferme les ports series utilise par les appareils peripherique de la manip
    
    ser.close()    #gps
    ser_temp.close()    #sbe38
    ser_ox.close()  #optode
    ser_mio.close() #miocard
    ser_licor.close()   #Licor

### execution de la procedure
 
close()