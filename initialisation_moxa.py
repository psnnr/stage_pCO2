# -*- coding: utf-8 -*-

def initialisation_moxa():
    
    port1 = "COM16"  # selectionner le port utilise
    port2 = "COM15"
    port3 = "COM13"
    port4 = "COM2"
    port5 = "COM12"
    
    ser_GPS = serial.Serial(port1,
    baudrate=4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

    ser_temp = serial.Serial(port2,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)
    
    ser_ox = serial.Serial(port3,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)
    
    ser_mio = serial.Serial(port4,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)
    
    ser_licor = serial.Serial(port5,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)
    
    config_oxy(ser_ox)
    
    return ser_GPS, ser_temp, ser_ox, ser_mio, ser_licor

