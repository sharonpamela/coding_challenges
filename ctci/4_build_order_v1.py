'''
Build Order: You are given a list of projects and a list of dependencies 
(which is a list of pairs of projects, where the second project is dependent 
on the first project). 
All of a project's dependencies must be built before the project is. 
Find a build order that will allow the projects to be built. If there
is no valid build order, return an error. 
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c 

'''

def find_build_order(projects, dependencies):
    # build a graph
    graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())

def build_graph(projects, dependencies):
    '''
    build a graph adding edge (a,b) if b depends on a.
    Assumes a pair is listed in "build order". 
    The pair (a, b) in dependencies indicates that b
    depends on a and a must be built before b.
    '''
    graph = Graph()

    # turn each project into an object and 
    # create a graph node for each project obj 
    for project in projects:
        graph.get_or_create_node(project)

    # create dependency edges between the project nodes
    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)

    return graph


# Return a list of the projects in a correct build order.
def order_projects(projects):
    build_order = [ None ] * len(projects)

    # Add "roots" (nodes w/o dependencies) to the build_order first.
    # add_node_depepndencies returns the index after the last root 
    # node in build_order
    end_of_list = add_non_dependent(build_order, projects, 0)
    
    to_be_processed = 0
    while to_be_processed < len(build_order):
        current_project_node = build_order[to_be_processed]

        # a circular dep is present if there are no remaining projects
        # with zero dependencies
        if (current_project_node == None): return None

        # Remove current node as a dependency.
        children = current_project_node.get_children()
        for child in children:
            child.decrement_dependencies()

        # Add children that have no one depending on them.
        end_of_list = add_non_dependent(build_order, children, end_of_list)
        to_be_processed += 1

    return build_order


# A helper function to insert projects with zero dependencies into the order
# array, starting at index offset.
def add_non_dependent(order, projects, offset):
    for project in projects:
        if project.get_number_dependencies() == 0:
            order[offset] = project
            offset += 1
    return offset


class Graph(object):
    def __init__(self):
        self.nodes = []
        self.graph_map = {}

    def get_or_create_node(self, name):
        if name not in self.graph_map:
            node = Project(name)
            self.nodes.append(node)
            self.graph_map[name] = node
        return self.graph_map[name]

    def add_edge(self, start_node, end_node):
        start_node = self.get_or_create_node(start_node)
        end_node = self.get_or_create_node(end_node)
        start_node.add_neighbor(end_node)

    def get_nodes(self):
        return self.nodes


class Project(object):
    def __init__(self, name):
        self.children = []
        self.project_map = {}
        self.name = name
        self.dependencies = 0

    def __repr__(self):
        return str(self.project_map)

    def add_neighbor(self, node):
        if node.name not in node.project_map:
            node.children.append(node)
            node.project_map[node.name] = node
            node.increment_dependencies()

    def increment_dependencies(self):
        self.dependencies += 1
    
    def decrement_dependencies(self):
        self.dependencies -= 1

    def get_name(self): 
        return self.name

    def get_children(self):
        return self.children

    def get_number_dependencies(self):
        return self.dependencies

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f','b'),('b','d'),('f','a'),('d','c')]

# graph = build_graph(projects, dependencies)
# print(graph.graph_map)

print(find_build_order(projects, dependencies))