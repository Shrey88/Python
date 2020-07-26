people = [
    ("John Cleese", "cleese@gmail.com"),
    ("Terry Gilliam", "gilliam@gmail.com"),
    ("Eric Idle", ""),
    ("Terry Jones", "jones@gmail.com"),
    ("Graham Chapman", "chapman@gmail.com"),
    ("Michael Palin", "")
]

if all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")