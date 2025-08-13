myobj = {
    "People": [

        {
            "id": "1",
            "FirstName": "Benjamin",
            "LastName": "Finkel",
            "Email": "ben.finkel@cbtnuggets.com",
            "Active": true
        },

        {
            "id": "2",
            "Name": [
                "Jane",
                "Doe"
            ],
            "Email": "jane.doe@cbtnuggets.com",
            "Active": true,
        },

        {
            id: "3",
            FirstName: "Pat",
            LastName: "Smith",
            Email: "pat.smith@cbtnuggets.com",
            "Active": true
        }

    ]
}

console.log(myobj.People[1].FirstName);
console.log(typeof myobj.People[1].id);
console.log(myobj.People[2].Name[1]);