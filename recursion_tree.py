from os import system
from random import choice
from string import ascii_letters, digits


class Digraph:
    """A simple dynamically grown Directed Graph"""
    def __init__(self):
        """Initializes a Graph object"""
        self.adj_list = []

    def add_node(self):
        """Adds a node to the graph"""
        self.adj_list.append([])

    def num_nodes(self):
        """Returns the number of nodes in the graph"""
        return len(self.adj_list)

    def add_edge(self, i, j):
        """Adds a directed edge between i and j"""
        assert len(self.adj_list) > i and len(self.adj_list) > j
        if j not in self.adj_list[i]:
            self.adj_list[i].append(j)

    def edges(self, i):
        """Returns all the edges node i leads to"""
        return self.adj_list[i]


def test_digraph():
    g = Digraph()
    g.add_node()
    g.add_node()
    g.add_edge(0, 1)
    assert list(g.edges(0)) == [1]
    assert len(g.edges(1)) == 0
    g.add_node()
    g.add_edge(1, 2)
    assert list(g.edges(1)) == [2]
    g.add_edge(0, 2)
    assert sorted(list(g.edges(0))) == [1, 2]
    for i, j in ([0, 3], [3, 0], [3, 3]):
        try:
            g.add_edge(i, j)
        except AssertionError:
            pass
        else:
            err = "Didn't throw error when adding edge with nodes not in graph"
            assert 1 == 0, err


class graph_to_dot:
    """Converts a graph to .dot code"""
    def __init__(self, graph, names=None):
        self.graph = graph
        if names is None:
            names = list(range(graph.num_nodes()))
        self.names = names
        self.generate_code()

    def generate_code(self):
        code = ['Digraph G {']
        for i in range(self.graph.num_nodes()):
            code.append('{0} [label ={1}];'.format(i, self.names[i]))
            for j in self.graph.edges(i):
                code.append('{0} -> {1};'.format(i, j))
        code.append('}')
        self.code = code

    def save_code(self):
        self.code_filename = ''.join([choice(ascii_letters) for _ in range(10)])
        with open(self.code_filename, 'w') as f:
            for line in self.code:
                f.write(line + '\n')

    def display(self):
        self.save_code()
        system('xdot {0}'.format(self.code_filename))
        system('rm {0}'.format(self.code_filename))

    def save(self, outputfile):
        self.save_code()
        system('dot -o{0}.png -Tpng {1}'.format(outputfile, self.code_filename))
        system('rm {0}'.format(self.code_filename))

def test_graph_to_dot():
    g = Digraph()
    g.add_node()
    g.add_node()
    g.add_edge(0, 1)
    g2d = graph_to_dot(g)
    g2d.display()


def get_rep(args, kwargs):
    if len(args) == 1:
        args_rep = str(args[0])
    else:
        args_rep = str(args)
    if len(kwargs) == 0:
        rep = args_rep
    else:
        rep = '{0}, {1}'.format(args_rep, str(kwargs))
    rep = rep.replace('\n', ' ')
    return rep


def get_file_name(func, args, kwargs):
    return ''.join([c if c in ascii_letters + digits else '_' for c in func.__name__ + get_rep(args, kwargs)])

def recursion_tree_dec(func, save_to_file):
    """prints out a recursion tree"""
    info = {'caller': None, 'names': [], 'graph': Digraph()}

    def wrap(*args, **kwargs):
        info['names'].append('"{0}"'.format(get_rep(args, kwargs)))
        info['graph'].add_node()
        current = len(info['names']) - 1
        if not info['caller'] is None:
            info['graph'].add_edge(info['caller'], current)
        caller = info['caller']
        info['caller'] = current
        result = func(*args, **kwargs)
        info['caller'] = caller
        if info['caller'] is None:
            g2d = graph_to_dot(info['graph'], info['names'])
            if save_to_file:
                g2d.save(get_file_name(func, args, kwargs))
            else:
                g2d.display()
            info['caller'] = None
            info['names'] = []
            info['graph'] = Digraph()
        return result
    wrap.__name__ = func.__name__
    return wrap

def recursion_tree(save_to_file=False):
    return lambda func: recursion_tree_dec(func, save_to_file)
