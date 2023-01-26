import os

#input
nameDoc = input("Document to generate the proof of membership:") 
posDoc = input("Position of the Document to generate the proof of membership:") 

f = open("finalmerkletree.txt", "r")
publicusefulInfo = f.readline() 
usefulInfo = publicusefulInfo.rsplit(":")
numNodes = int(usefulInfo[-2])
treeLayers = int(usefulInfo[-2])
hash = str(treeLayers-1) + ":0:" + usefulInfo[-1]
found = False
p = int(posDoc)
layer = 0

for i in f: #Checks if the Document and position is found in the tree / with hash
    if os.popen("cat doc.pre " + nameDoc + " | openssl dgst -sha1 -binary | xxd -p").read() in i and layer == int(i[0]) and p == int(i[2]):
        found = True
        break
f.close()

if found: 
    
    for i in range(treeLayers-1):
        f = open("finalmerkletree.txt", "r")
        
        if p+1 != numNodes:
            for z in f:
                if str(i) + ":" + str(p+1) in z:
                    print(z)
        p = int(p/2)
        if p%2 == 1:        
            for z in f:
                if str(i) + ":" + str(p-1) in z:
                    print(z)
        numNodes = int(numNodes/2) + numNodes%2
    f.close() 
    print(hash)

else: 
    print("no coincidences found")
