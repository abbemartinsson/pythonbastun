import random

def fahr_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{celsius:.2f} grader")
    kolla_grader(celsius)
    return celsius

def random_fahr_to_cel(farenheit):
    farenheit = (random.uniform(50,200))
    celsius = (farenheit - 32) * 5 / 9
    print(f"{celsius:.2f} grader")
    if 82 <= celsius <= 87:
        kolla_grader(celsius)
    elif celsius > 87:
        random_fahr_to_cel(farenheit)
    elif celsius < 82:
        random_fahr_to_cel(farenheit)
    return celsius 

def kolla_grader(celsius):
    if 82 <= celsius <= 87:
        print("Lagom!")

    elif celsius > 87:
        print("För Varmt! Testa igen")

    elif celsius < 82:
        print("För Kallt! Testa igen")
while True:
    print("1: starta program!")
    print("0: starta inte program!")
    start = input()
    match start:
        case "1":
            print("Skriv in farenheit:")
            farenheit = float(input())
        
            if farenheit > 0:
                celsius = fahr_to_cel(farenheit)

            else:
                celsius = random_fahr_to_cel(farenheit)
            break
        case "0":
            print("Hejdå!")
            break
        case _:
            print("Ange ett giltigt värde!")