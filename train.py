import csv

mileages = []
prices = []

#Lee el csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) #salta la primera linea (mileagre,price)
    for row in reader:
        #copia cada columna en las listas
        mileages.append(float(row[0]))
        prices.append(float(row[1]))

#Print de los datos leidos
print("Datos leidos: ")
for i in range(len(mileages)):
    print(f"Mileage: {mileages[i]}, Price: {prices[i]}")