import ciphers
from ciphers import caesar_cipher

def main():
    cypher2 =  caesar_cipher.Caesar()
    test_message = "...helloy"

    cypher2.print_translations(test_message)

if __name__=="__main__":
    main()
