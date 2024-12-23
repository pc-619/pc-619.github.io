# "blacklist" list for any digits that cannot be in a binary value
nonBin = ['2', '3', '4', '5', '6', '7', '8', '9']
while True:
    # initialize variables
    temp = 0
    i = 0
    bin = input("Enter a binary number (X to quit): ")
    
    # exit sequence
    if bin.upper() == 'X':
        break

    # check if input is fully numeric (no letters)
    # if not, prompt user to try again
    if bin.isnumeric() == False and bin.upper() != 'X':
        print("Your input isn't a number.")
        continue

    # further check if input is a valid binary value
    if any(ch in nonBin for ch in bin):
        print("Your input isn't a valid binary value.")
        continue

    # if input is valid binary value, go ahead
    else:
        # reverse input digits (this is just for preference
        # and makes it a bit easier to calculate)
        #
        # 123 --> 321
        bin = bin[::-1]

        # for loop converting bin to dec
        for digit in bin:
            # convert current digit into integer
            digit = int(digit)
                  #  1   * 2 ** 0 = 1
                  #  1   * 2 ** 1 = 2
                  #  1   * 2 ** 2 = 4...
            # this is where the actual conversion takes place
            temp += digit * 2 ** i
            print(temp)
            # iterate i for the next digit
            i += 1
    
    

            

            
        

    

