import time

def encrypt(message, shift):
  result = ""
  for char in message:
    if char.isalpha():
      shift_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)  # char.upper is used to convert all the text to capital form, ord is used to change char to ascii number, and chr converts the ascii to alphabet.
      if char.islower():
        result += shift_char.lower()
      else:
        result += shift_char
    else:
      result += char
  return result
#The subtraction of 65 and subsequent addition of 65 is used to ensure that the shift always stays within the range of the English alphabet (i.e., 'A' to 'Z').
#The "% 26" ensures that the shift wraps around from 'Z' (or 'z') back to 'A' (or 'a') if the shift would otherwise result in a character outside the range of the alphabet.

print("Welcome to caesar cipher!")
time.sleep(1)
print("Do you wish to Encrypt or Decrypt?")
time.sleep(1)
print('Enter 1 to "Encrypt" or 2 to "Decrypt".')
choice = int(input("Enter Your Choice: "))
if choice != 1 and choice != 2:
  print("Invalid choice.")
  exit()
time.sleep(1)
message = input("Enter your message: ")
time.sleep(1)
shift = int(input("Enter your Key: "))
time.sleep(1)

if choice == 1:
    result = encrypt(message, shift)
    print(f"Your Encrypted message is {result}.")
elif choice == 2:
    result = encrypt(message, 26-shift) # if the shift value for encryption is shift, the shift value for decryption is 26-shift, which will cancel out the original shift and return the original message.
    print(f"Your Decrypted message is {result}.")
