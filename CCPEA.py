# Conjuture Based Encryption
import random
import os



def generate_collatz_conjuture_key(message):
    n = random.randint(8,1029340)
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    firstprivkey = random.randint(1, len(sequence))
    secondprivkey = random.randint(1, len(sequence))
    thirdprivkey = random.randint(1, len(sequence))
    fourthprivkey = random.randint(1, len(sequence))
    message = message
    fifthprivkey = random.randint(1,len(sequence))
    sixthprivkey = random.randint(1,len(sequence))
    seventhprivkey = random.randint(1,len(sequence))
    eigithprivkey = random.randint(1,len(sequence))
    return firstprivkey,secondprivkey,thirdprivkey,fourthprivkey,fifthprivkey,sixthprivkey,seventhprivkey,eigithprivkey,message


l = generate_collatz_conjuture_key("World")
print(l)
firstprivatekey = l[0]
secondprivatekey = l[1]
thridprivatekey = l[2]
fourthprivatekey = l[3]
fifthprivatekey = l[4]
sixithprivatekey = l[5]
seventhprivatkey = l[6]
eigithprivatekey = l[7]
message = l[8]
firstprivatekeyanswer = input("Input the First Private Key")
firstprivatekeyanswerparsed = int(firstprivatekeyanswer)
secondprivatekeyanswer = input("Input the Second Private Key")
secondprivatekeyanswerparsed = int(secondprivatekeyanswer)
thridprivatekeyanswer = input("Input the Thrid Private Key")
thridprivatekeyanswerparsed = int(thridprivatekeyanswer)
fourthprivatekeyanswer = input("Input the Fourth Private Key")
fourthprivatekeyparsed = int(fourthprivatekeyanswer)
fifthprivatekeyanswer = input("Input the Fifth Private Key")
fifthprivatekeyparsed = int(fifthprivatekeyanswer)
sixithprivatekeyanswer = input("Input the Sixith Private Key")
sixithprivatekeyparsed = int(sixithprivatekeyanswer)
seventhprivatekeyanswer = input("Input the Seventh Private Key")
seventhprivatkeyparsed = int(seventhprivatekeyanswer)
eigithprivatekeyanswer = input("Input the Eigith Private Key")
eigithprivatekeyparsed = int(eigithprivatekeyanswer)
tries = 0

if(firstprivatekeyanswerparsed == firstprivatekey and secondprivatekeyanswerparsed == secondprivatekey and thridprivatekeyanswerparsed == thridprivatekey and fourthprivatekeyparsed == fourthprivatekey and fifthprivatekeyparsed == fifthprivatekey and sixithprivatekeyparsed == sixithprivatekey and seventhprivatkeyparsed == seventhprivatkey and eigithprivatekeyparsed == eigithprivatekey):
    print(message)
else:
    print("Unable to shade polygon normals Error:0x485720102")
