import data

#Codecademy Hurricane Analysis Project
#Started & Completed 5/16/2020
#Includes:
    #Converting strings to numbers (floats)
    #Writing & Reading Nested Dictionaries
    #Generating new dictionaries based on a specific value in another dictionary
    #Finding the max value (of a value) in a dictionary
    
#updates a list of number strings to a list of floats
def new_damages(list):
    new = []
    for damage in list:
        if damage == 'Damages not recorded':
            new.append("Damages not recorded")
        else:
            if 'M' in damage:
                num = damage[:-1]
                num = float(num)
                num *= 1000000
                new.append(num)
            else:
                num = damage[:-1]
                num = float(num)
                num *= 1000000000
                new.append(num)
    return new

#testing        
#print(data.damages)
#print(new_damages(data.damages))

#creates a dictionary from the supplied lists:
#name, month, year, max sustained wind, areas affected, damage, death
def hurricane_dict():
    new_dict = {}
    for num in range(len(data.names)):
        new_dict[data.names[num]] = {}
        new_dict[data.names[num]]['Name'] = data.names[num]
        new_dict[data.names[num]]['Month'] = data.months[num]
        new_dict[data.names[num]]['Year'] = data.years[num]
        new_dict[data.names[num]]['Max Sustained Wind'] = data.max_sustained_winds[num]
        new_dict[data.names[num]]['Areas Affected'] = data.areas_affected[num]
        new_dict[data.names[num]]['Damage'] = data.damages[num]
        new_dict[data.names[num]]['Death'] = data.deaths[num]
    return new_dict
 
#implementing
hurricane_dictionary = hurricane_dict()

#testing
#print(hurricane_dictionary['Cuba I'])
#print(hurricane_dictionary['Carla']['Name'])
#print(hurricane_dictionary['Carla']['Death'])

#generates a new dictionary with years as keys
def year_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        try:
            new_dict[value['Year']].append(value)
        except KeyError:
            new_dict[value['Year']] = []
            new_dict[value['Year']].append(value)
    return new_dict

#implementing    
years_dictionary = year_dict(hurricane_dictionary)

#testing
#print(years_dictionary[1932])

#generates a new dictionary with counts of affected areas
def area_dict(dict):
    new_dict = {}
    for value in dict.values():
        for area in value['Areas Affected']:
            try:
                new_dict[area] += 1
            except KeyError:
                new_dict[area] = 1
    return new_dict

#implementing
areas_dictionary = area_dict(hurricane_dictionary)

#testing
#print(areas_dictionary)

#find and return the max value in a dict
def most_affected(dict):
    largest = None
    place = None
    for key, value in dict.items():
        if not largest or value > largest:
            largest = value
            place = key
    print("The place most affected by hurricanes was {0}, which was hit {1} times.".format(place, largest))
    
#implementing & testing
most_affected(areas_dictionary)
    
#find and return the max value in a dictionary
def most_deaths(dict):
    largest = None
    name = None
    for key, value in dict.items():
        if not largest or value['Death'] > largest:
            largest = value['Death']
            name = key
    print("The hurricane that caused the greatest number of deaths was {0} ({1}).".format(name, largest))

#implementing & testing
most_deaths(hurricane_dictionary)

#judge the hurricanes according to a scale, and add them to a new dictionary based on that scale
def scale(dict):
    #initialize the new dict
    new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    #mort = {0:0, 1:100, 2:500, 3:1000, 4:10000}
    for value in dict.values():
        if value['Death'] > 10000:
            new_dict[5].append(value)
        elif value['Death'] >= 1000:
            new_dict[4].append(value)
        elif value['Death'] >= 500:
            new_dict[3].append(value)
        elif value['Death'] >= 100:
            new_dict[2].append(value)
        elif value['Death'] > 0:
            new_dict[1].append(value)
        else:
            new_dict[0].append(value)
    return new_dict
    
#implementing
mortality_scale = scale(hurricane_dictionary)

#testing
#print(mortality_scale)

#find the hurricane with the highest damage
def most_damage(dict):
    largest = None
    largest_string = None
    name = None
    for key, value in dict.items():
        if value['Damage'] != "Damages not recorded":
            temp = None
            if 'M' in value['Damage']:
                temp = value['Damage']
                temp = float(temp[:-1]) * 1000000
            else:
                temp = value['Damage']
                temp = float(temp[:-1]) * 1000000000
            if not largest or temp > largest:
                largest_string = value['Damage']
                largest = temp
                name = key
    print("The hurricane that caused the greatest damage was {0}, with ${1} of damage.".format(name, largest_string))
    
#implementing and testing
most_damage(hurricane_dictionary)

#generates dictionary based on damage scale
def scale2(dict):
    new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    #scale 0; 100,000,000; 1,000,000,000; 10,000,000,000; 50,000,000,000
    for value in dict.values():
        if value['Damage'] == "Damages not recorded":
            new_dict[0].append(value)
        else:
            if 'M' in value['Damage']:
                temp = value['Damage']
                temp = float(temp[:-1])
                if temp < 100:
                    new_dict[1].append(value)
                else:
                    new_dict[2].append(value)
            else:
                temp = value['Damage']
                temp = float(temp[:-1])
                if temp >= 50:
                    new_dict[5].append(value)
                elif temp >= 10:
                    new_dict[4].append(value)
                else:
                    new_dict[3].append(value)
    return new_dict

#implementing
damage_scale = scale2(hurricane_dictionary)

#testing
#print(damage_scale[2])

    
            
