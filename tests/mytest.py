import unittest

class mytests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(Hello.say('world'), 'world')