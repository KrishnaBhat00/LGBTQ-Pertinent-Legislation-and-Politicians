import json

names = []
with open('ballotpediaTestData.json', 'r') as json_data: 
    data = json.load(json_data)
with open('ArkansasA461Sponsors.txt', 'r') as sponsors:
    names = sponsors.read().split("\n")
sponsorsList = []
#print (names)
listCounter = 0
for i in data:
    if i['name'] == names[listCounter]:
        threatObject = {
            "name" : i['name'],
            "winPercent" : i['winPercent'],
            "years" : i['yearsInPosition']
        }
        sponsorsList.append(threatObject)
        listCounter += 1
#print (sponsorsList)
print (len(sponsorsList))
winPercentList = []
for i in sponsorsList:
    