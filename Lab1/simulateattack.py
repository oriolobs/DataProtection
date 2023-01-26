# python.v1 program for RC4 key and message decryption - Oriol & Sofia

from platform import java_ver
from re import M
from timeit import repeat

def most_frequent(List):
    return max(set(List), key = List.count)

def readtext(filetoread):                                       # function read text and fill variables
    global mylines
    global myivs
    mylines = []
    myivs = []
    with open (filetoread, 'rt') as myfile:                     # open file selected before for reading text       
        for myline in myfile:
            myivs.append(myline.strip('\n').split(" ")[0])          
            mylines.append(myline.strip('\n').split(" ")[1])    # get the 2nd valor of the column

def XOR_M():
    readtext("bytes_01FFxx.dat")
    global myxor_m
    global m
    myxor_m = []
    i = 0
    while i < 256:
        y = int(mylines[i].split("X")[1], 16)                   # convert hex to int with or without 0x
        if i == 254:                                            # 255 + 2 = 0
            z = 0
        if i == 255:                                            # 256 + 2 = 1
            z = 1
        else:
            z = int(myivs[i].split("01FF")[1], 16) + 2
        myxor_m.append(y^z)
        i = i + 1
    m = most_frequent(myxor_m) 

XOR_M()

def XOR_K0():
    readtext("bytes_03FFxx.dat")
    global k
    k = []
    myxor_k0 = []
    i = 0
    while i < 256:
        y = int(mylines[i].split("X")[1], 16)                   # convert hex to int with or without 0x
        z = int(myivs[i].split("03FF")[1], 16)
        myxor_k0.append(((y^m)-z-6)%256)
        i = i + 1
    k.append(myxor_k0)

XOR_K0()

k0 = most_frequent(k[0])

def XOR_KX(num, o):
    if num == 10:
        num = 'A'
    if num == 11:
        num = 'B'
    if num == 12:
        num = 'C'
    if num == 13:
        num = 'D'
    if num == 14:
        num = 'E'
    if num == 15:
        num = 'F'
    readtext("bytes_0{}FFxx.dat".format(num))
    myxor_kx = []
    i = 0
    
    while i < 256:
        y = int(mylines[i].split("X")[1], 16)                   # convert hex to int with or without 0x
        z = int(myivs[i].split("0{}FF".format(num))[1], 16)
        if o == 0:
            myxor_kx.append(((y^m)-z-10-k0)%256)
        if o == 1:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5)-k0-k1)%256)
        if o == 2:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6)-k0-k1-k2)%256)
        if o == 3:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7)-k0-k1-k2-k3)%256)
        if o == 4:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8)-k0-k1-k2-k3-k4)%256)
        if o == 5:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9)-k0-k1-k2-k3-k4-k5)%256)
        if o == 6:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9+10)-k0-k1-k2-k3-k4-k5-k6)%256)
        if o == 7:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9+10+11)-k0-k1-k2-k3-k4-k5-k6-k7)%256)
        if o == 8:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9+10+11+12)-k0-k1-k2-k3-k4-k5-k6-k7-k8)%256)
        if o == 9:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9+10+11+12+13)-k0-k1-k2-k3-k4-k5-k6-k7-k8-k9)%256)
        if o == 10:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9+10+11+12+13+14)-k0-k1-k2-k3-k4-k5-k6-k7-k8-k9-k10)%256)
        if o == 11:
            myxor_kx.append(((y^m)-z-(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15)-k0-k1-k2-k3-k4-k5-k6-k7-k8-k9-k10-k11)%256)

        i = i + 1
    k.append(myxor_kx)

filenum = 4
ifile = 0

while filenum < 16:
    XOR_KX(filenum, ifile)
    filenum = filenum +1
    ifile = ifile +1
    if ifile == 1:
        k1 = most_frequent(k[1])
    if ifile == 2:
        k2 = most_frequent(k[2])
    if ifile == 3:
        k3 = most_frequent(k[3])
    if ifile == 4:
        k4 = most_frequent(k[4])
    if ifile == 5:
        k5 = most_frequent(k[5])
    if ifile == 6:
        k6 = most_frequent(k[6])
    if ifile == 7:
        k7 = most_frequent(k[7])
    if ifile == 8:
        k8 = most_frequent(k[8])
    if ifile == 9:
        k9 = most_frequent(k[9])
    if ifile == 10:
        k10 = most_frequent(k[10])
    if ifile == 11:
        k11 = most_frequent(k[11])
    if ifile == 12:
        k12 = most_frequent(k[12])

message = hex(most_frequent(myxor_m))[2:].zfill(2)
key0 = hex(most_frequent(k[0]))[2:].zfill(2)
key1 = hex(most_frequent(k[1]))[2:].zfill(2)
key2 = hex(most_frequent(k[2]))[2:].zfill(2)
key3 = hex(most_frequent(k[3]))[2:].zfill(2)
key4 = hex(most_frequent(k[4]))[2:].zfill(2)
key5 = hex(most_frequent(k[5]))[2:].zfill(2)
key6 = hex(most_frequent(k[6]))[2:].zfill(2)
key7 = hex(most_frequent(k[7]))[2:].zfill(2)
key8 = hex(most_frequent(k[8]))[2:].zfill(2)
key9 = hex(most_frequent(k[9]))[2:].zfill(2)
key10 = hex(most_frequent(k[10]))[2:].zfill(2)
key11 = hex(most_frequent(k[11]))[2:].zfill(2)
key12 = hex(most_frequent(k[12]))[2:].zfill(2)

print("key is {}{}{}{}{}{}{}{}{}{}{}{}{} and message is {}".format(format(key0),format(key1),format(key2),format(key3),format(key4),format(key5),format(key6),format(key7),format(key8),format(key9),format(key10),format(key11),format(key12),format(message), 'x'))                                    
print("Gathering keystream first bytes for IV=01FFxx ... done")
print("Guessing m[0] ... done")
print(" Guessed m[0]= {} (with freq. {}) *** OK ***".format(format(message),myxor_m.count(most_frequent(myxor_m)), 'x'))     # to print the hex without 0x value
print("Gathering keystream first bytes for IV=03FFxx ... done\nGuessing k[0] ... done")
print(" Guessed k[0]= {} (with freq. {}) *** OK ***".format(format(key0),k[0].count(most_frequent(k[0])),'x'))
print("Gathering keystream first bytes for IV=04FFxx ... done\nGuessing k[1] ... done")
print(" Guessed k[1]= {} (with freq. {}) *** OK ***".format(format(key1),k[1].count(most_frequent(k[1])),'x'))
print("Gathering keystream first bytes for IV=05FFxx ... done\nGuessing k[2] ... done")
print(" Guessed k[2]= {} (with freq. {}) *** OK ***".format(format(key2),k[2].count(most_frequent(k[2])),'x'))
print("Gathering keystream first bytes for IV=06FFxx ... done\nGuessing k[3] ... done")
print(" Guessed k[3]= {} (with freq. {}) *** OK ***".format(format(key3),k[3].count(most_frequent(k[3])),'x'))
print("Gathering keystream first bytes for IV=07FFxx ... done\nGuessing k[4] ... done")
print(" Guessed k[4]= {} (with freq. {}) *** OK ***".format(format(key4),k[4].count(most_frequent(k[4])),'x'))
print("Gathering keystream first bytes for IV=08FFxx ... done\nGuessing k[5] ... done")
print(" Guessed k[5]= {} (with freq. {}) *** OK ***".format(format(key5),k[5].count(most_frequent(k[5])),'x'))
print("Gathering keystream first bytes for IV=09FFxx ... done\nGuessing k[6] ... done")
print(" Guessed k[6]= {} (with freq. {}) *** OK ***".format(format(key6),k[6].count(most_frequent(k[6])),'x'))
print("Gathering keystream first bytes for IV=0AFFxx ... done\nGuessing k[7] ... done")
print(" Guessed k[7]= {} (with freq. {}) *** OK ***".format(format(key7),k[7].count(most_frequent(k[7])),'x'))
print("Gathering keystream first bytes for IV=0BFFxx ... done\nGuessing k[8] ... done")
print(" Guessed k[8]= {} (with freq. {}) *** OK ***".format(format(key8),k[8].count(most_frequent(k[8])),'x'))
print("Gathering keystream first bytes for IV=0CFFxx ... done\nGuessing k[9] ... done")
print(" Guessed k[9]= {} (with freq. {}) *** OK ***".format(format(key9),k[9].count(most_frequent(k[9])),'x'))
print("Gathering keystream first bytes for IV=0DFFxx ... done\nGuessing k[10] ... done")
print(" Guessed k[10]= {} (with freq. {}) *** OK ***".format(format(key10),k[10].count(most_frequent(k[10])),'x'))
print("Gathering keystream first bytes for IV=0EFFxx ... done\nGuessing k[11] ... done")
print(" Guessed k[11]= {} (with freq. {}) *** OK ***".format(format(key11),k[11].count(most_frequent(k[11])),'x'))
print("Gathering keystream first bytes for IV=0FFFxx ... done\nGuessing k[12] ... done")
print(" Guessed k[12]= {} (with freq. {}) *** OK ***".format(format(key12),k[12].count(most_frequent(k[12])),'x'))