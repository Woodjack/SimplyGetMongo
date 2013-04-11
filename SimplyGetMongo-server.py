## 
##
## http service that runs continously, and serves up a json-array of results from a mongoDB
## see the readme for more information
##

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo

#This is used to produce a properly formated json-array,
from bson.json_util import dumps

#port options for webServer
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

#
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/(\w+)", RequestHandler)]
        #Define your pymongo Connection information here
        #Current is connection to mongo on the local host on port 27017
        mongoConnection = pymongo.Connection("localhost", 27017)
        #this is where you set the database name in mongoDB to use
        self.db = mongoConnection["blinkAPI"]
        tornado.web.Application.__init__(self, handlers, debug=True)



class RequestHandler(tornado.web.RequestHandler):
    def get(self, urlInput):

        #This is the collection.  In this example it's using the geojson collection in the blinkAPI database
        #The self.apllication simply refers to the class variable db above
        coll = self.application.db.geojson

        #change the urlInput from unicode to a python string
        urlInput = str(urlInput)

        #creates a mongo query 'dictionary'
        query = {}

        #if the request is noQuery, then simply query the whole db collection
        if urlInput == "noQuery":
            query = {}


        #here is where you could have other 'elif' statements to handle specific db queries


        mongoResults = coll.find( query, {"_id":0} )

        #check to see if there is anything returned
        if mongoResults:

            #this creates the json-array to be uploaded
            jsonArray = (dumps(mongoResults))

            #this is the line that 'prints' the json-array to the http request response
            self.write(str(jsonArray))

        else:
            self.set_status(404)
            self.write({"error": "word not found"})



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



