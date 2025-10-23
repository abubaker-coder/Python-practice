class Showroom:
    def __init__(self, name):
        self.name = name
        self.cars = ["Camry", "Accord", "Model S", "Civic", "Mustang"]

    def add_car(self, car_name):
        self.cars.append(car_name)
        print(f"'{car_name}' added to the showrooom!")
    
    def sell_car(self, car_name):
        if car_name in self.cars:
            self.cars.remove(car_name)
            print(f"You sold '{car_name}'from the showroom.")
        else:
            print("Sorry, that car is not available.")
    
    def display_cars(self):
        print("Available cars in the showroom:")
        for car in self.cars:
            print(f"- {car}")


def main():
    print("welcome to the car showroom")
    showroom = Showroom("Elite Cars")

    while True:
        print("1. Add Car")
        print("2. Sell Car")
        print("3. Show Available Cars")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            car_name = input("Enter car name:")
            showroom.add_car(car_name)

        elif choice == '2':
            car_name = input("Enter car name:")
            showroom.sell_car(car_name)

        elif choice == '3':
            showroom.display_cars()

        elif choice == '4':
            print("Thanks for visiting the showroom!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()