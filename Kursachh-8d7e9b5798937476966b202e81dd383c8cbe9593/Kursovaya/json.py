import json
filename = "json"
myyfile = open(filename, mode="w",encoding = "Latin-1")

airport = {
    'Name' : 'Sheremetievo',
    'flight' : [
        {
            'aircraft 1':{
                'Name':'aircraft 1',
                'Model':'Airbus A220',
                'Type' : 'type 1',
                'Class' : ['Business','1','2'],
                'point of departure' : 'Sheremetievo' ,
                'destination':'Pulkovo',
                'departure time':'10:00',
                'arrival time':'12:00',
                },
            },
        {    'aircraft 2':{},
         },
        ]


    }
