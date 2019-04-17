import unittest
from exercise_args import count_chars


class ExerciseArgsUnittests(unittest.TestCase):

    def test_single_char(self):
        assert count_chars('a', ('a', 5)) == 5

    def test_no_char_definition(self):
        assert count_chars('a', ('d', 1)) == 0

    def test_multiple_def(self):
        assert count_chars('a', ('a', 5), ('a', 1)) == 1

    def test_pass_int(self):
        assert count_chars(1, ('a', 1)) == 0

    def test_diff_tuple_param(self):
        assert count_chars('ab', ('a', 1), 4) == 1

    def test_just_string(self):
        assert count_chars('a') == 0

    def test_pass_empty_param(self):
        assert count_chars('', ('a', 1)) == 0

    def test_negative_value(self):
        assert count_chars('ab', ('a', 5), ('b', -5)) == 0

    def test_diff_value(self):
        assert count_chars('ab', ('a', 1), ('b', 'd')) == 1

if __name__ == '__main__':
    unittest.main()
