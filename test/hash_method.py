import hashlib

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    interger_list = tuple(integer_list)

    print(hash(interger_list))