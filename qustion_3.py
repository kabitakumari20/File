banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
file=open("bankname.txt","w")
i=0
while i<len(banks_list):
    file.write(banks_list[i])
    file.write("\n")
    i+=1
file.close()

# file=open("bankname.txt","r")
# print(file.read())
# file.close()
