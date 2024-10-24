from unittest import TestCase
from regexp import *


class RegexpTesting(TestCase):
    def test_default(self):
        self.assertTrue(word_is_tandem("blabla", regexp))
        self.assertTrue(word_is_tandem("123123", regexp))
        self.assertFalse(word_is_tandem("blablabl", regexp))
        self.assertFalse(word_is_tandem("Blabla", regexp))

    def test_empty_string(self):
        self.assertFalse(word_is_tandem("", regexp))
        self.assertFalse(word_is_tandem(" ", regexp))
        self.assertFalse(word_is_tandem("  ", regexp))

    def test_two_words(self):
        self.assertFalse(word_is_tandem("word word", regexp))
        self.assertFalse(word_is_tandem("word_word", regexp))

    def test_text(self):
        self.assertEqual(find_tandem_words_in_text('''123123 irara  0099
                                                hihi hehe        opaopa
                                                russia russia
                                                hihi hiha''', regexp), ["123123", "hihi", "hehe", "opaopa", "hihi"])

    def test_empty_text(self):
        self.assertEqual(find_tandem_words_in_text('''''', regexp), [])
        self.assertEqual(find_tandem_words_in_text('''   ''', regexp), [])