from datetime import datetime

class Pet:
    def __init__(self, id, name, species, age, owner_phone): #初始化寵物資訊
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.owner_phone = owner_phone

    def get_info(self): #寵物的資本資訊
        return "編號: {}, 名字: {}, 物種: {}, 年齡: {},主人電話: {}".format(self.id,self.name,self.species,self.age,self.owner_phone)
        

class Room:
    def __init__(self, number, room_type, price):  #初始化寵物旅館物件
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_occupied = False #是否被占用
        self.check_in_date = None #入住日期

    def set_status(self, is_occupied, check_in_date=None): #初始化房間占用狀態及入住時間
        self.is_occupied = is_occupied 
        self.check_in_date = check_in_date if is_occupied else None

class Hotel:
    def __init__(self): #初始化旅館內房間及入住寵物資訊
        self.rooms = []
        self.pets = {}

    def add_room(self, number, room_type, price): #新增可入住的房間的副函式
        self.rooms.append(Room(number, room_type, price))

    def add_pet(self, pet, room_number): #新增入住的寵物
        room = self.find_room(room_number)
        if room and not room.is_occupied:
            room.set_status(True, datetime.now()) #將房間的狀態改為已佔用，並記下入住時間
            self.pets[room_number] = pet #將該房間的寵物改為入住的寵物
            print(f"已將 {pet.name} 加入至房間 {room_number}.")
        else:
            print(f"房號 {room_number} 不可使用")

    def check_out(self, room_number): #將寵物退房的副函式
        room = self.find_room(room_number)
        if room and room.is_occupied:
            check_in_date = room.check_in_date #寵物入住時間
            days_stayed = (datetime.now() - check_in_date).days + 1 #寵物入住天數
            cost = days_stayed * room.price #寵物入住花額
            room.set_status(False) #將房間狀態改回未占用
            pet = self.pets.pop(room_number) #將寵物移除該房間
            print(f" {pet.name} 已退房。 總花額: ${cost:.2f}")
        else:
            print(f"房號 {room_number} 尚未被占用。")

    def find_room(self, room_number): #查找房間
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None

    def list_rooms(self): #列出各個房間的狀態
        for room in self.rooms:
            status = "已被占用" if room.is_occupied else "可入住"
            print(f"房號 {room.number}: {room.room_type}, ${room.price}/天, {status}")

    def find_pet(self, pet_id): #查找寵物
        for room_number, pet in self.pets.items():
            if pet.id == pet_id:
                return pet, room_number
        return None, None

    def search_rooms(self, room_type=None, price_range=None): #檢視各個房間的類型及價格
        results = []
        for room in self.rooms:
            if (room_type is None or room.room_type == room_type) and \
               (price_range is None or price_range[0] <= room.price <= price_range[1]):
                results.append(room)
        return results

def main():
    hotel = Hotel()
    #創建預設房間物件
    hotel.add_room(101, "豪華", 100)
    hotel.add_room(102, "標準", 50)

    while True: #命令列選單
        print("\n寵物旅館管理系統")
        print("1. 新增入住寵物")
        print("2. 寵物退房")
        print("3. 查看所有房間狀態")
        print("4. 查詢特定寵物資訊")
        print("5. 退出系統")
        
        #選單輸入
        choice = input("請輸入你的選擇: ")
        if choice == "1":
            id = input("請輸入寵物編號: ")
            name = input("請輸入寵物名: ")
            species = input("請輸入寵物物種: ")
            age = int(input("請輸入寵物年齡: "))
            owner_phone = input("請輸入主人電話: ")
            room_number = int(input("請輸入房間號碼: "))
            pet = Pet(id, name, species, age, owner_phone)
            hotel.add_pet(pet, room_number)
        elif choice == "2":
            room_number = int(input("請輸入房間號碼: "))
            hotel.check_out(room_number)
        elif choice == "3":
            hotel.list_rooms()
        elif choice == "4":
            pet_id = input("請輸入寵物編號: ")
            pet, room_number = hotel.find_pet(pet_id)
            if pet:
                print(f"該寵物在房號 {room_number} 中: 編號: {id}, 名字: {name}, 物種: {species}, 年齡: {age}, 主人電話: {owner_phone}")
            else:
                print("未找到該寵物。")
        elif choice == "5":
            print("退出系統.")
            break
        else:
            print("無效的選擇。請再試一次。")

if __name__ == "__main__":
    main()
