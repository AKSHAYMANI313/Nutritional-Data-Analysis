#Webscrapping of Chick-Fil-A data
from bs4 import BeautifulSoup
import requests
import csv
url = 'https://www.chick-fil-a.com/nutrition-allergens'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all('table',id=['MOBILE_BREAKFAST-nutrition','MOBILE_ENTREES-nutrition','MOBILE_TREATS-nutrition','MOBILE_KIDSMEALS-nutrition'])
table=tables[0]
table1=tables[1]
table2=tables[2]
table3=tables[3]
with open ("C:\\Users\\mania\\Downloads\\chick_fil_a_raw.csv",'w',newline='') as csv_file:
    csv_writer= csv.writer(csv_file)
    columns = list(map(lambda x: x.text,table.find_all(['th'])))
    csv_writer.writerow(columns)

    for row in table.find_all('tr'):
        records = list(map(lambda x:x.text.strip(),row.find_all(['td'])))
        csv_writer.writerow(records[:len(columns)])

    for row in table1.find_all('tr'):
        records = list(map(lambda x: x.text.strip(), row.find_all(['td'])))
        csv_writer.writerow(records[:len(columns)])

    for row in table2.find_all('tr'):
        records = list(map(lambda x:x.text.strip(),row.find_all(['td'])))
        csv_writer.writerow(records[:len(columns)])

    for row in table2.find_all('tr'):
        records = list(map(lambda x:x.text.strip(),row.find_all(['td'])))
        csv_writer.writerow(records[:len(columns)])

    for row in table3.find_all('tr'):
        records = list(map(lambda x:x.text.strip(),row.find_all(['td'])))
        csv_writer.writerow(records[:len(columns)])

#KFC Data was downloaded as a PDF
