from product_research.crew import ProductResearchCrew


def main():
    inputs = {
        "product_name": "Wireless Charging Station"
    }

    result = ProductResearchCrew().crew().kickoff(
        inputs=inputs
    )

    print("\n===== FINAL RESULT =====\n")
    print(result)


if __name__ == "__main__":
    main()