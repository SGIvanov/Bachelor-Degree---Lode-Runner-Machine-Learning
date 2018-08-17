import unittest

from generate.main import map_elements


class generate_tests(unittest.TestCase):

    def test_map_elements(self):
        self.assertEqual(map_elements([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),'#')
        self.assertEqual(map_elements([0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), '@')
        self.assertEqual(map_elements([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'H')
        self.assertEqual(map_elements([0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), '-')
        self.assertEqual(map_elements([0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 'X')
        self.assertEqual(map_elements([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]), 'S')
        self.assertEqual(map_elements([0, 0, 0, 0, 0, 0, 1, 0, 0, 0]), '$')
        self.assertEqual(map_elements([0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), '0')
        self.assertEqual(map_elements([0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), '&')


if __name__ == '__main__':
    unittest.main()