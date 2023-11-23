import re

IP = input("Enter the IP : ")

structure_errors = 0
number_erros = 0

if re.search("^(\d{1,3}\.){3}\d{1,3}$", IP):
    structure_errors = 0
else:
    structure_errors = 1

if structure_errors == 0:
    number_list = re.split(r"\.", IP)
    for number in number_list:
        if 0 <= int(number) <= 255:
            pass
        else:
            number_erros += 1
    if number_erros == 0:
        print("This is a valid IP") 
    else:
        print("This IP is invalid for Numbers!")
else:
    print("This IP is invalid for Structure!")