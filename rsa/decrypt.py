import os
import sys
import base64

from helpers import read_key


def main():
    cipher_text = input("Enter cipher text: ")

    keys = read_key('private')
    n = int(keys['n'])
    d = int(keys['d'])

    print('')
    print('n:',n)
    print('d:',d)
    print('')

    decrypted_int = pow(int(cipher_text), d, n)

    decrypted_text = decrypted_int.to_bytes(((decrypted_int.bit_length() + 7) // 8),"big").hex()
    decrypted_text = bytes.fromhex(str(decrypted_text))
    decrypted_message = decrypted_text.decode('utf-8')

    print('\n**********************************')
    print('Decrypted message:')
    print(decrypted_message)
    print('**********************************\n')


if __name__ == "__main__":
    main()