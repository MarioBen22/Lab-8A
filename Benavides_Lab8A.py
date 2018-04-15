# Mario Benavides
# Status - Complete
# This program reads the file’s contents and determines
# The number of uppercase & lowercase letters.
# The number of digits & whitespace characters in the file.


def main():
        infile = open('text.txt', 'r') # open the file
        data = infile.read() # read the file as a whole
        
        countUpper = 0 # initiate variable
        countLower = 0 # initiate variable
        countDigit = 0 # initiate variable
        countSpace = 0 # initiate variable
        
        for characters in data: 
                if characters.isupper():
                        countUpper += 1 # update variable

                elif characters.islower():
                        countLower += 1 # update variable

                elif characters.isdigit():
                        countDigit += 1 # update variable

                elif characters.isspace():
                        countSpace += 1 # update variable
 
                

        # display the values entered        
        print('Uppercase letters: ', countUpper)
        print('Lowercase letters: ', countLower)
        print('Digits: ', countDigit)
        print('Spaces: ', countSpace)

# call the main function       
main()
