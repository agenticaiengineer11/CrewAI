from crewai.tools import tool

@tool("Calculate Product Price")
def calculate_product_price(
    cost_price: float,
    desired_profit_margin: float
) -> str:
    """
    Calculate the selling price for a product based on cost price and desired profit margin.
    """

    if cost_price < 0:
        return "Error: cost price cannot be negative."

    if desired_profit_margin < 0 or desired_profit_margin > 100:
        return "Error: desired profit margin must be between 0 and 100."

    selling_price = cost_price / (1 - desired_profit_margin / 100)

    return f"Recommended Selling Price: ${selling_price:.2f}"