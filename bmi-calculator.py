height = float(input("Zadejte výšku v cm"))
weight = float(input("Zadejte váhu v kg"))

height /= 100   
bmi = weight/(height**2)

if(bmi <= 18.5):
    print("Podváha", round(bmi, 2))
elif(bmi <= 24.9):
    print("Norma", round(bmi, 2))
elif(bmi <= 29.9):
    print("Nadváha", round(bmi, 2))
elif(bmi <= 34.9):
    print("Obezita 1. stupně", round(bmi, 2))
elif(bmi <= 39.9):
    print("Obezita 2. stupně", round(bmi, 2))
else:
    print("Obezita 3. stupně", round(bmi, 2))