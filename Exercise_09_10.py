def main():
    try:
        # Get file contents as a list
        lines = get_file()

        # Create a dictionary with words as keys, line numbers as values
        line_numbers = get_dict(lines)

        # Write dictionary to a file sorted by keys
        write(line_numbers)
    except (IOError, IndexError, ValueError, TypeError) as e:
        print(e)


# Function returns a text file's contents
def get_file():
    # Open file for reading
    infile = open('Kennedy.txt', 'r')

    # Read file contents
    lines = infile.readlines()

    # Close the file
    infile.close()

    # Strip the newline character
    for line in range(len(lines)):
        lines[line] = lines[line].rstrip('\n').split()

    # Return the file
    return lines


def get_dict(lines):
    # Initialize an empty dictionary and keep track of line number
    my_dict, line = dict(), 1

    for index in lines:
        for word in list(set(index)):
            if word not in my_dict:
                my_dict[word] = str(line) + ' '
            elif word in my_dict:
                my_dict[word] += str(line) + ' '
        line += 1  # Increment line count after each main iteration

    return remove(my_dict)


# Function right strips the last empty space in each value
def remove(line_numbers):
    for k in line_numbers:
        line_numbers[k] = line_numbers[k].rstrip()
    return line_numbers


# Function writes dictionary to a file sorted by keys
def write(line_numbers):
    # Open file for writing
    outfile = open('Index.txt', 'w')

    for k in sorted(line_numbers.keys()):
        outfile.write(k + ': ')
        for v in line_numbers[k]:
            outfile.write(v)
        outfile.write('\n')

    # Close the file
    outfile.close()


# Call the main function
if __name__ == '__main__':
    main()
