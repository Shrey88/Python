# create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# use a for loop to loop "n" times, where n is the number of items inthe list.
# Each time round the loop, use next()on your list to print the next time.
#
# hint: use the len() function rather than counting the number of items in the list.

Names_List = ["Shreyas", "Shruti", "Yeshodhan", "Vilandi", "Jayant", "Anahita"]

Name_Iter = iter(Names_List)

for iCount in range(0, len(Names_List)):
    print(next(Name_Iter))
