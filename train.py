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

theta0 = 0.0
theta1 = 0.0

def estimated_price(mileages, theta0, theta1):
    return theta0 + (theta1 * mileages) 

estimated_prices = estimated_price(mileages[0], theta0, theta1)
real_prices = prices[0]

error = estimated_prices - real_prices

print("\nErrores para todos los coches: ")
for i in range(len(mileages)):
    estimated_prices = estimated_price(mileages[i], theta0, theta1)
    error = estimated_prices - prices[i]
    print(f"Error para el coche {i}: {error}")