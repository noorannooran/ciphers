'''caesar_cipher.py: for Caesar cipher encryption and decryption'''
__author__ = "noorannooran"

class Caesar:
    #initialization
    def __init__(self):
        self.letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                       'w', 'x', 'y', 'z']
        self.punctuation = ['.', ',', '?', ';', ':', '!', ' ']
        self.ord_punct = [] #to hold the string and ordinals of punctuation
        self.ord_let = [] #to "" of letters


    #iterates through letters and punctuation lists
    #appends values to ordinals lists
    def ordinal(self):
        for char in self.punctuation:
            self.ord_punct.append([char, ord(char)])
        for char in self.letters:
            self.ord_let.append([char, ord(char)])


    #shifts given text by shift amount, returns shifted text
    def cipher(self, message, shift):
        shifted_text = [] # hold result message
        new_letter = 0
        message = message.lower()

        for char in message:
            if [char, ord(char)] in self.ord_punct:
                shifted_text.append(str(char))
                continue
            elif ord(char)+ shift > 122:
                new_letter = ord(char)-26+shift
                shifted_text.append(str(chr(new_letter)))
                continue
            elif [char, ord(char)] in self.ord_let:
                new_letter = ord(char)+shift
                shifted_text.append(str(chr(new_letter)))
            else:
                shifted_text.append(str(char))
        return shifted_text


    #calls cipher, prints out shifted text
    def print_translations(self, message):
        self.ordinal()
    
        for x in range(1, 26):
            result = ""
            shifted_text = self.cipher(message, x)
            print("Shifted Text: " + str(x))
            for letter in shifted_text:
                result+= letter
            print(result)
            
'''
old non object oriented code
shifted_text = []


def cipher(letters, shift):
    shifted_text = []
    for letter in letters:
        if ord(letter) == 32:
            shifted_text.append(" ")
            continue
        if ord(letter) == 46:
            shifted_text.append(".")
            continue
        if ord(letter) == 44:
            shifted_text.append(",")
            continue
        if ord(letter)+shift >122:
            new_letter = ord(letter)-26+shift
        else:
            new_letter = ord(letter)+shift
        shifted_text.append(str(chr(new_letter)))

    return shifted_text

print("Original shifted message: " + message)

a = 65
z = 90
for x in range(1, 26):
    translated_message = ""
    shifted_text = cipher(message, x)
    print("Shifted Text " + str(x))
    for letter in shifted_text:
        translated_message += letter
    print(translated_message)
'''
