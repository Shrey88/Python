def split_and_join(line):
    # write your code here
    words = line.split(" ")
    str = "-".join(words)
    return str


if __name__ == '__main__':
    line = "this is a string"
    result = split_and_join(line)
    print(result)
