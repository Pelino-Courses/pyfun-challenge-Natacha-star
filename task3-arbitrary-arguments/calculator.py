#Answers for question 3
def calculate(*args, **kwargs):
    """
    Perform calculations on given numbers based on specified operations.

    Args:
        *args: Positional arguments, expected to be numbers.
        **kwargs: Keyword arguments for operations:
            - add (bool): If True, sum the numbers.
            - multiply (bool): If True, multiply the numbers.

    Returns:
        dict: A dictionary with the results of requested operations.

    Raises:
        ValueError: If non-numeric args are provided or no operation is specified.
    """
    if not args:
        raise ValueError("At least one number must be provided.")

    numbers = []
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError(f"Invalid input: {arg} is not a number.")
        numbers.append(arg)

    if not kwargs:
        raise ValueError("At least one operation (add, multiply) must be specified.")

    results = {}

    if kwargs.get('add'):
        results['sum'] = sum(numbers)

    if kwargs.get('multiply'):
        product = 1
        for num in numbers:
            product *= num
        results['product'] = product

    if not results:
        raise ValueError("No valid operations requested (use add=True, multiply=True).")

    return results


if __name__ == "__main__":
    print("Welcome to the Command-Line Calculator!")

    # Get numbers from user
    numbers_input = input("Enter numbers separated by spaces: ")
    try:
        numbers = [float(n) for n in numbers_input.strip().split()]
    except ValueError:
        print("Error: Please enter only numbers.")
        exit()

    # Get operations from user
    add_input = input("Do you want to add the numbers? (yes/no): ").strip().lower()
    multiply_input = input("Do you want to multiply the numbers? (yes/no): ").strip().lower()

    add = add_input == 'yes'
    multiply = multiply_input == 'yes'

    try:
        results = calculate(*numbers, add=add, multiply=multiply)
        print("\nCalculation Results:")
        for key, value in results.items():
            print(f"{key.capitalize()}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
