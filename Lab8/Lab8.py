import requests
import time
import csv


def valueCheck(value, listData):
    if value in listData.keys():
        try:
            if listData[value] is None:
                return ""
            else:
                return listData[value]
        except NameError:
            return ""
    else:
        return ""


API_KEY = '6c1082c64a6422032da0bbadba5889eaa726c5c256fc8f197ab70d800832a780'
fieldnames = ['vhash', 'creation_date', 'type_description', 'type_tag', 'meaningful_name', 'size', 'sha256',
              'type_extension', 'sha1', 'md5']
with open("data.csv", "wt", newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(fieldnames)
    with open('MD5.txt', 'r') as f:
        for sha in f:
            sha = sha.rstrip()
            headers = {'x-apikey': API_KEY}
            response = requests.get('https://www.virustotal.com/api/v3/search?query=' + sha, headers=headers)
            data = response.json()
            print(data)
            if len(data['data']) == 0:
                print('not in Virus Total')
            else:
                rows = []
                for value in fieldnames:
                    rows.append(valueCheck(value, data['data'][0]['attributes']))

            writer.writerow(rows)
            time.sleep(15)
    f.close()