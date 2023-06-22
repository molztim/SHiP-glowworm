# Bibliotheken laden
import machine
import network 
import utime as time
import binascii
import ubinascii

from eMUSIC_registers import *

from machine import SPI, Pin

CSN = 17
cs = Pin(CSN, mode=Pin.OUT, value=1)
spi = SPI(0, baudrate=1000000, polarity=0, phase=1,bits=8,firstbit=SPI.MSB,sck=Pin(18),mosi=Pin(19),miso=Pin(16)) #Mode 1 connection #1000000

def spi_write(spi, cs, reg,data):
    msg = bytearray()
    msg.append(reg)
    msg+=data
    try:
        cs.value(0)
        spi.write(msg)
        cs.value(1)
    except:
        print("Error 21: Error in writing via SPI. Check comm.")
    
def spi_read(spi,cs,reg,nbytes=2):           
    msg = bytearray()
    msg.append(reg+128)
    try:
        
        cs.value(0)
        spi.write(msg)
        data = spi.read(nbytes)
        cs.value(1)
        
        return data
    
    except Exception as e:
        print("Error 20: Could not read data ia SPI. Check SPI!")
        print("{0} : {1}".format(type(ex).__name__, ex.args))
        return None
    
def write_eMUSIC(data,registername,channel=0, debug=False):
    register = eMUSIC_register[registername][0][channel]
    bits = eMUSIC_register[registername][1]
    
    if debug:
        print("WRITE COMMAND")
        print("Reigster to be called:",register,", Position(s) in return:",bits)
        bit_data = ' '.join(f'{x:08b}' for x in data)
        print(f"Outgoing Data: {data} {bit_data}\n")
    
    spi_write(spi,cs,register,data)
    return None


def read_eMUSIC(registername, channel = 0, debug=False):
    data = None
    register = eMUSIC_register[registername][0][channel]
    bits = eMUSIC_register[registername][1]
    
    data = spi_read(spi,cs,register)
    
    if debug:
        print("READ COMMAND")
        print("Register to be called:",register,", Position(s) in return:",bits)
        bit_data = ' '.join(f'{x:08b}' for x in data)
        print(f"Read Data: {data} {bit_data}\n")
    return data

def read_config(debug=False):
    read_config = []
    channel = 0
    for key in CONFIG_KEY_LIST:
        if key == "FASTOR": continue
        data = read_eMUSIC(key, channel = channel,debug = debug)
        pos = eMUSIC_register[key][1]        
        bit_data = ''.join(f'{x:08b}' for x in data)
        bits = ''.join([bit_data[i] for i in pos])
        read_config.append(int(bits,2))
        if key == "PENZPZCOMP":
            channel +=1

    return read_config

def write_config(file,debug=False):
    data = ['0'*16]*(39)
    #leave registers 16-31 empty

    file_dict = {}
    for i in range(0,len(CONFIG_KEY_LIST)):
        if CONFIG_KEY_LIST[i] in file_dict.keys():
           file_dict[CONFIG_KEY_LIST[i]].append(EMUSIC_CONFIG[i]) 
        else:
            file_dict[CONFIG_KEY_LIST[i]] = [EMUSIC_CONFIG[i]]

    #These guys dont appear in the config file. I therefore set them manually    
    file_dict["ENPZLG"] = [1]
    file_dict["ENBYPASSLG"] = [0]
    file_dict["ENDIFFDRVLG"] = [1]
    file_dict["HLSUMLG"] = [1]

    for key,registerlist in eMUSIC_register.items():
        valuelist = file_dict[key]
        #print(f"{key} : {registerlist[0]} {registerlist[1]} {valuelist}")
        for i in range(len(valuelist)):
            value = valuelist[i]
            register = registerlist[0][i]
            positions = registerlist[1]
            bitcount = len(registerlist[1])
            bits = f'{value:016b}'[-bitcount:]
            data[register] = data[register][:positions[0]] + bits + data[register][positions[-1]+1:]
    
    for i in range(0,len(data)):
        if int(data[i],2) == 0: continue
        else:
            spi_write(spi,cs,i,data[i])
    return None
        

#data = b'\x04\xff'
reginame = 'ENCH'
#write_eMUSIC(data,reginame, debug=True)
read_eMUSIC(reginame, debug=True)

#write_config(EMUSIC_CONFIG)
#configile = read_config()
#print(configile)

#print(EMUSIC_CONFIG)
#print(EMUSIC_CONFIG == configile)

#for i in ["ENPZLG", "ENBYPASSLG", "ENDIFFDRVLG",  "HLSUMLG"]:
#    data = read_eMUSIC(i)
#    bit_data = ''.join(f'{x:08b}' for x in data)
#    pos = eMUSIC_register[i][1][0]
#    print(i,bit_data[pos])


