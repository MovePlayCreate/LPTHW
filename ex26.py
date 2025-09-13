#check the initialize syntax
class person(name, height, weight):
    self.__init__()
    self.name = name
    self.height = height
    self.weight = weight
    self.attitude = "ambitious"
    
patrick = Person("Patrick",71,188)
kayti = Person("Kayti", 63, 130)

print(patrick.attitude)
kayti.attitude = "curious"
print(kayti.attitude)

# playing with class systems
patrick.weight = 190
patrick.dives = 41

ryan = Person("Ryan", 70, 155)
ryan.height = 71