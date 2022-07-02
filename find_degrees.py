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


def find_degrees_2(initial_element: str, end_element: str, _database: list, path: list = []):
    path = path + [initial_element]
    current_id = None
    if initial_element == end_element:
        return path
    for elem in _database:
        extract_name = elem.get('name')
        if initial_element == extract_name:
            current_id = elem['id']
            break

    if current_id is None:
        return None
    current_links = [i['links'] for i in _database if i['name'] == initial_element]

    for elem_id in current_links[0]:
        elem_name = [i['name'] for i in _database if i['id'] == elem_id][0]

        if elem_name not in path:
            newpath = find_degrees_2(elem_name, end_element, _database, path)
            if newpath:
                return newpath
