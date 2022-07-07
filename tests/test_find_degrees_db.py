import unittest
from itertools import permutations

from flask_app.find_degrees import find_degrees

from flask_app.db import entries


class TestStringMethods(unittest.TestCase):

    def test_end_elements_of_path_are_searched_elements_friend_danja(self):
        path = find_degrees('Friend Like Me (End Title)', 'Danja', entries)
        self.assertEqual(('Friend Like Me (End Title)', 'Danja'), (path[0], path[-1]))

    def test_end_elements_of_path_are_searched_elements_id_n_and_id_n_11(self):
        n = min(i['id'] for i in entries)
        start = [i['name'] for i in entries if i['id'] == n][0]
        end = [i['name'] for i in entries if i['id'] == n + 11][0]
        path = find_degrees(start, end, entries)
        self.assertEqual((start, end), (path[0], path[-1]))

    def test_there_is_no_path(self):
        self.assertIsNone(find_degrees('Jimmy Fallon', 'Victor Vance', entries))

    def test_all_elems_permutations(self):
        all_elems = [i['name'] for i in entries]
        perm_all_elems = permutations(all_elems, 2)
        for perm in perm_all_elems:
            path = find_degrees(perm[0], perm[1], entries)
            self.assertEqual((perm[0], perm[1]), (path[0], path[-1]))

    def test_same_element(self):
        all_elems = [i['name'] for i in entries]
        for i in all_elems:
            path = find_degrees(i, i, entries)
            self.assertEqual((i, i), (path[0], path[-1]))

    def test_same_element_path_length(self):
        all_elems = [i['name'] for i in entries]
        for i in all_elems:
            path = find_degrees(i, i, entries)
            self.assertEqual(1, len(path))

    def test_first_element_is_digit_not_in_db(self):
        path = find_degrees('213', 'Danja', entries)
        self.assertEqual(None, path)

    def test_first_item_given_different_case(self):
        path = find_degrees('wall-e', 'Danja', entries)
        print('PATTTH:', path)
        self.assertEqual(['WALL-E', 'The_A.V._Club', 'Pink: The Truth About Love', 'Sober_(Pink_song)', 'Danja'], path)

    def test_second_item_given_different_case(self):
        path = find_degrees('WALL-E', 'danja', entries)
        self.assertEqual(['WALL-E', 'The_A.V._Club', 'Pink: The Truth About Love', 'Sober_(Pink_song)', 'Danja'], path)


if __name__ == '__main__':
    unittest.main()
