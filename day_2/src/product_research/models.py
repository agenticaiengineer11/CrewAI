from pydantic import BaseModel, Field


class ProductDecision(BaseModel):
    product_name: str = Field(
        description="Name of the product being evaluated."
    )

    competition_level: str = Field(
        description="Competition level: low, medium, or high."
    )

    market_potential: float = Field(
        ge=0,
        le=10,
        description="Market potential score from 0 to 10."
    )

    recommendation: str = Field(
        description="Final recommendation for the product."
    )

    key_risks: list[str] = Field(
        description="List of important product risks."
    )