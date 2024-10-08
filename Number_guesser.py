from random import randint


random_value = randint(0, 100) # Funkcija, kas atgriež nejaušu skaitli no a līdz b ieskaitot

while True:
    provided_value = int(input("Enter a value: "))
    if provided_value > random_value:
        print("Provided value > random value") # konsoles izvade
    elif provided_value < random_value:
        print("Provided value < random value") # konsoles izvade
    else:
        print("You guessed right.")
        break # - cikls tiek partraukts

