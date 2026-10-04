from crewai.tools import tool


@tool("Calculate Profit Margin")
def calculate_profit_margin(
    selling_price: float,
    cost_price: float,
) -> str:
    """
    Calculate profit and profit margin for an e-commerce product.
    """

    if selling_price <= 0:
        return "Error: selling price must be greater than zero."

    if cost_price < 0:
        return "Error: cost price cannot be negative."

    profit = selling_price - cost_price
    margin = (profit / selling_price) * 100

    return (
        f"Profit: ${profit:.2f}\n"
        f"Profit Margin: {margin:.2f}%"
    )