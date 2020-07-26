"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap


def wrap(string, max_width):
    newstring = ""
    for i in range(len(string)//2):
        newstring = newstring + string[0:max_width]
        newstring = newstring + '\n'
        string = string[max_width:] + '\n'
    return newstring


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)