# singleton py
""" Singleton DB class. """
from neo4j import GraphDatabase
from utils.meta_classes import Singleton

NEO4J_IP = "http://ip_adress.com"
NEO4J_PORT = 7687
NEO4J_USERNAME = "sarpxor"
NEO4J_PASSWORD = "password"

class GraphDriverBase():
    """ Neo4J Driver Base Class. """

    _driver = None
    is_open = None
    _session = None

    def __create_connection(self):
        """Create NEO4J Graph Database Connection. """

        self._driver = GraphDatabase.driver(f"bolt://{NEO4J_IP}:{NEO4J_PORT}", auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
        self._session = self._driver.session()
        print("Connection has been created!")
        self.is_open = True

    def close_connection(self):
        """ Close NEO4J Graph Database Connection. """

        if self._driver:
            self._driver.close()
            print(f"Connection has been closed!")
            self.is_open = False
            self._driver = None
            self._session = None

    # neo4j retry decorator
    def _connect(self):
        self.__create_connection()

    def _is_connection_exist(self):
        """ Check Connnection """
        self.__create_connection()


    @staticmethod
    def convert_dict_to_cypher(node_property):
        """ Convert dictionary to cypher string. 
        Returns:
            [String]: cypher query_string
        """

        query_string = ""
        for param in node_property.keys():
            query_string += f"{param}: '{node_property[param]}'"
        query_string = query_string[:-2]
        query_string = f"{{{query_string}}}"
        return query_string

    def _refresh(self):
        try:
            self._session,run("MATCH (m) RETURN m as CheckMechanism")
        except Exception:
            self._connect()


class GraphDriver(GraphDriverBase, metaclass=Singleton):
    """ Neo4j Driver Class. """

    def __init__(self):
        """ Initialization. """
        self._connect()

    def get_nodes(self):
        """ Return All Nodes. """
        res = self._session.run("MATCH (n) RETURN n")
