graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}


def find_path(_graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in _graph:
        return None
    for node in _graph[start]:
        if node not in path:
            newpath = find_path(_graph, node, end, path)
            if newpath:
                return newpath
    return None


print(find_path(graph, 'A', 'D'))

