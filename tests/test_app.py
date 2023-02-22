from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_graph_mappings(mocker):
    mocker.patch(
        "app.db.Neo4JDriver.run_query",
        return_value=[
            ("1A0S", "1", "1", "100", "1", "100", "A", "A", 0.89),
            ("1A0S", "1", "101", "200", "101", "200", "A", "A", 0.89),
        ],
    )
    response = client.get("/mappings/graph/Q14676")
    assert response.status_code == 200
    assert response.json() == {
        "accession": "Q14676",
        "mappings": [
            {
                "entry_id": "1A0S",
                "entity_id": 1,
                "pdb_start": 1,
                "pdb_end": 100,
                "unp_start": 1,
                "unp_end": 100,
                "struct_asym_id": "A",
                "auth_asym_id": "A",
                "identity": 0.89,
            },
            {
                "entry_id": "1A0S",
                "entity_id": 1,
                "pdb_start": 101,
                "pdb_end": 200,
                "unp_start": 101,
                "unp_end": 200,
                "struct_asym_id": "A",
                "auth_asym_id": "A",
                "identity": 0.89,
            },
        ],
    }


def test_get_oracle_mappings(mocker):
    mocker.patch(
        "app.db.OracleDriver.run_query",
        return_value=[
            ("1A0S", "1", "1", "100", "1", "100", "A", "A", 0.89),
            ("1A0S", "1", "101", "200", "101", "200", "A", "A", 0.89),
        ],
    )
    response = client.get("/mappings/oracle/Q14676")
    assert response.status_code == 200
    assert response.json() == {
        "accession": "Q14676",
        "mappings": [
            {
                "entry_id": "1A0S",
                "entity_id": 1,
                "pdb_start": 1,
                "pdb_end": 100,
                "unp_start": 1,
                "unp_end": 100,
                "struct_asym_id": "A",
                "auth_asym_id": "A",
                "identity": 0.89,
            },
            {
                "entry_id": "1A0S",
                "entity_id": 1,
                "pdb_start": 101,
                "pdb_end": 200,
                "unp_start": 101,
                "unp_end": 200,
                "struct_asym_id": "A",
                "auth_asym_id": "A",
                "identity": 0.89,
            },
        ],
    }
