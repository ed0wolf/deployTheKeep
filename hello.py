from flask import Flask, request

app = Flask(__name__)

@app.route("/trigger", methods=['POST'])
def trigger():
	# GitHub triggers calls endpoint with a SHA 
	# Check travis-ci
	# If OK pull master from github
	print("triggered with payload:" + request.data)
	return "Hello World!"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
