def swap_case(s):
    newstr = ""
    for words in s:
        for char in words:
            if char.isupper():
                char = char.lower()
            else:
                char = char.upper()

            newstr = newstr + char
    return newstr


if __name__ == '__main__':
    s = "Shreyas"
    result = swap_case(s)
    print(result)
