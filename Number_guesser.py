from random import randint


class Number_Guesser_Game:
    def __init__(self, min_value=0, max_value=100, max_attempts=6) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.attempt = 0
        self.max_attempts = max_attempts
        self.random_value = randint(a = self.min_value, b = self.max_value) # Atgriež nejaušu veselu skaitli diapazonā [a, b], ieskaitot abus beigu punktus.

    def start(self) -> bool:
        print(f"Try to guess the value from {self.min_value} to {self.max_value} from {self.max_attempts} attempts")
        
        # Galvenā cilpa, kas tiks izpildīta, līdz mēģinājumu skaits pārsniedz maksimālo skaitu vai spēlētājs uzminēs pareizi
        while True:
            self.attempt+=1
            # Ja mēģinājumu skaits ir pārsniegts, cikls beidzas
            if self.attempt > self.max_attempts:
                print(f"You exceeded max attempts ({self.max_attempts}), random number was {self.random_value}")
                return False # spēlētājs zaudēja

            # Cilpa, kas tiks izpildīta, līdz tiks saņemta pareizā tipa (int) vērtība
            while True:
                try:
                    provided_value = int(input("Enter a value: "))
                    break
                except ValueError:
                    print(f"Please enter a valid integer value.")
            
            
            # Pamata loģika
            if self.random_value > provided_value:
                print(f"Random value > Provided value ({self.max_attempts-self.attempt} attempts left)")
            elif self.random_value < provided_value:
                print(f"Random value < Provided value ({self.max_attempts-self.attempt} attempts left)")
            else:
                print(f"You guessed right from {self.attempt} attempt.")
                return True # Spēlētājs uzvarēja


# Ja fails darbojas kā galvenais
if __name__ == "__main__":
    game = Number_Guesser_Game()
    game.start()
