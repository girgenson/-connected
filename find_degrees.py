__entries_2 = {
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


def find_degrees(initial_element: int, end_element: int, _database: dict, path: list = []):
    path = path + [initial_element]
    if initial_element == end_element:
        return path
    if initial_element not in _database:
        return None
    for elem in _database[initial_element]['links']:
        if elem not in path:
            newpath = find_degrees(elem, end_element, _database, path)
            if newpath:
                return newpath


print(find_degrees(339, 222, __entries_2))
print(find_degrees(339, 6612, __entries_2))
