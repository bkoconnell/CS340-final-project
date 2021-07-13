# Project One Test Script

import argparse
import datetime
import json
import random
import uuid
import string
import sys

from project_one import AnimalShelter

# debugging statement
# print("The value of __name__ is:", repr(__name__))
# print('')


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help="The database username")
    parser.add_argument('password', help="The database password")
    args = parser.parse_args()
    username = args.username
    password = args.password
    
    # debugging statement
    # print(args)
    # print('')

    # instantiate object
    animalShelter = AnimalShelter(username, password)
    
    # create animal_id
    #animal_id = 'A'.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
    #print('Creating animal_id %s' % animal_id)
    animal_id = 'A123456'
    
    # convert json to python dict.  and assign to variable for testing the CREATE functionality
    testCreateFunc = json.loads('{"" : 12345, "age_upon_outcome": "2 years", "animal_id": "A123456", "animal_type": "Cat", "breed": "Ragdoll", "color": "White", "date_of_birth": "2015-05-09", "datetime": "2016-05-09 15:15:00", "monthyear": "2016-05-09T15:15:00", "name": "Ivory", "outcome_subtype": "Partner", "outcome_type": "Transfer", "sex_upon_outcome": "Spade Female", "location_lat": 30.29, "location_long": -97.31, "age_upon_outcome_in_weeks": 52}')
    print(testCreateFunc)
    print('')
        
    # test Create functionality
    if animalShelter.create(testCreateFunc):
        print('Test passed for CREATE functionality.')
        print('%s added successfully' % animal_id)
        print('')
    else:
        print('Test Failed for CREATE functionality.')
        print('')
        
        
    # test Read functionality
    animal = animalShelter.read({"animal_id": animal_id})
    if animal:
        print('Test passed for READ functionality.')
        print('')
    else:
        print('Test Failed for READ functionality.')
        print('')
    
    # test Update functionality
    keyValue = json.loads('{"name":"Ivory"}')
    updateValue = json.loads('{"$set":{"age_upon_outcome": "1 year"}}')
                             
    if animalShelter.update(keyValue, updateValue):
        print('Test passed for UPDATE functionality.')
        print('%s updated successfully' % animal_id)
        print('')
    else:
        print('Test Failed for UPDATE functionality.')
        print('')
    
    
    # test Delete functionality
    if animalShelter.delete(keyValue):
        print('Test passed for DELETE functionality.')
        print('%s removed successfully' % animal_id)
        print('')
    else:
        print('Test Failed for DELETE functionality.')
        print('')
        


# execute main
if __name__ == "__main__":
    main(sys.argv[1:])
    
    
                            
    
    