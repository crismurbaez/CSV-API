import requests
import csv


# app que permite cargar empresas que estaban guardadas en archivo de excell
# que luego fue guardado como formato csv separado por ;
# se guarda en una base de mongoDB
# la url dada es la que hace el CRUD a la base de mongoDB

URL_REQUEST = "https://api-companies.vercel.app/company"


# read file csv
onefile = input("Enter path to CSV file: ")
with open(onefile, newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    print(reader)
    for row in reader:
        print(row)
        # post row for file in API companies
        print("POST")
        payload = row
        response = requests.post(URL_REQUEST, json=payload)
        print(response.url)

        if response.status_code == 200:
            print(response.content)
