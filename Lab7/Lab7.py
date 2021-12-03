import requests
import re

listData = requests.get('https://bazaar.abuse.ch/browse/').text
shaValues = set(re.findall("[A-Fa-f0-9]{64}", listData))
print(shaValues)

#Write the sha_values into a txt file.......
f = open("shaValues.txt", "w")
for shaValue in shaValues:
	f.write(shaValue + '\n')
f.close()