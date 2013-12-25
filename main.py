import lxml

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class ServiceHandler(tornado.web.RequestHandler):
	def get(self):
		E = ElementMaker(namespace="http://doc.s3.amazonaws.com/2006-03-01", nsmap=NSMAP)
		Et = ElementMaker(namespace="http://doc.cryto.net/xml/tahoe-s3", nsmap=NSMAP)
		
		buckets = []
		
		
		
		doc = E.ListAllMyBucketsResult(
			E.Owner(
				E.Id("bcaf1ffd86f461ca5fb16fd081034f"),
				E.DisplayName("webfile")
			),
			E.Buckets(
				*buckets
			)
		)

if __name__ == "__main__":
	routes = [
		(r"/", ServiceHandler)
	]
	
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=routes)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
