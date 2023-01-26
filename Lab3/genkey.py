import os
import sys

name = sys.argv[1]

if not os.path.isfile("param.pem"):
    os.system("openssl genpkey -genparam -algorithm dh -pkeyopt dh_rfc5114:3 -out param.pem")

os.system("openssl genpkey -paramfile param.pem -out " + name + "_pkey.pem")
os.system("openssl pkey -in " + name + "_pkey.pem -pubout -out " + name + "_pubkey.pem")
