"""
DFS in Python


          A

        /   \    \

      B    C    D

            /       /

           F      E



"""

class Tree(object):

    def __init__(self, name='root', children=None):

        self.name = name

        self.children = []



        if children is not None:

            for child in children:

                self.add_child(child)



    def __repr__(self):

        return self.name



    def add_child(self, node):

        assert isinstance(node, Tree)

        self.children.append(node)





tree = Tree('A', [Tree('B'),

                      Tree('C', [Tree('F')]),

                      Tree('D', [Tree('E')])])





def DFS(tree, node):

    print(tree)



    if tree.name == node:

        print(f'found node: {node} in {tree}')

        return tree



    for child in tree.children:

        print(child)



        if child.name == node:

            print(f'found node: {node} in {child}')

            return child



        if child.children:

            print(f'attempt searching {child} for {node}')

            match = DFS(child, node)



            if match:

                print(match)

                return match

result = DFS(tree, 'E')

print("Result:",result)

#############################################################################

"""
DFS with Stack and Adjacency Metrix
"""

def dfs_iterative(graph, start):

    stack, path = [start], []



    while stack:

        vertex = stack.pop()

        if vertex in path:

            continue

        path.append(vertex)

        for neighbor in graph[vertex]:

            stack.append(neighbor)



    return path





adjacency_matrix = {1: [2, 3], 2: [4, 5],

                    3: [5], 4: [6], 5: [6],

                    6: [7], 7: []}



print(dfs_iterative(adjacency_matrix, 1))