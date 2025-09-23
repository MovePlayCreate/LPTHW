people = 20
cats = 30
dogs = 15
turtles = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
    
cats += 5

# I expect this line will print
if cats > dogs:
    print("Oh no! I'm a dog person overrun with cats!")
if dogs > cats:
    print("It's a dog eat dog world out there!")
    
print(f"Cats : {cats}")
print(f"Dogs : {dogs}")
print(f"People : {people}")