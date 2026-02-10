import csv

mileages = []
prices = []
theta0 = 0.0
theta1 = 0.0

#Lee datos
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) #salta la primera linea (mileagre,price)
    for row in reader:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))

print("Datos leidos (sin escalar):")
for i in range(len(mileages)):
    print(f"Mileage = {mileages[i]}, Price = {prices[i]}")

#Escala los datos
mileages = [m / 10000 for m in mileages]
prices = [p / 10000 for p in prices]

#Funcion estimar precio
def estimated_price(mileages, theta0, theta1):
    return theta0 + (theta1 * mileages)

#Configuracion entrenamiento
learning_rate = 0.01
iterations = 1000
m = len(mileages)

#Gradient descent
for i in range(iterations):
    total_error = 0.0
    total_error_mileage = 0.0

    for j in range(m):
        estimated = estimated_price(mileages[j], theta0, theta1)
        error = estimated - prices[j]
        total_error += error
        total_error_mileage += error * mileages[j]
    
    tmp_theta0 = learning_rate * (total_error / m)
    tmp_theta1 = learning_rate * (total_error_mileage / m)

    theta0 += tmp_theta0
    theta1 += tmp_theta1

    if i % 100 == 0:
        print(f"Iteration {i}: theta0={theta0:.5f}, theta1={theta1:.5f}")

#Resultado final
print("\nModelo entrenado:")
print(f"theta0 = {theta0:.5f}")
print(f"theta1 = {theta1:.5f}")

#Guardar theta0 y theta1 en un archivo
with open('theta.txt', 'w') as file:
    file.write(f"{theta0},{theta1}\n")

print("\nTheta guardado en theta.txt")