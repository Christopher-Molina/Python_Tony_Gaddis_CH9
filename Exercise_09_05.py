# Starting Out With Python 5th Edition: Chapter 9 - Exercise 5


def main():
    try:
        # Get text file in reading mode
        file_contents = get_file()

        # Add each word as a key, and frequency as value to a dictionary
        display_frequency(file_contents)
    except (IOError, TypeError, ValueError, IndexError) as e:
        print(e)


# Function returns a text file
def get_file():
    # Open file for reading
    infile = open('cia_experiment.txt', 'r')

    # Read file contents into a variable
    file_contents = infile.read()

    # Close the file
    infile.close()

    # Return file contents
    return file_contents


# Function displays frequency of each word as its key value
def display_frequency(file_contents):
    # Split the file contents
    file_contents = file_contents.lower()
    words = file_contents.split()

    # Calculate frequency of each word and display it in a dictionary
    frequency = {word: words.count(word) for word in words}
    print(frequency)


# Call the main function
if __name__ == '__main__':
    main()
