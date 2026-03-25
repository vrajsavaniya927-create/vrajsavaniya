f = open ("myfile.txt","r")
data = f.read()
print("file content:",data)
f.close()

f = open ("myfile.txt","r")
data = f.readline()
print("file content:",data)
f.close()

f = open ("myfile.txt","r")
data = f.readlines()
print("file content:",data)
f.close()