# create a program that takes an IP address entered a the keyboard
# and prints out the number of segments it contains, and the length of each segment.

ipAddress = input("Please enter an IP address : ")
iSegment = 0
iLenSegment = 0

for i in range(0, len(ipAddress)):
    if ipAddress[i] == '.':
        iSegment += 1
        print("Length of each segment : {}".format(iLenSegment))
        iLenSegment = 0
    else:
        iLenSegment += 1
if iSegment >= 0:
    print("Length of each segment : {}".format(iLenSegment))

print("\nTotal No Of Segments : {}".format(iSegment))
