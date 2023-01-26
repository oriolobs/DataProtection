import os

doc = input("Enter the new file:")

#number of tree's nodes
f = open("finalmerkletree.txt", "r")
public_info = f.readline() 
info = public_info.rsplit(":") 
nodes_num = int(info[-2]) 


info_nodes = ""
for i in range (nodes_num): 
    info_nodes = info_nodes + f.readline()
f.close()
os.system("cat doc.pre " + doc + " | openssl dgst -sha1 -binary | xxd -p > node0." + str(nodes_num)) 

f = open("newtree.txt", "a")
f.write(info_nodes)
f.close()
os.system("echo -n '" + str(0) + ":" + str(nodes_num) + ":' >> newtree.txt") 
os.system("cat node" + str(0) + "." + str(nodes_num) + " >> newtree.txt")
nodes_num = nodes_num + 1
old_nodes = nodes_num

layer = 0
while nodes_num > 1:
    num = 0
    for i in range(0, nodes_num, 2):
        if i == nodes_num-1 and nodes_num%2 == 1:
            os.system("cat node.pre node" + str(layer) + "." + str(i) + " | openssl dgst -sha1 -binary | xxd -p > node" + str(layer+1) + "." + str(num))
        else:
            os.system("cat node.pre node" + str(layer) + "." + str(i) + " node" + str(layer) + "." + str(i+1) + " | openssl dgst -sha1 -binary | xxd -p > node" + str(layer+1) + "." + str(num))
        os.system("echo -n '" + str(layer+1) + ":" + str(num) + ":' >> newtree.txt")
        os.system("cat node" + str(layer+1) + "." + str(num) + " >> newtree.txt")
        num = num+1

    layer = layer + 1
    
    if nodes_num%2 == 1:

        nodes_num = int(nodes_num/2) + 1
    else:

        nodes_num = int(nodes_num/2)

root = os.popen("cat node" + str(layer) + ".0").read()

os.system("echo -n '" "MerkleTree:sha1:353535353535:e8e8e8e8e8e8:" + str(old_nodes) + ":" + str(layer+1) + ":" + root + "' > finalmerkletree.txt")
os.system("cat newtree.txt >> finalmerkletree.txt") 
os.system("rm newtree.txt")
