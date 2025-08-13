import json

jsonstr = """

{
    "People": [
        {
            "id": 1,
            "FirstName": "Benjamin",
            "LastName": "Finkel",
            "Email": "ben.finkel@cbtnuggets.com",
            "Active": true
        },
        {
            "id": 2,
            "Name": {
                "FN": "Jane",
                "LN": "Doe"
            },
            "Email": "jane.doe@cbtnuggets.com",
            "Active": false
        },
        {
            "id": 3,
            "Name": [
                "Jane",
                "Doe"
            ],
            "Email": "pat.smith@cbtnuggets.com",
            "Active": true
        }
    ]
}"""

jsonobj = json.loads(jsonstr)
print(jsonobj)
print(type(jsonobj))

print(jsonobj["People"])
print(type(jsonobj["People"]))

print(jsonobj["People"][1])
print(type(jsonobj["People"][2]))

#Loading out of a file as opposed to string. use load instead of loads

jsonobj = json.load(open('sample.json'))
print(jsonobj['People'])