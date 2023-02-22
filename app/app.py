from fastapi import FastAPI, Path
from starlette import status

from app.db import Neo4JDriver, OracleDriver
from app.model import HelloModel, Mapping, MappingResponse

app = FastAPI()
neo4j_driver = Neo4JDriver()
oracle_driver = OracleDriver()


@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=HelloModel,
)
def read_root():
    return HelloModel(message="Hello World")


@app.get(
    "/mappings/graph/{accession}",
    response_model=MappingResponse,
)
def get_graph_mappings(
    accession=Path(
        ...,
        title="UniProt accession",
        description="A UniProt accession",
        example="Q14676",
    )
):

    query = """
    MATCH
        (uniprot:UniProt {ACCESSION:$accession})<-[rel:HAS_UNIPROT_SEGMENT]-
        (entity:Entity)<-[:HAS_ENTITY]-(entry:Entry)
    RETURN
        entry.ID, entity.ID, rel.PDB_START, rel.PDB_END, rel.UNP_START,
        rel.UNP_END, rel.STRUCT_ASYM_ID, rel.AUTH_ASYM_ID, toFloat(rel.IDENTITY)
    ORDER BY
        toInteger(rel.PDB_START)
    """
    mappings = []

    for record in neo4j_driver.run_query(query, accession=accession):
        (
            entry_id,
            entity_id,
            pdb_start,
            pdb_end,
            unp_start,
            unp_end,
            struct_asym_id,
            auth_asym_id,
            identity,
        ) = record

        mappings.append(
            Mapping(
                entry_id=entry_id,
                entity_id=entity_id,
                pdb_start=pdb_start,
                pdb_end=pdb_end,
                unp_start=unp_start,
                unp_end=unp_end,
                struct_asym_id=struct_asym_id,
                auth_asym_id=auth_asym_id,
                identity=identity,
            )
        )

    return MappingResponse(accession=accession, mappings=mappings)


@app.get(
    "/mappings/oracle/{accession}",
)
def get_oracle_mappings(
    accession=Path(
        ...,
        title="UniProt accession",
        description="A UniProt accession",
        example="Q14676",
    )
):
    query = """
    SELECT
        entry_id,
        entity_id,
        pdb_start,
        pdb_end,
        unp_start,
        unp_end,
        struct_asym_id,
        auth_asym_id,
        identity
    FROM
        sifts_xref_segment
    WHERE
        accession = :accession
    ORDER BY
        pdb_start
    """
    mappings = []

    for record in oracle_driver.run_query(query, accession=accession):
        (
            entry_id,
            entity_id,
            pdb_start,
            pdb_end,
            unp_start,
            unp_end,
            struct_asym_id,
            auth_asym_id,
            identity,
        ) = record

        mappings.append(
            Mapping(
                entry_id=entry_id,
                entity_id=entity_id,
                pdb_start=pdb_start,
                pdb_end=pdb_end,
                unp_start=unp_start,
                unp_end=unp_end,
                struct_asym_id=struct_asym_id,
                auth_asym_id=auth_asym_id,
                identity=identity,
            )
        )

    return MappingResponse(accession=accession, mappings=mappings)
