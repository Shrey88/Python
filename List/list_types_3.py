# defining list inside list
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
# print(numbers)


# to print the contents of the list inside list
for number_set in numbers:
    print(number_set)
    for values in number_set:
        print(values)
