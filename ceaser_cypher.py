def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
              cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
              cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
    return cipher

def decrypt(string, shift):
 
  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher

def Sub_Tech():
    print (''' \t\t\n\n Welcome to Encryption & Decryption using
               subtution Techniques of ceaser cypher ''' );
    print (" 1. Encrypt the Text ");
    print (" 2. Decrypt the Text ");
    option=int(input(" Enter your Option : "));
    if (option == 1):
        print (" \n Ready To Encrypt  ")
        text = input("enter string: ");
        s = int(input("enter shift number: "))
        print("After Encryption: ", encrypt(text, s))
        return Sub_Tech()
    elif(option == 2):
        print (" \n Ready To Decrypt  ")
        text = input("Enter string: ");
        s = int(input("Enter shift number: "))
        print("After Decryption: ", decrypt(text, s))
        return Sub_Tech()
Sub_Tech()
