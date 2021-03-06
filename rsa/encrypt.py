import os
import base64

from helpers import read_key


def main():
    message = input("Enter message: ")
    message_bytes = message.encode('utf-8')
    encoded_message = message_bytes.hex()

    keys = read_key('public')
    n = int(keys['n'])
    e = int(keys['e'])
    
    print('')
    print('n:',n)
    print('e:',e)

    encoded_message = int(encoded_message,16)
    encrypted_message = pow(encoded_message, e, n)
    
    print('\n**********************************')
    print('Encrypted message:')
    print(encrypted_message)
    print('**********************************\n')


if __name__ == "__main__":
    main()