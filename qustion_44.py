f=open("qustion_44.txt","r")
file1=open("delhi.text","w")
file2=open("shimla.txt","w")
file3=open("other.txt" ,"w")
data=f.read()
data1=data.split("\n")
for i in range(0,len(data1)):
    if "delhi" in data1[i]:
        file1.write(data1[i])
        file1.write("\n")
    elif "shimla" in data1[i]:
        file2.write(data1[i])
        file2.write("\n")
    else:
        file3.write(data1[i])
        file3.write("\n")
file1.close()
file2.close()
file3.close()
f.close()