from unittest import TestCase
from harfpy import harfbuzz

class HarfpyTest(TestCase):

    def test1(self):
        harfbuzz.get_version()