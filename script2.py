import json
from urllib import response
import requests

file = open('new2.json', 'r+')

url1 = 'https://raw.githubusercontent.com/portainer/templates/master/templates-2.0.json'
url2 = 'https://raw.githubusercontent.com/Qballjos/portainer_templates/master/Template/template.json'
url3 = 'https://raw.githubusercontent.com/nashosted/self-hosted-template/master/template.json'

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)

data1 = json.loads(response1.text)
data2 = json.loads(response2.text)
data3 = json.loads(response3.text)

# count = 0
# for i1 in data1['templates']:
#     print(i1)
#     count += 1
#     print(count)
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! EINDE DATA1\n')
#
# for i2 in data2['templates']:
#     print(i2)
#
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! EINDE DATA2\n')
#
# for i3 in data3['templates']:
#     print(i3)

newData = {}
newData["version"] = "2"
newData["templates"] = data1['templates'], data2['templates'], data3['templates']

for i in newData['templates']:
    print(i)

json.dump(newData, file, indent=2)

# for templates in data1['templates'], data2['templates'], data3['templates']:
