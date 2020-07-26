import platform

def main():
    message()

def message():
    print("This is python version {}", format(platform.python_version()))


""" *
    *   this line tells the interpreter to read the entire code before executing anything
    *   this is more like a procedural style of programming.
    * """
if __name__ == '__main__':
    main()