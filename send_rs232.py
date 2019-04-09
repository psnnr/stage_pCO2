# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:19:27 2018

@author: Paul
"""


def send_rs232(type_cycle, ser, ser_temp, ser_ox, ser_mio, ser_licor, fichier, valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li) :
    
    
        
    while True :
        for i in range(900):
            line = str(ser.readline())
            data = line.split(",")
            if line.split(",")[0] == "b'$GPRMC":
                data_GPS = line
                break
        
        datatemp = ser_temp.readline()
        data_temp = datatemp.decode()
        
        for i in range(300):
            line = ser_ox.readline()
            data = line.decode()
            if len(data) > 4 :
                if (line[3] == 69) | (line[3] == 17) :
                    data_ox = data
                    break
            
        dlicor = ser_licor.readline()
        data_licor = dlicor.decode()
        
        b = bytes("AD0\n\r",'utf-8')
        ser_mio.write(b)
        dataP1 = ser_mio.readline()
        data_P1 = conv_capt_pression(dataP1[6:9],425,900)
        if len(valeur_graph_pression_1) >= 250 :
            valeur_graph_pression_1 = valeur_graph_pression_1[1:]
        valeur_graph_pression_1.append(data_P1)
    
        
        b = bytes("AD1\n\r",'utf-8')
        ser_mio.write(b)
        dataP2 = ser_mio.readline()
        data_P2 = conv_capt_pression(dataP2[6:9],435,900)
        if len(valeur_graph_pression_2) >= 250 :
            valeur_graph_pression_2 = valeur_graph_pression_2[1:]
        valeur_graph_pression_2.append(data_P2)
              
        data_GPS = decode_frame_GPS(data_GPS)
        data_licor = decode_frame_licor(data_licor)
        data_ox = decode_frame_ox(data_ox)
        data_temp = decode_frame_temp(data_temp)
        
        if len(valeur_graph_temp_sbe38) >= 250 :
            valeur_graph_temp_sbe38 = valeur_graph_temp_sbe38[1:]
        valeur_graph_temp_sbe38.append(data_temp)
        
        if len(valeur_graph_temp_opt) >= 250 :
            valeur_graph_temp_opt = valeur_graph_temp_opt[1:]
        valeur_graph_temp_opt.append(data_ox.split()[1])
        
        if len(valeur_graph_o2) >= 250 :
            valeur_graph_o2 = valeur_graph_o2[1:]
        valeur_graph_o2.append(data_ox.split()[0])
        
        if len(valeur_graph_temp_li) >= 250 :
            valeur_graph_temp_li = valeur_graph_temp_li[1:]
        valeur_graph_temp_li.append(data_licor.split()[1])
        
        if len(valeur_graph_pco2) >= 250 :
            valeur_graph_pco2 = valeur_graph_pco2[1:]
        valeur_graph_pco2.append(data_licor.split()[0])
                
        ecriture(type_cycle, data_GPS, data_temp, data_P1, data_P2, data_licor, data_ox, fichier)
        
        #fig = plt.subplot(2,2,1)
        fig = plt.plot(valeur_graph_pression_1, label='AD0')
        fig = plt.plot(valeur_graph_pression_2, label = 'AD1')
        fig = plt.title('Pression AD0 et AD1')
        fig = plt.ylabel("hPa")
        fig = plt.show()
        
        #fig = plt.subplot(2,2,2)
        fig = plt.plot(valeur_graph_pco2)
        fig = plt.title('Taux de CO2')
        fig = plt.ylabel("ppm")
        fig = plt.show()
        
        #fig = plt.subplot(2,2,3)
        fig = plt.plot(valeur_graph_o2)
        fig = plt.title('Taux de O2')
        fig = plt.ylabel("??")
        fig = plt.show()
        
        #fig = plt.subplot(2,2,4)
        fig = plt.plot(valeur_graph_temp_li, label='licor')
        fig = plt.plot(valeur_graph_temp_opt, label='opt')
        fig = plt.plot(valeur_graph_temp_sbe38, label='SBE38')
        fig = plt.title('temp')
        fig = plt.ylabel("C")
        fig = plt.show()
        
        return valeur_graph_pression_1, valeur_graph_pression_2,valeur_graph_pco2, valeur_graph_o2, valeur_graph_temp_sbe38, valeur_graph_temp_opt, valeur_graph_temp_li