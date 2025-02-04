# PRÓBA ZROBIENIA STRONY INTERNETOWEJ Z ZAIMPORTOWANIEM DANYCH Z EXCELA, W KTÓRYM SĄ DANE Z API NBP

# MÓJ PROGRAM WYKORZYSTUJĄCY LISTY I SŁOWNIKI - Oraz requests.get(url)
import os
os.system("cls")

import sys
from dateutil import parser
import requests

data_tabeli_NBP = input("wpisz datę tabeli NBP w formacie YYYY-mm-dd:\n\t")
data = parser.parse(data_tabeli_NBP)
data_do_url = data.strftime('%Y-%m-%d')
url = f"http://api.nbp.pl/api/exchangerates/tables/a/{data_do_url}/?format=json"
response = requests.get(url)

# OBSŁUGA BŁĘDÓW DLA 'response'
if response.status_code == 404:
    print("Brak danych")
    sys.exit(2)
if not response.ok:
    print("Unexpected server response")
    sys.exit(3)

jsons = response.json()

#for x in list(range(32)):
# rates = jsons[0]['rates'][x]
#    print(rates)
# elements = rates.items()
#    print(elements)
# titlerow = ('WALUTA','KOD','KURS WALUTY z dnia: ' + data_do_url)

os.system("cls")
powt = '=' * 81

print('TABELA WALUT')
print(powt) 

print(f"{'WALUTA':40}","|",f"{'KOD':5}","|",f"{'KURS WALUTY z dnia: ' + data_do_url:10}")
# print(titlerow)
print(powt) 

lista_liczb = list(range(1,32))

for x in lista_liczb:
    rates = jsons[0]['rates'][x]
    column1=rates['currency']
    column2=rates['code']
    column3=rates['mid']
    # content = [column1,column2,column3]
    print(f"{column1:40}","|",f"{column2:5}","|",f"{column3:10}")

print(powt) 

from pandas import DataFrame
titlerow = ('WALUTA','KOD','KURS WALUTY z dnia: ' + data_do_url)

total_content = []
total_content.append(titlerow)
for x in lista_liczb:
    rates = jsons[0]['rates'][x]
    column1=rates['currency']
    column2=rates['code']
    column3=rates['mid']
    content = [column1,column2,column3]
    total_content.append(content)

df = DataFrame(total_content)

# Zapisujemy arkusz do pliku
tekst = (r"C:\Praktyczny_Python\ROBOCZE\tabela kursów NBP z dnia "+str(data_do_url)+".xlsx")
df.to_excel(tekst,sheet_name='NBP z '+str(data_do_url),index=False)
