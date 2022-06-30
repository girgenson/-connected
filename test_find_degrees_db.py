import unittest
from itertools import permutations

from find_degrees import find_degrees_2

from db import entries


class TestStringMethods(unittest.TestCase):
    def test_end_elements_of_path_are_searched_elements_friend_danja(self):
        path = find_degrees_2('Friend Like Me (End Title)', 'Danja', entries)
        self.assertEqual(('Friend Like Me (End Title)', 'Danja'), (path[0], path[-1]))

    def test_end_elements_of_path_are_searched_elements_id_n_and_id_n_11(self):
        n = min(i['id'] for i in entries)
        start = [i['name'] for i in entries if i['id'] == n][0]
        end = [i['name'] for i in entries if i['id'] == n + 11][0]
        path = find_degrees_2(start, end, entries)
        self.assertEqual((start, end), (path[0], path[-1]))

    def test_there_is_no_path(self):
        self.assertIsNone(find_degrees_2('Jimmy Fallon', 'Victor Vance', entries))

    def test_all_elems_permutations(self):
        all_elems = [i['name'] for i in entries]
        perm_all_elems = permutations(all_elems, 2)
        for perm in perm_all_elems:
            path = find_degrees_2(perm[0], perm[1], entries)
            self.assertEqual((perm[0], perm[1]), (path[0], path[-1]))


if __name__ == '__main__':
    unittest.main()
