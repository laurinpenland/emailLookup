"""
Author:  Laurin Penland

Course:  CSC 121

Assignment:  Lab Week 11:  Email dictionary with pickling

Description:  Creates and manipulates an email address book according to user input
"""

import pickle
#create output file for pickled email_address_book dictionary
output_file = open('pickled_email.dat', 'wb')

#lookup constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#functions to look up, add, change, and delete entries in the email address book
def create_dictionary(filename, dict_name):
    '''create empty dictionary in which to add names and email addresses
    Parameters: filename -- the name of the file to be opened and read, dict_name -- the desired name of the dictionary
    Returns: dictionary'''

    dict_name = {}
    #open file with names and email addresses in read mode
    try:
        with open(filename, 'r') as fhand:
            #loop through the text file, strip the line, put it in a list, and add it to the email_address_book dictionary
            for line in fhand:
                clean_line = line.rstrip()
                email_entry = clean_line.split(', ')
                dict_name.update({email_entry[0]: email_entry[1]})
    except FileNotFoundError:
        print(f"The file {filename} was not found")
        exit(-1)
    return dict_name

def get_emailaddress(dict_name):
    '''function to ask a user for a name and to look up the name in the dictionary
    Parameters: dict_name -- name of dictionary
    Returns: email address from dictionary
    '''
    name = input("\nWhat is the first and last name of the person you would like to look up?\n")
    address = dict_name.get(name, 'Sorry that name is not in the email address book')
    print(f"\nThe email address for {name} is {address}")

def new_entry(dict_name):
    '''function to add new names and email addresses to the dictionary
    Parameters: dict_name -- name of dictionary
    Returns: none'''
    name = input("\nWhat is the first and last name of the person you would like to add to the email address book?\n")
    if name not in dict_name:
        address = input(f"What is the email address of {name}?\n")
        dict_name.update({name: address})
        print(f"\n{name}, {address} has been added to the email address book")
    else:
        print(f'\nSorry {name} is already in the email address book. Choose menu option 3 if you would like to update the email address.')

def update_address(dict_name):
    '''function to change an existing address
    Parameters: dict_name -- name of the dictionary to updated
    Returns: none'''
    name = input("\nWhose address would you like to change? Please enter the first and last name\n")
    address = input("What is the new address?\n")
    dict_name.update({name: address})
    print(f"\nThanks. The new address for {name} is {address}.")

def delete_email(dict_name):
    '''Function to delete a name and email address from the dictionary
    Parameters: dict_name -- name of dictionary from which to delete_email
    Returns: none'''
    name = input("\nPlease enter the name of the person you would like to delete from the email address book\n")
    if name in dict_name:
        del dict_name[name]
        print(f"\n{name} has been deleted from the email address book.")
    else:
        print(f'\nSorry, I did not find {name} in the email address book.')

def get_menu_choice():
    '''function to create menu choices and receive input from the users
    Parameters: none
    Returns: none'''
    print()
    print('Names and Emails Address Book')
    print('-----------------------------')
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an email address')
    print('4. Delete a name and email address')
    print('5. Quit the program\n')

    #get the user's choice
    choice = int(input('Enter your choice: '))

    #validate the choice
    while choice < LOOK_UP or choice > QUIT:
        chioce = int(input('Enter a valid choice: '))

    #return the user's choice
    return choice

def main():
    '''main function process the user's menu choices, call the relevant functions, and pickle the email address book
    Parameters: none
    Returns: none'''

    #call the create_dictionary function
    email_address_book = create_dictionary('week12_data1.txt', 'email_address_book')

    #initialize variable for the user's choice
    choice = 0

    #present user with menu unless they choose to quit
    while choice != QUIT:
        #get the user's choice
        choice = get_menu_choice()

        #process the choice by calling relevant functions
        if choice == LOOK_UP:
            get_emailaddress(email_address_book)
        elif choice == ADD:
            new_entry(email_address_book)
        elif choice == CHANGE:
            update_address(email_address_book)
        elif choice == DELETE:
            delete_email(email_address_book)

    #pickle, unpickle, and print the email address dictionary
    pickle.dump(email_address_book, output_file)
    output_file.close()

    input_file = open('pickled_email.dat', 'rb')
    unpickled_emails = pickle.load(input_file)
    print(unpickled_emails)
    input_file.close()

if __name__ == '__main__':
    main()
