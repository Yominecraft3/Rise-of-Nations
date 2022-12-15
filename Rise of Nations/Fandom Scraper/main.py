# Import Packages
import requests
from bs4 import BeautifulSoup
import json
import time
# User Input of Selection
selection = int(input("Please select 1 for individual nation and 2 for all nations: "))
# Specific Nation Selection
if selection == 1:
    # Setup Lists and Dictionary
    label_output = []
    value_output = []
    output = {
    }
    nation = str(input("Input Nation: "))
    nation = nation.replace(' ', '_')
    url = "https://ronroblox.fandom.com/wiki/" + nation
    print(nation)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for label in soup.find_all(class_="pi-data-label"):
        label = (label.text)
        print(label)
        label_output.append(label)
    for value in soup.find_all(class_="pi-data-value"):
        value = (value.text)
        print(value)
        value_output.append(value)
    print(label_output)
    print(value_output)
    label_output.insert(0, 'Country')
    value_output.insert(0, nation)
    output = dict(zip(label_output, value_output))
    print(output)
    jsonfile = json.dumps(output)
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    f = open('fandom_scraper-master/data/nationout'+moment+'.json',"w")
    f.write(jsonfile)
    f.close()
elif selection == 2:
    # All Nations Grab - Collects nation strings from file
    natfile = open("fandom_scraper-master/nations.txt", "r")
    data = natfile.read()
    nations = data.split("\n")
    natfile.close()
    num = 1
    # Setup variables for external full dictionary
    metaoutput = {
    }
    metaoutint = 1
    for nation in nations:
        # Setup lists and sub-dictionary
        label_output = []
        value_output = []
        output = {
        }
        # Setup of parser
        url = "https://ronroblox.fandom.com/wiki/" + nation
        print(nation)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # Strip HTML tags
        for label in soup.find_all(class_="pi-data-label"):
            label = (label.text)
            print(label)
            label_output.append(label)
        for value in soup.find_all(class_="pi-data-value"):
            value = (value.text)
            print(value)
            value_output.append(value)
        # Organize into sub-dictionary
        label_output.insert(0,'Country')
        value_output.insert(0, nation)
        output = dict(zip(label_output, value_output))
        print(output)
        # Dump sub-dictionary to json file
        jsonfile = json.dumps(output)
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        f = open('fandom_scraper-master/data/nationout'+moment+'.json',"w")
        f.write(jsonfile)
        f.close()
        time.sleep(1)
        # Dump sub-dictionary into meta-dictionary
        metaoutput[metaoutint] = output
        metaoutint = metaoutint + 1
    print(metaoutput)




