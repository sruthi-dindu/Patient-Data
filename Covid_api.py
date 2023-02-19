'''import requests
import json

url = 'https://api.github.com/events'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
response = response.json()
for i,j in response.items():
    print(i + '  :', end='\t')
    print(j)'''

import requests
import pandas as pd
import json

url = "http://currencyscoop.p.rapidapi.com/latest"
 
headers = {
    'X-RapidAPI-Key': '155da60f68msh87ed548ac362842p1b5a56jsnf2c4e2972a0f',
    'X-RapidAPI-Host': 'currencyscoop.p.rapidapi.com'
}
 
response = requests.request("GET", url, headers=headers)
myjson = response.json()
print("converted response into json")
myjson_data = myjson['response']

'''data_csv = pd.DataFrame(myjson_data)
data_csv.to_csv('exercise.csv')


#writing data to a text file
df = pandas.read_csv('exercise.csv')
print(df)

with open('exercise.txt','w') as f:
    json.dump(myjson, f, indent=4)'''

