SimplyGetMongo
==============

A simple Tornado webServer (python) which handles GET requests, returning results from a mongoDB. The server returns the data as javascript friendly json-array (see example below).

The base service is modeled from "Introduction to Tornado" O'Reilly book.  (http://my.safaribooksonline.com/9781449312787/id2923693#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE0NDkzMTI3ODclMkZpZDI5MjM2OTMmcXVlcnk9)


The current version simply returns the entire collection. Once the service is running, simply go to a web browser and type in:   localhost:8000/noQuery

There is a comment in the code where you can insert some if statements to handle unique queries from the url GET request.

Please contribute to this repository.


#####################################################
## How to get up and running
1) you need to have the tornado python module.
			To download:     pip install tornado
2) open 'SimplyGetMongo-server.py'
3) change the pymongo.Connection parameters if you're not using a local mongo instance
4) update the database name to your desired database name on code-line 27 and database collection name on line 47
5) update the query handler if you want anything fancy
6) save the file
7) load a terminal, go to the file directory and type:  python SimplyGetMongo-server.py
8) go to a web browser and type in:  localhost:8000/noQuery










Here is an example of a json-array that is returned by the http request:

[
    {
        "geometry": {
            "type": "Point",
            "coordinates": [
                -122.846401,
                45.367027
            ]
        },
        "loc_id": 88058,
        "type": "Feature",
        "properties": {
            "levels": [
                "2",
                "DCFAST"
            ],
            "name": "Shari's Restaurant & Pies - Sherwood",
            "portCount": 3
        }
    }
]
