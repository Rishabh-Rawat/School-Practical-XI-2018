st = " "+input("Enter the string")
str = "" 
for i in range(0,len(st)-1):
     if st[i] == " ":
        str = str+st[i+1].capitalize()
     else:
        str = str+st[i+1]
print("New string:",str)
