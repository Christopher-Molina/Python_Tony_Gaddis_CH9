# Starting Out With Python 5th Edition: Chapter 9 - Exercise 3


def main():
    # Get coded alphabet
    codes = get_codes()

    # Open the encrypted text file
    encrypted = get_file_contents()

    # Decrypt the encrypted text file
    decrypt(encrypted, codes)


# Function returns a dictionary that assigns 'codes' to each letter of the alphabet
def get_codes():
    codes = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(',
               'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '`', 'P': '~', 'Q': '{', 'R': '[',
               'S': '}', 'T': ']', 'U': ':', 'V': ';', 'W': '"', 'X': '<', 'Y': '>', 'Z': '0', 'a': '1',
               'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': 'a',
               'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i', 's': 'j',
               't': 'k', 'u': 'l', 'v': 'm', 'w': 'n', 'x': 'o', 'y': 'p', 'z': 'q'}

    return codes


# Function returns an encrypted text file
def get_file_contents():
    # Open file for reading
    infile = open('encrypted.txt', 'r')

    # Read file contents
    file_contents = infile.read().strip('\n')

    # Close the file
    infile.close()

    # Return file contents
    return file_contents


# Decrypt and display the file
def decrypt(encrypted, codes):
    print('Decrypting file...')

    for ch in encrypted:
        if ch not in codes.values() or ch == '.' or ch == ',':
            print(ch, end='')
        else:
            for k, v in codes.items():
                if ch == v and ch != '.':
                    print(k, end='')


# Call the main function
if __name__ == '__main__':
    main()
