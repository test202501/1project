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

lista_liczb_test = list(range(1))

for x in lista_liczb_test:
    rates = jsons[0]['rates'][x]
    elements = rates.items()
    print("\n",'SKŁADOWE PLIKU JSON:')
    powt = '-' * 90
    print(powt)    
    print("json:","\n",jsons)
    print("\n","rates: ","\n",rates)
    print("\n","elements: ","\n",elements)
    print("\n",'docelowy układ:',"\n")
    print(rates['currency'],"\t",rates['code'],"\t",rates['mid'])

powt = '=' * 90
print(powt) 
print("jsons:",type(jsons))
print("rates:",type(rates))
print("elements:",type(elements))
print("x:",type(x))

print(powt) 
print('WŁAŚCIWA TABELA WALUT')
print(powt) 
titlerow = ('WALUTA','KOD','KURS WALUTY z dnia:',data_do_url)

powt = '-' * 90
print(powt)    

lista_liczb = list(range(1,32))
# test wygenerowania listy liczb z podanego wyżej zakresu
# for elem_lista_liczb in lista_liczb:
#     print("lista liczb:",elem_lista_liczb)

from pandas import DataFrame

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