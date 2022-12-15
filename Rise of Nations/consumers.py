import math
import glob
import os.path
import json
#Consumer Amount and Factory Amount
print("=== INPUT SELECTION ===")
print("1 for population")
print("2 for umits")
print("3 for most recent country file")
inputtype = input("Selection: ")
    
# Determine value input method

# Calculate value from population
if inputtype == "1":
    population = int(input("Input population (to nearest million)"))
    consumeamt = population

# Use manual value from user
elif inputtype == "2":
    consumeamt = float(input("How many Consumer Goods do you need?"))
    population = consumeamt

# Use dictionary element from other python scraper
elif inputtype == "3":
    # Find Nation JSON File
    folder_path = r'C:\Users\Cameron Labes\Documents\Programming\fandom_scraper-master\data'
    file_type = r'\*json'
    files = glob.glob(folder_path + file_type)
    natfile = max(files, key=os.path.getctime)
    print(natfile)
    
    # Extract Dictionary from JSON file
    with open(natfile, "r") as file:
        natdata = json.load(file)
    print(natdata)
    consumeamt = natdata['Consumers Required to Upkeep']
    
    # Conversion for calculation
    consumeamt = float(consumeamt)
    population = consumeamt

# Round variable to account for decimals and add overhead
if consumeamt < 40:
 consumeamt = 40
consumefac = float(round(consumeamt / 40))

#Ingrediant Amount and Factory Amount
fertamt = consumefac * 2.5
motoramt = consumefac * 2.5
elecamt = consumefac * 3
fertfac = math.ceil(fertamt / 12)
motorfac = math.ceil(motoramt / 6)
elecfac = math.ceil(elecamt / 16)
steelamt = motorfac
steelfac = math.ceil(steelamt / 3)

#Resource Amount
phosphateamt = math.ceil(fertfac * 3.5)
titaniumamt = math.ceil(steelfac * 0.2)
ironamt = math.ceil(steelfac * 4)
tugstenamt = math.ceil(motorfac * 2)
goldamt = math.ceil(elecfac * 2)
copperamt = math.ceil(elecfac * 2)

# Print result
print("For %d Million Population, you will need %d Consumer Goods which requires:" % (population, population))
print("=====================Factories=====================")
print("%d consumer factories." % (consumefac))
print("%d ferterlizer factories." % (fertfac))
print("%d motor factories." % (motorfac))
print("%d steel factories." % (steelfac))
print("%d electronic factories." % (elecfac))
print("===================Raw Resources===================")
print("%d units of phosphate." % (phosphateamt))
print("%d units of titanium." % (titaniumamt))
print("%d units of iron." % (ironamt))
print("%d units of tugsten." % (tugstenamt))
print("%d units of gold." % (goldamt))
print("%d units of copper." % (copperamt))
input('Press ENTER to exit')