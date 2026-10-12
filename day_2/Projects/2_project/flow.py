
import re

from pydantic import BaseModel, Field
from crewai.flow.flow import Flow, start, listen, router

from crew import ProductResearchCrew


class ProductResearchState(BaseModel):
    product_name: str = ""
    target_market: str = ""
    selling_price: float = 0.0
    supplier_cost: float = 0.0

    report: str = ""
    product_score: int = 0
    decision: str = "pending"


class ProductResearchFlow(Flow[ProductResearchState]):

    @start()
    def validate_input(self):
        """Validate the input before starting the Crew."""

        if not self.state.product_name.strip():
            raise ValueError("product_name is required")

        if not self.state.target_market.strip():
            raise ValueError("target_market is required")

        if self.state.selling_price <= 0:
            raise ValueError("selling_price must be greater than zero")

        if self.state.supplier_cost < 0:
            raise ValueError("supplier_cost cannot be negative")

        print(f"\nStarting research: {self.state.product_name}")

    @listen(validate_input)
    def run_research_crew(self):
        """Execute the existing three-agent Crew."""

        result = ProductResearchCrew().crew().kickoff(
            inputs={
                "product_name": self.state.product_name,
                "target_market": self.state.target_market,
                "selling_price": self.state.selling_price,
                "supplier_cost": self.state.supplier_cost,
            }
        )

        self.state.report = str(result)
        print("\nResearch Crew completed.")

    @router(run_research_crew)
    def route_by_score(self):
        """Extract the final score and choose a route."""

        match = re.search(
            r"FINAL SCORE:\s*(\d{1,3})\s*/\s*100",
            self.state.report,
            re.IGNORECASE,
        )

        if not match:
            self.state.decision = "manual_review"
            return "manual_review"

        score = int(match.group(1))

        if not 0 <= score <= 100:
            self.state.decision = "manual_review"
            return "manual_review"

        self.state.product_score = score

        if score >= 70:
            self.state.decision = "promising"
            return "promising"

        self.state.decision = "needs_validation"
        return "needs_validation"

    @listen("promising")
    def handle_promising_product(self):
        """Handle products scoring 70 or higher."""

        print(
            f"\nPROMISING PRODUCT: "
            f"{self.state.product_name} "
            f"({self.state.product_score}/100)"
        )

    @listen("needs_validation")
    def handle_validation_required(self):
        """Handle products scoring below 70."""

        print(
            f"\nFURTHER VALIDATION REQUIRED: "
            f"{self.state.product_name} "
            f"({self.state.product_score}/100)"
        )

    @listen("manual_review")
    def handle_manual_review(self):
        """Avoid making an automated decision without a valid score."""

        print(
            "\nMANUAL REVIEW REQUIRED: "
            "The report did not contain a valid FINAL SCORE."
        )


if __name__ == "__main__":
    inputs = {
        "product_name": "Portable Blender",
        "target_market": "United States",
        "selling_price": 39.99,
        "supplier_cost": 15.00,
    }

    flow = ProductResearchFlow()
    result = flow.kickoff(inputs=inputs)

    print("\n" + "=" * 55)
    print("HYBRID CREW + FLOW RESULTS")
    print("=" * 55)
    print("Product:", flow.state.product_name)
    print("Score:", flow.state.product_score, "/ 100")
    print("Decision:", flow.state.decision)
    print("\nFinal report:\n")
    print(flow.state.report)
