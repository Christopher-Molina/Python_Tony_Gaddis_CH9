# Starting Out With Python 5th Edition: Chapter 9 - Exercise 6


def main():
    try:
        # Get two text files
        file_one, file_two = get_files()

        # Get list of words from both files
        file_one_words, file_two_words = get_words(file_one), get_words(file_two)

        # Display unique words in both files
        unique_words(file_one_words, file_two_words)

        # Display words that appear in both files
        words_in_both_files(file_one_words, file_two_words)

        # Display words in first file only
        words_in_first_file_only(file_one_words, file_two_words)

        # Display words in second file only
        words_in_second_file_only(file_one_words, file_two_words)

        # Display words appearing in either first or second file, but not both
        words_in_first_or_second(file_one_words, file_two_words)
    except (IOError, TypeError, ValueError, IndexError) as e:
        print(e)


# Function returns two text files
def get_files():
    # Open file for reading
    infile = open('edison.txt', 'r')

    # Read file contents into a variable
    file_one = infile.read()

    # Repeat
    infile = open('nikola.txt', 'r')

    file_two = infile.read()

    # Close the file
    infile.close()

    # Return the files
    return file_one, file_two


# Function calculates and displays unique words in both files
def unique_words(file_one_words, file_two_words):
    print('Unique Words in File 1:\n', get_unique(file_one_words))
    print('\nUnique Words in File 2:\n', get_unique(file_two_words))


# Function returns a list of unique words
def get_unique(words):
    # Initialize empty list and add each unique word to the list
    unique = []
    [unique.append(word) for word in words if words.count(word) == 1]

    # Sort
    unique.sort()

    # Return the list
    return unique


# Function returns a list of words from a text file
def get_words(file_contents):
    words = file_contents.split()
    words = [word.strip('.,()[]!-;\n ').lower() for word in words]
    words = [word.replace("'s", '') for word in words]
    words = ' '.join(words).split()  # Remove any empty string in the list

    return words


# Function displays words that appear in both files
def words_in_both_files(file_one_words, file_two_words):
    set1, set2 = set(file_one_words), set(file_two_words)
    set3 = set1.intersection(set2)

    print('\nWords Present in Both Files:\n', set3)


# Return a set with each word found in a file
def get_set(file):
    my_set = set([])
    [my_set.update(word) for word in file]

    return my_set


# Function calculates and displays words present in file one only
def words_in_first_file_only(file_one_words, file_two_words):
    set1, set2 = set(file_one_words), set(file_two_words)
    set3 = set1.difference(set2)

    print('\nWords in File 1 Only:\n', set3)


# Function calculates and displays words present in file one only
def words_in_second_file_only(file_one_words, file_two_words):
    set1, set2 = set(file_one_words), set(file_two_words)
    set3 = set2.difference(set1)

    print('\nWords in File 2 Only:\n', set3)


# Function calculates words in either first or second file
def words_in_first_or_second(file_one_words, file_two_words):
    set1, set2 = set(file_one_words), set(file_two_words)
    set3 = set1.symmetric_difference(set2)

    print('\nWords in Either File 1 or File 2 (Not Both):\n', set3)


# Call the main function
if __name__ == '__main__':
    main()
