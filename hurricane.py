import data

#Codecademy Hurricane Analysis Project
#Started 5/16/2020
#Includes:
    #Converting strings to numbers (floats)
    #Writing & Reading Nested Dictionaries
    
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


