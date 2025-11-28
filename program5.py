def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest.

    Args:
        principal (float): Principal amount
        rate (float): Rate of interest
        time (float): Time period

    Returns:
        float: Simple Interest
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def main():
    # Get user input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period (in years): "))

    # Calculate Simple Interest
    interest = calculate_simple_interest(principal, rate, time)

    # Display the result
    print(f"Simple Interest: {interest}")

if _name_ == "_main_":
    main()
