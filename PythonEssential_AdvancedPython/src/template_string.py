""" *
    *   Template String
    * """

from string import Template


temp_1 = Template("You're watching ${title} by ${author}")  # <-- created a string template
print(type(temp_1))

print(temp_1.substitute(title="Advanced Python", author="Joe Martin" ))  # substituting the values in the template


# you can even use dictionary to substitute the values of template
data = {"author" : "Joe Martin",
        "title" : "Advanced Python"}

print(temp_1.substitute(data))  # <-- providing the dictionary to substitute the values in template