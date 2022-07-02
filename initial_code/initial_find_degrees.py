def initial_find_degrees(initial_element: int, end_element: int, _database: dict, path: list = []):
    path = path + [initial_element]
    if initial_element == end_element:
        return path
    if initial_element not in _database:
        return None
    for elem in _database[initial_element]['links']:
        if elem not in path:
            newpath = initial_find_degrees(elem, end_element, _database, path)
            if newpath:
                return newpath
