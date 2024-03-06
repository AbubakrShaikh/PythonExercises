#Pet Simulator Program

#Classes
class Pet():
    pet_name = None
    satisfaction = 0

    def __init__(self, name):
        self.name = name

    def eat(self, food)
        print(self.name + " is eating " + food + "...")
        if food == "carrots"
            self.satisfaction += 10
        elif food == "grains"
            self.satisfaction +=5
        elif food == "grass" 
            self.satisfaction += 1
        print(self.name + " is now " self.satisfaction +  "% satsisfied" )

#Program Start
owner_name = input("What is your name")
print("Welcome " + owner_name)

pet_1 = Pet(input("What is your pet's name"))

