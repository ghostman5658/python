
class Restaurant:

    def __init__(place, name, footyp):
        place.name = name
        place.footyp = footyp
        place.number_served = 0

    def open(place):
        print(f"{place.name} is now open.")

    def describe(place): 
        print(f"{place.name} has {place.footyp} food.")

    def set_number_served(place):
        number = input("How many people were served? ")
        place.number_served = number 
        print(number)

    def set_number_served2(place, num): 
        place.number_served = num
        print(place.number_served)

    def set_number_served3(place, num):
        place.number_served = num
        return place.number_served

    def increment_number_served(place, num):
        place.number_served += num
        print(f"The new amount of people served is {place.number_served}")


class User:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def getPW(self):
        pw = input(f"{self.fname} what is your password? ")
        return pw  

    def greetUser(self): 
        print(f"Hello {self.fname} {self.lname} you are now in the metaverse!")

    def getUserInfo(self, pw):
        print(f"{self.fname} {self.lname}'s password is {pw}")


b1 = User("Brody", "Turner")
k1 = User("Kyle", "Gotzman")
bpw = b1.getPW()
kpw = k1.getPW()
b1.greetUser() 
k1.greetUser()
b1.getUserInfo(bpw) 
k1.getUserInfo(kpw)

