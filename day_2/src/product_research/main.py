from product_research.crew import create_crew


def main():
    product_name = "Wireless Charging Station"

    crew = create_crew()

    result = crew.kickoff(
        inputs={
            "product_name": product_name
        }
    )

    print("\n===== FINAL RESULT =====\n")
    print(result)


if __name__ == "__main__":
    main()