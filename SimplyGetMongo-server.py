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
    def get(self, word):
        #This is the collection.  In this example it's using the geojson collection in the blinkAPI database
        #The self.apllication simply refers to the class variable db above
        coll = self.application.db.geojson
        #creates a mongo cursor to the query results
        #it's necessary NOT to have the '_id' field in the results.  For some reason it crashes if you do include it (beyond my knowledge set)
        mongoResults = coll.find( {}, {"_id":0} )
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



