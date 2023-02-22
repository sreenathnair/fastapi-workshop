import os

NEO4J_HOST = os.environ.get("NEO4J_HOST", "localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "neo4j")

ORACLE_HOST = os.environ.get("ORACLE_HOST", "localhost")
ORACLE_USER = os.environ.get("ORACLE_USER", "oracle")
ORACLE_PASSWORD = os.environ.get("ORACLE_PASSWORD", "oracle")
