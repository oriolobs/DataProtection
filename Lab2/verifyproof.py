import os

#input
publicusefulInfo = input("Public info of the Merkle tree:")
nameDoc = input("Document to verify the proof of membership:")
proofText = input("Filename with the necessary nodes to verify:")

hash = publicusefulInfo.rsplit(":")[-1]
treeLayers = int(publicusefulInfo.rsplit(":")[-2])
node = 0
layer = 0

f2 = open(proofText, "r")
numNodes = f2.read().rsplit(":")
f2.close()
nod = numNodes[node]

os.system("cat doc.pre " + nameDoc + " | openssl dgst -sha1 -binary | xxd -p > hashVerify.txt") #creates new .txt
for i in range(treeLayers):
    os.system("cp hashVerify.txt hashVerify2.txt")

    if int(nod[4]) == layer:
        if int(nod[6])%2 == 0:
            os.system("cat node.pre " + nod + " hashVerify2.txt | openssl dgst -sha1 -binary | xxd -p > hashVerify.txt")
        else:
            os.system("cat node.pre hashVerify2.txt " + nod + " | openssl dgst -sha1 -binary | xxd -p > hashVerify.txt")
        nod = numNodes[node + 1]
    if layer+1 == treeLayers: 
        hashVerify = os.popen("cat hashVerify2.txt").read()
        if hash in hashVerify:
            print("Proof of membership verified")
        else:
            print("Proof of membership not verified")
        os.system("rm hashVerify.txt") #detele temporal file
        os.system("rm hashVerify2.txt") #detele temporal file
    else:
        os.system("cat node.pre hashVerify2.txt | openssl dgst -sha1 -binary | xxd -p > hashVerify.txt")
    layer = layer + 1