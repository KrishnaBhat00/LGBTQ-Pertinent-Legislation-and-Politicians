from statenames import StateNames
import json

state = StateNames()
with open ('acluData.json', 'r') as json_data:
    data = json.load(json_data)
for i in data:
    print (
        state.fullName(i['state']) + "\\" + i['billId'] + "\\" + i['description'] + "\\" + i['status']
    )