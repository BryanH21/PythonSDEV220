class Vehicle: 
    def __init__(self, vehicle_type: str):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__ (self, year: int, make: str, model: str, doors, int, roof: str):
        super().__init__("car")
        
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def get_int(prompt: str) -> int:
    while True: 
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")

def get_doors() -> int: 
    while True: 
        doors = get_int("Number of doors (2 or 4): ")
        if doors in (2, 4):
            return doors
        print("Doors must be 2 or 4. ")
        
def get_roof() -> str:
    while True:
        roof = input("Type of roof (solid or sun roof): ").strip().lower()
        if roof in ("solid", "sun roof"):
            return roof
        print("Roof must be 'solid' or 'sun roof'.")
    
def main():
    year = get_int("Year: ")
    make = input("Make: ").strip()
    model = input("Model: ").strip()
    doors = get_doors()
    roof = get_roof()

    car = Automobile(year=year, make=make, model=model, doors=doors, roof=roof)

    print("\nVehicle Information")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")
    
if __name__ == "__main__":
    main()