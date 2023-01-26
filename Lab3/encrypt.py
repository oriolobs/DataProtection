import os
import sys

#read the message to encrypt
messagetoencrypt = sys.argv[2]

#generate the ephkeys
os.system("openssl genpkey -paramfile param.pem -out tempephkey.pem")
os.system("openssl pkey -in tempephkey.pem -pubout -out  ephpubkey.pem")

os.system("openssl pkeyutl -inkey tempephkey.pem -peerkey " + sys.argv[1] + "_pubkey.pem -derive -out common.bin")


os.system("cat common.bin | openssl dgst -sha256 -binary | head -c 16 > k1.bin")
os.system("cat common.bin | openssl dgst -sha256 -binary | tail -c 16 > k2.bin")

#random iv of 16 bytes
os.system("openssl rand 16 > iv.bin")

#encryption
os.system("echo -n \"" + sys.argv[2] +"\" | openssl enc -aes-128-cbc -K `cat k1.bin | xxd -p` -iv `cat iv.bin | xxd -p` > ciphertext.bin")

#tag
os.system("cat iv.bin ciphertext.bin | openssl dgst -sha256 -mac hmac -macopt hexkey:`cat k2.bin | xxd -p` -binary > tag.bin")

#write the file
os.system("cat ephpubkey.pem > ciphertext.pem")
os.system("echo \"-----BEGIN AES-128-CBC IV-----\" >> ciphertext.pem")
os.system("cat iv.bin | openssl base64 >> ciphertext.pem")
os.system("echo \"-----END AES-128-CBC IV-----\" >> ciphertext.pem")
os.system("echo \"-----BEGIN AES-128-CBC CIPHERTEXT-----\" >> ciphertext.pem")
os.system("cat ciphertext.bin | openssl base64 >> ciphertext.pem")
os.system("echo \"-----END AES-128-CBC CIPHERTEXT-----\" >> ciphertext.pem")
os.system("echo \"-----BEGIN SHA256-HMAC TAG-----\" >> ciphertext.pem")
os.system("cat tag.bin | openssl base64 >> ciphertext.pem")
os.system("echo \"-----END SHA256-HMAC TAG-----\" >> ciphertext.pem")
