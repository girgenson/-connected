def find_name_case_insensitive_in_db(element, db):
    for elem in db:
        if elem['name'].lower() == element.lower():
            return elem['name']


def find_degrees(initial_element: str, end_element: str, _database: list, path: list = []):
    elem_with_correct_case = find_name_case_insensitive_in_db(initial_element, _database)
    path = path + [elem_with_correct_case]
    current_id = None
    if initial_element.lower() == end_element.lower():
        return path
    for elem in _database:
        extract_name = elem.get('name')
        extract_name_lower = extract_name.lower()
        initial_element_lower = initial_element.lower()
        if initial_element_lower == extract_name_lower:
            current_id = elem['id']
            break

    if current_id is None:
        return None
    current_links = [i['links'] for i in _database if i['name'].lower() == initial_element.lower()]
    if current_links:
        for elem_id in current_links[0]:
            elem_name = [i['name'] for i in _database if i['id'] == elem_id][0]

            if elem_name not in path:
                newpath = find_degrees(elem_name, end_element, _database, path)
                if newpath:
                    return newpath
