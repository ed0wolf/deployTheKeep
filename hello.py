from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def pushTrigger():
	# GitHub triggers calls endpoint with a SHA 
	# Check travis-ci
	# If OK pull master from github
	print(request.method)
	return "Hello World!"

if __name__ == "__main__":
	app.run()
