import pandas

fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'], 
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Per16', ['Moderate', ['Fun', 'Weird']]],
    ['C'. ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

#I would like to turn a list into a pandas database
#testing this code from memory from phone check
data = pandas.list_tocsv(fruit)