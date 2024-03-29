from pydantic import BaseModel, ConfigDict, StringConstraints
from typing_extensions import Annotated


class JobSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    position: Annotated[str, StringConstraints(max_length=128)]
    city: Annotated[str, StringConstraints(max_length=128)]
    area: Annotated[str, StringConstraints(max_length=128)]
    salary: Annotated[str, StringConstraints(max_length=128)]
    tag: Annotated[str, StringConstraints(max_length=128)]
    education: Annotated[str, StringConstraints(max_length=128)]
    experience: Annotated[str, StringConstraints(max_length=128)]
    company_name: Annotated[str, StringConstraints(max_length=128)]
    industry: Annotated[str, StringConstraints(max_length=128)]
    financing_stage: Annotated[str, StringConstraints(max_length=128)]
    company_size: Annotated[str, StringConstraints(max_length=128)]
    welfare: Annotated[str, StringConstraints(max_length=128)]
    category: Annotated[str, StringConstraints(max_length=128)]


class SimpleJobSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    position: Annotated[str, StringConstraints(max_length=128)]
    city: Annotated[str, StringConstraints(max_length=128)]
    area: Annotated[str, StringConstraints(max_length=128)]
    salary: Annotated[str, StringConstraints(max_length=128)]
    # tag: Annotated[str, StringConstraints(max_length=128)]
    education: Annotated[str, StringConstraints(max_length=128)]
    experience: Annotated[str, StringConstraints(max_length=128)]
    company_name: Annotated[str, StringConstraints(max_length=128)]
    # industry: Annotated[str, StringConstraints(max_length=128)]
    # financing_stage: Annotated[str, StringConstraints(max_length=128)]
    # company_size: Annotated[str, StringConstraints(max_length=128)]
    # welfare: Annotated[str, StringConstraints(max_length=128)]
    category: Annotated[str, StringConstraints(max_length=128)]


class GPT_Input(BaseModel):
    input: str


class GPT_Output(BaseModel):
    output: str
    type: str | None = None
    content: str | None = None
