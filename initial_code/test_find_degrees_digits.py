import unittest

from flask_app.find_degrees import find_degrees


class TestStringMethods(unittest.TestCase):
    database_1 = {
        228: {'name': 'dvadva8', 'links': {339, 4410}},
        339: {'name': 'tritri9', 'links': {228, 441000}},
        4410: {'name': 'chetire410', 'links': {228, 5511}},
        5511: {'name': 'pyat511', 'links': {4410, 6612}},
        6612: {'name': 'pyat511', 'links': {5511}},
    }

    database_2 = {
        339: {'links': {228, 4410, 5511, 6612}},
        228: {'links': {7713, 8814, 9981, 339}},
        4410: {'links': {339}},
        5511: {'links': {339}},
        6612: {'links': {339}},
        7713: {'links': {1234, 121, 222, 228}},
        1234: {'links': {7713}},
        121: {'links': {7713}},
        222: {'links': {7713}},
        8814: {'links': {228}},
        9981: {'links': {228}},
    }

    def test_output_339_6612(self, _database=database_2):
        self.assertEqual([339, 6612], find_degrees(339, 6612, _database))

    def test_path_len_339_6612(self, _database=database_2):
        self.assertEqual(2, len(find_degrees(339, 6612, _database)))

    def test_output_339_228(self, _database=database_2):
        self.assertEqual([339, 228], find_degrees(339, 228, _database))

    def test_path_len_339_228(self, _database=database_2):
        self.assertEqual(2, len(find_degrees(339, 228, _database)))

    def test_output_339_121(self, _database=database_2):
        self.assertEqual([339, 228, 7713, 121], find_degrees(339, 121, _database))

    def test_path_len_339_121(self, _database=database_2):
        self.assertEqual(4, len(find_degrees(339, 121, _database)))

    # same_element

    def test_output_same_element(self, _database=database_2):
        self.assertEqual([339], find_degrees(339, 339, _database))

    def test_path_len_same_element(self, _database=database_2):
        self.assertEqual(1, len(find_degrees(339, 339, _database)))


if __name__ == '__main__':
    unittest.main()
