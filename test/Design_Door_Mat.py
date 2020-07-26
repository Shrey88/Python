"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N*M (N is an odd natural number, and M is N times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

if __name__ == '__main__':

    values = map(int, input().split())
    N, M = tuple(values)

    dash_val = ((M-3) // 2)
    dash = "-"
    design = ".|."
    design_val = 1

    for i in range(N//2):
        print( (dash*dash_val) + (design*design_val) + (dash*dash_val) )
        design_val = design_val + 2
        dash_val = dash_val - 3

    print((dash*((M-7)//2)) + "WELCOME" + (dash*( (M-7)//2) ))

    for i in range((N//2)):
        design_val = design_val - 2
        dash_val = dash_val + 3
        print( (dash*dash_val) + (design*design_val) + (dash*dash_val) )
