from flask import Flask, request
import logging
from logging import FileHandler
import subprocess

app = Flask(__name__)

file_handler = FileHandler("debug.log","a")
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

@app.route("/trigger", methods=['POST'])
def trigger():
	# GitHub triggers calls endpoint with a SHA 
	# Check travis-ci
	# If OK pull master from github
	#subprocess.call(['git', 'pull'], shell = True)
	return "Hello World!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
