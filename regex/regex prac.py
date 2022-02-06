"""
Name: frede
Filename: regex prac.py
Date: 8/8/2021
"""
import re


def main():
    with open("sample.txt", "r") as text:
        text_lst = text.readlines()
        for line in text_lst[:5]:
            print(line)
            charaters = "website (?:\w+)"
            match = re.finditer(charaters, line)
            # match = match.span()
            # print(match)
            for i in match:
                print(i)
                print(i.start())

if __name__ == '__main__':
    main()
