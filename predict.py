def load_theta():
	try:
		with open('theta.txt', 'r') as file:
			content = file.read()
			theta0, theta1 = map(float, content.split(','))
			return theta0, theta1
	except FileNotFoundError:
		print("Modelo no entrenado. Valores por defecto (0, 0)")
	return 0.0, 0.0

def estimated_price(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def main():
	theta0, theta1 = load_theta()

	mileage = float(input("Ingrese el kilometraje del auto: "))

	scaled_mileage = mileage / 10000
	scaled_price = estimated_price(scaled_mileage, theta0, theta1)
	price = scaled_price * 10000

	print(f"El precio estimado: {price:.2f}€")

if __name__ == "__main__":
	main()