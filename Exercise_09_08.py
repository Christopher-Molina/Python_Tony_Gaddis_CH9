# Starting Out With Python 5th Edition: Chapter 9 - Exercise 8
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
UNPICKLE = 5
EXIT = 6


# Main function
def main():
    try:
        # Open a file for appending in binary
        outfile = open('emails.dat', 'ab')

        # Create an empty dictionary
        emails = dict()

        # Create a variable to use as a flag
        flag = True
        while flag:
            # Get choice from user
            choice = get_choice()

            if choice == LOOK_UP:
                search(emails)
            elif choice == ADD:
                add(emails)
            elif choice == CHANGE:
                change(emails)
            elif choice == DELETE:
                delete(emails)
            elif choice == UNPICKLE:
                unpickle_obj()
            elif choice == EXIT:
                flag = False

        # Pickle the object
        pickle.dump(emails, outfile)

        # Close the file
        outfile.close()
    except (IOError, EOFError, TypeError, KeyError, AttributeError, ValueError) as e:
        print(e)


# Function returns a choice from the user
def get_choice():
    # Display menu
    print('Menu:')
    print('1. Look up an email address.')
    print('2. Add a new name and email address.')
    print('3. Change existing email address.')
    print('4. Delete existing name and email address.')
    print('5. Unpickle')
    print('6. Exit')

    # Prompt user for choice
    return input_validation()


# Function allows user to search for a name and email
def search(emails):
    # Prompt user for the name to search for
    name = input('Enter a name: ').lower()
    print(emails.get(name, 'Not found'))
    print()


# Function prompts user to enter person data in a dictionary
def add(emails):
    # Prompt for name and email
    name = input('Enter a name: ').lower()
    email = input('Enter an email: ')
    print()

    # If email doesn't exist, add it
    if name not in emails:
        emails[name] = email
    else:
        print('That entry already exists.\n')


# Function allows user to change an email address
def change(emails):
    # Prompt user for name
    name = input('Enter a name: ').lower()
    print()

    if name in emails:
        # Get a new email
        email = input('Enter a new email address: ')
        emails[name] = email  # Update the entry
        print()
    else:
        print('Entry not found.\n')


# Function allows user to delete an email
def delete(emails):
    # Prompt user for name
    name = input('Enter a name: ').lower()
    print()

    # If name is found delete the entry
    if name in emails:
        del emails[name]
    else:
        print('Entry not found.\n')


# Function un-pickles an object and displays its contents
def unpickle_obj():
    # Open file for binary reading
    infile = open('emails.dat', 'rb')

    eof = False
    while not eof:
        try:
            # Unpickle the object
            emails = pickle.load(infile)

            # Print data
            print(emails, '\n')
        except EOFError:
            eof = True

    # Close the file
    infile.close()


# Function validates input from the user
def input_validation():
    # Prompt user for choice
    value = input('\nEnter your choice: ')

    # Validate the input
    while value.isdigit() is False or int(value) < LOOK_UP or int(value) > EXIT:
        value = input('ERROR: Enter a valid choice, try again: ')

    # Return the value
    return int(value)


# Call the main function
if __name__ == '__main__':
    main()
