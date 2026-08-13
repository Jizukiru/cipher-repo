import sys
import argparse


alphabet = "abcdefghijklmnopqrstuvwxyz"
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", dest="key", metavar="KEY" , required=True, help="Sets keyword.")
parser.add_argument("-t", "--text", dest="text", metavar="TEXT", required=True, help="Sets plaintext/ciphertext to be manipulated.")

operationArg = parser.add_mutually_exclusive_group()
operationArg.add_argument("-e", "--encrypt", action="store_true", dest="operation", help="Encypts the plaintext (default flag).", default=True)
operationArg.add_argument("-d", "--decrypt", action="store_false", dest="operation", help="Decrypts the ciphertext.")

args = parser.parse_args()


finalText = ""
for i in range(len(args.text)):
    upper = False
    if args.text[i].isupper():
        upper = True
    letter = args.text[i].lower()
    if letter not in alphabet: #Handles spaces, numbers, punctuation marks and non-English characters
        finalText += args.text[i]
        continue
    
    if args.operation == True: #Encryption
        index = (alphabet.find(letter) + alphabet.find(args.key[i % len(args.key)].lower())) % 26 #Find index of plaintext letter and corresponding index of keyword letter (repeating), add together and mod 26 for shifted letter
    else: #Decryption
        index = (alphabet.find(letter) - alphabet.find(args.key[i % len(args.key)].lower())) % 26 #Find index of ciphertext letter and corresponding index of keyword letter (repeating), subtract key index from ciphertext and mod 26 for plaintext letter


    if upper:
        finalText += alphabet[index].upper()
    else:
        finalText += alphabet[index]

print(finalText)