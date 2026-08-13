This repository aims to create a lot of popular cryptography algorithms and ciphers, mainly for my practice. A list of the ones implemented follows:

## Ceasar's Cipher
An encryption/decryption algorithm that works through shifting the alphabet by a pre-agreed upon offset. The program can use both command line arguments and to get the input, itself, if command line arguments are not provided. To decrypt, input the opposite of the shift.

## Vigenere Cipher
A more competent version of Ceasar's cipher, where the shift value changes depending on the keyword, which repeats in the cases where it's shorter than the plaintext. Uses the argparse Python library to handle command line arguments, and does not function otherwise. If invalid arguments, the automatic help output of the aforementioned library is printed. ***Please note:** the program iterates through the key even if it doesn't shift the character (like a number, space or punctuation mark). This isn't standard for a Vigenere cipher and will be rectified in a later release*
