from flask.ext.testing import TestCase
import unittest
from unittest.mock import patch
import restserver
import json

class FlaskrTestCase(TestCase):


	def create_app(self):
		return restserver.app


	@patch('subprocess.Popen')
	def test_posting_trigger_for_master(self, mock_subprocess_call):
		repoName = "DestroyTheKeep"
		payload = {
			'ref': 'refs/heads/master',
			'repository': {
				'name': repoName
			}
		}

		response = self.client.post('/trigger', data=json.dumps(payload))

		self.assertEqual(response.status_code, 200)
		mock_subprocess_call.assert_called_with(['git pull --ff-only'], shell=True, cwd='/home/ubuntu/go-code/src/github.com/ed0wolf/'+repoName)


	@patch('subprocess.Popen')
	def test_posting_trigger_for_nonmaster_branch(self, mock_subprocess_call):
		payload = {
			'ref': 'refs/heads/not-master'
		}

		response = self.client.post('/trigger', data=json.dumps(payload))

		self.assertEqual(response.status_code, 200)
		assert not mock_subprocess_call.called, 'should not have pulled changes'


if __name__ == '__main__':
	unittest.main()