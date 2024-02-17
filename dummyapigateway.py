from flask import Flask, request, jsonify, Response
import requests



app = Flask(__name__)



service1_endpoint = 'http://127.0.0.1:5001'
service2_endpoint = 'http://127.0.0.1:5002'

@app.route('/service1', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def forward_to_service1():
    method = request.method
    # Forward the request to the service and get the response
    if method == 'GET':
        response = requests.get(f"{service1_endpoint}/service1")
    elif method == 'POST':
        response = requests.post(f"{service1_endpoint}/service1", json=request.json)
    elif method == 'PUT':
        response = requests.put(f"{service1_endpoint}/service1", json=request.json)
    elif method == 'PATCH':
        response = requests.patch(f"{service1_endpoint}/service1", json=request.json)
    elif method == 'DELETE':
        response = requests.delete(f"{service1_endpoint}/service1")
    else:
        return jsonify({'error': 'Method not supported'}), 405

    # Create a Flask Response object from the requests Response object
    return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

@app.route('/service2', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def forward_to_service2():
    method = request.method
    # Similar forwarding logic for service2
    if method == 'GET':
        response = requests.get(f"{service2_endpoint}/service2")
    elif method == 'POST':
        response = requests.post(f"{service2_endpoint}/service2", json=request.json)
    elif method == 'PUT':
        response = requests.put(f"{service2_endpoint}/service2", json=request.json)
    elif method == 'PATCH':
        response = requests.patch(f"{service2_endpoint}/service2", json=request.json)
    elif method == 'DELETE':
        response = requests.delete(f"{service2_endpoint}/service2")
    else:
        return jsonify({'error': 'Method not supported'}), 405

    return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])




if __name__ == '__main__':
	app.run(debug=True, port=5000)