class Lab:
    def __init__(self, name):
        self.name = name
        self.equipment = ["Microscope", "Centrifuge", "Spectrometer", "Pipette", "Incubator"]
        self.supplies = ["Gloves", "Test Tubes", "Slides", "Petri Dishes", "Beakers"]
        self.stuff = ["Abubaker", "Ali", "Ahmad", "Usman"]

    def add_equipment(self, equipment_name):
        self.equipment.append(equipment_name)
        print(f"'{equipment_name}' added to the lab!")

    def use_equipment(self, equipment_name):
        if equipment_name in self.equipment:
            self.equipment.remove(equipment_name)
            print(f"You used '{equipment_name}' from the lab.")
        else:
            print("Sorry, that equipment is not available.")

    def add_supply(self, supply_name):
        self.supplies.append(supply_name)
        print(f"'{supply_name}' added to the lab supplies!")

    def use_supply(self, supply_name):
        if supply_name in self.supplies:
            self.supplies.remove(supply_name)
            print(f"You used '{supply_name}' from the lab supplies.")
        else:
            print("Sorry, that supply is not available.")
    
    def add_staff(self, staff_name):
        self.stuff.append(staff_name)
        print(f"'{staff_name}' added to the lab staff!")

    def remove_staff(self, staff_name):
        if staff_name in self.stuff:
            self.stuff.remove(staff_name)
            print(f"'{staff_name}' has been removed from the lab staff.")
        else:
            print("Sorry, that staff member is not found.")

    def display_inventory(self):
        print("Available equipment in the lab:")
        for equipment in self.equipment:
            print(f"- {equipment}")
        print("Available supplies in the lab:")
        for supply in self.supplies:
            print(f"- {supply}")
        print("Lab staff members:")
        for staff in self.stuff:
            print(f"- {staff}")

def main():
    print("welcome to the Lab!")
    lab = Lab("DHA Branch")

    while True:
        print("\n1.add_equipment\n")
        print("2.use_equipment\n")
        print("3.add_supply\n")
        print("4.use_supply\n")
        print("5.add_staff\n")
        print("6.remove_staff\n")
        print("7.display_inventory\n")
        print("8.Exit\n")

        choice = input("Choice an option: ")


        if choice == '1':
            Equipment_name = input("Enter equipment name: ")
            lab.add_equipment(Equipment_name)

            
        elif choice == '2':
            Equipment_use = input("Enter Used Equipment: ")
            lab.use_equipment(Equipment_use)
        
        elif choice == '3':
            Supply_name = input("Enter Supply name:")
            lab.add_supply(Supply_name)
        
        elif choice == '4':
            Supply_use = input('Enter used supply: ')
            lab.use_supply(Supply_use)

        elif choice == '5':
            Staff_add = input("Enter Staff name: ")
            lab.add_staff(Staff_add)

        elif choice == '6':
            staff_remove = input("Enter staff name")
            lab.remove_staff(staff_remove)

        elif choice == '7':
            lab.display_inventory()
        
        elif choice == '8':
            print("Thanks for visiting the showroom!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
