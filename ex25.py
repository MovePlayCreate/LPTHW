def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette["color"], "can go")
corvette["run"]()


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