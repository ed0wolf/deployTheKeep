from flask.ext.testing import TestCase
import unittest
import restserver

class FlaskrTestCase(TestCase):

	def create_app(self):
		return restserver.app

	@
	def test_posting_trigger(self):
		response = self.client.post('/trigger', data={'valid-json': 1})
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()