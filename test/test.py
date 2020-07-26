quotes = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for quote in quotes:
    for words in quote:
        for char in words:
            if char.isupper():
                print(char)