import ciphers
from ciphers import caesar_cipher

def main():
    cypher =  caesar_cipher.Caesar()
    message = "... hello this is a TEST with punctuation; : and with capitals!?#$"
    cypher.print_translations(message)
    
if __name__=="__main__":
    main()
