#Carmel Norris

def print_menu():   #prints the menu
    print('\nMenu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):   #encodes the password by adding 3 to each digit
    encoded_password = ''
    for i in range(len(password)):
        if int(password[i]) <= 7:
            encoded_password += str(int(password[i]) + 3)
        else:
            encoded_password += str(int(password[i]) - 7)   #subtracts 7 if the digit is too large

    return encoded_password

def decode(password):  #decodes password using a dictionary
    decoded_password = ''
    my_dict = {"4": "1", "5": "2", "6": "3", "7": "4", "8": "5", "9": "6", "1": "7", "2": "8", "3": "9"}
    for element in password:
        decoded_password += my_dict[element]
    return decoded_password

if __name__ == "__main__":
    option = 0    
    while option != 3:    #enters loop and prompts user for option
        print_menu()
        option = int(input('\nPlease enter an option: '))

        if option == 1:
            password = input('Please enter your password to encode: ')
            encode(password)
            print('Your password has been encoded and stored!')

        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
