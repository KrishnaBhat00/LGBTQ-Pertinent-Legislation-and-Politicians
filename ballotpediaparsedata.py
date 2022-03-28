import json

names = []
with open('ballotpediaTestData.json', 'r') as json_data: 
    data = json.load(json_data)
print ("name\\\\term\\years\\district\\winpercent\topponent" )
for i in data:
    print (
        i['name'] + "\\" + i['termEnds'] + "\\" + i['firstYear'] + "\\" + i['yearsInPosition'] + "\\" + i['district'] + "\\" + i['party'] + "\\" + str(i['winPercent']) + "\\" + i['opponent']
    )