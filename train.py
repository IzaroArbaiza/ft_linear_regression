import csv

def read_database(filename):
    mileages = [] 
    prices = [] 

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) < 2:
                continue
            try:
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
            except ValueError:
                continue
    return mileages, prices

def scale_data(mileages, prices):
    scaled_mileages = [m / 10000 for m in mileages]
    scaled_prices = [p / 10000 for p in prices]
    return scaled_mileages, scaled_prices

def estimated_price(mileages, theta0, theta1):
    return theta0 + (theta1 * mileages)

def train(mileages, prices, learning_rate, iterations):
    theta0 = 0.0
    theta1 = 0.0
    m = len(mileages)

    for i in range(iterations):
        total_error = 0.0
        total_error_mileage = 0.0

        for j in range(m):
            estimated = estimated_price(mileages[j], theta0, theta1)
            error = estimated - prices[j]
            total_error += error
            total_error_mileage += error * mileages[j]
        theta0 -= learning_rate * (total_error / m)
        theta1 -= learning_rate * (total_error_mileage / m)
    return theta0, theta1

def save_theta(theta0, theta1):
    with open('theta.txt', 'w') as file:
        file.write(f"{theta0},{theta1}\n")

def main():
    mileages, prices = read_database('data.csv')
    mileages, prices = scale_data(mileages, prices)

    learning_rate = 0.01
    iterations = 1000

    theta0, theta1 = train(mileages, prices, learning_rate, iterations)

    save_theta(theta0, theta1)
    print("Entrenamiento completado.")
    print(f"theta0: {theta0}")
    print(f"theta1: {theta1}")

if __name__ == "__main__":
    main()
