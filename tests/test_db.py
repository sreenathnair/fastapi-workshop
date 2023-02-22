from unittest.mock import Mock

from app.db import Neo4JDriver


def test_db(mocker):
    mock_driver = Mock()
    mocker.patch("app.db.GraphDatabase.driver", return_value=mock_driver)
    driver = Neo4JDriver()
    assert driver.get_driver() == mock_driver
