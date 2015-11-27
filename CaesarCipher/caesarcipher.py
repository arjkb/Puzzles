# Program to encrypt a string by rotaing a letter k times forward

# AUTHOR	: Arjun Krishna Babu
# DATE		: Thu Nov 26 21:36:57 IST 2015
# OS		: Fedora 23 Workstation

def showLog(variable, label):
    print("LOG: ", label, ": ", variable, " ", ord(variable))

def rotate(character, key):
    old_ascii = ord(character)
    new_ascii = old_ascii

    upperBound = 0
    lowerBound = 0
    
    if character.isupper():
        lowerBound = ord('A')
        upperBound = ord('Z')

    elif character.islower():
        lowerBound = ord('a')
        upperBound = ord('z')


    for i in range(key):
        new_ascii = new_ascii + 1
        if( new_ascii > upperBound ):
                new_ascii = lowerBound

    return chr(new_ascii)

def getCipher(mystring, key):
    cipher = ""
    for character in mystring:
        if character.isalpha():
            cipher = cipher + rotate(character, key)
        else:
            cipher = cipher + character
    return cipher

    
n = int(input())
s = input()
k = int(input())

# print(" N: ", n)
# print(" S: ", s)
# print(" K: ", k)

print(getCipher(s, k))
