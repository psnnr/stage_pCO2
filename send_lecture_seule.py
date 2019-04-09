# -*- coding: utf-8 -*-

### lit les capteurs mais n'ecris rien dans le fichier et le terminal ###
def send_lecture_seule(ser, ser_temp, ser_ox, ser_mio, ser_licor) :
        
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
        
        b = bytes("AD1\n\r",'utf-8')
        ser_mio.write(b)
        dataP2 = ser_mio.readline()
        data_P2 = conv_capt_pression(dataP2[6:9],435,900)

        data_GPS = decode_frame_GPS(data_GPS)
        data_licor = decode_frame_licor(data_licor)

        return 0