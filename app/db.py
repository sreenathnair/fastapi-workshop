import oracledb
from neo4j import GraphDatabase

from app import (
    NEO4J_HOST,
    NEO4J_PASSWORD,
    NEO4J_USER,
    ORACLE_HOST,
    ORACLE_PASSWORD,
    ORACLE_USER,
)


class Neo4JDriver:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        if not self.driver:
            self.driver = GraphDatabase.driver(
                f"bolt://{NEO4J_HOST}", auth=(NEO4J_USER, NEO4J_PASSWORD)
            )
        return self.driver

    def run_query(self, query, **kwargs):
        with self.get_driver().session() as session:
            return list(session.run(query, **kwargs))


class OracleDriver:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if not self.connection:
            self.connection = oracledb.connect(
                user=ORACLE_USER,
                password=ORACLE_PASSWORD,
                dsn=ORACLE_HOST,
            )
        return self.connection

    def run_query(self, query, **kwargs):
        with self.get_connection().cursor() as cursor:
            cursor.execute(query, **kwargs)
            return cursor.fetchall()
