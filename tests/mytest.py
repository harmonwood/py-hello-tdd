import unittest
import src.hello

class mytests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(Hello.say('world'), 'world')