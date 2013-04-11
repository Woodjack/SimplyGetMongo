SimplyGetMongo
==============

A simple Tornado webServer (python) which handles GET requests to a local mongoDB. The server returns puts the data into a javascript friendly json array.

The base service is modeled from "Introduction to Tornado" O'Reilly book.  (http://my.safaribooksonline.com/9781449312787/id2923693#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE0NDkzMTI3ODclMkZpZDI5MjM2OTMmcXVlcnk9)


The current version simply returns the entire collection. Once the service is running, simply go to a web browser and type in:   localhost:8000/anything
If you don't put the 'anything', the error handler kicks in, so be sure to include some text there; noting that it doesn't change the outputs currently.

Please contribute to this repository.


## Technical stuff
1) you need to have the tornado python module.
			To download:     pip install tornado

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