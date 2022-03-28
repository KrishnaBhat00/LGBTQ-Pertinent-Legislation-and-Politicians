from bs4 import BeautifulSoup
import requests
import json

#get names
txt = open ('TexasPoliticansSenateFixed.txt', 'r')
namesArr = txt.read().split("\n")
#namesArr = ["Aaron Pilkington"] , "Andrew Collins", "Ashley Hudson", "Austin McCollum", "Brandt Smith", "Brian Evans", "Bruce Coleman", "Bruce Cozart", "Cameron Cooper", "Carlton Wing", "Carol Dalby", "Charlene Fite", "Cindy Crawford", "Clint Penzo", "Craig Christiansen", "Danny Watson", "David Fielding", "David Hillman", "David Ray", "David Tollett"]
politicansArr = []

baseUrl = 'https://ballotpedia.org/'
for name in namesArr:
    response = requests.get(baseUrl + name, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    print(content.find('title').text)

    if content.find('div', attrs={"class": "infobox person"}) == None or content.find('div', attrs={"class": 'results_table_container'}) == None:
        response = requests.get(baseUrl + name + "_(Texas)", timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    if content.find('div', attrs={"class": "infobox person"}) == None or content.find('div', attrs={"class": 'results_table_container'}) == None:
        response = requests.get(baseUrl + name + "_(Texas_House_of_Representatives)", timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    politican = content.find('div', attrs={"class": 'infobox person'})
    resultsbox = content.find('div', attrs={"class": 'results_table_container'})
    infoArr = politican.find_all('div')
    resultsArr = resultsbox.find_all('tr')


    #Infobox Related Methods 
    def findText(search):
        for i in range(len(infoArr)):
            if infoArr[i].text == search:
                return infoArr[i + 1].text.encode('ascii', errors="ignore")
    #encodes to ascii !!
    def cleanText(text):
        newText = ""
        for i in range(len(text)):
            if text[i] >= 32:
                newText = newText + chr(text[i])
        return newText
    def findDistrict():
        for i in infoArr:
            if "District" in i.text:
                words = i.text.split()
                return words[len(words) - 1]
    def firstYear(text):
        return text.split()[0]
    def findParty():
        party = ""
        for i in infoArr:
            if "Party" in i.text:
                party = i.text.encode('ascii', errors="ignore")
        if not("Party" in str(party)):
            party = "Independent".encode("ascii", errors="ignore")
        return party

    #Results box related methods
    def findOpponent():
        if len(resultsArr) < 3:
            return "unchallenged"
        else:
            row = resultsArr[2]
            name = row.find('td', attrs={"class":"votebox-results-cell--text"}).text.encode('ascii', errors="ignore")
        name2 = ""
        for i in name:
            if (i >= 32):
                name2 = name2 + chr(i)
        name = name2
        return name

    if resultsbox.find('div', attrs={"class": "percentage_number"}) != None:
        politicanObject = {
            'name' : name,
            'termEnds' : cleanText(findText("Term ends")),
            'firstYear' : firstYear(cleanText(findText("Tenure"))),
            'yearsInPosition' : cleanText(findText("Years in position")),
            'district' : findDistrict(),
            'party' : cleanText(findParty()),
            'winPercent' :  float(resultsbox.find('div', attrs={"class": "percentage_number"}).text),
            'opponent' : findOpponent()
        }
    else:
        politicanObject = {
            'name' : name,
            'termEnds' : cleanText(findText("Term ends")),
            'firstYear' : firstYear(cleanText(findText("Tenure"))),
            'yearsInPosition' : cleanText(findText("Years in position")),
            'district' : findDistrict(),
            'party' :   cleanText(findParty()),
            'winPercent' :  0.00,
            'opponent' : findOpponent()
        }
    politicansArr.append(politicanObject)

txt.close()

with open('ballotpediaTestData.json', 'w', encoding = 'utf8') as outfile:
    json.dump(politicansArr, outfile, default= str)
