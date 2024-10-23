from unittest import TestCase
from regexp import *


class RegexpTesting(TestCase):
    def test_default(self):
        self.assertTrue(word_is_tandem("blabla"))
        self.assertTrue(word_is_tandem("123123"))
        self.assertFalse(word_is_tandem("blablabl"))
        self.assertFalse(word_is_tandem("Blabla"))

    def test_empty_string(self):
        self.assertFalse(word_is_tandem(""))
        self.assertFalse(word_is_tandem(" "))
