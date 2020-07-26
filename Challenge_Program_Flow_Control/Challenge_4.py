# WAP to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5
# Zero is divisible by every number, so it should not appear in the output


# # without continue command
# for i in range(0, 20):
#     if i % 3 != 0 or i % 5 != 0:
#         print(i)


# with continue command
for i in range(0, 20):
    if i % 3 == 0 or i % 5 == 0:\
        continue
    print(i)
