import json
from encrypter import *
from getpass import getpass

def search_for_unit(unit, dict):
    for _type in dict.keys():
        if unit in dict[_type]:
            return True, _type
    return False, ""

def search_for_unit_unit(unit, out_unit, category, dict):
    for db_unit in dict[category][out_unit]:
        if db_unit == unit:
            return True, dict[category][out_unit][db_unit]
    return False, -1


def add_out_unit(unit, category, dict):
    file_write = open("conversions.json", "w")
    dict[category][unit] = {}
    json.dump(dict, file_write, indent= 4)
    file_write.close()

def add_inner_unit(unit, factor, category, out_unit, dict):
    file_write = open('conversions.json', 'w')
    dict[category][out_unit][unit] = factor
    json.dump(dict, file_write, indent= 4)
    file_write.close()

def add_category(category, dict):
    file_write = open('conversions.json', 'w')
    dict[category] = {}
    json.dump(dict, file_write, indent= 4)
    file_write.close()

def update_all_other_units(unit, category, skip_unit, dict, new= False):
    file_write = open('conversions.json', 'w')
    try:
        if new:
            dict[category][unit] = {}
        for db_unit in dict[category].keys():
            if db_unit == skip_unit or db_unit == unit:
                continue
            while True:
                try:
                    factor = float(input(f'How many {db_unit} equals one {unit}? '))
                    break
                except:
                    print("Sorry, that doesn't make sense.")
                    print()
                    continue
            dict[category][db_unit][unit] = 1 / factor    
            dict[category][unit][db_unit] = factor
            for sub_db_unit in dict[category][db_unit].keys():
                if sub_db_unit == unit:
                    continue
                temp_factor = factor * dict[category][db_unit][sub_db_unit]
                dict[category][sub_db_unit][unit] = 1 / temp_factor
                dict[category][unit][sub_db_unit] = temp_factor
            break
        json.dump(dict, file_write, indent= 4)
    finally:
        file_write.close()

def authenticate(entered_password, actual_password):
    actual_password = decoding_function(actual_password)
    if entered_password == actual_password:
        return True
    return False

def main():
    pwd = "RTH/iLc%|eO.N"

    print('Welcome to the Unit Converter!')

    while True:
        print('What would you like to do?')
        print()
        print('1. Convert a unit')
        print('2. Add a conversion to the database')
        print('3. Add a category to the database')
        print('4. Display current database units')
        print('5. Quit the program')
        print()
        
        try:
            choice = int(input('Please select one of the above choices: '))
            print()
        except:
            print('Please choose one of the valid choices.')
            print()
            continue

        if choice == 1: #Finished
            f = open('conversions.json', "r")
            f.seek(0)
            conv = json.load(f)
            while True:
                start_unit = input('Please type the plural form of the unit you are starting with (~ to exit): ').lower()
                found, category = search_for_unit(start_unit, conv)
                if start_unit == '~': # Exit from this step
                    print()
                    break
                elif found:
                    end_unit = input('What unit would you like to convert to?: ').lower()
                    found2, conv_factor = search_for_unit_unit(end_unit, start_unit, category, conv)
                    if found2:
                        while True:
                            try:
                                start_amount = float(input(f'How many {start_unit} do you have? '))
                                end_amount = start_amount * conv_factor
                                break
                            except:
                                print('Please enter a number.')
                                continue
                        print()
                        print(f'{start_amount} {start_unit} is approximately {end_amount:.6f} {end_unit}')
                        print()
                        break
                    else:
                        print(f'Sorry, {end_unit} was not found in our database.')
                        while True:
                            ans1 = input('Are you sure you typed the unit correctly? (Y or N): ')
                            if ans1.upper() == 'Y':
                                while True:
                                    ans2 = input(f'Would you like to add {end_unit} to the database? (Y or N): ')
                                    if ans2.upper() == 'Y':
                                        try_password = getpass('Please enter administrator password to authenticate: ')
                                        if not authenticate(try_password, pwd):
                                            print('***AUTHENTICATION FAILED***')
                                            print('Nice try idiot.')
                                            f.close()
                                            quit()
                                        print('Thank you for confirming administrator status!')
                                        print()
                                        while True:
                                            try:
                                                factor = float(input(f'How many {start_unit} equals one {end_unit}? '))
                                                factor = 1 / factor
                                                break
                                            except:
                                                print("Sorry, that doesn't make sense.")
                                                print()
                                                continue
                                        add_inner_unit(end_unit, factor, category, start_unit, conv)
                                        add_out_unit(end_unit, category, conv)
                                        add_inner_unit(start_unit, (1 / factor), category, end_unit, conv)
                                        update_all_other_units(end_unit, category, start_unit, conv)
                                        print()
                                        print('Database was successfully updated!')
                                        print()
                                    elif ans2.upper() == 'N':
                                        print()
                                        break
                                    else:
                                        print('Please enter Y or N.')
                                        continue
                                    break
                            elif ans1.upper() == 'N':
                                break
                            else:
                                continue
                            break

                else: # Unit not foud
                    print(f'Sorry, {start_unit} was not found in our database.')
                    while True:
                        ans1 = input('Are you sure you typed the unit correctly? (Y or N): ')
                        if ans1.upper() == 'Y':
                            while True:
                                ans2 = input(f'Would you like to add {start_unit} to the database? (Y or N): ')
                                if ans2.upper() == 'Y':
                                    try_password = getpass('Please enter administrator password to authenticate: ')
                                    if not authenticate(try_password, pwd):
                                        print('***AUTHENTICATION FAILED***')
                                        print('Nice try idiot.')
                                        f.close()
                                        quit()
                                    print('Thank you for confirming administrator status!')
                                    print()
                                    category = input(f'What category is {start_unit}? ').lower()
                                    update_all_other_units(start_unit, category, "", conv, new= True)
                                    print()
                                    print('Database was successfully updated!')
                                    print()
                                elif ans2.upper() == 'N':
                                    print()
                                    break
                                else:
                                    print('Please enter Y or N.')
                                    continue
                                break
                        elif ans1.upper() == 'N':
                            break
                        else:
                            continue
                        break
                f.close()
                break

        elif choice == 2:
            f = open('conversions.json', "r")
            f.seek(0)
            conv = json.load(f)
            try_password = getpass('Please enter administrator password to authenticate: ')
            if not authenticate(try_password, pwd):
                print('***AUTHENTICATION FAILED***')
                print('Nice try idiot.')
                f.close()
                quit()
            print('Thank you for confirming administrator status!')
            print()
            new_unit = input('What unit would you like to add to the database? ').lower()
            category = input('What category does this unit belong to? ').lower()
            if category in conv:
                update_all_other_units(new_unit, category, "", conv, new= True)
                print()
                print('Database was successfully updated!')
                print()
            else:
                while True:
                    add_cat = input((f'Would you like to add {category} as a new category? (Y or N): ')).upper()
                    if add_cat == 'Y':
                        add_category(category, conv)
                        print()
                        print('Database was successfully updated!')
                    elif add_cat == 'N':
                        break
                    else:
                        print('Please enter Y or N.')
                        continue
            f.close()
        elif choice == 3:
            f = open('conversions.json', "r")
            f.seek(0)
            conv = json.load(f)
            try_password = getpass('Please enter administrator password to authenticate: ')
            if not authenticate(try_password, pwd):
                print('***AUTHENTICATION FAILED***')
                print('Nice try idiot.')
                f.close()
                quit()
            print('Thank you for confirming administrator status!')
            print()
            new_cat = input('What category would you like to add to the database? ').lower()
            add_category(new_cat, conv)
            print()
            print('Database was successfully updated!')
            print()
            f.close()
        elif choice == 4:
            f = open('conversions.json', "r")
            f.seek(0)
            conv = json.load(f)
            for category in conv.keys():
                print(category.capitalize())
                for unit in conv[category].keys():
                    print(f'\t{unit.capitalize()}')
            print()
            f.close()
        elif choice == 5:
            print('Thank you for using the Unit Converter!')
            quit()
        else:
            pass
    # end of while loop
# end of main function


if __name__ == "__main__": 
    main()