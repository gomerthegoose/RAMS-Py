import json

content=[
    {
        "UserID" : 3,
        "StaffID" : 3,
        "Username": "xvu",
        "Password": "sdvv"
    },
    {
        "UserID" : 4,
        "StaffID": 4,
        "Username": "ddd",
        "Password": "ddd"
    }
  ]

for item in content:
    print("Name: {}\nEmail: {}\nID: {}\n".format(item['UserID'],item['StaffID'],item['Username']))