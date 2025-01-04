def main( ):

    with open("github.com/f263u/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

    #First Assignment:
    '''
    print(file_contents)
    '''

    #Second Assignment:
    '''
    #words = file_contents.split()
    #print(len(words))
    '''

    #Third Assignment:
    '''
    alphabet = {}
    file_contents = file_contents.lower()
    for character in file_contents:
        if not character in alphabet:
            alphabet[character] = 1
        else: 
            alphabet[character] += 1
    print(alphabet)
    '''

    #Fourth Assignment
    alphabet = {}
    file_contents = file_contents.lower()
    for character in file_contents:
        if not character in alphabet:
            alphabet[character] = 1
        else: 
            alphabet[character] += 1
    for character in alphabet:
        print(f"The '{character}' character was found {alphabet[character]} times")

if __name__ == "__main__":
    main()