
if __name__ == '__main__':
    N = int(input())
    dynamic_list = []

    for iCommands in range(N):
        command, *values = input().split()
        input_val = list(map(int, values))

        if command == "insert":
            dynamic_list.insert(input_val[0], input_val[1])
        elif command == "print":
            print(dynamic_list)
        elif command == "remove":
            dynamic_list.remove(input_val[0])
        elif command == "append":
            dynamic_list.append(input_val[0])
        elif command == "sort":
            dynamic_list.sort();
        elif command == "pop":
            dynamic_list.pop()
        elif command == "reverse":
            dynamic_list.reverse()


