# Caesar-Cipher
Building a simple caesar cipher using Python.

The basic mechanism of caesar cipher is it works by taking each letter in the message and replacing it with
another letter that is a certain number of places down the alphabet.

![ceaserCipher](https://user-images.githubusercontent.com/57087618/216802729-2d1ef0a5-1f98-4c51-be0b-48ee93aca8e6.png)


The subtraction of 65 and subsequent addition of 65 is used to ensure that the shift always stays within the 
range of the English alphabet (i.e., 'A' to 'Z').
The % 26 ensures that the shift wraps around from 'Z' (or 'z') back to 'A' (or 'a') if the shift would 
otherwise result in a character outside the range of the alphabet.
