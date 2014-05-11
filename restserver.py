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
	# Get repo and commit id from request body
	# Check travis-ci
	repoPath='/home/ubuntu/go-code/src/github.com/ed0wolf/comingsoon'
	pull(repoPath)
	return 'pulled '+repoPath

def pull(repoPath):
	subprocess.Popen(['git', 'pull'], cwd=repoPath, shell=True)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
