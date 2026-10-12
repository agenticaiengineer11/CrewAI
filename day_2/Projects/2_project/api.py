
import logging
from time import perf_counter

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from flow import ProductResearchFlow

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="CrewAI Product Research API",
    version="1.0.0",
    description="Product research powered by a CrewAI Crew + Flow.",
)


class ProductResearchRequest(BaseModel):
    product_name: str = Field(min_length=1, max_length=200)
    target_market: str = Field(min_length=1, max_length=100)
    selling_price: float = Field(gt=0)
    supplier_cost: float = Field(ge=0)


class ProductResearchResponse(BaseModel):
    product_name: str
    product_score: int
    decision: str
    report: str
    execution_seconds: float


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post(
    "/research",
    response_model=ProductResearchResponse,
)
def research_product(request: ProductResearchRequest):
    started = perf_counter()

    logger.info(
        "Starting product research: %s",
        request.product_name,
    )

    try:
        flow = ProductResearchFlow()

        flow.kickoff(
            inputs={
                "product_name": request.product_name,
                "target_market": request.target_market,
                "selling_price": request.selling_price,
                "supplier_cost": request.supplier_cost,
            }
        )

        elapsed = round(perf_counter() - started, 2)

        logger.info(
            "Research completed: product=%s decision=%s duration=%ss",
            request.product_name,
            flow.state.decision,
            elapsed,
        )

        return ProductResearchResponse(
            product_name=flow.state.product_name,
            product_score=flow.state.product_score,
            decision=flow.state.decision,
            report=flow.state.report,
            execution_seconds=elapsed,
        )

    except Exception:
        logger.exception(
            "Product research failed for %s",
            request.product_name,
        )
        raise HTTPException(
            status_code=500,
            detail="Product research failed. Check the application logs.",
        ) from None
