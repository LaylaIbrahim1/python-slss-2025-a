def AVARAGE(num_one, num_two, num_three):
    """
    Calculates the avarage of three numbers.

    Parameters:
    num_one (float): The first number.
    num_two (float): The second number.
    num_three (float): The third number

    Returns:
        Float: The avarage of the three numbers.
    """
    total = num_one + num_two + num_three
    avarage = total/3
    return avarage


result = AVARAGE(10, 20, 30)
print(result)
