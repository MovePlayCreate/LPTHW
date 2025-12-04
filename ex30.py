#animals
people = 20
cats = 30
dogs = 15
turtles = 17
octopus = 9
sharks = 7
rays = 11
dolphins = 9
shrimp = 17
anemone = 9


if turtles > octopus:
    print("Turtle power!")

if turtles + octopus > people:
    print("Under the sea!")

if sharks > 0:
    print("Keep your eyes peeled I want to see that!")

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5
people += 3

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
    print("Not really. And they are!")
    
cats += 6
sharks += 4

if cats > dogs:
    print("Oh no! I'm a dog person overrun with cats!")
if dogs > cats:
    print("It's a dog eat dog world out there!")
    
# taking inventory 
print(f"Cats: {cats}")
print(f"Dogs: {dogs}")
print(f"People: {people}")
print(f"Turtles: {turtles}")

print(f"Total animals equals {cats + dogs + people + turtles}")
