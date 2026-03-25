f = open("myfile.txt","w")
f.write("my name is vraj")
f.write("welcome to python file")
f.write("learning is fun")
f.close()

f = open("myfile.txt","w")
lr=["python\n","savaniya"]
f.writelines(lr)
f.close()