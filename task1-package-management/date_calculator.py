import datetime

def date_difference(day1, day2):
    """
    The program calculates the difference between two entered dates.
    
    Args:
        day1 (str): First date in 'YYYY-MM-DD' format.
        day2 (str): Second date in 'YYYY-MM-DD' format.
    
    Returns:
        int: Difference in days, or None if invalid input.
    """
    try:
        date1 = datetime.datetime.strptime(day1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(day2, "%Y-%m-%d").date()
        difference = abs((date1 - date2).days)
        return difference

    except ValueError as e:
        print(f"Error: {e}")
        print("Please provide dates in the format YYYY-MM-DD.")
        return None

if __name__ == "__main__":
    print("Welcome to Days Difference Calculator!")
    day1 = input("Enter the first date (YYYY-MM-DD): ")
    day2 = input("Enter the second date (YYYY-MM-DD): ")
    days = date_difference(day1, day2)

    if days is not None:
        print("The difference is:", days)
    else:
        print("Invalid input.")

print("go to input step")

