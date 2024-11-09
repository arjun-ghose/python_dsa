from src.utils.logger import Logger

logger = Logger('GraphLogger').get_logger()


class Graph:
    def __init__(self) -> None:
        """
        Creates a new Graph with no vertices or edges.
        """
        self.adj_list: dict = {}
        logger.info('Created new Graph successfully')

    def print_graph(self) -> None:
        """Prints out the graph in the class logs."""
        for vertex in self.adj_list:
            logger.info(f'{vertex}: {self.adj_list[vertex]}')

    def add_vertex(self, vertex: any) -> bool:
        """
        Adds a new vertex with no edges.
        :param vertex: The value of the vertex.
        :return: True if the vertex is created successfully, false otherwise.
        """
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            logger.info(f'Added vertex {vertex} successfully')
            return True
        logger.warning(f'Vertex {vertex} already exists')
        return False

    def add_edge(self, v1, v2) -> bool:
        """
        Adds a new edge between two vertices.
        :param v1: The first vertex.
        :param v2: The second vertex.
        :return: True if the edge is added successfully, false otherwise.
        """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            logger.info(f'Created new edge between {v1} and {v2} successfully')
            return True
        logger.warning('Either v1 or v2 does not exist in the graph')
        return False

    def remove_edge(self, v1, v2) -> bool:
        """
        Removes an edge between two vertices.
        :param v1: The first vertex.
        :param v2: The second vertex.
        :return: True if the edge is removed successfully, false otherwise.
        """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            logger.info(f'Removed edge between {v1} and {v2} successfully')
            return True
        logger.warning('Either v1 or v2 does not exist in the graph')
        return False

    def remove_vertex(self, vertex) -> bool:
        """
        Removes the vertex from the edge along with all edges containing that vertex.
        :param vertex: The vertex to be removed.
        :return: True if the vertex is removed successfully, false otherwise.
        """
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            logger.info(f'Removed vertex {vertex} successfully')
            return True
        logger.warning('Vertex does not exist in the graph')
        return False


# Usage
if __name__ == '__main__':
    # Creating empty graph
    my_graph = Graph()

    # Adding vertex
    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')
    my_graph.print_graph()

    # Adding edge
    my_graph.add_edge('A', 'B')
    my_graph.add_edge('B', 'C')
    my_graph.add_edge('C', 'A')
    my_graph.print_graph()

    # Removing edge
    my_graph.remove_edge('A', 'D')
    my_graph.remove_edge('A', 'B')
    my_graph.print_graph()

    # Remove vertex
    my_graph.remove_vertex('C')
    my_graph.print_graph()
