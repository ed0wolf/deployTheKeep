from flask.ext.testing import TestCase
import unittest
from unittest.mock import patch
import restserver

class FlaskrTestCase(TestCase):

	def create_app(self):
		return restserver.app

	@patch('subprocess.Popen')
	def test_posting_trigger(self, mock_subprocess_call):
		
		response = self.client.post('/trigger', data={'valid-json': 1})

		mock_subprocess_call.assert_called_with(['git', 'pull'], shell=True, cwd='/home/ubuntu/go-code/src/github.com/ed0wolf/comingsoon')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()