from typing import List

from pydantic import BaseModel, Field


class HelloModel(BaseModel):
    message: str


class Mapping(BaseModel):
    entry_id: str = Field(
        ..., title="Entry ID", description="A PDB entry ID", example="1A0S"
    )
    entity_id: int = Field(
        ..., title="Entity ID", description="A PDB entity ID", example=1
    )
    pdb_start: int = Field(
        ..., title="PDB start", description="A PDB start residue", example=1
    )
    pdb_end: int = Field(
        ..., title="PDB end", description="A PDB end residue", example=100
    )
    unp_start: int = Field(
        ..., title="UniProt start", description="A UniProt start residue", example=1
    )
    unp_end: int = Field(
        ..., title="UniProt end", description="A UniProt end residue", example=100
    )
    struct_asym_id: str = Field(
        ..., title="PDB chain ID", description="A PDB chain ID", example="A"
    )
    auth_asym_id: str = Field(
        ...,
        title="PDB author chain ID",
        description="A PDB author chain ID",
        example="A",
    )
    identity: float = Field(
        ...,
        title="Identity",
        description="A sequence identity",
        example=0.9,
        ge=0,
        le=1,
    )


class MappingResponse(BaseModel):
    accession: str
    mappings: List[Mapping]
