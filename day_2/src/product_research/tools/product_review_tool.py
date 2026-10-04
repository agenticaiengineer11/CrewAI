from crewai.tools import tool

@tool("Calculate product review sentiment")

def calculate_product_review_sentiment(review_text: str) -> str:
    """
    Analyze the sentiment of a product review and return whether it is positive, negative, or neutral.
    """

    if not review_text:
        return "Error: review text cannot be empty."

    # Simple sentiment analysis based on keywords
    positive_keywords = ["good", "great", "excellent", "amazing", "love", "fantastic"]
    negative_keywords = ["bad", "poor", "terrible", "hate", "awful", "disappointing"]

    review_lower = review_text.lower()
    positive_count = sum(1 for word in positive_keywords if word in review_lower)
    negative_count = sum(1 for word in negative_keywords if word in review_lower)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"