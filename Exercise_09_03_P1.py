# Starting Out With Python 5th Edition: Chapter 9 - Exercise 3


def main():
    # Get coded alphabet
    codes = get_codes()

    # Open file for reading
    file_contents = get_file()

    # Encrypt the file
    encrypt(file_contents, codes)

    # Display the encrypted file
    display_encrypted_file()


# Function returns a text file
def get_file():
    # Open file for reading
    infile = open('cia_experiment.txt', 'r')

    # Read file contents
    file_contents = infile.read().strip('\n')

    # Close the file
    infile.close()

    # Return the file
    return file_contents


# Function returns a dictionary that assigns 'codes' to each letter of the alphabet
def get_codes():
    codes = {'A': '!','B': '@','C': '#','D': '$','E': '%','F': '^','G': '&','H': '*','I': '(',
             'J': ')','K': '-','L': '_','M': '+','N': '=','O': '`','P': '~','Q': '{','R': '[',
             'S': '}','T': ']','U': ':','V': ';','W': '"','X': '<','Y': '>','Z': '0','a': '1',
             'b': '2','c': '3','d': '4','e': '5','f': '6','g': '7','h': '8','i': '9','j': 'a',
             'k': 'b','l': 'c','m': 'd','n': 'e','o': 'f','p': 'g','q': 'h','r': 'i','s': 'j',
             't': 'k','u': 'l','v': 'm','w': 'n','x': 'o','y': 'p','z': 'q'}

    return codes


# Function encrypts text file contents and writes data to an encrypted text file
def encrypt(file_contents, codes):
    # Open file for writing
    outfile = open('encrypted.txt', 'w', encoding='UTF-8')

    # Decrypt each character
    for ch in file_contents:
        if ch in codes.keys():
            outfile.write(codes[ch])
        else:
            outfile.write(ch)

    # Close the file
    outfile.close()


def display_encrypted_file():
    # Open file for reading
    infile = open('encrypted.txt', 'r')

    # Display file
    print('Encrypting file...\n')
    [print(line.rstrip('\n')) for line in infile]

    # Close the file
    infile.close()


# Call the main function
if __name__ == '__main__':
    main()
