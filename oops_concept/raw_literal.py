# =================================================================
# RAW STRING
# when you are working with the escape character, the escape character will come into action
# so in case if you want to treat the escape character like normal character the you need to use r as prefix to string literal
# =================================================================
print("String treated with the escape characters:")
a_string = "this is \na string split\t\tand tabbed"
print("{}\n".format(a_string))

"""
to print the string as is by not treating the escape character.
"""
print("String treated as normal string even though it has escape character:")
raw_string = r"this is \na string split\t\tand tabbed"
print("{}\n".format(raw_string))

"""
this is the other way of entering the escape character (by making use of ascii characters), which not only 
makes the code messy but they cause problems on different operating systems, so if Python didn't provide a 
mechanism for escaping certain characters we have to probably create strings like this.  

one disadvantage of using this ascii character is that, different operating system may use different ascii character 
for \n and \t
"""
print("String to be treated as normal string with the use of ascii character for the escape sequences:")
b_string = "this is " + chr(10) + "a string split" + chr(9)+chr(9) + "and tabbed"
print("{}\n".format(b_string))

"""
so here it is giving some strange character for \f
"""
backslash_string = "this is a backslash \followed by some test"
print("{}\n".format(backslash_string))

"""
by giving 2 backslashes it will retain one backslash
"""
backslash_string = "this is a backslash \\followed by some test"
print("{}\n".format(backslash_string))

"""
so the point of using the raw string literal was introduced to remove the need to double up backslashes in a string.
Python raw string literal does not suppress to escape if the backslash is used as the last character in the string.
so if you see the below string it is giving us the error because it is escaping the double quotes even when sing raw string literal
we need to put the double backslash in there to remove the error. 

so raw string literals are sometimes used to specify file paths in windows,
which used the backslash character rather than a forward slash to separate the directory name, but it is actually not necessary
to do as python takes care of it for us but if you do and your python ends up with a backslash such as C:/ then you need to double 
up that final backslash 
"""
# error_string = r"this string ends with \"
error_string = r"this string ends with \\"