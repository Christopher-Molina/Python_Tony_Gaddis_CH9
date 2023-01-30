# Starting Out With Python 5th Edition: Chapter 9 - Exercise 4


def main():
    try:
        # Get text file
        file_contents = get_file()

        # Display unique words
        get_words(file_contents)
    except (IOError, IndexError, ValueError, TypeError) as e:
        print(e)


# Function returns a text file
def get_file():
    # Open file for reading
    infile = open('cia_experiment.txt', 'r')

    # Read file contents into a list
    file_contents = infile.read()

    # Close the file
    infile.close()

    # Return file contents
    return file_contents


# Function adds each word to a set
def get_words(file_contents):
    # Split the file contents
    file_contents = file_contents.lower()
    words = file_contents.split()
    words = [word.strip('.,()[]!\n ') for word in words]  # Strip special chars

    # Initialize empty list and add each unique word to the list
    unique = []
    [unique.append(word) for word in words if words.count(word) == 1]

    # Sort
    unique.sort()

    # Display unique
    print(unique)


# Call the main function
if __name__ == '__main__':
    main()
