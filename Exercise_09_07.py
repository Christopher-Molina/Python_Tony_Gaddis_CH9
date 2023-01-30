# Starting Out With Python 5th Edition: Chapter 9 - Exercise 7


def main():
    try:
        # Get file
        winners = get_file()

        # Create a dictionary with times won per team as values
        wins = get_wins(winners)

        # Create a dictionary with the team that won during a year as values
        year_winners = get_year_winners(winners)

        # Prompt user for year in the range 1903-2009
        prompt(wins, year_winners)
    except (IOError, TypeError, IndexError, ValueError) as e:
        print(e)


# Function returns a text file
def get_file():
    # Open file for reading
    infile = open('WorldSeriesWinners.txt', 'r')

    # Read file contents into a list
    file_contents = infile.readlines()

    # Close the file
    infile.close()

    # Strip the newline character
    for line in range(len(file_contents)):
        file_contents[line] = file_contents[line].rstrip('\n')

    # Return the file contents
    return file_contents


# Function returns a dict with times won per team as values
def get_wins(winners):
    return {k: winners.count(k) for k in winners}


# Function returns dict with year winner as values
def get_year_winners(winners):
    return {k: v for k, v in enumerate(winners, start=1903)}


# Prompt user for a year in the range 1903-2009
def prompt(wins, year_winners):
    year = int(input('Enter a year in the range 1903-2009 inclusive: '))

    # Input validation
    while year < 1903 or year > 2009:
        year = input('ERROR: Enter a valid year in the range 1903-2009 inclusive, try again: ')

    if year != 1904 and year != 1994:
        print(f'World Series Winner in {year}: {year_winners[int(year)]}')
        print(f'{year_winners[int(year)]} Wins: {wins[year_winners[int(year)]]}')
    else:
        print(f'World Series Not Played in {year}')


# Call the main function
if __name__ == '__main__':
    main()
