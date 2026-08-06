import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
shiftArg = False
plainArg = False
if len(sys.argv) == 3:
    shift = int(sys.argv[1])
    plaintext = sys.argv[2]
    shiftArg = True
    plainArg = True
elif len(sys.argv) == 2:
    shift = int(sys.argv[1])
    shiftArg = True

if not shiftArg:
    shift = input("Enter shift amount: \n")
if not plainArg:
    plaintext = input("Enter text: \n")


encrypted_text = ""

for i in plaintext:
    upper = False
    if i.isupper():
         upper = True
    elif i == " " or i not in alphabet:
        encrypted_text += i 
        continue
    letter = i.lower()
    index = (alphabet.find(letter) + shift) % 26
    if upper:
        encrypted_text += alphabet[index].upper()
    else:
        encrypted_text += alphabet[index]

print(f"Text, shift of {shift}:\n{encrypted_text}")
