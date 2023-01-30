# Starting Out With Python 5th Edition: Chapter 9 - Exercise 2
import random


def main():
    # Get states and their capitals
    capitals = get_capitals()

    # Randomly quiz the user
    play_game(capitals)


def get_capitals():
    # Create us states capitals dictionary
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
                'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
                'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
                'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
                'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
                'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
                'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
                'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
                'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
                'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    return capitals


# Function lets user play game until exit
def play_game(capitals):
    # Initialize accumulator variables
    correct = incorrect = 0

    # Set a boolean variable to use as a flag
    flag = True
    while flag:
        # Display random name of a state and prompt user for answer
        state = random.choice(list(capitals))
        answer = input(f'What is {state}\'s capital (0 to exit)? ')

        if answer.lower() == capitals[state].lower():
            correct += 1
            print('Correct!\n')
        elif answer.lower() != capitals[state].lower() and answer != '0':
            incorrect += 1
            print('Incorrect\n')
        elif answer == '0':
            flag = False
    print(f'\nCorrect: {correct}\nIncorrect: {incorrect}')


# Call the main function
if __name__ == '__main__':
    main()
