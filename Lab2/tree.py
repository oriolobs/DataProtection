import os

#prefixes
os.system("echo -n ''\x35\x35\x35\x35\x35\x35'' > doc.pre") 
os.system("echo -n '\xe8\xe8\xe8\xe8\xe8\xe8' > node.pre") 

doc_num = input ("Enter the number of the doc files files:") #number of documents to be hashed
doc_num = int(doc_num)

file = []
for i in range(doc_num): #hash the documents
    file.append(input("Enter the document" + str(i+1) + ":"))
    os.system("cat doc.pre " + file[i] + " | openssl dgst -sha1 -binary | xxd -p > node0." + str(i))
    os.system("echo -n '" + str(0) + ":" + str(i) + ":' >> merkletree.txt")
    os.system("cat node" + str(0) + "." + str(i) + " >> merkletree.txt")

layer = 0
hashes_num = doc_num
while hashes_num > 1:  #create new layers
    
    num = 0
    for i in range(0, hashes_num, 2): 
        if i == hashes_num-1 and hashes_num%2 == 1:
            os.system("cat node.pre node" + str(layer) + "." + str(i) + " | openssl dgst -sha1 -binary | xxd -p > node" + str(layer+1) + "." + str(num)) #the node(i-1).(2j+1) doesn't exist
        else:
            os.system("cat node.pre node" + str(layer) + "." + str(i) + " node" + str(layer) + "." + str(i+1) + " | openssl dgst -sha1 -binary | xxd -p > node" + str(layer+1) + "." + str(num))
        

        os.system("echo -n '" + str(layer+1) + ":" + str(num) + ":' >> merkletree.txt")
        os.system("cat node" + str(layer+1) + "." + str(num) + " >> merkletree.txt")
        num = num+1

    layer = layer + 1
    
    if hashes_num%2 == 1:

        hashes_num = int(hashes_num/2) + 1
    else:

        hashes_num = int(hashes_num/2)

root = os.popen("cat node" + str(layer) + ".0").read()

os.system("echo -n '" "MerkleTree:sha1:353535353535:e8e8e8e8e8e8:" + str(doc_num) + ":" + str(layer+1) + ":" + root + "' > finalmerkletree.txt")

os.system("cat merkletree.txt >> finalmerkletree.txt")