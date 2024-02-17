from flask import Flask
from flask_restful import Resource, Api


app = Flask("service2")

api = Api(app)

class Service2(Resource):

	def post(self):
		return "POST Method- Gateway Forwarder to Service2 Successfully."
	
	def get(self):
		return "GET Method- Gateway Forwarder to Service2 Successfully."
	
	def put(self):
		return "PUT Method- Gateway Forwarder to Service2 Successfully."

	def patch(self):
		return "PATCH Method- Gateway Forwarder to Service2 Successfully."
	
	def delete(self):
		return "DELETE Method- Gateway Forwarder to Service2 Successfully."
	






api.add_resource(Service2, '/service2')


if __name__ == '__main__':
	app.run(port=5002)
