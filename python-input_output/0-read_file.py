#!/usr/bin/python3
def read_file(filename=""):
    #Reads a UTF-8 text file and prints its contents
    with open(filename, 'r', encoding='utf-8') as f:
        #print the content of the dile using .read() function
        print(f.read(), end="")
