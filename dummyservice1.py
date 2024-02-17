from flask import Flask
from flask_restful import Resource, Api


app = Flask("service1")

api = Api(app)

class Service1(Resource):

	def post(self):
		return "POST Method- Gateway Forwarder to Service1 Successfully."
	
	def get(self):
		return "GET Method- Gateway Forwarder to Service1 Successfully."
	
	def put(self):
		return "PUT Method- Gateway Forwarder to Service1 Successfully."

	def patch(self):
		return "PATCH Method- Gateway Forwarder to Service1 Successfully."
	
	def delete(self):
		return "DELETE Method- Gateway Forwarder to Service1 Successfully."
	






api.add_resource(Service1, '/service1')


if __name__ == '__main__':
	app.run(port=5001)
