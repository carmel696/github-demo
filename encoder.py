#Carmel Norris
# test
def print_menu():
    print('\nMenu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):
    encoded_password = ''
    for i in range(len(password)):

        if int(password[i]) <= 7:
            encoded_password += str(int(password[i]) + 3)
        else:
            encoded_password += str(int(password[i]) - 7)

    return encoded_password

def decode(password):
    pass

if __name__ == "__main__":
    option = 0
    while option != 3:
        print_menu()
        option = int(input('\nPlease enter an option: '))

        if option == 1:
            password = input('Please enter your password to encode: ')
            encode(password)
            print('Your password has been encoded and stored!')

        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}')
