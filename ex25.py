def run():
    print("VROOM")
    
def check():
    print("pressure")

corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette["color"], "can go")
corvette["run"]()

#added line from Bonaire
print(f"To go {corvette["run"]} better check the tire {check()}) 

def create_car(color, transmission, gas_mileage):
    specs = {
        "color" = color, 
        "transmission" = transmission, 
        "gas mileage" = gas_mileage
}

volkswagen = create_car("black", "auto", 32)
toyota = create_car("red", "manual", 29)

print(volkswagen)
volkswagen["color"] = "silver"
print(volkswagen)
print(toyota)