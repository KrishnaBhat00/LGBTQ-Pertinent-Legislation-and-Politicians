from tkinter.font import names


firstText = open("TexasPoliticansSenate.txt", 'r')
secondText = open("TexasPoliticansSenateFixed.txt", 'a')

namesArr = firstText.read().split("\n")
for i in namesArr:
    pog = i.split()
    if len(pog) > 1:
        print(pog)
        lastName = pog[0].split(",")
        name = pog[1] + " " + lastName[0] + "\n"
        secondText.write(name)
firstText.close()
secondText.close()
