days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

# this is the reuglar iteration
for m in range(len(days)):
    print(m+1, days[m])


# enumerate iteration is easy to read
for i, m in enumerate(days, start=1):
    print(i, m)  # <-- where i is the value assigned to list of values.