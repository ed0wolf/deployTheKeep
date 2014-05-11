from flask import Flask, request
import logging
from logging import FileHandler
import subprocess

app = Flask(__name__)

file_handler = FileHandler("debug.log","a")
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

pathToRepos = '/home/ubuntu/go-code/src/github.com/ed0wolf/'

@app.route('/trigger', methods=['POST'])
def trigger():
	# TODO: Check status in travis-ci before pulling
	payload = request.get_json(force=True)

	if(payload['ref'] != 'refs/heads/master'):
		return "non-master push"

	repoPath = pathToRepos+payload['repository']['name']

	pull(repoPath)
	return 'pulled '+repoPath


def pull(repoPath):
	subprocess.Popen(['git pull --ff-only'], cwd=repoPath, shell=True)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
