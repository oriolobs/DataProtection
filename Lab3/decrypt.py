import sys
import os

#We open the file and read the 4 variables
f = open(sys.argv[1], "r")
variable = f.read()
f.close()

ephpubkey_pos = variable.find("-----END PUBLIC KEY-----")
ephpubkey = variable[:ephpubkey_pos+24]
os.system("echo -n \"" + ephpubkey + "\" > ephpubkey.pem")

iv_pos = variable.find("-----END AES-128-CBC IV-----")
iv = variable[ephpubkey_pos+56:iv_pos]
os.system("echo -n \"" + iv + "\" | openssl base64 -d -out iv.bin")

ciphertext_position = variable.find("-----END AES-128-CBC CIPHERTEXT-----")
ciphertext = variable[iv_pos+68:ciphertext_position]
os.system("echo -n \"" + ciphertext + "\" | openssl base64 -d -out ciphertext.bin")

tag_position = variable.find("-----END SHA256-HMAC TAG-----")
tag = variable[ciphertext_position+69:tag_position]
os.system("echo -n \"" + tag + "\" | openssl base64 -d -out tag.bin")

os.system("openssl pkeyutl -inkey " + sys.argv[2] + "_pkey.pem -peerkey ephpubkey.pem -derive -out common.bin")

#Split the key values
os.system("cat common.bin | openssl dgst -sha256 -binary | head -c 16 > k1.bin")
os.system("cat common.bin | openssl dgst -sha256 -binary | tail -c 16 > k2.bin")

os.system("cat iv.bin ciphertext.bin | openssl dgst -sha256 -mac hmac -macopt hexkey:`cat k2.bin | xxd -p` -binary > outcome_tag.bin")

#Abort the decryption process and notify the error if the outcome differs from the file tag.bin.
if os.popen("cat tag.bin | openssl base64").read() == os.popen("cat outcome_tag.bin | openssl base64").read():
    os.system("openssl enc -aes-128-cbc -d -in ciphertext.bin -iv `cat iv.bin | xxd -p` -K `cat k1.bin | xxd -p` -out deciphered.txt")
else:
    print("Decryption process aborted, tag.bin differs from file")