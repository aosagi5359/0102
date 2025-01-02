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
        return{
            "ID":self.id,
            "Name":self.name,
            "Species":self.species,
            "Age":self.age,
            "Owner Phone":self.owner_phone
        }
        
 
class Room:
    def __init__(self, number, room_type, price):
        self.number= number
        self.room_type = room_type
        self.price = price
        self.ioccupied = False
        self.check_in_date = None
     
    def set_status(self, is_occupied, check_in_date = None):
        self.is_occupied= is_occupied
        self.sheck_in_date = check_in_date if is_occupied else None
 
class Hotel:
    def __init__(self):
        self.room = []
        self.pet= {}
     
    def add_room(self, number, room_type, price):
        room = self.rooms.append(Room(number, room_type, price))
        if room and not room.is_occupied:
            room.set_status = (True(str))
            
        
    def add_pet(self, pet, room_number):
       
     
    def check_out(self, room_number):
        # 處理退房
        pass
 
def main():
    # 主程式與使用者介面
    pass
 
if __name__ == "__main__":
    main()