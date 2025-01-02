import json
from datetime import datetime

class Pet:
    def __init__(self, id, name, species, age, owner_phone):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.owner_phone = owner_phone

    def get_info(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Species": self.species,
            "Age": self.age,
            "Owner Phone": self.owner_phone
        }

class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_occupied = False
        self.check_in_date = None

    def set_status(self, is_occupied, check_in_date=None):
        self.is_occupied = is_occupied
        self.check_in_date = check_in_date if is_occupied else None

class Hotel:
    def __init__(self):
        self.rooms = []
        self.pets = {}

    def add_room(self, number, room_type, price):
        self.rooms.append(Room(number, room_type, price))

    def add_pet(self, pet, room_number):
        room = self.find_room(room_number)
        if room and not room.is_occupied:
            room.set_status(True, datetime.now())
            self.pets[room_number] = pet
            print(f"Pet {pet.name} has been added to room {room_number}.")
        else:
            print(f"Room {room_number} is not available.")

    def check_out(self, room_number):
        room = self.find_room(room_number)
        if room and room.is_occupied:
            check_in_date = room.check_in_date
            days_stayed = (datetime.now() - check_in_date).days + 1
            cost = days_stayed * room.price
            room.set_status(False)
            pet = self.pets.pop(room_number)
            print(f"Pet {pet.name} checked out. Total cost: ${cost:.2f}")
        else:
            print(f"Room {room_number} is not occupied.")

    def find_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None

    def list_rooms(self):
        for room in self.rooms:
            status = "Occupied" if room.is_occupied else "Available"
            print(f"Room {room.number}: {room.room_type}, ${room.price}/day, {status}")

    def find_pet(self, pet_id):
        for room_number, pet in self.pets.items():
            if pet.id == pet_id:
                return pet, room_number
        return None, None

    def search_rooms(self, room_type=None, price_range=None):
        results = []
        for room in self.rooms:
            if (room_type is None or room.room_type == room_type) and \
               (price_range is None or price_range[0] <= room.price <= price_range[1]):
                results.append(room)
        return results

    def save_data(self, filename):
        data = {
            "rooms": [room.__dict__ for room in self.rooms],
            "pets": {room: pet.get_info() for room, pet in self.pets.items()}
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        self.rooms = [Room(**room) for room in data["rooms"]]
        self.pets = {int(room): Pet(**info) for room, info in data["pets"].items()}

def main():
    hotel = Hotel()
    hotel.add_room(101, "Deluxe", 100)
    hotel.add_room(102, "Standard", 50)

    while True:
        print("\nPet Hotel Management System")
        print("1. Add Pet Check-in")
        print("2. Pet Check-out")
        print("3. View All Rooms")
        print("4. Search Pet Information")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter pet ID: ")
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            age = int(input("Enter pet age: "))
            owner_phone = input("Enter owner phone: ")
            room_number = int(input("Enter room number: "))
            pet = Pet(id, name, species, age, owner_phone)
            hotel.add_pet(pet, room_number)
        elif choice == "2":
            room_number = int(input("Enter room number: "))
            hotel.check_out(room_number)
        elif choice == "3":
            hotel.list_rooms()
        elif choice == "4":
            pet_id = input("Enter pet ID: ")
            pet, room_number = hotel.find_pet(pet_id)
            if pet:
                print(f"Pet found in room {room_number}: {pet.get_info()}")
            else:
                print("Pet not found.")
        elif choice == "5":
            filename = input("Enter filename to save data: ")
            hotel.save_data(filename)
        elif choice == "6":
            filename = input("Enter filename to load data: ")
            hotel.load_data(filename)
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
