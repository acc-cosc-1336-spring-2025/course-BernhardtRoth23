#
import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating
class Test_Config(unittest.TestCase):
    def test_get_options_ratio(self):
        assert get_options_ratio(5,20) == 0.25
        assert get_options_ratio(10,20) == 0.5

    def test_get_faculty_rating(self):
        assert get_faculty_rating(ratio = .91) 
        assert get_faculty_rating(ratio = .85)
        assert get_faculty_rating(ratio = .71)
        assert get_faculty_rating(ratio = .66)
        assert get_faculty_rating(ratio = .59)
         
      