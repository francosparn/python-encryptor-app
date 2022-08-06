from colorama import Fore

# Title and credits
print(Fore.LIGHTRED_EX + '------------------------------------------------------')
print('-                                                    -')
print('-             Encryption Application v1.0            -')
print('-        [ Developed by Franco Sparn © 2022 ]        -')
print('-                                                    -')
print('------------------------------------------------------' + Fore.RESET)

# Options menu text
def options_menu():
    print('==================== Options Menu ====================')
    print('a) Press the letter "E" if you want to encrypt a file.')
    print('b) Press the letter "D" if you want to decrypt a file.')
    print('c) Press the letter "Q" if you want to close the program.')

options_menu()

# Encrypt content
def encrypt(content):
    encrypted_content = ''
    
    for character in content:
        ascii_code = ord(character)
        ascii_code += 1
        encrypted_content += chr(ascii_code)
    
    return encrypted_content
    
# Decrypt content
def decrypt(content):
    decrypt_content = ''
    
    for character in content:
        ascii_code = ord(character)
        ascii_code -= 1
        decrypt_content += chr(ascii_code)
    
    return decrypt_content
    
# Encrypt file
def encrypt_file(file_route):
    # Open file and write content
    filename = open(file_route, 'r')
    
    # Read file content
    content = filename.read()
    
    # Close file
    filename.close()
    
    encrypted_content = encrypt(content)
    
    # Replace content
    filename = open(file_route, 'w')
    filename.write(encrypted_content) 
    filename.close()
    
    # Success message
    print(Fore.GREEN + 'The file has been encrypted successfully' + Fore.RESET)

# Decrypt file
def decrypt_file(file_route):
    # Open file and write content
    filename = open(file_route, 'r')
    
    # Read file content
    content = filename.read()
    
    # Close file
    filename.close()
    
    decrypted_content = decrypt(content)
    
    # Replace content
    filename = open(file_route, 'w')
    filename.write(decrypted_content) 
    filename.close()
    
    # Success message
    print(Fore.GREEN + 'The file has been decrypted successfully' + Fore.RESET)

# Function to continue or exit the program
def continue_or_exit():
    print(Fore.WHITE + 'Do you wish to continue? Press "Y" to continue or "N" to exit.' + Fore.RESET)
    response = input(Fore.YELLOW + 'Writing: ' + Fore.RESET)
    
    # User response validation
    if response.upper() == 'Y':
        options_menu()
        response_user()
    elif response.upper() == 'N':
        print(Fore.CYAN + 'See you soon!' + Fore.RESET)
    else:
        print(Fore.RED + 'The parameter "' + response + '" is not valid.' + Fore.RESET)
        continue_or_exit()
        
# Function to validate the user response    
def response_user(): 
    # User response 
    response = input(Fore.YELLOW + 'Writing: ' + Fore.RESET)
  
    # User response validation
    if response.upper() == 'E':
        print('Enter the path of the file you want to encrypt:')
        file_route = input(Fore.YELLOW + 'Filename: ' + Fore.RESET)
        encrypt_file(file_route)
        continue_or_exit()
    elif response.upper() == 'D':
        print('Enter the path of the file you want to decrypt:')
        file_route = input(Fore.YELLOW + 'Filename: ' + Fore.RESET)
        decrypt_file(file_route)
        continue_or_exit()
    elif response.upper() == 'Q':
        print(Fore.YELLOW + 'The program will close. Thank you for using the app, we look forward to seeing you soon!' + Fore.RESET)
    else:
        print(Fore.RED + 'The parameter "' + response + '" is not valid.' + Fore.RESET)
        continue_or_exit()

response_user()