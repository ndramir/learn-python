import re


my_re = "^((2[0-5]{2}|1?\d{1,2})\.){3}(2[0-5]{2}|1?\d{1,2})$"


def validate(ip):

    if re.search(my_re, ip):
        print("\nYour IP is Valid")

    else:
        print("\nYour IP is Invalid")


if __name__ == "__main__":
    ip_input = input("\nPlease enter your computer IP: ").replace(' ', '')
    validate(ip_input)
    print("\nWe hope that was useful\nThank you for using 🙏🙏🙏\n")
