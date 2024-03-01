def average_calculator():
    num_list = input("Enter a list of numbers separated by spaces: ").split()

    try:
        num_list = [float(num) for num in num_list]
        average = sum(num_list) / len(num_list)
        print(f"The average of the numbers is: {average}")
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")


average_calculator()
