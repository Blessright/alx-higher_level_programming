#!/usr/bin/python3


def uppercase(str):
    for i in range(len(str)):
        uni_code = ord(str[i])
        if uni_code >= 97 and uni_code < 123:
            letter = 32
        else:
            letter = 0
            print("{:c}".format(uni_code) - letter, end='')
            print()
