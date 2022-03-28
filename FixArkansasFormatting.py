txtFile = open('ArkansasPoliticans.txt', 'r')
names = txtFile
string = ""
num = 0
for name in names:
    if name.endswith(","):
        temp = ""
        for i in range(len(name) - 1):
            temp += i
        name = temp
    if len(name.split()) > 2:
        if not("Jr" in name.split()[2]):
            temp = name.split()                
            string += temp[0] + " " + temp[2] + "\n"
        else:
            string += name
    else:
        string += name

txtFile.close()
txtFile = open('ArkansasPoliticansFixed.txt', 'w')
txtFile.write(string)
txtFile.close()