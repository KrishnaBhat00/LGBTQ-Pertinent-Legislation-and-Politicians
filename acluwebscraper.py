from bs4 import BeautifulSoup
from billparse import billparse
import requests
import json

url = 'https://www.aclu.org/legislation-affecting-lgbtq-rights-across-country'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

allTables = content.findAll('table')
# = allTables[1].find_all('tr')
#state1 = sectionA[0].find_all('td')
allHeaders = content.findAll('h3')

billArr = []

def descriptionFormatting(text):
    arr = str(text).split(" ")
    desc = ""
    if len(arr) > 0:
        for i in range(len(arr)):
            if i >= 1 and len(arr[i]) > 2:
                desc += arr[i] + " "
            elif i >= 1:
                desc += arr[i] + " "
            else:
                desc = ""
    return desc
    
for table in range(len(allTables)):
    allRows = allTables[table].find_all('tr')
    if (table < len(allHeaders)):
        description = descriptionFormatting(allHeaders[table].text)
    else:
        description = "default"
    for row in range(len(allRows)):
        if row == 0:
            continue
        cells = allRows[row].find_all('td')
        #parser = billparse(allRows[row].text.encode('ascii', errors="ignore"))
        if len(allRows[row].text.encode('ascii', errors="ignore")) != 0:
            state = cells[0].text
            allBillIDs = cells[1].findAll('p')
            allStatuses = cells[2].findAll('p')
            print(allBillIDs[0].text)
            for bill in range(len(allBillIDs)):
                billObject = {
                    "state" : state,
                    "billId" : allBillIDs(bill).text,
                    "description" : description,
                    "status" : allStatuses(bill).text
                }
                print (billObject)
                billArr.append(billObject)
#print (billArr)
print (len(billArr))
with open ('acluData.json', 'w') as outfile:
    json.dump(billArr, outfile, default=str)